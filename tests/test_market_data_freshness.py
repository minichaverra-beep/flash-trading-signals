"""Tests del guard de frescura de velas (oro CME, horario NY)."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from app.models.market_data_freshness import (
    DEFAULT_MAX_LAG_MIN,
    assess_freshness,
    gold_market_open,
    open_minutes_between,
)
from app.views.btc_e1_report import collect_red_flags, derive_e1_verdict


def _utc(*args) -> datetime:
    return datetime(*args, tzinfo=timezone.utc)


def test_gold_market_hours_ny():
    # 2026-09-30 es miércoles; NY = UTC-4 (EDT)
    assert gold_market_open(_utc(2026, 9, 30, 14, 0)) is True
    assert gold_market_open(_utc(2026, 9, 30, 21, 30)) is False  # pausa 17-18 NY
    assert gold_market_open(_utc(2026, 10, 2, 21, 30)) is False  # viernes tras cierre
    assert gold_market_open(_utc(2026, 10, 3, 12, 0)) is False  # sábado
    assert gold_market_open(_utc(2026, 10, 4, 21, 0)) is False  # domingo antes de abrir
    assert gold_market_open(_utc(2026, 10, 4, 22, 30)) is True  # domingo abierto


def test_fresh_candle_not_stale():
    now = _utc(2026, 9, 30, 14, 15)
    f = assess_freshness(now - timedelta(minutes=10), now)
    assert f["stale"] is False
    assert f["message"] is None
    assert f["age_min"] == 10


def test_week_old_candle_is_stale_with_spanish_message():
    now = _utc(2026, 9, 30, 14, 15)
    f = assess_freshness(_utc(2026, 9, 23, 16, 25), now)
    assert f["stale"] is True
    assert f["open_lag_min"] > DEFAULT_MAX_LAG_MIN
    assert f["message"].startswith("Datos desactualizados: última vela 2026-09-23 16:25 UTC")


def test_weekend_closure_is_not_stale():
    # Última vela viernes 16:55 NY; ahora sábado → 5 min de mercado abierto
    last = _utc(2026, 10, 2, 20, 55)
    now = _utc(2026, 10, 3, 15, 0)
    assert open_minutes_between(last, now) == 5
    assert assess_freshness(last, now)["stale"] is False


def test_monday_with_friday_candle_is_stale():
    last = _utc(2026, 10, 2, 20, 55)
    now = _utc(2026, 10, 5, 14, 0)
    assert assess_freshness(last, now)["stale"] is True


def test_naive_datetime_treated_as_utc():
    now = _utc(2026, 9, 30, 14, 15)
    f = assess_freshness(datetime(2026, 9, 30, 14, 5), now)
    assert f["last_candle_utc"] == "2026-09-30 14:05"
    assert f["stale"] is False


def _setup_data(stale: bool) -> dict:
    return {
        "setup": {"direction": "LONG", "red_flags": [], "entry": 1, "sl": 1, "tp": 1,
                  "verdict": "SETUP_A+"},
        "confirm_long": True,
        "confirm_short": False,
        "bias_h1": "BULLISH",
        "data_stale": stale,
        "data_freshness": {"message": "Datos desactualizados: última vela X"} if stale else {},
    }


def test_stale_data_forces_no_operar_and_red_flag():
    data = _setup_data(True)
    assert derive_e1_verdict(data, {"rules_pct": 100}) == "NO_OPERAR"
    assert collect_red_flags(data)[0].startswith("Datos desactualizados")


def test_fresh_data_does_not_add_stale_flag():
    data = _setup_data(False)
    assert derive_e1_verdict(data, {"rules_pct": 100}) != "NO_OPERAR"
    assert not any("desactualizados" in f for f in collect_red_flags(data))
