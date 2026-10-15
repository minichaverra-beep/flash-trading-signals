"""Resultados reales de operaciones registrados por la app (flash-signals).

Archivo: live/outcomes/<asset>_outcomes.jsonl — append-only, una línea por cambio.
Cada registro trae `historyId` y `revision`; si el resultado de una fila cambia la app
añade otro registro con `supersedes` = revision anterior. El vigente por historyId es
el de mayor `revision` (empate → el último del archivo).

Solo ganada/perdida cuentan para acierto/Brier; no_tomada se informa aparte.
Las capas ML / Neural se validan con estas predicciones vivas (fuera de muestra por
construcción: el modelo estaba entrenado antes de la señal) y solo si hay
≥ MIN_N_EFF muestras con predicción de esa capa y su Brier mejora a la constante.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from app.config import LIVE_DIR

SCHEMA_VERSION = 1
RESOLVED = ("ganada", "perdida")
_DIR_ENV = "TRADING_OUTCOMES_DIR"
MAX_LAYER_WEIGHT = 0.5

LAYER_SPECS = {
    "ml": ("mlPct", "ML"),
    "neural": ("neuralPct", "Neural"),
}


def outcomes_dir() -> Path:
    return Path(os.environ[_DIR_ENV]) if os.environ.get(_DIR_ENV) else LIVE_DIR / "outcomes"


def outcomes_path(asset: str | None) -> Path:
    from app.models.probability_calibration import asset_key

    return outcomes_dir() / f"{asset_key(asset).lower()}_outcomes.jsonl"


def _read_lines(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if isinstance(rec, dict) and rec.get("schemaVersion") == SCHEMA_VERSION and rec.get("historyId") is not None:
            rows.append(rec)
    return rows


def load_outcomes(asset: str | None = "BTC", path: Path | None = None) -> list[dict[str, Any]]:
    """Registro vigente por historyId (mayor revision; empate → último en el archivo)."""
    latest: dict[str, tuple[int, dict]] = {}
    for rec in _read_lines(path or outcomes_path(asset)):
        key = str(rec["historyId"])
        rev = int(rec.get("revision") or 0)
        prev = latest.get(key)
        if prev is None or rev >= prev[0]:
            latest[key] = (rev, rec)
    return [rec for _, rec in latest.values()]


def _label(rec: dict) -> int | None:
    res = ((rec.get("outcome") or {}).get("resultado") or "").lower()
    if res not in RESOLVED:
        return None
    return 1 if res == "ganada" else 0


def _prob(rec: dict, key: str) -> float | None:
    v = (rec.get("prediction") or {}).get(key)
    try:
        p = float(v) / 100.0
    except (TypeError, ValueError):
        return None
    return p if 0.0 <= p <= 1.0 else None


def _pairs(records: list[dict], key: str) -> tuple[list[int], list[float]]:
    ys, ps = [], []
    for rec in records:
        y = _label(rec)
        p = _prob(rec, key)
        if y is not None and p is not None:
            ys.append(y)
            ps.append(p)
    return ys, ps


def _brier_stats(ys: list[int], ps: list[float]) -> dict[str, Any]:
    n = len(ys)
    if not n:
        return {"n": 0, "hit_rate": None, "mean_pred": None, "brier": None, "brier_const": None, "skill": None}
    base = sum(ys) / n
    brier = sum((p - y) ** 2 for p, y in zip(ps, ys)) / n
    brier_c = sum((base - y) ** 2 for y in ys) / n
    skill = 1 - brier / brier_c if brier_c else None
    return {
        "n": n,
        "hit_rate": round(base, 4),
        "mean_pred": round(sum(ps) / n, 4),
        "brier": round(brier, 5),
        "brier_const": round(brier_c, 5),
        "skill": round(skill, 5) if skill is not None else None,
    }


def evaluate_outcomes(records: list[dict]) -> dict[str, Any]:
    """Acierto real vs probabilidad predicha (y por capa) sobre registros vigentes."""
    counts: dict[str, int] = {}
    pnl = 0.0
    for rec in records:
        res = str((rec.get("outcome") or {}).get("resultado") or "")
        counts[res] = counts.get(res, 0) + 1
        try:
            pnl += float((rec.get("outcome") or {}).get("pnlUsd") or 0.0)
        except (TypeError, ValueError):
            pass
    resolved = [r for r in records if _label(r) is not None]
    wins = sum(_label(r) for r in resolved)
    return {
        "n_records": len(records),
        "counts": counts,
        "n_resolved": len(resolved),
        "hit_rate": round(wins / len(resolved), 4) if resolved else None,
        "pnl_usd": round(pnl, 2),
        "probability": _brier_stats(*_pairs(records, "probabilityPct")),
        "layers": {name: _brier_stats(*_pairs(records, key)) for name, (key, _) in LAYER_SPECS.items()},
    }


def layer_validation(records: list[dict], min_n: int | None = None) -> dict[str, dict[str, Any]]:
    """`layers` del artefacto de calibración a partir de predicciones vivas con resultado."""
    from app.models.probability_calibration import MIN_N_EFF

    min_n = MIN_N_EFF if min_n is None else min_n
    out: dict[str, dict[str, Any]] = {}
    for name, (key, label) in LAYER_SPECS.items():
        st = _brier_stats(*_pairs(records, key))
        n = st["n"]
        cfg: dict[str, Any] = {"oos_ok": False, "weight": 0.0, "n": n, "min_n": min_n,
                               "brier": st["brier"], "brier_const": st["brier_const"], "skill": st["skill"]}
        if n == 0:
            cfg["reason"] = f"sin predicciones {label} con resultado registradas (0/{min_n})"
        elif n < min_n:
            cfg["reason"] = f"predicciones {label} con resultado insuficientes ({n}/{min_n})"
        elif not st["skill"] or st["skill"] <= 0:
            cfg["reason"] = f"{label} sin ventaja en vivo (Brier skill {st['skill']}) n={n}"
        else:
            cfg["oos_ok"] = True
            cfg["weight"] = round(min(MAX_LAYER_WEIGHT, st["skill"]), 3)
            cfg["reason"] = f"{label} validada en vivo n={n} · Brier skill {st['skill'] * 100:+.1f}%"
        out[name] = cfg
    return out


def apply_layers_to_calibration(calib: dict, records: list[dict], min_n: int | None = None) -> dict:
    """Sustituye calib['layers'] por la validación con resultados reales (muta y retorna)."""
    calib["layers"] = layer_validation(records, min_n=min_n)
    calib["layers_source"] = "live_outcomes"
    return calib
