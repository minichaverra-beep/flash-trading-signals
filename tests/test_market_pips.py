"""Unit tests for daytrader pip / SL clamp helpers."""
from __future__ import annotations

from app.models.market_pips import (
    MAX_SL_PIPS,
    clamp_sl_tp,
    max_sl_distance,
    pip_size,
    pull_entry_toward_price,
)


def test_pip_sizes_per_market():
    assert pip_size("BTC") == 1.0
    assert pip_size("US30") == 1.0
    assert pip_size("XAUUSD") == 0.10
    assert max_sl_distance("BTC") == 60.0
    assert max_sl_distance("XAUUSD") == 6.0


def test_clamp_sl_tp_btc_long():
    sl, tp, risk, clamped = clamp_sl_tp(100_000.0, 99_800.0, None, "LONG", "BTC")
    assert clamped is True
    assert risk == MAX_SL_PIPS * pip_size("BTC")
    assert abs(sl - (100_000.0 - 60.0)) < 1e-9
    assert abs(tp - (100_000.0 + 120.0)) < 1e-9


def test_clamp_sl_tp_xau_short():
    sl, tp, risk, clamped = clamp_sl_tp(4300.0, 4280.0, None, "SHORT", "XAUUSD")
    assert clamped is True
    assert risk == 6.0
    assert abs(sl - 4306.0) < 1e-9
    assert abs(tp - 4288.0) < 1e-9


def test_pull_entry_toward_price_no_chase():
    # LONG limit below price → pull up
    assert pull_entry_toward_price(100.0, 110.0, "LONG", blend=0.5) == 105.0
    # LONG already at/above price → no chase
    assert pull_entry_toward_price(110.0, 100.0, "LONG", blend=0.5) == 110.0
