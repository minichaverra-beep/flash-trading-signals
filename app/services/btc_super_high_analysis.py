"""Super High tier — analyze user TradingView capture with entry/SL/TP."""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
OUT_DIR = LIVE_DIR
CAPTURE_NAMES = [
    "super_high_entry.png",
    "super_high_entry.jpg",
    "super_high_entry.jpeg",
    "super_high_entry.webp",
]
CAPTURES_DIR = OUT_DIR / "super_high_captures"
NOTES_PATH = OUT_DIR / "super_high_entry.md"
DEFAULT_OUTPUT = OUT_DIR / "btc_super_high_signal.md"

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

WEIGHT_NEURAL = 0.50
WEIGHT_ML = 0.30
WEIGHT_RULES = 0.20


def resolve_capture_path() -> Path | None:
    """Find user capture: fixed names first, then newest in super_high_captures/."""
    for name in CAPTURE_NAMES:
        p = OUT_DIR / name
        if p.is_file():
            return p
    if CAPTURES_DIR.is_dir():
        imgs = sorted(
            [f for f in CAPTURES_DIR.iterdir() if f.suffix.lower() in IMAGE_EXTENSIONS],
            key=lambda x: x.stat().st_mtime,
            reverse=True,
        )
        if imgs:
            return imgs[0]
    return None


def parse_manual_notes(path: Path | None = None) -> dict[str, Any]:
    """Parse optional super_high_entry.md for entry, SL, TP, direction."""
    path = path or NOTES_PATH
    out: dict[str, Any] = {
        "entry": None,
        "sl": None,
        "tp": None,
        "direction": None,
        "notes": "",
        "source": None,
    }
    if not path.is_file():
        return out

    text = path.read_text(encoding="utf-8")
    out["notes"] = text.strip()
    out["source"] = str(path.relative_to(BASE)) if path.is_relative_to(BASE) else str(path)

    patterns = {
        "entry": r"(?i)(?:entrada|entry)\s*[:=]\s*([\d.,]+)",
        "sl": r"(?i)(?:sl|stop)\s*[:=]\s*([\d.,]+)",
        "tp": r"(?i)(?:tp|take\s*profit|objetivo)\s*[:=]\s*([\d.,]+)",
        "direction": r"(?i)(?:direccion|direction|setup)\s*[:=]\s*(long|short|largo|corto)",
    }
    for key, pat in patterns.items():
        m = re.search(pat, text)
        if not m:
            continue
        val = m.group(1).strip()
        if key == "direction":
            val_u = val.upper()
            if val_u in ("LONG", "LARGO"):
                out["direction"] = "LONG"
            elif val_u in ("SHORT", "CORTO"):
                out["direction"] = "SHORT"
        else:
            try:
                out[key] = float(val.replace(",", ""))
            except ValueError:
                pass

    if out["direction"] is None:
        if re.search(r"(?i)\blong\b|\blargo\b", text):
            out["direction"] = "LONG"
        elif re.search(r"(?i)\bshort\b|\bcorto\b", text):
            out["direction"] = "SHORT"

    return out


def try_ocr(image_path: Path) -> dict[str, Any]:
    """Optional OCR with pytesseract; graceful fallback if unavailable."""
    out: dict[str, Any] = {
        "available": False,
        "text": "",
        "numbers": [],
        "entry_guess": None,
        "sl_guess": None,
        "tp_guess": None,
        "error": None,
    }
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        out["error"] = "pytesseract/PIL no instalados — omitido"
        return out

    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        out["available"] = True
        out["text"] = text.strip()[:500]
        nums = re.findall(r"\b(\d{2,3}[,.]?\d{0,2})\b", text)
        floats: list[float] = []
        for n in nums:
            try:
                v = float(n.replace(",", ""))
                if 1000 <= v <= 500000:
                    floats.append(v)
            except ValueError:
                continue
        out["numbers"] = sorted(set(floats))
        if len(out["numbers"]) >= 3:
            out["entry_guess"] = out["numbers"][1]
            out["sl_guess"] = out["numbers"][0]
            out["tp_guess"] = out["numbers"][-1]
        elif len(out["numbers"]) == 2:
            out["entry_guess"] = out["numbers"][0]
            out["sl_guess"] = out["numbers"][1]
    except Exception as exc:
        out["error"] = str(exc)
    return out


def analyze_visual_heuristics(image_path: Path) -> dict[str, Any]:
    """Simple green/red zone ratio and horizontal-line proxy via PIL."""
    out: dict[str, Any] = {
        "available": False,
        "green_ratio": None,
        "red_ratio": None,
        "bias_hint": "NEUTRAL",
        "horizontal_lines_proxy": 0,
        "score": 0.5,
        "error": None,
    }
    try:
        from PIL import Image
        import numpy as np
    except ImportError:
        out["error"] = "PIL/numpy no disponibles — omitido"
        return out

    try:
        img = Image.open(image_path).convert("RGB")
        arr = np.array(img.resize((320, 180)))
        r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
        green_mask = (g > r + 25) & (g > b + 25)
        red_mask = (r > g + 25) & (r > b + 25)
        total = arr.shape[0] * arr.shape[1]
        green_ratio = float(green_mask.sum()) / total
        red_ratio = float(red_mask.sum()) / total
        out["available"] = True
        out["green_ratio"] = round(green_ratio, 4)
        out["red_ratio"] = round(red_ratio, 4)

        if green_ratio > red_ratio * 1.3:
            out["bias_hint"] = "BULLISH"
        elif red_ratio > green_ratio * 1.3:
            out["bias_hint"] = "BEARISH"

        gray = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
        row_std = gray.std(axis=1)
        out["horizontal_lines_proxy"] = int((row_std < 8).sum())

        line_bonus = min(out["horizontal_lines_proxy"] / 40.0, 0.15)
        color_balance = 1.0 - abs(green_ratio - red_ratio)
        out["score"] = round(min(0.35 + line_bonus + color_balance * 0.25, 0.85), 4)
    except Exception as exc:
        out["error"] = str(exc)
    return out


def grade_from_probability(prob: float) -> str:
    if prob > 0.80:
        return "A+"
    if prob >= 0.65:
        return "B"
    if prob >= 0.50:
        return "C"
    return "NO_OPERAR"


def verdict_from_result(prob: float, grade: str, rules_ok: int, rules_total: int) -> str:
    if grade == "NO_OPERAR" or prob < 0.50:
        return "NO_OPERAR"
    if rules_ok < rules_total // 2:
        return "NO_OPERAR"
    if grade == "A+" and rules_ok >= 6:
        return "ENTRAR"
    if grade in ("A+", "B") and rules_ok >= 5:
        return "ENTRAR" if prob >= 0.70 else "ESPERAR"
    return "ESPERAR"


def compute_combined_probability(
    neural_prob: float | None,
    ml_prob: float | None,
    rules_pct: float | None,
    visual_score: float | None = None,
) -> tuple[float, dict[str, float]]:
    """Weighted success probability with graceful renormalization when sources missing."""
    weights: dict[str, float] = {}
    values: dict[str, float] = {}

    if neural_prob is not None:
        weights["neural"] = WEIGHT_NEURAL
        values["neural"] = neural_prob
    if ml_prob is not None:
        weights["ml"] = WEIGHT_ML
        values["ml"] = ml_prob
    if rules_pct is not None:
        weights["rules"] = WEIGHT_RULES
        values["rules"] = rules_pct / 100.0
    elif visual_score is not None and neural_prob is None and ml_prob is None:
        weights["visual"] = 1.0
        values["visual"] = visual_score

    if not weights:
        return 0.5, {}

    total_w = sum(weights.values())
    combined = sum(values[k] * weights[k] for k in weights) / total_w
    return round(combined, 4), {k: round(v, 4) for k, v in values.items()}


def _build_live_context(use_live: bool = True) -> dict[str, Any] | None:
    """Fetch or reuse live BTC M5 context for E1 rules cross-check."""
    if not use_live:
        return None

    snap_path = OUT_DIR / "btc_m5_snapshot.md"
    try:
        from app.controllers.analyze_btc_m5 import (
            fetch_klines,
            h1_bias,
            last_n_candle_summary,
            nearest_zone,
            pdh_pdl,
            rsi,
            session_flags,
            suggest_setup,
            swing_levels,
            two_candle_confirm,
        )
        from app.services.btc_high_analysis import build_high_context

        now = datetime.now(timezone.utc)
        m5 = fetch_klines("BTCUSDT", "5m", 200)
        h1 = fetch_klines("BTCUSDT", "1h", 200)
        if not m5:
            return None

        price = m5[-1]["close"]
        closes_m5 = [c["close"] for c in m5]
        closes_h1 = [c["close"] for c in h1]
        rsi_m5 = rsi(closes_m5)
        rsi_h1 = rsi(closes_h1)
        bias = h1_bias(h1)
        pdh, pdl = pdh_pdl(h1, now)
        sh, sl = swing_levels(m5)
        zone = nearest_zone(price, sh, sl)
        session = session_flags(now)
        confirm_long = two_candle_confirm(m5, "LONG")
        confirm_short = two_candle_confirm(m5, "SHORT")
        setup = suggest_setup(
            price, bias, zone, rsi_m5, confirm_long, confirm_short,
            session["in_ny_window"], pdh, pdl,
        )

        data = {
            "generated": now.strftime("%Y-%m-%d %H:%M"),
            "symbol": "BTCUSDT",
            "price": price,
            "session": session,
            "bias_h1": bias,
            "rsi_m5": rsi_m5,
            "rsi_h1": rsi_h1,
            "pdh": pdh,
            "pdl": pdl,
            "swing_highs": sh,
            "swing_lows": sl,
            "zone": zone,
            "confirm_long": confirm_long,
            "confirm_short": confirm_short,
            "setup": setup,
            "chart": False,
            "snapshot_ref": str(snap_path.relative_to(BASE)) if snap_path.is_file() else None,
        }
        high_data = build_high_context(data, m5, h1, last_n_candle_summary)
        return high_data
    except Exception:
        return None


def analyze_entry_capture(
    image_path: Path,
    live_data: dict | None = None,
    use_ml: bool = True,
    use_neural: bool = True,
    manual_notes: dict | None = None,
    bias_mode: str = "auto",
) -> dict[str, Any]:
    """
    Analyze user TradingView capture for success probability.

    Pipeline: neural vision, ML tabular, OCR (optional), visual heuristics, E1 rules.
    """
    image_path = Path(image_path)
    manual = manual_notes or parse_manual_notes()
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

    result: dict[str, Any] = {
        "generated": generated,
        "capture_path": str(image_path),
        "capture_name": image_path.name,
        "manual_notes": manual,
        "neural": None,
        "ml": None,
        "ocr": None,
        "visual": None,
        "rules": None,
        "combined_prob": 0.5,
        "grade": "C",
        "verdict": "ESPERAR",
        "key_reason": "",
        "invalidation": "",
        "component_probs": {},
        "warnings": [],
    }

    # Neural vision
    neural_prob = None
    if use_neural:
        try:
            from app.models.btc_neural_signals import model_available, predict_chart_similarity

            if model_available():
                result["neural"] = predict_chart_similarity(image_path)
                neural_prob = result["neural"]["prob_win"]
            else:
                result["warnings"].append("Modelo neural no encontrado — omitido")
        except Exception as exc:
            result["warnings"].append(f"Neural error: {exc}")

    # Live context + ML + rules
    ctx = live_data or _build_live_context(use_live=True)
    ml_prob = None
    rules_pct = None
    rules_ok = 0
    rules_total = 8

    if ctx:
        crt = ctx.get("crt")
        div = ctx.get("divergence")
        dmi = ctx.get("dmi")
        e2 = ctx.get("e2")
        from app.models.btc_signal_categories import score_e1_rules_8

        rules_ok, rules_total, rules_pct, rules_items = score_e1_rules_8(ctx, crt, div, dmi, e2)
        result["rules"] = {
            "ok": rules_ok,
            "total": rules_total,
            "pct": rules_pct,
            "items": rules_items,
            "bias_h1": ctx.get("bias_h1"),
            "session": ctx.get("session", {}).get("window"),
            "price": ctx.get("price"),
            "setup_direction": ctx.get("setup", {}).get("direction"),
            "crt_state": crt.get("h1_state") if crt else "n/a",
            "fakeout": crt.get("fakeout_note", "") if crt else "",
        }

        if use_ml:
            try:
                from app.models.btc_ml_signals import model_available as ml_ok, predict_signal_quality

                if ml_ok():
                    result["ml"] = predict_signal_quality(ctx, crt=crt, div=div, dmi=dmi, e2=e2)
                    ml_prob = result["ml"]["prob_win"]
                else:
                    result["warnings"].append("Modelo ML no encontrado — omitido")
            except Exception as exc:
                result["warnings"].append(f"ML error: {exc}")
    else:
        result["warnings"].append("Datos live BTC no disponibles — rules/ML omitidos")

    # OCR + visual heuristics
    result["ocr"] = try_ocr(image_path)
    result["visual"] = analyze_visual_heuristics(image_path)
    visual_score = result["visual"].get("score") if result["visual"] else None

    combined, components = compute_combined_probability(
        neural_prob, ml_prob, rules_pct, visual_score,
    )
    result["combined_prob"] = combined
    result["component_probs"] = components
    result["grade"] = grade_from_probability(combined)
    result["verdict"] = verdict_from_result(
        combined, result["grade"], rules_ok, rules_total,
    )

    # Bando + recomendación
    from app.models.btc_signal_categories import bando_usado_label, format_recomendacion

    direction = manual.get("direction")
    if bias_mode in ("bullish", "bearish"):
        bando_usado = bando_usado_label(bias_mode)
        if not direction:
            direction = "LONG" if bias_mode == "bullish" else "SHORT"
    elif direction == "LONG":
        bando_usado = "BULLISH"
    elif direction == "SHORT":
        bando_usado = "BEARISH"
    else:
        bando_usado = "AUTO"
        direction = direction or (result["rules"].get("setup_direction") if result.get("rules") else None) or "NONE"

    bando_mercado = result["rules"].get("bias_h1", "NEUTRAL") if result.get("rules") else "NEUTRAL"

    result["bando_usado"] = bando_usado
    result["bando_mercado"] = bando_mercado
    result["recomendacion"] = format_recomendacion(
        result["verdict"], direction or "NONE",
    )
    result["direction"] = direction or "NONE"
    result["bias_mode"] = bias_mode

    # Key reason + invalidation
    reasons: list[str] = []
    if neural_prob is not None:
        reasons.append(f"Neural {neural_prob * 100:.0f}% similitud WIN galería")
    if ml_prob is not None:
        reasons.append(f"ML {ml_prob * 100:.0f}% calidad señal")
    if rules_pct is not None:
        reasons.append(f"Reglas E1 {rules_ok}/{rules_total} ({rules_pct}%)")
    if manual.get("direction"):
        reasons.append(f"Dirección manual: {manual['direction']}")
    result["key_reason"] = " · ".join(reasons) if reasons else "Análisis limitado — confirmar en TradingView"

    invalidations: list[str] = []
    if result["rules"]:
        failed = [lbl for lbl, ok, _ in result["rules"]["items"] if not ok]
        if failed:
            invalidations.append(f"Reglas fallidas: {', '.join(failed[:3])}")
    if neural_prob is not None and neural_prob < 0.50:
        invalidations.append("Neural <50% WIN — baja similitud galería")
    if ml_prob is not None and ml_prob < 0.45:
        invalidations.append("ML <45% — sesgo histórico contra entrada")
    if manual.get("sl") and manual.get("entry"):
        invalidations.append(f"Invalidación técnica: cierre M5 más allá de SL {manual['sl']}")
    else:
        invalidations.append("Invalidación: ruptura SL dibujado en captura o contra bias H1")
    result["invalidation"] = " · ".join(invalidations)

    return result


def write_super_high_signal(path: Path, result: dict[str, Any]) -> None:
    """Write live/btc_super_high_signal.md from analysis result."""
    prob_pct = result["combined_prob"] * 100
    neural_pct = (
        f"{result['neural']['prob_win'] * 100:.0f}%"
        if result.get("neural")
        else "n/d"
    )
    ml_pct = (
        f"{result['ml']['prob_win'] * 100:.0f}%"
        if result.get("ml")
        else "n/d (no disponible)"
    )
    rules_line = "n/d"
    if result.get("rules"):
        r = result["rules"]
        rules_line = f"{r['ok']}/{r['total']} ({r['pct']}%)"

    manual = result.get("manual_notes") or {}
    lines = [
        "# BTC Super High Signal — Probabilidad de éxito (captura usuario)",
        "",
        f"> {result['generated']} UTC | Tier **Super High** | Captura: `{result['capture_name']}`",
        f"> Pipeline: Neural 50% · ML 30% · Rules 20% (renormalizado si falta fuente)",
        "",
        "---",
        "",
        "## Resumen ejecutivo",
        "",
        f"| Campo | Valor |",
        f"|-------|-------|",
        f"| **PROBABILIDAD ÉXITO** | **{prob_pct:.0f}%** |",
        f"| **GRADO** | **{result['grade']}** |",
        f"| **NEURAL** | {neural_pct} similar WIN galería |",
        f"| **ML** | {ml_pct} |",
        f"| **RULES** | {rules_line} |",
        f"| **VEREDICTO** | **{result['verdict']}** |",
        f"| **Bando usado** | **{result.get('bando_usado', 'AUTO')}** |",
        f"| **Bando mercado (H1)** | **{result.get('bando_mercado', 'NEUTRAL')}** |",
        f"| **Recomendación** | **{result.get('recomendacion', result['verdict'])}** |",
        f"| **RAZÓN CLAVE** | {result['key_reason']} |",
        f"| **INVALIDACIÓN** | {result['invalidation']} |",
        "",
        "---",
        "",
        "## Captura analizada",
        "",
        f"![Captura entrada]({Path(result['capture_path']).name})",
        "",
    ]

    if manual.get("entry") or manual.get("direction"):
        lines += [
            "### Notas manuales (`super_high_entry.md`)",
            "",
            f"- Entrada: {manual.get('entry', 'n/d')}",
            f"- SL: {manual.get('sl', 'n/d')}",
            f"- TP: {manual.get('tp', 'n/d')}",
            f"- Dirección: {manual.get('direction', 'n/d')}",
            "",
        ]

    if result.get("neural"):
        n = result["neural"]
        lines += [
            "## Neural galería (50% peso)",
            "",
            f"- Prob WIN: **{n['prob_win'] * 100:.1f}%** | Prob LOSS: {n['prob_loss'] * 100:.1f}%",
            f"- Grado neural: {n['grade']} | Confianza: {n['confidence']}",
            f"- Etiqueta predicha: {n.get('predicted_label', 'n/d')}",
            f"- Alineado galería WIN: {'SÍ' if n.get('gallery_aligned') else 'NO'}",
            "",
        ]

    if result.get("ml"):
        m = result["ml"]
        lines += [
            "## ML tabular (30% peso)",
            "",
            f"- Prob win: **{m['prob_win'] * 100:.1f}%** | Grado: {m['suggested_grade']}",
            f"- Confianza: {m['confidence']} | Features: {m.get('features_used', 'n/d')}",
            "",
        ]

    if result.get("rules"):
        r = result["rules"]
        lines += [
            "## Reglas E1 live (20% peso)",
            "",
            f"- Precio live: **{r.get('price', 'n/d')}** | Bias H1: {r.get('bias_h1', 'n/d')}",
            f"- Reloj (info): {r.get('session', 'n/d')} | Setup auto: {r.get('setup_direction', 'n/d')}",
            f"- CRT: {r.get('crt_state', 'n/a')} | {r.get('fakeout', '')}",
            "",
            "| Regla | OK | Nota |",
            "|-------|----|------|",
        ]
        for label, passed, note in r["items"]:
            lines.append(f"| {label} | {'SÍ' if passed else 'NO'} | {note} |")
        lines.append("")

    if result.get("ocr"):
        o = result["ocr"]
        lines += [
            "## OCR (opcional)",
            "",
            f"- Disponible: {'SÍ' if o.get('available') else 'NO'}",
        ]
        if o.get("numbers"):
            lines.append(f"- Números detectados: {o['numbers'][:8]}")
        if o.get("error"):
            lines.append(f"- Nota: {o['error']}")
        lines.append("")

    if result.get("visual"):
        v = result["visual"]
        lines += [
            "## Heurísticas visuales",
            "",
            f"- Bias hint: {v.get('bias_hint', 'n/d')}",
            f"- Verde/rojo: {v.get('green_ratio', 'n/d')} / {v.get('red_ratio', 'n/d')}",
            f"- Líneas horizontales proxy: {v.get('horizontal_lines_proxy', 0)}",
            f"- Score visual: {v.get('score', 'n/d')}",
            "",
        ]

    if result.get("warnings"):
        lines += ["## Advertencias", ""]
        for w in result["warnings"]:
            lines.append(f"- {w}")
        lines.append("")

    lines += [
        "---",
        "",
        "## Cursor Super High response",
        "",
        "Usar formato del protocolo `docs/protocols/TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md`:",
        "",
        "```",
        f"PROBABILIDAD ÉXITO: {prob_pct:.0f}%",
        f"GRADO: {result['grade']}",
        f"NEURAL: {neural_pct} similar WIN galería",
        f"ML: {ml_pct}",
        f"RULES: {rules_line}",
        f"VEREDICTO: {result['verdict']}",
        f"BANDO USADO: {result.get('bando_usado', 'AUTO')}",
        f"RECOMENDACIÓN: {result.get('recomendacion', result['verdict'])}",
        f"RAZÓN CLAVE: {result['key_reason']}",
        f"INVALIDACIÓN: {result['invalidation']}",
        "```",
        "",
        f"---",
        f"*Super High signal | {result['generated']} UTC*",
        "",
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
