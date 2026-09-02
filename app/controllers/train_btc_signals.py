"""
Train ML model on historical BTCUSDT M5/H1 data for E1 signal quality.

Usage:
  python -m app.controllers.train_btc_signals
  python -m app.controllers.train_btc_signals --quick
  python -m app.controllers.train_btc_signals --days 180 --horizon 48
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
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
REPORT_PATH = DATA_DIR / "ml_training_report.md"

# Reuse live analysis helpers
from app.controllers.analyze_btc_m5 import (  # noqa: E402
    BINANCE,
    h1_bias,
    nearest_zone,
    pdh_pdl,
    rsi,
    session_flags,
    suggest_setup,
    swing_levels,
    two_candle_confirm,
)
from app.services.btc_high_analysis import analyze_crt, detect_rsi_divergence, dmi_proxy  # noqa: E402
from app.models.btc_ml_signals import (  # noqa: E402
    FEATURES_PATH,
    MODEL_PATH,
    SL_USD_REF,
    BTC_PRICE_REF,
    extract_features,
    features_to_vector,
    feature_config,
    _default_feature_names,
)

M5_CACHE = DATA_DIR / "btcusdt_m5.parquet"
H1_CACHE = DATA_DIR / "btcusdt_h1.parquet"


def fetch_klines_paginated(
    symbol: str,
    interval: str,
    start: datetime,
    end: datetime,
) -> list[dict]:
    """Fetch klines from Binance public API with pagination (1000 per request)."""
    import json as _json
    from urllib.error import HTTPError, URLError
    from urllib.request import Request, urlopen

    rows: list[dict] = []
    start_ms = int(start.timestamp() * 1000)
    end_ms = int(end.timestamp() * 1000)
    current = start_ms

    while current < end_ms:
        url = (
            f"{BINANCE}?symbol={symbol}&interval={interval}"
            f"&startTime={current}&endTime={end_ms}&limit=1000"
        )
        req = Request(url, headers={"User-Agent": "CursorTrading-ML/1.0"})
        try:
            with urlopen(req, timeout=30) as resp:
                raw = _json.loads(resp.read().decode())
        except (URLError, HTTPError, TimeoutError) as e:
            raise RuntimeError(f"Binance fetch failed: {e}") from e

        if not raw:
            break

        for k in raw:
            rows.append({
                "open_time": datetime.fromtimestamp(k[0] / 1000, tz=timezone.utc),
                "open": float(k[1]),
                "high": float(k[2]),
                "low": float(k[3]),
                "close": float(k[4]),
                "volume": float(k[5]),
                "close_time": datetime.fromtimestamp(k[6] / 1000, tz=timezone.utc),
            })

        last_close = int(raw[-1][6])
        next_start = last_close + 1
        if next_start <= current:
            break
        current = next_start
        time.sleep(0.15)

    # Deduplicate by open_time
    seen: set[datetime] = set()
    unique: list[dict] = []
    for r in sorted(rows, key=lambda x: x["open_time"]):
        if r["open_time"] not in seen:
            seen.add(r["open_time"])
            unique.append(r)
    return unique


def candles_to_df(candles: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(candles)


def df_to_candles(df: pd.DataFrame) -> list[dict]:
    return df.to_dict("records")


def load_or_fetch_data(symbol: str, days: int, force: bool = False) -> tuple[list[dict], list[dict]]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)

    if not force and M5_CACHE.is_file() and H1_CACHE.is_file():
        m5_df = pd.read_parquet(M5_CACHE)
        h1_df = pd.read_parquet(H1_CACHE)
        m5 = df_to_candles(m5_df)
        h1 = df_to_candles(h1_df)
        if m5 and h1:
            print(f"Loaded cache: M5={len(m5)} H1={len(h1)} bars")
            return m5, h1

    print(f"Fetching {days}d {symbol} from Binance ({start.date()} -> {end.date()})...")
    t0 = time.time()
    m5 = fetch_klines_paginated(symbol, "5m", start, end)
    h1 = fetch_klines_paginated(symbol, "1h", start, end)
    print(f"Downloaded M5={len(m5)} H1={len(h1)} in {time.time() - t0:.1f}s")

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
    """
    Label 1 if TP (1:2) hit before SL within horizon bars.
    SL = structure from setup or fixed ~$9 at entry price.
    Returns None if neither TP nor SL hit (excluded from training).
    """
    sl_pct = SL_USD_REF / entry
    if direction == "LONG":
        sl_fixed = entry * (1.0 - sl_pct)
        sl = setup_sl if setup_sl is not None and setup_sl < entry else sl_fixed
        risk = entry - sl
        if risk <= 0:
            return None
        tp = entry + rr * risk
        for bar in future[:horizon]:
            hit_sl = bar["low"] <= sl
            hit_tp = bar["high"] >= tp
            if hit_sl and hit_tp:
                return 0
            if hit_sl:
                return 0
            if hit_tp:
                return 1
    elif direction == "SHORT":
        sl_fixed = entry * (1.0 + sl_pct)
        sl = setup_sl if setup_sl is not None and setup_sl > entry else sl_fixed
        risk = sl - entry
        if risk <= 0:
            return None
        tp = entry - rr * risk
        for bar in future[:horizon]:
            hit_sl = bar["high"] >= sl
            hit_tp = bar["low"] <= tp
            if hit_sl and hit_tp:
                return 0
            if hit_sl:
                return 0
            if hit_tp:
                return 1
    else:
        return None
    return None


def build_snapshot_at_index(
    m5: list[dict],
    h1: list[dict],
    idx: int,
    min_m5: int = 120,
) -> dict | None:
    """Reconstruct analysis `data` dict at historical bar idx."""
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
    sh, sl = swing_levels(window)
    zone = nearest_zone(price, sh, sl)
    session = session_flags(ts)
    confirm_long = two_candle_confirm(window, "LONG")
    confirm_short = two_candle_confirm(window, "SHORT")
    setup = suggest_setup(
        price, bias, zone, rsi_m5, confirm_long, confirm_short,
        session["in_ny_window"], pdh, pdl,
    )

    if setup["direction"] == "NONE":
        return None

    return {
        "generated": ts.strftime("%Y-%m-%d %H:%M"),
        "symbol": "BTCUSDT",
        "price": price,
        "session": session,
        "bias_h1": bias,
        "rsi_m5": rsi_m5,
        "rsi_h1": rsi_h1,
        "pdh": pdh,
        "pdl": pdl,
        "swing_highs": sh,
        "swing_lows": sl,
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
    """Generate labeled samples by walking M5 history."""
    feature_names = _default_feature_names()
    rows_x: list[np.ndarray] = []
    rows_y: list[int] = []
    meta: list[dict] = []

    total = len(m5) - horizon - 1
    processed = 0
    for idx in range(120, total, stride):
        processed += 1
        if processed % 500 == 0:
            print(f"  ... {processed} bars scanned, {len(rows_y)} samples so far")
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
            "rules_pct": int(feats.get("rules_pct_norm", 0) * 100),
            "label": label,
            "in_ny": data["session"]["in_ny_window"],
        })

    if not rows_x:
        raise RuntimeError("No training samples generated — check data range or filters.")

    X = np.vstack(rows_x)
    y = np.array(rows_y, dtype=np.int32)
    meta_df = pd.DataFrame(meta)
    return X, y, feature_names, meta_df


def winrate_by_bucket(y_true: np.ndarray, y_prob: np.ndarray, buckets: list[tuple[float, float]]) -> list[dict]:
    out = []
    for lo, hi in buckets:
        mask = (y_prob >= lo) & (y_prob < hi)
        n = int(mask.sum())
        if n == 0:
            out.append({"bucket": f"{lo:.0%}-{hi:.0%}", "n": 0, "winrate": None})
            continue
        wr = float(y_true[mask].mean())
        out.append({"bucket": f"{lo:.0%}-{hi:.0%}", "n": n, "winrate": round(wr * 100, 1)})
    return out


def train_model(X: np.ndarray, y: np.ndarray, algorithm: str = "gb"):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y if len(np.unique(y)) > 1 else None,
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
        "buckets": winrate_by_bucket(
            y_test, y_prob,
            [(0.0, 0.45), (0.45, 0.55), (0.55, 0.65), (0.65, 0.75), (0.75, 1.01)],
        ),
    }
    return clf, metrics


def write_report(
    metrics: dict,
    meta_df: pd.DataFrame,
    days: int,
    horizon: int,
    algorithm: str,
    elapsed: float,
) -> None:
    sl_pct = SL_USD_REF / BTC_PRICE_REF
    lines = [
        "# ML Training Report — BTC M5 E1 Signals",
        "",
        f"> Generado: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC",
        "",
        "## Configuración",
        "",
        f"| Parámetro | Valor |",
        f"|-----------|-------|",
        f"| Días históricos | {days} |",
        f"| Horizonte label (velas M5) | {horizon} ({horizon * 5 / 60:.1f} h) |",
        f"| Algoritmo | {algorithm} |",
        f"| SL referencia | ${SL_USD_REF} @ BTC ~${BTC_PRICE_REF:,.0f} → **{sl_pct*100:.4f}%** precio |",
        f"| TP objetivo | 1:2 R:R |",
        f"| Muestras totales | {len(meta_df)} |",
        f"| Win rate dataset | {meta_df['label'].mean()*100:.1f}% |",
        f"| Tiempo entrenamiento | {elapsed:.1f}s |",
        "",
        "## Métricas test (hold-out 25%)",
        "",
        f"- **Accuracy:** {metrics['accuracy']}",
        f"- **Precision:** {metrics['precision']}",
        f"- **Recall:** {metrics['recall']}",
        f"- **Win rate baseline test:** {metrics['test_winrate_baseline']*100:.1f}%",
        "",
        "### Win rate por bucket de probabilidad predicha",
        "",
        "| Bucket prob | N | Win rate real |",
        "|-------------|---|---------------|",
    ]
    for b in metrics["buckets"]:
        wr = f"{b['winrate']}%" if b["winrate"] is not None else "n/a"
        lines.append(f"| {b['bucket']} | {b['n']} | {wr} |")

    lines += [
        "",
        "### Classification report",
        "",
        "```",
        metrics["report"].strip(),
        "```",
        "",
        "## Notas",
        "",
        "- El modelo **complementa** las 8 reglas E1; no reemplaza validación TradingView.",
        "- Re-entrenar semanalmente o tras cambios en el plan E1.",
        "- SL dinámico: `9 / precio_entrada` cuando no hay SL estructural.",
        "",
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Train BTC M5 E1 signal ML model")
    parser.add_argument("--symbol", default="BTCUSDT")
    parser.add_argument("--days", type=int, default=365, help="History days (default 1 year)")
    parser.add_argument("--quick", action="store_true", help="30 days for testing")
    parser.add_argument("--horizon", type=int, default=48, help="Forward bars for label (default 48 = 4h)")
    parser.add_argument("--stride", type=int, default=3, help="Sample every N M5 bars")
    parser.add_argument("--algorithm", choices=("gb", "rf", "lr"), default="gb")
    parser.add_argument("--force-download", action="store_true")
    parser.add_argument("--ny-only", action="store_true", help="Train only on NY session bars")
    args = parser.parse_args()

    if args.quick:
        args.days = 30
        args.stride = 12  # every hour on M5 — fast smoke test

    t0 = time.time()
    try:
        m5, h1 = load_or_fetch_data(args.symbol, args.days, force=args.force_download)
        print("Building training dataset...")
        t_build = time.time()
        X, y, feature_names, meta_df = build_training_dataset(
            m5, h1, horizon=args.horizon, stride=args.stride, ny_only=args.ny_only,
        )
        print(f"Dataset built in {time.time() - t_build:.1f}s")
        print(f"Samples: {len(y)} | Win rate: {y.mean()*100:.1f}%")

        print(f"Training ({args.algorithm})...")
        model, metrics = train_model(X, y, algorithm=args.algorithm)

        MODELS_DIR.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, MODEL_PATH)

        cfg = feature_config()
        cfg.update({
            "feature_names": feature_names,
            "trained_at": datetime.now(timezone.utc).isoformat(),
            "days": args.days,
            "horizon_bars": args.horizon,
            "algorithm": args.algorithm,
            "samples": len(y),
            "dataset_winrate": round(float(y.mean()), 4),
            "metrics": {k: v for k, v in metrics.items() if k not in ("report", "buckets")},
        })
        FEATURES_PATH.write_text(json.dumps(cfg, indent=2), encoding="utf-8")

        elapsed = time.time() - t0
        write_report(metrics, meta_df, args.days, args.horizon, args.algorithm, elapsed)

        print("=" * 56)
        print(f"Model saved:  {MODEL_PATH}")
        print(f"Features:     {FEATURES_PATH}")
        print(f"Report:       {REPORT_PATH}")
        print(f"Accuracy:     {metrics['accuracy']}  Precision: {metrics['precision']}  Recall: {metrics['recall']}")
        print(f"Elapsed:      {elapsed:.1f}s")
        print("=" * 56)
        return 0
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
