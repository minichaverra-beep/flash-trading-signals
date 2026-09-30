"""Frescura de velas live: evita emitir señales con datos viejos.

Horario oro (CME Globex, America/New_York): domingo 18:00 → viernes 17:00,
con pausa diaria 17:00–18:00. Solo cuentan los minutos con mercado abierto,
así el cierre de fin de semana no marca los datos como desactualizados.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Callable
from zoneinfo import ZoneInfo

NY_TZ = ZoneInfo("America/New_York")

# Yahoo GC=F llega con ~10 min de retraso + vela M5 en curso.
DEFAULT_MAX_LAG_MIN = 45
_MAX_SCAN = timedelta(days=14)


def gold_market_open(ts: datetime) -> bool:
    ny = ts.astimezone(NY_TZ)
    wd, hour = ny.weekday(), ny.hour  # lunes=0 … domingo=6
    if wd == 5:
        return False
    if wd == 6:
        return hour >= 18
    if wd == 4:
        return hour < 17
    return hour != 17


def open_minutes_between(
    start: datetime,
    end: datetime,
    is_open: Callable[[datetime], bool] = gold_market_open,
    step_min: int = 5,
) -> int:
    """Minutos con mercado abierto entre start y end (resolución step_min)."""
    if end <= start:
        return 0
    start = max(start, end - _MAX_SCAN)
    step = timedelta(minutes=step_min)
    total = 0.0
    t = start
    while t < end:
        nxt = min(t + step, end)
        if is_open(t):
            total += (nxt - t).total_seconds() / 60
        t = nxt
    return int(total)


def _as_utc(ts: datetime) -> datetime:
    return ts.replace(tzinfo=timezone.utc) if ts.tzinfo is None else ts.astimezone(timezone.utc)


def assess_freshness(
    last_candle: datetime,
    now: datetime | None = None,
    max_lag_min: int = DEFAULT_MAX_LAG_MIN,
    is_open: Callable[[datetime], bool] = gold_market_open,
) -> dict:
    """Evalúa si la última vela es lo bastante reciente para operar."""
    now = _as_utc(now or datetime.now(timezone.utc))
    last = _as_utc(last_candle)
    age_min = max(0, int((now - last).total_seconds() // 60))
    open_lag = open_minutes_between(last, now, is_open)
    stale = open_lag > max_lag_min
    last_label = last.strftime("%Y-%m-%d %H:%M")
    message = (
        f"Datos desactualizados: última vela {last_label} UTC "
        f"(hace {_fmt_age(age_min)}, {open_lag} min de mercado abierto) — no operar"
        if stale else None
    )
    return {
        "last_candle_utc": last_label,
        "age_min": age_min,
        "open_lag_min": open_lag,
        "max_lag_min": max_lag_min,
        "market_open": is_open(now),
        "stale": stale,
        "message": message,
    }


def freshness_md_lines(fresh: dict | None, source: str | None = None) -> list[str]:
    """Cabecera markdown: «Última vela M5 …» y aviso ⚠️ si los datos están desactualizados."""
    fresh = fresh or {}
    lines: list[str] = []
    if fresh.get("last_candle_utc"):
        src = f" · fuente {source}" if source is not None else ""
        lines.append(
            f"> Última vela M5 **{fresh['last_candle_utc']} UTC** · hace {fresh['age_min']} min{src}"
        )
    if fresh.get("stale"):
        lines.append(f"> ⚠️ **{fresh['message']}**")
    return lines


def log_freshness(fresh: dict) -> None:
    """Imprime WARN si la vela está desactualizada, si no la hora de la última vela."""
    if fresh["stale"]:
        print(f"WARN {fresh['message']}")
    else:
        print(f"Última vela M5: {fresh['last_candle_utc']} UTC (hace {fresh['age_min']} min)")


def _fmt_age(minutes: int) -> str:
    if minutes < 90:
        return f"{minutes} min"
    hours = minutes / 60
    if hours < 48:
        return f"{hours:.1f} h"
    return f"{hours / 24:.1f} días"
