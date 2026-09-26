"""Pip / point equivalents for daytrader SL/TP clamps (shared BTC / US30 / XAUUSD).

Not classic forex pips for every market — project convention:

| Market  | 1 pip =              | Max SL 60 pips = |
|---------|----------------------|------------------|
| BTC     | 1.0 USD (price pt)   | 60 USD           |
| US30    | 1.0 index point      | 60 pts           |
| XAUUSD  | 0.10 USD/oz (XAU pip)| 6.00 USD/oz      |

Gold uses the common CFD pip (0.1); BTC/US30 treat 1 price point as 1 pip
(aligned with cash-mgmt / OCR “pips ≈ pts”). Clamp SL to ≤60 pips and rebuild
TP at R:R 1:2 so overlays stay coherent after the clamp.
"""
from __future__ import annotations

from typing import Any

MAX_SL_PIPS = 60
DEFAULT_RR = 2.0

# Price units per 1 pip
PIP_SIZE: dict[str, float] = {
    "BTC": 1.0,
    "BTCUSDT": 1.0,
    "US30": 1.0,
    "DJ30": 1.0,
    "XAUUSD": 0.10,
    "GOLD": 0.10,
    "GC=F": 0.10,
}


def normalize_asset(asset: str | None) -> str:
    key = (asset or "BTC").strip().upper()
    aliases = {
        "BTCUSD": "BTC",
        "XAU": "XAUUSD",
        "YM=F": "US30",
        "YM": "US30",
    }
    return aliases.get(key, key)


def pip_size(asset: str | None) -> float:
    key = normalize_asset(asset)
    return float(PIP_SIZE.get(key, 1.0))


def max_sl_distance(asset: str | None, max_pips: int = MAX_SL_PIPS) -> float:
    return float(max_pips) * pip_size(asset)


def asset_from_data(data: dict[str, Any] | None) -> str:
    if not data:
        return "BTC"
    for key in ("asset_label", "asset", "symbol_label", "market"):
        val = data.get(key)
        if val:
            return normalize_asset(str(val))
    sym = str(data.get("symbol") or data.get("ml_symbol") or "BTC")
    return normalize_asset(sym)


def clamp_sl_tp(
    entry: float,
    sl: float,
    tp: float | None,
    direction: str,
    asset: str | None,
    *,
    rr: float = DEFAULT_RR,
    max_pips: int = MAX_SL_PIPS,
) -> tuple[float, float, float, bool]:
    """Clamp |entry−SL| to max_pips and rebuild TP at `rr` (default 1:2).

    Returns (sl, tp, risk, clamped).
    """
    max_risk = max_sl_distance(asset, max_pips=max_pips)
    risk = abs(float(entry) - float(sl))
    clamped = False
    if risk > max_risk + 1e-12:
        risk = max_risk
        clamped = True
        if direction == "LONG":
            sl = float(entry) - risk
            tp = float(entry) + rr * risk
        elif direction == "SHORT":
            sl = float(entry) + risk
            tp = float(entry) - rr * risk
        else:
            tp = float(tp) if tp is not None else float(entry)
    elif tp is None:
        if direction == "LONG":
            tp = float(entry) + rr * risk
        elif direction == "SHORT":
            tp = float(entry) - rr * risk
        else:
            tp = float(entry)
    else:
        tp = float(tp)
    return float(sl), float(tp), float(risk), clamped


def pull_entry_toward_price(
    entry: float,
    price: float,
    direction: str,
    *,
    blend: float = 0.55,
) -> float:
    """Move limit entry toward last price (daytrader fill closer to spot).

    `blend` in [0,1]: fraction of the gap closed toward `price`.
    Only pulls when price is on the fillable side of the limit (no chase).
    """
    blend = max(0.0, min(1.0, float(blend)))
    if direction == "LONG" and price > entry:
        return float(entry) + (float(price) - float(entry)) * blend
    if direction == "SHORT" and price < entry:
        return float(entry) - (float(entry) - float(price)) * blend
    return float(entry)


def zone_matches_direction(direction: str, ztype: str | None) -> bool:
    """True when S/R type is the structural anchor for that side."""
    z = (ztype or "").lower()
    if direction == "LONG":
        return z == "soporte_debil"
    if direction == "SHORT":
        return z == "resistencia_debil"
    return False


def raw_sl_from_zone(
    entry: float,
    direction: str,
    zone: dict[str, Any] | None,
) -> float:
    """Structural raw SL — only use zone level when type matches direction.

    LONG + resistencia_debil (or unknown) must NOT use level*0.997: that parks
    SL/TP deep under resistance while price sits on it (broken High chart).
    Same for SHORT + soporte. Fallback is a tight % beyond entry (clamp later).
    """
    entry = float(entry)
    level = (zone or {}).get("level")
    ztype = (zone or {}).get("type")
    matched = zone_matches_direction(direction, ztype) and level is not None

    if direction == "SHORT":
        if matched:
            sl = max(float(level), entry) * 1.002
        else:
            sl = entry * 1.003
        if sl <= entry:
            sl = entry * 1.003
        return float(sl)

    if direction == "LONG":
        if matched:
            sl = min(float(level), entry) * 0.998
        else:
            sl = entry * 0.997
        if sl >= entry:
            sl = entry * 0.997
        return float(sl)

    return entry


def raw_entry_from_zone(
    price: float,
    direction: str,
    zone: dict[str, Any] | None,
    *,
    zone_pct: float = 0.0009,
    entry_ratio: float = 0.18,
    blend: float = 0.55,
) -> tuple[float, float | None, float | None]:
    """Daytrader entry + zone band.

    Matching S/R → retest band on the level. Mismatch (e.g. LONG at resistencia)
    → entry near spot so SL/TP stay actionable; zone_lo/hi still mark the ref.
    Returns (entry, zone_lo, zone_hi).
    """
    price = float(price)
    level = (zone or {}).get("level")
    ztype = (zone or {}).get("type")
    if level is None or direction not in ("LONG", "SHORT"):
        return price, None, None

    level = float(level)
    matched = zone_matches_direction(direction, ztype)

    if direction == "SHORT":
        zone_lo = level * (1 - zone_pct)
        zone_hi = level
        if matched:
            entry = level - (level - zone_lo) * entry_ratio
        else:
            entry = price
        entry = pull_entry_toward_price(entry, price, direction, blend=blend)
        return float(entry), float(zone_lo), float(zone_hi)

    # LONG
    zone_lo = level
    zone_hi = level * (1 + zone_pct)
    if matched:
        entry = level + (zone_hi - level) * entry_ratio
    else:
        entry = price
    entry = pull_entry_toward_price(entry, price, direction, blend=blend)
    return float(entry), float(zone_lo), float(zone_hi)


def actual_rr(entry: float | None, sl: float | None, tp: float | None) -> float | None:
    """Realized R:R from levels; None if incomplete / zero risk."""
    if entry is None or sl is None or tp is None:
        return None
    risk = abs(float(entry) - float(sl))
    if risk <= 1e-12:
        return None
    return abs(float(tp) - float(entry)) / risk
