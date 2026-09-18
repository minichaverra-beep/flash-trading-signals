"""Tests mínimos presets Zentinel BTC vs US30."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.models.zentinel_presets import (  # noqa: E402
    classify_killzone,
    classify_volume,
    get_fvg_volume,
    get_watchtower,
    normalize_market,
    relative_volume_ratio,
    volume_confluence_points,
)


def test_normalize_market_btc_us30():
    assert normalize_market("BTCUSDT") == "BTC"
    assert normalize_market("US30") == "US30"
    assert normalize_market("YM=F") == "US30"


def test_fvg_volume_thresholds_differ_by_market():
    btc = get_fvg_volume("BTC")
    us30 = get_fvg_volume("US30")
    assert btc["preset_name"] == "Zentinel_BTC_E1"
    assert us30["preset_name"] == "Zentinel_US30_E1"
    assert btc["high"] == 1.7
    assert us30["high"] == 1.6
    assert btc["extreme"] == 2.6
    assert us30["extreme"] == 2.8
    assert btc["period"] == 84
    assert us30["period"] == 48
    assert btc["low"] == 0.75
    assert us30["low"] == 0.70
    assert btc["very_low"] == 0.45
    assert us30["very_low"] == 0.40
    assert btc["role"] == "confluence_filter"
    assert us30["role"] == "confluence_filter"


def test_watchtower_smt_and_bias_differ():
    btc = get_watchtower("BTC")
    us30 = get_watchtower("US30")
    assert btc["preset_name"] == "Watchtower_BTC_E1"
    assert us30["preset_name"] == "Watchtower_US30_E1"
    assert btc["smt"]["lookback"] == 5
    assert btc["smt"]["sym1"] == "ETH"
    assert us30["smt"]["lookback"] == 3
    assert us30["smt"]["sym1"] == "ES"
    assert btc["bias_table"]["neutral_pct"] == 0.5
    assert us30["bias_table"]["neutral_pct"] == 0.3
    assert btc["mno"] is True
    assert us30["org"] is True
    assert us30["pw_mid"] is True


def test_killzone_ny_on_and_lunch_off():
    # 09:30 NY ≈ 13:30 UTC (EDT -4)
    am = classify_killzone(
        datetime(2026, 9, 18, 13, 30, tzinfo=timezone.utc),
        asset="BTC",
    )
    assert am["killzone_on"] is True
    assert am["in_ny_window"] is True
    assert "NY AM" in am["window"]

    # 12:00 NY ≈ 16:00 UTC → Lunch OFF
    lunch = classify_killzone(
        datetime(2026, 9, 18, 16, 0, tzinfo=timezone.utc),
        asset="US30",
    )
    assert lunch["killzone_on"] is False
    assert lunch["in_ny_window"] is False
    assert lunch["off_reason"] == "Lunch"

    # 15:00 NY ≈ 19:00 UTC → NY PM ON (hasta 16:00)
    pm = classify_killzone(
        datetime(2026, 9, 18, 19, 0, tzinfo=timezone.utc),
        asset="BTC",
    )
    assert pm["killzone_on"] is True
    assert "NY PM" in pm["window"]

    # 16:30 NY ≈ 20:30 UTC → fuera (PM termina 16:00)
    late = classify_killzone(
        datetime(2026, 9, 18, 20, 30, tzinfo=timezone.utc),
        asset="BTC",
    )
    assert late["killzone_on"] is False


def test_volume_classify_uses_market_period():
    # 50 velas con vol=10; última = 20 → ratio 2.0
    candles = [{"volume": 10.0} for _ in range(50)]
    candles.append({"volume": 20.0})
    btc = classify_volume(candles, asset="BTC")
    us30 = classify_volume(candles, asset="US30")
    assert btc["period"] == 84
    assert us30["period"] == 48
    assert btc["never_trigger"] is True
    # ratio ~2.0 → BTC alto (>=1.7), US30 alto (>=1.6)
    assert btc["band"] in ("alto", "extremo", "normal")
    assert us30["band"] in ("alto", "extremo", "normal")
    assert relative_volume_ratio(candles, 48) == 2.0


def test_volume_confluence_points_soft_filter():
    score, mx, note = volume_confluence_points({"band": "alto"})
    assert mx == 2.0
    assert score == 1.5
    assert "Vol" in note
    score0, mx0, _ = volume_confluence_points({"band": "muy_bajo"})
    assert score0 == 0.0
    assert mx0 == 2.0
