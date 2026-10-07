"""Probabilidad de éxito calibrada (E1) — logística walk-forward sobre replay del motor.

Dataset: se reproduce el motor E1 vela a vela sobre el histórico M5 y se etiqueta
cada señal con TP 1:2 antes que SL (horizonte 48 velas). Con eso se estiman:

  logit p = b0 + Σ w_i · x_i        (x_i graduadas, ver FEATURES)

validado walk-forward con purga de `horizon` velas. Si el modelo no mejora el
Brier de la tasa base fuera de muestra, se muestra la tasa base (sin inventar ventaja).
ML / Neural solo entran si el artefacto marca `layers.<capa>.oos_ok`.

Artefacto: models/<asset>_prob_calibration.json (generado por
`python -m app.controllers.calibrate_signals --asset btc`).
"""
from __future__ import annotations

import json
import math
import os
from datetime import timedelta
from pathlib import Path
from typing import Any

from app.config import MODELS_DIR

FEATURES = ("rsi_ext", "pd_favor", "confirm_2m5", "crt_coherent")
FEATURE_LABELS = {
    "rsi_ext": "RSI M5 vs dirección",
    "pd_favor": "Zona premium/discount",
    "confirm_2m5": "2 velas M5 confirman",
    "crt_coherent": "Rango CRT coherente",
}
RSI_EXT_CLIP = 4.0
# Bins de extensión RSI en el sentido del trade (0 = RSI 50; +3 = RSI 80 en LONG / 20 en SHORT)
RSI_EXT_BINS = (-99.0, -1.0, 0.0, 1.0, 2.0, 3.0, 99.0)
MIN_N_EFF = 30
KELLY_FRACTION = 0.25
KELLY_CAP = 0.01
DEFAULT_COST_PCT = {"BTC": 0.015, "US30": 0.006, "XAUUSD": 0.008}
_DISABLE_ENV = "TRADING_PROB_CALIBRATION"
_DIR_ENV = "TRADING_PROB_CALIBRATION_DIR"

_CACHE: dict[str, tuple[float, dict]] = {}


# ---------------------------------------------------------------------------
# Features
# ---------------------------------------------------------------------------

def _sigmoid(z: float) -> float:
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    e = math.exp(z)
    return e / (1.0 + e)


def _logit(p: float) -> float:
    p = min(max(p, 1e-4), 1 - 1e-4)
    return math.log(p / (1 - p))


def rsi_extension(rsi: float | None, direction: str) -> float:
    """RSI en unidades de 10 pts a favor de la dirección (positivo = extendido)."""
    if rsi is None or direction not in ("LONG", "SHORT"):
        return 0.0
    ext = (rsi - 50.0) / 10.0 if direction == "LONG" else (50.0 - rsi) / 10.0
    return max(-RSI_EXT_CLIP, min(RSI_EXT_CLIP, ext))


def pd_favor_value(pd: str | None, direction: str) -> int:
    favor = {"LONG": "DISCOUNT", "SHORT": "PREMIUM"}.get(direction)
    against = {"LONG": "PREMIUM", "SHORT": "DISCOUNT"}.get(direction)
    pd_u = str(pd or "").upper()
    if favor and pd_u == favor:
        return 1
    if against and pd_u == against:
        return -1
    return 0


def extract_features(data: dict, crt: dict | None) -> dict[str, float] | None:
    from app.models.btc_signal_categories import _confirm_for_direction, _crt_coherent

    direction = (data.get("setup") or {}).get("direction")
    if direction not in ("LONG", "SHORT"):
        return None
    crt_ok, _ = _crt_coherent(data, crt)
    return {
        "rsi_ext": rsi_extension(data.get("rsi_m5"), direction),
        "pd_favor": float(pd_favor_value((crt or {}).get("premium_discount"), direction)),
        "confirm_2m5": 1.0 if _confirm_for_direction(data, direction) else 0.0,
        "crt_coherent": 1.0 if crt_ok else 0.0,
    }


def rsi_ext_bin(ext: float) -> str:
    for lo, hi in zip(RSI_EXT_BINS[:-1], RSI_EXT_BINS[1:]):
        if lo <= ext < hi:
            return f"{lo:g}..{hi:g}"
    return f"{RSI_EXT_BINS[-2]:g}..{RSI_EXT_BINS[-1]:g}"


# ---------------------------------------------------------------------------
# Artefacto
# ---------------------------------------------------------------------------

def asset_key(asset: str | None) -> str:
    a = str(asset or "BTC").upper()
    if a.startswith("BTC"):
        return "BTC"
    if "US30" in a or "DJ" in a:
        return "US30"
    if "XAU" in a or "GOLD" in a:
        return "XAUUSD"
    return a


def calibration_path(asset: str | None) -> Path:
    base = Path(os.environ[_DIR_ENV]) if os.environ.get(_DIR_ENV) else MODELS_DIR
    return base / f"{asset_key(asset).lower()}_prob_calibration.json"


def load_calibration(asset: str | None = "BTC") -> dict | None:
    if os.environ.get(_DISABLE_ENV, "").lower() in ("off", "0", "false"):
        return None
    path = calibration_path(asset)
    if not path.is_file():
        return None
    mtime = path.stat().st_mtime
    key = str(path)
    cached = _CACHE.get(key)
    if cached and cached[0] == mtime:
        return cached[1]
    try:
        calib = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    _CACHE[key] = (mtime, calib)
    return calib


def _linear(coef: dict[str, float], intercept: float, feats: dict[str, float]) -> float:
    return intercept + sum(coef.get(k, 0.0) * feats.get(k, 0.0) for k in FEATURES)


def _layer_logit_shift(calib: dict, categories: dict | None, base: float) -> tuple[float, list[str]]:
    """ML / Neural solo suman si el artefacto los validó fuera de muestra."""
    shift = 0.0
    used: list[str] = []
    cats = categories or {}
    layers = calib.get("layers") or {}
    for name, key in (("ml", "ml_prob_win"), ("neural", "neural_effective_prob_win")):
        cfg = layers.get(name) or {}
        prob = cats.get(key)
        if prob is None and name == "neural":
            prob = cats.get("neural_prob_win")
        if not cfg.get("oos_ok") or prob is None:
            continue
        shift += float(cfg.get("weight", 0.0)) * (_logit(float(prob)) - _logit(base))
        used.append(name)
    return shift, used


def predict_proba(calib: dict, feats: dict[str, float]) -> float:
    return _sigmoid(_linear(calib["coef"], calib["intercept"], feats))


def _model_point(calib: dict, feats: dict[str, float], shift: float) -> tuple[float, list[float], dict[str, float]]:
    """p del modelo, simulaciones bootstrap ordenadas y contribución por feature (pts vs su media)."""
    p = _sigmoid(_linear(calib["coef"], calib["intercept"], feats) + shift)
    sims = sorted(
        _sigmoid(_linear(b["coef"], b["intercept"], feats) + shift) for b in calib.get("bootstrap") or []
    )
    means = calib.get("feature_means") or {}
    contrib = {}
    for k in FEATURES:
        alt = {**feats, k: float(means.get(k, 0.0))}
        contrib[k] = (p - _sigmoid(_linear(calib["coef"], calib["intercept"], alt) + shift)) * 100
    return p, sims, contrib


def _band80(sims: list[float], p: float) -> tuple[float, float]:
    if not sims:
        return p, p
    return sims[int(0.10 * (len(sims) - 1))], sims[int(0.90 * (len(sims) - 1))]


def _trade_economics(
    data: dict, calib: dict, asset: str, p: float
) -> tuple[float, float | None, float, float, float]:
    """R:R, riesgo % del precio, coste en R, EV en R y Kelly fraccional acotado."""
    setup = data.get("setup") or {}
    rr = float(setup.get("rr") or calib.get("rr", 2.0))
    price = float(data.get("price") or 0.0)
    sl = setup.get("sl")
    risk_pct = abs(price - float(sl)) / price * 100 if sl and price else None
    cost_pct = float(calib.get("cost_pct", DEFAULT_COST_PCT.get(asset_key(asset), 0.01)))
    cost_r = cost_pct / risk_pct if risk_pct else 0.0
    ev_r = p * rr - (1 - p) - cost_r
    kelly = max(0.0, min(KELLY_CAP, KELLY_FRACTION * ev_r / rr)) if rr > 0 else 0.0
    return rr, risk_pct, cost_r, ev_r, kelly


def calibrated_estimate(
    data: dict,
    crt: dict | None,
    *,
    categories: dict | None = None,
    asset: str | None = None,
) -> dict[str, Any] | None:
    """Probabilidad calibrada + intervalo 80% + EV en R + Kelly fraccional."""
    asset = asset or data.get("asset_label") or data.get("symbol") or "BTC"
    calib = load_calibration(asset)
    if not calib:
        return None
    feats = extract_features(data, crt)
    if feats is None:
        return None

    base = float(calib["base_rate"])
    has_edge = bool(calib.get("has_edge"))
    shift, layers_used = _layer_logit_shift(calib, categories, base)
    if has_edge:
        p, sims, contrib = _model_point(calib, feats, shift)
    else:
        p = base
        sims = sorted(float(b["base_rate"]) for b in calib.get("bootstrap") or [] if "base_rate" in b)
        contrib = dict.fromkeys(FEATURES, 0.0)
    lo, hi = _band80(sims, p)
    rr, risk_pct, cost_r, ev_r, kelly = _trade_economics(data, calib, asset, p)

    n_eff = int(calib.get("n_eff", 0))
    return {
        "p": p,
        "lo": lo,
        "hi": hi,
        "base": base,
        "has_edge": has_edge,
        "n": int(calib.get("n", 0)),
        "n_eff": n_eff,
        "low_confidence": n_eff < MIN_N_EFF,
        "features": feats,
        "contrib": contrib,
        "rr": rr,
        "risk_pct": risk_pct,
        "cost_r": cost_r,
        "ev_r": ev_r,
        "kelly": kelly,
        "layers_used": layers_used,
        "asset": asset_key(asset),
        "calib": calib,
    }


def format_estimate_source(est: dict) -> str:
    conf = " · baja confianza" if est["low_confidence"] else ""
    kind = "calibrado walk-forward" if est["has_edge"] else "tasa base (modelo sin ventaja OOS)"
    return (
        f"{kind} {est['asset']} E1 · 80%: {est['lo'] * 100:.0f}–{est['hi'] * 100:.0f}% · "
        f"n={est['n']} (n_eff {est['n_eff']}){conf} · EV {est['ev_r']:+.2f}R"
    )


def store_estimate(categories: dict, est: dict, legacy_pct: float | None = None) -> None:
    """Claves nuevas en categories (las existentes no cambian de significado)."""
    categories["prob_calibrated"] = True
    categories["prob_pct"] = round(est["p"] * 100, 1)
    categories["prob_ci"] = (round(est["lo"] * 100, 1), round(est["hi"] * 100, 1))
    categories["prob_n"] = est["n"]
    categories["prob_n_eff"] = est["n_eff"]
    categories["prob_has_edge"] = est["has_edge"]
    categories["ev_r"] = round(est["ev_r"], 3)
    categories["kelly_frac"] = round(est["kelly"], 4)
    if legacy_pct is not None:
        categories["prob_legacy_pct"] = round(legacy_pct, 1)


def prob_log_path(asset: str | None) -> Path:
    from app.config import LIVE_DIR

    return LIVE_DIR / f"{asset_key(asset).lower()}_prob_log.jsonl"


def log_prediction(data: dict, est: dict, path: Path | None = None) -> None:
    """Append-only: predicción mostrada para evaluar calibración en vivo."""
    setup = data.get("setup") or {}
    row = {
        "generated_utc": data.get("generated"),
        "asset": est["asset"],
        "direction": setup.get("direction"),
        "price": data.get("price"),
        "sl": setup.get("sl"),
        "tp": setup.get("tp"),
        "rr": est["rr"],
        "p": round(est["p"], 4),
        "lo": round(est["lo"], 4),
        "hi": round(est["hi"], 4),
        "ev_r": round(est["ev_r"], 4),
        "has_edge": est["has_edge"],
        "features": est["features"],
    }
    path = path or prob_log_path(est["asset"])
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Reglas revisadas graduadas
# ---------------------------------------------------------------------------

GRADE_MARKS = (
    (4.0, "✓✓"),
    (1.0, "✓"),
    (-1.0, "~"),
    (-4.0, "✗"),
)


def grade_from_impact(pp: float) -> str:
    for threshold, mark in GRADE_MARKS:
        if pp >= threshold:
            return mark
    return "✗✗"


RSI_HEURISTIC_GRADES = ((-1.0, "✓✓"), (1.0, "✓"), (2.0, "~"), (3.0, "✗"))


def _grade_rsi_heuristic(x: float) -> str:
    if x <= RSI_HEURISTIC_GRADES[0][0]:
        return RSI_HEURISTIC_GRADES[0][1]
    for upper, mark in RSI_HEURISTIC_GRADES[1:]:
        if x < upper:
            return mark
    return "✗✗"


def _grade_heuristic(name: str, feats: dict[str, float]) -> str:
    x = feats[name]
    if name == "rsi_ext":
        return _grade_rsi_heuristic(x)
    if x > 0:
        return "✓"
    if name == "pd_favor" and x >= 0:
        return "~"
    return "✗"


def _rsi_value_text(rsi: float | None, direction: str, ext: float) -> str:
    if rsi is None:
        return "n/d"
    if ext >= 3:
        state = "muy extendido"
    elif ext >= 2:
        state = "extendido"
    elif ext >= 1:
        state = "con impulso"
    elif ext > -1:
        state = "neutral"
    else:
        state = "con recorrido a favor"
    return f"RSI {rsi:.1f} ({direction}: {state})"


def _pct(v: float | None) -> str:
    return "n/d" if v is None else f"{v * 100:.0f}%"


def build_rules_review_rows(
    data: dict,
    crt: dict | None,
    est: dict | None,
    rules_items: list[tuple[str, bool, str]] | None = None,
) -> list[dict[str, str]]:
    """Tabla única: Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo."""
    feats = (est or {}).get("features") or extract_features(data, crt)
    if feats is None:
        return []
    direction = data["setup"]["direction"]
    stats = ((est or {}).get("calib") or {}).get("rule_stats") or {}
    contrib = est["contrib"] if est and est.get("has_edge") else None
    crt = crt or {}

    def row(name: str, value: str, wr: str) -> dict[str, str]:
        grade, impact = _impact_cell(name, feats, contrib)
        return {"label": FEATURE_LABELS[name], "grade": grade, "value": value,
                "impact": impact, "wr": wr, "type": "ponderada"}

    zst = (stats.get("rsi_ext_bins") or {}).get(rsi_ext_bin(feats["rsi_ext"]))
    side = {1.0: "a favor", -1.0: "en contra"}.get(feats["pd_favor"], "neutral")
    rows = [
        row("rsi_ext", _rsi_value_text(data.get("rsi_m5"), direction, feats["rsi_ext"]),
            f"esta zona {_pct(zst['wr'])} (n={zst['n']})" if zst else "n/d"),
        row("pd_favor", f"{crt.get('premium_discount') or 'n/d'} ({side})", _pd_winrate(stats.get("pd_favor"))),
        row("confirm_2m5", "sí" if feats["confirm_2m5"] else "no", _pass_fail_winrate(stats.get("confirm_2m5"))),
        _crt_row(row, data, crt, direction, stats.get("crt_coherent")),
    ]
    rows.extend(_precondition_rows(rules_items))
    return rows


def _impact_cell(name: str, feats: dict[str, float], contrib: dict[str, float] | None) -> tuple[str, str]:
    if contrib is not None:
        pp = contrib[name]
        return grade_from_impact(pp), f"{pp:+.1f} pts"
    return _grade_heuristic(name, feats), "sin calibrar"


def _pd_winrate(pst: dict | None) -> str:
    pst = pst or {}
    if "1" not in pst or "-1" not in pst:
        return "n/d"
    return f"a favor {_pct(pst['1']['wr'])} / en contra {_pct(pst['-1']['wr'])}"


def _pass_fail_winrate(st: dict | None) -> str:
    st = st or {}
    if st.get("pass_wr") is None:
        return "n/d"
    return f"sí {_pct(st['pass_wr'])} / no {_pct(st['fail_wr'])}"


def _crt_row(row, data: dict, crt: dict, direction: str, rst: dict | None) -> dict[str, str]:
    """CRT ponderado; veto duro si hay fakeout en contra de la dirección."""
    from app.models.btc_signal_categories import _crt_coherent

    _, crt_note = _crt_coherent(data, crt)
    out = row("crt_coherent", crt_note, _pass_fail_winrate(rst))
    fakeout_key = "fakeout_pdh" if direction == "LONG" else "fakeout_pdl"
    if direction in ("LONG", "SHORT") and crt.get(fakeout_key):
        out.update(grade="✗✗", type="veto")
    return out


PRECONDITION_RULES = frozenset({"Solo E1", "Tendencia H1 alineada", "R:R mínimo 1:2"})


def _precondition_rows(rules_items: list[tuple[str, bool, str]] | None) -> list[dict[str, str]]:
    """Precondiciones constantes por construcción del setup → info (o veto si fallan)."""
    return [
        {
            "label": label, "grade": "·" if passed else "✗✗",
            "value": note or ("sí" if passed else "no"),
            "impact": "—", "wr": "constante en histórico",
            "type": "info" if passed else "veto",
        }
        for label, passed, note in rules_items or []
        if label in PRECONDITION_RULES
    ]


def format_rules_review_md(rows: list[dict[str, str]], est: dict | None) -> list[str]:
    if not rows:
        return []
    if est and est.get("has_edge"):
        src = f"impacto medido walk-forward n={est['n']} (n_eff {est['n_eff']})"
    elif est:
        src = "modelo sin ventaja OOS — impacto no significativo"
    else:
        src = "sin calibración — estado por zonas fijas"
    lines = [
        "### Reglas revisadas (graduadas)",
        "",
        f"_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: {src}._",
        "",
        "| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |",
        "|-------|--------|--------------|---------|-------------------|------|",
    ]
    for r in rows:
        lines.append(
            f"| {r['label']} | {r['grade']} | {r['value']} | {r['impact']} | {r['wr']} | {r['type']} |"
        )
    lines.append("")
    return lines


# ---------------------------------------------------------------------------
# Entrenamiento (replay + walk-forward)
# ---------------------------------------------------------------------------

def build_replay_dataset(
    m5: list[dict],
    h1: list[dict],
    *,
    horizon: int = 48,
    stride: int = 3,
    cooldown: int = 12,
    window: int = 600,
    h1_window: int = 300,
) -> list[dict]:
    """Reproduce el motor E1 sobre el histórico y etiqueta TP 1:2 antes que SL."""
    import bisect

    from app.controllers.train_btc_signals import build_snapshot_at_index, label_outcome
    from app.models.btc_signal_categories import _heuristic_winrate_estimate, score_e1_rules_8
    from app.services.btc_high_analysis import analyze_crt

    h1_times = [c["open_time"] for c in h1]
    last_sig = {"LONG": -10**9, "SHORT": -10**9}
    rows: list[dict] = []
    for idx in range(window + 100, len(m5) - horizon - 1, stride):
        sub = m5[idx - window: idx + 1]
        ts = sub[-1]["open_time"]
        j = bisect.bisect_right(h1_times, ts)
        hsub = h1[max(0, j - h1_window): j]
        data = build_snapshot_at_index(sub, hsub, len(sub) - 1)
        if data is None:
            continue
        direction = data["setup"]["direction"]
        if direction not in ("LONG", "SHORT") or idx - last_sig[direction] < cooldown:
            continue
        last_sig[direction] = idx
        crt = analyze_crt(data["price"], data.get("pdh"), data.get("pdl"), hsub, sub)
        label = label_outcome(
            direction, data["price"], data["setup"].get("sl"),
            m5[idx + 1: idx + 1 + horizon], horizon,
        )
        feats = extract_features(data, crt)
        _, _, rules_pct, _ = score_e1_rules_8(data, crt, None, None, None)
        legacy, _ = _heuristic_winrate_estimate(rules_pct, None, data=data, crt=crt)
        sl = data["setup"].get("sl")
        rows.append({
            "time": ts,
            "bar": idx,
            "direction": direction,
            "label": label,
            "legacy_pct": float(legacy.strip("~%")) if legacy != "N/A" else None,
            "risk_pct": abs(data["price"] - sl) / data["price"] * 100 if sl else None,
            **feats,
        })
    return rows


def _brier(y: list[int], p: list[float]) -> float:
    return sum((pi - yi) ** 2 for yi, pi in zip(y, p)) / len(y)


def _logloss(y: list[int], p: list[float]) -> float:
    eps = 1e-6
    return -sum(
        yi * math.log(max(pi, eps)) + (1 - yi) * math.log(max(1 - pi, eps))
        for yi, pi in zip(y, p)
    ) / len(y)


def _ece(y: list[int], p: list[float], bins: int = 10) -> float:
    total = len(y)
    err = 0.0
    for b in range(bins):
        lo, hi = b / bins, (b + 1) / bins
        idx = [i for i, pi in enumerate(p) if lo <= pi < hi or (b == bins - 1 and pi >= hi)]
        if idx:
            err += len(idx) / total * abs(
                sum(p[i] for i in idx) / len(idx) - sum(y[i] for i in idx) / len(idx)
            )
    return err


def _metrics(y: list[int], p: list[float]) -> dict[str, float]:
    return {
        "brier": round(_brier(y, p), 5),
        "logloss": round(_logloss(y, p), 5),
        "ece": round(_ece(y, p), 5),
    }


def _fit_logistic(X, y, c: float):
    from sklearn.linear_model import LogisticRegression

    clf = LogisticRegression(C=c, max_iter=1000)
    clf.fit(X, y)
    return clf


def _effective_n(bars: list[int], horizon: int) -> int:
    """Señales separadas ≥ horizon velas (sin solape de ventanas de resultado)."""
    n, last = 0, -10**9
    for b in sorted(bars):
        if b - last >= horizon:
            n += 1
            last = b
    return n


def _rule_stats(rows: list[dict]) -> dict[str, Any]:
    def wr(sub: list[dict]) -> dict[str, Any]:
        return {"n": len(sub), "wr": round(sum(r["label"] for r in sub) / len(sub), 4) if sub else None}

    out: dict[str, Any] = {}
    for name in ("confirm_2m5", "crt_coherent"):
        yes = [r for r in rows if r[name] > 0]
        no = [r for r in rows if r[name] <= 0]
        out[name] = {
            "pass_rate": round(len(yes) / len(rows), 4),
            "pass_wr": wr(yes)["wr"], "pass_n": len(yes),
            "fail_wr": wr(no)["wr"], "fail_n": len(no),
        }
    out["pd_favor"] = {
        str(v): wr([r for r in rows if int(r["pd_favor"]) == v]) for v in (-1, 0, 1)
    }
    bins: dict[str, Any] = {}
    for r in rows:
        bins.setdefault(rsi_ext_bin(r["rsi_ext"]), []).append(r)
    out["rsi_ext_bins"] = {
        k: wr(v) for k, v in sorted(bins.items(), key=lambda kv: float(kv[0].split("..")[0]))
    }
    return out


def _calibration_table(y: list[int], p: list[float], edges: list[float]) -> list[dict]:
    out = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        idx = [i for i, pi in enumerate(p) if lo <= pi < hi]
        if idx:
            out.append({
                "bucket": f"{lo * 100:.0f}-{hi * 100:.0f}%",
                "n": len(idx),
                "pred": round(sum(p[i] for i in idx) / len(idx), 4),
                "real": round(sum(y[i] for i in idx) / len(idx), 4),
            })
    return out


def _walk_forward(data: list[dict], X, y, *, horizon: int, folds: int, c: float) -> dict[str, list]:
    """Predicciones fuera de muestra por bloques cronológicos con purga de `horizon` velas M5."""
    import numpy as np

    times = [r["time"] for r in data]
    purge = timedelta(minutes=5 * horizon)
    oos: dict[str, list] = {"y": [], "model": [], "const": [], "legacy_y": [], "legacy": []}
    bounds = np.linspace(0, len(data), folds + 1, dtype=int)
    for k in range(1, folds):
        a, b = bounds[k], bounds[k + 1]
        cutoff = times[a] - purge
        train = [i for i in range(a) if times[i] < cutoff]
        if len(train) < 50 or len(set(y[train])) < 2:
            continue
        clf = _fit_logistic(X[train], y[train], c)
        oos["y"] += y[a:b].tolist()
        oos["model"] += clf.predict_proba(X[a:b])[:, 1].tolist()
        oos["const"] += [float(y[train].mean())] * (b - a)
        legacy = [i for i in range(a, b) if data[i]["legacy_pct"] is not None]
        oos["legacy_y"] += [int(y[i]) for i in legacy]
        oos["legacy"] += [data[i]["legacy_pct"] / 100 for i in legacy]
    return oos


def _day_bootstrap(X, y, times: list, full: tuple[dict, float], *, c: float, n_boot: int, seed: int) -> list[dict]:
    """Remuestreo por días completos (respeta la autocorrelación intradía)."""
    import random

    coef, intercept = full
    # Remuestreo estadístico reproducible (semilla fija), no criptográfico.
    rng = random.Random(seed)  # NOSONAR
    days: dict[Any, list[int]] = {}
    for i, t in enumerate(times):
        days.setdefault(t.date(), []).append(i)
    day_keys = list(days)
    boot = []
    for _ in range(n_boot):
        idx = [i for d in (rng.choice(day_keys) for _ in day_keys) for i in days[d]]  # NOSONAR
        yb = y[idx]
        entry: dict[str, Any] = {"base_rate": round(float(yb.mean()), 5), "coef": coef, "intercept": intercept}
        if len(set(yb)) == 2:
            cb = _fit_logistic(X[idx], yb, c)
            entry["coef"] = {k: round(float(w), 5) for k, w in zip(FEATURES, cb.coef_[0])}
            entry["intercept"] = round(float(cb.intercept_[0]), 5)
        boot.append(entry)
    return boot


def fit_calibration(
    rows: list[dict],
    *,
    asset: str = "BTC",
    horizon: int = 48,
    rr: float = 2.0,
    folds: int = 5,
    c: float = 0.5,
    n_boot: int = 200,
    seed: int = 7,
) -> dict[str, Any]:
    """Walk-forward con purga + bootstrap por días. Devuelve el artefacto JSON."""
    import numpy as np

    data = sorted((r for r in rows if r["label"] is not None), key=lambda r: r["time"])
    if len(data) < 100:
        raise RuntimeError(f"Muestra insuficiente para calibrar ({len(data)} señales)")
    X = np.array([[r[k] for k in FEATURES] for r in data], dtype=float)
    y = np.array([int(r["label"]) for r in data])
    times = [r["time"] for r in data]

    oos = _walk_forward(data, X, y, horizon=horizon, folds=folds, c=c)
    m_model = _metrics(oos["y"], oos["model"])
    m_const = _metrics(oos["y"], oos["const"])
    skill = 1 - m_model["brier"] / m_const["brier"] if m_const["brier"] else 0.0
    has_edge = skill > 0

    clf = _fit_logistic(X, y, c)
    coef = {k: round(float(w), 5) for k, w in zip(FEATURES, clf.coef_[0])}
    intercept = round(float(clf.intercept_[0]), 5)
    boot = _day_bootstrap(X, y, times, (coef, intercept), c=c, n_boot=n_boot, seed=seed)
    oos_y, oos_model = oos["y"], oos["model"]
    oos_legacy_y, oos_legacy = oos["legacy_y"], oos["legacy"]

    edges = [0.0, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 1.01]
    risk = sorted(r["risk_pct"] for r in data if r["risk_pct"])
    return {
        "asset": asset_key(asset),
        "version": 1,
        "horizon_bars": horizon,
        "rr": rr,
        "label": f"TP 1:{rr:g} antes que SL en {horizon} velas M5",
        "period": [times[0].isoformat(), times[-1].isoformat()],
        "n": len(data),
        "n_eff": _effective_n([r["bar"] for r in data], horizon),
        "timeouts": sum(1 for r in rows if r["label"] is None),
        "base_rate": round(float(y.mean()), 5),
        "features": list(FEATURES),
        "feature_means": {k: round(float(X[:, i].mean()), 5) for i, k in enumerate(FEATURES)},
        "coef": coef,
        "intercept": intercept,
        "regularization_C": c,
        "has_edge": has_edge,
        "oos": {
            "n": len(oos_y),
            "model": m_model,
            "constant": m_const,
            "legacy": _metrics(oos_legacy_y, oos_legacy) if oos_legacy else None,
            "brier_skill_vs_constant": round(skill, 5),
            "calibration_model": _calibration_table(oos_y, oos_model, edges),
            "calibration_legacy": _calibration_table(oos_legacy_y, oos_legacy, edges),
        },
        "rule_stats": _rule_stats(data),
        "risk_pct_median": round(risk[len(risk) // 2], 5) if risk else None,
        "cost_pct": DEFAULT_COST_PCT.get(asset_key(asset), 0.01),
        "layers": {
            "ml": {"oos_ok": False, "weight": 0.0,
                   "reason": "sin predicciones ML fuera de muestra registradas"},
            "neural": {"oos_ok": False, "weight": 0.0,
                       "reason": "galería sin histórico de predicciones con resultado"},
        },
        "bootstrap": boot,
    }
