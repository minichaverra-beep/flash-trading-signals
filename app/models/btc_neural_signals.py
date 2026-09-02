"""Neural vision inference for BTC M5 — augments Categories from live chart PNG."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
TRAINING_DIR = TRAINING_NEURAL_DIR
MODEL_PATH = TRAINING_DIR / "models" / "desktop_vision_model.pt"
DEFAULT_CHART = LIVE_DIR / "btc_m5_chart.png"


def _training_on_path() -> None:
    p = str(TRAINING_DIR)
    if p not in sys.path:
        sys.path.insert(0, p)


def model_available() -> bool:
    return MODEL_PATH.is_file()


def load_neural_model():
    """Load torch ResNet18 (or sklearn fallback) from desktop_vision_model.pt."""
    _training_on_path()
    from neural_desktop_model import load_model_artifact, load_torch_model

    if not model_available():
        raise FileNotFoundError(
            f"Neural model not found at {MODEL_PATH}. "
            "Run: python -m ... or: python \"app/services/learning/training neuronal/train_desktop_vision.py\""
        )
    mode, artifact = load_model_artifact()
    if mode == "torch":
        model, ckpt, device = load_torch_model()
        return "torch", (model, ckpt, device)
    if mode == "simple":
        clf = artifact.get("classifier") if isinstance(artifact, dict) else artifact
        return "simple", clf
    raise RuntimeError("Unknown neural model format")


def prob_to_grade(prob_win: float) -> str:
    if prob_win >= 0.85:
        return "A+"
    if prob_win >= 0.70:
        return "B"
    if prob_win >= 0.50:
        return "B"
    return "C"


def prob_to_confidence(prob_win: float) -> str:
    margin = abs(prob_win - 0.5)
    if margin >= 0.30:
        return "high"
    if margin >= 0.15:
        return "medium"
    return "low"


def predict_chart_similarity(chart_path: Path) -> dict[str, Any]:
    """
    Classify live M5 chart vs desktop gallery WIN/LOSS patterns.

    Returns prob_win, prob_loss, grade (A+/B/C), confidence, gallery_aligned.
    """
    chart_path = Path(chart_path)
    if not chart_path.is_file():
        raise FileNotFoundError(f"Chart not found: {chart_path}")

    _training_on_path()
    from neural_desktop_model import predict_simple, predict_torch_batch

    mode, predictor = load_neural_model()

    if mode == "torch":
        model, ckpt, device = predictor
        preds, confs = predict_torch_batch(
            model, [chart_path], device, ckpt.get("image_size", 224),
        )
        pred_label = preds[0]
        conf = confs[0]
        prob_win = conf if pred_label == "WIN" else 1.0 - conf
        prob_loss = 1.0 - prob_win
    else:
        preds, confs = predict_simple(predictor, [chart_path])
        pred_label = preds[0]
        conf = confs[0]
        prob_win = conf if pred_label == "WIN" else 1.0 - conf
        prob_loss = 1.0 - prob_win

    prob_win = round(float(prob_win), 4)
    prob_loss = round(float(prob_loss), 4)

    return {
        "prob_win": prob_win,
        "prob_loss": prob_loss,
        "grade": prob_to_grade(prob_win),
        "confidence": prob_to_confidence(prob_win),
        "gallery_aligned": prob_win >= 0.70,
        "predicted_label": pred_label,
        "model_confidence": round(float(conf), 4),
    }


def augment_categories_neural(categories: dict, chart_path: Path | None) -> dict:
    """Add neural fields to categories dict (no-op if model/chart missing)."""
    if not model_available() or chart_path is None:
        return categories
    chart_path = Path(chart_path)
    if not chart_path.is_file():
        return categories
    try:
        pred = predict_chart_similarity(chart_path)
    except Exception:
        return categories
    out = dict(categories)
    out["neural_prob_win"] = pred["prob_win"]
    out["neural_prob_loss"] = pred["prob_loss"]
    out["neural_grade"] = pred["grade"]
    out["neural_confidence"] = pred["confidence"]
    out["neural_gallery_aligned"] = pred["gallery_aligned"]
    out["neural_source"] = "desktop_vision_model.pt"
    return out
