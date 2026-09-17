"""
Ground-truth from mobile ops (v_ops_apr_sep) → ML samples + vision labels.

Matches OCR trades to M5 candles, labels WIN/LOSS with real SL/TP when available,
and builds feature vectors compatible with BTC/US30 signal models.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable

import numpy as np
import pandas as pd

from app.config import DATA_DIR, MOBILE_OPS_DIR, OPS_MOBILE_DATA_DIR

OPS_VERSION = "v_ops_apr_sep"
OPS_TRADES = OPS_MOBILE_DATA_DIR / OPS_VERSION / "trades.csv"
try:
    from zoneinfo import ZoneInfo

    LOCAL_TZ = ZoneInfo("America/Bogota")
except Exception:  # noqa: BLE001 — Windows without tzdata
    LOCAL_TZ = timezone(timedelta(hours=-5))


@dataclass
class MatchedOp:
    trade_id: str
    source_image: str
    symbol: str
    side: str  # long|short
    entry_price: float
    stop_loss: float | None
    take_profit: float | None
    capture_ts_utc: datetime
    bar_index: int
    bar_time: datetime
    price_at_bar: float
    price_error_pct: float
    label: int  # 1=win, 0=loss
    label_source: str  # real_sl_tp | fixed_rr
    confidence: float


def load_ops_trades(
    path: Path | None = None,
    *,
    min_confidence: float = 0.45,
    symbols: set[str] | None = None,
) -> pd.DataFrame:
    path = path or OPS_TRADES
    if not path.is_file():
        raise FileNotFoundError(f"Ops dataset not found: {path}")
    df = pd.read_csv(path)
    df = df[df["confidence"].fillna(0) >= min_confidence].copy()
    df = df[df["entry_price"].notna() & df["side"].notna()].copy()
    # Normalize symbol
    df["symbol_norm"] = df["symbol"].astype(str).str.upper().str.replace("BTCUSDT_REVIEW", "SKIP")
    if symbols:
        df = df[df["symbol_norm"].isin(symbols)].copy()
    else:
        df = df[df["symbol_norm"].isin({"BTCUSDT", "US30", "XAUUSD"})].copy()
    return df.reset_index(drop=True)


def parse_capture_ts(value: Any) -> datetime | None:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return None
    s = str(value).strip()
    if not s or s.lower() == "nan":
        return None
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=LOCAL_TZ)
    return dt.astimezone(timezone.utc)


def _ensure_aware(ts: datetime) -> datetime:
    if ts.tzinfo is None:
        return ts.replace(tzinfo=timezone.utc)
    return ts.astimezone(timezone.utc)


def find_bar_index(
    m5: list[dict],
    target_utc: datetime,
    entry_price: float,
    *,
    window_hours: float = 3.0,
    max_price_err_pct: float = 0.45,
) -> tuple[int, float, float] | None:
    """Nearest M5 bar by time within window, filtered by price proximity."""
    target_utc = _ensure_aware(target_utc)
    if not m5:
        return None
    # Binary search approximate index
    lo, hi = 0, len(m5) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if _ensure_aware(m5[mid]["open_time"]) < target_utc:
            lo = mid + 1
        else:
            hi = mid
    center = lo
    half = timedelta(hours=window_hours)
    # Bars span ~5m → window_hours*12 bars each side + margin
    radius = int(window_hours * 12) + 5
    i0 = max(0, center - radius)
    i1 = min(len(m5), center + radius + 1)
    best: tuple[int, float, float, float] | None = None
    for i in range(i0, i1):
        ts = _ensure_aware(m5[i]["open_time"])
        if abs(ts - target_utc) > half:
            continue
        close = float(m5[i]["close"])
        if close <= 0:
            continue
        perr = abs(close - entry_price) / entry_price * 100.0
        if perr > max_price_err_pct:
            continue
        terr = abs((ts - target_utc).total_seconds())
        if best is None or (perr, terr) < (best[1], best[2]):
            best = (i, perr, terr, close)
    if best is None:
        return None
    return best[0], best[3], best[1]


def label_with_levels(
    side: str,
    entry: float,
    sl: float | None,
    tp: float | None,
    future: list[dict],
    horizon: int,
    fallback_label_fn: Callable[..., int | None],
) -> tuple[int | None, str]:
    """Prefer real SL/TP from screenshot; else fallback to trainer label_outcome."""
    direction = "LONG" if side.lower() == "long" else "SHORT"
    if sl is not None and tp is not None and entry > 0:
        for bar in future[:horizon]:
            if direction == "LONG":
                hit_sl = bar["low"] <= sl
                hit_tp = bar["high"] >= tp
            else:
                hit_sl = bar["high"] >= sl
                hit_tp = bar["low"] <= tp
            if hit_sl and hit_tp:
                return 0, "real_sl_tp"
            if hit_sl:
                return 0, "real_sl_tp"
            if hit_tp:
                return 1, "real_sl_tp"
        return None, "real_sl_tp_open"
    lab = fallback_label_fn(direction, entry, sl, future, horizon)
    if lab is None:
        return None, "fixed_rr_open"
    return lab, "fixed_rr"


def match_ops_to_m5(
    ops: pd.DataFrame,
    m5: list[dict],
    *,
    horizon: int,
    fallback_label_fn: Callable[..., int | None],
    max_price_err_pct: float = 0.45,
    window_hours: float = 3.0,
) -> list[MatchedOp]:
    matched: list[MatchedOp] = []
    for _, row in ops.iterrows():
        ts = parse_capture_ts(row.get("capture_ts_from_name") or row.get("entry_time"))
        if ts is None:
            continue
        entry = float(row["entry_price"])
        # Try local-as-UTC-5 first (already converted in parse), also try raw-as-UTC
        candidates = [ts]
        raw = row.get("capture_ts_from_name") or row.get("entry_time")
        try:
            naive = datetime.fromisoformat(str(raw))
            if naive.tzinfo is None:
                candidates.append(naive.replace(tzinfo=timezone.utc))
        except Exception:
            pass

        hit = None
        used_ts = ts
        for cand in candidates:
            hit = find_bar_index(
                m5,
                cand,
                entry,
                window_hours=window_hours,
                max_price_err_pct=max_price_err_pct,
            )
            if hit is not None:
                used_ts = cand
                break
        if hit is None:
            continue
        idx, bar_close, perr = hit
        if idx + 1 + horizon >= len(m5):
            continue
        side = str(row["side"]).lower()
        sl = float(row["stop_loss"]) if pd.notna(row.get("stop_loss")) else None
        tp = float(row["take_profit"]) if pd.notna(row.get("take_profit")) else None
        label, src = label_with_levels(
            side,
            entry,
            sl,
            tp,
            m5[idx + 1 : idx + 1 + horizon],
            horizon,
            fallback_label_fn,
        )
        if label is None:
            continue
        matched.append(
            MatchedOp(
                trade_id=str(row.get("trade_id")),
                source_image=str(row.get("source_image")),
                symbol=str(row.get("symbol_norm") or row.get("symbol")),
                side=side,
                entry_price=entry,
                stop_loss=sl,
                take_profit=tp,
                capture_ts_utc=used_ts,
                bar_index=idx,
                bar_time=_ensure_aware(m5[idx]["open_time"]),
                price_at_bar=bar_close,
                price_error_pct=perr,
                label=int(label),
                label_source=src,
                confidence=float(row.get("confidence") or 0),
            )
        )
    return matched


def build_ops_feature_rows(
    matched: list[MatchedOp],
    m5: list[dict],
    h1: list[dict],
    *,
    build_snapshot_fn: Callable,
    analyze_crt_fn: Callable,
    detect_div_fn: Callable,
    dmi_fn: Callable,
    extract_features_fn: Callable,
    features_to_vector_fn: Callable,
    feature_names: list[str],
    h1_up_to_fn: Callable,
    force_direction: bool = True,
) -> tuple[np.ndarray, np.ndarray, pd.DataFrame]:
    """Build X,y from matched ops. Optionally override setup direction to trade side."""
    rows_x: list[np.ndarray] = []
    rows_y: list[int] = []
    meta: list[dict] = []

    for op in matched:
        data = build_snapshot_fn(m5, h1, op.bar_index, require_setup=False)
        if data is None:
            # Force a minimal snapshot path: try nearby bars
            for delta in range(1, 12):
                for idx in (op.bar_index - delta, op.bar_index + delta):
                    if 120 <= idx < len(m5) - 1:
                        found = build_snapshot_fn(m5, h1, idx, require_setup=False)
                        if found is not None:
                            op = MatchedOp(**{**op.__dict__, "bar_index": idx})
                            data = found
                            break
                if data is not None:
                    break
        if data is None:
            continue

        if force_direction:
            direction = "LONG" if op.side == "long" else "SHORT"
            setup = dict(data.get("setup") or {})
            setup["direction"] = direction
            if op.stop_loss is not None:
                setup["sl"] = op.stop_loss
            data = dict(data)
            data["setup"] = setup
            # Align confirm flags loosely
            if direction == "LONG":
                data["confirm_long"] = True
            else:
                data["confirm_short"] = True

        ts = m5[op.bar_index]["open_time"]
        h1_at = h1_up_to_fn(h1, ts)
        m5_at = m5[: op.bar_index + 1]
        crt = analyze_crt_fn(data["price"], data.get("pdh"), data.get("pdl"), h1_at, m5_at)
        div = detect_div_fn(m5_at)
        dmi = dmi_fn([c["close"] for c in m5_at])
        feats = extract_features_fn(data, crt, div, dmi)
        rows_x.append(features_to_vector_fn(feats, feature_names))
        rows_y.append(op.label)
        meta.append(
            {
                "time": _ensure_aware(ts).isoformat(),
                "direction": data["setup"]["direction"],
                "price": data["price"],
                "label": op.label,
                "source": "mobile_ops",
                "source_image": op.source_image,
                "trade_id": op.trade_id,
                "label_source": op.label_source,
                "price_error_pct": round(op.price_error_pct, 4),
                "ops_confidence": op.confidence,
            }
        )

    if not rows_x:
        return (
            np.zeros((0, len(feature_names))),
            np.zeros((0,), dtype=np.int32),
            pd.DataFrame(meta),
        )
    return np.vstack(rows_x), np.array(rows_y, dtype=np.int32), pd.DataFrame(meta)


def write_vision_labels(matched: list[MatchedOp], out_csv: Path) -> Path:
    """WIN/LOSS CSV for neural training (filename,label)."""
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for op in matched:
        rows.append(
            {
                "filename": op.source_image,
                "label": "WIN" if op.label == 1 else "LOSS",
                "trade_id": op.trade_id,
                "symbol": op.symbol,
                "label_source": op.label_source,
                "confidence": op.confidence,
            }
        )
    pd.DataFrame(rows).drop_duplicates(subset=["filename"]).to_csv(out_csv, index=False)
    return out_csv


def match_summary(matched: list[MatchedOp]) -> dict[str, Any]:
    if not matched:
        return {"n": 0, "winrate": None}
    wins = sum(1 for m in matched if m.label == 1)
    return {
        "n": len(matched),
        "wins": wins,
        "losses": len(matched) - wins,
        "winrate": round(wins / len(matched), 4),
        "by_label_source": (
            pd.Series([m.label_source for m in matched]).value_counts().to_dict()
        ),
        "mean_price_error_pct": round(
            float(np.mean([m.price_error_pct for m in matched])), 4
        ),
    }
