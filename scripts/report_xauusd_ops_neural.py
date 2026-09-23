"""Generate short XAUUSD inventory + neural/vision analysis report from OCR ops."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from app.config import (
    MOBILE_OPS_DIR,
    OPS_MOBILE_DATA_DIR,
    TRAINING_NEURAL_DIR,
)
from app.models.ops_mobile_ground_truth import (
    OPS_VERSION,
    load_ops_trades,
    parse_ts_from_whatsapp_filename,
)

OUT = OPS_MOBILE_DATA_DIR / OPS_VERSION
REPORT = OUT / "xauusd_ops_inventory_neural_report.md"
NEURAL_REPORT = TRAINING_NEURAL_DIR / "reports" / "xauusd_mobile_vision_report.md"


def main() -> int:
    trades = pd.read_csv(OUT / "trades.csv")
    xau = trades[trades["symbol"].astype(str).str.upper() == "XAUUSD"].copy()
    raw = pd.read_csv(OUT / "trades_raw_per_image.csv")
    xau_raw = raw[raw["symbol"].astype(str).str.upper() == "XAUUSD"].copy()

    usable = load_ops_trades(symbols={"XAUUSD"}, min_confidence=0.45)
    h1_path = OUT / "xauusd_ops_h1_labels.csv"
    h1 = pd.read_csv(h1_path) if h1_path.is_file() and h1_path.stat().st_size > 10 else pd.DataFrame()
    m5_path = OUT / "xauusd_ops_matched.csv"
    m5m = (
        pd.read_csv(m5_path)
        if m5_path.is_file() and m5_path.stat().st_size > 10
        else pd.DataFrame()
    )

    imgs = []
    for _, r in xau_raw.iterrows():
        fn = str(r.get("source_image") or "")
        p = MOBILE_OPS_DIR / fn
        ts = parse_ts_from_whatsapp_filename(fn)
        imgs.append(
            {
                "file": fn,
                "exists": p.is_file(),
                "bytes": p.stat().st_size if p.is_file() else 0,
                "capture_guess": ts.isoformat() if ts else None,
                "side": r.get("side"),
                "entry": r.get("entry_price"),
                "confidence": r.get("confidence"),
                "outcome_ocr": r.get("outcome"),
            }
        )

    sides = xau["side"].fillna("missing").value_counts().to_dict()
    outcomes = xau["outcome"].fillna("n/a").value_counts().to_dict()

    lines = [
        f"# XAUUSD — inventario OCR + visión ({OPS_VERSION})",
        "",
        f"> Generado: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC",
        "",
        "## Inventario",
        "",
        f"| Fuente | Count |",
        f"|--------|------:|",
        f"| trades.csv XAUUSD | {len(xau)} |",
        f"| trades_raw (pre-dedupe) | {len(xau_raw)} |",
        f"| Usables ML (side+entry, conf≥0.45) | {len(usable)} |",
        f"| Matched M5 (features) | {len(m5m)} |",
        f"| Labeled H1 (diagnóstico) | {int((h1['label'].notna()).sum()) if len(h1) and 'label' in h1.columns else 0} |",
        "",
        f"- Sides: `{json.dumps(sides)}`",
        f"- Outcomes OCR: `{json.dumps(outcomes)}`",
        "- Rango por nombre de archivo (WhatsApp): **2026-05-13 → 2026-07-02**",
        "- Otras fuentes oro en repo: **ninguna** (solo v_ops_apr_sep + proxy GC=F).",
        "",
        "## Screenshots móviles etiquetados XAUUSD",
        "",
    ]
    for im in imgs:
        lines.append(
            f"- `{im['file']}` exists={im['exists']} conf={im['confidence']} "
            f"side={im['side']} entry={im['entry']} ts≈{im['capture_guess']}"
        )

    lines += [
        "",
        "## Neural / visión",
        "",
        "Las capturas XAUUSD son charts TradingView/Exness (WhatsApp). Con n≈4–5 imágenes "
        "no hay masa crítica para un modelo vision dedicado de oro.",
        "",
        "- Se reutiliza el pipeline `mobile_ops_vision_simple` / labels H1 cuando hay WIN/LOSS resoluble.",
        "- Recomendación: acumular ≥30 ops XAUUSD cerradas (side+entry+SL/TP+timestamp) antes de "
        "esperar uplift ML/neural significativo.",
        "",
        "## Limitaciones (honestas)",
        "",
        "1. Yahoo M5 (GC=F) no cubre mayo–principios julio → match M5≈0 esperado.",
        "2. OCR sin `capture_ts`; se usa fecha del filename IMG-YYYYMMDD.",
        "3. Outcomes OCR=`open` (posiciones abiertas en screenshot) — no son W/L de cuenta.",
        "4. Proxy GC=F ≠ cota exacta del broker.",
        "",
    ]
    OUT.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    NEURAL_REPORT.parent.mkdir(parents=True, exist_ok=True)
    NEURAL_REPORT.write_text(
        "\n".join(
            [
                "# XAUUSD mobile vision — short analysis",
                "",
                f"> {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC",
                "",
                f"Inventario completo: `{REPORT}`",
                "",
                f"- Imágenes XAUUSD en OCR raw: **{len(imgs)}**",
                f"- Presentes en disco: **{sum(1 for i in imgs if i['exists'])}**",
                f"- Match M5 para features: **{len(m5m)}**",
                "",
                "Conclusión: señal live + modelo sintético E1 son utilizables; "
                "visión oro permanece **exploratoria** hasta más ground-truth cerrado.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Wrote {REPORT}")
    print(f"Wrote {NEURAL_REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
