"""
Suite de reglas high-signal BTC/US30 (2M5, entrada óptima, checklist, 2ª indicación).

Fixtures sintéticas — sin llamadas de red.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.controllers.analyze_btc_m5 import two_candle_confirm  # noqa: E402
from app.services.btc_high_analysis import (  # noqa: E402
    _candle_color,
    _last_n_colors,
    adjust_crt_for_setup_mode,
    adjust_e2_for_setup_mode,
    analyze_breakout,
    compute_advanced_scorecard,
    compute_optimal_entry,
    compute_second_indication,
    filter_m5_from_entry_touch,
    find_m5_index_at_user_entry,
    format_2m5_checklist,
    format_2m5_valid_invalid,
    format_optimal_entry_md,
    optimize_sl_tp_from_past,
    parse_entry_price,
)
from app.models.btc_signal_categories import (  # noqa: E402
    build_advanced_table_rows,
    build_contingency_guidance,
    compute_confluencia_setup,
    format_augmented_categories_md,
    format_contingency_table_rows,
    format_entrada_optima_cell,
    format_entry_usuario_cell,
    format_recomendacion,
    is_esperar_recomendacion,
    score_e1_rules_8,
    winrate_estimate,
)
from app.models.btc_neural_signals import (  # noqa: E402
    gated_prob_toward_neutral,
    neural_gate_factor,
    prob_to_confidence,
)
from app.views.btc_e1_report import collect_red_flags, derive_e1_verdict  # noqa: E402
from app.views.illustrate_high_entry import (  # noqa: E402
    create_annotated_entry_chart,
    format_illustration_md,
    format_salidas_block,
    savefig_png,
    write_entry_overlay_charts,
)


# ---------------------------------------------------------------------------
# Helpers / fixtures
# ---------------------------------------------------------------------------

def _c(o: float, h: float, l: float, cl: float) -> dict:
    """OHLC candle dict."""
    return {"open": o, "high": h, "low": l, "close": cl}


def _red(price: float = 100.0, body: float = 1.0) -> dict:
    return _c(price, price + 0.2, price - body - 0.1, price - body)


def _green(price: float = 100.0, body: float = 1.0) -> dict:
    return _c(price - body, price + 0.2, price - body - 0.1, price)


def _doji(price: float = 100.0) -> dict:
    return _c(price, price + 0.3, price - 0.3, price)


def make_data(
    *,
    price: float = 100_000.0,
    direction: str = "SHORT",
    bias_h1: str = "BEARISH",
    zone_level: float | None = 100_050.0,
    zone_type: str = "resistencia_debil",
    dist_pct: float | None = 0.05,
    confirm_long: bool = False,
    confirm_short: bool = True,
    in_ny: bool = True,
    rsi_m5: float | None = 45.0,
    m5: list[dict] | None = None,
    mode_bias: str = "auto",
    price_decimals: int = 1,
) -> dict:
    """Minimal fake `data` dict for high-signal formatters / optimal entry."""
    zone = {
        "level": zone_level,
        "type": zone_type,
        "dist_pct": dist_pct,
    }
    return {
        "price": price,
        "price_decimals": price_decimals,
        "bias_h1": bias_h1,
        "zone": zone,
        "confirm_long": confirm_long,
        "confirm_short": confirm_short,
        "rsi_m5": rsi_m5,
        "session": {
            "in_ny_window": in_ny,
            "window": "NY AM" if in_ny else "FUERA",
        },
        "setup": {
            "direction": direction,
            "verdict": "SETUP_B_ESPERAR",
            "rr": 2.0,
            "reasons": [],
            "red_flags": [],
        },
        "mode_bias": mode_bias,
        "m5": m5 if m5 is not None else [_red(price), _red(price - 1)],
    }


def make_crt(premium_discount: str = "PREMIUM", pd_reading: str = "BEARISH") -> dict:
    return {
        "premium_discount": premium_discount,
        "pd_reading": pd_reading,
        "h1_state": "COMPLETED_BEAR",
    }


# ---------------------------------------------------------------------------
# 1. 2M5 confirmation (two_candle_confirm + color helpers)
# ---------------------------------------------------------------------------

class TestTwoCandleConfirm:
    """Confirmación de las últimas 2 velas M5."""

    def test_short_ok_two_red(self):
        m5 = [_green(101), _red(100), _red(99)]
        assert two_candle_confirm(m5, "SHORT") is True
        assert _last_n_colors(m5, 2) == ["R", "R"]

    def test_long_ok_two_green(self):
        m5 = [_red(99), _green(100), _green(101)]
        assert two_candle_confirm(m5, "LONG") is True
        assert _last_n_colors(m5, 2) == ["G", "G"]

    def test_short_invalid_green_then_red(self):
        m5 = [_green(100), _red(99)]
        assert two_candle_confirm(m5, "SHORT") is False
        assert _last_n_colors(m5, 2) == ["G", "R"]

    def test_short_invalid_red_then_green(self):
        m5 = [_red(100), _green(101)]
        assert two_candle_confirm(m5, "SHORT") is False
        assert _last_n_colors(m5, 2) == ["R", "G"]

    def test_only_last_two_matter_after_older_rr(self):
        """[R][R] antiguas luego [G][R] — solo cuentan las últimas 2."""
        m5 = [_red(102), _red(101), _green(100), _red(99)]
        assert two_candle_confirm(m5, "SHORT") is False
        assert _last_n_colors(m5, 2) == ["G", "R"]
        # Si las últimas fueran [R][R], sí confirmaría
        m5_ok = [_green(102), _green(101), _red(100), _red(99)]
        assert two_candle_confirm(m5_ok, "SHORT") is True

    def test_doji_treated_as_green_not_short(self):
        """close==open → color G; no confirma SHORT (close < open estricto)."""
        doji = _doji(100.0)
        assert _candle_color(doji) == "G"
        m5 = [_red(101), doji]
        assert two_candle_confirm(m5, "SHORT") is False
        assert _last_n_colors(m5, 2) == ["R", "G"]
        # Doji + doji tampoco SHORT
        assert two_candle_confirm([doji, doji], "SHORT") is False

    def test_single_red_only_fails_short(self):
        m5 = [_red(100)]
        assert two_candle_confirm(m5, "SHORT") is False
        assert two_candle_confirm([], "SHORT") is False

    def test_long_invalid_patterns(self):
        assert two_candle_confirm([_red(100), _green(101)], "LONG") is False
        assert two_candle_confirm([_green(100), _red(99)], "LONG") is False


# ---------------------------------------------------------------------------
# 2. Optimal entry (compute_optimal_entry)
# ---------------------------------------------------------------------------

class TestComputeOptimalEntry:
    """AHORA vs ENTRADA OPTIMIZADA + niveles SL/TP 1:2."""

    def test_short_near_resistance_enter_when_confirm(self):
        data = make_data(
            price=100_040.0,
            direction="SHORT",
            zone_level=100_050.0,
            zone_type="resistencia_debil",
            dist_pct=0.01,
            confirm_short=True,
        )
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        assert opt["valid"] is True
        assert opt["ahora_near"] is True
        assert opt["ahora_2m5"] == "Sí"
        assert "ENTRAR SHORT" in opt["ahora_action"]
        assert "ENTRAR SHORT" in opt["opti_action"]
        assert opt["entry"] is not None
        assert opt["sl"] is not None
        assert opt["tp"] is not None
        assert opt["sl"] > opt["entry"] > opt["tp"]
        assert "invalidacion" in opt and opt["invalidacion"] != "n/d"

    def test_short_near_without_confirm_esperar(self):
        data = make_data(dist_pct=0.05, confirm_short=False, direction="SHORT")
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        assert "ESPERAR" in opt["ahora_action"]
        assert "ENTRAR SHORT" in opt["opti_action"]

    def test_long_near_support_mirrored(self):
        data = make_data(
            price=99_960.0,
            direction="LONG",
            bias_h1="BULLISH",
            zone_level=99_950.0,
            zone_type="soporte_debil",
            dist_pct=0.01,
            confirm_long=True,
            confirm_short=False,
            m5=[_green(99_940), _green(99_960)],
        )
        opt = compute_optimal_entry(data, "LONG", make_crt("DISCOUNT", "BULLISH"), data["zone"])
        assert opt["valid"] is True
        assert opt["ahora_near"] is True
        assert "ENTRAR LONG" in opt["ahora_action"]
        assert opt["tp"] > opt["entry"] > opt["sl"]

    def test_far_from_zone_esperar(self):
        data = make_data(
            dist_pct=0.35,  # > 0.15%
            confirm_short=True,
            direction="SHORT",
        )
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        assert opt["ahora_near"] is False
        assert "ESPERAR" in opt["ahora_action"]
        # OPTI sigue apuntando a entrar en retest
        assert "ENTRAR SHORT" in opt["opti_action"]

    def test_direction_none_graceful(self):
        data = make_data(direction="NONE", confirm_short=False, confirm_long=False)
        opt = compute_optimal_entry(data, "NONE", make_crt(), data["zone"])
        assert opt["valid"] is False
        assert opt["ahora_action"] == "ESPERAR"
        assert opt["entry"] is None
        assert opt["sl"] is None
        assert opt["tp"] is None

    def test_missing_zone_level_graceful(self):
        data = make_data(zone_level=None, dist_pct=None, direction="SHORT")
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        assert opt["valid"] is False
        assert opt["entry"] is None

    def test_rr_approximately_1_to_2(self):
        data = make_data(direction="SHORT", dist_pct=0.05, confirm_short=True)
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        assert opt["rr"] == 2.0
        risk = abs(opt["sl"] - opt["entry"])
        reward = abs(opt["entry"] - opt["tp"])
        assert risk > 0
        assert abs(reward / risk - 2.0) < 1e-9

        data_l = make_data(
            direction="LONG",
            zone_level=99_950.0,
            zone_type="soporte_debil",
            dist_pct=0.05,
            confirm_long=True,
            confirm_short=False,
        )
        opt_l = compute_optimal_entry(data_l, "LONG", make_crt("DISCOUNT"), data_l["zone"])
        risk_l = abs(opt_l["entry"] - opt_l["sl"])
        reward_l = abs(opt_l["tp"] - opt_l["entry"])
        assert abs(reward_l / risk_l - 2.0) < 1e-9


# ---------------------------------------------------------------------------
# 2b. CLI --entry / -Entry parse + override
# ---------------------------------------------------------------------------

class TestParseEntryPrice:
    """European thousands + plain floats for High -Entry."""

    def test_plain_and_decimal(self):
        assert parse_entry_price(53128) == 53128.0
        assert parse_entry_price("53128") == 53128.0
        assert parse_entry_price("53128.0") == 53128.0
        assert parse_entry_price("53128.5") == 53128.5

    def test_european_single_thousands(self):
        assert parse_entry_price("53.128") == 53128.0
        assert parse_entry_price("97.450") == 97450.0

    def test_european_multi_dot_us30(self):
        # User typing 53.12.800 → 53128.0 (US30 European-style thousands)
        assert parse_entry_price("53.12.800") == 53128.0

    def test_comma_decimal(self):
        assert parse_entry_price("53128,5") == 53128.5
        assert parse_entry_price("53.128,50") == 53128.5

    def test_empty_none(self):
        assert parse_entry_price(None) is None
        assert parse_entry_price("") is None
        assert parse_entry_price("   ") is None


class TestEntryOverride:
    """CLI -Entry = Entry usuario; Entrada óptima stays system-computed."""

    def test_override_keeps_optimal_separate_from_user(self):
        data = make_data(direction="SHORT", dist_pct=0.05, confirm_short=True)
        data["entry_override"] = 53128.0
        opt_auto = compute_optimal_entry(
            {**data, "entry_override": None}, "SHORT", make_crt(), data["zone"],
        )
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        assert opt["user_entry"] == 53128.0
        assert opt["entry_manual"] is True
        assert opt["entry_source"] == "manual"
        # System optimal must not be replaced by CLI fill
        assert opt["entry"] == opt_auto["entry"]
        assert opt["entry"] != opt["user_entry"]
        assert opt["sl"] is not None and opt["tp"] is not None
        # SL/TP plan is relative to user fill
        assert opt["sl"] > opt["user_entry"] > opt["tp"]
        risk = abs(opt["sl"] - opt["user_entry"])
        reward = abs(opt["user_entry"] - opt["tp"])
        assert abs(reward / risk - opt["rr"]) < 1e-6
        assert opt.get("sl_tp_source") in ("past", "fallback")
        assert format_entrada_optima_cell(opt, data) == f"{opt['entry']:.1f}"
        assert "(manual" not in format_entrada_optima_cell(opt, data)
        user_cell = format_entry_usuario_cell(opt, data)
        assert user_cell is not None and user_cell.startswith("53128.0 (CLI")
        md = "\n".join(format_optimal_entry_md(opt, data, "SHORT", make_crt()))
        assert "Entry usuario" in md
        assert "53128.0" in md
        assert "Entrada óptima" in md

    def test_override_param_user_differs_from_optimal(self):
        data = make_data(direction="LONG", zone_level=99_950.0, zone_type="soporte_debil",
                         dist_pct=0.05, confirm_long=True, confirm_short=False)
        opt_auto = compute_optimal_entry(data, "LONG", make_crt("DISCOUNT"), data["zone"])
        opt_manual = compute_optimal_entry(
            data, "LONG", make_crt("DISCOUNT"), data["zone"], entry_override=100_100.0,
        )
        assert opt_manual["user_entry"] == 100_100.0
        assert opt_manual["entry"] == opt_auto["entry"]
        assert opt_manual["entry"] != opt_manual["user_entry"]
        assert opt_manual["entry_manual"] is True

    def test_override_long_user_entry_below_zone_keeps_sl_under_user(self):
        """US30 case: Entry usuario 53128 while zone ~53487 — SL under user fill."""
        data = make_data(
            price=53465.0,
            direction="LONG",
            zone_level=53487.0,
            zone_type="soporte_debil",
            dist_pct=0.04,
            confirm_long=False,
            confirm_short=False,
        )
        opt = compute_optimal_entry(
            data, "LONG", make_crt("DISCOUNT"), data["zone"], entry_override=53128.0,
        )
        assert opt["user_entry"] == 53128.0
        assert opt["entry"] != opt["user_entry"]
        assert opt["sl"] < opt["user_entry"] < opt["tp"]
        risk = abs(opt["user_entry"] - opt["sl"])
        reward = abs(opt["tp"] - opt["user_entry"])
        assert abs(reward / risk - opt["rr"]) < 1e-6

    def test_categories_show_both_optimal_and_user(self):
        cats = {
            "precio": "53465.0",
            "entrada_optima": "53495.1",
            "entry_usuario": "53312.0 (CLI · past)",
            "bando_usado": "BULLISH",
            "bando_mercado": "BULLISH",
            "recomendacion": "ESPERAR LONG",
            "confluencia_setup": "MEDIA",
        }
        md = "\n".join(format_augmented_categories_md(cats))
        assert "| Entrada óptima | **53495.1** |" in md
        assert "| Entry usuario | **53312.0 (CLI · past)** |" in md
        assert md.index("| Entrada óptima |") < md.index("| Entry usuario |")


class TestFilterM5FromEntry:
    """Pre-entry M5 candles ignored for past / post-entry context."""

    def test_last_touch_drops_earlier_bars(self):
        m5 = [
            _c(53_000, 53_050, 52_900, 53_020),  # before
            _c(53_020, 53_100, 52_950, 53_080),  # before
            _c(53_080, 53_320, 53_050, 53_300),  # first touch 53312
            _c(53_300, 53_350, 53_250, 53_280),  # also touches 53312
            _c(53_280, 53_310, 53_200, 53_250),  # after (no touch)
        ]
        entry = 53_312.0
        idx = find_m5_index_at_user_entry(m5, entry)
        assert idx == 3  # last interaction with level
        filtered = filter_m5_from_entry_touch(m5, entry)
        assert len(filtered) == 2
        assert filtered[0] is m5[3]

    def test_compute_ignores_pre_entry_m5_for_past_sl_tp(self):
        entry = 53_200.0
        # Pre-entry bar has an extreme low that would pull SL if not filtered.
        # Zone kept above entry so it does not compete as LONG support.
        m5 = [
            _c(53_100, 53_180, 52_400, 53_150),  # deep low before entry (in risk band)
            _c(53_150, 53_220, 53_100, 53_200),  # touches entry
            _c(53_200, 53_260, 53_180, 53_250),  # also touches entry → last touch
            _c(53_250, 53_280, 53_220, 53_270),  # after (no touch of 53200)
        ]
        data = make_data(
            price=53_270.0,
            direction="LONG",
            zone_level=53_450.0,
            zone_type="soporte_debil",
            dist_pct=0.3,
            confirm_long=True,
            confirm_short=False,
            price_decimals=1,
            m5=m5,
        )
        # No swings/PD — force past levels to lean on M5 window
        data["swing_lows"] = []
        data["swing_highs"] = [53_500.0]
        data["pdl"] = None
        data["pdh"] = None
        opt = compute_optimal_entry(
            data, "LONG", make_crt("DISCOUNT"), data["zone"], entry_override=entry,
        )
        assert opt["user_entry"] == entry
        assert opt["entry"] != entry
        assert opt.get("m5_pre_entry_ignored") is True
        assert opt.get("m5_from_entry_len") == 2
        assert opt["m5_entry_touch_index"] == 2  # last touch on full M5 series
        # Unfiltered past would use the 52400 pre-entry low
        past_full = optimize_sl_tp_from_past(
            {**data, "swing_lows": [], "pdl": None, "pdh": None},
            entry, "LONG", make_crt("DISCOUNT"), data["zone"],
        )
        past_filt = optimize_sl_tp_from_past(
            {**data, "m5": filter_m5_from_entry_touch(m5, entry),
             "swing_lows": [], "pdl": None, "pdh": None},
            entry, "LONG", make_crt("DISCOUNT"), data["zone"],
        )
        assert past_full is not None and past_filt is not None
        assert past_full["sl"] < 52_500.0  # pulled by pre-entry extreme
        assert past_filt["sl"] > 52_800.0  # post-entry structure only
        assert opt["sl"] == past_filt["sl"]# ---------------------------------------------------------------------------
# 2c. Past-structure SL/TP with --entry
# ---------------------------------------------------------------------------

class TestOptimizeSlTpFromPast:
    """SL beyond past swings/S-R; TP structural (≥1.5) or 1:2 from that SL."""

    def test_long_sl_below_swing_tp_structural_or_1to2(self):
        entry = 53_200.0
        data = make_data(
            price=53_250.0,
            direction="LONG",
            zone_level=53_100.0,
            zone_type="soporte_debil",
            dist_pct=0.2,
            confirm_long=True,
            confirm_short=False,
            price_decimals=1,
        )
        data["swing_lows"] = [53_050.0, 53_080.0]
        data["swing_highs"] = [53_450.0, 53_500.0]
        data["pdl"] = 52_900.0
        data["pdh"] = 53_600.0
        data["m5"] = [
            _c(53_100, 53_180, 53_050, 53_150),
            _c(53_150, 53_220, 53_100, 53_200),
            _c(53_200, 53_260, 53_180, 53_250),
        ]
        past = optimize_sl_tp_from_past(data, entry, "LONG", make_crt("DISCOUNT"), data["zone"])
        assert past is not None
        assert past["sl"] < entry < past["tp"]
        assert past["sl_tp_source"] == "past"
        assert past["rr"] >= 1.5
        # SL beyond nearest support (zone/swing), not arbitrary %
        assert past["sl"] < 53_100.0
        risk = entry - past["sl"]
        reward = past["tp"] - entry
        assert abs(reward / risk - past["rr"]) < 1e-6

        opt = compute_optimal_entry(
            data, "LONG", make_crt("DISCOUNT"), data["zone"], entry_override=entry,
        )
        assert opt["user_entry"] == entry
        assert opt["entry"] != entry
        assert opt["sl_tp_source"] == "past"
        assert format_entry_usuario_cell(opt, data) == "53200.0 (CLI · past)"
        assert "(manual" not in format_entrada_optima_cell(opt, data)
        md = "\n".join(format_optimal_entry_md(opt, data, "LONG", make_crt("DISCOUNT")))
        assert "estructura pasada" in md.lower() or "past" in md.lower()
        assert "Entry usuario" in md

    def test_short_sl_above_swing_tp_from_structure(self):
        entry = 53_400.0
        data = make_data(
            price=53_350.0,
            direction="SHORT",
            zone_level=53_480.0,
            zone_type="resistencia_debil",
            dist_pct=0.15,
            confirm_short=True,
            confirm_long=False,
            price_decimals=1,
        )
        data["swing_highs"] = [53_500.0, 53_520.0]
        data["swing_lows"] = [53_050.0, 53_100.0]
        data["pdh"] = 53_550.0
        data["pdl"] = 53_000.0
        data["m5"] = [
            _c(53_450, 53_520, 53_400, 53_480),
            _c(53_480, 53_510, 53_420, 53_430),
            _c(53_430, 53_450, 53_380, 53_350),
        ]
        past = optimize_sl_tp_from_past(data, entry, "SHORT", make_crt(), data["zone"])
        assert past is not None
        assert past["tp"] < entry < past["sl"]
        assert past["sl_tp_source"] == "past"
        assert past["sl"] > 53_480.0  # beyond resistance / swing high
        assert past["rr"] >= 1.5

        opt = compute_optimal_entry(
            data, "SHORT", make_crt(), data["zone"], entry_override=entry,
        )
        assert opt["user_entry"] == entry
        assert opt["sl"] > opt["user_entry"] > opt["tp"]
        assert opt["sl_tp_source"] == "past"
        assert format_entry_usuario_cell(opt, data) == "53400.0 (CLI · past)"

    def test_fallback_when_no_safe_structure(self):
        data = make_data(direction="SHORT", dist_pct=0.05, confirm_short=True)
        # No swings/PDH near entry — only far zone → past returns None
        data["swing_highs"] = []
        data["swing_lows"] = []
        data["pdh"] = None
        data["pdl"] = None
        data["m5"] = [_red(100_000), _red(99_999)]
        past = optimize_sl_tp_from_past(
            data, 53_128.0, "SHORT", make_crt(), data["zone"],
        )
        assert past is None
        opt = compute_optimal_entry(
            data, "SHORT", make_crt(), data["zone"], entry_override=53_128.0,
        )
        assert opt["user_entry"] == 53_128.0
        assert opt["sl_tp_source"] == "fallback"
        assert opt["rr"] == 2.0
        assert "1:2" in (format_entry_usuario_cell(opt, data) or "")
        assert "fallback" in (opt.get("sl_tp_note") or "").lower()


# ---------------------------------------------------------------------------
# 3. Checklist 2M5
# ---------------------------------------------------------------------------

class TestFormat2m5Checklist:
    """Checklist de 5 ítems con ✅/❌."""

    def _joined(self, lines: list[str]) -> str:
        return "\n".join(lines)

    def test_all_five_pass_short_ny_near_confirm(self):
        m5 = [
            _c(100_040, 100_055, 100_030, 100_035),
            _c(100_035, 100_045, 100_020, 100_025),
        ]
        data = make_data(
            price=100_030.0,
            direction="SHORT",
            bias_h1="BEARISH",
            zone_level=100_050.0,
            dist_pct=0.05,
            confirm_short=True,
            in_ny=True,
            rsi_m5=45.0,
            m5=m5,
        )
        crt = make_crt(premium_discount="PREMIUM")
        text = self._joined(format_2m5_checklist(data, "SHORT", data["session"], crt))
        assert text.count("✅") >= 5
        assert "Las 5 ✅" in text or "2M5 OK" in text
        assert "Sesión NY activa" not in text
        assert "❌" not in text.replace("## Checklist 2M5", "")

    def test_session_outside_ny_is_info_not_blocking_row(self):
        """Sesión fuera NY = reloj info; no fila bloqueante en checklist 2M5."""
        data = make_data(in_ny=False, direction="SHORT", confirm_short=True, dist_pct=0.05)
        m5 = [
            _c(100_040, 100_055, 100_030, 100_035),
            _c(100_035, 100_045, 100_020, 100_025),
        ]
        data["m5"] = m5
        text = self._joined(
            format_2m5_checklist(data, "SHORT", data["session"], make_crt())
        )
        assert "Sesión NY activa" not in text
        assert "[❌] Sesión NY" not in text
        assert "[❌] Sesión NY activa" not in text
        assert "Reloj (info)" in text or "info" in text.lower()
        # Checklist sigue evaluando zona/2M5 aunque fuera NY
        assert "Cerca de zona" in text
        assert "2 velas M5 confirman SHORT" in text

    def test_missing_2m5_fails_item(self):
        data = make_data(confirm_short=False, direction="SHORT", dist_pct=0.05, in_ny=True)
        text = self._joined(
            format_2m5_checklist(data, "SHORT", data["session"], make_crt())
        )
        assert "2 velas M5 confirman SHORT" in text
        assert "[❌] 2 velas M5 confirman SHORT" in text

    def test_far_from_zone_fails_near_item(self):
        data = make_data(dist_pct=0.40, confirm_short=True, in_ny=True, direction="SHORT")
        text = self._joined(
            format_2m5_checklist(data, "SHORT", data["session"], make_crt())
        )
        assert "Cerca de zona" in text
        assert "[❌] Cerca de zona" in text

    def test_long_all_pass_with_discount(self):
        level = 99_950.0
        m5 = [
            _c(level - 5, level + 10, level - 20, level + 2),
            _c(level + 2, level + 15, level - 5, level + 8),
        ]
        data = make_data(
            price=level + 10,
            direction="LONG",
            bias_h1="BULLISH",
            zone_level=level,
            zone_type="soporte_debil",
            dist_pct=0.04,
            confirm_long=True,
            confirm_short=False,
            in_ny=True,
            rsi_m5=40.0,
            m5=m5,
        )
        text = self._joined(
            format_2m5_checklist(data, "LONG", data["session"], make_crt("DISCOUNT", "BULLISH"))
        )
        assert text.count("✅") >= 5


# ---------------------------------------------------------------------------
# 3b. Session no longer blocks status/recomendación
# ---------------------------------------------------------------------------

class TestSessionNotBlockingStatus:
    def test_score_e1_rules_omits_sesion_ny(self):
        data = make_data(in_ny=False, direction="SHORT", confirm_short=True, dist_pct=0.05)
        ok, total, pct, items = score_e1_rules_8(data, make_crt(), None, None, None)
        labels = [lab for lab, _, _ in items]
        assert "Sesión NY" not in labels
        assert total == 7
        assert ok >= 1

    def test_format_recomendacion_ignores_fuera_ny(self):
        rec = format_recomendacion("ESPERAR", "LONG", session_in_ny=False)
        assert "fin sesión" not in rec
        assert rec == "ESPERAR LONG"
        rec2 = format_recomendacion("ENTRAR", "SHORT", session_in_ny=False)
        assert rec2 == "ENTRAR SHORT"

    def test_suggest_setup_fuera_ny_no_red_flag(self):
        from app.controllers.analyze_btc_m5 import suggest_setup
        from app.models.market_analysis_core import suggest_setup as suggest_us30

        zone = {"level": 100_050.0, "type": "resistencia_debil", "dist_pct": 0.05}
        s = suggest_setup(
            100_040.0, "BEARISH", zone, 45.0, False, True, False, None, None,
        )
        assert not any("NY" in r for r in s["red_flags"])
        s2 = suggest_us30(
            53700.0, "BEARISH",
            {"level": 53735.0, "type": "resistencia_debil", "dist_pct": 0.05},
            45.0, False, True, False, None, None,
        )
        assert not any("NY" in r for r in s2["red_flags"])

    def test_derive_verdict_not_forced_by_fuera_ny(self):
        data = make_data(
            in_ny=False,
            direction="SHORT",
            bias_h1="BEARISH",
            confirm_short=True,
            dist_pct=0.05,
        )
        data["setup"]["verdict"] = "SETUP_A+"
        data["setup"]["rr"] = 2.0
        cats = {"rules_pct": 85, "rules_ok": 6, "rules_total": 7}
        crt = make_crt()
        flags = collect_red_flags(data, crt)
        assert not any("ventana NY" in f or "FUERA" in f.upper() or "fuera NY" in f.lower() for f in flags)
        assert not any(f == "Fuera ventana NY — NO_OPERAR" for f in flags)
        v = derive_e1_verdict(data, cats, crt=crt)
        # Fuera NY ya no fuerza NO_OPERAR; con rules altos + confirm puede ENTRAR/ESPERAR
        assert v in ("ENTRAR", "ESPERAR")


# ---------------------------------------------------------------------------
# 3c. Break vs Reverse
# ---------------------------------------------------------------------------

class TestBreakVsReverse:
    def test_break_detects_held_breakout_not_fakeout(self):
        # Precio por encima de resistencia + 2 verdes = breakout hold
        level = 100_000.0
        m5 = [_green(level + 10), _green(level + 20)]
        data = make_data(
            price=level + 25,
            direction="LONG",
            bias_h1="BULLISH",
            zone_level=level,
            zone_type="resistencia_debil",
            confirm_long=True,
            confirm_short=False,
            m5=m5,
        )
        crt = make_crt("DISCOUNT", "BULLISH")
        crt["fakeout_pdh"] = False
        bo = analyze_breakout(data["price"], m5, data["zone"], crt, data, "LONG")
        assert bo["valid"] is True
        assert "breakout" in bo["kind"]

        # Fakeout: wick above then close back below = NOT break
        data_f = make_data(
            price=level - 50,
            direction="LONG",
            zone_level=level,
            zone_type="resistencia_debil",
            confirm_long=True,
            m5=m5,
        )
        crt_f = make_crt()
        crt_f["fakeout_pdh"] = True
        bo_f = analyze_breakout(data_f["price"], m5, data_f["zone"], crt_f, data_f, "LONG")
        assert bo_f["valid"] is False
        assert bo_f["kind"] == "failed_break_fakeout"

    def test_break_crt_notes_distinct_from_reverse(self):
        data = make_data(direction="SHORT", confirm_short=True, m5=[_red(), _red()])
        data["m5"] = data["m5"]
        crt = make_crt()
        crt["fakeout_pdl"] = True
        br = adjust_crt_for_setup_mode(crt, "break", data)
        rev = adjust_crt_for_setup_mode(crt, "reverse", data)
        assert "breakout" in (br.get("crt_action_e1") or "").lower() or "BREAK" in (br.get("fakeout_note") or "")
        assert "turtle" in (rev.get("crt_action_e1") or "").lower() or "REVERSE" in (rev.get("fakeout_note") or "")
        assert br.get("breakout") is not None
        assert rev.get("breakout") is None

    def test_reverse_operable_with_two_same_direction_candles(self):
        data = make_data(
            direction="SHORT",
            bias_h1="BEARISH",
            confirm_short=True,
            confirm_long=False,
            m5=[_red(), _red()],
            mode_bias="bearish",
        )
        data["mode_setup"] = "reverse"
        e2 = {
            "checks": [("1. x", False, "d")],
            "score": 2,
            "max": 6,
            "eligible": False,
            "verdict": "E2_NO",
            "note": "base",
        }
        out = adjust_e2_for_setup_mode(e2, "reverse", data)
        assert out["eligible"] is True
        assert out["winrate"] is not None
        assert "61" in out["winrate"] or "~" in out["winrate"]
        assert any("2 velas" in c[0] for c in out["checks"])

    def test_reverse_not_operable_without_two_candles(self):
        data = make_data(
            direction="SHORT",
            confirm_short=False,
            confirm_long=False,
            m5=[_green(), _red()],
        )
        data["mode_setup"] = "reverse"
        e2 = {"checks": [], "score": 2, "max": 6, "eligible": False, "verdict": "E2_NO", "note": ""}
        out = adjust_e2_for_setup_mode(e2, "reverse", data)
        assert out["eligible"] is False
        assert out["winrate"] is not None

    def test_break_keeps_e2_not_operable(self):
        data = make_data(direction="LONG", confirm_long=True)
        e2 = {"checks": [], "score": 4, "max": 6, "eligible": True, "verdict": "E2_WATCH", "note": ""}
        out = adjust_e2_for_setup_mode(e2, "break", data)
        assert out["eligible"] is False
        assert out["verdict"] == "E2_NO"
        assert "breakout" in out["note"].lower() or "BREAK" in out["note"]

    def test_reverse_winrate_estimate(self):
        wr, src = winrate_estimate(80, setup_mode="reverse")
        assert "61" in wr or "~61" in wr
        assert "E2" in src or "revers" in src.lower()


# ---------------------------------------------------------------------------
# 4. Segunda indicación (H1 NEUTRAL)
# ---------------------------------------------------------------------------

class TestSecondIndication:
    """compute_second_indication solo cuando bias_h1 == NEUTRAL."""

    def test_returns_hints_when_h1_neutral(self):
        data = make_data(bias_h1="NEUTRAL", direction="NONE")
        crt = make_crt(premium_discount="DISCOUNT", pd_reading="BULLISH")
        dmi = {"bias": "BULL", "note": "DI+ > DI-"}
        struct = {"hl": "HL", "lh": "HH"}
        segunda = compute_second_indication(data, "NEUTRAL", crt, dmi, struct)
        assert segunda
        assert "hints" in segunda
        assert len(segunda["hints"]) == 3
        assert segunda["suggested"] == "LONG"
        assert "explanation" in segunda

    def test_empty_when_h1_bearish(self):
        data = make_data(bias_h1="BEARISH")
        segunda = compute_second_indication(
            data, "BEARISH", make_crt(), {"bias": "BEAR"}, {"hl": "LL", "lh": "LH"}
        )
        assert segunda == {}

    def test_empty_when_h1_bullish(self):
        segunda = compute_second_indication(
            make_data(bias_h1="BULLISH"),
            "BULLISH",
            make_crt("DISCOUNT"),
            {"bias": "BULL"},
            {"hl": "HL", "lh": "HH"},
        )
        assert segunda == {}

    def test_short_suggestion_from_bearish_votes(self):
        segunda = compute_second_indication(
            make_data(bias_h1="NEUTRAL"),
            "NEUTRAL",
            make_crt(premium_discount="PREMIUM", pd_reading="BEARISH"),
            {"bias": "BEAR", "note": "DI- dominante"},
            {"hl": "LL", "lh": "LH"},
        )
        assert segunda["suggested"] == "SHORT"

    def test_cli_bearish_conflict_with_second_long(self):
        """
        Conflicto: CLI/forced BEARISH vs segunda indicación LONG (H1 NEUTRAL).
        Segunda indicación sigue LONG; bando mercado NEUTRAL documenta el conflicto.
        """
        data = make_data(
            bias_h1="NEUTRAL",
            direction="SHORT",
            mode_bias="bearish",
        )
        segunda = compute_second_indication(
            data,
            "NEUTRAL",
            make_crt(premium_discount="DISCOUNT", pd_reading="BULLISH"),
            {"bias": "BULL", "note": "alcista"},
            {"hl": "HL", "lh": "HH"},
        )
        assert segunda["suggested"] == "LONG"
        # CLI fuerza SHORT; segunda dice LONG → conflicto operativo
        assert data["setup"]["direction"] == "SHORT"
        assert data["mode_bias"] == "bearish"
        assert segunda["suggested"] != data["setup"]["direction"]


# ---------------------------------------------------------------------------
# 5. Categories hide ML
# ---------------------------------------------------------------------------

class TestCategoriesHideMl:
    def test_hide_ml_true_omits_ml_prob(self):
        cats = {
            "bando_usado": "AUTO",
            "bando_mercado": "BEARISH",
            "recomendacion": "Esperar",
            "signal_e1": "ESPERAR",
            "direction": "SHORT",
            "ml_prob_win": 0.72,
            "ml_grade": "B",
            "ml_confidence": "med",
            "neural_prob_win": 0.61,
            "neural_grade": "B",
            "neural_confidence": "med",
            "neural_gallery_aligned": True,
        }
        md = "\n".join(format_augmented_categories_md(cats, hide_ml=True))
        assert "ML prob" not in md
        assert "Neural" in md or "galería" in md
        assert "Bando usado" in md

    def test_hide_ml_false_shows_ml(self):
        cats = {
            "bando_usado": "AUTO",
            "bando_mercado": "BULLISH",
            "recomendacion": "Entrar Long",
            "ml_prob_win": 0.81,
            "ml_grade": "A+",
            "ml_confidence": "alta",
        }
        md = "\n".join(format_augmented_categories_md(cats, hide_ml=False))
        assert "ML prob" in md
        assert "81.0%" in md or "81%" in md

    def test_hide_ml_default_false_shows_when_present(self):
        cats = {"ml_prob_win": 0.55, "ml_grade": "C", "ml_confidence": "baja"}
        md = "\n".join(format_augmented_categories_md(cats))
        assert "ML prob" in md


# ---------------------------------------------------------------------------
# 6. Valid/Invalid markdown
# ---------------------------------------------------------------------------

class TestFormat2m5ValidInvalid:
    def test_short_contains_ok_and_invalid_marks(self):
        m5 = [_red(100_040), _red(100_030)]
        data = make_data(
            direction="SHORT",
            dist_pct=0.05,
            zone_level=100_050.0,
            m5=m5,
            confirm_short=True,
        )
        text = "\n".join(format_2m5_valid_invalid(data, "SHORT"))
        assert "✅" in text
        assert "❌" in text
        assert "SHORT OK" in text or "[R][R]" in text
        assert "[G][R]" in text
        assert "INVÁLIDO" in text

    def test_long_contains_ok_and_invalid_marks(self):
        m5 = [_green(99_940), _green(99_960)]
        data = make_data(
            direction="LONG",
            bias_h1="BULLISH",
            zone_level=99_950.0,
            zone_type="soporte_debil",
            dist_pct=0.05,
            confirm_long=True,
            confirm_short=False,
            m5=m5,
        )
        text = "\n".join(format_2m5_valid_invalid(data, "LONG"))
        assert "✅" in text
        assert "❌" in text
        assert "LONG OK" in text or "[G][G]" in text
        assert "[R][G]" in text

    def test_none_direction_no_ok_pattern(self):
        data = make_data(direction="NONE")
        text = "\n".join(format_2m5_valid_invalid(data, "NONE"))
        assert "Sin dirección" in text


# ---------------------------------------------------------------------------
# 7. Edge / smoke / US30 reuse
# ---------------------------------------------------------------------------

class TestEdgeAndSmoke:
    def test_minimal_fake_data_pipeline_short(self):
        """Smoke: optimal + valid/invalid + checklist sin red."""
        data = make_data(direction="SHORT", dist_pct=0.08, confirm_short=True)
        crt = make_crt()
        opt = compute_optimal_entry(data, "SHORT", crt, data["zone"])
        vi = format_2m5_valid_invalid(data, "SHORT")
        cl = format_2m5_checklist(data, "SHORT", data["session"], crt)
        assert opt["valid"] is True
        assert any("✅" in line or "❌" in line for line in vi)
        assert any("Checklist" in line for line in cl)

    def test_us30_style_decimals_same_functions(self):
        """
        US30 reutiliza write_high_signal / compute_optimal_entry.
        Solo cambia price_decimals (típicamente 1) y niveles de precio.
        """
        data = make_data(
            price=42_150.0,
            zone_level=42_180.0,
            dist_pct=0.07,
            direction="SHORT",
            confirm_short=True,
            price_decimals=1,
            m5=[_red(42_160), _red(42_145)],
        )
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        assert opt["valid"] is True
        assert opt["rr"] == 2.0
        assert opt["entry"] is not None
        text = "\n".join(format_2m5_valid_invalid(data, "SHORT"))
        assert "SHORT" in text

    def test_empty_m5_colors_safe(self):
        assert _last_n_colors([], 2) == []
        assert _last_n_colors([_red(100)], 2) == []


# ---------------------------------------------------------------------------
# 8. Ilustrate / annotated chart
# ---------------------------------------------------------------------------

class TestIlustrate:
    def test_ilustrate_default_off_omits_section(self):
        """Sin flag ilustrate → no sección Ilustración en Entrada optimizada."""
        data = make_data(direction="SHORT", dist_pct=0.05, confirm_short=True)
        assert not data.get("ilustrate")
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        md = "\n".join(format_optimal_entry_md(opt, data, "SHORT", make_crt()))
        assert "Ilustración entrada" not in md
        assert "btc_m5_chart_annotated.png" not in md

    def test_ilustrate_true_includes_markdown_image_link(self):
        data = make_data(direction="SHORT", dist_pct=0.05, confirm_short=True)
        data["ilustrate"] = True
        data["annotated_chart_file"] = "btc_m5_chart_annotated.png"
        data["annotated_chart_abs"] = r"D:\Danilo\Trading\Cursor Trading\live\btc_m5_chart_annotated.png"
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        md = "\n".join(format_optimal_entry_md(opt, data, "SHORT", make_crt()))
        assert "## Ilustración entrada (2M5 + óptima)" in md
        assert "![chart](btc_m5_chart_annotated.png)" in md
        assert "live/btc_m5_chart_annotated.png" in md
        assert "Salidas" in md

    def test_ilustrate_false_omits_illustration_section(self):
        data = make_data(direction="SHORT", dist_pct=0.05, confirm_short=True)
        data["ilustrate"] = False
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        md = "\n".join(format_optimal_entry_md(opt, data, "SHORT", make_crt()))
        assert "Ilustración entrada" not in md

    def test_format_illustration_md_relative_link(self):
        lines = format_illustration_md(
            "live/us30_m5_chart_annotated.png",
            absolute_path=r"D:\tmp\us30_m5_chart_annotated.png",
        )
        text = "\n".join(lines)
        assert "![chart](us30_m5_chart_annotated.png)" in text
        assert "live/us30_m5_chart_annotated.png" in text
        assert "## Ilustración entrada" in text
        assert "Salidas" in text
        assert "Ruta absoluta" in text

    def test_format_salidas_block_paths(self):
        text = "\n".join(
            format_salidas_block(
                signal_md=Path("live/btc_m5_high_signal.md"),
                annotated_file="btc_m5_chart_annotated.png",
                annotated_abs=r"D:\Danilo\Trading\Cursor Trading\live\btc_m5_chart_annotated.png",
            )
        )
        assert "## Salidas" in text
        assert "live/btc_m5_high_signal.md" in text
        assert "live/btc_m5_chart_annotated.png" in text
        assert "![chart](btc_m5_chart_annotated.png)" in text
        assert "Chart (abs)" in text

    def test_create_annotated_entry_chart_writes_png(self, tmp_path):
        """Synthetic M5 + optimal entry → PNG file exists."""
        m5 = []
        base = 100_000.0
        for i in range(20):
            o = base + i * 5
            m5.append(_c(o, o + 20, o - 15, o - 8 if i % 2 else o + 10))
        # last 2 red near resistance
        m5[-2] = _red(100_040, body=12)
        m5[-1] = _red(100_028, body=10)
        data = make_data(
            price=100_018.0,
            zone_level=100_050.0,
            dist_pct=0.03,
            confirm_short=True,
            m5=m5,
            direction="SHORT",
        )
        data["generated"] = "2026-09-02 12:00"
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        out = tmp_path / "btc_m5_chart_annotated.png"
        path = create_annotated_entry_chart(data, opt, out, asset="BTC")
        assert path.exists()
        assert path.stat().st_size > 500
        assert path.suffix == ".png"
        assert opt["entry"] is not None
        assert opt["sl"] is not None
        assert opt["tp"] is not None

    def test_write_entry_overlay_charts_main_and_annotated(self, tmp_path):
        """Default High chart path + Ilustrate path both get OPTI overlays."""
        m5 = [_red(100_040, body=12), _red(100_028, body=10)]
        data = make_data(
            price=100_018.0,
            zone_level=100_050.0,
            dist_pct=0.03,
            confirm_short=True,
            m5=m5,
            direction="SHORT",
        )
        data["generated"] = "2026-09-03 12:00"
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        main = tmp_path / "btc_m5_chart.png"
        ann = tmp_path / "btc_m5_chart_annotated.png"
        written = write_entry_overlay_charts(
            data, opt, asset="BTC", main_chart_path=main, annotated_path=ann,
        )
        assert main.exists() and main.stat().st_size > 500
        assert ann.exists() and ann.stat().st_size > 500
        assert written["annotated_file"] == "btc_m5_chart_annotated.png"
        assert "main_chart" in written and "annotated_chart" in written

    def test_create_annotated_entry_chart_us30_asset(self, tmp_path):
        m5 = [_red(42_160), _red(42_145)]
        data = make_data(
            price=42_145.0,
            zone_level=42_180.0,
            dist_pct=0.08,
            confirm_short=True,
            m5=m5,
            price_decimals=1,
        )
        data["generated"] = "2026-09-02 12:00"
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        out = tmp_path / "us30_m5_chart_annotated.png"
        path = create_annotated_entry_chart(data, opt, out, asset="US30")
        assert path.exists()
        assert path.stat().st_size > 200

    def test_savefig_png_atomic_helper(self, tmp_path):
        """Tiny figure via savefig_png → valid PNG (overwrite + same-dir temp)."""
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        out = tmp_path / "us30_m5_chart_annotated.png"
        # Seed an existing file (viewer-lock / overwrite path)
        out.write_bytes(b"old")
        fig = None
        try:
            fig, ax = plt.subplots(figsize=(2, 1), facecolor="#1e1e1e")
            ax.plot([0, 1], [0, 1], color="#4ec9b0")
            path = savefig_png(fig, out, dpi=72, facecolor="#1e1e1e")
        finally:
            if fig is not None:
                plt.close(fig)
        assert path == out
        assert path.exists()
        assert path.stat().st_size > 100
        assert path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
        # No leftover *.png.tmp
        assert not list(tmp_path.glob("*.png.tmp"))


# ---------------------------------------------------------------------------
# 9. Categories: Entrada óptima, Confluencia, Advanced
# ---------------------------------------------------------------------------

class TestCategoriesEntradaConfluenciaAdvanced:
    def _base_cats(self, **extra) -> dict:
        cats = {
            "bando_usado": "BEARISH",
            "bando_mercado": "BEARISH",
            "recomendacion": "ESPERAR SHORT",
            "signal_e1": "ESPERAR",
            "direction": "SHORT",
            "rules_ok": 6,
            "rules_total": 7,
            "rules_pct": 85,
            "winrate": "~82%",
            "winrate_source": "histórico E1 BTC",
            "precio": "100040.0",
            "entrada_optima": "100023.6",
            "confluencia_setup": "MEDIA",
            "confluencia_detalle": "70% · Rules 85%",
        }
        cats.update(extra)
        return cats

    def test_entrada_optima_immediately_after_precio(self):
        md = "\n".join(format_augmented_categories_md(self._base_cats()))
        assert "| Precio |" in md
        assert "| Entrada óptima |" in md
        precio_i = md.index("| Precio |")
        entrada_i = md.index("| Entrada óptima |")
        bando_i = md.index("| Bando usado |")
        assert precio_i < entrada_i < bando_i

    def test_confluencia_is_last_status_row(self):
        cats = self._base_cats(
            neural_prob_win=0.53,
            neural_grade="B",
            neural_confidence="low",
            neural_gallery_aligned=False,
        )
        md = "\n".join(format_augmented_categories_md(cats, hide_ml=True))
        assert "| Confluencia setup | **MEDIA**" in md
        # última fila de datos de la tabla (antes del blank final)
        table_lines = [ln for ln in md.splitlines() if ln.startswith("| ") and "Campo" not in ln and "---" not in ln]
        assert table_lines[-1].startswith("| Confluencia setup |")

    def test_advanced_extras_only_when_advanced_true(self):
        lean = "\n".join(format_augmented_categories_md(self._base_cats()))
        assert "— Advanced —" not in lean
        assert "Dist. a Entry" not in lean

        adv_cats = self._base_cats(
            advanced=True,
            advanced_rows=[
                ("R:R", "1:2"),
                ("Dist. a Entry", "+10.0 pts (0.010%)"),
                ("Estado 2M5", "En zona · falta 2M5"),
            ],
        )
        adv = "\n".join(format_augmented_categories_md(adv_cats))
        assert "— Advanced —" in adv
        assert "Dist. a Entry" in adv
        assert "R:R" in adv
        # Confluencia sigue última
        table_lines = [ln for ln in adv.splitlines() if ln.startswith("| ") and "Campo" not in ln and "---" not in ln]
        assert table_lines[-1].startswith("| Confluencia setup |")

    def test_format_entrada_optima_prefers_entry_number(self):
        opt = {"entry": 77449.3, "opti_zone": "77373.8–77490.0", "dec": 1}
        assert format_entrada_optima_cell(opt) == "77449.3"
        assert format_entrada_optima_cell({"opti_zone": "100–101", "dec": 1}) == "Retest 100–101"
        assert format_entrada_optima_cell(None) == "n/d"

    def test_compute_confluencia_alta_media_nula(self):
        data = make_data(
            direction="SHORT",
            bias_h1="BEARISH",
            mode_bias="bearish",
            dist_pct=0.05,
            confirm_short=True,
        )
        data["mode_setup"] = "break"
        cats = {
            "rules_pct": 85,
            "neural_prob_win": 0.80,
            "neural_gallery_aligned": True,
        }
        level, detail = compute_confluencia_setup(cats, data, crt=make_crt(), e2={"eligible": False})
        assert level in ("ALTA", "MEDIA", "BAJA", "NULA")
        assert level == "ALTA"
        assert "%" in detail

        weak = make_data(direction="NONE", bias_h1="NEUTRAL", dist_pct=0.5, confirm_short=False)
        weak["mode_setup"] = "auto"
        level2, _ = compute_confluencia_setup({"rules_pct": 20}, weak, crt=make_crt(), e2=None)
        assert level2 in ("BAJA", "NULA")

    def test_build_advanced_table_rows_real_metrics_only(self):
        data = make_data(direction="SHORT", dist_pct=0.05, confirm_short=True, price=100_040.0)
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        cats = {
            "rules_ok": 6,
            "rules_total": 7,
            "rules_pct": 85,
            "winrate": "~82%",
            "winrate_source": "E1",
            "bando_usado": "BEARISH",
            "bando_mercado": "BEARISH",
            "neural_prob_win": 0.53,
            "neural_grade": "B",
            "neural_confidence": "low",
        }
        rows = build_advanced_table_rows(cats, data, opt=opt, ext_pct=72, e2={"eligible": False, "verdict": "E2_NO"})
        labels = [r[0] for r in rows]
        assert "R:R" in labels
        assert "Dist. a Entry" in labels
        assert "Estado 2M5" in labels
        assert "Neural grade/conf" in labels
        assert "Score Rules extendido" in labels
        # no inventar ATR si no existe
        assert "ATR" not in labels

    def test_write_high_signal_us30_categories_advanced_salidas(self, tmp_path):
        """US30 High: Precio→Entrada óptima, Confluencia última, Advanced, Salidas us30 paths."""
        from app.services.btc_high_analysis import write_high_signal
        from app.models.btc_signal_categories import verdict_to_signal

        data = make_data(
            price=42_145.0,
            zone_level=42_180.0,
            dist_pct=0.08,
            direction="SHORT",
            bias_h1="BEARISH",
            confirm_short=True,
            mode_bias="bearish",
            price_decimals=1,
            m5=[_red(42_160), _red(42_145)],
        )
        data.update({
            "generated": "2026-09-02 12:00",
            "asset_label": "US30",
            "chart_file": "us30_m5_chart.png",
            "mode_setup": "break",
            "rsi_h1": 48.0,
            "pdh": 42_500.0,
            "pdl": 41_800.0,
            "swing_highs": [42_200.0],
            "swing_lows": [41_900.0],
            "last_m5_12": ["12:00 O=42160.0 H=42170.0 L=42140.0 C=42145.0 [R]"],
            "session": {
                "in_ny_window": True,
                "window": "NY AM",
                "ny_local": "08:00",
            },
            "crt": make_crt(),
            "divergence": {"type": "NONE", "note": "sin divergencia"},
            "dmi": {"bias": "BEARISH", "note": "DI- > DI+"},
            "structure": {"hl": "LH", "lh": "LL"},
            "e2": {
                "checks": [],
                "score": 1,
                "max": 6,
                "eligible": False,
                "verdict": "E2_NO",
                "note": "Break mode",
                "mode_setup": "break",
            },
            "gallery_patterns": ["WIN: BREAK breakout bajista + hold"],
            "ilustrate": True,
            "annotated_chart_file": "us30_m5_chart_annotated.png",
            "annotated_chart_abs": str(tmp_path / "us30_m5_chart_annotated.png"),
            "signal_history_dir": str(tmp_path),
        })
        out = tmp_path / "us30_m5_high_signal.md"
        write_high_signal(out, data, verdict_to_signal, use_ml=False, advanced=True)
        text = out.read_text(encoding="utf-8")
        assert "# US30 M5 High Signal" in text
        assert "| Precio |" in text
        assert "| Entrada óptima |" in text
        assert text.index("| Precio |") < text.index("| Entrada óptima |")
        assert "| Última señal |" in text
        assert "| Calificación entrada |" in text
        assert "SIN HISTORIAL" in text
        assert (tmp_path / "us30_signal_history.json").exists()
        assert "| Confluencia setup |" in text
        # Confluencia es la última fila de la tabla Categories (antes de blank/sección)
        cats_block = text.split("## Categories")[1].split("##")[0]
        table_rows = [
            ln for ln in cats_block.splitlines()
            if ln.startswith("| ") and "Campo" not in ln and "---" not in ln
        ]
        assert table_rows[-1].startswith("| Confluencia setup |")
        assert "— Advanced —" in text or "Dist. a Entry" in text
        assert "Modo **ADVANCED**" in text
        assert "TRADING_LIVE_US30_HIGH_SIGNAL.md" in text
        assert "## Salidas" in text
        assert "live/us30_m5_high_signal.md" in text
        assert "live/us30_m5_chart_annotated.png" in text
        assert "![chart](us30_m5_chart_annotated.png)" in text
        # Sesión no es fila de status Categories
        assert "| Sesión |" not in cats_block


# ---------------------------------------------------------------------------
# 9b. Contingencias Si entraste (ESPERAR LONG/SHORT)
# ---------------------------------------------------------------------------

class TestContingencyGuidanceEsperar:
    def _cats(self, **extra) -> dict:
        cats = {
            "recomendacion": "ESPERAR LONG",
            "signal_e1": "ESPERAR",
            "direction": "LONG",
            "rules_pct": 71,
            "rules_ok": 5,
            "rules_total": 7,
            "confluencia_setup": "MEDIA",
            "bando_usado": "BULLISH",
            "bando_mercado": "BULLISH",
            "neural_prob_win": 0.72,
            "neural_grade": "B",
            "neural_gallery_aligned": True,
        }
        cats.update(extra)
        return cats

    def test_is_esperar_recomendacion(self):
        assert is_esperar_recomendacion("ESPERAR LONG")
        assert is_esperar_recomendacion("ESPERAR SHORT")
        assert not is_esperar_recomendacion("ENTRAR LONG")
        assert not is_esperar_recomendacion("NO_OPERAR")

    def test_esperar_long_without_user_entry(self):
        data = make_data(
            direction="LONG",
            bias_h1="BULLISH",
            confirm_long=True,
            confirm_short=False,
            price=100_000.0,
            zone_level=99_980.0,
            dist_pct=0.05,
        )
        opt = {"entry": 99_980.0, "dec": 1, "direction": "LONG"}
        g = build_contingency_guidance(self._cats(), data, opt=opt)
        assert g is not None
        assert g["side"] == "LONG"
        assert "ESPERAR LONG" in g["headline"] or "LONG" in g["headline"]
        assert 2 <= len(g["options"]) <= 4
        joined = " ".join(g["options"])
        assert "Neural" in joined
        assert "Rules" in joined or "Confluencia" in joined
        assert "Entrada óptima" in joined or "óptima" in g["headline"].lower() or "óptima" in joined

    def test_esperar_short_with_user_entry(self):
        data = make_data(
            direction="SHORT",
            bias_h1="BEARISH",
            confirm_short=True,
            price=53_500.0,
            zone_level=53_484.0,
            dist_pct=0.03,
            price_decimals=1,
        )
        opt = {
            "entry": 53_484.1,
            "user_entry": 53_490.0,
            "dec": 1,
            "direction": "SHORT",
            "sl": 53_520.0,
            "tp": 53_420.0,
            "sl_tp_source": "past",
        }
        cats = self._cats(
            recomendacion="ESPERAR SHORT",
            direction="SHORT",
            rules_pct=55,
            confluencia_setup="BAJA",
            neural_prob_win=0.48,
            ml_prob_win=0.40,
            bando_usado="BEARISH",
            bando_mercado="BEARISH",
        )
        g = build_contingency_guidance(cats, data, opt=opt)
        assert g is not None
        assert g["side"] == "SHORT"
        assert "Entry usuario" in g["headline"] or "Entry usuario" in " ".join(g["options"])
        assert any("Rules" in o and ("<70%" in o or "55%" in o) for o in g["options"])
        assert any("BE" in o or "reducir" in o.lower() for o in g["options"])

    def test_none_when_entrar_or_history(self):
        data = make_data(direction="LONG", confirm_long=True, confirm_short=False)
        opt = {"entry": 100_000.0, "dec": 1}
        g_enter = build_contingency_guidance(
            self._cats(recomendacion="ENTRAR LONG", signal_e1="ENTRAR"),
            data,
            opt=opt,
        )
        assert g_enter is None
        g_hist = build_contingency_guidance(
            self._cats(history_mode=True),
            data,
            opt=opt,
        )
        assert g_hist is None

    def test_categories_md_shows_si_entraste_before_confluencia(self):
        g = build_contingency_guidance(
            self._cats(recomendacion="ESPERAR SHORT", direction="SHORT"),
            make_data(direction="SHORT", confirm_short=True, price=53_500.0),
            opt={"entry": 53_484.0, "dec": 1, "direction": "SHORT"},
        )
        rows = format_contingency_table_rows(g)
        assert rows[0][0] == "Si entraste"
        assert any(r[0].startswith("Contingencia") for r in rows)

        cats = {
            "bando_usado": "BEARISH",
            "bando_mercado": "BEARISH",
            "recomendacion": "ESPERAR SHORT",
            "signal_e1": "ESPERAR",
            "direction": "SHORT",
            "precio": "53500.0",
            "entrada_optima": "53484.0",
            "confluencia_setup": "MEDIA",
            "confluencia_detalle": "58%",
            "contingency_rows": rows,
        }
        md = "\n".join(format_augmented_categories_md(cats))
        assert "| **— Si entraste —** |" in md
        assert "| Si entraste |" in md
        assert "| Contingencia 1 |" in md
        si_i = md.index("| Si entraste |")
        conf_i = md.index("| Confluencia setup |")
        assert si_i < conf_i
        table_lines = [
            ln for ln in md.splitlines()
            if ln.startswith("| ") and "Campo" not in ln and "---" not in ln
        ]
        assert table_lines[-1].startswith("| Confluencia setup |")


# ---------------------------------------------------------------------------
# 10. Signal history + calificación entrada vs última Entrada óptima
# ---------------------------------------------------------------------------

class TestSignalHistoryReflection:
    def test_append_minimal_schema_and_cap(self, tmp_path):
        from app.models.signal_history import (
            append_signal_history,
            history_path_for_asset,
            load_signal_history,
        )

        path = history_path_for_asset("BTC", tmp_path)
        for i in range(5):
            append_signal_history(
                path,
                asset="BTC",
                time_str=f"2026-09-0{i + 1} 10:00 NY",
                optimal_entry=77_000.0 + i,
                cap=3,
            )
        hist = load_signal_history(path)
        assert len(hist) == 3
        assert set(hist[0].keys()) == {"id", "time", "optimal_entry"}
        assert hist[-1]["optimal_entry"] == 77_004.0
        assert hist[-1]["id"].startswith("btc-")
        # IDs monotónicos pese al trim
        assert hist[0]["id"] == "btc-003"
        assert hist[-1]["id"] == "btc-005"

        # Con side opcional
        append_signal_history(
            path, asset="BTC", time_str="t-side", optimal_entry=77_010.0, side="SHORT", cap=3,
        )
        hist2 = load_signal_history(path)
        assert hist2[-1]["side"] == "SHORT"
        assert set(hist2[-1].keys()) == {"id", "time", "optimal_entry", "side"}

    def test_us30_separate_file(self, tmp_path):
        from app.models.signal_history import append_signal_history, history_path_for_asset

        btc = history_path_for_asset("BTC", tmp_path)
        us30 = history_path_for_asset("US30", tmp_path)
        append_signal_history(btc, asset="BTC", time_str="t1", optimal_entry=1.0)
        append_signal_history(us30, asset="US30", time_str="t2", optimal_entry=42_000.0)
        assert btc.name == "btc_signal_history.json"
        assert us30.name == "us30_signal_history.json"
        assert btc.read_text(encoding="utf-8") != us30.read_text(encoding="utf-8")

    def test_pair_isolation_reflect_uses_only_own_last(self, tmp_path):
        """BTC refleja solo btc_signal_history; US30 solo us30 — nunca mezcla."""
        from app.models.signal_history import (
            append_signal_history,
            history_path_for_asset,
            persist_and_reflect_entry,
        )

        btc_path = history_path_for_asset("BTC", tmp_path)
        us30_path = history_path_for_asset("US30", tmp_path)
        append_signal_history(btc_path, asset="BTC", time_str="t-btc", optimal_entry=100_000.0)
        append_signal_history(us30_path, asset="US30", time_str="t-us30", optimal_entry=42_000.0)

        data_btc = {
            "asset_label": "BTC",
            "price": 100_010.0,
            "price_decimals": 1,
            "signal_history_dir": str(tmp_path),
            "setup": {"direction": "SHORT"},
            "zone": {"dist_pct": 0.05, "level": 100_050.0},
            "confirm_short": True,
            "bias_h1": "BEARISH",
            "mode_bias": "bearish",
            "mode_setup": "break",
            "session": {"ny_local": "08:00"},
        }
        opt_btc = {"entry": 100_020.0, "dec": 1, "ahora_action": "ENTRAR SHORT", "direction": "SHORT"}
        ref_btc = persist_and_reflect_entry(data_btc, opt_btc, history_dir=tmp_path)
        assert ref_btc["last_id"] == "btc-001"
        assert ref_btc["last_entry"] == 100_000.0
        assert ref_btc["grade"] in ("BUENA", "REGULAR", "MALA", "EVITAR")

        data_us30 = {
            "asset_label": "US30",
            "price": 42_100.0,
            "price_decimals": 1,
            "signal_history_dir": str(tmp_path),
            "setup": {"direction": "LONG"},
            "zone": {"dist_pct": 0.8, "level": 41_500.0},
            "confirm_long": False,
            "bias_h1": "BEARISH",
            "mode_bias": "auto",
            "mode_setup": "auto",
            "session": {"ny_local": "09:00"},
        }
        opt_us30 = {"entry": 41_800.0, "dec": 1, "ahora_action": "ESPERAR LONG", "direction": "LONG"}
        ref_us30 = persist_and_reflect_entry(data_us30, opt_us30, history_dir=tmp_path)
        assert ref_us30["last_id"] == "us30-001"
        assert ref_us30["last_entry"] == 42_000.0
        # No debe haber leído el last de BTC
        assert ref_us30["last_id"] != "btc-001"
        assert "btc-" not in (ref_us30.get("cell_ultima") or "")

    def test_reflect_sin_historial_mas_cerca_lejos_misma_zona(self):
        from app.models.signal_history import reflect_last_entry

        empty = reflect_last_entry(None, price=100.0, current_entry=100.0)
        assert empty["status"] == "SIN HISTORIAL"
        assert empty["grade"] == "SIN HISTORIAL"
        assert "SIN HISTORIAL" in empty["cell_vs"]

        last = {"id": "btc-001", "time": "2026-09-01 10:00 NY", "optimal_entry": 100_000.0}
        # Entry casi igual → MISMA ZONA
        same = reflect_last_entry(last, price=100_010.0, current_entry=100_020.0, dec=1)
        assert same["status"] == "MISMA ZONA"

        # Precio mucho más cerca de entry actual que de la última → MÁS CERCA
        last_far = {"id": "btc-002", "time": "t", "optimal_entry": 99_000.0}
        closer = reflect_last_entry(last_far, price=100_000.0, current_entry=100_050.0, dec=1)
        assert closer["status"] == "MÁS CERCA"
        assert closer["delta_entry_pts"] is not None
        assert closer["grade"] in ("BUENA", "REGULAR", "MALA", "EVITAR")

        # Precio más cerca de la última entry que de la actual → MÁS LEJOS
        last_near = {"id": "btc-003", "time": "t", "optimal_entry": 100_000.0}
        farther = reflect_last_entry(last_near, price=100_500.0, current_entry=102_000.0, dec=1)
        assert farther["status"] == "MÁS LEJOS"

    def test_reflect_califica_buena_cerca_2m5(self):
        """Precio cerca de última Entry + 2M5 + zona + bando → BUENA."""
        from app.models.signal_history import reflect_last_entry

        last = {"id": "btc-010", "time": "t", "optimal_entry": 100_000.0}
        data = {
            "setup": {"direction": "SHORT"},
            "zone": {"dist_pct": 0.05, "level": 100_050.0},
            "confirm_short": True,
            "bias_h1": "BEARISH",
            "mode_bias": "bearish",
            "mode_setup": "break",
        }
        opt = {
            "entry": 100_020.0,
            "dec": 1,
            "ahora_action": "ENTRAR SHORT",
            "direction": "SHORT",
        }
        ref = reflect_last_entry(
            last, price=100_010.0, current_entry=100_020.0, dec=1, data=data, opt=opt,
        )
        assert ref["grade"] == "BUENA"
        assert ref["revisited_last"] is True
        assert "2M5" in ref["grade_reason"] or "última Entry" in ref["grade_reason"]
        assert "**BUENA**" in ref["cell_calificacion"]

    def test_reflect_califica_evitar_lejos_sin_confirm(self):
        from app.models.signal_history import reflect_last_entry

        last = {"id": "btc-011", "time": "t", "optimal_entry": 100_000.0}
        data = {
            "setup": {"direction": "SHORT"},
            "zone": {"dist_pct": 1.2, "level": 100_050.0},
            "confirm_short": False,
            "bias_h1": "BULLISH",
            "mode_bias": "auto",
            "mode_setup": "auto",
        }
        opt = {
            "entry": 99_500.0,
            "dec": 1,
            "ahora_action": "ESPERAR SHORT",
            "direction": "SHORT",
        }
        # Precio lejos de última (105k vs 100k) y de actual
        ref = reflect_last_entry(
            last, price=105_000.0, current_entry=99_500.0, dec=1, data=data, opt=opt,
        )
        assert ref["grade"] == "EVITAR"
        assert "**EVITAR**" in ref["cell_calificacion"]

    def test_categories_md_shows_reflection_after_entrada(self):
        cats = {
            "precio": "100040.0",
            "entrada_optima": "100023.6",
            "ultima_senal_entrada": "**btc-001** · 2026-09-01 10:00 NY · Entry **100000.0**",
            "calificacion_entrada": (
                "**BUENA** — precio cerca de última Entry + 2M5 OK · (MISMA ZONA)"
            ),
            "bando_usado": "BEARISH",
            "bando_mercado": "BEARISH",
            "recomendacion": "ESPERAR SHORT",
            "confluencia_setup": "MEDIA",
        }
        md = "\n".join(format_augmented_categories_md(cats))
        assert "| Última señal |" in md
        assert "| Calificación entrada |" in md
        assert "| vs última |" not in md
        assert md.index("| Entrada óptima |") < md.index("| Última señal |")
        assert md.index("| Última señal |") < md.index("| Calificación entrada |")
        assert md.index("| Calificación entrada |") < md.index("| Bando usado |")
        table_rows = [
            ln for ln in md.splitlines()
            if ln.startswith("| ") and "Campo" not in ln and "---" not in ln
        ]
        assert table_rows[-1].startswith("| Confluencia setup |")

    def test_categories_md_history_review_mode(self):
        """history_mode: Revisión P&L — sin Entrada óptima ni Recomendación ENTRAR."""
        cats = {
            "history_mode": True,
            "precio": "100150.0",
            "revision_ultima_entry": (
                "**btc-001** · 2026-09-01 10:00 NY · Entry **100000.0** · SHORT"
            ),
            "pnl_vs_precio": "**+150.0 pts (+0.150%)** · **EN BENEFICIO** · SHORT",
            "calificacion_entrada": "**BUENA** — Entry SHORT en beneficio",
            "bando_usado": "BEARISH",
            "bando_mercado": "BEARISH",
            "recomendacion": "ENTRAR SHORT",  # no debe mostrarse en history_mode
            "entrada_optima": "100023.6",  # tampoco
            "confluencia_setup": "MEDIA",
        }
        md = "\n".join(format_augmented_categories_md(cats))
        assert "| Revisión última Entry |" in md
        assert "| P&L vs precio actual |" in md
        assert "| Calificación Entry |" in md
        assert "Revisión última Entry" in md
        assert "| Entrada óptima |" not in md
        assert "| Recomendación |" not in md
        assert "ENTRAR SHORT" not in md
        assert "| Precio actual |" in md

    def test_history_review_pnl_long_short_and_no_append(self, tmp_path):
        from app.models.signal_history import (
            append_signal_history,
            history_path_for_asset,
            load_signal_history,
            persist_and_reflect_entry,
            review_last_entry_pnl,
        )

        path = history_path_for_asset("BTC", tmp_path)
        append_signal_history(
            path,
            asset="BTC",
            time_str="2026-09-01 10:00 NY",
            optimal_entry=100_000.0,
            side="SHORT",
        )

        # SHORT: precio bajó → beneficio
        last = load_signal_history(path)[-1]
        short_win = review_last_entry_pnl(last, price=99_500.0, dec=1)
        assert short_win["side"] == "SHORT"
        assert short_win["pnl_pts"] == pytest.approx(500.0)
        assert short_win["pnl_status"] == "EN_BENEFICIO"
        assert short_win["grade"] in ("EN_BENEFICIO", "BUENA")
        assert "EN BENEFICIO" in short_win["cell_pnl"]

        # LONG sin side en JSON → CLI bullish
        long_ref = review_last_entry_pnl(
            {"id": "btc-009", "time": "t", "optimal_entry": 100_000.0},
            price=100_300.0,
            dec=1,
            data={"mode_bias": "bullish"},
        )
        assert long_ref["side"] == "LONG"
        assert long_ref["side_source"] == "CLI -Bullish"
        assert long_ref["pnl_pts"] == pytest.approx(300.0)
        assert long_ref["pnl_status"] == "EN_BENEFICIO"

        # CERCA_BE
        be = review_last_entry_pnl(
            {"id": "btc-010", "time": "t", "optimal_entry": 100_000.0, "side": "LONG"},
            price=100_020.0,
            dec=1,
        )
        assert be["grade"] == "CERCA_BE"
        assert be["pnl_status"] == "NEUTRO"

        # history_mode: NO append
        data = {
            "asset_label": "BTC",
            "price": 99_400.0,
            "price_decimals": 1,
            "signal_history_dir": str(tmp_path),
            "history_mode": True,
            "mode_bias": "bearish",
            "setup": {"direction": "SHORT"},
            "zone": {"dist_pct": 0.1},
            "session": {"ny_local": "2026-09-02 08:00"},
        }
        opt = {"entry": 99_000.0, "dec": 1, "direction": "SHORT"}
        before = len(load_signal_history(path))
        ref = persist_and_reflect_entry(data, opt, history_dir=tmp_path, history_mode=True)
        after = load_signal_history(path)
        assert len(after) == before
        assert ref["mode"] == "history_review"
        assert ref["last_id"] == "btc-001"
        assert ref["pnl_status"] == "EN_BENEFICIO"

    def test_write_high_signal_history_review_no_append(self, tmp_path):
        from app.services.btc_high_analysis import write_high_signal
        from app.models.btc_signal_categories import verdict_to_signal
        from app.models.signal_history import (
            append_signal_history,
            history_path_for_asset,
            load_signal_history,
        )

        hist_dir = tmp_path / "hist"
        hist_dir.mkdir()
        path_hist = history_path_for_asset("BTC", hist_dir)
        append_signal_history(
            path_hist,
            asset="BTC",
            time_str="2026-09-01 09:00 NY",
            optimal_entry=100_000.0,
            side="SHORT",
        )

        data = make_data(
            price=99_700.0,
            zone_level=100_050.0,
            dist_pct=0.05,
            direction="SHORT",
            bias_h1="BEARISH",
            confirm_short=True,
            mode_bias="bearish",
            m5=[_red(100_060), _red(99_700)],
        )
        data.update({
            "generated": "2026-09-02 12:00",
            "asset_label": "BTC",
            "chart_file": "btc_m5_chart.png",
            "mode_setup": "auto",
            "history_mode": True,
            "signal_history_dir": str(hist_dir),
            "rsi_h1": 48.0,
            "pdh": 101_000.0,
            "pdl": 99_000.0,
            "swing_highs": [100_200.0],
            "swing_lows": [99_800.0],
            "last_m5_12": ["12:00 O=100060 H=100070 L=99600 C=99700 [R]"],
            "session": {
                "in_ny_window": True,
                "window": "NY AM",
                "ny_local": "2026-09-02 08:00",
            },
            "crt": make_crt(),
            "divergence": {"type": "NONE", "note": "sin divergencia"},
            "dmi": {"bias": "BEARISH", "note": "DI- > DI+"},
            "structure": {"hl": "LH", "lh": "LL"},
            "e2": {
                "checks": [],
                "score": 1,
                "max": 6,
                "eligible": False,
                "verdict": "E2_NO",
                "note": "n/a",
                "mode_setup": "auto",
            },
            "gallery_patterns": [],
        })
        out = tmp_path / "btc_m5_high_signal.md"
        write_high_signal(out, data, verdict_to_signal, use_ml=False, advanced=False)
        text = out.read_text(encoding="utf-8")
        assert "| Revisión última Entry |" in text
        assert "| P&L vs precio actual |" in text
        assert "| Calificación Entry |" in text
        assert "| Entrada óptima |" not in text
        assert "btc-001" in text
        assert "EN BENEFICIO" in text or "EN PÉRDIDA" in text or "NEUTRO" in text
        # Sin append
        hist = load_signal_history(path_hist)
        assert len(hist) == 1
        assert hist[-1]["id"] == "btc-001"

    def test_write_high_signal_persists_and_reflects(self, tmp_path):
        from app.services.btc_high_analysis import write_high_signal
        from app.models.btc_signal_categories import verdict_to_signal
        from app.models.signal_history import (
            append_signal_history,
            history_path_for_asset,
            load_signal_history,
        )

        hist_dir = tmp_path / "hist"
        hist_dir.mkdir()
        path_hist = history_path_for_asset("BTC", hist_dir)
        append_signal_history(
            path_hist,
            asset="BTC",
            time_str="2026-09-01 09:00 NY",
            optimal_entry=100_000.0,
        )

        data = make_data(
            price=100_040.0,
            zone_level=100_050.0,
            dist_pct=0.05,
            direction="SHORT",
            bias_h1="BEARISH",
            confirm_short=True,
            mode_bias="bearish",
            m5=[_red(100_060), _red(100_040)],
        )
        data.update({
            "generated": "2026-09-02 12:00",
            "asset_label": "BTC",
            "chart_file": "btc_m5_chart.png",
            "mode_setup": "auto",
            "signal_history_dir": str(hist_dir),
            "rsi_h1": 48.0,
            "pdh": 101_000.0,
            "pdl": 99_000.0,
            "swing_highs": [100_200.0],
            "swing_lows": [99_800.0],
            "last_m5_12": ["12:00 O=100060 H=100070 L=100030 C=100040 [R]"],
            "session": {
                "in_ny_window": True,
                "window": "NY AM",
                "ny_local": "2026-09-02 08:00",
            },
            "crt": make_crt(),
            "divergence": {"type": "NONE", "note": "sin divergencia"},
            "dmi": {"bias": "BEARISH", "note": "DI- > DI+"},
            "structure": {"hl": "LH", "lh": "LL"},
            "e2": {
                "checks": [],
                "score": 1,
                "max": 6,
                "eligible": False,
                "verdict": "E2_NO",
                "note": "n/a",
                "mode_setup": "auto",
            },
            "gallery_patterns": [],
        })
        out = tmp_path / "btc_m5_high_signal.md"
        write_high_signal(out, data, verdict_to_signal, use_ml=False, advanced=False)
        text = out.read_text(encoding="utf-8")
        assert "| Última señal |" in text
        assert "btc-001" in text
        assert "| Calificación entrada |" in text
        assert any(g in text for g in ("BUENA", "REGULAR", "MALA", "EVITAR"))
        # Tras el write hay 2 registros (previo + actual)
        hist = load_signal_history(path_hist)
        assert len(hist) == 2
        assert hist[-1]["id"] == "btc-002"
        assert "optimal_entry" in hist[-1]
        # High guarda side cuando se puede inferir
        assert hist[-1].get("side") == "SHORT"
        assert set(hist[-1].keys()) == {"id", "time", "optimal_entry", "side"}
        assert "NY" in hist[-1]["time"]


# ---------------------------------------------------------------------------
# Fusion score + Neural/ML confidence gating (High DL path)
# ---------------------------------------------------------------------------

class TestFusionAndNeuralGating:
    """Smarter High fusion: no Neural pad, low-conf gate, ML in scorecard."""

    def _base_ctx(self, rules_pct: int = 85, ext_pct: int = 80) -> dict:
        return {
            "verdict": "ENTRAR",
            "ext_pct": ext_pct,
            "categories": {
                "rules_ok": 6,
                "rules_total": 7,
                "rules_pct": rules_pct,
            },
        }

    def test_neural_gate_factor_low_and_grade_c(self):
        assert neural_gate_factor("high", "B") == 1.0
        assert neural_gate_factor("low", "B") == 0.35
        assert neural_gate_factor("low", "C") < neural_gate_factor("low", "B")
        assert gated_prob_toward_neutral(0.80, 0.35) < 0.65
        assert gated_prob_toward_neutral(0.80, 0.35) > 0.50

    def test_prob_to_confidence_respects_model_softmax(self):
        assert prob_to_confidence(0.90, model_confidence=0.52) == "low"
        assert prob_to_confidence(0.90, model_confidence=0.95) == "high"

    def test_confluencia_downweights_low_conf_neural(self):
        data = make_data(
            direction="SHORT",
            bias_h1="BEARISH",
            mode_bias="bearish",
            dist_pct=0.05,
            confirm_short=True,
        )
        data["mode_setup"] = "break"
        strong = {
            "rules_pct": 85,
            "neural_prob_win": 0.78,
            "neural_grade": "B",
            "neural_confidence": "high",
            "neural_gallery_aligned": True,
            "neural_gate_factor": 1.0,
            "neural_effective_prob_win": 0.78,
        }
        weak = {
            **strong,
            "neural_confidence": "low",
            "neural_gallery_aligned": False,
            "neural_gate_factor": 0.35,
            "neural_effective_prob_win": gated_prob_toward_neutral(0.78, 0.35),
        }
        level_hi, detail_hi = compute_confluencia_setup(
            strong, data, crt=make_crt(), e2={"eligible": False},
        )
        level_lo, detail_lo = compute_confluencia_setup(
            weak, data, crt=make_crt(), e2={"eligible": False},
        )
        # Extraer % del detalle ("66% · ...")
        pct_hi = int(detail_hi.split("%")[0])
        pct_lo = int(detail_lo.split("%")[0])
        assert pct_hi > pct_lo
        assert level_hi in ("ALTA", "MEDIA")
        assert "gated" in detail_lo.lower() or "gating" in detail_lo.lower() or "débil" in detail_lo.lower() or "Neural" in detail_lo

    def test_scorecard_omits_missing_neural_no_pad50(self):
        data = make_data(direction="SHORT", bias_h1="BEARISH", confirm_short=True)
        data["mode_setup"] = "break"
        ctx = self._base_ctx()
        cats_no = dict(ctx["categories"])
        combined_no, rows_no = compute_advanced_scorecard(
            data, ctx, cats_no, make_crt(), {"eligible": False}, "break",
        )
        assert any("omitido" in r[3] for r in rows_no if "Neural" in r[0])
        assert not any("neutral 50%" in r[3] for r in rows_no if "Neural" in r[0])
        assert "neural" not in cats_no.get("fusion_weights", {})
        assert cats_no["fusion_score"] == round(combined_no, 1)

        # High-conf Neural vs low-conf same raw prob: low gate must not inflate
        cats_hi = {
            **ctx["categories"],
            "neural_prob_win": 0.88,
            "neural_confidence": "high",
            "neural_grade": "A+",
            "neural_gallery_aligned": True,
            "neural_gate_factor": 1.0,
            "neural_effective_prob_win": 0.88,
        }
        cats_lo = {
            **cats_hi,
            "neural_confidence": "low",
            "neural_gallery_aligned": False,
            "neural_gate_factor": 0.35,
            "neural_effective_prob_win": gated_prob_toward_neutral(0.88, 0.35),
        }
        combined_hi, _ = compute_advanced_scorecard(
            data, ctx, cats_hi, make_crt(), {"eligible": False}, "break",
        )
        combined_lo, _ = compute_advanced_scorecard(
            data, ctx, cats_lo, make_crt(), {"eligible": False}, "break",
        )
        assert combined_hi > combined_lo
        assert "neural" in cats_hi["fusion_weights"]
        assert cats_hi["fusion_score"] == round(combined_hi, 1)
    def test_scorecard_includes_ml_and_gates_low_conf(self):
        data = make_data(direction="SHORT", bias_h1="BEARISH", confirm_short=True)
        data["mode_setup"] = "break"
        ctx = self._base_ctx()
        cats = {
            **ctx["categories"],
            "ml_prob_win": 0.80,
            "ml_grade": "A+",
            "ml_confidence": "high",
            "neural_prob_win": 0.80,
            "neural_confidence": "low",
            "neural_grade": "B",
            "neural_gate_factor": 0.35,
            "neural_effective_prob_win": gated_prob_toward_neutral(0.80, 0.35),
            "neural_gallery_aligned": False,
        }
        combined, rows = compute_advanced_scorecard(
            data, ctx, cats, make_crt(), {"eligible": False}, "break",
        )
        assert any("ML tabular" in r[0] for r in rows)
        assert "ml" in cats["fusion_weights"]
        # Low-conf Neural effective ~60.5%, not raw 80%
        neural_row = next(r for r in rows if "Neural" in r[0])
        assert "gate×0.35" in neural_row[3]
        assert combined < 90  # would be higher if raw 80% neural counted fully

    def test_direction_penalty_lowers_combined(self):
        ctx = self._base_ctx()
        cats = dict(ctx["categories"])
        aligned = make_data(direction="SHORT", bias_h1="BEARISH", confirm_short=True)
        aligned["mode_setup"] = "break"
        conflict = make_data(direction="SHORT", bias_h1="BULLISH", confirm_short=True)
        conflict["mode_setup"] = "break"
        c_ok, _ = compute_advanced_scorecard(
            aligned, ctx, dict(cats), make_crt(), {}, "break",
        )
        c_bad, rows = compute_advanced_scorecard(
            conflict, ctx, dict(cats), make_crt(pd_reading="BULLISH"), {}, "break",
        )
        assert c_bad < c_ok
        assert any("Penalización" in r[0] for r in rows)


# ---------------------------------------------------------------------------
# Entrypoint unittest-compatible
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
