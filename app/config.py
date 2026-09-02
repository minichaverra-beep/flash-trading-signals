"""Rutas del proyecto — única fuente de verdad."""
from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LIVE_DIR = PROJECT_ROOT / "live"
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
# Código + artefactos vision viven bajo app/services/learning/ tras MVC
TRAINING_NEURAL_DIR = (
    PROJECT_ROOT / "app" / "services" / "learning" / "training neuronal"
)
# Galería / reportes bajo assets/ (carpetas raíz images|training ML ya no existen)
IMAGES_DIR = PROJECT_ROOT / "assets" / "images"
DESKTOP_OPS_DIR = IMAGES_DIR / "operaciones - desktop"
TRAINING_ML_DIR = PROJECT_ROOT / "assets" / "reportes ML"  # reportes estáticos; train → app/controllers
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
DOCS_DIR = PROJECT_ROOT / "docs"
DOCS_PROTOCOLS_DIR = DOCS_DIR / "protocols"
DOCS_STRATEGY_DIR = DOCS_DIR / "strategy"
