"""Captura automática del resultado: detección TP/SL con velas M5 reales y gráfico posterior."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

import pytest

from app.views import trade_outcome_chart as toc
from app.views.trade_outcome_chart import (
    OutcomeDataError,
    TradeOutcome,
    align_shift,
    detect_outcome,
    infer_direction,
    outcome_message,
    render_outcome_chart,
)

T0 = datetime(2026, 10, 1, 16, 55, tzinfo=timezone.utc)


def _c(i: int, low: float, high: float, o: float | None = None, c: float | None = None) -> dict:
    o = (low + high) / 2 if o is None else o
    c = (low + high) / 2 if c is None else c
    return {"open_time": T0 + timedelta(minutes=5 * i), "open": o, "high": high, "low": low, "close": c}


def _seq(*ranges: tuple[float, float]) -> list[dict]:
    return [_c(i, lo, hi) for i, (lo, hi) in enumerate(ranges)]


LONG = {"direction": "LONG", "entry": 100.0, "sl": 98.0, "tp": 104.0}
SHORT = {"direction": "SHORT", "entry": 100.0, "sl": 102.0, "tp": 96.0}


class TestInferDirection:
    def test_long_short_and_incoherent(self):
        assert infer_direction(100, 98, 104) == "LONG"
        assert infer_direction(100, 102, 96) == "SHORT"
        assert infer_direction(100, 98, 97) is None


class TestMarketEntry:
    def test_long_tp_first(self):
        out = detect_outcome(_seq((99.5, 101), (100, 103), (102, 104.2)), **LONG,
                             ref_price=100.0, market_entry=True)
        assert out == TradeOutcome("tp", 0, 2)

    def test_long_sl_first(self):
        out = detect_outcome(_seq((99.5, 101), (97.9, 100), (100, 105)), **LONG,
                             ref_price=100.0, market_entry=True)
        assert (out.status, out.fill_index, out.exit_index) == ("sl", 0, 1)

    def test_short_tp_first(self):
        out = detect_outcome(_seq((99, 101), (95.9, 99)), **SHORT, ref_price=100.0, market_entry=True)
        assert (out.status, out.exit_index) == ("tp", 1)

    def test_short_sl_first(self):
        out = detect_outcome(_seq((99, 101), (100, 102.5), (95, 99)), **SHORT,
                             ref_price=100.0, market_entry=True)
        assert (out.status, out.exit_index) == ("sl", 1)

    def test_both_in_one_candle_is_ambiguous(self):
        out = detect_outcome(_seq((99, 101), (97.5, 104.5)), **LONG, ref_price=100.0, market_entry=True)
        assert (out.status, out.exit_index) == ("ambiguous", 1)

    def test_unresolved(self):
        out = detect_outcome(_seq((99, 101), (99.5, 102)), **LONG, ref_price=100.0, market_entry=True)
        assert (out.status, out.fill_index, out.exit_index) == ("open", 0, None)


class TestLimitEntry:
    def test_long_limit_filled_then_tp(self):
        # precio 101.5, entrada límite 100 por debajo
        out = detect_outcome(_seq((101, 102), (99.8, 101), (101, 104.1)), **LONG,
                             ref_price=101.5, market_entry=False)
        assert out == TradeOutcome("tp", 1, 2)

    def test_long_limit_sl_in_fill_candle_is_sequential_loss(self):
        out = detect_outcome(_seq((101, 102), (97.5, 101)), **LONG, ref_price=101.5, market_entry=False)
        assert (out.status, out.fill_index, out.exit_index) == ("sl", 1, 1)

    def test_long_limit_tp_in_fill_candle_is_ambiguous(self):
        out = detect_outcome(_seq((101, 102), (99.8, 104.5)), **LONG, ref_price=101.5, market_entry=False)
        assert out.status == "ambiguous"

    def test_not_filled_when_tp_reached_first(self):
        out = detect_outcome(_seq((101, 102), (102, 104.5), (99, 101)), **LONG,
                             ref_price=101.5, market_entry=False)
        assert (out.status, out.fill_index, out.exit_index) == ("not_filled", None, 1)
        assert "antes de ejecutar" in out.reason

    def test_not_filled_when_price_never_reaches_entry(self):
        out = detect_outcome(_seq((101, 102), (101.2, 103)), **LONG, ref_price=101.5, market_entry=False)
        assert (out.status, out.fill_index, out.exit_index) == ("not_filled", None, None)

    def test_short_limit_above_price_filled_then_sl(self):
        # SHORT con entrada 100 por encima del precio 98.5
        out = detect_outcome(_seq((98, 99), (98.5, 100.2), (100, 102.1)), **SHORT,
                             ref_price=98.5, market_entry=False)
        assert out == TradeOutcome("sl", 1, 2)

    def test_long_stop_above_price_cancelled_by_sl(self):
        # LONG stop: entrada 100 sobre el precio 99; SL 98 tocado antes
        out = detect_outcome(_seq((98.5, 99.5), (97.8, 99)), **LONG, ref_price=99.0, market_entry=False)
        assert out.status == "not_filled"


def test_align_shift_uses_candle_at_signal_time():
    candles = [_c(-2, 4180, 4186, c=4185.0), _c(-1, 4183, 4190, c=4189.0), _c(0, 4185, 4192)]
    signal = T0 - timedelta(minutes=2)
    assert align_shift(candles, signal, 4163.9) == pytest.approx(4163.9 - 4189.0)
    assert align_shift(candles, signal, None) == 0.0
    assert align_shift(candles, signal, 9000.0) == 0.0  # fuera de rango → sin ajuste


def test_old_signal_reports_yahoo_limit():
    with pytest.raises(OutcomeDataError, match="60 días"):
        toc._yahoo_range(timedelta(days=75))


def test_outcome_message_spanish():
    post = _seq((99, 101), (102, 104.2))
    assert outcome_message(TradeOutcome("tp", 0, 1), post, T0) == "✓ TP alcanzado 17:00 UTC"
    assert outcome_message(TradeOutcome("sl", 0, 1), post, T0).startswith("✗ SL alcanzado")
    assert "no ejecutada" in outcome_message(TradeOutcome("not_filled", reason="x"), post, T0)


@pytest.mark.parametrize("outcome", [TradeOutcome("tp", 1, 3), TradeOutcome("not_filled", None, None)])
def test_render_outcome_chart_writes_png(tmp_path, outcome):
    pre = [_c(i - 40, 100 + (i % 5) * 0.3, 101 + (i % 5) * 0.3) for i in range(40)]
    post = _seq((101, 102), (99.8, 101), (100.5, 102.5), (102, 104.2), (103, 104))
    p = render_outcome_chart(
        pre, post, outcome, tmp_path / "r.png", asset="XAUUSD", direction="LONG",
        entry=100.0, sl=98.0, tp=104.0, dec=2, signal_time=T0, market_entry=False, dpi=60,
    )
    assert p.is_file() and p.stat().st_size > 0


def _stats(outcome, post, params, *, ref_price=100.0, market_entry=True, unit_size=0.1):
    return toc.compute_trade_stats(outcome, post, **params, unit_size=unit_size,
                                   ref_price=ref_price, market_entry=market_entry)


class TestTradeStats:
    def test_long_tp_duration_r_and_excursions(self):
        post = _seq((99.5, 101), (99.0, 103), (102, 104.5))
        s = _stats(TradeOutcome("tp", 0, 2), post, LONG)
        assert s.filled and not s.in_progress
        assert s.duration_min == 10 and s.exit_price == 104.0
        assert s.r_multiple == pytest.approx(2.0) and s.units == pytest.approx(40.0)
        assert s.mfe_r == pytest.approx(2.0)  # recortado al TP aunque la vela lo supere
        assert s.mae_r == pytest.approx(0.5)

    def test_short_sl(self):
        post = _seq((98.5, 100.5), (99, 102.3))
        s = _stats(TradeOutcome("sl", 0, 1), post, SHORT)
        assert s.r_multiple == pytest.approx(-1.0) and s.units == pytest.approx(-20.0)
        assert s.mfe_r == pytest.approx(0.75) and s.mae_r == pytest.approx(1.0)

    def test_short_unresolved_is_floating_at_last_close(self):
        post = [_c(0, 99, 101), _c(1, 98.5, 100.5), _c(2, 98.6, 99.5, c=99.0)]
        s = _stats(TradeOutcome("open", 0, None), post, SHORT)
        assert s.in_progress and s.duration_min == 10 and s.exit_price == 99.0
        assert s.r_multiple == pytest.approx(0.5)
        assert s.mfe_r == pytest.approx(0.75) and s.mae_r == pytest.approx(0.5)

    def test_limit_fill_candle_counts_only_side_beyond_entry(self):
        # LONG límite 100 bajo el precio 101.5: el máximo 102 de la vela de ejecución fue previo
        post = _seq((101, 102), (99.5, 102), (100.2, 101))
        s = _stats(TradeOutcome("open", 1, None), post, LONG, ref_price=101.5, market_entry=False)
        assert s.mfe_r == pytest.approx(0.5) and s.mae_r == pytest.approx(0.25)

    def test_not_filled_and_ambiguous(self):
        post = _seq((101, 102), (102, 104.5))
        assert _stats(TradeOutcome("not_filled", None, 1), post, LONG).filled is False
        amb = _stats(TradeOutcome("ambiguous", 0, 1), _seq((99, 101), (97.5, 104.5)), LONG)
        assert amb.r_multiple is None and amb.exit_price is None
        assert (amb.mfe_r, amb.mae_r) == (pytest.approx(2.0), pytest.approx(1.0))

    def test_payload(self):
        s = _stats(TradeOutcome("tp", 0, 2), _seq((99.5, 101), (99.0, 103), (102, 104.5)), LONG)
        p = toc.stats_payload(s, "pips")
        assert p == {"filled": True, "inProgress": False, "durationMin": 10, "exitPrice": 104.0,
                     "rMultiple": 2.0, "units": 40.0, "unitLabel": "pips", "mfeR": 2.0, "maeR": 0.5}
        assert toc.stats_payload(toc.TradeStats(filled=False), "$") == {"filled": False}


@pytest.mark.parametrize("minutes,text", [(0, "0m"), (35, "35m"), (95, "1h 35m"), (125, "2h 05m"),
                                          (1530, "1d 1h 30m")])
def test_fmt_duration(minutes, text):
    assert toc.fmt_duration(minutes) == text


class TestStatsLines:
    def test_unresolved_short(self):
        s = toc.TradeStats(True, True, 95, 84707.4, 0.48, 85.3, 1.68, 0.22)
        lines = toc.stats_lines(s, TradeOutcome("open", 0, None), direction="SHORT",
                                entry=84792.7, unit_label="$", fmt=".1f")
        assert lines == [
            "SHORT  ·  Duración 1h 35m  ·  en curso",
            "Flotante +0.5R · +85.3 $  ·  MFE +1.7R · MAE −0.2R",
            "Entrada 84792.7 → Actual 84707.4",
        ]

    def test_resolved_loss(self):
        s = toc.TradeStats(True, False, 50, 4157.9, -1.0, -60.0, 0.4, 1.0)
        lines = toc.stats_lines(s, TradeOutcome("sl", 0, 3), direction="LONG",
                                entry=4163.9, unit_label="pips", fmt=".2f")
        assert lines[0] == "LONG  ·  Duración 50m"
        assert lines[1] == "−1.0R · −60.0 pips  ·  MFE +0.4R · MAE −1.0R"
        assert lines[2] == "Entrada 4163.90 → Salida 4157.90"

    def test_not_filled(self):
        lines = toc.stats_lines(toc.TradeStats(filled=False),
                                TradeOutcome("not_filled", None, 1, "TP alcanzado antes de ejecutar la entrada"),
                                direction="LONG", entry=100.0, unit_label="pips", fmt=".2f")
        assert lines == ["LONG  ·  Entrada no ejecutada", "TP alcanzado antes de ejecutar la entrada"]


@pytest.mark.parametrize("outcome,title", [
    (TradeOutcome("tp", 0, 3), "Resultado: TP alcanzado"),
    (TradeOutcome("sl", 0, 1), "Resultado: SL alcanzado"),
    (TradeOutcome("open", 0, None), "Resultado: Sin resolver"),
    (TradeOutcome("ambiguous", 0, 1), "Resultado: Ambiguo"),
    (TradeOutcome("not_filled", None, None, "el precio no llegó a la entrada"), "Resultado: Entrada no ejecutada"),
])
def test_render_title_and_box_text(tmp_path, monkeypatch, outcome, title):
    from app.views import illustrate_high_entry

    seen = {}

    def fake_save(fig, out_path, **_kw):
        seen["title"] = fig._suptitle.get_text()
        seen["texts"] = [t.get_text() for ax in fig.axes for t in ax.texts]
        return out_path

    monkeypatch.setattr(illustrate_high_entry, "savefig_png", fake_save)
    pre = [_c(i - 40, 100 + (i % 5) * 0.3, 101 + (i % 5) * 0.3) for i in range(40)]
    post = _seq((99.5, 101), (97.5, 104.5), (100.5, 102.5), (102, 104.2), (103, 104))
    render_outcome_chart(pre, post, outcome, tmp_path / "r.png", asset="XAUUSD", direction="LONG",
                         entry=100.0, sl=98.0, tp=104.0, dec=2, signal_time=T0, market_entry=True, dpi=60)
    assert seen["title"].endswith(title) and "(" not in seen["title"]
    box = next(t for t in seen["texts"] if t.startswith("LONG"))
    assert "Velas" not in box and "Sin resolver:" not in box


def _render_capture(tmp_path, monkeypatch, outcome, **kw):
    """Renderiza con savefig simulado → (título, textos, rectángulos de la caja real alpha 0.28)."""
    from matplotlib.patches import Rectangle

    from app.views import illustrate_high_entry

    seen = {}

    def fake_save(fig, out_path, **_kw):
        ax = fig.axes[0]
        seen["title"] = fig._suptitle.get_text()
        seen["texts"] = [t.get_text() for a in fig.axes for t in a.texts]
        seen["result_rects"] = [p for p in ax.patches if isinstance(p, Rectangle) and p.get_alpha() == 0.28]
        return out_path

    monkeypatch.setattr(illustrate_high_entry, "savefig_png", fake_save)
    pre = [_c(i - 40, 100 + (i % 5) * 0.3, 101 + (i % 5) * 0.3) for i in range(40)]
    post = _seq((99.5, 101), (99.8, 103), (102, 103.8), (101, 102), (100, 101), (99, 100))
    render_outcome_chart(pre, post, outcome, tmp_path / "r.png", asset="XAUUSD", direction="LONG",
                         entry=100.0, sl=98.0, tp=104.0, dec=2, signal_time=T0, market_entry=True,
                         dpi=60, **kw)
    return seen


REAL_WIN = toc.RealExecution(entry=100.2, exit=103.5, close_time=T0 + timedelta(minutes=12),
                             open_time=T0 + timedelta(minutes=1), sl=97.8, ticket=7)


class TestRealExecution:
    def test_box_ends_at_real_close_candle_with_real_exit_label_and_plan_lines(self, tmp_path, monkeypatch):
        seen = _render_capture(tmp_path, monkeypatch, TradeOutcome("open", 0, None), real=REAL_WIN)
        # 36 velas previas visibles → la vela 2 (cierre 17:07) está en x=38 → la caja acaba en 38.5
        rect = seen["result_rects"][0]
        assert rect.get_x() == pytest.approx(35.5) and rect.get_x() + rect.get_width() == pytest.approx(38.5)
        texts = seen["texts"]
        assert any(t.startswith("Salida 103.50 · +33.0 pips") for t in texts)
        assert "Entrada MT5 100.20" in texts
        assert "TP plan 104.00" in texts and "SL plan 98.00" in texts and "Entrada plan 100.00" in texts
        assert any("Salida MT5 17:07" in t for t in texts)
        assert seen["title"].endswith("Resultado: Ganada en MT5") and "(" not in seen["title"]
        box = next(t for t in texts if t.startswith("LONG"))
        assert "Entrada 100.20 → Salida 103.50  ·  MT5 17:07 UTC" in box
        assert "+1.4R" in box  # (103.5 − 100.2) / (100.2 − 97.8)

    def test_loss_closed_before_sl_shows_real_exit(self, tmp_path, monkeypatch):
        real = toc.RealExecution(entry=100.0, exit=99.1, close_time=T0 + timedelta(minutes=22))
        seen = _render_capture(tmp_path, monkeypatch, TradeOutcome("open", 0, None), real=real)
        assert any(t.startswith("Salida 99.10 · −9.0 pips") for t in seen["texts"])
        assert "SL plan 98.00" not in seen["texts"]  # sin SL real se dibuja el del plan (no se duplica)
        assert seen["title"].endswith("Resultado: Perdida en MT5")

    def test_without_mt5_box_ends_at_detected_exit_labelled_estimated(self, tmp_path, monkeypatch):
        seen = _render_capture(tmp_path, monkeypatch, TradeOutcome("tp", 0, 2))
        assert any("TP alcanzado · cierre estimado 17:05" in t for t in seen["texts"])
        box = next(t for t in seen["texts"] if t.startswith("LONG"))
        assert "cierre estimado 17:05" in box

    def test_realized_r_and_duration(self):
        post = _seq((99.5, 101), (99.8, 103), (102, 103.8))
        s = toc.compute_real_stats(REAL_WIN, post, direction="LONG", sl=97.8, unit_size=0.1)
        assert s.exit_price == 103.5 and s.duration_min == 11 and not s.in_progress
        assert s.r_multiple == pytest.approx(3.3 / 2.4) and s.units == pytest.approx(33.0)
        short = toc.RealExecution(entry=100.0, exit=100.8, close_time=T0 + timedelta(minutes=5))
        assert toc.compute_real_stats(short, post, direction="SHORT", sl=102.0, unit_size=0.1).r_multiple == \
            pytest.approx(-0.4)

    def test_real_message(self):
        assert toc.real_message(REAL_WIN, "LONG", T0) == "✓ Ganada en MT5: salida 103.5 a las 17:07 UTC"
        loss = toc.RealExecution(entry=100.0, exit=100.8, close_time=T0 + timedelta(days=1))
        assert toc.real_message(loss, "SHORT", T0).startswith("✗ Perdida en MT5: salida 100.8 a las 02/10")
        btc = toc.RealExecution(entry=84792.7, exit=84610.17, close_time=T0)
        assert "salida 84610.17 " in toc.real_message(btc, "SHORT", T0)

    def test_price_decimals_keeps_broker_precision(self):
        assert toc.price_decimals(1, 84792.7, 84610.17, 85067.54) == 2
        assert toc.price_decimals(2, 100.0, 103.5) == 2

    def test_candle_index_clamps(self):
        post = _seq((1, 2), (1, 2), (1, 2))
        assert toc.candle_index_at(post, T0 - timedelta(minutes=3)) == 0
        assert toc.candle_index_at(post, T0 + timedelta(minutes=7)) == 1
        assert toc.candle_index_at(post, T0 + timedelta(hours=5)) == 2

    def test_cli_real_args(self):
        args = toc._parse_args(["--market", "btc", "--signal-time", "2026-10-01T20:17:26Z", "--entry", "1",
                                "--sl", "2", "--tp", "0.5", "--out", "x.png", "--real-entry", "84792.7",
                                "--real-exit", "84610.17", "--real-close-time", "2026-10-01T20:54:12.000Z",
                                "--real-ticket", "680126942"])
        real = toc.real_from_args(args)
        assert (real.entry, real.exit, real.ticket) == (84792.7, 84610.17, 680126942)
        assert real.close_time == datetime(2026, 10, 1, 20, 54, 12, tzinfo=timezone.utc)
        args.real_exit = None
        assert toc.real_from_args(args) is None


def test_cli_rejects_incoherent_levels(tmp_path, capsys):
    rc = toc.main(["--market", "xauusd", "--signal-time", "2026-10-01T16:52:34Z", "--entry", "100",
                   "--sl", "98", "--tp", "97", "--out", str(tmp_path / "x.png")])
    assert rc == 1
    assert "incoherentes" in capsys.readouterr().out


AVG_PATH = r"\\.\avgMonFltProxy\348fb67027ee185f"


def _avg_error() -> PermissionError:
    return PermissionError(13, "Permission denied", AVG_PATH)


class TestRenderRetry:
    def test_transient_av_block_is_retried_and_font_caches_cleared(self, monkeypatch):
        cleared = []
        monkeypatch.setattr(toc, "_reset_font_path_caches", lambda: cleared.append(1))
        calls = []

        def render():
            calls.append(1)
            if len(calls) < 3:
                raise _avg_error()
            return "ok.png"

        assert toc.render_with_retry(render, sleep=lambda _s: None) == "ok.png"
        assert len(calls) == 3 and len(cleared) == 2

    def test_persistent_block_raises_file_access_blocked(self, monkeypatch):
        monkeypatch.setattr(toc, "_reset_font_path_caches", lambda: None)
        with pytest.raises(toc.FileAccessBlockedError, match="avgMonFltProxy"):
            toc.render_with_retry(lambda: (_ for _ in ()).throw(_avg_error()), sleep=lambda _s: None)

    def test_other_errors_are_not_retried(self):
        calls = []

        def render():
            calls.append(1)
            raise FileNotFoundError(2, "No such file", "x.ttf")

        with pytest.raises(FileNotFoundError):
            toc.render_with_retry(render, sleep=lambda _s: None)
        assert len(calls) == 1

    def test_reset_font_path_caches_clears_matplotlib_lru(self):
        import matplotlib

        matplotlib.use("Agg")
        from matplotlib import font_manager as fm

        fm.get_font(fm.findfont("DejaVu Sans"))
        assert fm._cached_realpath.cache_info().currsize > 0
        toc._reset_font_path_caches()
        assert fm._cached_realpath.cache_info().currsize == 0
        assert fm._get_font.cache_info().currsize == 0


def test_error_payload_av_block_is_clean_spanish():
    p = toc.error_payload(toc.FileAccessBlockedError(str(_avg_error())))
    assert p["ok"] is False and p["code"] == toc.FILE_BLOCKED_CODE
    assert p["error"].startswith("El antivirus bloqueó") and "}" not in p["error"]
    assert "avgMonFltProxy" in p["detail"]
    assert toc.error_payload(_avg_error())["code"] == toc.FILE_BLOCKED_CODE
    assert toc.error_payload(ValueError("malo")) == {"ok": False, "error": "malo"}


def test_cli_av_block_prints_json_and_traceback(tmp_path, capsys, monkeypatch):
    def boom(*_a, **_k):
        raise toc.FileAccessBlockedError(str(_avg_error()))

    monkeypatch.setattr(toc, "evaluate_signal", boom)
    rc = toc.main(["--market", "btc", "--signal-time", "2026-10-01T20:17:26Z", "--entry", "100",
                   "--sl", "102", "--tp", "96", "--out", str(tmp_path / "x.png")])
    out, err = capsys.readouterr()
    payload = json.loads(out.strip().splitlines()[-1])
    assert rc == 1 and payload["code"] == "file_blocked"
    assert "Traceback" in err
