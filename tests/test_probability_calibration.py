"""Probabilidad calibrada (walk-forward) + Reglas revisadas graduadas."""
from __future__ import annotations

import json
import math
import random
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.controllers.train_btc_signals import temporal_split  # noqa: E402
from app.models import probability_calibration as pc  # noqa: E402
from app.models.btc_signal_categories import winrate_estimate  # noqa: E402
from app.services.btc_high_analysis import compute_advanced_scorecard  # noqa: E402


def _rows(n: int = 1500, *, signal: bool = True, seed: int = 3) -> list[dict]:
    rng = random.Random(seed)
    t0 = datetime(2026, 3, 1, tzinfo=timezone.utc)
    rows = []
    for i in range(n):
        rsi_ext = rng.uniform(-2, 4)
        pd_favor = rng.choice([-1.0, -1.0, -1.0, 1.0])
        confirm = float(rng.random() < 0.3)
        crt = float(rng.random() < 0.9)
        z = -0.1 - 0.35 * rsi_ext + 0.3 * pd_favor if signal else -0.15
        rows.append({
            "time": t0 + timedelta(minutes=60 * i),
            "bar": i * 12,
            "direction": "SHORT",
            "label": int(rng.random() < 1 / (1 + math.exp(-z))),
            "legacy_pct": 64.0,
            "risk_pct": 0.09,
            "rsi_ext": rsi_ext,
            "pd_favor": pd_favor,
            "confirm_2m5": confirm,
            "crt_coherent": crt,
        })
    return rows


@pytest.fixture(scope="module")
def calib_edge() -> dict:
    return pc.fit_calibration(_rows(), n_boot=40)


@pytest.fixture
def calib_env(tmp_path, monkeypatch, calib_edge):
    path = tmp_path / "btc_prob_calibration.json"
    path.write_text(json.dumps(calib_edge, default=str), encoding="utf-8")
    monkeypatch.setenv("TRADING_PROB_CALIBRATION", "on")
    monkeypatch.setenv("TRADING_PROB_CALIBRATION_DIR", str(tmp_path))
    return calib_edge


def _data(direction: str = "SHORT", rsi: float = 45.0, confirm: bool = True) -> dict:
    return {
        "asset_label": "BTC",
        "price": 100_000.0,
        "bias_h1": "BEARISH" if direction == "SHORT" else "BULLISH",
        "rsi_m5": rsi,
        "confirm_long": confirm and direction == "LONG",
        "confirm_short": confirm and direction == "SHORT",
        "session": {"in_ny_window": True, "window": "NY AM"},
        "setup": {"direction": direction, "verdict": "SETUP_A+", "rr": 2.0,
                  "sl": 100_090.0 if direction == "SHORT" else 99_910.0},
        "mode_setup": "auto",
    }


def _crt(pd: str = "DISCOUNT", **kw) -> dict:
    return {"premium_discount": pd, "pd_reading": "BEARISH", **kw}


class TestFit:
    def test_detects_edge_and_rsi_sign(self, calib_edge):
        assert calib_edge["has_edge"] is True
        assert calib_edge["coef"]["rsi_ext"] < 0
        assert calib_edge["coef"]["pd_favor"] > 0
        oos = calib_edge["oos"]
        assert oos["model"]["brier"] < oos["constant"]["brier"]
        assert oos["legacy"]["brier"] > oos["model"]["brier"]

    def test_noise_has_no_edge(self):
        calib = pc.fit_calibration(_rows(signal=False, seed=11), n_boot=10)
        assert calib["has_edge"] is False

    def test_effective_n_removes_overlap(self):
        assert pc._effective_n([0, 10, 20, 48, 60, 100], 48) == 3

    def test_rejects_tiny_sample(self):
        rows = _rows(50)
        with pytest.raises(RuntimeError):
            pc.fit_calibration(rows, n_boot=5)


class TestEstimate:
    def test_disabled_falls_back_to_heuristic(self):
        wr, src = winrate_estimate(83, data=_data(), crt=_crt())
        assert "calibrado" not in src
        assert "histórico" in src

    def test_winrate_estimate_uses_calibration(self, calib_env):
        cats: dict = {}
        wr, src = winrate_estimate(83, data=_data(), crt=_crt(), categories=cats)
        assert "calibrado walk-forward" in src
        assert "80%:" in src
        assert "EV" in src
        lo, hi = cats["prob_ci"]
        assert lo <= cats["prob_pct"] <= hi
        assert wr == f"~{cats['prob_pct']:.0f}%"

    def test_extended_rsi_lowers_probability(self, calib_env):
        p_ok = pc.calibrated_estimate(_data(rsi=55), _crt())["p"]
        p_ext = pc.calibrated_estimate(_data(rsi=19), _crt())["p"]
        assert p_ext < p_ok

    def test_ev_and_kelly(self, calib_env):
        est = pc.calibrated_estimate(_data(), _crt())
        expected = est["p"] * 2.0 - (1 - est["p"]) - est["cost_r"]
        assert est["ev_r"] == pytest.approx(expected)
        assert 0.0 <= est["kelly"] <= pc.KELLY_CAP
        if est["ev_r"] <= 0:
            assert est["kelly"] == 0.0

    def test_reverse_keeps_e2_heuristic(self, calib_env):
        wr, src = winrate_estimate(80, setup_mode="reverse", data=_data(), crt=_crt())
        assert "calibrado" not in src

    def test_low_confidence_flag(self, tmp_path, monkeypatch, calib_edge):
        small = dict(calib_edge, n_eff=12)
        (tmp_path / "btc_prob_calibration.json").write_text(json.dumps(small, default=str))
        monkeypatch.setenv("TRADING_PROB_CALIBRATION", "on")
        monkeypatch.setenv("TRADING_PROB_CALIBRATION_DIR", str(tmp_path))
        est = pc.calibrated_estimate(_data(), _crt())
        assert est["low_confidence"] is True
        assert "baja confianza" in pc.format_estimate_source(est)

    def test_unvalidated_layers_do_not_move_probability(self, calib_env):
        base = pc.calibrated_estimate(_data(), _crt())["p"]
        with_ml = pc.calibrated_estimate(
            _data(), _crt(), categories={"ml_prob_win": 0.95, "neural_prob_win": 0.95},
        )
        assert with_ml["p"] == pytest.approx(base)
        assert with_ml["layers_used"] == []


class TestScorecard:
    def test_final_row_is_calibrated(self, calib_env):
        cats = {"rules_ok": 5, "rules_total": 6, "rules_pct": 83}
        ctx = {"verdict": "ENTRAR", "ext_pct": 80, "categories": cats}
        combined, rows = compute_advanced_scorecard(_data(), ctx, cats, _crt(), {"eligible": False}, "auto")
        final = rows[-1]
        assert "Probabilidad de éxito" in final[0]
        assert final[2].startswith("80%:")
        assert cats["fusion_score"] == round(combined, 1)
        assert cats["prob_legacy_pct"] is not None
        assert any(r[0].startswith("Fusión heurística") for r in rows)
        assert all(r[2] in ("info", "—") or r is final for r in rows)


class TestRulesReview:
    ITEMS = [
        ("Solo E1", True, "Operar solo E1"),
        ("Tendencia H1 alineada", True, "Bajista"),
        ("R:R mínimo 1:2", True, "1:2"),
        ("RSI no contradice", False, "RSI 19 sobrevendido"),
    ]

    def test_grades_vary_with_rsi(self, calib_env):
        def rsi_grade(rsi: float) -> str:
            est = pc.calibrated_estimate(_data(rsi=rsi), _crt())
            return pc.build_rules_review_rows(_data(rsi=rsi), _crt(), est, self.ITEMS)[0]["grade"]

        assert rsi_grade(19) in ("✗", "✗✗")
        assert rsi_grade(65) in ("✓", "✓✓")

    def test_constant_rules_are_info(self, calib_env):
        est = pc.calibrated_estimate(_data(), _crt())
        rows = pc.build_rules_review_rows(_data(), _crt(), est, self.ITEMS)
        info = {r["label"]: r for r in rows if r["type"] == "info"}
        assert set(info) == {"Solo E1", "Tendencia H1 alineada", "R:R mínimo 1:2"}
        assert all(r["grade"] == "·" for r in info.values())
        assert "RSI no contradice" not in {r["label"] for r in rows}

    def test_fakeout_is_veto(self, calib_env):
        crt = _crt(fakeout_pdl=True)
        est = pc.calibrated_estimate(_data(), crt)
        row = next(r for r in pc.build_rules_review_rows(_data(), crt, est, []) if r["label"] == "Rango CRT coherente")
        assert row["type"] == "veto"
        assert row["grade"] == "✗✗"

    def test_heuristic_grades_without_calibration(self):
        rows = pc.build_rules_review_rows(_data(rsi=19), _crt(), None, [])
        assert rows[0]["grade"] == "✗✗"
        assert rows[0]["impact"] == "sin calibrar"

    def test_markdown_table(self, calib_env):
        est = pc.calibrated_estimate(_data(), _crt())
        md = pc.format_rules_review_md(pc.build_rules_review_rows(_data(), _crt(), est, self.ITEMS), est)
        assert md[0] == "### Reglas revisadas (graduadas)"
        assert "| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |" in md


def test_temporal_split_purges_and_keeps_order():
    X = np.arange(100).reshape(-1, 1)
    y = np.arange(100) % 2
    xtr, xte, _, _ = temporal_split(X, y, test_size=0.25, purge=5)
    assert xtr[-1, 0] == 69
    assert xte[0, 0] == 75
