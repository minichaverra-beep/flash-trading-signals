"""
Train ML model on historical US30 M5/H1 data (yfinance) for E1 signal quality.

Usage:
  python -m app.controllers.train_us30_signals
  python -m app.controllers.train_us30_signals --quick
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score
from sklearn.model_selection import train_test_split

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
REPORT_PATH = DATA_DIR / "us30_ml_training_report.md"

from app.models.us30_data import DEFAULT_TICKERS, fetch_us30_klines as fetch_yfinance_klines  # noqa: E402
from app.services.btc_high_analysis import analyze_crt, detect_rsi_divergence, dmi_proxy  # noqa: E402
from app.models.market_analysis_core import (  # noqa: E402
    h1_bias,
    nearest_zone,
    pdh_pdl,
    rsi,
    session_flags,
    suggest_setup,
    swing_levels,
    two_candle_confirm,
)
from app.models.ml_signals import (  # noqa: E402
    SYMBOL_CONFIG,
    extract_features,
    feature_config,
    features_to_vector,
    model_paths,
    sl_pct_at_price,
)

M5_CACHE = DATA_DIR / "us30_m5.parquet"
H1_CACHE = DATA_DIR / "us30_h1.parquet"
ML_SYMBOL = "us30"
PRICE_DECIMALS = 1
SL_USD_REF = SYMBOL_CONFIG[ML_SYMBOL]["sl_usd_ref"]


def candles_to_df(candles: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(candles)


def df_to_candles(df: pd.DataFrame) -> list[dict]:
    return df.to_dict("records")


def load_or_fetch_data(days: int, force: bool = False) -> tuple[list[dict], list[dict]]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not force and M5_CACHE.is_file() and H1_CACHE.is_file():
        m5_df = pd.read_parquet(M5_CACHE)
        h1_df = pd.read_parquet(H1_CACHE)
        m5 = df_to_candles(m5_df)
        h1 = df_to_candles(h1_df)
        if m5 and h1:
            print(f"Loaded cache: M5={len(m5)} H1={len(h1)} bars")
            return m5, h1

    print(f"Fetching US30 from yfinance (target ~{days}d)...")
    t0 = time.time()
    m5_bars = min(days * 24 * 12, 5000)
    h1_bars = min(days * 24, 2000)
    m5, h1, meta = fetch_yfinance_klines(
        tickers=DEFAULT_TICKERS,
        m5_bars=m5_bars,
        h1_bars=h1_bars,
    )
    print(f"Downloaded M5={len(m5)} H1={len(h1)} in {time.time() - t0:.1f}s — {meta}")
    candles_to_df(m5).to_parquet(M5_CACHE, index=False)
    candles_to_df(h1).to_parquet(H1_CACHE, index=False)
    return m5, h1


def h1_up_to(h1: list[dict], ts: datetime) -> list[dict]:
    return [c for c in h1 if c["open_time"] <= ts]


def label_outcome(
    direction: str,
    entry: float,
    setup_sl: float | None,
    future: list[dict],
    horizon: int,
    rr: float = 2.0,
) -> int | None:
    sl_pct = sl_pct_at_price(ML_SYMBOL, entry)
    if direction == "LONG":
        sl_fixed = entry * (1.0 - sl_pct)
        sl = setup_sl if setup_sl is not None and setup_sl < entry else sl_fixed
        risk = entry - sl
        if risk <= 0:
            return None
        tp = entry + rr * risk
        for bar in future[:horizon]:
            if bar["low"] <= sl and bar["high"] >= tp:
                return 0
            if bar["low"] <= sl:
                return 0
            if bar["high"] >= tp:
                return 1
    elif direction == "SHORT":
        sl_fixed = entry * (1.0 + sl_pct)
        sl = setup_sl if setup_sl is not None and setup_sl > entry else sl_fixed
        risk = sl - entry
        if risk <= 0:
            return None
        tp = entry - rr * risk
        for bar in future[:horizon]:
            if bar["high"] >= sl and bar["low"] <= tp:
                return 0
            if bar["high"] >= sl:
                return 0
            if bar["low"] <= tp:
                return 1
    else:
        return None
    return None


def build_snapshot_at_index(m5: list[dict], h1: list[dict], idx: int, min_m5: int = 120) -> dict | None:
    if idx < min_m5:
        return None
    window = m5[: idx + 1]
    ts = window[-1]["open_time"]
    h1_slice = h1_up_to(h1, ts)
    if len(h1_slice) < 55:
        return None

    price = window[-1]["close"]
    closes_m5 = [c["close"] for c in window]
    closes_h1 = [c["close"] for c in h1_slice]
    rsi_m5 = rsi(closes_m5)
    rsi_h1 = rsi(closes_h1)
    bias = h1_bias(h1_slice)
    pdh, pdl = pdh_pdl(h1_slice, ts)
    sh, slv = swing_levels(window)
    zone = nearest_zone(price, sh, slv)
    session = session_flags(ts)
    confirm_long = two_candle_confirm(window, "LONG")
    confirm_short = two_candle_confirm(window, "SHORT")
    setup = suggest_setup(
        price, bias, zone, rsi_m5, confirm_long, confirm_short,
        session["in_ny_window"], pdh, pdl, price_decimals=PRICE_DECIMALS,
    )
    if setup["direction"] == "NONE":
        return None

    return {
        "generated": ts.strftime("%Y-%m-%d %H:%M"),
        "symbol": "US30",
        "price": price,
        "session": session,
        "bias_h1": bias,
        "rsi_m5": rsi_m5,
        "rsi_h1": rsi_h1,
        "pdh": pdh,
        "pdl": pdl,
        "swing_highs": sh,
        "swing_lows": slv,
        "zone": zone,
        "confirm_long": confirm_long,
        "confirm_short": confirm_short,
        "setup": setup,
    }


def build_training_dataset(
    m5: list[dict],
    h1: list[dict],
    horizon: int = 48,
    stride: int = 1,
    ny_only: bool = False,
) -> tuple[np.ndarray, np.ndarray, list[str], pd.DataFrame]:
    from app.models.ml_signals import feature_config as fc

    feature_names = fc(ML_SYMBOL)["feature_names"]
    rows_x, rows_y, meta = [], [], []

    total = len(m5) - horizon - 1
    for idx in range(120, total, stride):
        data = build_snapshot_at_index(m5, h1, idx)
        if data is None:
            continue
        if ny_only and not data["session"]["in_ny_window"]:
            continue

        ts = m5[idx]["open_time"]
        h1_at = h1_up_to(h1, ts)
        m5_at = m5[: idx + 1]
        crt = analyze_crt(data["price"], data.get("pdh"), data.get("pdl"), h1_at, m5_at)
        div = detect_rsi_divergence(m5_at)
        dmi = dmi_proxy([c["close"] for c in m5_at])

        label = label_outcome(
            data["setup"]["direction"],
            data["price"],
            data["setup"].get("sl"),
            m5[idx + 1 : idx + 1 + horizon],
            horizon,
        )
        if label is None:
            continue

        feats = extract_features(data, crt, div, dmi)
        rows_x.append(features_to_vector(feats, feature_names))
        rows_y.append(label)
        meta.append({
            "time": ts.isoformat(),
            "direction": data["setup"]["direction"],
            "price": data["price"],
            "label": label,
            "in_ny": data["session"]["in_ny_window"],
        })

    if not rows_x:
        raise RuntimeError("No training samples — check yfinance data range")

    return np.vstack(rows_x), np.array(rows_y, dtype=np.int32), feature_names, pd.DataFrame(meta)


def train_model(X: np.ndarray, y: np.ndarray, algorithm: str = "gb"):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42,
        stratify=y if len(np.unique(y)) > 1 else None,
    )
    if algorithm == "rf":
        clf = RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42, class_weight="balanced")
    elif algorithm == "lr":
        clf = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
    else:
        clf = GradientBoostingClassifier(n_estimators=150, max_depth=4, learning_rate=0.08, random_state=42)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)[:, 1]
    metrics = {
        "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
        "precision": round(float(precision_score(y_test, y_pred, zero_division=0)), 4),
        "recall": round(float(recall_score(y_test, y_pred, zero_division=0)), 4),
        "test_winrate_baseline": round(float(y_test.mean()), 4),
        "train_samples": int(len(y_train)),
        "test_samples": int(len(y_test)),
        "report": classification_report(y_test, y_pred, zero_division=0),
    }
    return clf, metrics


def write_report(metrics: dict, meta_df: pd.DataFrame, days: int, horizon: int, elapsed: float) -> None:
    lines = [
        "# ML Training Report — US30 M5 E1 Signals",
        "",
        f"> Generado: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC",
        "",
        f"| Días históricos (objetivo) | {days} |",
        f"| Horizonte label (velas) | {horizon} |",
        f"| Muestras | {len(meta_df)} |",
        f"| Win rate dataset | {meta_df['label'].mean()*100:.1f}% |",
        f"| SL referencia | ${SL_USD_REF} (~9 pts $1/pt · ~90 pts micro) |",
        "",
        f"- Accuracy: {metrics['accuracy']}",
        f"- Precision: {metrics['precision']}",
        f"- Recall: {metrics['recall']}",
        "",
        "**Nota:** yfinance limita 5m/15m a ~60 días; el dataset real puede ser menor que `--days`.",
        "",
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Train US30 M5 E1 signal ML model")
    parser.add_argument("--days", type=int, default=365)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--horizon", type=int, default=48)
    parser.add_argument("--stride", type=int, default=3)
    parser.add_argument("--algorithm", choices=("gb", "rf", "lr"), default="gb")
    parser.add_argument("--force-download", action="store_true")
    parser.add_argument("--ny-only", action="store_true")
    args = parser.parse_args()

    if args.quick:
        args.days = 30
        args.stride = 12

    model_path, features_path = model_paths(ML_SYMBOL)
    t0 = time.time()
    try:
        m5, h1 = load_or_fetch_data(args.days, force=args.force_download)
        print("Building training dataset...")
        X, y, feature_names, meta_df = build_training_dataset(
            m5, h1, horizon=args.horizon, stride=args.stride, ny_only=args.ny_only,
        )
        print(f"Samples: {len(y)} | Win rate: {y.mean()*100:.1f}%")
        model, metrics = train_model(X, y, algorithm=args.algorithm)

        MODELS_DIR.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, model_path)

        cfg = feature_config(ML_SYMBOL)
        cfg.update({
            "feature_names": feature_names,
            "trained_at": datetime.now(timezone.utc).isoformat(),
            "days": args.days,
            "horizon_bars": args.horizon,
            "algorithm": args.algorithm,
            "samples": len(y),
            "dataset_winrate": round(float(y.mean()), 4),
            "metrics": {k: v for k, v in metrics.items() if k != "report"},
        })
        features_path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
        write_report(metrics, meta_df, args.days, args.horizon, time.time() - t0)

        print("=" * 56)
        print(f"Model saved:  {model_path}")
        print(f"Features:     {features_path}")
        print(f"Report:       {REPORT_PATH}")
        print(f"Accuracy:     {metrics['accuracy']}")
        print("=" * 56)
        return 0
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
