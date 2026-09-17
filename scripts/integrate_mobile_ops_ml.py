"""
Integrate mobile ops ground-truth into ML (BTC/US30) + neural vision labels.

1) Refresh market cache to cover ops range
2) Match OCR trades → M5 bars → WIN/LOSS labels
3) Train baseline vs enriched (ops oversampled) and compare metrics
4) Export vision labels for neuronal training

Usage:
  python -m scripts.integrate_mobile_ops_ml
  python -m scripts.integrate_mobile_ops_ml --quick
  python -m scripts.integrate_mobile_ops_ml --skip-us30
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)

from app.config import DATA_DIR, MODELS_DIR, OPS_MOBILE_DATA_DIR, PROJECT_ROOT, TRAINING_NEURAL_DIR
from app.models.ops_mobile_ground_truth import (
    OPS_VERSION,
    build_ops_feature_rows,
    load_ops_trades,
    match_ops_to_m5,
    match_summary,
    write_vision_labels,
)

OUT_DIR = OPS_MOBILE_DATA_DIR / OPS_VERSION
REPORT_PATH = OUT_DIR / "ml_ops_integration_report.md"


def _f1_safe(y_true, y_pred) -> float:
    return float(f1_score(y_true, y_pred, zero_division=0))


def train_eval(X, y, algorithm: str, sample_weight=None):
    from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split

    weights = sample_weight if sample_weight is not None else np.ones(len(y))
    X_train, X_test, y_train, y_test, w_train, _w_test = train_test_split(
        X,
        y,
        weights,
        test_size=0.25,
        random_state=42,
        stratify=y if len(np.unique(y)) > 1 else None,
    )
    if algorithm == "rf":
        clf = RandomForestClassifier(
            n_estimators=200, max_depth=8, random_state=42, class_weight="balanced"
        )
    elif algorithm == "lr":
        clf = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
    else:
        clf = GradientBoostingClassifier(
            n_estimators=150, max_depth=4, learning_rate=0.08, random_state=42
        )

    clf.fit(X_train, y_train, sample_weight=w_train)

    y_pred = clf.predict(X_test)
    metrics = {
        "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
        "precision": round(float(precision_score(y_test, y_pred, zero_division=0)), 4),
        "recall": round(float(recall_score(y_test, y_pred, zero_division=0)), 4),
        "f1": round(_f1_safe(y_test, y_pred), 4),
        "test_winrate_baseline": round(float(y_test.mean()), 4),
        "train_samples": int(len(y_train)),
        "test_samples": int(len(y_test)),
    }
    return clf, metrics


def run_btc(args: argparse.Namespace) -> dict:
    from app.controllers import train_btc_signals as btc
    from app.models.btc_ml_signals import (
        FEATURES_PATH,
        MODEL_PATH,
        _default_feature_names,
        extract_features,
        feature_config,
        features_to_vector,
    )
    from app.services.btc_high_analysis import analyze_crt, detect_rsi_divergence, dmi_proxy

    print("\n=== BTC: load/fetch market data ===")
    m5, h1 = btc.load_or_fetch_data("BTCUSDT", args.days, force=args.force_download)
    print(f"M5={len(m5)} H1={len(h1)}")

    # Quick: train synthetic on a recent window (full m5 still used for ops match)
    m5_train, h1_train = m5, h1
    if args.quick and m5:
        from datetime import timedelta

        cutoff = m5[-1]["open_time"] - timedelta(days=min(60, max(30, args.days)))
        m5_train = [c for c in m5 if c["open_time"] >= cutoff]
        h1_train = [c for c in h1 if c["open_time"] >= cutoff - timedelta(days=2)]
        print(f"Quick baseline window: M5={len(m5_train)} H1={len(h1_train)} from {cutoff}")

    print("Building baseline synthetic dataset...")
    X0, y0, feature_names, meta0 = btc.build_training_dataset(
        m5_train, h1_train, horizon=args.horizon, stride=args.stride, ny_only=args.ny_only
    )
    print(f"Baseline samples: {len(y0)} wr={y0.mean()*100:.1f}%")

    ops = load_ops_trades(symbols={"BTCUSDT"})
    print(f"Ops BTC candidates: {len(ops)}")
    matched = match_ops_to_m5(
        ops,
        m5,
        horizon=args.horizon,
        fallback_label_fn=btc.label_outcome,
        max_price_err_pct=args.max_price_err_pct,
        window_hours=args.window_hours,
    )
    print(f"Matched BTC ops: {len(matched)} | {match_summary(matched)}")

    X_ops, y_ops, meta_ops = build_ops_feature_rows(
        matched,
        m5,
        h1,
        build_snapshot_fn=btc.build_snapshot_at_index,
        analyze_crt_fn=analyze_crt,
        detect_div_fn=detect_rsi_divergence,
        dmi_fn=dmi_proxy,
        extract_features_fn=extract_features,
        features_to_vector_fn=features_to_vector,
        feature_names=feature_names,
        h1_up_to_fn=btc.h1_up_to,
    )
    print(f"Ops feature rows: {len(y_ops)}")

    # Baseline train
    clf0, m0 = train_eval(X0, y0, args.algorithm)
    # Enriched: concat + weight ops
    if len(y_ops):
        X1 = np.vstack([X0, X_ops])
        y1 = np.concatenate([y0, y_ops])
        w = np.concatenate(
            [np.ones(len(y0)), np.full(len(y_ops), float(args.ops_weight))]
        )
        meta1 = pd.concat(
            [meta0.assign(source="synthetic"), meta_ops], ignore_index=True
        )
    else:
        X1, y1, w, meta1 = X0, y0, np.ones(len(y0)), meta0.assign(source="synthetic")

    clf1, m1 = train_eval(X1, y1, args.algorithm, sample_weight=w)

    # Backup previous model then save enriched
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    if MODEL_PATH.is_file():
        bak = MODEL_PATH.with_suffix(".joblib.bak_pre_ops")
        shutil.copy2(MODEL_PATH, bak)
    joblib.dump(clf1, MODEL_PATH)
    cfg = feature_config()
    cfg.update(
        {
            "feature_names": feature_names,
            "trained_at": datetime.now(timezone.utc).isoformat(),
            "days": args.days,
            "horizon_bars": args.horizon,
            "algorithm": args.algorithm,
            "samples": int(len(y1)),
            "ops_matched": int(len(matched)),
            "ops_feature_rows": int(len(y_ops)),
            "ops_weight": args.ops_weight,
            "dataset_winrate": round(float(y1.mean()), 4),
            "metrics_before": m0,
            "metrics_after": m1,
            "ops_dataset_version": OPS_VERSION,
        }
    )
    FEATURES_PATH.write_text(json.dumps(cfg, indent=2), encoding="utf-8")

    # Persist match table + vision labels
    match_df = pd.DataFrame([m.__dict__ for m in matched])
    match_df.to_csv(OUT_DIR / "btc_ops_matched.csv", index=False)
    labels_path = write_vision_labels(matched, OUT_DIR / "mobile_vision_labels.csv")

    return {
        "symbol": "BTCUSDT",
        "baseline_samples": int(len(y0)),
        "ops_candidates": int(len(ops)),
        "ops_matched": int(len(matched)),
        "ops_feature_rows": int(len(y_ops)),
        "match_summary": match_summary(matched),
        "metrics_before": m0,
        "metrics_after": m1,
        "labels_path": str(labels_path),
        "model_path": str(MODEL_PATH),
    }


def run_us30(args: argparse.Namespace) -> dict:
    from app.controllers import train_us30_signals as us30
    from app.models.ml_signals import (
        extract_features,
        feature_config,
        features_to_vector,
        model_paths,
    )
    from app.services.btc_high_analysis import analyze_crt, detect_rsi_divergence, dmi_proxy

    print("\n=== US30: load/fetch market data ===")
    m5, h1 = us30.load_or_fetch_data(args.days, force=args.force_download)
    print(f"M5={len(m5)} H1={len(h1)}")

    X0, y0, feature_names, meta0 = us30.build_training_dataset(
        m5, h1, horizon=args.horizon, stride=args.stride, ny_only=args.ny_only
    )
    print(f"Baseline samples: {len(y0)} wr={y0.mean()*100:.1f}%")

    ops = load_ops_trades(symbols={"US30"})
    matched = match_ops_to_m5(
        ops,
        m5,
        horizon=args.horizon,
        fallback_label_fn=us30.label_outcome,
        max_price_err_pct=min(args.max_price_err_pct, 0.8),
        window_hours=args.window_hours,
    )
    print(f"Matched US30 ops: {len(matched)} | {match_summary(matched)}")

    X_ops, y_ops, meta_ops = build_ops_feature_rows(
        matched,
        m5,
        h1,
        build_snapshot_fn=us30.build_snapshot_at_index,
        analyze_crt_fn=analyze_crt,
        detect_div_fn=detect_rsi_divergence,
        dmi_fn=dmi_proxy,
        extract_features_fn=extract_features,
        features_to_vector_fn=features_to_vector,
        feature_names=feature_names,
        h1_up_to_fn=us30.h1_up_to,
    )

    clf0, m0 = train_eval(X0, y0, args.algorithm)
    if len(y_ops):
        X1 = np.vstack([X0, X_ops])
        y1 = np.concatenate([y0, y_ops])
        w = np.concatenate(
            [np.ones(len(y0)), np.full(len(y_ops), float(args.ops_weight))]
        )
    else:
        X1, y1, w = X0, y0, np.ones(len(y0))
    clf1, m1 = train_eval(X1, y1, args.algorithm, sample_weight=w)

    model_path, features_path = model_paths("us30")
    if model_path.is_file():
        shutil.copy2(model_path, model_path.with_suffix(".joblib.bak_pre_ops"))
    joblib.dump(clf1, model_path)
    cfg = feature_config("us30")
    cfg.update(
        {
            "feature_names": feature_names,
            "trained_at": datetime.now(timezone.utc).isoformat(),
            "samples": int(len(y1)),
            "ops_matched": int(len(matched)),
            "ops_weight": args.ops_weight,
            "metrics_before": m0,
            "metrics_after": m1,
            "ops_dataset_version": OPS_VERSION,
        }
    )
    features_path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
    pd.DataFrame([m.__dict__ for m in matched]).to_csv(
        OUT_DIR / "us30_ops_matched.csv", index=False
    )
    # append US30 labels into vision csv if exists
    vis = OUT_DIR / "mobile_vision_labels.csv"
    write_vision_labels(matched, OUT_DIR / "us30_mobile_vision_labels.csv")
    if vis.is_file() and matched:
        a = pd.read_csv(vis)
        b = pd.read_csv(OUT_DIR / "us30_mobile_vision_labels.csv")
        pd.concat([a, b], ignore_index=True).drop_duplicates(subset=["filename"]).to_csv(
            vis, index=False
        )

    return {
        "symbol": "US30",
        "baseline_samples": int(len(y0)),
        "ops_candidates": int(len(ops)),
        "ops_matched": int(len(matched)),
        "ops_feature_rows": int(len(y_ops)),
        "match_summary": match_summary(matched),
        "metrics_before": m0,
        "metrics_after": m1,
        "model_path": str(model_path),
    }


def update_neural_labels_and_train(args: argparse.Namespace, btc_result: dict) -> dict:
    """Copy vision labels into neural data dir and train a simple mobile vision model."""
    labels_src = OUT_DIR / "mobile_vision_labels.csv"
    neural_data = TRAINING_NEURAL_DIR / "data"
    neural_data.mkdir(parents=True, exist_ok=True)
    labels_dst = neural_data / "mobile_ops_labels.csv"
    if labels_src.is_file():
        shutil.copy2(labels_src, labels_dst)

    note = neural_data / "MOBILE_OPS_LABELS.md"
    note.write_text(
        "\n".join(
            [
                "# Mobile ops labels",
                "",
                f"Source: `{labels_src}`",
                f"Copy: `{labels_dst}`",
                "",
                "Generated from OCR trades matched to M5 outcomes (WIN/LOSS).",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result: dict = {"labels_dst": str(labels_dst), "trained": False, "metrics": None}
    if args.skip_neural:
        return result
    if not labels_dst.is_file():
        result["note"] = "No vision labels file"
        return result
    try:
        result.update(_train_mobile_simple(labels_dst, args.quick))
    except Exception as exc:  # noqa: BLE001
        result["error"] = str(exc)
    return result


def _train_mobile_simple(labels_csv: Path, quick: bool) -> dict:
    """Minimal sklearn vision trainer on mobile ops only."""
    from PIL import Image
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    from app.config import MOBILE_OPS_DIR

    lab = pd.read_csv(labels_csv)
    X, y, kept = [], [], []
    for _, r in lab.iterrows():
        p = MOBILE_OPS_DIR / str(r["filename"])
        if not p.is_file():
            continue
        label = str(r["label"]).upper()
        if label not in ("WIN", "LOSS"):
            continue
        img = Image.open(p).convert("RGB").resize((64, 64))
        arr = np.asarray(img, dtype=np.float32).reshape(-1) / 255.0
        # simple color histogram extras
        hist = np.histogram(arr, bins=16, range=(0, 1))[0].astype(np.float32)
        hist = hist / (hist.sum() + 1e-6)
        X.append(np.concatenate([arr[::16], hist]))  # subsample pixels + hist
        y.append(0 if label == "WIN" else 1)
        kept.append(p.name)
        if quick and len(X) >= 40:
            break

    if len(X) < 8:
        return {"trained": False, "note": f"mobile only n={len(X)}"}

    X_arr = np.vstack(X)
    y_arr = np.array(y)
    Xtr, Xte, ytr, yte = train_test_split(
        X_arr, y_arr, test_size=0.25, random_state=42,
        stratify=y_arr if len(np.unique(y_arr)) > 1 else None,
    )
    pipe = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )
    pipe.fit(Xtr, ytr)
    pred = pipe.predict(Xte)
    metrics = {
        "accuracy": round(float(accuracy_score(yte, pred)), 4),
        "precision": round(float(precision_score(yte, pred, zero_division=0)), 4),
        "recall": round(float(recall_score(yte, pred, zero_division=0)), 4),
        "f1": round(_f1_safe(yte, pred), 4),
        "n": len(y_arr),
        "val_n": len(yte),
    }
    out_model = TRAINING_NEURAL_DIR / "models" / "mobile_ops_vision_simple.joblib"
    out_model.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"pipeline": pipe, "files": kept, "metrics": metrics}, out_model)
    return {"trained": True, "metrics": metrics, "model": str(out_model), "mode": "mobile_simple"}


def write_report(results: list[dict], neural: dict, elapsed: float) -> None:
    lines = [
        f"# ML + Neural integration — {OPS_VERSION}",
        "",
        f"> Generado: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC",
        f"> Elapsed: {elapsed:.1f}s",
        "",
        "Operaciones reales del celular enriquecen el dataset sintético (peso `ops_weight`) "
        "y generan etiquetas WIN/LOSS para visión.",
        "",
    ]
    for r in results:
        mb, ma = r["metrics_before"], r["metrics_after"]
        lines += [
            f"## {r['symbol']}",
            "",
            f"| Métrica | Before | After | Δ |",
            f"|---------|--------|-------|---|",
            f"| Accuracy | {mb['accuracy']} | {ma['accuracy']} | {ma['accuracy']-mb['accuracy']:+.4f} |",
            f"| Precision | {mb['precision']} | {ma['precision']} | {ma['precision']-mb['precision']:+.4f} |",
            f"| Recall | {mb['recall']} | {ma['recall']} | {ma['recall']-mb['recall']:+.4f} |",
            f"| F1 | {mb['f1']} | {ma['f1']} | {ma['f1']-mb['f1']:+.4f} |",
            "",
            f"- Baseline samples: **{r['baseline_samples']}**",
            f"- Ops candidates / matched / feature rows: "
            f"**{r['ops_candidates']}** / **{r['ops_matched']}** / **{r['ops_feature_rows']}**",
            f"- Match summary: `{json.dumps(r['match_summary'])}`",
            f"- Model: `{r.get('model_path')}`",
            "",
        ]
    lines += [
        "## Neural / visión",
        "",
        f"```json",
        json.dumps(neural, indent=2, default=str),
        "```",
        "",
        "## Archivos",
        "",
        f"- `{OUT_DIR / 'btc_ops_matched.csv'}`",
        f"- `{OUT_DIR / 'us30_ops_matched.csv'}`",
        f"- `{OUT_DIR / 'mobile_vision_labels.csv'}`",
        f"- `{REPORT_PATH}`",
        "",
        "## Notas",
        "",
        "- Modelos previos respaldados como `*.joblib.bak_pre_ops`.",
        "- No se inventaron trades: solo OCR + velas históricas.",
        "- US30 M5 vía yfinance suele cubrir ~60 días → pocas matches esperables.",
        "",
    ]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Integrate mobile ops into ML + neural")
    parser.add_argument("--days", type=int, default=220, help="History days for BTC fetch")
    parser.add_argument("--horizon", type=int, default=48)
    parser.add_argument("--stride", type=int, default=3)
    parser.add_argument("--algorithm", choices=("gb", "rf", "lr"), default="gb")
    parser.add_argument(
        "--ops-weight",
        type=float,
        default=None,
        help="Sample weight for real ops (default 8; 5 with --quick)",
    )
    parser.add_argument("--force-download", action="store_true", default=True)
    parser.add_argument("--no-force-download", action="store_true")
    parser.add_argument("--ny-only", action="store_true")
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--skip-us30", action="store_true")
    parser.add_argument("--skip-neural", action="store_true")
    parser.add_argument(
        "--max-price-err-pct",
        type=float,
        default=0.9,
        help="Max %% price error when matching OCR entry to M5 close",
    )
    parser.add_argument(
        "--window-hours",
        type=float,
        default=4.0,
        help="Time window (hours) around capture for M5 match",
    )
    args = parser.parse_args()

    if args.no_force_download:
        args.force_download = False
    if args.quick:
        args.days = 90
        args.stride = max(args.stride, 12)
    # Default weight: lighter under --quick unless user passed --ops-weight
    if args.ops_weight is None:
        args.ops_weight = 5.0 if args.quick else 8.0

    t0 = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    try:
        results.append(run_btc(args))
        if not args.skip_us30:
            results.append(run_us30(args))
        neural = update_neural_labels_and_train(args, results[0])
        write_report(results, neural, time.time() - t0)
        print("\n" + "=" * 56)
        print(f"Report: {REPORT_PATH}")
        for r in results:
            print(
                f"{r['symbol']}: matched={r['ops_matched']} "
                f"acc {r['metrics_before']['accuracy']} -> {r['metrics_after']['accuracy']}"
            )
        print("=" * 56)
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
