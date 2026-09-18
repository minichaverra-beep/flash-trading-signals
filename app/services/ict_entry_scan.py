"""ICT-informed entry scan and refinement for high-signal optimal entry.

Minimal focused logic: FVG, order blocks, liquidity sweeps, premium/discount,
displacement, session/killzone alignment. Does not replace rules engine or verdict.
"""
from __future__ import annotations

from typing import Any


def _avg_body(m5: list[dict], n: int = 14) -> float:
    if not m5:
        return 0.0
    window = m5[-n:]
    return sum(abs(c["close"] - c["open"]) for c in window) / len(window)


def detect_fvgs(m5: list[dict], *, lookback: int = 48) -> list[dict]:
    """Fair value gaps: 3-candle imbalance (ICT)."""
    out: list[dict] = []
    if len(m5) < 3:
        return out
    start = max(2, len(m5) - lookback)
    for i in range(start, len(m5)):
        c0, c2 = m5[i - 2], m5[i]
        # Bullish FVG: gap between c0 high and c2 low
        if c0["high"] < c2["low"]:
            out.append({
                "type": "BULLISH",
                "lo": float(c0["high"]),
                "hi": float(c2["low"]),
                "mid": (float(c0["high"]) + float(c2["low"])) / 2,
                "idx": i,
            })
        # Bearish FVG
        if c0["low"] > c2["high"]:
            out.append({
                "type": "BEARISH",
                "lo": float(c2["high"]),
                "hi": float(c0["low"]),
                "mid": (float(c2["high"]) + float(c0["low"])) / 2,
                "idx": i,
            })
    return out


def detect_order_blocks(m5: list[dict], *, lookback: int = 48) -> list[dict]:
    """Order blocks: last opposing candle before displacement."""
    out: list[dict] = []
    if len(m5) < 4:
        return out
    avg_body = _avg_body(m5)
    if avg_body <= 0:
        return out
    start = max(3, len(m5) - lookback)
    for i in range(start, len(m5)):
        c = m5[i]
        prev = m5[i - 1]
        body = abs(c["close"] - c["open"])
        if body < avg_body * 1.4:
            continue
        bull = c["close"] > c["open"]
        bear = c["close"] < c["open"]
        if bull and prev["close"] < prev["open"]:
            out.append({
                "type": "BULLISH",
                "lo": float(prev["low"]),
                "hi": float(prev["high"]),
                "mid": (float(prev["low"]) + float(prev["high"])) / 2,
                "idx": i - 1,
            })
        elif bear and prev["close"] > prev["open"]:
            out.append({
                "type": "BEARISH",
                "lo": float(prev["low"]),
                "hi": float(prev["high"]),
                "mid": (float(prev["low"]) + float(prev["high"])) / 2,
                "idx": i - 1,
            })
    return out


def detect_liquidity_sweeps(
    m5: list[dict],
    swing_highs: list[float] | None,
    swing_lows: list[float] | None,
    pdh: float | None,
    pdl: float | None,
    *,
    lookback: int = 36,
) -> list[dict]:
    """Liquidity sweeps: wick beyond level + reclaim close."""
    out: list[dict] = []
    if not m5:
        return out
    window = m5[-lookback:] if len(m5) >= lookback else m5
    levels: list[tuple[float, str]] = []
    for lvl in swing_lows or []:
        levels.append((float(lvl), "swing_low"))
    for lvl in swing_highs or []:
        levels.append((float(lvl), "swing_high"))
    if pdl is not None:
        levels.append((float(pdl), "PDL"))
    if pdh is not None:
        levels.append((float(pdh), "PDH"))

    for lvl, label in levels:
        for c in window:
            if c["low"] < lvl and c["close"] > lvl:
                out.append({
                    "type": "BULLISH",
                    "level": lvl,
                    "label": label,
                    "entry_hint": float(lvl),
                    "note": f"Sweep {label} @ {lvl:.1f} + reclaim",
                })
            if c["high"] > lvl and c["close"] < lvl:
                out.append({
                    "type": "BEARISH",
                    "level": lvl,
                    "label": label,
                    "entry_hint": float(lvl),
                    "note": f"Sweep {label} @ {lvl:.1f} + reclaim",
                })
    return out


def _session_killzone(session: dict | None) -> tuple[str, bool]:
    if not session:
        return "n/d", False
    if "killzone_on" in session:
        return str(session.get("window") or "n/d"), bool(session.get("killzone_on"))
    window = str(session.get("window") or "")
    aligned = bool(session.get("in_ny_window")) or any(
        k in window for k in ("NY AM", "NY PM", "08-10", "10-11", "14-16", "08-11")
    )
    return window or "n/d", aligned


def scan_ict_context(
    data: dict,
    direction: str,
    crt: dict | None,
    zone: dict | None,
) -> dict[str, Any]:
    """Scan M5/H1/CRT for ICT structures relevant to entry refinement."""
    m5 = data.get("m5") or []
    crt = crt or {}
    zone = zone or data.get("zone") or {}
    price = float(data.get("price") or 0)
    fvgs = detect_fvgs(m5)
    obs = detect_order_blocks(m5)
    sweeps = detect_liquidity_sweeps(
        m5, data.get("swing_highs"), data.get("swing_lows"),
        data.get("pdh"), data.get("pdl"),
    )
    prem = crt.get("premium_discount", "n/a")
    mid = crt.get("midpoint")
    h1_state = crt.get("h1_state", "n/a")
    session_win, killzone_ok = _session_killzone(data.get("session"))

    dir_fvgs = [f for f in fvgs if f["type"] == ("BULLISH" if direction == "LONG" else "BEARISH")]
    dir_obs = [o for o in obs if o["type"] == ("BULLISH" if direction == "LONG" else "BEARISH")]
    dir_sweeps = [s for s in sweeps if s["type"] == ("BULLISH" if direction == "LONG" else "BEARISH")]

    displacement = False
    if m5:
        last = m5[-1]
        avg_b = _avg_body(m5)
        if avg_b > 0 and abs(last["close"] - last["open"]) >= avg_b * 1.5:
            displacement = True

    pd_ok = (
        (direction == "LONG" and prem in ("DISCOUNT", "EQUILIBRIO 0.5", "n/a"))
        or (direction == "SHORT" and prem in ("PREMIUM", "EQUILIBRIO 0.5", "n/a"))
    )

    return {
        "fvgs": dir_fvgs[-5:],
        "order_blocks": dir_obs[-5:],
        "sweeps": dir_sweeps[-5:],
        "premium_discount": prem,
        "midpoint": mid,
        "pd_ok": pd_ok,
        "h1_state": h1_state,
        "displacement": displacement,
        "killzone": session_win,
        "killzone_ok": killzone_ok,
        "price": price,
        "zone_level": zone.get("level"),
        "zone_type": zone.get("type"),
        "direction": direction,
    }


def _score_candidate(
    entry: float,
    price: float,
    direction: str,
    source: str,
    ict: dict,
) -> float:
    score = 0.0
    mid = ict.get("midpoint")
    if direction == "LONG":
        if entry <= price:
            score += 3.0
        elif (entry - price) / max(price, 1) * 100 > 0.05:
            score -= 4.0
        if mid and entry <= float(mid):
            score += 2.5
        if ict.get("pd_ok"):
            score += 1.0
    else:
        if entry >= price:
            score += 3.0
        elif (price - entry) / max(price, 1) * 100 > 0.05:
            score -= 4.0
        if mid and entry >= float(mid):
            score += 2.5
        if ict.get("pd_ok"):
            score += 1.0

    if "sweep" in source.lower() or ict.get("sweeps"):
        score += 2.0
    if "FVG" in source:
        score += 1.5
    if "OB" in source:
        score += 1.5
    if ict.get("h1_state") in ("PENDING_BULL", "PENDING_BEAR"):
        score += 1.0
    if ict.get("killzone_ok"):
        score += 0.5
    if ict.get("displacement"):
        score += 0.5

    dist_pct = abs(entry - price) / max(price, 1) * 100
    if dist_pct <= 0.15:
        score += 1.0
    elif dist_pct > 0.35:
        score -= 1.0
    return score


def _collect_entry_candidates(
    base_entry: float,
    direction: str,
    ict: dict,
    zone: dict,
) -> list[tuple[float, str, float]]:
    """Return (entry, source_label, score) candidates."""
    price = float(ict["price"])
    cands: list[tuple[float, str, float]] = [
        (base_entry, "zona base", _score_candidate(base_entry, price, direction, "zona base", ict)),
    ]
    level = zone.get("level")
    ztype = zone.get("type") or ""

    for fvg in ict.get("fvgs") or []:
        edge = float(fvg["lo"]) if direction == "LONG" else float(fvg["hi"])
        src = f"FVG {fvg['type']} edge"
        cands.append((edge, src, _score_candidate(edge, price, direction, src, ict)))

    for ob in ict.get("order_blocks") or []:
        edge = float(ob["hi"]) if direction == "LONG" else float(ob["lo"])
        src = f"OB {ob['type']} edge"
        cands.append((edge, src, _score_candidate(edge, price, direction, src, ict)))

    for sw in ict.get("sweeps") or []:
        hint = float(sw["entry_hint"])
        src = f"sweep {sw.get('label', 'liq')}"
        cands.append((hint, src, _score_candidate(hint, price, direction, src, ict)))

    mid = ict.get("midpoint")
    if mid is not None:
        mid_f = float(mid)
        if direction == "LONG" and mid_f < price:
            cands.append((mid_f, "discount 0.5", _score_candidate(mid_f, price, direction, "discount", ict)))
        elif direction == "SHORT" and mid_f > price:
            cands.append((mid_f, "premium 0.5", _score_candidate(mid_f, price, direction, "premium", ict)))

    if level is not None:
        lvl = float(level)
        if direction == "LONG" and ztype == "soporte_debil":
            cands.append((lvl, "soporte debil", _score_candidate(lvl, price, direction, "zona", ict)))
        elif direction == "SHORT" and ztype == "resistencia_debil":
            cands.append((lvl, "resistencia debil", _score_candidate(lvl, price, direction, "zona", ict)))

    return cands


def build_scalp_entry_levels(
    opt: dict,
    data: dict,
    direction: str,
    crt: dict | None,
    zone: dict | None,
    *,
    limit: int = 3,
) -> list[tuple[float, str]]:
    """Top micro-entradas scalp (ICT + zona) para history-review."""
    if not opt.get("valid") or opt.get("entry") is None:
        return []
    dec = int(opt.get("dec", data.get("price_decimals", 1)))
    ict = opt.get("ict_scan") or scan_ict_context(data, direction, crt, zone)
    base = float(opt["entry"])
    cands = _collect_entry_candidates(base, direction, ict, zone or {})
    seen: set[float] = set()
    out: list[tuple[float, str]] = []
    for entry, src, score in sorted(cands, key=lambda x: (-x[2], x[0])):
        rounded = round(float(entry), dec)
        if rounded in seen:
            continue
        seen.add(rounded)
        out.append((rounded, src))
        if len(out) >= limit:
            break
    return out


def _recalc_sl_tp_from_entry(
    entry: float,
    direction: str,
    zone: dict,
    data: dict,
    dec: int,
) -> tuple[float, float, float]:
    """Structural SL/TP 1:2 from refined entry (same rules as core)."""
    level = zone.get("level")
    ztype = zone.get("type", "zona")
    fmt = f".{dec}f"
    _ = fmt
    if direction == "SHORT":
        if level:
            sl = float(level) * 1.002 if ztype == "resistencia_debil" else float(level) * 1.003
        else:
            sl = entry * 1.003
        if sl <= entry:
            sl = entry * 1.003
        risk = abs(sl - entry)
        tp = entry - 2 * risk
    else:
        if level:
            sl = float(level) * 0.998 if ztype == "soporte_debil" else float(level) * 0.997
        else:
            sl = entry * 0.997
        if sl >= entry:
            sl = entry * 0.997
        risk = abs(entry - sl)
        tp = entry + 2 * risk
    return sl, tp, risk


def refine_entry_with_ict(
    opt: dict,
    data: dict,
    direction: str,
    crt: dict | None,
    zone: dict | None,
) -> dict:
    """Refine system optimal entry using ICT scan; preserve plan fields."""
    if not opt.get("valid") or direction not in ("LONG", "SHORT"):
        return opt
    if opt.get("entry") is None:
        return opt

    ict = scan_ict_context(data, direction, crt, zone)
    base_entry = float(opt["entry"])
    cands = _collect_entry_candidates(base_entry, direction, ict, zone or {})
    best_entry, best_src, best_score = max(cands, key=lambda x: x[2])

    out = dict(opt)
    out["entry_before_ict"] = base_entry
    out["ict_scan"] = ict
    dec = int(opt.get("dec", data.get("price_decimals", 1)))

    if abs(best_entry - base_entry) < 10 ** (-dec) / 2:
        out["ict_refined"] = False
        out["ict_source"] = "zona base (sin cambio ICT)"
        out["ict_note"] = _build_ict_note(ict, base_entry, base_entry, best_src, refined=False)
        if data.get("history_mode") or data.get("scalp_mode"):
            out["scalp_entries"] = build_scalp_entry_levels(
                out, data, direction, crt, zone, limit=3,
            )
        return out

    sl, tp, risk = _recalc_sl_tp_from_entry(best_entry, direction, zone or {}, data, dec)
    fmt = f".{dec}f"
    out["entry"] = best_entry
    out["sl"] = sl
    out["tp"] = tp
    out["risk_pts"] = risk
    out["rr"] = 2.0
    out["ict_refined"] = True
    out["ict_source"] = best_src
    out["ict_score"] = best_score

    zone_lo = out.get("zone_lo")
    zone_hi = out.get("zone_hi")
    if direction == "LONG" and zone_lo is not None and zone_hi is not None:
        out["zone_lo"] = min(float(zone_lo), best_entry)
        out["zone_hi"] = max(float(zone_hi), best_entry)
        out["opti_zone"] = f"{out['zone_lo']:{fmt}}–{out['zone_hi']:{fmt}}"
    elif direction == "SHORT" and zone_lo is not None and zone_hi is not None:
        out["zone_lo"] = min(float(zone_lo), best_entry)
        out["zone_hi"] = max(float(zone_hi), best_entry)
        out["opti_zone"] = f"{out['zone_lo']:{fmt}}–{out['zone_hi']:{fmt}}"

    chase = (
        (direction == "LONG" and best_entry > float(data["price"]) * 1.0005)
        or (direction == "SHORT" and best_entry < float(data["price"]) * 0.9995)
    )
    if chase:
        out["opti_action"] = f"ESPERAR {direction} (ICT limit · no chase)"
    elif "ESPERAR" in str(out.get("ahora_action", "")):
        out["opti_action"] = f"ENTRAR {direction} (ICT retest · {best_src})"

    out["trigger"] = (
        f"ICT retest {best_src} @ {best_entry:{fmt}} "
        f"+ 2 velas M5 {'verdes' if direction == 'LONG' else 'rojas'} en zona"
    )
    out["ict_note"] = _build_ict_note(ict, base_entry, best_entry, best_src, refined=True)
    if data.get("history_mode") or data.get("scalp_mode"):
        out["scalp_entries"] = build_scalp_entry_levels(
            out, data, direction, crt, zone, limit=3,
        )
    return out


def _build_ict_note(
    ict: dict,
    before: float,
    after: float,
    source: str,
    *,
    refined: bool,
) -> str:
    parts = []
    if refined:
        parts.append(f"Refinada {before:.1f}→{after:.1f} ({source})")
    else:
        parts.append(f"Base {after:.1f} ({source})")
    if ict.get("sweeps"):
        parts.append(ict["sweeps"][-1].get("note", "sweep"))
    if ict.get("premium_discount") not in (None, "n/a"):
        parts.append(f"PD {ict['premium_discount']}")
    if ict.get("h1_state") not in (None, "n/a"):
        parts.append(f"H1 {ict['h1_state']}")
    if ict.get("killzone_ok"):
        parts.append(f"killzone {ict.get('killzone')}")
    return " · ".join(parts)


def format_ict_scan_cell(opt: dict | None) -> str | None:
    """One-line ICT summary for Categories table."""
    if not opt or not opt.get("ict_scan"):
        return None
    note = opt.get("ict_note") or opt.get("ict_source", "n/d")
    if opt.get("ict_refined") and opt.get("entry_before_ict") is not None:
        dec = int(opt.get("dec", 1))
        fmt = f".{dec}f"
        return (
            f"{opt['entry_before_ict']:{fmt}}→{opt['entry']:{fmt}} · {note}"
        )
    return note


def format_ict_scan_md(opt: dict, data: dict) -> list[str]:
    """Markdown ICT scan section for High signal report."""
    ict = opt.get("ict_scan")
    if not ict:
        return []
    dec = int(opt.get("dec", data.get("price_decimals", 1)))
    fmt = f".{dec}f"
    lines = [
        "## ICT scan (entrada)",
        "",
        "| Concepto | Detalle |",
        "|----------|---------|",
        f"| Premium/Discount | **{ict.get('premium_discount', 'n/a')}** "
        f"{'✅' if ict.get('pd_ok') else '⚠️'} |",
    ]
    if ict.get("midpoint") is not None:
        lines.append(f"| 0.5 midpoint | {ict['midpoint']:{fmt}} |")
    lines.append(f"| H1 CRT state | **{ict.get('h1_state', 'n/a')}** |")
    lines.append(
        f"| Killzone / sesión | {ict.get('killzone', 'n/d')} "
        f"{'✅' if ict.get('killzone_ok') else '(info)'} |"
    )
    lines.append(f"| Displacement M5 | {'Sí' if ict.get('displacement') else 'No'} |")

    if ict.get("sweeps"):
        sw = ict["sweeps"][-1]
        lines.append(f"| Liquidity sweep | {sw.get('note', 'n/d')} |")
    else:
        lines.append("| Liquidity sweep | Sin sweep+reclaim reciente |")

    fvg_n = len(ict.get("fvgs") or [])
    ob_n = len(ict.get("order_blocks") or [])
    lines.append(f"| FVG alineados | {fvg_n} |")
    lines.append(f"| Order blocks | {ob_n} |")

    if opt.get("ict_refined"):
        lines.append(
            f"| Entrada refinada | **{opt['entry']:{fmt}}** "
            f"(antes {opt.get('entry_before_ict', 0):{fmt}} · {opt.get('ict_source', 'ICT')}) |"
        )
    else:
        lines.append(f"| Entrada | **{opt.get('entry', 0):{fmt}}** (zona base · sin cambio) |")
    if opt.get("ict_note"):
        lines.append(f"| Nota | {opt['ict_note']} |")
    lines += ["", "---", ""]
    return lines
