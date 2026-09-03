"""Historial ligero de Entrada óptima (High signal) — BTC / US30.

Esquema mínimo por registro: id, time, optimal_entry [, side].
`side` (LONG|SHORT) es opcional pero preferible para P&L correcto.

El asset se implica por el nombre de archivo bajo live/.
- High signal: append + reflexión geométrica (compat).
- history_mode / --history-review: solo revisión P&L de la última Entry
  del mismo par vs precio vivo — NO es señal de entrada nueva; NO append.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from app.config import LIVE_DIR

HISTORY_CAP = 80
_SAME_ZONE_ENTRY_PCT = 0.05  # |Δ entry| / last ≤ 0.05% → MISMA ZONA
_SAME_ZONE_PRICE_PCT = 0.15  # precio dentro de 0.15% de última entry → MISMA ZONA
_NEAR_ENTRY_PCT = 0.15  # cerca de entry (última o actual)
_SOFT_NEAR_PCT = 0.40  # cerca suave (REGULAR posible)
_BE_PCT = 0.05  # |P&L %| ≤ 0.05% → CERCA_BE / NEUTRO
_GOOD_PNL_PCT = 0.15  # |P&L %| ≥ 0.15% → BUENA / MALA más claro

_ASSET_FILE = {
    "btc": "btc_signal_history.json",
    "us30": "us30_signal_history.json",
}


def normalize_asset_key(asset: str | None) -> str:
    """Map asset_label → btc | us30."""
    a = (asset or "BTC").strip().upper()
    if "US30" in a or a in ("DJ30", "DJI", "YM"):
        return "us30"
    return "btc"


def history_path_for_asset(asset: str | None, base: Path | None = None) -> Path:
    key = normalize_asset_key(asset)
    return (base or LIVE_DIR) / _ASSET_FILE[key]


def _normalize_side(raw: Any) -> str | None:
    if raw is None:
        return None
    s = str(raw).strip().upper()
    if s in ("LONG", "SHORT"):
        return s
    if s in ("BULLISH", "BUY", "L"):
        return "LONG"
    if s in ("BEARISH", "SELL", "S"):
        return "SHORT"
    return None


def resolve_side(
    last: dict[str, Any] | None = None,
    *,
    data: dict | None = None,
    opt: dict | None = None,
) -> tuple[str | None, str]:
    """Resuelve lado para P&L: history.side → CLI bias → setup/opt direction.

    Returns (side|None, source_note).
    """
    data = data or {}
    opt = opt or {}
    if last:
        side = _normalize_side(last.get("side"))
        if side:
            return side, "historial"

    mode_bias = (data.get("mode_bias") or "auto").lower()
    if mode_bias == "bullish":
        return "LONG", "CLI -Bullish"
    if mode_bias == "bearish":
        return "SHORT", "CLI -Bearish"

    for src in (opt.get("direction"), (data.get("setup") or {}).get("direction")):
        side = _normalize_side(src)
        if side:
            return side, "setup vivo"
    return None, "desconocido"


def load_signal_history(path: Path) -> list[dict[str, Any]]:
    """Load history list; empty if missing/corrupt."""
    if not path.exists():
        return []
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeError):
        return []
    if isinstance(raw, dict):
        items = raw.get("signals") or raw.get("history") or []
    elif isinstance(raw, list):
        items = raw
    else:
        return []
    out: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        entry = item.get("optimal_entry")
        sid = item.get("id")
        t = item.get("time")
        if sid is None or t is None or entry is None:
            continue
        try:
            row: dict[str, Any] = {
                "id": str(sid),
                "time": str(t),
                "optimal_entry": float(entry),
            }
            side = _normalize_side(item.get("side"))
            if side:
                row["side"] = side
            out.append(row)
        except (TypeError, ValueError):
            continue
    return out


def _next_id(asset_key: str, history: list[dict[str, Any]]) -> str:
    """Sequential id: btc-001, us30-042 — survives trim via max suffix."""
    prefix = f"{asset_key}-"
    max_n = 0
    for row in history:
        sid = str(row.get("id", ""))
        m = re.fullmatch(rf"{re.escape(asset_key)}-(\d+)", sid, flags=re.IGNORECASE)
        if m:
            max_n = max(max_n, int(m.group(1)))
    return f"{prefix}{max_n + 1:03d}"


def append_signal_history(
    path: Path,
    *,
    asset: str | None,
    time_str: str,
    optimal_entry: float,
    side: str | None = None,
    cap: int = HISTORY_CAP,
) -> dict[str, Any]:
    """Append one record (id, time, optimal_entry [, side]); trim to `cap`."""
    history = load_signal_history(path)
    asset_key = normalize_asset_key(asset)
    row: dict[str, Any] = {
        "id": _next_id(asset_key, history),
        "time": time_str,
        "optimal_entry": float(optimal_entry),
    }
    norm_side = _normalize_side(side)
    if norm_side:
        row["side"] = norm_side
    history.append(row)
    if cap > 0 and len(history) > cap:
        history = history[-cap:]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(history, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return row


def format_history_time(data: dict) -> str:
    """NY-friendly timestamp when session.ny_local exists; else generated UTC."""
    ny = (data.get("session") or {}).get("ny_local")
    if ny:
        return f"{ny} NY"
    gen = data.get("generated") or "n/d"
    return f"{gen} UTC"


def compute_entry_pnl(
    *,
    entry: float,
    price: float,
    side: str,
) -> dict[str, float]:
    """P&L de Entry previa vs precio vivo.

    LONG:  + cuando precio > entry
    SHORT: + cuando precio < entry
    """
    if side == "LONG":
        pts = float(price) - float(entry)
    else:  # SHORT
        pts = float(entry) - float(price)
    pct = (pts / float(entry) * 100.0) if entry else 0.0
    return {"pnl_pts": pts, "pnl_pct": pct}


def _pnl_standing(pnl_pct: float) -> str:
    if abs(pnl_pct) <= _BE_PCT:
        return "NEUTRO"
    return "EN_BENEFICIO" if pnl_pct > 0 else "EN_PERDIDA"


def _pnl_grade(pnl_pct: float, *, dist_to_entry_pct: float | None = None) -> str:
    """Calificación de cómo va la Entry pasada (no es señal nueva)."""
    standing = _pnl_standing(pnl_pct)
    if standing == "NEUTRO":
        return "CERCA_BE"
    if standing == "EN_BENEFICIO":
        if abs(pnl_pct) >= _GOOD_PNL_PCT:
            return "BUENA"
        if dist_to_entry_pct is not None and dist_to_entry_pct <= _NEAR_ENTRY_PCT:
            return "EN_BENEFICIO"
        return "EN_BENEFICIO"
    # EN_PERDIDA
    if abs(pnl_pct) >= _GOOD_PNL_PCT:
        return "MALA"
    return "EN_PERDIDA"


def review_last_entry_pnl(
    last: dict[str, Any] | None,
    *,
    price: float,
    dec: int = 1,
    data: dict | None = None,
    opt: dict | None = None,
) -> dict[str, Any]:
    """Revisión P&L de la última Entry del mismo par vs precio actual.

    NO propone Entrada óptima nueva ni ENTRAR. Solo califica el outcome
    de la Entry histórica (con lado inferido si falta en el JSON).
    """
    fmt = f".{dec}f"
    data = data or {}
    opt = opt or {}

    if not last or last.get("optimal_entry") is None:
        return {
            "mode": "history_review",
            "status": "SIN_HISTORIAL",
            "grade": "SIN_HISTORIAL",
            "pnl_status": "SIN_HISTORIAL",
            "grade_reason": "no hay Entry previa del mismo par",
            "last_id": None,
            "last_time": None,
            "last_entry": None,
            "side": None,
            "side_source": None,
            "pnl_pts": None,
            "pnl_pct": None,
            "cell_revision": "—",
            "cell_pnl": "**SIN HISTORIAL** — corre High primero para guardar una Entry",
            "cell_calificacion": "**SIN_HISTORIAL** — sin Entry previa que revisar",
            "cell_ultima": "—",
            "cell_vs": "**SIN_HISTORIAL** — sin Entry previa que revisar",
        }

    last_entry = float(last["optimal_entry"])
    last_id = str(last.get("id", "?"))
    last_time = str(last.get("time", "n/d"))
    side, side_src = resolve_side(last, data=data, opt=opt)

    side_label = side or "?"
    cell_revision = (
        f"**{last_id}** · {last_time} · Entry **{last_entry:{fmt}}** · {side_label}"
    )
    if side and side_src != "historial":
        cell_revision += f" (lado {side_src})"

    if not side:
        dist = abs(float(price) - last_entry)
        dist_pct = (dist / last_entry * 100.0) if last_entry else 0.0
        reason = (
            "lado desconocido — pasa -Bullish/-Bearish o guarda `side` en historial"
        )
        cell_pnl = (
            f"distancia {dist:{fmt}} pts ({dist_pct:.3f}%) · **NEUTRO** — {reason}"
        )
        cell_calif = f"**SIN_LADO** — {reason}"
        return {
            "mode": "history_review",
            "status": "SIN_LADO",
            "grade": "SIN_LADO",
            "pnl_status": "NEUTRO",
            "grade_reason": reason,
            "last_id": last_id,
            "last_time": last_time,
            "last_entry": last_entry,
            "side": None,
            "side_source": side_src,
            "pnl_pts": None,
            "pnl_pct": None,
            "dist_price_to_last_pts": dist,
            "dist_price_to_last_pct": dist_pct,
            "cell_revision": cell_revision,
            "cell_pnl": cell_pnl,
            "cell_calificacion": cell_calif,
            "cell_ultima": cell_revision,
            "cell_vs": cell_calif,
        }

    pnl = compute_entry_pnl(entry=last_entry, price=float(price), side=side)
    pnl_pts = pnl["pnl_pts"]
    pnl_pct = pnl["pnl_pct"]
    standing = _pnl_standing(pnl_pct)
    dist_pct = abs(float(price) - last_entry) / last_entry * 100.0 if last_entry else 0.0
    grade = _pnl_grade(pnl_pct, dist_to_entry_pct=dist_pct)

    # Contexto vivo solo para matizar (no propone entry nueva)
    zone = data.get("zone") or {}
    dist_zone = zone.get("dist_pct")
    near_zone = dist_zone is not None and float(dist_zone) <= _NEAR_ENTRY_PCT
    context_bits: list[str] = []
    if near_zone:
        context_bits.append("aún cerca de zona")
    if dist_pct <= _NEAR_ENTRY_PCT:
        context_bits.append("precio cerca de Entry previa")

    standing_es = {
        "EN_BENEFICIO": "EN BENEFICIO",
        "EN_PERDIDA": "EN PÉRDIDA",
        "NEUTRO": "NEUTRO",
    }[standing]
    sign = "+" if pnl_pts >= 0 else ""
    cell_pnl = (
        f"**{sign}{pnl_pts:{fmt}} pts ({sign}{pnl_pct:.3f}%)** · **{standing_es}**"
        f" · {side}"
    )
    reason_parts = [f"Entry {side} {standing_es.lower()}"]
    reason_parts.extend(context_bits[:2])
    reason = "; ".join(reason_parts)
    cell_calif = f"**{grade}** — {reason}"

    return {
        "mode": "history_review",
        "status": standing,
        "grade": grade,
        "pnl_status": standing,
        "grade_reason": reason,
        "last_id": last_id,
        "last_time": last_time,
        "last_entry": last_entry,
        "side": side,
        "side_source": side_src,
        "pnl_pts": pnl_pts,
        "pnl_pct": pnl_pct,
        "dist_price_to_last_pts": abs(float(price) - last_entry),
        "dist_price_to_last_pct": dist_pct,
        "cell_revision": cell_revision,
        "cell_pnl": cell_pnl,
        "cell_calificacion": cell_calif,
        "cell_ultima": cell_revision,
        "cell_vs": cell_calif,
    }


def _proximity_pts(dist_pct: float | None) -> int:
    if dist_pct is None:
        return 0
    if dist_pct <= _NEAR_ENTRY_PCT:
        return 2
    if dist_pct <= _SOFT_NEAR_PCT:
        return 1
    return 0


def _live_setup_flags(data: dict | None, opt: dict | None) -> dict[str, Any]:
    """Extrae flags reales del pipeline High (sin inventar visión de gráfico)."""
    data = data or {}
    opt = opt or {}
    setup = data.get("setup") or {}
    direction = setup.get("direction") or opt.get("direction") or "NONE"
    zone = data.get("zone") or {}
    dist_zone = zone.get("dist_pct")
    near_zone = dist_zone is not None and float(dist_zone) <= _NEAR_ENTRY_PCT
    confirm = (
        bool(data.get("confirm_long")) if direction == "LONG"
        else bool(data.get("confirm_short")) if direction == "SHORT"
        else False
    )
    bias_h1 = data.get("bias_h1", "NEUTRAL")
    mode_bias = (data.get("mode_bias") or "auto").lower()
    aligned_h1 = (
        (direction == "LONG" and bias_h1 == "BULLISH")
        or (direction == "SHORT" and bias_h1 == "BEARISH")
    )
    aligned_cli = (
        (direction == "LONG" and mode_bias == "bullish")
        or (direction == "SHORT" and mode_bias == "bearish")
    )
    bias_conflict = (
        (direction == "LONG" and bias_h1 == "BEARISH" and mode_bias != "bullish")
        or (direction == "SHORT" and bias_h1 == "BULLISH" and mode_bias != "bearish")
    )
    ahora = str(opt.get("ahora_action") or "")
    entrar_ahora = "ENTRAR" in ahora.upper()
    setup_mode = (data.get("mode_setup") or "auto").lower()
    e2 = data.get("e2") or {}
    if setup_mode == "reverse":
        setup_ok = bool(e2.get("eligible"))
        setup_note = "E2 operable" if setup_ok else "E2 no operable"
    elif setup_mode == "break":
        setup_ok = direction in ("LONG", "SHORT")
        setup_note = "Break" if setup_ok else "Break sin dirección"
    else:
        setup_ok = direction in ("LONG", "SHORT")
        setup_note = "Setup con dirección" if setup_ok else "Sin dirección"

    return {
        "direction": direction,
        "near_zone": near_zone,
        "dist_zone_pct": float(dist_zone) if dist_zone is not None else None,
        "confirm_2m5": confirm,
        "aligned_h1": aligned_h1,
        "aligned_cli": aligned_cli,
        "bias_conflict": bias_conflict,
        "entrar_ahora": entrar_ahora,
        "setup_ok": setup_ok,
        "setup_note": setup_note,
        "setup_mode": setup_mode,
    }


def _qualify_grade(
    *,
    dist_to_last_pct: float | None,
    dist_to_curr_pct: float | None,
    revisited_last: bool,
    flags: dict[str, Any],
) -> tuple[str, str, int]:
    """Califica oportunidad ahora vs última entry + contexto High en vivo.

    Returns (grade, short_reason, score). Solo path High (no history_review).
    """
    score = 0
    reasons: list[str] = []

    near_last = dist_to_last_pct is not None and dist_to_last_pct <= _NEAR_ENTRY_PCT
    near_curr = dist_to_curr_pct is not None and dist_to_curr_pct <= _NEAR_ENTRY_PCT

    p_last = _proximity_pts(dist_to_last_pct)
    p_curr = _proximity_pts(dist_to_curr_pct)
    score += p_last + p_curr
    if near_last or revisited_last:
        reasons.append("precio cerca de última Entry")
    elif p_last == 1:
        reasons.append("cerca suave de última Entry")
    if near_curr and not (near_last or revisited_last):
        reasons.append("precio cerca de Entry actual")
    elif p_curr == 1 and not near_curr:
        reasons.append("cerca suave de Entry actual")

    if flags["confirm_2m5"]:
        score += 2
        reasons.append("2M5 OK")
    else:
        reasons.append("sin 2M5")

    if flags["near_zone"]:
        score += 1
        reasons.append("zona OK")
    else:
        reasons.append("lejos de zona")

    if flags["setup_ok"]:
        score += 1
    if flags["aligned_h1"] or flags["aligned_cli"]:
        score += 1
        if flags["aligned_h1"]:
            reasons.append("bando alineado")
    elif flags["bias_conflict"]:
        reasons.append("bias en conflicto")

    if flags["entrar_ahora"]:
        score += 1

    far = (
        (dist_to_last_pct is None or dist_to_last_pct > _SOFT_NEAR_PCT)
        and (dist_to_curr_pct is None or dist_to_curr_pct > _SOFT_NEAR_PCT)
    )
    no_confirm = not flags["confirm_2m5"] and not flags["near_zone"]

    if flags["bias_conflict"] and far:
        grade = "EVITAR"
    elif far and no_confirm:
        grade = "EVITAR"
    elif flags["direction"] == "NONE" and far:
        grade = "EVITAR"
    elif score >= 7 and (near_last or near_curr or flags["entrar_ahora"]):
        grade = "BUENA"
    elif score >= 4:
        grade = "REGULAR"
    elif score >= 2:
        grade = "MALA"
    else:
        grade = "EVITAR"

    if grade == "BUENA":
        prefer = [r for r in reasons if r in (
            "precio cerca de última Entry",
            "precio cerca de Entry actual",
            "2M5 OK",
            "zona OK",
            "bando alineado",
        )]
        reason = " + ".join(prefer[:3]) if prefer else "setup operable cerca de entry"
    elif grade == "EVITAR":
        bad = [r for r in reasons if r in (
            "lejos de zona",
            "sin 2M5",
            "bias en conflicto",
        )]
        if far:
            bad.insert(0, "lejos")
        reason = " y ".join(dict.fromkeys(bad[:3])) if bad else "sin confirmación"
    elif grade == "MALA":
        reason = "; ".join(reasons[:3]) if reasons else "setup débil"
    else:
        reason = "; ".join(reasons[:3]) if reasons else "parcial"

    return grade, reason, score


def reflect_last_entry(
    last: dict[str, Any] | None,
    *,
    price: float,
    current_entry: float | None,
    dec: int = 1,
    data: dict | None = None,
    opt: dict | None = None,
) -> dict[str, Any]:
    """Compara precio / Entrada óptima actuales vs último registro del mismo par.

    Path High (no history_review). Status: SIN HISTORIAL | MISMA ZONA | MÁS CERCA | MÁS LEJOS
    Calificación: BUENA | REGULAR | MALA | EVITAR | SIN HISTORIAL
    """
    fmt = f".{dec}f"
    flags = _live_setup_flags(data, opt)

    if not last or last.get("optimal_entry") is None:
        dist_curr = None
        dist_curr_pct = None
        if current_entry is not None and price:
            dist_curr = abs(float(price) - float(current_entry))
            dist_curr_pct = (dist_curr / float(current_entry) * 100.0) if current_entry else 0.0
        grade, reason, score = _qualify_grade(
            dist_to_last_pct=None,
            dist_to_curr_pct=dist_curr_pct,
            revisited_last=False,
            flags=flags,
        )
        if grade == "BUENA":
            grade = "REGULAR"
            reason = f"sin historial; {reason}"
        else:
            reason = f"sin historial; {reason}"
        cell_calif = f"**SIN HISTORIAL** · live **{grade}** — {reason}"
        return {
            "mode": "high",
            "status": "SIN HISTORIAL",
            "grade": "SIN HISTORIAL",
            "grade_live": grade,
            "grade_reason": reason,
            "grade_score": score,
            "last_id": None,
            "last_time": None,
            "last_entry": None,
            "delta_entry_pts": None,
            "delta_entry_pct": None,
            "dist_price_to_last_pts": None,
            "dist_price_to_last_pct": None,
            "dist_price_to_curr_pts": dist_curr,
            "dist_price_to_curr_pct": dist_curr_pct,
            "revisited_last": False,
            "cell_ultima": "—",
            "cell_vs": cell_calif,
            "cell_calificacion": cell_calif,
        }

    last_entry = float(last["optimal_entry"])
    last_id = str(last.get("id", "?"))
    last_time = str(last.get("time", "n/d"))
    dist_to_last = abs(price - last_entry)
    dist_to_last_pct = (dist_to_last / last_entry * 100.0) if last_entry else 0.0
    revisited_last = dist_to_last_pct <= _SAME_ZONE_PRICE_PCT

    delta_pts: float | None = None
    delta_pct: float | None = None
    if current_entry is not None:
        delta_pts = float(current_entry) - last_entry
        delta_pct = (delta_pts / last_entry * 100.0) if last_entry else 0.0

    dist_to_curr: float | None = None
    dist_to_curr_pct: float | None = None
    if current_entry is not None:
        dist_to_curr = abs(price - float(current_entry))
        dist_to_curr_pct = (
            (dist_to_curr / float(current_entry) * 100.0) if current_entry else 0.0
        )

    if current_entry is not None and abs(delta_pct or 0.0) <= _SAME_ZONE_ENTRY_PCT:
        status = "MISMA ZONA"
    elif revisited_last:
        status = "MISMA ZONA"
    elif current_entry is not None and dist_to_curr is not None:
        if dist_to_curr < dist_to_last:
            status = "MÁS CERCA"
        elif dist_to_curr > dist_to_last:
            status = "MÁS LEJOS"
        else:
            status = "MISMA ZONA"
    else:
        status = "MISMA ZONA" if revisited_last else "MÁS LEJOS"

    grade, reason, score = _qualify_grade(
        dist_to_last_pct=dist_to_last_pct,
        dist_to_curr_pct=dist_to_curr_pct,
        revisited_last=revisited_last,
        flags=flags,
    )

    cell_ultima = (
        f"**{last_id}** · {last_time} · Entry **{last_entry:{fmt}}**"
    )
    parts = [f"**{grade}** — {reason}"]
    parts.append(f"({status})")
    if delta_pts is not None:
        parts.append(f"Δ Entry {delta_pts:+{fmt}} pts ({delta_pct:+.3f}%)")
    parts.append(f"precio→última {dist_to_last:{fmt}} pts ({dist_to_last_pct:.3f}%)")
    if dist_to_curr is not None and dist_to_curr_pct is not None:
        parts.append(f"precio→actual {dist_to_curr:{fmt}} pts ({dist_to_curr_pct:.3f}%)")
    cell_calif = " · ".join(parts)

    return {
        "mode": "high",
        "status": status,
        "grade": grade,
        "grade_live": grade,
        "grade_reason": reason,
        "grade_score": score,
        "last_id": last_id,
        "last_time": last_time,
        "last_entry": last_entry,
        "delta_entry_pts": delta_pts,
        "delta_entry_pct": delta_pct,
        "dist_price_to_last_pts": dist_to_last,
        "dist_price_to_last_pct": dist_to_last_pct,
        "dist_price_to_curr_pts": dist_to_curr,
        "dist_price_to_curr_pct": dist_to_curr_pct,
        "revisited_last": revisited_last,
        "cell_ultima": cell_ultima,
        "cell_vs": cell_calif,
        "cell_calificacion": cell_calif,
    }


def _infer_append_side(data: dict, opt: dict | None) -> str | None:
    side, _ = resolve_side(None, data=data, opt=opt)
    return side


def persist_and_reflect_entry(
    data: dict,
    opt: dict | None,
    *,
    history_dir: Path | None = None,
    cap: int = HISTORY_CAP,
    history_mode: bool | None = None,
    append: bool | None = None,
) -> dict[str, Any]:
    """Load last record del mismo asset, reflect/review, optionally append.

    history_mode=True (--history-review): revisión P&L, NO append, NO señal nueva.
    history_mode=False (High): reflexión geométrica + append si hay Entrada óptima.

    Isolation: path = btc_signal_history.json | us30_signal_history.json según asset_label.
    """
    if history_mode is None:
        history_mode = bool(data.get("history_mode"))
    if append is None:
        append = not history_mode

    asset = data.get("asset_label", "BTC")
    base = history_dir
    if base is None and data.get("signal_history_dir"):
        base = Path(data["signal_history_dir"])
    path = history_path_for_asset(asset, base)

    history = load_signal_history(path)
    last = history[-1] if history else None

    dec = int((opt or {}).get("dec", data.get("price_decimals", 1)))
    current_entry = (opt or {}).get("entry")
    if current_entry is not None:
        try:
            current_entry = float(current_entry)
        except (TypeError, ValueError):
            current_entry = None

    price = float(data.get("price") or 0.0)

    if history_mode:
        reflection = review_last_entry_pnl(
            last,
            price=price,
            dec=dec,
            data=data,
            opt=opt,
        )
    else:
        reflection = reflect_last_entry(
            last,
            price=price,
            current_entry=current_entry,
            dec=dec,
            data=data,
            opt=opt,
        )

    if append and current_entry is not None:
        append_signal_history(
            path,
            asset=asset,
            time_str=format_history_time(data),
            optimal_entry=current_entry,
            side=_infer_append_side(data, opt),
            cap=cap,
        )

    return reflection
