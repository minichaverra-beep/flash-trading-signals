"""
Desktop gallery vision model — E1 WIN/LOSS classification from TradingView screenshots.

Label sources (priority):
  1. data/desktop_labels.csv (manual override)
  2. docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md index tables
  3. Filename / subfolder heuristics (WIN, LOSS in name)
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

import numpy as np
from PIL import Image

# Este módulo vive en app/services/learning/training neuronal/
TRAINING_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = TRAINING_DIR.parents[3]  # Cursor Trading/
DESKTOP_DIR = _PROJECT_ROOT / "operaciones - desktop"
CONTEXT_MD = (
    _PROJECT_ROOT / "docs" / "strategy" / "TRADING_OPERATIONS_DESKTOP_CONTEXT.md"
)
LABELS_CSV = TRAINING_DIR / "data" / "desktop_labels.csv"
MODEL_PATH = TRAINING_DIR / "models" / "desktop_vision_model.pt"
IMAGE_CACHE = TRAINING_DIR / "data" / "desktop_image_list.json"

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
CLASS_NAMES = ("WIN", "LOSS")
CLASS_TO_IDX = {c: i for i, c in enumerate(CLASS_NAMES)}
IDX_TO_CLASS = {i: c for c, i in CLASS_TO_IDX.items()}

# balance/ and admin screenshots — excluded from training
SKIP_FOLDER_PARTS = {"balance"}
SKIP_NAME_PARTS = ("screenshot", "comparacion", "meta trader", "metatrader")


@dataclass
class LabeledImage:
    path: Path
    filename: str
    label: str | None  # WIN, LOSS, or None (SKIP/unknown)
    label_source: str
    relative: str


def scan_desktop_images(root: Path | None = None) -> list[Path]:
    """Return all image paths under operaciones - desktop."""
    root = root or DESKTOP_DIR
    if not root.is_dir():
        return []
    images: list[Path] = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS:
            images.append(p)
    return images


def _should_skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    parts_lower = [x.lower() for x in rel.parts[:-1]]
    if any(s in SKIP_FOLDER_PARTS for s in parts_lower):
        return True
    name_lower = path.name.lower()
    return any(s in name_lower for s in SKIP_NAME_PARTS)


def parse_labels_from_context(md_path: Path | None = None) -> dict[str, str]:
    """
    Parse WIN/LOSS/OPEN from docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md tables.
    OPEN is mapped to None (excluded from binary training).
    """
    md_path = md_path or CONTEXT_MD
    if not md_path.is_file():
        return {}

    text = md_path.read_text(encoding="utf-8")
    labels: dict[str, str] = {}

    for line in text.splitlines():
        if "|" not in line or line.strip().startswith("|---"):
            continue
        m = re.search(r"`([^`]+\.(?:png|jpg|jpeg|webp))`", line, re.I)
        if not m:
            continue
        fname = m.group(1)
        if "**LOSS**" in line:
            labels[fname] = "LOSS"
        elif "OPEN" in line.upper() and "**LOSS**" not in line:
            labels[fname] = "OPEN"
        elif re.search(r"\bWIN\b", line) and "**LOSS**" not in line:
            labels[fname] = "WIN"

    return labels


def load_manual_labels(csv_path: Path | None = None) -> dict[str, str]:
    """Load optional manual labels CSV: filename,label"""
    csv_path = csv_path or LABELS_CSV
    if not csv_path.is_file():
        return {}
    out: dict[str, str] = {}
    with csv_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fn = (row.get("filename") or row.get("file") or "").strip()
            lab = (row.get("label") or row.get("result") or "").strip().upper()
            if fn and lab in ("WIN", "LOSS", "OPEN", "SKIP"):
                out[Path(fn).name] = lab
    return out


def label_from_filename(filename: str) -> str | None:
    """Heuristic labels from filename tokens."""
    upper = filename.upper()
    if re.search(r"(?:^|[-_])LOSS(?:$|[-_.])", upper) or "-LOSS" in upper:
        return "LOSS"
    if re.search(r"(?:^|[-_])WIN(?:$|[-_.])", upper) or "-WIN" in upper:
        return "WIN"
    return None


def build_labeled_dataset(
    root: Path | None = None,
    context_md: Path | None = None,
    manual_csv: Path | None = None,
) -> list[LabeledImage]:
    """Assign labels to every image in the desktop gallery."""
    root = root or DESKTOP_DIR
    context = parse_labels_from_context(context_md)
    manual = load_manual_labels(manual_csv)
    items: list[LabeledImage] = []

    for path in scan_desktop_images(root):
        rel = str(path.relative_to(root))
        fname = path.name
        source = "none"
        label: str | None = None

        if _should_skip(path, root):
            label = None
            source = "skip_folder"
        elif fname in manual:
            lab = manual[fname]
            if lab in CLASS_NAMES:
                label = lab
                source = "manual_csv"
            else:
                label = None
                source = "manual_skip"
        elif fname in context:
            lab = context[fname]
            if lab in CLASS_NAMES:
                label = lab
                source = "context_md"
            else:
                label = None
                source = f"context_{lab.lower()}"
        else:
            guessed = label_from_filename(fname)
            if guessed:
                label = guessed
                source = "filename"

        items.append(
            LabeledImage(
                path=path,
                filename=fname,
                label=label,
                label_source=source,
                relative=rel,
            )
        )
    return items


def labeled_for_training(items: Iterable[LabeledImage]) -> list[LabeledImage]:
    return [x for x in items if x.label in CLASS_NAMES]


def cache_image_list(items: list[LabeledImage], cache_path: Path | None = None) -> None:
    import json

    cache_path = cache_path or IMAGE_CACHE
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    payload = [
        {
            "relative": x.relative,
            "filename": x.filename,
            "label": x.label,
            "label_source": x.label_source,
        }
        for x in items
    ]
    cache_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


# --- PyTorch model (optional import) ---

def build_cnn_model(
    architecture: str = "resnet18",
    num_classes: int = 2,
    pretrained: bool = True,
):
    """Transfer-learning backbone with replaced classifier head."""
    import torch
    import torch.nn as nn
    from torchvision import models

    weights = None
    if pretrained:
        if architecture == "resnet18":
            weights = models.ResNet18_Weights.IMAGENET1K_V1
        elif architecture == "mobilenet_v3_small":
            weights = models.MobileNet_V3_Small_Weights.IMAGENET1K_V1

    if architecture == "resnet18":
        model = models.resnet18(weights=weights)
        in_features = model.fc.in_features
        model.fc = nn.Sequential(
            nn.Dropout(0.25),
            nn.Linear(in_features, num_classes),
        )
    elif architecture == "mobilenet_v3_small":
        model = models.mobilenet_v3_small(weights=weights)
        in_features = model.classifier[-1].in_features
        model.classifier[-1] = nn.Linear(in_features, num_classes)
    else:
        raise ValueError(f"Unknown architecture: {architecture}")

    return model


def get_train_transforms(image_size: int = 224):
    from torchvision import transforms

    return transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.RandomHorizontalFlip(p=0.1),
        transforms.ColorJitter(brightness=0.1, contrast=0.1),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])


def get_eval_transforms(image_size: int = 224):
    from torchvision import transforms

    return transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])


class DesktopImageDataset:
    """Thin wrapper — real torch Dataset created at runtime if torch available."""

    def __init__(
        self,
        items: list[LabeledImage],
        transform: Callable | None = None,
    ):
        from torch.utils.data import Dataset

        class _DS(Dataset):
            def __len__(self_inner):
                return len(items)

            def __getitem__(self_inner, idx: int):
                item = items[idx]
                img = Image.open(item.path).convert("RGB")
                if transform:
                    img = transform(img)
                y = CLASS_TO_IDX[item.label]  # type: ignore[index]
                return img, y

        self.dataset = _DS()
        self.items = items


# --- Simple sklearn fallback (--simple) ---

def extract_simple_features(path: Path) -> np.ndarray:
    """Color histogram + edge density — lightweight CPU fallback."""
    img = Image.open(path).convert("RGB").resize((128, 128))
    arr = np.asarray(img, dtype=np.float32) / 255.0
    hist_r, _ = np.histogram(arr[:, :, 0], bins=16, range=(0, 1))
    hist_g, _ = np.histogram(arr[:, :, 1], bins=16, range=(0, 1))
    hist_b, _ = np.histogram(arr[:, :, 2], bins=16, range=(0, 1))
    gray = arr.mean(axis=2)
    gx = np.abs(np.diff(gray, axis=1)).mean()
    gy = np.abs(np.diff(gray, axis=0)).mean()
    purple_mask = (arr[:, :, 0] > 0.35) & (arr[:, :, 2] > 0.35) & (arr[:, :, 1] < 0.45)
    purple_ratio = float(purple_mask.mean())
    green_ratio = float((arr[:, :, 1] > arr[:, :, 0]).mean())
    red_ratio = float((arr[:, :, 0] > arr[:, :, 1]).mean())
    stats = np.array([gx, gy, purple_ratio, green_ratio, red_ratio], dtype=np.float32)
    return np.concatenate([hist_r, hist_g, hist_b, stats]).astype(np.float32)


def train_simple_classifier(X: np.ndarray, y: np.ndarray):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    clf = Pipeline([
        ("scaler", StandardScaler()),
        ("rf", RandomForestClassifier(n_estimators=120, max_depth=12, random_state=42, class_weight="balanced")),
    ])
    clf.fit(X, y)
    return clf


def predict_simple(clf, paths: list[Path]) -> tuple[list[str], list[float]]:
    X = np.vstack([extract_simple_features(p) for p in paths])
    probs = clf.predict_proba(X)
    preds = []
    confs = []
    for row in probs:
        idx = int(np.argmax(row))
        class_val = int(clf.classes_[idx])
        preds.append("WIN" if class_val == 0 else "LOSS")
        confs.append(float(row[idx]))
    return preds, confs


def load_model_artifact():
    """Load torch or joblib checkpoint from MODEL_PATH."""
    if not MODEL_PATH.is_file():
        return None, None
    try:
        import torch
        ckpt = torch.load(MODEL_PATH, map_location="cpu", weights_only=False)
        if isinstance(ckpt, dict) and "state_dict" in ckpt:
            return "torch", ckpt
    except Exception:
        pass
    from joblib import load
    return "simple", load(MODEL_PATH)


def model_available() -> bool:
    return MODEL_PATH.is_file()


def load_torch_model(device=None):
    import torch

    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")
    checkpoint = torch.load(MODEL_PATH, map_location=device, weights_only=False)
    arch = checkpoint.get("architecture", "resnet18")
    model = build_cnn_model(arch, num_classes=len(CLASS_NAMES), pretrained=False)
    model.load_state_dict(checkpoint["state_dict"])
    model.to(device)
    model.eval()
    return model, checkpoint, device


def predict_torch_batch(
    model,
    paths: list[Path],
    device,
    image_size: int = 224,
) -> tuple[list[str], list[float]]:
    import torch

    tfm = get_eval_transforms(image_size)
    tensors = []
    for p in paths:
        img = Image.open(p).convert("RGB")
        tensors.append(tfm(img))
    batch = torch.stack(tensors).to(device)
    with torch.no_grad():
        logits = model(batch)
        probs = torch.softmax(logits, dim=1).cpu().numpy()
    preds = [IDX_TO_CLASS[int(np.argmax(row))] for row in probs]
    confs = [float(np.max(row)) for row in probs]
    return preds, confs
