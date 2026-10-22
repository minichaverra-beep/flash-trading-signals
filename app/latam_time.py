"""Hora de pared para Colombia, Perú y Ecuador.

Desfase fijo de −5 h respecto a UTC. No usa la zona del equipo ni America/New_York.
Un datetime sin zona, o un texto `yyyy-MM-dd HH:mm` del motor, se toma como UTC
y después se resta 5 h. Un ISO con `Z` o con desfase es un instante absoluto.
"""
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone

LATAM = timezone(timedelta(hours=-5))
_TOKEN = re.compile(
    r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(?::\d{2})?(?:\.\d+)?(?:Z|[+-]\d{2}:?\d{2})?(?:\s*UTC)?",
    re.IGNORECASE,
)


def format_latam(t: datetime | None, *, seconds: bool = False) -> str:
    if t is None:
        return "—"
    if t.tzinfo is None:
        t = t.replace(tzinfo=timezone.utc)
    local = t.astimezone(LATAM)
    fmt = "%d/%m/%Y %H:%M:%S" if seconds else "%d/%m/%Y %H:%M"
    return local.strftime(fmt)


def parse_as_utc(raw: str) -> datetime | None:
    s = str(raw or "").strip()
    if s.upper().endswith(" UTC"):
        s = s[:-4].strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    if "T" in s or (len(s) > 10 and ("+" in s[10:] or "-" in s[10:])):
        try:
            dt = datetime.fromisoformat(s)
        except ValueError:
            dt = None
        if dt is not None:
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def show_clock(value: datetime | str | None, *, seconds: bool = False) -> str:
    """Texto de pantalla. Si no se reconoce, se devuelve el original."""
    if isinstance(value, datetime):
        return format_latam(value, seconds=seconds)
    raw = str(value or "").strip()
    if not raw:
        return ""
    parsed = parse_as_utc(raw)
    return format_latam(parsed, seconds=seconds) if parsed else raw


def format_latam_text(text: str) -> str:
    return _TOKEN.sub(lambda m: show_clock(m.group(0)) or m.group(0), text)
