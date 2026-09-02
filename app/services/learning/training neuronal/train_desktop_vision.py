"""
Train desktop gallery vision classifier (WIN vs LOSS) for E1 strategy screenshots.

Usage:
  python "training neuronal/train_desktop_vision.py"
  python "training neuronal/train_desktop_vision.py" --quick
  python "training neuronal/train_desktop_vision.py" --simple
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from neural_desktop_model import (
    BASE,
    CLASS_NAMES,
    DESKTOP_DIR,
    MODEL_PATH,
    TRAINING_DIR,
    build_cnn_model,
    build_labeled_dataset,
    cache_image_list,
    extract_simple_features,
    get_eval_transforms,
    get_train_transforms,
    labeled_for_training,
    train_simple_classifier,
)

REPORT_PATH = TRAINING_DIR / "reports" / "training_report.md"


def write_training_report(
    *,
    mode: str,
    metrics: dict,
    n_total: int,
    n_labeled: int,
    label_breakdown: dict,
    elapsed: float,
    args: argparse.Namespace,
) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Informe de entrenamiento — Visión desktop E1",
        "",
        f"> Generado: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC",
        "",
        "## Configuración",
        "",
        "| Parámetro | Valor |",
        "|-----------|-------|",
        f"| Modo | {mode} |",
        f"| Carpeta fuente | `{DESKTOP_DIR}` |",
        f"| Imágenes totales | {n_total} |",
        f"| Imágenes etiquetadas | {n_labeled} |",
        f"| Épocas | {args.epochs} |",
        f"| Arquitectura | {getattr(args, 'architecture', 'n/a')} |",
        f"| Tiempo | {elapsed:.1f}s |",
        "",
        "### Etiquetas por clase",
        "",
        "| Clase | N |",
        "|-------|---|",
    ]
    for c in CLASS_NAMES:
        lines.append(f"| {c} | {label_breakdown.get(c, 0)} |")

    lines += [
        "",
        "## Métricas (hold-out 20%)",
        "",
        f"- **Accuracy:** {metrics.get('accuracy', 'n/a')}",
        f"- **Precision WIN:** {metrics.get('precision_win', 'n/a')}",
        f"- **Recall WIN:** {metrics.get('recall_win', 'n/a')}",
        f"- **Muestras train:** {metrics.get('train_n', 'n/a')}",
        f"- **Muestras val:** {metrics.get('val_n', 'n/a')}",
        "",
        "## Notas",
        "",
        "- Etiquetas desde `TRADING_OPERATIONS_DESKTOP_CONTEXT.md` (+ CSV manual opcional).",
        "- El modelo **complementa** reglas E1; no reemplaza validación en TradingView.",
        "- Re-entrenar al añadir capturas nuevas en `operaciones - desktop`.",
        "",
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def split_train_val(items, val_ratio: float = 0.2, seed: int = 42):
    rng = random.Random(seed)
    by_class: dict[str, list] = {c: [] for c in CLASS_NAMES}
    for it in items:
        by_class[it.label].append(it)
    train, val = [], []
    for c in CLASS_NAMES:
        pool = by_class[c][:]
        rng.shuffle(pool)
        n_val = max(1, int(len(pool) * val_ratio)) if len(pool) >= 3 else (1 if len(pool) > 1 else 0)
        val.extend(pool[:n_val])
        train.extend(pool[n_val:])
    rng.shuffle(train)
    rng.shuffle(val)
    return train, val


def train_torch(args) -> dict:
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader
    from sklearn.metrics import accuracy_score, precision_score, recall_score

    from neural_desktop_model import DesktopImageDataset

    all_items = build_labeled_dataset()
    cache_image_list(all_items)
    train_items = labeled_for_training(all_items)

    if args.quick and len(train_items) > 24:
        rng = random.Random(42)
        train_items = rng.sample(train_items, 24)

    if len(train_items) < 4:
        raise RuntimeError(
            f"Solo {len(train_items)} imágenes etiquetadas. "
            "Revisa TRADING_OPERATIONS_DESKTOP_CONTEXT.md o data/desktop_labels.csv"
        )

    train_split, val_split = split_train_val(train_items, val_ratio=0.2)
    label_breakdown = {c: sum(1 for x in train_items if x.label == c) for c in CLASS_NAMES}

    device = torch.device("cuda" if torch.cuda.is_available() and not args.cpu else "cpu")
    image_size = 160 if args.quick else 224
    train_ds = DesktopImageDataset(train_split, get_train_transforms(image_size)).dataset
    val_ds = DesktopImageDataset(val_split, get_eval_transforms(image_size)).dataset

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, num_workers=0)

    model = build_cnn_model(args.architecture, num_classes=2, pretrained=True).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    best_acc = 0.0
    best_state = None
    epochs = 2 if args.quick else args.epochs

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            out = model(xb)
            loss = criterion(out, yb)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * len(yb)

        model.eval()
        y_true, y_pred = [], []
        with torch.no_grad():
            for xb, yb in val_loader:
                xb = xb.to(device)
                logits = model(xb)
                preds = logits.argmax(dim=1).cpu().numpy()
                y_pred.extend(preds.tolist())
                y_true.extend(yb.numpy().tolist())

        acc = accuracy_score(y_true, y_pred) if y_true else 0.0
        print(f"Epoch {epoch + 1}/{epochs} loss={running_loss / max(len(train_split), 1):.4f} val_acc={acc:.3f}")
        if acc >= best_acc:
            best_acc = acc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    if best_state:
        model.load_state_dict(best_state)

    model.eval()
    y_true, y_pred = [], []
    with torch.no_grad():
        for xb, yb in val_loader:
            xb = xb.to(device)
            preds = model(xb).argmax(dim=1).cpu().numpy()
            y_pred.extend(preds.tolist())
            y_true.extend(yb.numpy().tolist())

    metrics = {
        "accuracy": round(float(accuracy_score(y_true, y_pred)), 4) if y_true else 0.0,
        "precision_win": round(float(precision_score(y_true, y_pred, pos_label=0, zero_division=0)), 4),
        "recall_win": round(float(recall_score(y_true, y_pred, pos_label=0, zero_division=0)), 4),
        "train_n": len(train_split),
        "val_n": len(val_split),
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "state_dict": model.state_dict(),
            "architecture": args.architecture,
            "class_names": list(CLASS_NAMES),
            "image_size": image_size,
            "mode": "torch",
            "metrics": metrics,
            "trained_at": datetime.now(timezone.utc).isoformat(),
        },
        MODEL_PATH,
    )

    return {
        "mode": f"torch/{args.architecture}",
        "metrics": metrics,
        "n_total": len(all_items),
        "n_labeled": len(train_items),
        "label_breakdown": label_breakdown,
    }


def train_simple(args) -> dict:
    from sklearn.metrics import accuracy_score, precision_score, recall_score
    from joblib import dump

    all_items = build_labeled_dataset()
    cache_image_list(all_items)
    train_items = labeled_for_training(all_items)

    if args.quick and len(train_items) > 30:
        train_items = random.Random(42).sample(train_items, 30)

    if len(train_items) < 4:
        raise RuntimeError(f"Solo {len(train_items)} imágenes etiquetadas para entrenar.")

    train_split, val_split = split_train_val(train_items)
    label_breakdown = {c: sum(1 for x in train_items if x.label == c) for c in CLASS_NAMES}

    X_train = np.vstack([extract_simple_features(x.path) for x in train_split])
    y_train = np.array([0 if x.label == "WIN" else 1 for x in train_split])
    X_val = np.vstack([extract_simple_features(x.path) for x in val_split])
    y_val = np.array([0 if x.label == "WIN" else 1 for x in val_split])

    clf = train_simple_classifier(X_train, y_train)
    y_pred = clf.predict(X_val)

    metrics = {
        "accuracy": round(float(accuracy_score(y_val, y_pred)), 4),
        "precision_win": round(float(precision_score(y_val, y_pred, pos_label=0, zero_division=0)), 4),
        "recall_win": round(float(recall_score(y_val, y_pred, pos_label=0, zero_division=0)), 4),
        "train_n": len(train_split),
        "val_n": len(val_split),
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    dump(
        {
            "classifier": clf,
            "mode": "simple",
            "class_names": list(CLASS_NAMES),
            "metrics": metrics,
            "trained_at": datetime.now(timezone.utc).isoformat(),
        },
        MODEL_PATH,
    )

    return {
        "mode": "simple/sklearn",
        "metrics": metrics,
        "n_total": len(all_items),
        "n_labeled": len(train_items),
        "label_breakdown": label_breakdown,
    }


def main() -> int:
    # Allow running from repo root or from training neuronal/
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    parser = argparse.ArgumentParser(description="Train desktop WIN/LOSS vision model")
    parser.add_argument("--quick", action="store_true", help="Small subset + few epochs")
    parser.add_argument("--simple", action="store_true", help="sklearn on hand-crafted features (no torch)")
    parser.add_argument("--architecture", choices=("resnet18", "mobilenet_v3_small"), default="resnet18")
    parser.add_argument("--epochs", type=int, default=8)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--cpu", action="store_true", help="Force CPU even if CUDA available")
    args = parser.parse_args()

    if args.quick:
        args.epochs = min(args.epochs, 3)
        args.batch_size = min(args.batch_size, 4)

    t0 = time.time()
    try:
        if args.simple:
            result = train_simple(args)
        else:
            try:
                import torch  # noqa: F401
            except ImportError:
                print("WARN: torch no instalado — usando modo --simple")
                args.simple = True
                result = train_simple(args)
            else:
                result = train_torch(args)

        elapsed = time.time() - t0
        write_training_report(
            mode=result["mode"],
            metrics=result["metrics"],
            n_total=result["n_total"],
            n_labeled=result["n_labeled"],
            label_breakdown=result["label_breakdown"],
            elapsed=elapsed,
            args=args,
        )

        print("=" * 56)
        print(f"Modelo:   {MODEL_PATH}")
        print(f"Reporte:  {REPORT_PATH}")
        print(f"Accuracy: {result['metrics']['accuracy']}")
        print(f"Imágenes: {result['n_total']} total, {result['n_labeled']} etiquetadas")
        print(f"Tiempo:   {elapsed:.1f}s")
        print("=" * 56)
        return 0
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
