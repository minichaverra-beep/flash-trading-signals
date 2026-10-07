"""
Calibra la Probabilidad de éxito E1 con replay histórico + walk-forward.

Usage:
  python -m app.controllers.calibrate_signals --asset btc
  python -m app.controllers.calibrate_signals --asset btc --evaluate-log
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone

import pandas as pd

from app.config import DATA_DIR
from app.models.probability_calibration import (
    FEATURE_LABELS,
    FEATURES,
    asset_key,
    build_replay_dataset,
    calibration_path,
    fit_calibration,
    prob_log_path,
)

_DATA_FILES = {"BTC": ("btcusdt_m5.parquet", "btcusdt_h1.parquet")}


def _load_candles(asset: str) -> tuple[list[dict], list[dict]]:
    key = asset_key(asset)
    if key not in _DATA_FILES:
        raise SystemExit(f"Calibración aún no disponible para {key} (solo BTC por ahora)")
    m5_name, h1_name = _DATA_FILES[key]
    m5 = pd.read_parquet(DATA_DIR / m5_name).to_dict("records")
    h1 = pd.read_parquet(DATA_DIR / h1_name).to_dict("records")
    return m5, h1


def _pct(v: float | None) -> str:
    return "n/d" if v is None else f"{v * 100:.1f}%"


def _rsi_zone_label(zone: str) -> str:
    lo, hi = (float(x) for x in zone.split(".."))
    def bound(ext: float, sign: int) -> str:
        return "" if abs(ext) > 10 else f"{50 + sign * 10 * ext:.0f}"
    long_txt = f"{bound(lo, 1) or '<'}–{bound(hi, 1) or '>'}".replace("<–", "<").replace("–>", "+")
    short_txt = f"{bound(hi, -1) or '<'}–{bound(lo, -1) or '>'}".replace("<–", "<").replace("–>", "+")
    return f"LONG {long_txt} · SHORT {short_txt}"


def write_report(calib: dict, path) -> None:
    oos = calib["oos"]
    lines = [
        f"# Calibración Probabilidad de éxito — {calib['asset']} E1",
        "",
        f"> Generado: {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC · "
        f"`python -m app.controllers.calibrate_signals --asset {calib['asset'].lower()}`",
        "",
        "| Parámetro | Valor |",
        "|-----------|-------|",
        f"| Periodo | {calib['period'][0][:10]} → {calib['period'][1][:10]} |",
        f"| Etiqueta | {calib['label']} |",
        f"| Señales con resultado | {calib['n']} (n_eff sin solape {calib['n_eff']}) |",
        f"| Timeouts excluidos | {calib['timeouts']} |",
        f"| Tasa base real | {_pct(calib['base_rate'])} |",
        f"| Riesgo SL mediano | {calib['risk_pct_median']}% del precio |",
        f"| Costo supuesto | {calib['cost_pct']}% del precio por operación |",
        f"| ¿Ventaja fuera de muestra? | **{'SÍ' if calib['has_edge'] else 'NO'}** "
        f"(Brier skill {oos['brier_skill_vs_constant'] * 100:+.1f}%) |",
        "",
        "## Métricas fuera de muestra (walk-forward, purga 48 velas)",
        "",
        "| Predictor | Brier | Log-loss | ECE |",
        "|-----------|-------|----------|-----|",
        f"| Modelo calibrado | {oos['model']['brier']} | {oos['model']['logloss']} | {oos['model']['ece']} |",
        f"| Constante (tasa base) | {oos['constant']['brier']} | {oos['constant']['logloss']} | {oos['constant']['ece']} |",
    ]
    if oos.get("legacy"):
        lines.append(
            f"| Heurística anterior | {oos['legacy']['brier']} | {oos['legacy']['logloss']} | {oos['legacy']['ece']} |"
        )
    lines += [
        "",
        "_Menor es mejor. La heurística anterior se mide sin acuerdo entre capas ni galería (no reproducibles en replay)._",
        "",
        "## Coeficientes (log-odds)",
        "",
        "| Variable | Coef | Media |",
        "|----------|------|-------|",
    ]
    for k in FEATURES:
        lines.append(f"| {FEATURE_LABELS[k]} (`{k}`) | {calib['coef'][k]:+.3f} | {calib['feature_means'][k]:.3f} |")
    lines.append(f"| Intercepto | {calib['intercept']:+.3f} | — |")

    for title, key in (("Curva de calibración — modelo", "calibration_model"),
                       ("Curva de calibración — heurística anterior", "calibration_legacy")):
        lines += ["", f"## {title}", "", "| Bucket | N | Predicho | Real |", "|--------|---|----------|------|"]
        for b in oos.get(key) or []:
            lines.append(f"| {b['bucket']} | {b['n']} | {_pct(b['pred'])} | {_pct(b['real'])} |")

    rs = calib["rule_stats"]
    lines += [
        "",
        "## Reglas — acierto real cuando cumple / no cumple",
        "",
        "| Regla | Cumple | Acierto si cumple | Acierto si no |",
        "|-------|--------|-------------------|---------------|",
    ]
    for k in ("confirm_2m5", "crt_coherent"):
        s = rs[k]
        lines.append(
            f"| {FEATURE_LABELS[k]} | {_pct(s['pass_rate'])} | {_pct(s['pass_wr'])} (n={s['pass_n']}) "
            f"| {_pct(s['fail_wr'])} (n={s['fail_n']}) |"
        )
    lines += ["", "| Zona premium/discount | N | Acierto |", "|---|---|---|"]
    for v, name in (("1", "a favor"), ("0", "equilibrio"), ("-1", "en contra")):
        s = rs["pd_favor"].get(v) or {}
        if s.get("n"):
            lines.append(f"| {name} | {s['n']} | {_pct(s['wr'])} |")
    lines += ["", "| RSI M5 (LONG · SHORT) | N | Acierto |", "|---|---|---|"]
    for zone, s in rs["rsi_ext_bins"].items():
        lines.append(f"| {_rsi_zone_label(zone)} | {s['n']} | {_pct(s['wr'])} |")
    lines += [
        "",
        "## Capas ML / Neural",
        "",
    ]
    for name, cfg in calib["layers"].items():
        lines.append(f"- **{name}:** {'entra' if cfg['oos_ok'] else 'no entra'} — {cfg['reason']}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def evaluate_log(asset: str) -> int:
    """Resuelve predicciones registradas con velas M5 y mide calibración en vivo."""
    from app.controllers.train_btc_signals import label_outcome

    path = prob_log_path(asset)
    if not path.is_file():
        print(f"Sin log de predicciones: {path}")
        return 1
    m5, _ = _load_candles(asset)
    times = [c["open_time"] for c in m5]
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    ys, ps = [], []
    import bisect

    for r in rows:
        try:
            ts = pd.Timestamp(r["generated_utc"], tz="UTC")
        except (TypeError, ValueError):
            continue
        i = bisect.bisect_right(times, ts)
        lab = label_outcome(r["direction"], r["price"], r.get("sl"), m5[i: i + 48], 48, rr=r.get("rr") or 2.0)
        if lab is not None:
            ys.append(lab)
            ps.append(r["p"])
    if not ys:
        print("Ninguna predicción resuelta todavía.")
        return 0
    base = sum(ys) / len(ys)
    brier = sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ys)
    brier_c = sum((base - y) ** 2 for y in ys) / len(ys)
    print(f"Resueltas {len(ys)}/{len(rows)} · acierto real {base * 100:.1f}% · "
          f"predicho medio {sum(ps) / len(ps) * 100:.1f}% · Brier {brier:.4f} vs constante {brier_c:.4f}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Calibrar Probabilidad de éxito E1")
    parser.add_argument("--asset", default="btc")
    parser.add_argument("--horizon", type=int, default=48)
    parser.add_argument("--stride", type=int, default=3)
    parser.add_argument("--cooldown", type=int, default=12)
    parser.add_argument("--evaluate-log", action="store_true")
    args = parser.parse_args()

    if args.evaluate_log:
        return evaluate_log(args.asset)

    t0 = time.time()
    m5, h1 = _load_candles(args.asset)
    print(f"Replay {asset_key(args.asset)}: M5={len(m5)} H1={len(h1)} …")
    rows = build_replay_dataset(m5, h1, horizon=args.horizon, stride=args.stride, cooldown=args.cooldown)
    calib = fit_calibration(rows, asset=args.asset, horizon=args.horizon)
    out = calibration_path(args.asset)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(calib, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    report = DATA_DIR / f"{asset_key(args.asset).lower()}_prob_calibration_report.md"
    write_report(calib, report)
    oos = calib["oos"]
    print(f"n={calib['n']} n_eff={calib['n_eff']} base={calib['base_rate'] * 100:.1f}% "
          f"has_edge={calib['has_edge']} skill={oos['brier_skill_vs_constant'] * 100:+.2f}% "
          f"({time.time() - t0:.0f}s)")
    print(f"Artefacto: {out}\nReporte: {report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
