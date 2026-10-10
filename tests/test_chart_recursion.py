"""Regresión: «maximum recursion depth exceeded» al generar gráficos (capturas / resultado / señal).

Causa: matplotlib interpreta como mathtext los textos con `$…$`. Los gráficos pintan importes en $ y
textos externos (comentario/motivo de cierre MT5, notas) → ValueError o RecursionError en el parser.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

import matplotlib
import pytest

from app.views import trade_outcome_chart as toc
from app.views.mpl_safe import MAX_TEXT_LEN, safe_text
from app.views.trade_outcome_chart import TradeOutcome, render_outcome_chart

T0 = datetime(2026, 10, 1, 16, 55, tzinfo=timezone.utc)

# Disparan RecursionError en el parser mathtext de matplotlib si `text.parse_math` está activo.
NESTED_BRACES = "$ " + "{" * 600 + " $"
NESTED_SQRT = "$" + "\\sqrt{" * 120 + "x" + "}" * 120 + "$"
PARSE_ERROR_USD = "+$572 (+0.68%) · -$300 (-0.4%)"  # ValueError (ParseException) en BTC


def _c(i: int, low: float, high: float) -> dict:
    mid = (low + high) / 2
    return {"open_time": T0 + timedelta(minutes=5 * i), "open": mid, "high": high, "low": low, "close": mid}


def _candles():
    pre = [_c(i - 40, 100 + (i % 5) * 0.3, 101 + (i % 5) * 0.3) for i in range(40)]
    post = [_c(i, lo, hi) for i, (lo, hi) in enumerate(
        [(99.5, 101), (99.8, 103), (102, 103.8), (101, 102), (100, 101), (99, 100)])]
    return pre, post


@pytest.fixture(autouse=True)
def _mathtext_on_like_fresh_process(monkeypatch):
    """Un proceso nuevo arranca con mathtext activo: el código del gráfico debe apagarlo él mismo."""
    monkeypatch.setitem(matplotlib.rcParams, "text.parse_math", True)


@pytest.mark.parametrize("hostile", [NESTED_BRACES, NESTED_SQRT, PARSE_ERROR_USD], ids=["llaves", "sqrt", "usd"])
def test_outcome_chart_with_hostile_text_renders_png(tmp_path, hostile):
    pre, post = _candles()
    trades = [
        toc.RealExecution(entry=100.2, exit=99.4, open_time=T0 + timedelta(minutes=1),
                          close_time=T0 + timedelta(minutes=3), sl=98.0, label=hostile,
                          pnl_usd=-2.42, close_reason=hostile),
        toc.RealExecution(entry=100.5, exit=102.9, open_time=T0 + timedelta(minutes=6),
                          close_time=T0 + timedelta(minutes=24), sl=98.3, tp=104.5, label="duplicada",
                          pnl_usd=11.74, close_reason=hostile),
    ]
    out = tmp_path / "r.png"
    render_outcome_chart(pre, post, TradeOutcome("sl", 0, 1), out, asset="BTCUSD", direction="LONG",
                         entry=100.0, sl=98.0, tp=104.0, dec=2, signal_time=T0, market_entry=True,
                         note=hostile, dpi=60, trades=trades)
    assert out.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
    assert matplotlib.rcParams["text.parse_math"] is False


@pytest.mark.parametrize("hostile", [NESTED_BRACES, NESTED_SQRT, PARSE_ERROR_USD], ids=["llaves", "sqrt", "usd"])
def test_signal_chart_with_hostile_note_renders_png(tmp_path, hostile):
    from app.views.trade_chart import render_trade_chart
    from tests.test_trade_chart import _m5

    m5 = _m5(100, base=67000.0)
    price = m5[-1]["close"]
    opt = {"valid": True, "direction": "LONG", "dec": 2, "entry": price, "sl": price - 60, "tp": price + 120}
    data = {"m5": m5, "price": price, "price_decimals": 2, "chart_verdict": "ESPERAR",
            "generated": "2026-09-30 15:20", "session": {"in_ny_window": True, "window": "NY AM 10-11"}}
    out = tmp_path / "s.png"
    render_trade_chart(data, opt, out, asset="BTC", dpi=60, callout=hostile, zone_edges=(None, None), note=hostile)
    assert out.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_trades_json_sanitizes_external_text():
    raw = json.dumps([{"label": NESTED_BRACES * 3, "entry": 1.0, "exit": 2.0, "closeReason": "\x00ok\x07" * 200}])
    (trade,) = toc.trades_from_json(raw)
    assert len(trade.label) <= MAX_TEXT_LEN
    assert "\x00" not in trade.close_reason and "\x07" not in trade.close_reason
    assert len(trade.close_reason) <= MAX_TEXT_LEN


def test_trades_json_deep_nesting_is_a_clean_value_error():
    deep = "[" * 100_000 + "]" * 100_000  # json.loads recursivo → RecursionError sin la guarda
    with pytest.raises(ValueError, match="demasiado"):
        toc.trades_from_json(deep)
    with pytest.raises(ValueError, match="máximo"):
        toc.trades_from_json(json.dumps([{"entry": 1, "exit": 2}] * (toc.MAX_TRADES + 1)))


def test_trades_json_ignores_non_object_items():
    assert toc.trades_from_json(json.dumps([[[]], 5, None, "x", {"entry": 1, "exit": 2}]))[0].entry == 1.0


def test_safe_text_basics():
    assert safe_text(None) == ""
    assert safe_text("a\x00b") == "ab"
    assert safe_text("x" * 1000).endswith("…") and len(safe_text("x" * 1000)) == MAX_TEXT_LEN


def test_error_payload_recursion_is_clean_and_keeps_detail():
    payload = toc.error_payload(RecursionError("maximum recursion depth exceeded"))
    assert payload["ok"] is False and payload["code"] == toc.RECURSION_CODE
    assert "maximum recursion" not in payload["error"] and payload["detail"].startswith("maximum recursion")


def test_cli_recursion_error_prints_json_and_exits_1(tmp_path, capsys, monkeypatch):
    def boom(*_a, **_k):
        raise RecursionError("maximum recursion depth exceeded")

    monkeypatch.setattr(toc, "evaluate_signal", boom)
    code = toc.main(["--market", "btc", "--signal-time", "2026-10-07T13:46:00Z", "--entry", "100",
                     "--sl", "98", "--tp", "104", "--out", str(tmp_path / "x.png")])
    captured = capsys.readouterr()
    assert code == 1
    result = json.loads(captured.out.strip().splitlines()[-1])
    assert result["code"] == toc.RECURSION_CODE and result["ok"] is False
