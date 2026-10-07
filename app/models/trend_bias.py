"""Tendencia H1 actual → bias a forzar (-Bullish / -Bearish) en la corrida de señal.

Mismo criterio que el «Bias H1 (EMA20/50)» del reporte (`h1_bias`). Cuando ese criterio
estricto sale NEUTRAL (EMAs y precio no alineados), desempata con la posición EMA20 vs
EMA50 y, si aún no hay dato, con la pendiente de la EMA20 (últimas 3 velas).
Solo sin datos suficientes queda NEUTRAL: la corrida no fuerza bias.
"""
from __future__ import annotations

from app.models.market_analysis_core import ema, h1_bias

BULLISH = "BULLISH"
BEARISH = "BEARISH"
NEUTRAL = "NEUTRAL"

LABELS = {BULLISH: "ALCISTA", BEARISH: "BAJISTA", NEUTRAL: "NEUTRAL"}
FLAGS = {BULLISH: "bullish", BEARISH: "bearish"}


def _last(values: list[float | None], back: int = 1) -> float | None:
    return values[-back] if len(values) >= back else None


def decide_trend_bias(h1: list[dict]) -> dict:
    """Bias H1 actual: {bias, flag, label, method, strict, ema20, ema50, close, slope}."""
    closes = [float(c["close"]) for c in h1 or []]
    strict = h1_bias(h1) if closes else NEUTRAL
    e20 = ema(closes, 20)
    e50 = ema(closes, 50)
    e20_last, e50_last = _last(e20), _last(e50)
    e20_prev = _last(e20, 4)
    slope = closes[-1] - closes[-4] if len(closes) >= 4 else 0.0

    if strict in (BULLISH, BEARISH):
        bias, method = strict, "h1_bias"
    elif e20_last is not None and e50_last is not None and e20_last != e50_last:
        bias, method = (BULLISH if e20_last > e50_last else BEARISH), "ema20_vs_ema50"
    elif e20_last is not None and e20_prev is not None and e20_last != e20_prev:
        bias, method = (BULLISH if e20_last > e20_prev else BEARISH), "ema20_slope"
    else:
        bias, method = NEUTRAL, "sin_datos"

    return {
        "bias": bias,
        "flag": FLAGS.get(bias),
        "label": LABELS[bias],
        "method": method,
        "strict": strict,
        "ema20": e20_last,
        "ema50": e50_last,
        "close": closes[-1] if closes else None,
        "slope": slope,
        "bars": len(closes),
    }
