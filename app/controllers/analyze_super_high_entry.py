"""
Analyze user TradingView capture (entry/SL/TP) for Super High tier.

Usage:
  python -m app.controllers.analyze_super_high_entry
  python -m app.controllers.analyze_super_high_entry --ml --neural
  python -m app.controllers.analyze_super_high_entry --capture live/super_high_entry.png

Input:
  live/super_high_entry.png (or .jpg/.jpeg/.webp)
  live/super_high_captures/ (first image fallback)
  live/super_high_entry.md (optional manual notes)

Output:
  live/btc_super_high_signal.md
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
OUT_DIR = LIVE_DIR
DESKTOP_DIR = BASE / "operaciones - desktop"

from app.services.btc_super_high_analysis import (  # noqa: E402
    DEFAULT_OUTPUT,
    analyze_entry_capture,
    parse_manual_notes,
    resolve_capture_path,
    write_super_high_signal,
)


def _copy_smoke_test_capture(dest: Path) -> bool:
    """Copy a WIN image from desktop gallery for smoke test."""
    candidates: list[Path] = []
    if DESKTOP_DIR.is_dir():
        for pat in ("BTC-01-07-26.png", "BTC-02-06-26.png", "BTC*.png"):
            candidates.extend(DESKTOP_DIR.glob(pat))
        if not candidates:
            candidates = list(DESKTOP_DIR.rglob("*.png"))[:20]
    chart = OUT_DIR / "btc_m5_chart.png"
    if chart.is_file():
        candidates.insert(0, chart)

    for src in candidates:
        if src.is_file():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            print(f"Smoke test: copiado {src.name} -> {dest}")
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Super High — analizar captura entry/SL/TP")
    parser.add_argument("--capture", type=str, default=None, help="Ruta a captura (default: live/super_high_entry.*)")
    parser.add_argument("--ml", action="store_true", help="Incluir ML tabular")
    parser.add_argument("--neural", action="store_true", help="Incluir neural galería")
    parser.add_argument("--no-live", action="store_true", help="Omitir fetch live BTC para rules/ML")
    parser.add_argument("--smoke-test", action="store_true", help="Copiar imagen WIN si falta captura")
    parser.add_argument("--output", type=str, default=str(DEFAULT_OUTPUT))
    parser.add_argument(
        "--bias",
        choices=("auto", "bullish", "bearish"),
        default="auto",
        help="Sesgo forzado: bullish (LONG) | bearish (SHORT) | auto",
    )
    args = parser.parse_args()

    capture: Path | None = Path(args.capture) if args.capture else resolve_capture_path()

    if capture is None or not capture.is_file():
        if args.smoke_test:
            dest = OUT_DIR / "super_high_entry.png"
            if not _copy_smoke_test_capture(dest):
                print("ERROR: no hay captura ni imagen WIN para smoke test")
                return 1
            capture = dest
        else:
            print("ERROR: no se encontró captura.")
            print("  Guarda tu screenshot en: live/super_high_entry.png")
            print("  O en: live/super_high_captures/")
            print("  Usa --smoke-test para probar con imagen WIN de galería")
            return 1

    use_ml = args.ml
    use_neural = args.neural
    if not use_ml and not use_neural:
        use_ml = True
        use_neural = True

    live_data = None
    if not args.no_live:
        from app.services.btc_super_high_analysis import _build_live_context
        live_data = _build_live_context(use_live=True)

    manual = parse_manual_notes()
    result = analyze_entry_capture(
        capture,
        live_data=live_data,
        use_ml=use_ml,
        use_neural=use_neural,
        manual_notes=manual,
        bias_mode=args.bias,
    )

    out_path = Path(args.output)
    write_super_high_signal(out_path, result)

    prob = result["combined_prob"] * 100
    print("=" * 56)
    print(f"Super High | {capture.name}")
    print(f"PROBABILIDAD ÉXITO: {prob:.0f}%")
    print(f"GRADO: {result['grade']} | VEREDICTO: {result['verdict']}")
    print(f"BANDO: {result.get('bando_usado', 'AUTO')} | REC: {result.get('recomendacion', result['verdict'])}")
    if result.get("neural"):
        print(f"NEURAL: {result['neural']['prob_win'] * 100:.0f}% WIN")
    if result.get("ml"):
        print(f"ML: {result['ml']['prob_win'] * 100:.0f}%")
    if result.get("rules"):
        r = result["rules"]
        print(f"RULES: {r['ok']}/{r['total']} ({r['pct']}%)")
    if result.get("warnings"):
        for w in result["warnings"]:
            print(f"WARN: {w}")
    print(f"Output: {out_path}")
    print("=" * 56)
    print("Cursor -> @live/btc_super_high_signal.md @docs/protocols/TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
