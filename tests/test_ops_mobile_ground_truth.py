"""Unit tests for mobile ops ground-truth matching helpers."""
from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.models.ops_mobile_ground_truth import (  # noqa: E402
    MatchedOp,
    build_ops_feature_rows,
    find_bar_index,
    label_with_levels,
    load_ops_trades,
    match_ops_to_m5,
    match_summary,
    parse_capture_ts,
    write_vision_labels,
)


def _bar(ts: datetime, close: float, high: float | None = None, low: float | None = None) -> dict:
    return {
        "open_time": ts,
        "open": close,
        "high": high if high is not None else close + 10,
        "low": low if low is not None else close - 10,
        "close": close,
    }


def test_parse_capture_ts_none_and_nan():
    assert parse_capture_ts(None) is None
    assert parse_capture_ts(float("nan")) is None
    assert parse_capture_ts("nan") is None
    assert parse_capture_ts("not-a-date") is None


def test_parse_capture_ts_aware_and_naive():
    aware = parse_capture_ts("2026-06-01T12:00:00+00:00")
    assert aware is not None
    assert aware.tzinfo is not None
    naive = parse_capture_ts("2026-06-01T12:00:00")
    assert naive is not None
    assert naive.utcoffset() == timedelta(0) or naive.tzinfo is not None


def test_find_bar_index_nearest_by_price_and_time():
    base = datetime(2026, 6, 1, 12, 0, tzinfo=timezone.utc)
    m5 = [_bar(base + timedelta(minutes=5 * i), 100.0 + i) for i in range(40)]
    hit = find_bar_index(m5, base + timedelta(minutes=50), 110.0, window_hours=2.0, max_price_err_pct=1.0)
    assert hit is not None
    idx, close, perr = hit
    assert idx == 10
    assert close == 110.0
    assert perr == 0.0


def test_find_bar_index_rejects_far_price():
    base = datetime(2026, 6, 1, 12, 0, tzinfo=timezone.utc)
    m5 = [_bar(base + timedelta(minutes=5 * i), 100.0) for i in range(20)]
    assert find_bar_index(m5, base, 200.0, max_price_err_pct=0.5) is None
    assert find_bar_index([], base, 100.0) is None


def test_label_with_levels_long_tp_and_sl():
    entry = 100.0
    future_tp = [{"high": 110.0, "low": 99.0}]
    lab, src = label_with_levels("long", entry, 95.0, 108.0, future_tp, 5, lambda *a, **k: 0)
    assert lab == 1 and src == "real_sl_tp"

    future_sl = [{"high": 101.0, "low": 94.0}]
    lab, src = label_with_levels("long", entry, 95.0, 108.0, future_sl, 5, lambda *a, **k: 1)
    assert lab == 0 and src == "real_sl_tp"


def test_label_with_levels_short_and_fallback():
    entry = 100.0
    future = [{"high": 101.0, "low": 90.0}]
    lab, src = label_with_levels("short", entry, 105.0, 92.0, future, 5, lambda *a, **k: None)
    assert lab == 1 and src == "real_sl_tp"

    lab, src = label_with_levels("long", entry, None, None, future, 5, lambda *a, **k: 1)
    assert lab == 1 and src == "fixed_rr"

    lab, src = label_with_levels("long", entry, None, None, future, 5, lambda *a, **k: None)
    assert lab is None and src == "fixed_rr_open"

    lab, src = label_with_levels("long", entry, 95.0, 110.0, [{"high": 100.5, "low": 99.5}], 1, lambda *a, **k: 0)
    assert lab is None and src == "real_sl_tp_open"


def test_label_both_hit_same_bar_counts_loss():
    future = [{"high": 120.0, "low": 80.0}]
    lab, src = label_with_levels("long", 100.0, 90.0, 110.0, future, 3, lambda *a, **k: 1)
    assert lab == 0 and src == "real_sl_tp"


def test_match_ops_to_m5_and_summary(tmp_path: Path):
    base = datetime(2026, 6, 1, 15, 0, tzinfo=timezone.utc)
    m5 = [_bar(base + timedelta(minutes=5 * i), 64000.0 + i) for i in range(80)]
    ops = pd.DataFrame(
        [
            {
                "trade_id": "t1",
                "source_image": "a.png",
                "symbol_norm": "BTCUSDT",
                "side": "long",
                "entry_price": 64010.0,
                "stop_loss": 63900.0,
                "take_profit": 64150.0,
                "capture_ts_from_name": (base + timedelta(minutes=50)).isoformat(),
                "confidence": 0.9,
            }
        ]
    )
    # Ensure future bars can hit TP
    for i in range(11, 40):
        m5[i]["high"] = 64200.0

    matched = match_ops_to_m5(
        ops,
        m5,
        horizon=20,
        fallback_label_fn=lambda *a, **k: 0,
        max_price_err_pct=1.0,
        window_hours=4.0,
    )
    assert len(matched) == 1
    assert matched[0].label == 1
    summary = match_summary(matched)
    assert summary["n"] == 1 and summary["wins"] == 1 and summary["winrate"] == 1.0
    assert match_summary([])["n"] == 0

    out = write_vision_labels(matched, tmp_path / "labels.csv")
    assert out.is_file()
    df = pd.read_csv(out)
    assert list(df["label"]) == ["WIN"]


def test_load_ops_trades_filters(tmp_path: Path):
    csv_path = tmp_path / "trades.csv"
    pd.DataFrame(
        [
            {
                "confidence": 0.9,
                "entry_price": 100.0,
                "side": "long",
                "symbol": "BTCUSDT",
            },
            {
                "confidence": 0.1,
                "entry_price": 100.0,
                "side": "long",
                "symbol": "BTCUSDT",
            },
            {
                "confidence": 0.9,
                "entry_price": 100.0,
                "side": "long",
                "symbol": "ETHUSDT",
            },
        ]
    ).to_csv(csv_path, index=False)
    df = load_ops_trades(csv_path, min_confidence=0.45)
    assert len(df) == 1
    assert df.iloc[0]["symbol_norm"] == "BTCUSDT"
    with pytest.raises(FileNotFoundError):
        load_ops_trades(tmp_path / "missing.csv")


def test_build_ops_feature_rows_empty_and_forced():
    base = datetime(2026, 6, 1, 12, 0, tzinfo=timezone.utc)
    m5 = [_bar(base + timedelta(minutes=5 * i), 100.0 + i * 0.1) for i in range(150)]
    h1 = m5[::12]
    op = MatchedOp(
        trade_id="t",
        source_image="x.png",
        symbol="BTCUSDT",
        side="long",
        entry_price=100.0,
        stop_loss=99.0,
        take_profit=102.0,
        capture_ts_utc=base,
        bar_index=130,
        bar_time=m5[130]["open_time"],
        price_at_bar=100.0,
        price_error_pct=0.01,
        label=1,
        label_source="fixed_rr",
        confidence=0.8,
    )

    def snap(m5_, h1_, idx, require_setup=True):
        return {
            "price": m5_[idx]["close"],
            "pdh": 110.0,
            "pdl": 90.0,
            "setup": {"direction": "NONE"},
        }

    X, y, meta = build_ops_feature_rows(
        [op],
        m5,
        h1,
        build_snapshot_fn=snap,
        analyze_crt_fn=lambda *a, **k: {},
        detect_div_fn=lambda *a, **k: {},
        dmi_fn=lambda *a, **k: {},
        extract_features_fn=lambda *a, **k: {"f": 1.0},
        features_to_vector_fn=lambda feats, names: np.array([1.0]),
        feature_names=["f"],
        h1_up_to_fn=lambda h, ts: h,
    )
    assert X.shape == (1, 1)
    assert list(y) == [1]
    assert meta.iloc[0]["source"] == "mobile_ops"

    X0, y0, meta0 = build_ops_feature_rows(
        [],
        m5,
        h1,
        build_snapshot_fn=snap,
        analyze_crt_fn=lambda *a, **k: {},
        detect_div_fn=lambda *a, **k: {},
        dmi_fn=lambda *a, **k: {},
        extract_features_fn=lambda *a, **k: {},
        features_to_vector_fn=lambda feats, names: np.zeros(len(names)),
        feature_names=["f"],
        h1_up_to_fn=lambda h, ts: h,
    )
    assert X0.shape == (0, 1) and len(y0) == 0 and meta0.empty
