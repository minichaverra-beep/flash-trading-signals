"""Resultados reales de la app (live/outcomes/<asset>_outcomes.jsonl) → evaluación y capas."""
from __future__ import annotations

import json

import pytest

from app.models.real_outcomes import (
    apply_layers_to_calibration,
    evaluate_outcomes,
    layer_validation,
    load_outcomes,
    outcomes_path,
)


def _rec(hid, resultado, *, prob=None, ml=None, neural=None, revision=1, pnl=None, schema=1):
    return {
        "schemaVersion": schema,
        "recordedUtc": "2026-10-15T13:00:00Z",
        "historyId": hid,
        "revision": revision,
        "signalId": f"btc-{hid:03d}",
        "asset": "BTC",
        "prediction": {"probabilityPct": prob, "mlPct": ml, "neuralPct": neural},
        "outcome": {"resultado": resultado, "pnlUsd": pnl},
        "source": "manual",
    }


def _write(path, rows, garbage=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(r) for r in rows]
    if garbage:
        lines.insert(1, "{no es json")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


@pytest.fixture
def outcomes_dir(tmp_path, monkeypatch):
    monkeypatch.setenv("TRADING_OUTCOMES_DIR", str(tmp_path))
    return tmp_path


def test_path_per_asset(outcomes_dir):
    assert outcomes_path("BTCUSDT") == outcomes_dir / "btc_outcomes.jsonl"
    assert outcomes_path("XAUUSD") == outcomes_dir / "xauusd_outcomes.jsonl"


def test_latest_revision_wins_and_skips_invalid(outcomes_dir):
    _write(outcomes_path("btc"), [
        _rec(1, "perdida", prob=60, revision=1),
        _rec(1, "ganada", prob=60, revision=2),
        _rec(2, "no_tomada", prob=55),
        _rec(3, "ganada", schema=99),
    ], garbage=True)
    recs = {r["historyId"]: r for r in load_outcomes("btc")}
    assert set(recs) == {1, 2}
    assert recs[1]["outcome"]["resultado"] == "ganada"


def test_evaluate_hit_rate_and_brier(outcomes_dir):
    rows = [_rec(1, "ganada", prob=80, pnl=20), _rec(2, "perdida", prob=20, pnl=-10),
            _rec(3, "ganada", prob=60, pnl=15), _rec(4, "no_tomada", prob=50)]
    ev = evaluate_outcomes(rows)
    assert ev["n_records"] == 4
    assert ev["n_resolved"] == 3
    assert ev["counts"]["no_tomada"] == 1
    assert ev["hit_rate"] == pytest.approx(2 / 3, abs=1e-4)
    assert ev["pnl_usd"] == 25.0
    prob = ev["probability"]
    assert prob["n"] == 3
    assert prob["brier"] == pytest.approx((0.04 + 0.04 + 0.16) / 3, abs=1e-5)
    assert prob["skill"] > 0
    assert ev["layers"]["ml"]["n"] == 0


def test_layers_stay_off_below_min_samples():
    rows = [_rec(i, "ganada" if i % 2 else "perdida", ml=70 if i % 2 else 30) for i in range(1, 11)]
    layers = layer_validation(rows, min_n=30)
    assert layers["ml"]["oos_ok"] is False
    assert layers["ml"]["n"] == 10
    assert "10/30" in layers["ml"]["reason"]
    assert layers["neural"]["oos_ok"] is False
    assert "sin predicciones Neural con resultado" in layers["neural"]["reason"]


def test_layer_turns_on_with_enough_skilled_samples():
    rows = [_rec(i, "ganada" if i % 2 else "perdida", ml=75 if i % 2 else 25) for i in range(1, 41)]
    layers = layer_validation(rows, min_n=30)
    assert layers["ml"]["oos_ok"] is True
    assert 0 < layers["ml"]["weight"] <= 0.5
    calib = apply_layers_to_calibration({"layers": {}}, rows, min_n=30)
    assert calib["layers"]["ml"]["oos_ok"] is True
    assert calib["layers_source"] == "live_outcomes"


def test_layer_without_skill_stays_off():
    rows = [_rec(i, "ganada" if i % 2 else "perdida", ml=25 if i % 2 else 75) for i in range(1, 41)]
    layers = layer_validation(rows, min_n=30)
    assert layers["ml"]["oos_ok"] is False
    assert "sin ventaja" in layers["ml"]["reason"]


def test_evaluate_outcomes_cmd_reports_and_applies(outcomes_dir, tmp_path, monkeypatch, capsys):
    from app.controllers import calibrate_signals

    calib_dir = tmp_path / "calib"
    calib_dir.mkdir()
    monkeypatch.setenv("TRADING_PROB_CALIBRATION_DIR", str(calib_dir))
    art = calib_dir / "btc_prob_calibration.json"
    art.write_text(json.dumps({"asset": "BTC", "layers": {"ml": {"oos_ok": False}}}), encoding="utf-8")
    _write(outcomes_path("btc"), [_rec(1, "ganada", prob=60, ml=70), _rec(2, "perdida", prob=40)])
    assert calibrate_signals.evaluate_outcomes_cmd("btc", apply_layers=True) == 0
    out = capsys.readouterr().out
    assert "resueltas 2" in out
    assert "layers.ml: no entra" in out
    saved = json.loads(art.read_text(encoding="utf-8"))
    assert saved["layers"]["ml"]["n"] == 1
    assert saved["layers"]["ml"]["oos_ok"] is False
