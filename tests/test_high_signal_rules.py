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
    compute_optimal_entry,
    compute_second_indication,
    format_2m5_checklist,
    format_2m5_valid_invalid,
    format_optimal_entry_md,
)
from app.models.btc_signal_categories import format_augmented_categories_md  # noqa: E402
from app.views.illustrate_high_entry import (  # noqa: E402
    create_annotated_entry_chart,
    format_illustration_md,
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
        assert "❌" not in text.replace("## Checklist 2M5", "")

    def test_session_outside_ny_fails(self):
        data = make_data(in_ny=False, direction="SHORT", confirm_short=True, dist_pct=0.05)
        text = self._joined(
            format_2m5_checklist(data, "SHORT", data["session"], make_crt())
        )
        assert "Sesión NY activa" in text
        assert "❌] Sesión NY" in text or "[❌] Sesión NY activa" in text
        assert "Falta al menos 1" in text

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
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        md = "\n".join(format_optimal_entry_md(opt, data, "SHORT", make_crt()))
        assert "## Ilustración entrada (2M5 + óptima)" in md
        assert "![annotated](btc_m5_chart_annotated.png)" in md

    def test_ilustrate_false_omits_illustration_section(self):
        data = make_data(direction="SHORT", dist_pct=0.05, confirm_short=True)
        data["ilustrate"] = False
        opt = compute_optimal_entry(data, "SHORT", make_crt(), data["zone"])
        md = "\n".join(format_optimal_entry_md(opt, data, "SHORT", make_crt()))
        assert "Ilustración entrada" not in md

    def test_format_illustration_md_relative_link(self):
        lines = format_illustration_md("live/us30_m5_chart_annotated.png")
        text = "\n".join(lines)
        assert "![annotated](us30_m5_chart_annotated.png)" in text
        assert "## Ilustración entrada" in text

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


# ---------------------------------------------------------------------------
# Entrypoint unittest-compatible
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
