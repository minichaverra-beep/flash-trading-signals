"""«Tendencia actual»: bias H1 que se fuerza en la corrida (-Bullish / -Bearish)."""
from __future__ import annotations

from app.models.market_analysis_core import h1_bias
from app.models.trend_bias import decide_trend_bias


def _h1(closes: list[float]) -> list[dict]:
    return [{"open": c, "high": c + 1, "low": c - 1, "close": c} for c in closes]


def test_alcista_estricto():
    r = decide_trend_bias(_h1([100 + i for i in range(80)]))
    assert r["bias"] == "BULLISH" and r["flag"] == "bullish" and r["label"] == "ALCISTA"
    assert r["method"] == "h1_bias" and r["strict"] == "BULLISH"


def test_bajista_estricto():
    r = decide_trend_bias(_h1([200 - i for i in range(80)]))
    assert r["bias"] == "BEARISH" and r["flag"] == "bearish" and r["label"] == "BAJISTA"
    assert r["method"] == "h1_bias"


def test_neutral_estricto_desempata_por_ema20_vs_ema50():
    # Tendencia bajista larga y rebote corto: precio > EMA20 (h1_bias NEUTRAL) pero EMA20 < EMA50.
    closes = [200 - i for i in range(80)] + [121, 123, 125, 127]
    h1 = _h1(closes)
    assert h1_bias(h1) == "NEUTRAL"
    r = decide_trend_bias(h1)
    assert r["strict"] == "NEUTRAL"
    assert r["bias"] == "BEARISH" and r["method"] == "ema20_vs_ema50"
    assert r["ema20"] < r["ema50"]


def test_pocas_velas_desempata_por_pendiente_ema20():
    r = decide_trend_bias(_h1([100 + i for i in range(30)]))
    assert r["ema50"] is None
    assert r["bias"] == "BULLISH" and r["method"] == "ema20_slope"


def test_plano_queda_neutral_sin_forzar():
    r = decide_trend_bias(_h1([100.0] * 80))
    assert r["bias"] == "NEUTRAL" and r["flag"] is None and r["method"] == "sin_datos"


def test_sin_velas_neutral():
    r = decide_trend_bias([])
    assert r["bias"] == "NEUTRAL" and r["flag"] is None and r["bars"] == 0
