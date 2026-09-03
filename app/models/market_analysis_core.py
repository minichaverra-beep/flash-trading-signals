"""Shared technical analysis helpers for BTC / US30 M5 analyzers."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

NY_OFFSET = timedelta(hours=-4)


def rsi(closes: list[float], period: int = 14) -> float | None:
    if len(closes) < period + 1:
        return None
    gains, losses = [], []
    for i in range(-period, 0):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    avg_g = sum(gains) / period
    avg_l = sum(losses) / period
    if avg_l == 0:
        return 100.0
    rs = avg_g / avg_l
    return 100.0 - (100.0 / (1.0 + rs))


def ema(values: list[float], period: int) -> list[float | None]:
    out: list[float | None] = [None] * len(values)
    if len(values) < period:
        return out
    k = 2 / (period + 1)
    seed = sum(values[:period]) / period
    out[period - 1] = seed
    for i in range(period, len(values)):
        out[i] = values[i] * k + out[i - 1] * (1 - k)
    return out


def swing_levels(candles: list[dict], lookback: int = 3) -> tuple[list[float], list[float]]:
    highs, lows = [], []
    for i in range(lookback, len(candles) - lookback):
        h = candles[i]["high"]
        l = candles[i]["low"]
        if all(h >= candles[i + j]["high"] for j in range(-lookback, lookback + 1) if j != 0):
            highs.append(h)
        if all(l <= candles[i + j]["low"] for j in range(-lookback, lookback + 1) if j != 0):
            lows.append(l)
    return highs[-5:], lows[-5:]


def pdh_pdl(daily_or_h1: list[dict], now_utc: datetime) -> tuple[float | None, float | None]:
    """Approximate PDH/PDL from UTC days using H1 candles."""
    yesterday = (now_utc - timedelta(days=1)).date()
    day_bars = [c for c in daily_or_h1 if c["open_time"].date() == yesterday]
    if not day_bars:
        return None, None
    return max(c["high"] for c in day_bars), min(c["low"] for c in day_bars)


def h1_bias(h1: list[dict]) -> str:
    closes = [c["close"] for c in h1]
    e20 = ema(closes, 20)
    e50 = ema(closes, 50)
    if e20[-1] is None or e50[-1] is None:
        return "NEUTRAL"
    last = closes[-1]
    slope = closes[-1] - closes[-4] if len(closes) >= 4 else 0
    if e20[-1] > e50[-1] and last > e20[-1] and slope > 0:
        return "BULLISH"
    if e20[-1] < e50[-1] and last < e20[-1] and slope < 0:
        return "BEARISH"
    return "NEUTRAL"


def session_flags(now_utc: datetime) -> dict:
    ny = now_utc + NY_OFFSET
    h = ny.hour + ny.minute / 60
    morning = 8.0 <= h < 11.0
    afternoon = 14.0 <= h < 17.0
    return {
        "ny_local": ny.strftime("%Y-%m-%d %H:%M"),
        "utc": now_utc.strftime("%Y-%m-%d %H:%M"),
        "in_ny_window": morning or afternoon,
        "window": "NY AM 08-11" if morning else ("NY PM 14-17" if afternoon else "FUERA_NY"),
    }


def last_n_candle_summary(candles: list[dict], n: int = 6, price_decimals: int = 1) -> list[str]:
    lines = []
    fmt = f".{price_decimals}f"
    for c in candles[-n:]:
        body = c["close"] - c["open"]
        color = "G" if body >= 0 else "R"
        lines.append(
            f"{c['open_time'].strftime('%H:%M')} O={c['open']:{fmt}} H={c['high']:{fmt}} "
            f"L={c['low']:{fmt}} C={c['close']:{fmt}} [{color}]"
        )
    return lines


def two_candle_confirm(candles: list[dict], direction: str) -> bool:
    if len(candles) < 2:
        return False
    a, b = candles[-2], candles[-1]
    if direction == "LONG":
        return a["close"] > a["open"] and b["close"] > b["open"]
    if direction == "SHORT":
        return a["close"] < a["open"] and b["close"] < b["open"]
    return False


def nearest_zone(price: float, swings_h: list[float], swings_l: list[float]) -> dict:
    candidates = [(lvl, "resistencia_debil") for lvl in swings_h] + [
        (lvl, "soporte_debil") for lvl in swings_l
    ]
    if not candidates:
        return {"level": None, "type": None, "dist_pct": None}
    level, ztype = min(candidates, key=lambda x: abs(x[0] - price))
    dist = abs(level - price) / price * 100
    return {"level": level, "type": ztype, "dist_pct": dist}


def suggest_setup(
    price: float,
    bias: str,
    zone: dict,
    rsi_m5: float | None,
    confirm_long: bool,
    confirm_short: bool,
    in_ny: bool,
    pdh: float | None,
    pdl: float | None,
    price_decimals: int = 1,
) -> dict:
    verdict = "OBSERVAR"
    direction = "NONE"
    reasons = []
    red_flags = []

    _ = in_ny  # reloj opcional; no bloquea setup ni fuerza NO_OPERAR

    if bias == "BULLISH":
        direction = "LONG"
    elif bias == "BEARISH":
        direction = "SHORT"
    else:
        red_flags.append("Bias H1 NEUTRAL — no forzar dirección")

    if pdh and pdl:
        if pdl < price < pdh:
            reasons.append(f"Precio dentro PDH/PDL ({pdl:.{price_decimals}f}–{pdh:.{price_decimals}f}) → contexto NEUTRAL posible")
        elif price > pdh:
            reasons.append(f"Precio > PDH {pdh:.{price_decimals}f} → sesgo alcista CRT")
        elif price < pdl:
            reasons.append(f"Precio < PDL {pdl:.{price_decimals}f} → sesgo bajista CRT")

    near_zone = zone["dist_pct"] is not None and zone["dist_pct"] <= 0.15
    if near_zone:
        reasons.append(
            f"Cerca de {zone['type']} @ {zone['level']:.{price_decimals}f} ({zone['dist_pct']:.3f}%)"
        )
    else:
        red_flags.append("Lejos de swing S/R débil (>0.15%) — esperar zona")

    if rsi_m5 is not None:
        if direction == "LONG" and rsi_m5 > 70:
            red_flags.append(f"RSI M5 {rsi_m5:.1f} sobrecomprado — filtro TORYS-like")
        elif direction == "SHORT" and rsi_m5 < 30:
            red_flags.append(f"RSI M5 {rsi_m5:.1f} sobrevendido — filtro TORYS-like")
        else:
            reasons.append(f"RSI M5 {rsi_m5:.1f} no extremo contra dirección")

    if direction == "LONG" and confirm_long:
        reasons.append("2 velas M5 verdes (confirmación)")
    elif direction == "SHORT" and confirm_short:
        reasons.append("2 velas M5 rojas (confirmación)")
    elif direction != "NONE":
        red_flags.append("Sin 2 velas M5 de confirmación")

    hard = [r for r in red_flags if "NEUTRAL" in r or "Lejos" in r or "Sin 2" in r]
    if direction != "NONE" and not hard and near_zone:
        verdict = "SETUP_A+"
    elif direction != "NONE" and len(hard) <= 1 and near_zone:
        verdict = "SETUP_B_ESPERAR"
    elif direction != "NONE":
        verdict = "NO_TRADE"
    else:
        verdict = "OBSERVAR"

    sl = tp = rr = None
    if direction == "LONG" and zone["level"]:
        sl = min(zone["level"], price) * 0.998 if zone["type"] == "soporte_debil" else price * 0.997
        risk = abs(price - sl)
        tp = price + 2 * risk
        rr = 2.0
    elif direction == "SHORT" and zone["level"]:
        sl = max(zone["level"], price) * 1.002 if zone["type"] == "resistencia_debil" else price * 1.003
        risk = abs(sl - price)
        tp = price - 2 * risk
        rr = 2.0

    return {
        "verdict": verdict,
        "direction": direction,
        "reasons": reasons,
        "red_flags": red_flags,
        "sl": sl,
        "tp": tp,
        "rr": rr,
    }
