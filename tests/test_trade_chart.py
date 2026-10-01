"""Tests del gráfico Long/Short compartido (BTC / US30 / XAUUSD) y del piso ATR del SL."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from app.models.market_pips import atr_sl_floor, clamp_sl_tp, m5_atr
from app.views.illustrate_high_entry import create_annotated_entry_chart
from app.views.trade_chart import (
    _stack_tags,
    _time_ticks,
    compute_position_levels,
    format_distance,
    format_rr,
    market_unit,
    position_box_rects,
    resolve_signal_state,
)


def _m5(n: int = 90, base: float = 4200.0, rng: float = 4.0, start: datetime | None = None) -> list[dict]:
    start = start or datetime(2026, 9, 30, 7, 0, tzinfo=timezone.utc)
    out = []
    for i in range(n):
        o = base + (i % 7) - 3
        c = o + (1.0 if i % 2 else -1.0)
        out.append({
            "open_time": start + timedelta(minutes=5 * i),
            "open": o, "close": c, "high": max(o, c) + rng / 2, "low": min(o, c) - rng / 2,
        })
    return out


class TestPositionLevels:
    def test_long_sides_distances_and_rr(self):
        pos = compute_position_levels("LONG", 4317.30, 4308.67, 4334.57, "XAUUSD")
        assert pos["valid"]
        assert pos["sl_ok"]
        assert pos["tp_ok"]
        assert pos["risk"] == pytest.approx(8.63)
        assert pos["reward"] == pytest.approx(17.27)
        assert pos["rr"] == pytest.approx(17.27 / 8.63)
        assert pos["tp_units"] == pytest.approx(172.7)
        assert pos["sl_units"] == pytest.approx(-86.3)

    def test_short_sides(self):
        pos = compute_position_levels("SHORT", 51825.0, 51885.0, 51705.0, "US30")
        assert pos["valid"]
        assert pos["tp_delta"] == pytest.approx(-120.0)
        assert pos["sl_delta"] == pytest.approx(60.0)
        assert pos["rr"] == pytest.approx(2.0)

    def test_wrong_side_is_flagged(self):
        pos = compute_position_levels("LONG", 100.0, 105.0, 110.0, "BTC")
        assert pos["sl_ok"] is False
        assert pos["valid"] is False

    def test_incomplete_returns_none(self):
        assert compute_position_levels("NONE", 1.0, 0.9, 1.2) is None
        assert compute_position_levels("LONG", 1.0, None, 1.2) is None

    @pytest.mark.parametrize("direction,entry,sl,tp", [
        ("LONG", 100.0, 95.0, 110.0),
        ("SHORT", 100.0, 105.0, 90.0),
    ])
    def test_box_rects_on_correct_side(self, direction, entry, sl, tp):
        pos = compute_position_levels(direction, entry, sl, tp, "BTC")
        rects = position_box_rects(pos, 10.0, 38.0)
        tp_x, tp_y, tp_w, tp_h = rects["tp"]
        sl_x, sl_y, sl_w, sl_h = rects["sl"]
        assert tp_x == sl_x == 10.0
        assert tp_w == sl_w == 28.0
        assert tp_h == pytest.approx(10.0)
        assert sl_h == pytest.approx(5.0)
        if direction == "LONG":
            assert tp_y == pytest.approx(entry)  # TP arriba de la entrada
            assert sl_y + sl_h == pytest.approx(entry)  # SL debajo
        else:
            assert tp_y + tp_h == pytest.approx(entry)  # TP debajo
            assert sl_y == pytest.approx(entry)  # SL arriba


class TestFormatting:
    def test_units_per_market(self):
        assert market_unit("XAUUSD").kind == "pips"
        assert market_unit("US30").kind == "pts"
        assert market_unit("BTC").kind == "usd"

    def test_format_distance(self):
        assert format_distance(17.27, market_unit("XAUUSD"), 2, 4317.3) == "+17.27 · +172.7 pips"
        assert format_distance(-60.0, market_unit("US30"), 1, 51825.0) == "−60.0 pts"
        assert format_distance(603.0, market_unit("BTC"), 1, 84000.0) == "+$603 (+0.72%)"

    def test_format_rr(self):
        assert format_rr(2.0) == "R:R 1:2"
        assert format_rr(1.5) == "R:R 1:1.5"
        assert format_rr(None) == "R:R n/d"


class TestHelpers:
    def test_state_stale_forces_no_operar(self):
        assert resolve_signal_state({"data_stale": True, "chart_verdict": "ENTRAR"}, {}) == "NO_OPERAR"

    def test_state_explicit_and_fallback(self):
        assert resolve_signal_state({"chart_verdict": "ESPERAR"}, {}) == "ESPERAR"
        assert resolve_signal_state({}, {"ahora_action": "ENTRAR LONG"}) == "ENTRAR"
        assert resolve_signal_state({}, {"ahora_action": "ESPERAR LONG"}) == "ESPERAR"

    def test_time_ticks_hourly_with_future(self):
        m5 = _m5(24, start=datetime(2026, 9, 30, 12, 0, tzinfo=timezone.utc))
        m5[-1]["open_time"] = m5[-1]["open_time"] + timedelta(seconds=22)
        times = [c["open_time"] for c in m5]
        ticks, labels = _time_ticks(times, len(m5) + 30)
        assert ticks[:2] == [0.0, 12.0]
        assert labels[0] == "12:00\n08:00 NY"
        assert any(t >= len(m5) for t in ticks), "debe haber horas en la zona futura"

    def test_stack_tags_no_overlap_inside_bounds(self):
        tags = [{"y": 100.0}, {"y": 100.2}, {"y": 99.9}, {"y": 150.0}]
        _stack_tags(tags, min_gap=1.0, y_min=90.0, y_max=160.0)
        ys = sorted(t["y_draw"] for t in tags)
        assert all(b - a >= 1.0 - 1e-9 for a, b in zip(ys, ys[1:]))
        assert all(90.0 <= y <= 160.0 for y in ys)


class TestEntryRelationAndStatus:
    # Caso real US30 01-oct: SHORT entrada 51001.3 · SL 51078.9 · TP 50846.3
    POS = compute_position_levels("SHORT", 51001.3, 51078.9, 50846.3, "US30")

    @pytest.mark.parametrize("price,relation", [
        (51009.0, "at_entry"),     # 7.7 pts < ¼ del riesgo (19.4)
        (51040.0, "crossed"),      # sobre la entrada, bajo el SL
        (50931.6, "limit"),        # aún no sube a la entrada
        (51080.0, "beyond_sl"),
        (50840.0, "beyond_tp"),
    ])
    def test_short_relation(self, price, relation):
        from app.views.trade_chart import entry_relation

        assert entry_relation(self.POS, price, 1) == relation

    def test_long_relation_mirror(self):
        from app.views.trade_chart import entry_relation

        pos = compute_position_levels("LONG", 100.0, 90.0, 120.0, "BTC")
        assert entry_relation(pos, 110.0, 1) == "limit"
        assert entry_relation(pos, 94.0, 1) == "crossed"
        assert entry_relation(pos, 89.0, 1) == "beyond_sl"

    def test_relation_text_es_veraz(self):
        from app.views.trade_chart import relation_text

        txt = relation_text("crossed", 51040.0, self.POS, ".1f")
        assert "51040.0" in txt and "sobre la entrada 51001.3" in txt
        assert relation_text("beyond_sl", 51080.0, self.POS, ".1f").startswith("INVALIDADO")
        assert relation_text("at_entry", 51009.0, self.POS, ".1f") is None

    def test_callout_nunca_entrar_si_no_operar(self):
        from app.views.trade_chart import consistent_callout

        out = consistent_callout("NO_OPERAR", "Setup listo → ENTRAR", ["Precio dentro PDH/PDL", "fuera de killzone (FUERA_NY (Asia))"])
        assert "ENTRAR" not in out
        assert out == "No entrar: Precio dentro PDH/PDL · fuera de killzone (FUERA_NY (Asia))"
        assert consistent_callout("ESPERAR", "2M5 OK → ENTRAR", []) == "Esperar"
        assert consistent_callout("ENTRAR", "Setup listo → ENTRAR", ["x"]) == "Setup listo → ENTRAR"
        assert consistent_callout("NO_OPERAR", "Sin 2M5 · revisar bias/SL", ["x"]) == "Sin 2M5 · revisar bias/SL"

    def test_verdict_reasons(self):
        from app.views.trade_chart import verdict_reasons

        data = {"data_stale": True, "session": {"in_ny_window": False, "window": "FUERA_NY (Asia)"}}
        assert verdict_reasons(data, "NO_OPERAR") == ["datos desactualizados", "fuera de killzone (FUERA_NY (Asia))"]
        assert verdict_reasons(data, "ENTRAR") == []
        assert verdict_reasons({"state_reasons": ["guardado"]}, "ESPERAR") == ["guardado"]

    def test_state_lines_posicion_abierta(self):
        from app.views.trade_chart import _state_lines

        lines = _state_lines("NO_OPERAR", "SHORT", "No entrar: x", self.POS, active=True,
                             relation_txt=None, session={}, note="Reajustado con MT5", order_state="open")
        assert lines[1] == "Posición SHORT ABIERTA en MT5 (entrada ejecutada)"
        assert not any("pendiente" in ln for ln in lines)

    def test_ticks_que_chocan_con_etiquetas_se_ocultan(self):
        from app.views.trade_chart import visible_ticks

        assert visible_ticks([50800.0, 50900.0, 51000.0], [50927.6, 50931.6], 10.0) == [True, True, True]
        assert visible_ticks([50800.0, 50900.0, 51000.0], [50905.0, 51001.3], 10.0) == [True, False, False]


class TestAtrFloor:
    def test_m5_atr(self):
        assert m5_atr(_m5(10)) is None
        atr = m5_atr(_m5(40, rng=4.0))
        assert atr is not None
        assert atr >= 4.0

    def test_floor_overrides_pip_cap_when_larger(self):
        # BTC: tope 60 USD, pero 0.8×ATR = 300 → SL a 300, TP 1:2
        sl, tp, risk, clamped = clamp_sl_tp(84_000.0, 83_800.0, None, "LONG", "BTC", min_risk=300.0)
        assert clamped is True
        assert risk == pytest.approx(300.0)
        assert sl == pytest.approx(83_700.0)
        assert tp == pytest.approx(84_600.0)

    def test_floor_short_side(self):
        sl, tp, risk, _ = clamp_sl_tp(84_000.0, 84_010.0, None, "SHORT", "BTC", min_risk=300.0)
        assert sl == pytest.approx(84_300.0)
        assert tp == pytest.approx(83_400.0)

    def test_floor_below_cap_keeps_cap(self):
        sl, tp, risk, clamped = clamp_sl_tp(4300.0, 4280.0, None, "SHORT", "XAUUSD", min_risk=5.0)
        assert clamped is True
        assert risk == pytest.approx(6.0)
        assert sl == pytest.approx(4306.0)

    def test_atr_sl_floor_mult(self):
        m5 = _m5(40)
        assert atr_sl_floor(m5) == pytest.approx(0.8 * m5_atr(m5))


class TestChartSmoke:
    @pytest.mark.parametrize("asset,direction,verdict", [
        ("XAUUSD", "LONG", "ESPERAR"),
        ("US30", "SHORT", "ENTRAR"),
        ("BTC", "LONG", "NO_OPERAR"),
    ])
    def test_png_written(self, tmp_path, asset, direction, verdict):
        m5 = _m5(100, base=4200.0)
        price = m5[-1]["close"]
        long_ = direction == "LONG"
        opt = {
            "valid": True, "direction": direction, "dec": 2, "level": price - 2 if long_ else price + 2,
            "ztype": "soporte_debil" if long_ else "resistencia_debil",
            "entry": price, "sl": price - 6 if long_ else price + 6, "tp": price + 12 if long_ else price - 12,
            "ahora_action": f"{verdict} {direction}", "ahora_2m5": "No",
        }
        data = {
            "m5": m5, "price": price, "price_decimals": 2, "chart_verdict": verdict,
            "generated": "2026-09-30 15:20", "pdh": price + 8, "pdl": price - 30,
            "data_freshness": {"last_candle_utc": "2026-09-30 15:15", "stale": False},
            "session": {"in_ny_window": True, "window": "NY AM 10-11"},
        }
        out = tmp_path / f"{asset.lower()}_m5_chart_annotated.png"
        path = create_annotated_entry_chart(data, opt, out, asset=asset, dpi=80)
        assert path.exists()
        assert path.stat().st_size > 5_000
        assert path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"

    def test_png_without_times_or_levels(self, tmp_path):
        m5 = [{k: v for k, v in c.items() if k != "open_time"} for c in _m5(30)]
        data = {"m5": m5, "price": m5[-1]["close"], "price_decimals": 2}
        path = create_annotated_entry_chart(data, {"direction": "NONE"}, tmp_path / "x.png", asset="XAUUSD", dpi=60)
        assert path.exists()
