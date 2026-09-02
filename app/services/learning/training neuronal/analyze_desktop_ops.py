"""
Scan operaciones - desktop and classify WIN/LOSS alignment with E1 gallery patterns.

Usage:
  python "training neuronal/analyze_desktop_ops.py"
  python "training neuronal/analyze_desktop_ops.py" --simple
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from neural_desktop_model import (
    BASE,
    CLASS_NAMES,
    DESKTOP_DIR,
    MODEL_PATH,
    TRAINING_DIR,
    build_labeled_dataset,
    extract_simple_features,
    load_torch_model,
    model_available,
    predict_simple,
    predict_torch_batch,
)

REPORT_PATH = TRAINING_DIR / "reports" / "desktop_analysis_report.md"


def alignment_note(known: str | None, predicted: str) -> str:
    if known is None:
        return "sin etiqueta conocida"
    if known == predicted:
        return "alineado"
    return "desalineado"


def strategy_compliance_notes(predicted_win: int, predicted_loss: int, aligned: int, misaligned: int) -> list[str]:
    notes = [
        "Las predicciones WIN deben parecerse a patrones §5.1 de `TRADING_OPERATIONS_DESKTOP_CONTEXT.md` "
        "(sweep+reclaim, breakout+retest, bias alineado, 2 velas M5, sesión NY).",
        "Predicciones LOSS suelen coincidir con §5.2 (bias contrario, cuchillo cayendo, fakeout, sobreoperar).",
        "El modelo aprende de **capturas históricas**; no sustituye precio en vivo ni las 8 reglas inmutables.",
    ]
    total = predicted_win + predicted_loss
    if total:
        win_pct = predicted_win / total * 100
        notes.append(f"Rentabilidad estimada de la galería (pred. WIN): **{win_pct:.1f}%** ({predicted_win}/{total}).")
    if misaligned:
        notes.append(
            f"Hay **{misaligned}** imágenes donde la predicción no coincide con la etiqueta del contexto — "
            "revisar manualmente o actualizar `data/desktop_labels.csv`."
        )
    return notes


def write_report(rows: list[dict], summary: dict) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Análisis desktop — operaciones E1",
        "",
        f"> Generado: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC",
        "",
        "## Resumen",
        "",
        f"| Métrica | Valor |",
        f"|---------|-------|",
        f"| Imágenes analizadas | {summary['total']} |",
        f"| Predicción WIN | {summary['pred_win']} |",
        f"| Predicción LOSS | {summary['pred_loss']} |",
        f"| Sin modelo / omitidas | {summary['skipped']} |",
        f"| Alineación con etiqueta conocida | {summary['aligned']} / {summary['labeled_known']} |",
        f"| Rentabilidad estimada (WIN%) | {summary.get('win_pct', 'n/a')}% |",
        "",
        "## Detalle por imagen",
        "",
        "| Archivo | Etiqueta conocida | Predicción | Confianza | Alineación | Fuente etiqueta |",
        "|---------|-------------------|------------|-----------|------------|-----------------|",
    ]

    for r in rows:
        conf = f"{r['confidence']*100:.1f}%" if r.get("confidence") is not None else "n/a"
        known = r.get("known_label") or "—"
        lines.append(
            f"| `{r['filename']}` | {known} | **{r['predicted']}** | {conf} | {r['alignment']} | {r['label_source']} |"
        )

    lines += [
        "",
        "## Cumplimiento estrategia E1",
        "",
    ]
    for note in summary.get("notes", []):
        lines.append(f"- {note}")

    lines += [
        "",
        "## Referencias",
        "",
        "- `TRADING_OPERATIONS_DESKTOP_CONTEXT.md` — galería WIN/LOSS",
        "- `TRADING_VISUAL_CONTEXT.md` — 8 reglas inmutables",
        "- `training neuronal/TRADING_NEURAL_STRATEGY.md` — arquitectura ML visión",
        "",
    ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def load_predictor(simple: bool):
    from neural_desktop_model import load_model_artifact

    if not model_available():
        return "none", None
    mode, artifact = load_model_artifact()
    if simple or mode == "simple":
        clf = artifact.get("classifier") if isinstance(artifact, dict) else artifact
        return "simple", clf
    if mode == "torch":
        model, ckpt, device = load_torch_model()
        return "torch", (model, ckpt, device)
    return "none", None


def main() -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    parser = argparse.ArgumentParser(description="Analyze desktop operations gallery")
    parser.add_argument("--simple", action="store_true", help="Force sklearn features (no torch)")
    parser.add_argument("--limit", type=int, default=0, help="Max images (0 = all)")
    args = parser.parse_args()

    items = build_labeled_dataset()
    if args.limit:
        items = items[: args.limit]

    mode, predictor = load_predictor(args.simple)

    # Include all trade screenshots; skip only balance/admin
    paths = [x.path for x in items if x.label_source != "skip_folder"]

    if not paths:
        print(f"No hay imágenes en {DESKTOP_DIR}")
        return 1

    if mode == "torch" and predictor:
        model, ckpt, device = predictor
        preds, confs = predict_torch_batch(model, paths, device, ckpt.get("image_size", 224))
    elif mode == "simple" and predictor:
        preds, confs = predict_simple(predictor, paths)
    else:
        print("WARN: Sin modelo entrenado. Ejecuta train_desktop_vision.py primero.")
        path_to_item_tmp = {x.path: x for x in items}
        preds = [path_to_item_tmp[p].label or "LOSS" for p in paths]
        confs = [0.5] * len(preds)

    path_to_item = {x.path: x for x in items}
    rows: list[dict] = []
    pred_win = pred_loss = aligned = labeled_known = 0

    for path, pred, conf in zip(paths, preds, confs):
        item = path_to_item[path]
        known = item.label
        if known in CLASS_NAMES:
            labeled_known += 1
            if known == pred:
                aligned += 1
        if pred == "WIN":
            pred_win += 1
        else:
            pred_loss += 1
        rows.append({
            "filename": item.filename,
            "known_label": known,
            "predicted": pred,
            "confidence": conf,
            "alignment": alignment_note(known, pred),
            "label_source": item.label_source,
        })

    total = len(rows)
    win_pct = round(pred_win / total * 100, 1) if total else 0.0
    summary = {
        "total": total,
        "pred_win": pred_win,
        "pred_loss": pred_loss,
        "skipped": len(items) - total,
        "aligned": aligned,
        "labeled_known": labeled_known,
        "win_pct": win_pct,
        "notes": strategy_compliance_notes(pred_win, pred_loss, aligned, labeled_known - aligned),
    }

    write_report(rows, summary)
    print("=" * 56)
    print(f"Reporte: {REPORT_PATH}")
    print(f"Imágenes: {total} | WIN pred: {pred_win} | LOSS pred: {pred_loss}")
    print(f"Alineación: {aligned}/{labeled_known} | WIN% estimado: {win_pct}%")
    print("=" * 56)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
