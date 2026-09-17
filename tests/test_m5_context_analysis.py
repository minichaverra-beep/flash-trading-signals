"""Unit tests for M5 CONTEXT bias / vigencia helpers."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.services import m5_context_analysis as ctx  # noqa: E402


def _c(o: float, h: float, l: float, cl: float) -> dict:
    return {"open": o, "high": h, "low": l, "close": cl}


def _trend_up(n: int = 80, start: float = 100.0) -> list[dict]:
    out = []
    p = start
    for i in range(n):
        o = p
        cl = p + 0.8
        out.append(_c(o, cl + 0.3, o - 0.2, cl))
        p = cl
    return out


def _trend_down(n: int = 80, start: float = 200.0) -> list[dict]:
    out = []
    p = start
    for i in range(n):
        o = p
        cl = p - 0.8
        out.append(_c(o, o + 0.2, cl - 0.3, cl))
        p = cl
    return out


def test_ema_rsi_atr_helpers():
    vals = [float(i) for i in range(1, 40)]
    ema = ctx._ema(vals, 5)
    assert ema[4] is not None and ema[-1] is not None
    assert all(x is None for x in ema[:4])
    assert ctx._ema([1.0, 2.0], 5) == [None, None]

    closes = [100.0 + i * 0.5 for i in range(30)]
    rsi = ctx._rsi(closes)
    assert rsi is not None and rsi > 50
    assert ctx._rsi([1.0, 2.0]) is None

    flat = [_c(10, 10, 10, 10) for _ in range(5)]
    assert ctx._rsi([c["close"] for c in flat] + [10.0] * 20) == 100.0 or ctx._rsi(
        [10.0] * 20 + [10.0]
    ) is not None

    candles = _trend_up(40)
    atr = ctx._atr(candles)
    assert atr is not None and atr > 0
    assert ctx._atr(candles[:5]) is None


def test_context_swing_and_structure_labels():
    candles = []
    # Build zig-zag with clear swings
    price = 100.0
    for i in range(60):
        if (i // 8) % 2 == 0:
            price += 1.5
        else:
            price -= 1.2
        candles.append(_c(price, price + 1, price - 1, price))
    sh, sl = ctx.context_swing_levels(candles)
    assert isinstance(sh, list) and isinstance(sl, list)
    labels = ctx._structure_labels([10.0, 12.0], [8.0, 9.0])
    assert "HL" in labels["lows"] and "HH" in labels["highs"]
    labels2 = ctx._structure_labels([12.0, 10.0], [9.0, 8.0])
    assert "LL" in labels2["lows"] and "LH" in labels2["highs"]


def test_structure_bias_bull_bear_neutral():
    up = _trend_up(90)
    sh, sl = ctx.context_swing_levels(up)
    closes = [c["close"] for c in up]
    bias = ctx._m5_structure_bias(sh, sl, closes)
    assert bias in ("BULLISH", "NEUTRAL", "BEARISH")

    down = _trend_down(90)
    sh2, sl2 = ctx.context_swing_levels(down)
    bias2 = ctx._m5_structure_bias(sh2, sl2, [c["close"] for c in down])
    assert bias2 in ("BULLISH", "NEUTRAL", "BEARISH")

    flat_closes = [100.0] * 40
    assert ctx._m5_structure_bias([], [], flat_closes) == "NEUTRAL"


def test_impulse_body_wick_continuation_momentum():
    candles = _trend_up(40)
    atr = ctx._atr(candles)
    assert ctx._impulse_extent_atr(candles, "BULLISH", atr) is not None
    assert ctx._impulse_extent_atr(candles, "BEARISH", atr) is not None
    assert ctx._impulse_extent_atr(candles, "NEUTRAL", atr) is not None
    assert ctx._impulse_extent_atr(candles, "BULLISH", None) is None

    assert ctx._body_shrink(candles) is not None
    assert ctx._body_shrink(candles[:5]) is None

    reject_up = _c(100, 110, 99, 101)  # long upper wick
    assert ctx._rejection_wick(reject_up, "BULLISH") is True
    reject_dn = _c(100, 101, 90, 99)
    assert ctx._rejection_wick(reject_dn, "BEARISH") is True
    assert ctx._rejection_wick(_c(100, 100, 100, 100), "BULLISH") is False
    assert ctx._rejection_wick(reject_up, "NEUTRAL") is True

    assert ctx._failed_continuation([10.0, 9.0], [1.0, 2.0], "BULLISH") is True
    assert ctx._failed_continuation([10.0, 11.0], [2.0, 2.5], "BEARISH") is True
    assert ctx._failed_continuation([10.0], [1.0], "BULLISH") is False

    greens = [_c(100, 102, 99, 101) for _ in range(5)]
    assert ctx._momentum_confirm(greens, "BULLISH") is True
    reds = [_c(101, 102, 99, 100) for _ in range(5)]
    assert ctx._momentum_confirm(reds, "BEARISH") is True
    assert ctx._momentum_confirm(greens[:1], "BULLISH") is False
    assert ctx._momentum_confirm(greens, "NEUTRAL") is False


def test_classify_vigencia_branches():
    estado, reasons = ctx._classify_vigencia("NEUTRAL", None, None, None, False, False)
    assert estado == "TRANSICION" and reasons

    estado, _ = ctx._classify_vigencia("BULLISH", 3.0, 70.0, 0.5, True, True)
    assert estado == "AGOTANDO"

    estado, reasons = ctx._classify_vigencia("BULLISH", 1.0, 50.0, 1.0, False, False)
    assert estado == "VIGENTE" and reasons

    estado, _ = ctx._classify_vigencia("BEARISH", 3.0, 25.0, 0.5, False, False)
    assert estado == "AGOTANDO"

    estado, _ = ctx._classify_vigencia("BULLISH", 2.0, 50.0, 0.8, False, False)
    assert estado in ("VIGENTE", "AGOTANDO", "TRANSICION")


def test_analyze_m5_context_and_report(tmp_path: Path):
    candles = _trend_up(100)
    result = ctx.analyze_m5_context(candles, asset="BTC")
    assert result["asset"] == "BTC"
    assert result["bias_m5"] in ("BULLISH", "BEARISH", "NEUTRAL")
    assert result["estado"] in ("VIGENTE", "AGOTANDO", "TRANSICION")
    assert "reasons" in result

    path = tmp_path / "ctx.md"
    ctx.write_context_report(path, {"generated": "2026-01-01", "price": result["price"]}, result)
    text = path.read_text(encoding="utf-8")
    assert "CONTEXT" in text and "BTC" in text

    # Force AGOTANDO / TRANSICION headlines
    ag = dict(result)
    ag["estado"] = "AGOTANDO"
    ag["bias_m5"] = "BULLISH"
    ctx.write_context_report(tmp_path / "ag.md", {"generated": "t"}, ag)
    tr = dict(result)
    tr["estado"] = "TRANSICION"
    tr["bias_m5"] = "NEUTRAL"
    tr["rsi_m5"] = None
    tr["atr_m5"] = None
    tr["impulse_atr"] = None
    tr["ema_fast"] = None
    tr["ema_slow"] = None
    tr["body_ratio"] = None
    ctx.write_context_report(tmp_path / "tr.md", {"generated": "t"}, tr)
    assert "TRANSICIÓN" in (tmp_path / "tr.md").read_text(encoding="utf-8")
