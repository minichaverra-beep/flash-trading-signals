"""ML inference for BTC M5 E1 signal quality — backward-compatible wrapper."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from app.models.ml_signals import (
    SYMBOL_CONFIG,
    augment_categories as _augment_categories,
    extract_features,
    feature_config as _feature_config_ml,
    features_to_vector,
    model_available as _model_available,
    model_paths,
    predict_signal_quality,
    sl_pct_at_price as _sl_pct_at_price,
)

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
MODEL_PATH, FEATURES_PATH = model_paths("btc")

_cfg = SYMBOL_CONFIG["btc"]
SL_USD_REF = _cfg["sl_usd_ref"]
BTC_PRICE_REF = _cfg["price_ref"]
SL_PCT_DEFAULT = SL_USD_REF / BTC_PRICE_REF


def sl_pct_at_price(price: float) -> float:
    return _sl_pct_at_price("btc", price)


def _default_feature_names() -> list[str]:
    return _feature_config_ml("btc")["feature_names"]


def feature_config() -> dict:
    return _feature_config_ml("btc")


def model_available() -> bool:
    return _model_available("btc")


def load_model_and_config():
    from app.models.ml_signals import load_model_and_config as _load
    return _load("btc")


def augment_categories(
    categories: dict,
    data: dict,
    crt: dict | None = None,
    div: dict | None = None,
    dmi: dict | None = None,
    e2: dict | None = None,
) -> dict:
    return _augment_categories(categories, data, "btc", crt, div, dmi, e2)
