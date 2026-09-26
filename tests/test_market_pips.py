"""Unit tests for daytrader pip / SL clamp helpers."""
from __future__ import annotations

import pytest

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


def test_raw_sl_long_ignores_resistencia_level():
    """Chart bug: LONG + resistencia must not SL = level*0.997 under the zone."""
    from app.models.market_pips import raw_sl_from_zone

    level = 84_078.2
    entry_low = 83_849.7
    sl_low = raw_sl_from_zone(entry_low, "LONG", {"level": level, "type": "resistencia_debil"})
    assert abs(sl_low - entry_low * 0.997) < 1e-6
    # Old bug used level*0.997 (=83826) and squeezed TP under resistance
    assert abs(sl_low - (level * 0.997)) > 1.0


def test_raw_sl_long_uses_soporte():
    from app.models.market_pips import raw_sl_from_zone

    entry = 83_900.0
    level = 83_850.0
    sl = raw_sl_from_zone(entry, "LONG", {"level": level, "type": "soporte_debil"})
    assert abs(sl - level * 0.998) < 1e-6


def test_raw_entry_long_at_resistencia_uses_spot():
    from app.models.market_pips import raw_entry_from_zone

    price = 84_078.2
    entry, lo, hi = raw_entry_from_zone(
        price, "LONG", {"level": price, "type": "resistencia_debil"},
    )
    assert abs(entry - price) < 1e-6
    assert lo == price


def test_actual_rr():
    from app.models.market_pips import actual_rr

    assert actual_rr(100.0, 90.0, 120.0) == pytest.approx(2.0)
    assert actual_rr(100.0, 100.0, 120.0) is None