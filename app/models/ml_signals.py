"""ML inference for M5 E1 signal quality — BTC and US30 models."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import joblib
import numpy as np

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT

SYMBOL_CONFIG: dict[str, dict[str, Any]] = {
    "btc": {
        "model_file": "btc_signal_model.joblib",
        "features_file": "btc_signal_features.json",
        "sl_usd_ref": 9.0,
        "price_ref": 78000.0,
        "ml_source": "btc_signal_model.joblib",
    },
    "us30": {
        "model_file": "us30_signal_model.joblib",
        "features_file": "us30_signal_features.json",
        "sl_usd_ref": 9.0,
        "price_ref": 42000.0,
        "ml_source": "us30_signal_model.joblib",
        # SL ~$9: at Dow ~42000 with ~$1/point → ~9 pts; micro ($0.10/pt) → ~90 pts
        "sl_points_note": "~9 pts ($1/pt) o ~90 pts ($0.10/pt micro)",
    },
}


def _cfg(symbol: str) -> dict[str, Any]:
    key = symbol.lower()
    if key not in SYMBOL_CONFIG:
        raise ValueError(f"Unknown symbol for ML: {symbol}")
    return SYMBOL_CONFIG[key]


def model_paths(symbol: str) -> tuple[Path, Path]:
    c = _cfg(symbol)
    return MODELS_DIR / c["model_file"], MODELS_DIR / c["features_file"]


def sl_pct_at_price(symbol: str, price: float) -> float:
    c = _cfg(symbol)
    if price <= 0:
        return c["sl_usd_ref"] / c["price_ref"]
    return c["sl_usd_ref"] / price


def sl_points_estimate(symbol: str, price: float, dollars_per_point: float = 1.0) -> float:
    """Approximate SL distance in index points for fixed $9 account risk."""
    c = _cfg(symbol)
    if dollars_per_point <= 0:
        dollars_per_point = 1.0
    return c["sl_usd_ref"] / dollars_per_point


def _default_feature_names() -> list[str]:
    rule_names = [
        "rule_ny_session",
        "rule_e1_only",
        "rule_h1_bias",
        "rule_near_zone",
        "rule_2m5_confirm",
        "rule_rr_min",
        "rule_rsi_ok",
        "rule_crt_coherent",
    ]
    base = [
        "bias_bullish",
        "bias_bearish",
        "rsi_m5_norm",
        "rsi_h1_norm",
        "zone_dist_pct",
        "near_zone",
        "confirm_2m5",
        "in_ny_window",
        "pd_above_pdh",
        "pd_below_pdl",
        "pd_inside",
        "rr_available",
        "rules_pct_norm",
        "direction_long",
        "direction_short",
        "crt_fakeout_pdh",
        "crt_fakeout_pdl",
        "crt_pd_bull",
        "crt_pd_bear",
        "crt_pd_neutral",
        "crt_h1_completed_bull",
        "crt_h1_completed_bear",
        "crt_h1_pending_bull",
        "crt_h1_pending_bear",
        "crt_h1_inside",
        "dmi_bull",
        "dmi_bear",
        "rsi_div_bull",
        "rsi_div_bear",
    ]
    return base + rule_names


def feature_config(symbol: str = "btc") -> dict[str, Any]:
    c = _cfg(symbol)
    return {
        "feature_names": _default_feature_names(),
        "symbol": symbol,
        "sl_usd_ref": c["sl_usd_ref"],
        "price_ref": c["price_ref"],
        "sl_pct_ref": c["sl_usd_ref"] / c["price_ref"],
        "label_horizon_bars": 48,
        "rr_target": 2.0,
    }


def extract_features(
    data: dict,
    crt: dict | None = None,
    div: dict | None = None,
    dmi: dict | None = None,
    e2: dict | None = None,
) -> dict[str, float]:
    from app.models.btc_signal_categories import score_e1_rules_8

    s = data["setup"]
    direction = s["direction"]
    bias = data.get("bias_h1", "NEUTRAL")
    zone = data.get("zone") or {}
    dist = zone.get("dist_pct")
    rsi_m5 = data.get("rsi_m5")
    rsi_h1 = data.get("rsi_h1")
    price = data["price"]
    pdh, pdl = data.get("pdh"), data.get("pdl")

    _, _, rules_pct, rule_items = score_e1_rules_8(data, crt, div, dmi, e2)
    rule_map = {label: (1.0 if passed else 0.0) for label, passed, _ in rule_items}

    pd_above = pd_below = pd_inside = 0.0
    if pdh and pdl:
        if price > pdh:
            pd_above = 1.0
        elif price < pdl:
            pd_below = 1.0
        else:
            pd_inside = 1.0

    crt = crt or {}
    div = div or {}
    dmi = dmi or {}
    h1_state = crt.get("h1_state", "n/a")

    return {
        "bias_bullish": 1.0 if bias == "BULLISH" else 0.0,
        "bias_bearish": 1.0 if bias == "BEARISH" else 0.0,
        "rsi_m5_norm": (rsi_m5 / 100.0) if rsi_m5 is not None else 0.5,
        "rsi_h1_norm": (rsi_h1 / 100.0) if rsi_h1 is not None else 0.5,
        "zone_dist_pct": min((dist or 999.0) / 1.0, 1.0),
        "near_zone": 1.0 if dist is not None and dist <= 0.15 else 0.0,
        "confirm_2m5": 1.0 if (
            (direction == "LONG" and data.get("confirm_long"))
            or (direction == "SHORT" and data.get("confirm_short"))
        ) else 0.0,
        "in_ny_window": 1.0 if data.get("session", {}).get("in_ny_window") else 0.0,
        "pd_above_pdh": pd_above,
        "pd_below_pdl": pd_below,
        "pd_inside": pd_inside,
        "rr_available": 1.0 if s.get("rr") is not None else 0.0,
        "rules_pct_norm": rules_pct / 100.0,
        "direction_long": 1.0 if direction == "LONG" else 0.0,
        "direction_short": 1.0 if direction == "SHORT" else 0.0,
        "crt_fakeout_pdh": 1.0 if crt.get("fakeout_pdh") else 0.0,
        "crt_fakeout_pdl": 1.0 if crt.get("fakeout_pdl") else 0.0,
        "crt_pd_bull": 1.0 if crt.get("pd_reading") == "BULLISH" else 0.0,
        "crt_pd_bear": 1.0 if crt.get("pd_reading") == "BEARISH" else 0.0,
        "crt_pd_neutral": 1.0 if crt.get("pd_reading") == "NEUTRAL" else 0.0,
        "crt_h1_completed_bull": 1.0 if h1_state == "COMPLETED_BULL" else 0.0,
        "crt_h1_completed_bear": 1.0 if h1_state == "COMPLETED_BEAR" else 0.0,
        "crt_h1_pending_bull": 1.0 if h1_state == "PENDING_BULL" else 0.0,
        "crt_h1_pending_bear": 1.0 if h1_state == "PENDING_BEAR" else 0.0,
        "crt_h1_inside": 1.0 if h1_state == "INSIDE_RANGE" else 0.0,
        "dmi_bull": 1.0 if dmi.get("bias") == "BULL" else 0.0,
        "dmi_bear": 1.0 if dmi.get("bias") == "BEAR" else 0.0,
        "rsi_div_bull": 1.0 if div.get("type") == "BULLISH" else 0.0,
        "rsi_div_bear": 1.0 if div.get("type") == "BEARISH" else 0.0,
        "rule_ny_session": 1.0 if data.get("session", {}).get("in_ny_window") else 0.0,
        "rule_e1_only": rule_map.get("Solo E1", 0.0),
        "rule_h1_bias": rule_map.get("Tendencia H1 alineada", 0.0),
        "rule_near_zone": rule_map.get("Cerca de zona clave", 0.0),
        "rule_2m5_confirm": rule_map.get("2 velas M5 confirman", 0.0),
        "rule_rr_min": rule_map.get("R:R mínimo 1:2", 0.0),
        "rule_rsi_ok": rule_map.get("RSI no contradice", 0.0),
        "rule_crt_coherent": rule_map.get("Rango coherente", 0.0),
    }


def features_to_vector(feats: dict[str, float], feature_names: list[str]) -> np.ndarray:
    return np.array([feats.get(n, 0.0) for n in feature_names], dtype=np.float64)


def model_available(symbol: str = "btc") -> bool:
    model_path, features_path = model_paths(symbol)
    return model_path.is_file() and features_path.is_file()


def load_model_and_config(symbol: str = "btc") -> tuple[Any, dict]:
    model_path, features_path = model_paths(symbol)
    if not model_path.is_file() or not features_path.is_file():
        raise FileNotFoundError(f"Model not found for {symbol}. Run train script first.")
    model = joblib.load(model_path)
    cfg = json.loads(features_path.read_text(encoding="utf-8"))
    return model, cfg


def prob_to_grade(prob: float) -> str:
    if prob >= 0.72:
        return "A+"
    if prob >= 0.55:
        return "B"
    return "C"


def prob_to_confidence(prob: float) -> str:
    margin = abs(prob - 0.5)
    if margin >= 0.25:
        return "high"
    if margin >= 0.12:
        return "medium"
    return "low"


def predict_signal_quality(
    data_dict: dict,
    symbol: str = "btc",
    crt: dict | None = None,
    div: dict | None = None,
    dmi: dict | None = None,
    e2: dict | None = None,
) -> dict[str, Any]:
    model, cfg = load_model_and_config(symbol)
    feats = extract_features(data_dict, crt, div, dmi, e2)
    names = cfg.get("feature_names", _default_feature_names())
    x = features_to_vector(feats, names).reshape(1, -1)
    prob = float(model.predict_proba(x)[0, 1])
    return {
        "prob_win": round(prob, 4),
        "suggested_grade": prob_to_grade(prob),
        "confidence": prob_to_confidence(prob),
        "features_used": len(names),
    }


def augment_categories(
    categories: dict,
    data: dict,
    symbol: str = "btc",
    crt: dict | None = None,
    div: dict | None = None,
    dmi: dict | None = None,
    e2: dict | None = None,
) -> dict:
    if not model_available(symbol):
        return categories
    try:
        pred = predict_signal_quality(data, symbol, crt, div, dmi, e2)
    except Exception:
        return categories
    c = _cfg(symbol)
    out = dict(categories)
    out["ml_prob_win"] = pred["prob_win"]
    out["ml_grade"] = pred["suggested_grade"]
    out["ml_confidence"] = pred["confidence"]
    out["ml_source"] = c["ml_source"]
    return out
