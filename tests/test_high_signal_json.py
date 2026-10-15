"""JSON estructurado de la señal High (live/<asset>_m5_high_signal.json)."""
from __future__ import annotations

import json
import math

import numpy as np

from app.views.high_signal_json import (
    SCHEMA_VERSION,
    build_high_signal_json,
    json_path_for,
    to_jsonable,
    write_json_atomic,
)
from tests.test_high_signal_rules import _red, make_crt, make_data

TOP_KEYS = {
    "schemaVersion", "asset", "mode", "generatedUtc", "signalId", "verdict", "direction", "price",
    "bias", "setup", "plan", "probability", "fusion", "confluence", "rules", "ml", "neural",
    "zentinel", "macdQuant", "ict", "crt", "contingencies", "redFlags", "checklists",
    "dataFreshness", "chart",
}
PLAN_KEYS = {"entry", "sl", "tp", "rr", "risk", "trigger", "invalidation", "confirmation"}
PROB_KEYS = {"pct", "ci", "evR", "kellyFrac", "calibrated", "method"}
LAYER_KEYS = {"rules", "extended", "crt", "neural", "ml", "e2"}


def _high_data(tmp_path, **extra):
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
        "signal_history_dir": str(tmp_path / "hist"),
        "rsi_h1": 48.0,
        "pdh": 101_000.0,
        "pdl": 99_000.0,
        "swing_highs": [100_200.0],
        "swing_lows": [99_800.0],
        "last_m5_12": ["12:00 O=100060 H=100070 L=100030 C=100040 [R]"],
        "session": {"in_ny_window": True, "window": "NY AM", "ny_local": "2026-09-02 08:00"},
        "crt": make_crt(),
        "divergence": {"type": "NONE", "note": "sin divergencia"},
        "dmi": {"bias": "BEARISH", "note": "DI- > DI+"},
        "structure": {"hl": "LH", "lh": "LL"},
        "e2": {"checks": [], "score": 1, "max": 6, "eligible": False, "verdict": "E2_NO",
               "note": "n/a", "mode_setup": "auto"},
        "gallery_patterns": [],
    })
    data.update(extra)
    return data


class TestToJsonable:
    def test_numpy_and_nan(self):
        out = to_jsonable({
            "f": np.float64(1.5), "i": np.int64(3), "b": np.bool_(True),
            "nan": float("nan"), "inf": math.inf, "t": (1, 2), 5: "k",
        })
        assert out == {"f": 1.5, "i": 3, "b": True, "nan": None, "inf": None, "t": [1, 2], "5": "k"}
        json.dumps(out, allow_nan=False)

    def test_unknown_object_to_str(self):
        class Foo:
            def __str__(self):
                return "foo"

        assert to_jsonable([Foo()]) == ["foo"]


class TestBuilder:
    def test_minimal_payload_schema_and_nulls(self):
        data = {"asset_label": "US30", "price": np.float64(42000.5), "setup": {"direction": "NONE"},
                "generated": "2026-10-15 13:19"}
        ctx = {"categories": {}, "verdict": "NO_OPERAR"}
        payload = build_high_signal_json(data, ctx, None)
        assert TOP_KEYS <= set(payload)
        assert payload["schemaVersion"] == SCHEMA_VERSION == 1
        assert payload["asset"] == "US30"
        assert payload["generatedUtc"] == "2026-10-15T13:19:00Z"
        assert payload["price"] == 42000.5
        assert set(payload["plan"]) >= PLAN_KEYS
        assert all(payload["plan"][k] is None for k in ("entry", "sl", "tp"))
        assert set(payload["probability"]) >= PROB_KEYS
        assert payload["probability"]["calibrated"] is False
        assert set(payload["fusion"]["layers"]) == LAYER_KEYS
        for key in ("ml", "neural", "zentinel", "macdQuant"):
            assert payload[key] is None
        json.dumps(payload, allow_nan=False)

    def test_calibrated_probability_from_categories(self):
        cats = {
            "prob_pct": 59.5, "prob_ci": (50.5, 66.8), "ev_r": np.float64(0.71), "kelly_frac": 0.01,
            "prob_has_edge": True, "prob_n": 2097, "prob_n_eff": 755,
            "fusion_score": 59.5, "fusion_weights": {"rules_e1": 0.5, "rules_ext": 0.25, "crt": 0.25},
            "ml_prob_win": np.float64(0.62), "ml_grade": "B", "ml_confidence": "media",
            "confluencia_pct": 55, "confluencia_setup": "MEDIA", "rules_pct": 66,
            "contingency": {"headline": "Gestiona", "options": ["BE en 1:1", "Cerrar si CRT invalid"]},
        }
        data = {"asset_label": "BTC", "setup": {"direction": "LONG"}, "price": 1.0,
                "zentinel_volume": {"band": "alto", "ratio": np.float64(1.9), "candles": [1, 2]},
                "zentinel": {"market": "BTC"},
                "session": {"window": "NY AM", "in_ny_window": True},
                "macd_quant": {"available": True, "soft_filter_ok": np.bool_(True), "histogram": np.float64(2.5)},
                "data_freshness": {"stale": True, "message": "Datos viejos"}}
        ctx = {"categories": cats, "verdict": "ESPERAR", "ext_pct": 70, "flags": ["rf1"]}
        p = build_high_signal_json(data, ctx, {"entry": 10.0, "sl": 9.0, "tp": 12.0, "rr": 2.0, "risk_pts": 1.0})
        assert p["probability"]["pct"] == 59.5
        assert p["probability"]["ci"] == [50.5, 66.8]
        assert p["probability"]["calibrated"] is True
        assert p["probability"]["method"] == "walk_forward_logistic"
        assert p["fusion"]["weights"]["rules_e1"] == 0.5
        assert p["fusion"]["layers"]["ml"] == 62.0
        assert p["ml"] == {"pct": 62.0, "grade": "B", "conf": "media"}
        assert p["zentinel"]["volume"] == {"band": "alto", "ratio": 1.9}
        assert p["zentinel"]["killzoneOn"] is True
        assert p["macdQuant"]["soft_filter_ok"] is True
        assert p["contingencies"] == ["Gestiona", "BE en 1:1", "Cerrar si CRT invalid"]
        assert p["dataFreshness"]["stale"] is True
        assert p["plan"]["entry"] == 10.0
        assert p["plan"]["rr"] == 2.0
        assert p["redFlags"] == ["rf1"]
        json.dumps(p, allow_nan=False)


class TestAtomicWrite:
    def test_write_and_replace(self, tmp_path):
        target = tmp_path / "live" / "btc_m5_high_signal.json"
        write_json_atomic(target, {"schemaVersion": 1, "a": 1})
        write_json_atomic(target, {"schemaVersion": 1, "a": 2})
        assert json.loads(target.read_text(encoding="utf-8"))["a"] == 2
        assert [p.name for p in target.parent.iterdir()] == [target.name]

    def test_json_path_for(self, tmp_path):
        assert json_path_for(tmp_path / "us30_m5_high_signal.md").name == "us30_m5_high_signal.json"


class TestWriteHighSignalIntegration:
    def test_md_and_json_written(self, tmp_path):
        from app.models.btc_signal_categories import verdict_to_signal
        from app.services.btc_high_analysis import write_high_signal

        (tmp_path / "hist").mkdir()
        out = tmp_path / "btc_m5_high_signal.md"
        write_high_signal(out, _high_data(tmp_path), verdict_to_signal, use_ml=False, advanced=False)
        assert "## Resumen High" in out.read_text(encoding="utf-8")
        payload = json.loads((tmp_path / "btc_m5_high_signal.json").read_text(encoding="utf-8"))
        assert TOP_KEYS <= set(payload)
        assert payload["asset"] == "BTC"
        assert payload["mode"] == "high"
        assert payload["direction"] == "SHORT"
        assert payload["verdict"]
        assert payload["signalId"] == "btc-001"
        assert payload["plan"]["entry"] is not None
        assert payload["checklists"]["e1"]
