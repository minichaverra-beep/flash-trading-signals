"""Soporte/resistencia del PNG quantum y el salto de TimesFM sin red ni pesos."""
from __future__ import annotations

import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from datetime import date

from app.models.quantum_levels import (  # noqa: E402
    chart_level_tags,
    format_price,
    interest_labels,
    previous_completed_day,
    previous_day_tip,
    select_interest_points,
)
from app.models.timesfm_quantum import forecast_closes  # noqa: E402


def _flat(n: int = 64, price: float = 100.0):
    return [price + 1.0] * n, [price - 1.0] * n, [price] * n


def _stamp_low(highs, lows, closes, index: int, price: float) -> None:
    lows[index] = price
    highs[index] = price + 1.5
    closes[index] = price + 1.0


def _stamp_high(highs, lows, closes, index: int, price: float) -> None:
    highs[index] = price
    lows[index] = price - 1.5
    closes[index] = price - 1.0


def _clustered_book():
    """Tres toques en 90 y en 110, y un spike suelto en 70 y en 140."""
    highs, lows, closes = _flat()
    for index in (8, 20, 32):
        _stamp_low(highs, lows, closes, index, 90.0)
    for index in (14, 26, 38):
        _stamp_high(highs, lows, closes, index, 110.0)
    _stamp_low(highs, lows, closes, 44, 70.0)
    _stamp_high(highs, lows, closes, 50, 140.0)
    return highs, lows, closes


def test_strong_levels_come_from_clustered_pivots_not_spikes():
    highs, lows, closes = _clustered_book()
    points = select_interest_points(highs, lows, closes)
    supports = [p for p in points if p.kind == "support"]
    resistances = [p for p in points if p.kind == "resistance"]
    assert supports and resistances
    fuerte_s = next(p for p in supports if p.role == "fuerte")
    fuerte_r = next(p for p in resistances if p.role == "fuerte")
    assert 88.0 <= fuerte_s.price <= 92.0
    assert 108.0 <= fuerte_r.price <= 112.0
    assert fuerte_s.touches >= 2
    assert fuerte_r.touches >= 2
    assert all(abs(p.price - 70.0) > 5 for p in supports)
    assert all(abs(p.price - 140.0) > 5 for p in resistances)
    labels = interest_labels(points)
    assert any(label.startswith("Soporte fuerte") for label in labels)
    assert any(label.startswith("Resistencia fuerte") for label in labels)


def test_second_support_cluster_is_kept_when_it_is_competitive():
    highs, lows, closes = _flat(80)
    for index in (30, 42, 54):
        _stamp_low(highs, lows, closes, index, 90.0)
    for index in (36, 48):
        _stamp_low(highs, lows, closes, index, 96.0)
    for index in (33, 45, 57):
        _stamp_high(highs, lows, closes, index, 110.0)
    _stamp_low(highs, lows, closes, 18, 70.0)
    _stamp_high(highs, lows, closes, 22, 140.0)
    points = select_interest_points(highs, lows, closes)
    supports = [p for p in points if p.kind == "support"]
    assert any(abs(p.price - 96.0) < 1.5 for p in supports)
    assert any(abs(p.price - 90.0) < 1.5 for p in supports)
    assert all(p.price > 80.0 for p in supports)


def test_forecast_horizon_is_an_extra_point_with_its_own_price():
    highs, lows, closes = _clustered_book()
    points = select_interest_points(highs, lows, closes, forecast_level=105.25)
    forecast = [p for p in points if p.kind == "forecast"]
    assert len(forecast) == 1
    assert forecast[0].price == 105.25
    assert forecast[0].role == "horizonte"
    assert any(label.startswith("Horizonte TimesFM 105.25") for label in interest_labels(points))


def test_monotonic_series_does_not_use_min_or_max():
    highs = [100.0 + i for i in range(40)]
    lows = [99.0 + i for i in range(40)]
    closes = [99.5 + i for i in range(40)]
    points = select_interest_points(highs, lows, closes)
    assert points == []
    assert all(p.price != lows[0] and p.price != highs[-1] for p in points)


def test_timesfm_skips_when_library_missing(monkeypatch):
    import builtins

    real_import = builtins.__import__

    def guarded(name, *args, **kwargs):
        if name.split(".")[0] == "timesfm":
            raise ModuleNotFoundError("timesfm")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", guarded)
    sys.modules.pop("timesfm", None)
    note = forecast_closes([100.0 + (i % 5) for i in range(48)])
    assert note.status == "skipped"
    assert note.horizon_level is None
    assert note.summary.startswith("skipped ")
    assert "biblioteca" in note.summary


def test_timesfm_skips_without_weights_and_does_not_run_the_model(monkeypatch):
    import app.models.timesfm_quantum as mod

    fake = types.ModuleType("timesfm")
    monkeypatch.setitem(sys.modules, "timesfm", fake)
    monkeypatch.setattr(mod, "_local_checkpoint", lambda: None)

    def fail_if_called(*_args, **_kwargs):
        raise AssertionError("no debe cargar el modelo ni descargar pesos")

    monkeypatch.setattr(mod, "_forecast_log_prices", fail_if_called)
    note = forecast_closes([100.0 + (i % 7) * 0.1 for i in range(64)])
    assert note.status == "skipped"
    assert note.summary == "skipped sin pesos locales"
    assert note.horizon_level is None


def test_timesfm_invalid_prices_do_not_raise():
    note = forecast_closes([])
    assert note.status == "skipped"
    note_bad = forecast_closes([1.0, 0.0, 2.0] * 20)
    assert note_bad.status == "skipped"
    assert note_bad.horizon_level is None


def test_chart_tags_use_the_strong_levels_and_the_last_close():
    highs, lows, closes = _clustered_book()
    points = select_interest_points(highs, lows, closes)
    tags = [tag.text for tag in chart_level_tags(points, closes[-1])]
    assert "Resistencia macro 110" in tags
    assert "Soporte macro 90" in tags
    assert f"Precio {format_price(closes[-1])}" in tags
    assert sum(text.startswith("Soporte macro") for text in tags) == 1
    assert sum(text.startswith("Resistencia macro") for text in tags) == 1


def _prior_day():
    yesterday = date(2024, 10, 18)
    today = date(2024, 10, 19)
    days = [yesterday, yesterday, yesterday, today, today]
    opens = [104.0, 106.0, 108.0, 100.0, 101.0]
    highs = [108.0, 112.0, 120.0, 103.0, 500.0]
    lows = [100.0, 105.0, 107.0, 50.0, 100.2]
    closes = [106.0, 110.0, 118.0, 101.0, 100.4]
    return previous_completed_day(days, opens, highs, lows, closes)


def test_tip_names_yesterday_low_and_stays_quiet_when_far():
    prior = _prior_day()
    assert prior is not None
    assert prior.low == 100.0
    assert prior.high == 120.0
    assert prior.open == 104.0
    assert prior.close == 118.0
    # 15% de ATR 10 = 1.5; 10% del rango 20 = 2. El umbral es 2.
    assert previous_day_tip(100.4, prior, 10) == "En el mínimo de ayer 100"
    assert previous_day_tip(150.0, prior, 10) is None


def test_closer_prior_reference_wins_and_open_counts():
    prior = _prior_day()
    # 15% de ATR 20 = 3; 10% del rango 20 = 2. Umbral 3.
    # 118.4 está a 0.4 del cierre y a 1.6 del máximo.
    assert previous_day_tip(118.4, prior, 20) == "En el cierre de ayer 118"
    assert previous_day_tip(119.2, prior, 20) == "En el máximo de ayer 120"
    assert previous_day_tip(104.2, prior, 10) == "En la apertura de ayer 104"


def test_forming_day_is_not_used_as_yesterday():
    today = date(2024, 10, 19)
    assert (
        previous_completed_day(
            [today, today, today, today],
            [10.0, 10.0, 10.0, 10.0],
            [12.0, 12.0, 12.0, 12.0],
            [8.0, 8.0, 8.0, 8.0],
            [11.0, 11.0, 11.0, 11.0],
        )
        is None
    )
    prior = _prior_day()
    # 50 es el mínimo de hoy, no el de ayer (100).
    assert previous_day_tip(50.2, prior, 2) is None
    assert previous_day_tip(100.4, None, 10) is None
