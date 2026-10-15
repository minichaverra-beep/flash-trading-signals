"""JSON estructurado de la señal High (live/<asset>_m5_high_signal.json).

Mismo contenido que el .md pero versionado y serializable para la app
(flash-signals). Solo lo que el motor calculó: lo ausente va como null.
Escritura atómica (temp + replace) para que el lector nunca vea medio archivo.
"""
from __future__ import annotations

import json
import math
import os
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1

_SCALARS = (str, int, float, bool, type(None))


def to_jsonable(value: Any) -> Any:
    """numpy/tuplas/Path/datetime → tipos JSON; NaN/inf → None."""
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, int):
        return int(value)
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    if isinstance(value, dict):
        return {str(k): to_jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [to_jsonable(v) for v in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    item = getattr(value, "item", None)
    if callable(item):
        try:
            return to_jsonable(item())
        except (TypeError, ValueError):
            pass
    return str(value)


def _num(value: Any, ndigits: int | None = None) -> float | None:
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(f):
        return None
    return round(f, ndigits) if ndigits is not None else f


def _pct_from_prob(value: Any) -> float | None:
    f = _num(value)
    return round(f * 100, 1) if f is not None else None


def _scalar_items(d: dict | None) -> dict[str, Any] | None:
    """Solo claves escalares (evita volcar listas de velas / estructuras grandes)."""
    if not isinstance(d, dict):
        return None
    return {str(k): to_jsonable(v) for k, v in d.items() if isinstance(v, _SCALARS) or hasattr(v, "item")}


def _iso_utc(generated: Any) -> str | None:
    if not generated:
        return None
    try:
        dt = datetime.strptime(str(generated), "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
    except ValueError:
        return str(generated)
    return dt.strftime("%Y-%m-%dT%H:%M:00Z")


def json_path_for(md_path: Path) -> Path:
    return Path(md_path).with_suffix(".json")


def latest_signal_id(data: dict) -> str | None:
    """Id de la última Entry del historial del asset (btc-NNN), si existe."""
    from app.models.signal_history import history_path_for_asset, load_signal_history

    base = Path(data["signal_history_dir"]) if data.get("signal_history_dir") else None
    hist = load_signal_history(history_path_for_asset(data.get("asset_label", "BTC"), base))
    return str(hist[-1]["id"]) if hist and hist[-1].get("id") else None


def _items(rows: list | None) -> list[dict[str, Any]]:
    out = []
    for row in rows or []:
        if isinstance(row, (list, tuple)) and len(row) >= 2:
            out.append({
                "label": to_jsonable(row[0]),
                "ok": bool(row[1]),
                "note": to_jsonable(row[2]) if len(row) > 2 else None,
            })
    return out


def _plan(opt: dict | None) -> dict[str, Any]:
    opt = opt or {}
    rr = _num(opt.get("rr"))
    return {
        "entry": _num(opt.get("user_entry") if opt.get("user_entry") is not None else opt.get("entry")),
        "optimalEntry": _num(opt.get("entry")),
        "sl": _num(opt.get("sl")),
        "tp": _num(opt.get("tp")),
        "rr": rr,
        "risk": _num(opt.get("risk_pts")),
        "trigger": to_jsonable(opt.get("trigger")),
        "invalidation": to_jsonable(opt.get("invalidacion")),
        "confirmation": to_jsonable(opt.get("confirmacion")),
        "planB": to_jsonable(opt.get("plan_b")),
        "slTpSource": to_jsonable(opt.get("sl_tp_source")),
    }


def _probability(cats: dict, est: dict | None) -> dict[str, Any]:
    if cats.get("prob_pct") is not None:
        ci = cats.get("prob_ci") or (None, None)
        return {
            "pct": _num(cats.get("prob_pct"), 1),
            "ci": [_num(ci[0], 1), _num(ci[1], 1)],
            "evR": _num(cats.get("ev_r"), 3),
            "kellyFrac": _num(cats.get("kelly_frac"), 4),
            "calibrated": True,
            "hasEdge": bool(cats.get("prob_has_edge")),
            "method": "walk_forward_logistic" if cats.get("prob_has_edge") else "base_rate",
            "n": to_jsonable(cats.get("prob_n")),
            "nEff": to_jsonable(cats.get("prob_n_eff")),
            "legacyPct": _num(cats.get("prob_legacy_pct"), 1),
            "layersUsed": to_jsonable((est or {}).get("layers_used") or []),
        }
    if est:
        return {
            "pct": _pct_from_prob(est.get("p")),
            "ci": [_pct_from_prob(est.get("lo")), _pct_from_prob(est.get("hi"))],
            "evR": _num(est.get("ev_r"), 3),
            "kellyFrac": _num(est.get("kelly"), 4),
            "calibrated": True,
            "hasEdge": bool(est.get("has_edge")),
            "method": "walk_forward_logistic" if est.get("has_edge") else "base_rate",
            "n": to_jsonable(est.get("n")),
            "nEff": to_jsonable(est.get("n_eff")),
            "legacyPct": None,
            "layersUsed": to_jsonable(est.get("layers_used") or []),
        }
    pct = _num(cats.get("fusion_score"), 1)
    return {
        "pct": pct,
        "ci": None,
        "evR": None,
        "kellyFrac": None,
        "calibrated": False,
        "hasEdge": None,
        "method": "heuristic_fusion" if pct is not None else None,
        "n": None,
        "nEff": None,
        "legacyPct": None,
        "layersUsed": [],
    }


def _crt_ok(data: dict, crt: dict | None) -> bool | None:
    try:
        from app.models.btc_signal_categories import _crt_coherent

        return bool(_crt_coherent(data, crt)[0])
    except (KeyError, TypeError, ValueError):
        return None


def _fusion(data: dict, ctx: dict, cats: dict, crt: dict | None, e2: dict | None) -> dict[str, Any]:
    crt_ok = _crt_ok(data, crt)
    crt_score = None
    if crt_ok is not None:
        crt_score = 100.0 if crt_ok else 0.0
    e2 = e2 or {}
    e2_max = _num(e2.get("max"))
    e2_score = _num(e2.get("score"))
    e2_pct = None
    if e2_max and e2_score is not None:
        e2_pct = round(e2_score / e2_max * 100, 1)
    neural_eff = cats.get("neural_effective_prob_win")
    if neural_eff is None:
        neural_eff = cats.get("neural_prob_win")
    return {
        "score": _num(cats.get("fusion_score"), 1),
        "preAcuerdo": _num(cats.get("fusion_pre_acuerdo"), 1),
        "weights": to_jsonable(cats.get("fusion_weights") or None),
        "layers": {
            "rules": _num(cats.get("rules_pct"), 1),
            "extended": _num(ctx.get("ext_pct"), 1),
            "crt": crt_score,
            "neural": _pct_from_prob(neural_eff),
            "ml": _pct_from_prob(cats.get("ml_prob_win")),
            "e2": e2_pct,
        },
    }


def _layer(cats: dict, prefix: str) -> dict[str, Any] | None:
    prob = cats.get(f"{prefix}_prob_win")
    if prob is None:
        return None
    out = {
        "pct": _pct_from_prob(prob),
        "grade": to_jsonable(cats.get(f"{prefix}_grade")),
        "conf": to_jsonable(cats.get(f"{prefix}_confidence")),
    }
    if prefix == "neural":
        out["effectivePct"] = _pct_from_prob(cats.get("neural_effective_prob_win"))
        out["gate"] = _num(cats.get("neural_gate_factor"), 3)
    return out


def _zentinel(data: dict) -> dict[str, Any] | None:
    vol = data.get("zentinel_volume")
    meta = data.get("zentinel")
    ses = data.get("session") or {}
    if not vol and not meta:
        return None
    return {
        "volume": _scalar_items(vol),
        "presets": _scalar_items(meta),
        "killzone": to_jsonable(ses.get("window")),
        "killzoneOn": bool(ses.get("killzone_on") or ses.get("in_ny_window")),
        "nyLocal": to_jsonable(ses.get("ny_local")),
    }


def _ict(opt: dict | None, cats: dict) -> dict[str, Any] | None:
    opt = opt or {}
    scan = opt.get("ict_scan")
    if not scan and not opt.get("ict_note") and not cats.get("ict_scan"):
        return None
    return {
        "refined": to_jsonable(opt.get("ict_refined")),
        "source": to_jsonable(opt.get("ict_source")),
        "note": to_jsonable(opt.get("ict_note")),
        "entryBeforeIct": _num(opt.get("entry_before_ict")),
        "summary": to_jsonable(cats.get("ict_scan")),
        "scan": _scalar_items(scan) if isinstance(scan, dict) else None,
    }


def _contingencies(cats: dict) -> list[str]:
    guidance = cats.get("contingency") or {}
    out = []
    if guidance.get("headline"):
        out.append(str(guidance["headline"]))
    out.extend(str(o) for o in guidance.get("options") or [])
    return out


def _freshness(data: dict) -> dict[str, Any]:
    fresh = data.get("data_freshness") or {}
    stale = fresh.get("stale")
    if stale is None and data.get("data_stale") is not None:
        stale = bool(data.get("data_stale"))
    return {
        "stale": None if stale is None else bool(stale),
        "message": to_jsonable(fresh.get("message")),
        "lastCandleUtc": to_jsonable(fresh.get("last_candle_utc")),
        "ageMin": to_jsonable(fresh.get("age_min")),
        "source": to_jsonable(data.get("data_source")),
    }


def _chart(data: dict) -> dict[str, Any]:
    ann = data.get("annotated_chart_abs") if data.get("ilustrate") else None
    render = None
    if ann:
        candidate = Path(str(ann)).with_suffix(".render.json")
        render = str(candidate) if candidate.is_file() else None
    pub = data.get("chart_archive") or {}
    return {
        "main": to_jsonable(data.get("chart_file")) if data.get("chart") else None,
        "annotated": to_jsonable(ann),
        "renderJson": render,
        "archive": _scalar_items(pub) if pub.get("ok") else None,
    }


def build_high_signal_json(
    data: dict,
    ctx: dict,
    opt: dict | None,
    *,
    signal_id: str | None = None,
    advanced: bool = False,
) -> dict[str, Any]:
    """Payload schemaVersion 1 a partir de data/ctx/categories ya calculados por write_high_signal."""
    from app.services.btc_high_analysis import _mode_bias_label, _mode_setup_label

    cats = ctx.get("categories") or {}
    crt = data.get("crt")
    e2 = data.get("e2")
    setup = data.get("setup") or {}
    history_mode = bool(data.get("history_mode"))
    est = ctx.get("prob_estimate")
    payload = {
        "schemaVersion": SCHEMA_VERSION,
        "asset": str(data.get("asset_label") or data.get("symbol") or "BTC").upper(),
        "symbol": to_jsonable(data.get("symbol")),
        "mode": "history_review" if history_mode else "high",
        "advanced": bool(advanced),
        "generatedUtc": _iso_utc(data.get("generated")),
        "signalId": None if history_mode else signal_id,
        "reviewedSignalId": signal_id if history_mode else None,
        "verdict": to_jsonable(ctx.get("verdict")),
        "direction": to_jsonable(setup.get("direction")),
        "price": _num(data.get("price")),
        "bias": _mode_bias_label(str(data.get("mode_bias") or "auto")),
        "biasH1": to_jsonable(data.get("bias_h1")),
        "setup": _mode_setup_label(str(data.get("mode_setup") or "auto")),
        "setupGrade": to_jsonable(cats.get("setup_grade")),
        "winrate": {"value": to_jsonable(cats.get("winrate")), "source": to_jsonable(cats.get("winrate_source"))},
        "plan": _plan(opt),
        "probability": _probability(cats, est),
        "fusion": _fusion(data, ctx, cats, crt, e2),
        "confluence": {
            "pct": _num(cats.get("confluencia_pct"), 1),
            "label": to_jsonable(cats.get("confluencia_setup")),
            "detail": to_jsonable(cats.get("confluencia_detalle")),
        },
        "rules": {
            "e1": {
                "ok": to_jsonable(cats.get("rules_ok")),
                "total": to_jsonable(cats.get("rules_total")),
                "pct": _num(cats.get("rules_pct"), 1),
            },
            "extended": {"pct": _num(ctx.get("ext_pct"), 1)},
        },
        "ml": _layer(cats, "ml"),
        "neural": _layer(cats, "neural"),
        "zentinel": _zentinel(data),
        "macdQuant": to_jsonable(data.get("macd_quant")) if data.get("macd_quant") else None,
        "ict": _ict(opt, cats),
        "crt": _scalar_items(crt),
        "e2": _scalar_items(e2),
        "contingencies": _contingencies(cats),
        "redFlags": [str(f) for f in ctx.get("flags") or []],
        "checklists": {
            "e1": _items(ctx.get("rules_items")),
            "extended": _items(ctx.get("ext_items")),
            "rulesReview": to_jsonable(ctx.get("rules_review") or []),
        },
        "dataFreshness": _freshness(data),
        "chart": _chart(data),
    }
    return to_jsonable(payload)


def write_json_atomic(path: Path, payload: dict) -> Path:
    """Escribe JSON vía archivo temporal en el mismo directorio + os.replace."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=1, allow_nan=False) + "\n"
    fd, tmp = tempfile.mkstemp(prefix=f".{path.stem}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    return path
