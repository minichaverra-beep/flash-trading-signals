"""Presets Zentinel (TradingView) — calibraciones BTC / US30 para el stack local.

Fuente YAML: ``config/zentinel_presets.yaml``.
El pipeline Advanced/High usa estos umbrales en:
  - sesión / killzones NY (Watchtower)
  - filtro de confluencia por volumen relativo (FVG Multi TF + Volumen)
  - anotaciones ligeras en chart / reporte Advanced

No lee TradingView en vivo: los valores son checklist TV + lógica local.
Rol volumen: filtro de confluencia, NUNCA trigger. Entrada = H1/CTR + zona + 2M5.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.config import CONFIG_DIR, PROJECT_ROOT

YAML_PATH = CONFIG_DIR / "zentinel_presets.yaml"
NY_TZ_NAME = "America/New_York"
# Fallback fijo EDT (-4) si zoneinfo no está disponible; alinea con market_analysis_core.
_NY_OFFSET = timedelta(hours=-4)

# Defaults embebidos (espejo del YAML) — tests / entornos sin PyYAML.
_DEFAULTS: dict[str, Any] = {
    "version": "2026-09-18",
    "timezone": NY_TZ_NAME,
    "role_note": (
        "FVG Multi TF + Volumen = filtro de confluencia, NUNCA trigger. "
        "Entrada = H1/CTR + zona + 2M5."
    ),
    "markets": {
        "BTC": {
            "fvg_volume": {
                "preset_name": "Zentinel_BTC_E1",
                "high": 1.7,
                "extreme": 2.6,
                "low": 0.75,
                "very_low": 0.45,
                "period": 84,
                "labels": "small",
                "role": "confluence_filter",
            },
            "watchtower": {
                "preset_name": "Watchtower_BTC_E1",
                "killzones": {
                    "off": [
                        {"name": "Asia", "start": "19:00", "end": "20:00"},
                        {"name": "London", "start": "02:00", "end": "05:00"},
                        {"name": "Lunch", "start": "11:00", "end": "14:00"},
                    ],
                    "on": [
                        {"name": "NY_AM_open", "start": "08:00", "end": "10:00"},
                        {"name": "NY_AM_mid", "start": "10:00", "end": "11:00"},
                        {"name": "NY_PM", "start": "14:00", "end": "16:00"},
                    ],
                },
                "smt": {
                    "htf": False,
                    "max": 3,
                    "lookback": 5,
                    "sym1": "ETH",
                    "sym2": "ES",
                },
                "bias_table": {"avg": 3, "neutral_pct": 0.5},
                "mno": True,
                "org": False,
                "pw_mid": False,
            },
        },
        "US30": {
            "fvg_volume": {
                "preset_name": "Zentinel_US30_E1",
                "high": 1.6,
                "extreme": 2.8,
                "low": 0.70,
                "very_low": 0.40,
                "period": 48,
                "labels": "small",
                "role": "confluence_filter",
            },
            "watchtower": {
                "preset_name": "Watchtower_US30_E1",
                "killzones": {
                    "off": [
                        {"name": "Asia", "start": "19:00", "end": "20:00"},
                        {"name": "London", "start": "02:00", "end": "05:00"},
                        {"name": "Lunch", "start": "11:00", "end": "14:00"},
                    ],
                    "on": [
                        {"name": "NY_AM_open", "start": "08:00", "end": "10:00"},
                        {"name": "NY_AM_mid", "start": "10:00", "end": "11:00"},
                        {"name": "NY_PM", "start": "14:00", "end": "16:00"},
                    ],
                },
                "smt": {
                    "htf": False,
                    "max": 3,
                    "lookback": 3,
                    "sym1": "ES",
                    "sym2": "NQ",
                },
                "bias_table": {"avg": 3, "neutral_pct": 0.3},
                "org": True,
                "org_rth": {"start": "09:30", "end": "16:15"},
                "ce50": True,
                "labels": False,
                "pw_mid": True,
                "mno": False,
            },
        },
    },
}


def normalize_market(asset: str | None) -> str:
    a = (asset or "BTC").upper().strip()
    if a in ("BTC", "BTCUSDT", "XBT"):
        return "BTC"
    if "US30" in a or a in ("DJI", "YM", "YM=F", "^DJI"):
        return "US30"
    return "BTC" if a.startswith("BTC") else a


def _parse_hhmm(s: str) -> float:
    hh, mm = s.split(":")
    return int(hh) + int(mm) / 60.0


def _in_window(h: float, start: str, end: str) -> bool:
    a, b = _parse_hhmm(start), _parse_hhmm(end)
    if a <= b:
        return a <= h < b
    # overnight (p.ej. Asia 19-20 no cruza medianoche aquí)
    return h >= a or h < b


@lru_cache(maxsize=1)
def load_presets() -> dict[str, Any]:
    """Carga YAML si existe; si no, defaults embebidos."""
    path = YAML_PATH if YAML_PATH.is_file() else PROJECT_ROOT / "config" / "zentinel_presets.yaml"
    if not path.is_file():
        return _DEFAULTS
    try:
        import yaml  # type: ignore

        with path.open(encoding="utf-8") as fh:
            raw = yaml.safe_load(fh) or {}
        if not isinstance(raw, dict) or "markets" not in raw:
            return _DEFAULTS
        # PyYAML puede convertir on/off → True/False; normalizar keys killzones
        for mkt in (raw.get("markets") or {}).values():
            if not isinstance(mkt, dict):
                continue
            wt = mkt.get("watchtower") or {}
            kz = wt.get("killzones")
            if isinstance(kz, dict):
                fixed: dict[str, Any] = {}
                for k, v in kz.items():
                    if k is True or k == "on":
                        fixed["on"] = v
                    elif k is False or k == "off":
                        fixed["off"] = v
                    else:
                        fixed[str(k)] = v
                wt["killzones"] = fixed
        return raw
    except Exception:
        return _DEFAULTS


def get_market_preset(asset: str | None) -> dict[str, Any]:
    market = normalize_market(asset)
    markets = load_presets().get("markets") or _DEFAULTS["markets"]
    return dict(markets.get(market) or markets.get("BTC") or {})


def get_fvg_volume(asset: str | None) -> dict[str, Any]:
    return dict(get_market_preset(asset).get("fvg_volume") or {})


def get_watchtower(asset: str | None) -> dict[str, Any]:
    return dict(get_market_preset(asset).get("watchtower") or {})


def ny_local_now(now_utc: datetime | None = None) -> datetime:
    """Datetime en zona NY (o offset -4 fallback)."""
    now = now_utc or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    try:
        from zoneinfo import ZoneInfo

        return now.astimezone(ZoneInfo(NY_TZ_NAME))
    except Exception:
        return now + _NY_OFFSET


def classify_killzone(
    now_utc: datetime | None = None,
    *,
    asset: str | None = "BTC",
) -> dict[str, Any]:
    """Evalúa killzones Watchtower (chart TZ America/New_York).

    Returns keys: in_ny_window, window, killzone_name, killzone_on,
    ny_local, utc, preset_name, off_reason.
    """
    wt = get_watchtower(asset)
    ny = ny_local_now(now_utc)
    h = ny.hour + ny.minute / 60.0
    utc = (now_utc or datetime.now(timezone.utc))
    if utc.tzinfo is None:
        utc = utc.replace(tzinfo=timezone.utc)

    kz = wt.get("killzones") or {}
    for z in kz.get("on") or []:
        if _in_window(h, z["start"], z["end"]):
            name = str(z.get("name") or "NY")
            start_hh = z["start"][:2]
            end_hh = z["end"][:2]
            if name.startswith("NY_AM"):
                window = f"NY AM {start_hh}-{end_hh}"
            elif name.startswith("NY_PM"):
                window = f"NY PM {start_hh}-{end_hh}"
            else:
                window = name
            return {
                "ny_local": ny.strftime("%Y-%m-%d %H:%M"),
                "utc": utc.strftime("%Y-%m-%d %H:%M"),
                "in_ny_window": True,
                "window": window,
                "killzone_name": name,
                "killzone_on": True,
                "preset_name": wt.get("preset_name"),
                "off_reason": None,
            }

    off_reason = None
    for z in kz.get("off") or []:
        if _in_window(h, z["start"], z["end"]):
            off_reason = str(z.get("name") or "OFF")
            break

    return {
        "ny_local": ny.strftime("%Y-%m-%d %H:%M"),
        "utc": utc.strftime("%Y-%m-%d %H:%M"),
        "in_ny_window": False,
        "window": f"FUERA_NY ({off_reason})" if off_reason else "FUERA_NY",
        "killzone_name": off_reason or "FUERA",
        "killzone_on": False,
        "preset_name": wt.get("preset_name"),
        "off_reason": off_reason,
    }


def relative_volume_ratio(candles: list[dict], period: int) -> float | None:
    """Volumen de la última vela / media de las ``period`` anteriores (excluye última)."""
    if not candles or period < 1:
        return None
    vols = [float(c.get("volume") or 0) for c in candles]
    if len(vols) < period + 1:
        # Usa lo disponible
        if len(vols) < 2:
            return None
        window = vols[:-1]
        avg = sum(window) / len(window) if window else 0.0
    else:
        window = vols[-(period + 1) : -1]
        avg = sum(window) / period
    if avg <= 0:
        return None
    return vols[-1] / avg


def classify_volume(
    candles: list[dict],
    *,
    asset: str | None = "BTC",
) -> dict[str, Any]:
    """Clasifica volumen relativo con umbrales del preset. Nunca es trigger."""
    fv = get_fvg_volume(asset)
    period = int(fv.get("period") or 48)
    ratio = relative_volume_ratio(candles, period)
    high = float(fv.get("high") or 1.7)
    extreme = float(fv.get("extreme") or 2.6)
    low = float(fv.get("low") or 0.75)
    very_low = float(fv.get("very_low") or 0.45)

    if ratio is None:
        band = "n/d"
        confluence = "neutral"
        note = "sin volumen suficiente"
    elif ratio >= extreme:
        band = "extremo"
        confluence = "strong_filter"
        note = f"vol×{ratio:.2f} ≥ extremo {extreme}"
    elif ratio >= high:
        band = "alto"
        confluence = "positive_filter"
        note = f"vol×{ratio:.2f} ≥ alto {high}"
    elif ratio <= very_low:
        band = "muy_bajo"
        confluence = "negative_filter"
        note = f"vol×{ratio:.2f} ≤ muy_bajo {very_low}"
    elif ratio <= low:
        band = "bajo"
        confluence = "soft_negative"
        note = f"vol×{ratio:.2f} ≤ bajo {low}"
    else:
        band = "normal"
        confluence = "neutral"
        note = f"vol×{ratio:.2f} en rango normal"

    return {
        "ratio": ratio,
        "band": band,
        "confluence": confluence,
        "note": note,
        "period": period,
        "thresholds": {
            "high": high,
            "extreme": extreme,
            "low": low,
            "very_low": very_low,
        },
        "preset_name": fv.get("preset_name"),
        "role": fv.get("role") or "confluence_filter",
        "never_trigger": True,
    }


def volume_confluence_points(vol: dict | None) -> tuple[float, float, str]:
    """Puntos (score, max) para compute_confluencia_setup. Soft filter."""
    if not vol or vol.get("band") in (None, "n/d"):
        return 0.0, 0.0, ""
    band = vol.get("band")
    if band == "extremo":
        return 2.0, 2.0, f"Vol {band}"
    if band == "alto":
        return 1.5, 2.0, f"Vol {band}"
    if band == "normal":
        return 1.0, 2.0, "Vol normal"
    if band == "bajo":
        return 0.5, 2.0, "Vol bajo"
    if band == "muy_bajo":
        return 0.0, 2.0, "Vol muy bajo"
    return 0.0, 2.0, ""


def zentinel_chart_note(asset: str | None, session: dict | None = None) -> str:
    """Nota corta para título/subtítulo de chart (sin saturar)."""
    m = normalize_market(asset)
    fv = get_fvg_volume(m)
    wt = get_watchtower(m)
    win = (session or {}).get("window") or "n/d"
    return (
        f"{fv.get('preset_name')} · {wt.get('preset_name')} · KZ {win} · "
        f"vol filtro (no trigger)"
    )


def zentinel_report_lines(asset: str | None, data: dict | None = None) -> list[str]:
    """Bloque markdown breve para Advanced / High."""
    m = normalize_market(asset)
    fv = get_fvg_volume(m)
    wt = get_watchtower(m)
    data = data or {}
    ses = data.get("session") or {}
    vol = data.get("zentinel_volume") or {}
    ratio = vol.get("ratio")
    ratio_s = f"{ratio:.2f}×" if isinstance(ratio, (int, float)) else "n/d"
    lines = [
        "### Zentinel (presets TV → stack local)",
        "",
        f"- **FVG+Vol:** `{fv.get('preset_name')}` — alto {fv.get('high')} / "
        f"extremo {fv.get('extreme')} / bajo {fv.get('low')} / muy bajo {fv.get('very_low')} "
        f"/ período {fv.get('period')} · **rol: filtro, nunca trigger**",
        f"- **Watchtower:** `{wt.get('preset_name')}` — KZ NY only "
        f"(08-10 · 10-11 · 14-16) · ahora **{ses.get('window', 'n/d')}**",
        f"- **Vol relativo:** {ratio_s} → banda **{vol.get('band', 'n/d')}** "
        f"({vol.get('note', '')})",
        f"- **Bias table:** avg {wt.get('bias_table', {}).get('avg', 3)} · "
        f"neutral {wt.get('bias_table', {}).get('neutral_pct', '?')}%",
        "- Checklist TV manual (stack no lee indicadores en vivo).",
        "",
    ]
    return lines


def attach_zentinel_to_data(data: dict, *, asset: str | None = None) -> dict:
    """Enriquece ``data`` con volumen clasificado + meta presets (muta y retorna)."""
    market = normalize_market(asset or data.get("asset_label") or data.get("symbol"))
    m5 = data.get("m5") or []
    vol = classify_volume(m5, asset=market)
    data["zentinel_volume"] = vol
    data["zentinel"] = {
        "market": market,
        "fvg_volume_preset": get_fvg_volume(market).get("preset_name"),
        "watchtower_preset": get_watchtower(market).get("preset_name"),
        "role_note": load_presets().get("role_note") or _DEFAULTS["role_note"],
    }
    # Refresca sesión con killzones si falta detalle
    ses = data.get("session")
    if isinstance(ses, dict) and "killzone_on" not in ses:
        # Mantén ny_local/utc existentes; solo añade flags si vienen de legacy
        pass
    return data
