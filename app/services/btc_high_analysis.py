"""Deep CRT + Turtle Soup analysis for btc_m5_high_signal.md"""
from __future__ import annotations

import copy
from pathlib import Path


def _mode_bias_label(mode: str) -> str:
    return {"auto": "AUTO", "bullish": "BULLISH", "bearish": "BEARISH"}.get(mode, mode.upper())


def _mode_setup_label(mode: str) -> str:
    return {
        "auto": "AUTO",
        "break": "BREAK (breakout)",
        "reverse": "REVERSE (E2)",
    }.get(mode, mode.upper())


def apply_forced_bias(data: dict, bias_mode: str) -> dict:
    """Override setup direction when user forces bullish/bearish bias."""
    if bias_mode not in ("bullish", "bearish"):
        return data
    out = copy.copy(data)
    setup = copy.copy(out["setup"])
    direction = "LONG" if bias_mode == "bullish" else "SHORT"
    setup["direction"] = direction
    setup["red_flags"] = [
        r for r in setup.get("red_flags", [])
        if "NEUTRAL" not in r and "no forzar" not in r.lower()
    ]
    hint = "Bias forzado CLI: alcista (LONG)" if bias_mode == "bullish" else "Bias forzado CLI: bajista (SHORT)"
    setup["reasons"] = [hint] + [r for r in setup.get("reasons", []) if "Bias" not in r]
    price = out["price"]
    zone = out["zone"]
    if direction == "LONG" and zone.get("level"):
        sl = min(zone["level"], price) * 0.998 if zone.get("type") == "soporte_debil" else price * 0.997
        risk = abs(price - sl)
        setup["sl"], setup["tp"], setup["rr"] = sl, price + 2 * risk, 2.0
    elif direction == "SHORT" and zone.get("level"):
        sl = max(zone["level"], price) * 1.002 if zone.get("type") == "resistencia_debil" else price * 1.003
        risk = abs(sl - price)
        setup["sl"], setup["tp"], setup["rr"] = sl, price - 2 * risk, 2.0
    near = zone.get("dist_pct") is not None and zone["dist_pct"] <= 0.15
    confirm = out["confirm_long"] if direction == "LONG" else out["confirm_short"]
    # Sesión NY no es hard-block para SETUP_A+
    hard = [r for r in setup["red_flags"] if any(k in r for k in ("Lejos", "Sin 2"))]
    if not hard and near and confirm:
        setup["verdict"] = "SETUP_A+"
    elif not hard and near:
        setup["verdict"] = "SETUP_B_ESPERAR"
    elif direction != "NONE":
        setup["verdict"] = "NO_TRADE"
    out["setup"] = setup
    out["forced_bias"] = bias_mode
    return out


def analyze_breakout(
    price: float,
    m5: list[dict],
    zone: dict,
    crt: dict,
    data: dict,
    direction: str,
) -> dict:
    """Breakout de nivel/estructura — distinto de Reverse (fakeout/reclaim).

    Break válido = cierre más allá del nivel y precio que **mantiene** el break
    (no reclaim). Fakeout = barrido + vuelta = NO es Break.
    """
    level = zone.get("level")
    ztype = zone.get("type") or ""
    pdh, pdl = data.get("pdh"), data.get("pdl")
    confirm_long = data.get("confirm_long", False)
    confirm_short = data.get("confirm_short", False)
    held = False
    broken_level = None
    kind = "none"
    note = "Sin breakout de nivel detectado"

    # Prefer structure zone; fall back to PDH/PDL
    if direction == "LONG":
        target = level if ztype == "resistencia_debil" else (pdh or level)
        if target and price > target:
            # Held breakout: last 2 closes above level (not a wick fakeout)
            recent = m5[-2:] if len(m5) >= 2 else m5
            held = bool(recent) and all(c["close"] > target for c in recent)
            broken_level = target
            kind = "bullish_breakout"
            note = (
                f"Breakout alcista sostenido > {target:.0f}"
                if held
                else f"Precio > {target:.0f} pero sin hold de 2 cierres — no chase"
            )
        elif crt.get("fakeout_pdh"):
            note = "Fakeout PDH (barrido + reclaim) — NO es Break; es contexto Reverse"
            kind = "failed_break_fakeout"
    elif direction == "SHORT":
        target = level if ztype == "soporte_debil" else (pdl or level)
        if target and price < target:
            recent = m5[-2:] if len(m5) >= 2 else m5
            held = bool(recent) and all(c["close"] < target for c in recent)
            broken_level = target
            kind = "bearish_breakout"
            note = (
                f"Breakout bajista sostenido < {target:.0f}"
                if held
                else f"Precio < {target:.0f} pero sin hold de 2 cierres — no chase"
            )
        elif crt.get("fakeout_pdl"):
            note = "Fakeout PDL (barrido + reclaim) — NO es Break; es contexto Reverse"
            kind = "failed_break_fakeout"

    candles_ok = (
        (direction == "LONG" and confirm_long)
        or (direction == "SHORT" and confirm_short)
    )
    valid = held and candles_ok and kind.endswith("breakout")
    return {
        "valid": valid,
        "held": held,
        "kind": kind,
        "level": broken_level,
        "candles_ok": candles_ok,
        "note": note,
    }


def adjust_crt_for_setup_mode(crt: dict, setup_mode: str, data: dict) -> dict:
    """Emphasize breakout (Break) vs reversal/fakeout (Reverse)."""
    if setup_mode == "auto":
        return crt
    out = copy.copy(crt)
    notes: list[str] = []
    direction = data.get("setup", {}).get("direction", "NONE")
    if setup_mode == "break":
        bo = analyze_breakout(
            data["price"], data.get("m5", []), data.get("zone", {}), out, data, direction,
        )
        out["breakout"] = bo
        out["crt_action_e1"] = (
            out.get("crt_action_e1", "") + " | Modo BREAK: breakout de nivel/estructura (no reversión)"
        ).strip(" |")
        if bo.get("valid"):
            notes.append(f"BREAK OK: {bo['note']}")
        elif bo.get("kind") == "failed_break_fakeout":
            notes.append(f"BREAK inválido: {bo['note']}")
        else:
            notes.append(f"BREAK pendiente: {bo['note']}")
        if out.get("fakeout_pdh") or out.get("fakeout_pdl"):
            notes.append("Fakeout ≠ Break — no tratar sweep+reclaim como breakout")
    elif setup_mode == "reverse":
        out["crt_action_e1"] = (
            out.get("crt_action_e1", "") + " | Modo REVERSE: turtle soup / fakeout / sweep+reclaim"
        ).strip(" |")
        if out.get("fakeout_pdh"):
            notes.append("REVERSE: fakeout PDH — turtle soup bajista posible")
        if out.get("fakeout_pdl"):
            notes.append("REVERSE: fakeout PDL + reclaim — watchlist E2")
        if out.get("h1_state", "").startswith("PENDING"):
            notes.append(f"REVERSE: H1 {out['h1_state']} — sweep+reclaim E2 ctx")
    if notes:
        extra = " | ".join(notes)
        out["fakeout_note"] = (
            extra if not out.get("fakeout_note") else out["fakeout_note"] + " | " + extra
        )
    out["mode_setup"] = setup_mode
    return out


def adjust_e2_for_setup_mode(e2: dict, setup_mode: str, data: dict | None = None) -> dict:
    """Elevate Reverse (operable con 2 velas alineadas) o despriorizar E2 en Break."""
    if setup_mode == "auto":
        return e2
    out = copy.copy(e2)
    checks = list(out.get("checks", []))
    score = out.get("score", 0)
    data = data or {}
    direction = data.get("setup", {}).get("direction", "NONE")
    confirm = (
        data.get("confirm_long", False) if direction == "LONG"
        else data.get("confirm_short", False) if direction == "SHORT"
        else False
    )

    if setup_mode == "break":
        out["note"] = (
            "Modo BREAK: breakout de nivel — E2/reversión despriorizada, NO operable"
        )
        out["eligible"] = False
        out["verdict"] = "E2_NO"
        out["winrate"] = None
    elif setup_mode == "reverse":
        from app.models.btc_signal_categories import WR_BTC_E2, WR_E2_GLOBAL

        boosted = min(score + 1, out.get("max", 6))
        out["score"] = boosted
        # Operable si las últimas 2 velas van en la misma dirección del bando
        operable = bool(confirm and direction in ("LONG", "SHORT"))
        out["eligible"] = operable
        if operable:
            out["verdict"] = "E2_READY" if boosted >= 4 else "E2_WATCH"
            out["note"] = (
                f"Modo REVERSE operable — 2 velas M5 alineadas ({direction}); "
                f"WR histórico E2 ~{WR_BTC_E2:.0f}% BTC / ~{WR_E2_GLOBAL:.0f}% global"
            )
        else:
            out["verdict"] = "E2_WATCH" if boosted >= 3 else "E2_NO"
            out["note"] = (
                "Modo REVERSE: falta 2 velas M5 misma dirección del bando — "
                f"no operable aún (WR E2 ~{WR_BTC_E2:.0f}% si se confirma)"
            )
        out["winrate"] = f"~{WR_BTC_E2:.0f}%"
        out["winrate_source"] = f"histórico E2 BTC reversión (~{WR_E2_GLOBAL:.0f}% E2 global)"
        if checks:
            checks = list(checks)
            checks.append(
                (
                    "7. 2 velas misma dirección",
                    operable,
                    f"{direction} confirmado" if operable else "Esperar 2 velas alineadas",
                )
            )
            checks.append(("8. Winrate E2", True, out["winrate"]))
            out["checks"] = checks
    out["mode_setup"] = setup_mode
    return out


def adjust_gallery_for_setup_mode(
    patterns: list[str], setup_mode: str, data: dict, crt: dict,
) -> list[str]:
    """Weight gallery hints toward breakout or reversal."""
    pats = list(patterns)
    if setup_mode == "break":
        bo = crt.get("breakout") or {}
        if bo.get("valid") and data.get("confirm_long"):
            pats.insert(0, "WIN: BREAK breakout alcista + hold (continuación tras ruptura)")
        if bo.get("valid") and data.get("confirm_short"):
            pats.insert(0, "WIN: BREAK breakout bajista + hold (continuación tras ruptura)")
        if bo.get("kind") == "failed_break_fakeout" or crt.get("fakeout_pdh"):
            pats.append("LOSS: fakeout tratado como breakout — no es Break")
    elif setup_mode == "reverse":
        if crt.get("fakeout_pdl"):
            pats.insert(0, "WIN: REVERSE turtle soup PDL + reclaim")
        if crt.get("fakeout_pdh"):
            pats.insert(0, "WIN: REVERSE turtle soup PDH sweep")
        if crt.get("h1_state", "").startswith("PENDING"):
            pats.insert(0, "WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26)")
        if data.get("confirm_long") or data.get("confirm_short"):
            pats.insert(0, "WIN: REVERSE 2 velas alineadas al bando")
    return pats or patterns


def mode_reasoning_notes(bias_mode: str, setup_mode: str, data: dict, crt: dict, e2: dict) -> list[str]:
    """Verdict reasoning lines when bias/setup forced."""
    notes: list[str] = []
    if bias_mode == "bullish":
        notes.append("Bias CLI **BULLISH** — setup re-puntuado como LONG")
        if data["bias_h1"] == "BEARISH":
            notes.append("⚠ H1 bajista vs bias forzado — confirmar en TV antes de entrar")
    elif bias_mode == "bearish":
        notes.append("Bias CLI **BEARISH** — setup re-puntuado como SHORT")
        if data["bias_h1"] == "BULLISH":
            notes.append("⚠ H1 alcista vs bias forzado — confirmar en TV antes de entrar")
    if setup_mode == "break":
        bo = crt.get("breakout") or {}
        notes.append("Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)")
        notes.append(bo.get("note", "Evaluar hold post-ruptura en TV"))
        if bo.get("valid"):
            notes.append("Breakout válido + 2 velas en dirección — continuación post-ruptura")
    elif setup_mode == "reverse":
        wr = e2.get("winrate", "~61%")
        notes.append("Setup **REVERSE** — turtle soup / PDH-PDL fakeout / sweep+reclaim")
        notes.append(
            f"E2: {e2.get('verdict', 'E2_NO')} ({e2.get('score', 0)}/{e2.get('max', 6)}) · "
            f"operable={'SÍ' if e2.get('eligible') else 'NO'} · WR {wr}"
        )
    return notes


def last_h1_summary(h1: list[dict], n: int = 3) -> list[str]:
    """Resumen últimas N velas H1 para CRT deep dive."""
    lines = []
    for c in h1[-n:]:
        body = c["close"] - c["open"]
        color = "G" if body >= 0 else "R"
        lines.append(
            f"{c['open_time'].strftime('%m-%d %H:%M')} O={c['open']:.0f} H={c['high']:.0f} "
            f"L={c['low']:.0f} C={c['close']:.0f} [{color}]"
        )
    return lines


def _pdh_pdl_distances(price: float, pdh: float | None, pdl: float | None) -> dict:
    out = {"pdh_pts": None, "pdh_pct": None, "pdl_pts": None, "pdl_pct": None}
    if pdh:
        out["pdh_pts"] = price - pdh
        out["pdh_pct"] = (price - pdh) / pdh * 100
    if pdl:
        out["pdl_pts"] = price - pdl
        out["pdl_pct"] = (price - pdl) / pdl * 100
    return out


def _ml_bucket_note(ml_prob: float) -> str:
    pct = ml_prob * 100
    if pct < 45:
        return "NO_OPERAR — WR real 24.8% (bucket <45%)"
    if pct < 55:
        return "ESPERAR — zona gris WR 60.9% (45–55%)"
    if pct < 65:
        return "NO_OPERAR — anomalía WR 21.1% (55–65%)"
    if pct < 75:
        return "Confluencia positiva si Rules ≥70% (65–75%, WR 75%)"
    return "A+ si Rules ≥70% + extendidas ≥70% (>75%, WR 83.3%)"


def _ml_neural_agreement(categories: dict) -> tuple[str, str]:
    """ALIGNED | CONFLICT | NEUTRAL + explicación."""
    ml = categories.get("ml_prob_win")
    nw = categories.get("neural_prob_win")
    if ml is None and nw is None:
        return "NEUTRAL", "Sin datos ML/Neural"
    if ml is None or nw is None:
        return "NEUTRAL", "Solo una fuente disponible — cruzar con Rules %"
    ml_h, ml_l = ml >= 0.65, ml < 0.45
    nw_h, nw_l = nw >= 0.70, nw < 0.50
    if (ml_h and nw_h) or (ml_l and nw_l):
        return "ALIGNED", "ML y Neural apuntan misma dirección de confianza"
    if ml_l and nw_h:
        return (
            "CONFLICT",
            "Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual "
            "fuerte pero features ML desfavorables; priorizar Rules % + CRT",
        )
    if ml_h and nw_l:
        return (
            "CONFLICT",
            "Tensión: ML favorable vs Neural bajo — galería no valida; exigir TV + CRT",
        )
    return "NEUTRAL", "Ambos en zona media — decidir con Rules % y CRT"


def _pattern_tags(pattern: str) -> str:
    p = pattern.lower()
    tags = []
    if "continu" in p or "break" in p:
        tags.append("continuación")
    if "fakeout" in p or "trampa" in p:
        tags.append("fakeout")
    if "contra bias" in p or "contra-bias" in p:
        tags.append("contra-bias")
    if "sweep" in p or "reclaim" in p or "turtle" in p:
        tags.append("sweep+reclaim")
    if "rechazo" in p or "resistencia" in p:
        tags.append("rechazo")
    if pattern.startswith("LOSS"):
        tags.append("LOSS")
    elif pattern.startswith("WIN"):
        tags.append("WIN")
    return ", ".join(tags) if tags else "general"


def _extract_btc_filename(pattern: str) -> str | None:
    import re
    m = re.search(r"BTC[-\d]+[-\d]+[-\d]+", pattern.upper())
    if m:
        return m.group(0) + ".png"
    return None


# High fusion weights (documented). Missing sources are omitted and renormalized —
# never pad Neural with fake 50%. See docs/strategy/DEEP_LEARNING_SIGNALS.md.
HIGH_FUSION_WEIGHTS = {
    "rules_e1": 0.28,
    "rules_ext": 0.12,
    "crt": 0.12,
    "neural": 0.25,  # gated toward neutral if low conf / grade C
    "ml": 0.18,      # gated by ml_confidence; omit if absent
    "e2": 0.05,      # reverse mode only
}


def _ml_gate_factor(confidence: str | None) -> float:
    return {"high": 1.0, "medium": 0.75, "low": 0.45}.get(
        (confidence or "medium").lower(), 0.60,
    )


def _direction_penalty(data: dict) -> tuple[float, str]:
    """Return multiplier ≤1 and note when H1 conflicts with setup direction."""
    direction = data.get("setup", {}).get("direction", "NONE")
    bias = data.get("bias_h1", "NEUTRAL")
    conflict = (
        (direction == "LONG" and bias == "BEARISH")
        or (direction == "SHORT" and bias == "BULLISH")
    )
    if conflict:
        return 0.88, f"penalización H1 {bias} vs {direction}"
    return 1.0, ""


def compute_advanced_scorecard(
    data: dict,
    ctx: dict,
    categories: dict,
    crt: dict,
    e2: dict,
    setup_mode: str,
) -> tuple[float, list[tuple[str, str, str, str]]]:
    """Score combinado ponderado Rules+ML+Neural+CRT (pesos documentados).

    Pesos base (renormalizados si falta ML/Neural/E2):
      Rules E1 28% · Extendidas 12% · CRT 12% · Neural gated 25% · ML gated 18% · E2 5%
    Neural ausente → no relleno 50%; se redistribuye. Low conf → shrink a neutro.
    """
    from app.models.btc_signal_categories import _crt_coherent
    from app.models.btc_neural_signals import (
        gated_prob_toward_neutral,
        neural_gate_factor,
    )

    rules_pct = float(categories.get("rules_pct", 0) or 0)
    rules_ok = categories.get("rules_ok", 0)
    rules_total = categories.get("rules_total", 8)
    ext_pct = float(ctx.get("ext_pct", 0) or 0)
    nw = categories.get("neural_prob_win")
    ml = categories.get("ml_prob_win")
    crt_ok, crt_note = _crt_coherent(data, crt)

    rows: list[tuple[str, str, str, str]] = []
    scores: list[tuple[float, float]] = []
    used_keys: list[str] = []

    w = HIGH_FUSION_WEIGHTS
    rows.append(("Rules E1 (8)", f"{rules_ok}/{rules_total}", f"{int(w['rules_e1']*100)}%", f"{rules_pct:.0f}% OK"))
    scores.append((rules_pct, w["rules_e1"]))
    used_keys.append("rules_e1")

    rows.append(("Rules extendidas (10)", f"{ext_pct:.0f}%", f"{int(w['rules_ext']*100)}%", "meta >70%"))
    scores.append((ext_pct, w["rules_ext"]))
    used_keys.append("rules_ext")

    rows.append(("CRT coherence", "pass" if crt_ok else "fail", f"{int(w['crt']*100)}%", crt_note))
    scores.append((100.0 if crt_ok else 0.0, w["crt"]))
    used_keys.append("crt")

    if nw is not None:
        gate = float(
            categories.get("neural_gate_factor")
            or neural_gate_factor(
                categories.get("neural_confidence"),
                categories.get("neural_grade"),
            )
        )
        eff = float(
            categories.get("neural_effective_prob_win")
            or gated_prob_toward_neutral(float(nw), gate)
        )
        nw_pct = float(nw) * 100
        eff_pct = eff * 100
        conf = categories.get("neural_confidence", "?")
        align = "alineado WIN" if categories.get("neural_gallery_aligned") else "no alineado"
        note = f"{align}; conf={conf}; gate×{gate:.2f} → {eff_pct:.0f}%"
        rows.append(("Neural galería (gated)", f"{nw_pct:.1f}%", f"{int(w['neural']*100)}%", note))
        scores.append((eff_pct, w["neural"]))
        used_keys.append("neural")
    else:
        rows.append(("Neural galería", "n/d", "—", "omitido — sin chart/modelo (no pad 50%)"))

    if ml is not None:
        ml_gate = _ml_gate_factor(categories.get("ml_confidence"))
        ml_eff = gated_prob_toward_neutral(float(ml), ml_gate) * 100
        ml_pct = float(ml) * 100
        note = (
            f"grade {categories.get('ml_grade', '?')}; "
            f"conf={categories.get('ml_confidence', '?')}; → {ml_eff:.0f}%"
        )
        rows.append(("ML tabular (gated)", f"{ml_pct:.1f}%", f"{int(w['ml']*100)}%", note))
        scores.append((ml_eff, w["ml"]))
        used_keys.append("ml")
    else:
        rows.append(("ML tabular", "n/d", "—", "omitido — sin --ml o modelo"))

    show_e2 = setup_mode == "reverse" or e2.get("mode_setup") == "reverse"
    if show_e2:
        e2_score = e2.get("score", 0)
        e2_max = e2.get("max", 6)
        e2_pct = int(e2_score / e2_max * 100) if e2_max else 0
        rows.append(("E2 turtle", f"{e2_score}/{e2_max}", f"{int(w['e2']*100)}%", e2.get("verdict", "E2_NO")))
        scores.append((float(e2_pct), w["e2"]))
        used_keys.append("e2")

    total_w = sum(weight for _, weight in scores)
    combined = sum(s * weight for s, weight in scores) / total_w if total_w else 0.0

    dir_mult, dir_note = _direction_penalty(data)
    if dir_mult < 1.0:
        combined *= dir_mult
        rows.append(("Penalización dirección", f"×{dir_mult:.2f}", "—", dir_note))

    categories["fusion_score"] = round(combined, 1)
    categories["fusion_weights"] = {
        k: round(wt / total_w, 3)
        for k, (_, wt) in zip(used_keys, scores)
    } if total_w else {}

    rows.append(("**Score combinado**", f"**{combined:.0f}%**", "100%", "pesos renormalizados"))
    return combined, rows


def format_executive_synthesis(
    data: dict, ctx: dict, categories: dict, crt: dict, e2: dict, combined: float,
) -> list[str]:
    """A) Síntesis ejecutiva en español."""
    verdict = ctx["verdict"]
    bando_cli = categories.get("bando_usado", "AUTO")
    bando_mkt = categories.get("bando_mercado", data["bias_h1"])
    setup_mode = data.get("mode_setup", "auto")
    lines = [
        "## A) Síntesis ejecutiva",
        "",
    ]
    # Macro context (reloj opcional — no gate)
    ses = data["session"]
    pd_read = crt.get("pd_reading", "n/a")
    macro = (
        f"**Contexto macro:** Precio {data['price']:.0f} · "
        f"reloj {ses.get('window', 'n/d')} · "
        f"CRT PD={pd_read} · H1 bias **{data['bias_h1']}**"
    )
    lines.append(f"- {macro}")

    # Setup
    rec = categories.get("recomendacion", verdict)
    dir_u = data["setup"]["direction"]
    setup_txt = (
        f"**Setup:** {rec} · dirección **{dir_u}** · "
        f"modo **{setup_mode.upper()}** · reglas E1 {categories['rules_ok']}/"
        f"{categories['rules_total']} ({categories['rules_pct']}%)"
    )
    lines.append(f"- {setup_txt}")

    # CLI vs H1 conflict
    if bando_cli != "AUTO" and bando_cli != bando_mkt:
        lines.append(
            f"- **Conflicto bando:** CLI **{bando_cli}** vs mercado H1 **{bando_mkt}** — "
            "confirmar en TradingView antes de ejecutar"
        )
    elif bando_cli == "AUTO":
        lines.append(f"- **Bando:** AUTO — mercado H1 **{bando_mkt}** guía dirección")
    else:
        lines.append(f"- **Bando:** CLI y H1 alineados (**{bando_cli}**)")

    # Integrated verdict
    if combined >= 75 and verdict == "ENTRAR":
        vtxt = f"**Veredicto integrado:** ENTRAR candidato A+ (score combinado {combined:.0f}%)"
    elif combined >= 63:
        vtxt = f"**Veredicto integrado:** ESPERAR — score {combined:.0f}% requiere confirmación TV"
    else:
        vtxt = f"**Veredicto integrado:** {verdict} — score combinado {combined:.0f}%"
    lines.append(f"- {vtxt}")

    if setup_mode == "reverse":
        wr = e2.get("winrate", "~61%")
        lines.append(
            f"- **E2 contexto:** {e2.get('verdict', 'E2_NO')} "
            f"({e2.get('score', 0)}/{e2.get('max', 6)}) · "
            f"operable={'SÍ' if e2.get('eligible') else 'NO'} · WR {wr}"
        )

    lines += ["", "---", ""]
    return lines


def format_scorecard_table(rows: list[tuple[str, str, str, str]]) -> list[str]:
    """B) Multi-layer scorecard."""
    lines = [
        "## B) Scorecard multicapa",
        "",
        "| Capa | Score | Peso | Nota |",
        "|------|-------|------|------|",
    ]
    for capa, score, peso, nota in rows:
        lines.append(f"| {capa} | {score} | {peso} | {nota} |")
    lines += ["", "---", ""]
    return lines


def format_crt_deep_dive(data: dict, crt: dict, h1_lines: list[str]) -> list[str]:
    """C) CRT deep dive expandido."""
    price = data["price"]
    pdh, pdl = data.get("pdh"), data.get("pdl")
    dist = _pdh_pdl_distances(price, pdh, pdl)
    mid = crt.get("midpoint")
    pd_zone = crt.get("premium_discount", "n/a")

    lines = [
        "## C) CRT deep dive",
        "",
        "### Distancias PDH/PDL",
        "",
    ]
    if pdh:
        lines.append(
            f"- **PDH** {pdh:.0f}: {dist['pdh_pts']:+.1f} pts ({dist['pdh_pct']:+.3f}%)"
        )
    if pdl:
        lines.append(
            f"- **PDL** {pdl:.0f}: {dist['pdl_pts']:+.1f} pts ({dist['pdl_pct']:+.3f}%)"
        )

    lines += [
        "",
        "### Premium / Discount 0.5",
        "",
        f"- Midpoint 0.5: **{mid:.0f}**" if mid else "- Midpoint: n/d",
        f"- Posición precio: **{pd_zone}** (precio {price:.0f})",
        f"- Lectura PD: **{crt.get('pd_reading', 'n/a')}**",
        "",
        "### Fakeout — análisis paso a paso",
        "",
    ]
    if crt.get("fakeout_pdh"):
        lines += [
            "1. Wick M5 superó PDH en últimas ~18 velas",
            "2. Precio actual **por debajo** de PDH → trampa alcista",
            "3. **Acción:** NO long E1 · CRT invalid bearish · posible short en reclaim",
        ]
    elif crt.get("fakeout_pdl"):
        lines += [
            "1. Wick M5 barrió PDL en últimas ~18 velas",
            "2. Precio actual **por encima** de PDL → turtle soup context",
            "3. **Acción:** NO chase E1 long · contexto E2 si reclaim confirmado",
        ]
    else:
        lines.append("- Sin fakeout PDH/PDL detectado en ventana M5 reciente")

    lines += [
        "",
        "### Timeline H1 (últimas 3 velas)",
        "",
    ]
    for row in h1_lines:
        lines.append(f"- `{row}`")
    lines += [
        "",
        f"- Estado CRT H1: **{crt.get('h1_state', 'n/a')}** — {crt.get('h1_detail', '')}",
        "",
        "### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)",
        "",
        "| Lectura CRT | Acción E1 | Estado actual |",
        "|-------------|-----------|---------------|",
    ]
    pd_read = crt.get("pd_reading", "n/a")
    matrix = [
        ("Dentro PDH/PDL", "NEUTRAL — no forzar", pd_read == "NEUTRAL"),
        ("Cierre > PDH", "Sesgo alcista — long pullback", pd_read == "BULLISH"),
        ("Cierre < PDL", "Sesgo bajista — short rechazo", pd_read == "BEARISH"),
        ("Fakeout PDH", "NO long E1", crt.get("fakeout_pdh", False)),
        ("Fakeout PDL", "Contexto E2 turtle soup", crt.get("fakeout_pdl", False)),
    ]
    for lectura, accion, active in matrix:
        mark = "**→**" if active else ""
        lines.append(f"| {lectura} | {accion} | {mark} |")
    lines += ["", "---", ""]
    return lines


def format_e2_expanded(e2: dict, crt: dict, setup_mode: str) -> list[str]:
    """D) E2 Turtle Soup expandido."""
    if setup_mode != "reverse" and e2.get("mode_setup") != "reverse":
        return []
    lines = [
        "## D) E2 Turtle Soup expandido",
        "",
        "| # | Check | OK | Evidencia |",
        "|---|-------|----|-----------|",
    ]
    for label, ok, detail in e2.get("checks", []):
        lines.append(f"| {label} | {'✅' if ok else '❌'} | {'SÍ' if ok else 'NO'} | {detail} |")
    lines += [
        "",
        f"**Score:** {e2.get('score', 0)}/{e2.get('max', 6)} · "
        f"Veredicto: **{e2.get('verdict', 'E2_NO')}**",
        "",
        "### Interpretación fakeout PDL/PDH",
        "",
    ]
    if crt.get("fakeout_pdl"):
        lines.append(
            "- **Fakeout PDL:** barrido de liquidez bajo mínimo ayer + reclaim → "
            "watchlist turtle soup LONG (solo demo, SL grande)"
        )
    if crt.get("fakeout_pdh"):
        lines.append(
            "- **Fakeout PDH:** sweep sobre máximo ayer sin hold → "
            "watchlist turtle soup SHORT (solo demo)"
        )
    if not crt.get("fakeout_pdl") and not crt.get("fakeout_pdh"):
        lines.append("- Sin fakeout macro activo — E2 requiere sweep+reclaim explícito")

    verdict = e2.get("verdict", "E2_NO")
    wr = e2.get("winrate")
    wr_txt = f" · WR {wr}" if wr else ""
    if e2.get("eligible"):
        action = f"**OPERABLE** — 2 velas alineadas al bando{wr_txt}"
    elif verdict in ("E2_WATCH", "E2_READY"):
        action = f"**Observar** — falta confirmación 2 velas o checklist incompleto{wr_txt}"
    else:
        action = f"**NO ENTRAR** — setup Reverse incompleto{wr_txt}"
    lines += ["", f"### Decisión E2: {action}", "", "---", ""]
    return lines


def format_ml_neural_cross(categories: dict) -> list[str]:
    """E) Neural cross-analysis (ML oculto en Categories; gated en scorecard)."""
    agreement, explanation = _ml_neural_agreement(categories)
    lines = [
        "## E) Cruce Neural + Rules",
        "",
        f"**Acuerdo Rules/Neural:** {agreement}",
        "",
        f"- {explanation}",
        "",
    ]
    if "neural_prob_win" in categories:
        nw = categories["neural_prob_win"] * 100
        gate = categories.get("neural_gate_factor")
        eff = categories.get("neural_effective_prob_win")
        gate_txt = ""
        if gate is not None and eff is not None:
            gate_txt = f" · gate×{float(gate):.2f} → {float(eff)*100:.0f}% efectivo"
        lines += [
            f"- **Neural galería:** {nw:.1f}% WIN "
            f"(grade {categories.get('neural_grade', '?')}, "
            f"conf {categories.get('neural_confidence', '?')})"
            f"{gate_txt}",
        ]
    lines += ["", "---", ""]
    return lines


def format_gallery_advanced(
    patterns: list[str], categories: dict,
) -> list[str]:
    """F) Galería WIN/LOSS — top 3 con tags."""
    lines = [
        "## F) Galería WIN/LOSS match",
        "",
        "| # | Patrón | Archivo | Similitud | Tags |",
        "|---|--------|---------|-----------|------|",
    ]
    nw = categories.get("neural_prob_win")
    base_sim = nw * 100 if nw is not None else None
    top = patterns[:3] if patterns else ["Sin patrón similar en historial"]
    for i, pat in enumerate(top, 1):
        fname = _extract_btc_filename(pat) or "—"
        if base_sim is not None:
            sim = f"{max(base_sim - (i - 1) * 5, 40):.0f}%"
        else:
            sim = "heurística"
        tags = _pattern_tags(pat)
        lines.append(f"| {i} | {pat[:60]} | {fname} | {sim} | {tags} |")
    lines += [
        "",
        "- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1",
        "",
        "---",
        "",
    ]
    return lines


def format_trading_plan_advanced(data: dict, ctx: dict, combined: float) -> list[str]:
    """G) Plan de trading si candidato ENTRAR."""
    verdict = ctx["verdict"]
    if verdict != "ENTRAR" and combined < 70:
        return []
    s = data["setup"]
    direction = s["direction"]
    if direction == "NONE":
        return []
    zone = data["zone"]
    lines = [
        "## G) Plan de trading",
        "",
        f"- **Entrada:** {direction} @ zona {zone.get('type', 'n/d')} "
        f"{zone.get('level', 0):.0f} (precio actual {data['price']:.0f})",
    ]
    if s.get("sl") and s.get("tp"):
        lines += [
            f"- **SL estructural:** {s['sl']:.0f} | **SL cuenta:** ~$9 (ajustar lotaje)",
            f"- **TP 1:2:** {s['tp']:.0f} | **BE:** mover a BE en 1:1",
        ]
    checks = [
        ("Bias H1 alineado", data["bias_h1"] in ("BULLISH", "BEARISH")),
        ("Zona ≤0.15%", zone.get("dist_pct") is not None and zone["dist_pct"] <= 0.15),
        ("2 velas M5 confirmación", data["confirm_long"] if direction == "LONG" else data["confirm_short"]),
        ("Rules E1 ≥63%", ctx["categories"]["rules_pct"] >= 63),
        ("Extendidas ≥70%", ctx["ext_pct"] >= 70),
        ("Sin fakeout contra", not any("fakeout" in f.lower() for f in ctx["flags"][:3])),
        ("SL ~$9 definido", s.get("sl") is not None),
        ("R:R 1:2", s.get("rr") is not None),
    ]
    lines += [
        "- **Invalidación:** cierre M5 fuera zona / CRT invalid / fakeout contra dirección",
        "- **Confluencias Notion sugeridas:** Continuación/Breakout E1, Zona débil morada, "
        "CRT alineado",
        "",
        "### Pre-trade checklist (8 ítems)",
        "",
        "| # | Ítem | OK |",
        "|---|------|----|",
    ]
    for i, (label, ok) in enumerate(checks, 1):
        lines.append(f"| {i} | {label} | {'✅' if ok else '❌'} |")
    lines += ["", "---", ""]
    return lines


def format_psychology_guards(data: dict, categories: dict, combined: float) -> list[str]:
    """H) Psicología y guardas de riesgo (sesión NY no es gate)."""
    flags = []
    flags.append("❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)")
    ml = categories.get("ml_prob_win")
    nw = categories.get("neural_prob_win")
    if nw and nw >= 0.70 and categories.get("rules_pct", 0) < 63:
        flags.append("⚠ FOMO risk: Neural alto pero Rules <63% — no forzar entrada")
    if ml and ml < 0.45 and nw and nw > 0.70:
        flags.append("⚠ Tensión ML/Neural — no entrar por galería sola")

    lines = [
        "## H) Psicología y guardas",
        "",
    ]
    for f in flags:
        lines.append(f"- {f}")
    lines += [
        "",
        "> **Frase guía:** \"Si no es A+ con CRT + 2 velas M5, es ESPERAR — "
        "el mercado mañana sigue ahí.\" (TRADING_VISUAL §7)",
        "",
        "---",
        "",
    ]
    return lines


def _high_asset_refs(asset: str | None = None) -> dict[str, str]:
    """Protocolo + live MD según asset (BTC / US30)."""
    label = (asset or "BTC").upper()
    if label == "US30":
        return {
            "label": "US30",
            "protocol": "docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md",
            "live": "live/us30_m5_high_signal.md",
        }
    return {
        "label": "BTC",
        "protocol": "docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md",
        "live": "live/btc_m5_high_signal.md",
    }


def format_cursor_advanced_block(asset: str | None = None) -> list[str]:
    """I) Bloque prompt Cursor ADVANCED en live file."""
    refs = _high_asset_refs(asset)
    return [
        "## I) Cursor — prompt ADVANCED",
        "",
        f"Usar con `@{refs['protocol']}` sección **Modo Advanced**.",
        "",
        "```",
        f"Análisis E1 CRT ADVANCED — {refs['label']} M5 HIGH mode.",
        f"Lee TODAS las secciones A–H de {refs['live']}.",
        "NO acortar. Responde estructurado en español con síntesis ejecutiva,",
        "scorecard, CRT deep dive, E2 (si aplica), cruce ML×Neural, galería,",
        "plan (si ENTRAR), red flags y guardas psicológicas.",
        "Confirmar TradingView antes de ejecutar. 2 SL = límite de riesgo diario.",
        "```",
        "",
    ]


def format_advanced_sections(
    data: dict,
    ctx: dict,
    crt: dict,
    e2: dict,
    pats: list[str],
    h1_lines: list[str],
) -> list[str]:
    """Todas las secciones A–I del modo advanced."""
    categories = ctx["categories"]
    setup_mode = data.get("mode_setup", "auto")
    combined, score_rows = compute_advanced_scorecard(
        data, ctx, categories, crt, e2, setup_mode,
    )
    lines: list[str] = [
        "",
        "---",
        "",
        "> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)",
        "",
    ]
    lines += format_executive_synthesis(data, ctx, categories, crt, e2, combined)
    lines += format_scorecard_table(score_rows)
    lines += format_crt_deep_dive(data, crt, h1_lines)
    lines += format_e2_expanded(e2, crt, setup_mode)
    lines += format_ml_neural_cross(categories)
    lines += format_gallery_advanced(pats, categories)
    lines += format_trading_plan_advanced(data, ctx, combined)
    lines += format_psychology_guards(data, categories, combined)
    lines += format_cursor_advanced_block(data.get("asset_label"))
    return lines


def last_h1_range(h1: list[dict]) -> dict | None:
    if len(h1) < 2:
        return None
    c = h1[-2]
    return {
        "high": c["high"], "low": c["low"], "open": c["open"], "close": c["close"],
        "time": c["open_time"].strftime("%Y-%m-%d %H:%M"),
    }


def rsi_at(closes: list[float], period: int = 14) -> float | None:
    if len(closes) < period + 1:
        return None
    gains, losses = [], []
    for i in range(-period, 0):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    avg_g = sum(gains) / period
    avg_l = sum(losses) / period
    if avg_l == 0:
        return 100.0
    return 100.0 - (100.0 / (1.0 + (avg_g / avg_l)))


def rsi_series(closes: list[float], period: int = 14) -> list[float | None]:
    out: list[float | None] = [None] * len(closes)
    for i in range(period, len(closes) + 1):
        out[i - 1] = rsi_at(closes[:i], period)
    return out


def analyze_crt(price: float, pdh: float | None, pdl: float | None,
                h1: list[dict], m5: list[dict]) -> dict:
    out: dict = {
        "pd_reading": "n/a", "midpoint": None, "premium_discount": "n/a",
        "h1_state": "n/a", "h1_detail": "", "fakeout_pdh": False, "fakeout_pdl": False,
        "fakeout_note": "", "crt_action_e1": "",
    }
    if pdh and pdl:
        mid = (pdh + pdl) / 2
        out["midpoint"] = mid
        if pdl < price < pdh:
            out["pd_reading"] = "NEUTRAL"
            out["crt_action_e1"] = "No forzar; esperar pending CRT HTF"
        elif price > pdh:
            out["pd_reading"] = "BULLISH"
            out["crt_action_e1"] = "Longs E1 pullback soporte debil (discount)"
        else:
            out["pd_reading"] = "BEARISH"
            out["crt_action_e1"] = "Shorts E1 rechazo resistencia (premium)"
        out["premium_discount"] = (
            "DISCOUNT" if price <= mid else "PREMIUM" if price >= mid else "EQUILIBRIO 0.5"
        )

    recent = m5[-18:]
    if pdh and any(c["high"] > pdh for c in recent) and price < pdh:
        out["fakeout_pdh"] = True
        out["fakeout_note"] = "Fakeout PDH: NO long E1; CRT invalid bearish"
    if pdl and any(c["low"] < pdl for c in recent) and price > pdl:
        out["fakeout_pdl"] = True
        extra = "Fakeout PDL: turtle soup E2 watch"
        out["fakeout_note"] = extra if not out["fakeout_note"] else out["fakeout_note"] + " | " + extra

    hr = last_h1_range(h1)
    if hr:
        rng = hr["high"] - hr["low"]
        eq = hr["low"] + rng / 2
        if price >= hr["high"]:
            out["h1_state"] = "COMPLETED_BULL"
            out["h1_detail"] = f"High H1 {hr['high']:.0f} alcanzado"
        elif price <= hr["low"]:
            out["h1_state"] = "COMPLETED_BEAR"
            out["h1_detail"] = f"Low H1 {hr['low']:.0f} alcanzado"
        elif any(c["high"] > hr["high"] for c in m5[-6:]) and price < hr["high"]:
            out["h1_state"] = "PENDING_BEAR"
            out["h1_detail"] = "Sweep high H1 sin hold"
        elif any(c["low"] < hr["low"] for c in m5[-6:]) and price > hr["low"]:
            out["h1_state"] = "PENDING_BULL"
            out["h1_detail"] = "Sweep low H1 + reclaim"
        else:
            out["h1_state"] = "INSIDE_RANGE"
            out["h1_detail"] = f"Rango H1 {hr['low']:.0f}-{hr['high']:.0f}; 0.5={eq:.0f}"
    return out


def detect_rsi_divergence(m5: list[dict]) -> dict:
    closes = [c["close"] for c in m5]
    lows = [c["low"] for c in m5]
    highs = [c["high"] for c in m5]
    rs = rsi_series(closes, 14)
    w = 20
    if len(m5) < w:
        return {"type": "NONE", "note": "Datos insuficientes TORYS-proxy"}
    i1, i2 = len(m5) - w, len(m5) - 1
    if lows[i2] < lows[i1] and rs[i2] and rs[i1] and rs[i2] > rs[i1]:
        return {"type": "BULLISH", "note": "Fondo verde TORYS-proxy - filtro long"}
    if highs[i2] > highs[i1] and rs[i2] and rs[i1] and rs[i2] < rs[i1]:
        return {"type": "BEARISH", "note": "Fondo rojo TORYS-proxy - filtro short"}
    return {"type": "NONE", "note": "Sin divergencia M5 clara"}


def dmi_proxy(closes: list[float]) -> dict:
    if len(closes) < 20:
        return {"bias": "NEUTRAL", "note": "n/a"}
    up = sum(max(closes[i] - closes[i - 1], 0) for i in range(-14, 0))
    down = sum(max(closes[i - 1] - closes[i], 0) for i in range(-14, 0))
    if up > down * 1.15:
        return {"bias": "BULL", "note": f"+DI domina ({up:.0f}/{down:.0f})"}
    if down > up * 1.15:
        return {"bias": "BEAR", "note": f"-DI domina ({down:.0f}/{up:.0f})"}
    return {"bias": "NEUTRAL", "note": "Momentum mixto"}


def structure_notes(sh: list[float], sl: list[float]) -> dict:
    hl = lh = "n/a"
    if len(sl) >= 2:
        hl = f"HL {sl[-2]:.0f}->{sl[-1]:.0f}" if sl[-1] > sl[-2] else f"LL {sl[-2]:.0f}->{sl[-1]:.0f}"
    if len(sh) >= 2:
        lh = f"HH {sh[-2]:.0f}->{sh[-1]:.0f}" if sh[-1] > sh[-2] else f"LH {sh[-2]:.0f}->{sh[-1]:.0f}"
    return {"hl": hl, "lh": lh}


def analyze_turtle_soup_e2(price: float, m5: list[dict], crt: dict,
                           swing_l: list[float], div: dict) -> dict:
    checks = [
        ("1. Reversion MACRO", False, "Barrido pool/PDL-PDH"),
        ("2. Rompe min/max previo", False, "Sweep liquidez"),
        ("3. Reclaim agresivo", False, "Cierre M5 reclaim"),
        ("4. Entrada zona SL original", False, "Cerca nivel barrido"),
        ("5. SL grande E2", False, "No SL $9 E1"),
        ("6. Max 1/sem NO eval", False, "Confirmar bitacora"),
    ]
    swept = False
    if swing_l and min(c["low"] for c in m5[-8:]) < swing_l[-1] and price > swing_l[-1]:
        checks[1] = (checks[1][0], True, "Sweep swing low + reclaim")
        checks[2] = (checks[2][0], True, "Reclaim M5")
        swept = True
    if crt.get("fakeout_pdl"):
        checks[0] = (checks[0][0], True, "Fakeout PDL macro")
        checks[1] = (checks[1][0], True, "PDL barrido")
        checks[2] = (checks[2][0], True, "Reclaim post PDL")
        swept = True
    if swing_l and abs(price - swing_l[-1]) / price * 100 <= 0.2:
        if div["type"] == "BULLISH" or crt.get("fakeout_pdl"):
            checks[3] = (checks[3][0], True, "Cerca pool post sweep")
    score = sum(1 for c in checks if c[1])
    return {
        "checks": checks, "score": score, "max": 6,
        "eligible": score >= 4 and swept,
        "verdict": "E2_WATCH" if score >= 3 else "E2_NO",
        "note": "E2 max 10%; PF E1=4.77; PROHIBIDO eval (TRADING_VISUAL SS7)",
    }


def match_gallery_pattern(data: dict, crt: dict) -> list[str]:
    s = data["setup"]
    pats = []
    if data["confirm_long"] and "PENDING_BULL" in crt.get("h1_state", ""):
        pats.append("WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26)")
    if s["direction"] == "SHORT" and data["zone"].get("type") == "resistencia_debil":
        pats.append("WIN: Rechazo resistencia (BTC-02-07-26)")
    if crt.get("fakeout_pdh"):
        pats.append("LOSS: fakeout (BTC-22-05-26)")
    if data["bias_h1"] == "BEARISH" and s["direction"] == "LONG":
        pats.append("LOSS: contra bias (BTC-01-06-26)")
    return pats or ["Esperar setup A+ galeria WIN"]


def score_rules_pct(data: dict, crt: dict, div: dict, dmi: dict, e2: dict) -> tuple[int, list]:
    """Score extendido HIGH — delega a btc_e1_report."""
    from app.views.btc_e1_report import score_extended_rules
    pct, _, items = score_extended_rules(data, crt, div, dmi, e2)
    return pct, items


def _candle_color(c: dict) -> str:
    return "G" if c["close"] >= c["open"] else "R"


def _last_n_colors(m5: list[dict], n: int) -> list[str]:
    if len(m5) < n:
        return []
    return [_candle_color(c) for c in m5[-n:]]


def _candles_in_zone(m5: list[dict], zone: dict) -> bool:
    """True if last 2 M5 closes are within 0.15% of zone level."""
    level = zone.get("level")
    if not level or len(m5) < 2:
        return False
    for c in m5[-2:]:
        if abs(c["close"] - level) / c["close"] * 100 > 0.15:
            return False
    return True


def parse_entry_price(raw: str | float | int | None) -> float | None:
    """Parse CLI `--entry` / `-Entry` into a float price.

    Accepts plain (`53128`, `53128.0`), European thousands (`53.128`),
    comma decimals (`53128,5` / `53.128,50`), and multi-dot European
    thousands as typed on US30 (`53.12.800` → `53128.0`).
    """
    if raw is None:
        return None
    if isinstance(raw, bool):
        raise ValueError("entry price cannot be boolean")
    if isinstance(raw, (int, float)):
        return float(raw)

    s = str(raw).strip().replace(" ", "").replace("'", "").replace("\u00a0", "")
    if not s:
        return None

    # European decimal comma: 53.128,50 or 53128,5
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
        return float(s)

    # Multi-dot European thousands (e.g. 53.12.800 → 53128.0)
    if s.count(".") >= 2:
        parts = s.split(".")
        if not parts or not all(p.isdigit() for p in parts):
            raise ValueError(f"invalid multi-dot entry price: {raw!r}")
        joined = "".join(parts)
        # Last 3-digit group often carries implied ,00 (53.12.800 → 5312800 → 53128.00)
        if len(parts) >= 3 and len(parts[-1]) == 3:
            return float(joined) / 100.0
        return float(joined)

    # Single dot: thousands (53.128) vs decimal (53128.0 / 97450.5)
    if s.count(".") == 1:
        left, right = s.split(".")
        if left.isdigit() and right.isdigit():
            if len(right) == 3 and 1 <= len(left) <= 3:
                return float(left + right)
            return float(s)
        raise ValueError(f"invalid entry price: {raw!r}")

    return float(s)


# Past-structure SL/TP: keep risk within [min, max] of entry (pct)
_PAST_SL_MIN_RISK_PCT = 0.05
_PAST_SL_MAX_RISK_PCT = 2.0
_PAST_STRUCT_TP_MIN_RR = 1.5


def find_m5_index_at_user_entry(m5: list[dict], entry: float) -> int | None:
    """Index of last M5 bar that touched `entry`, or closest approach if never touched.

    Used to ignore candles strictly before the user's fill for past structure.
    """
    if not m5:
        return None
    entry = float(entry)
    last_touch: int | None = None
    for i, c in enumerate(m5):
        lo = float(c["low"])
        hi = float(c["high"])
        if lo <= entry <= hi:
            last_touch = i
    if last_touch is not None:
        return last_touch

    best_i = 0
    best_d = float("inf")
    for i, c in enumerate(m5):
        lo = float(c["low"])
        hi = float(c["high"])
        if entry < lo:
            d = lo - entry
        elif entry > hi:
            d = entry - hi
        else:
            d = 0.0
        if d < best_d or (abs(d - best_d) < 1e-12 and i >= best_i):
            best_d = d
            best_i = i
    return best_i


def filter_m5_from_entry_touch(m5: list[dict], entry: float) -> list[dict]:
    """Return a copy of M5 from the entry-touch (or approach) bar forward inclusive."""
    if not m5:
        return []
    idx = find_m5_index_at_user_entry(m5, entry)
    if idx is None:
        return list(m5)
    return list(m5[idx:])


def data_with_m5_from_entry(data: dict, entry: float) -> dict:
    """Shallow copy of `data` with `m5` filtered to ignore pre-entry candles."""
    out = copy.copy(data)
    m5 = data.get("m5") or []
    idx = find_m5_index_at_user_entry(m5, entry) if m5 else None
    filtered = filter_m5_from_entry_touch(m5, entry) if m5 else []
    out["m5"] = filtered
    out["m5_pre_entry_ignored"] = True
    out["m5_entry_touch_index"] = idx
    out["m5_from_entry_len"] = len(filtered)
    return out


def _past_structure_levels(
    data: dict,
    zone: dict | None,
    crt: dict | None,
) -> tuple[list[tuple[float, str]], list[tuple[float, str]]]:
    """Collect (level, label) supports below / resistances above from past data."""
    supports: list[tuple[float, str]] = []
    resistances: list[tuple[float, str]] = []

    for lvl in data.get("swing_lows") or []:
        supports.append((float(lvl), "swing_low M5"))
    for lvl in data.get("swing_highs") or []:
        resistances.append((float(lvl), "swing_high M5"))

    z = zone or data.get("zone") or {}
    zlvl = z.get("level")
    ztype = z.get("type") or ""
    if zlvl is not None:
        if ztype == "soporte_debil":
            supports.append((float(zlvl), "soporte_debil"))
        elif ztype == "resistencia_debil":
            resistances.append((float(zlvl), "resistencia_debil"))

    pdl = data.get("pdl")
    pdh = data.get("pdh")
    if pdl is not None:
        supports.append((float(pdl), "PDL"))
    if pdh is not None:
        resistances.append((float(pdh), "PDH"))

    # Recent M5 extremes as soft structure (around entry conceptually)
    m5 = data.get("m5") or []
    if len(m5) >= 1:
        window = m5[-24:]
        supports.append((min(c["low"] for c in window), "M5 low reciente"))
        resistances.append((max(c["high"] for c in window), "M5 high reciente"))

    # Optional H1 extremes if present on data
    h1 = data.get("h1") or []
    if len(h1) >= 3:
        window_h1 = h1[-12:]
        supports.append((min(c["low"] for c in window_h1), "H1 low reciente"))
        resistances.append((max(c["high"] for c in window_h1), "H1 high reciente"))

    _ = crt  # CRT PDH/PDL already via data; reserved for future fakeout-aware picks
    return supports, resistances


def _pick_past_sl(
    entry: float,
    direction: str,
    supports: list[tuple[float, str]],
    resistances: list[tuple[float, str]],
) -> tuple[float, str, float] | None:
    """Return (sl, label, raw_level) beyond nearest safe past structure, or None."""
    min_risk = entry * (_PAST_SL_MIN_RISK_PCT / 100.0)
    max_risk = entry * (_PAST_SL_MAX_RISK_PCT / 100.0)

    if direction == "LONG":
        # Protective side: below entry — prefer closest structure that yields sane risk
        cands = []
        for lvl, label in supports:
            if lvl >= entry:
                continue
            # Buffer beyond swing / S/R (match zone multipliers)
            buf = 0.998 if "debil" in label else 0.997
            sl = float(lvl) * buf
            if sl >= entry:
                continue
            risk = entry - sl
            if min_risk <= risk <= max_risk:
                cands.append((risk, sl, label, float(lvl)))
        if not cands:
            return None
        # Closest structural stop (smallest risk among valid)
        _, sl, label, raw = min(cands, key=lambda x: x[0])
        return sl, label, raw

    if direction == "SHORT":
        cands = []
        for lvl, label in resistances:
            if lvl <= entry:
                continue
            buf = 1.002 if "debil" in label else 1.003
            sl = float(lvl) * buf
            if sl <= entry:
                continue
            risk = sl - entry
            if min_risk <= risk <= max_risk:
                cands.append((risk, sl, label, float(lvl)))
        if not cands:
            return None
        _, sl, label, raw = min(cands, key=lambda x: x[0])
        return sl, label, raw

    return None


def _pick_past_tp(
    entry: float,
    direction: str,
    risk: float,
    supports: list[tuple[float, str]],
    resistances: list[tuple[float, str]],
) -> tuple[float, float, str, bool]:
    """Return (tp, rr, label, used_structure). Prefer opposing S/R if RR ≥ 1.5."""
    min_rr = _PAST_STRUCT_TP_MIN_RR
    fallback_rr = 2.0

    if direction == "LONG":
        struct_cands = []
        for lvl, label in resistances:
            if lvl <= entry:
                continue
            reward = lvl - entry
            rr = reward / risk if risk > 0 else 0.0
            if rr >= min_rr:
                # Prefer nearest opposing structure with acceptable RR (not runaway)
                struct_cands.append((rr, float(lvl), label))
        if struct_cands:
            # Prefer RR closest to 2.0 among ≥1.5, then nearer target
            rr, tp, label = min(struct_cands, key=lambda x: (abs(x[0] - 2.0), x[1] - entry))
            return tp, rr, label, True
        tp = entry + fallback_rr * risk
        return tp, fallback_rr, "1:2 desde SL estructural", False

    # SHORT
    struct_cands = []
    for lvl, label in supports:
        if lvl >= entry:
            continue
        reward = entry - lvl
        rr = reward / risk if risk > 0 else 0.0
        if rr >= min_rr:
            struct_cands.append((rr, float(lvl), label))
    if struct_cands:
        rr, tp, label = min(struct_cands, key=lambda x: (abs(x[0] - 2.0), entry - x[1]))
        return tp, rr, label, True
    tp = entry - fallback_rr * risk
    return tp, fallback_rr, "1:2 desde SL estructural", False


def optimize_sl_tp_from_past(
    data: dict,
    entry: float,
    direction: str,
    crt: dict | None = None,
    zone: dict | None = None,
) -> dict | None:
    """Optimal SL/TP from past M5/H1 structure around a manual entry.

    - SL: beyond nearest swing / weak S/R / PDH-PDL (structural, not arbitrary %).
    - TP: opposing structure if R:R ≥ 1.5, else 1:2 from structural SL.

    Returns None when structure cannot be resolved safely (caller falls back to 1:2).
    """
    if direction not in ("LONG", "SHORT"):
        return None
    entry = float(entry)
    if entry <= 0:
        return None

    supports, resistances = _past_structure_levels(data, zone, crt)
    picked = _pick_past_sl(entry, direction, supports, resistances)
    if picked is None:
        return None

    sl, sl_label, raw_level = picked
    risk = abs(sl - entry)
    if risk <= 0:
        return None

    tp, rr, tp_label, tp_structural = _pick_past_tp(
        entry, direction, risk, supports, resistances,
    )

    # Final side sanity
    if direction == "LONG" and not (sl < entry < tp):
        return None
    if direction == "SHORT" and not (tp < entry < sl):
        return None

    return {
        "sl": sl,
        "tp": tp,
        "rr": float(rr),
        "risk_pts": risk,
        "sl_source": "past",
        "tp_source": "past_structure" if tp_structural else "past_1to2",
        "sl_label": sl_label,
        "tp_label": tp_label,
        "sl_raw_level": raw_level,
        "sl_tp_source": "past",
        "sl_tp_note": (
            f"SL/TP desde estructura pasada "
            f"(SL={sl_label} @ {raw_level:.1f}; TP={tp_label})"
        ),
    }


def _apply_entry_override_naive_rr(
    out: dict,
    entry: float,
    direction: str,
    zone: dict,
    data: dict,
    *,
    fallback_note: str | None = None,
) -> dict:
    """Legacy 1:2 from entry/zone when past structure is unavailable."""
    dec = int(out.get("dec", data.get("price_decimals", 1)))
    fmt = f".{dec}f"
    level = zone.get("level") if zone else out.get("level")
    ztype = (zone.get("type") if zone else None) or out.get("ztype") or "zona"
    rr = 2.0
    note = fallback_note or "SL/TP 1:2 (fallback; sin estructura pasada segura)"

    if direction == "SHORT":
        if level:
            sl = level * 1.002 if ztype == "resistencia_debil" else level * 1.003
        elif out.get("sl") is not None:
            sl = float(out["sl"])
        else:
            sl = entry * 1.003
        if sl <= entry:
            sl = entry * 1.003
        risk = abs(sl - entry)
        if risk <= 0:
            risk = max(entry * 0.003, 10 ** (-dec))
            sl = entry + risk
        tp = entry - rr * risk
        out.update({
            "valid": True,
            "sl": sl,
            "tp": tp,
            "rr": rr,
            "risk_pts": risk,
            "sl_source": "fallback_1to2",
            "tp_source": "fallback_1to2",
            "sl_tp_source": "fallback",
            "sl_tp_note": note,
            "opti_action": f"ENTRAR {direction} (Entry usuario)",
            "invalidacion": (
                f"Cierre M5 > {sl:{fmt}} o breakout sin rechazo "
                f"(Entry usuario {entry:{fmt}})"
            ),
            "trigger": f"Entry usuario CLI @ {entry:{fmt}} (SHORT)",
        })
    elif direction == "LONG":
        if level:
            sl = level * 0.998 if ztype == "soporte_debil" else level * 0.997
        elif out.get("sl") is not None:
            sl = float(out["sl"])
        else:
            sl = entry * 0.997
        if sl >= entry:
            sl = entry * 0.997
        risk = abs(entry - sl)
        if risk <= 0:
            risk = max(entry * 0.003, 10 ** (-dec))
            sl = entry - risk
        tp = entry + rr * risk
        out.update({
            "valid": True,
            "sl": sl,
            "tp": tp,
            "rr": rr,
            "risk_pts": risk,
            "sl_source": "fallback_1to2",
            "tp_source": "fallback_1to2",
            "sl_tp_source": "fallback",
            "sl_tp_note": note,
            "opti_action": f"ENTRAR {direction} (Entry usuario)",
            "invalidacion": (
                f"Cierre M5 < {sl:{fmt}} o breakdown sin reclaim "
                f"(Entry usuario {entry:{fmt}})"
            ),
            "trigger": f"Entry usuario CLI @ {entry:{fmt}} (LONG)",
        })
    else:
        out["valid"] = True
        out["opti_action"] = "ESPERAR (Entry usuario sin dirección)"
        out["trigger"] = f"Entry usuario CLI @ {entry:{fmt}}"
        out["sl_tp_source"] = "n/a"
        out["sl_tp_note"] = "Sin dirección — no SL/TP"

    return out


def _apply_entry_override(
    opt: dict,
    entry: float,
    direction: str,
    zone: dict,
    data: dict,
) -> dict:
    """Attach CLI `-Entry` as user fill; keep system Entrada óptima; SL/TP from post-entry past."""
    out = dict(opt)
    user_entry = float(entry)
    # Keep system optimal in out["entry"]; user fill is separate
    out["user_entry"] = user_entry
    out["entry_manual"] = True
    out["entry_source"] = "manual"
    if data.get("m5_pre_entry_ignored"):
        filtered = data
    else:
        filtered = data_with_m5_from_entry(data, user_entry)
    out["m5_entry_touch_index"] = filtered.get("m5_entry_touch_index")
    out["m5_from_entry_len"] = filtered.get("m5_from_entry_len")
    out["m5_pre_entry_ignored"] = True
    dec = int(out.get("dec", data.get("price_decimals", 1)))
    fmt = f".{dec}f"

    past = optimize_sl_tp_from_past(
        filtered, user_entry, direction, crt=filtered.get("crt"), zone=zone,
    )
    if past is not None:
        sl, tp, rr, risk = past["sl"], past["tp"], past["rr"], past["risk_pts"]
        out.update({
            "valid": True,
            "sl": sl,
            "tp": tp,
            "rr": rr,
            "risk_pts": risk,
            "sl_source": past["sl_source"],
            "tp_source": past["tp_source"],
            "sl_label": past.get("sl_label"),
            "tp_label": past.get("tp_label"),
            "sl_tp_source": "past",
            "sl_tp_note": past.get("sl_tp_note"),
            "opti_action": f"ENTRAR {direction} (Entry usuario · SL/TP past)",
            "invalidacion": (
                (
                    f"Cierre M5 > {sl:{fmt}} o breakout sin rechazo "
                    if direction == "SHORT"
                    else f"Cierre M5 < {sl:{fmt}} o breakdown sin reclaim "
                )
                + f"(Entry usuario {user_entry:{fmt}}; SL past={past.get('sl_label', 'estructura')})"
            ),
            "trigger": (
                f"Entry usuario CLI @ {user_entry:{fmt}} ({direction}) · "
                f"SL/TP desde estructura post-entry"
            ),
        })
        return out

    return _apply_entry_override_naive_rr(
        out, user_entry, direction, zone, filtered,
        fallback_note="SL/TP 1:2 (fallback; sin estructura pasada segura post-entry)",
    )


def _compute_optimal_entry_core(
    data: dict, direction: str, zone: dict,
) -> dict:
    """System Entrada óptima from zone/price (no CLI user entry)."""
    price = data["price"]
    dec = data.get("price_decimals", 1)
    level = zone.get("level")
    near = zone.get("dist_pct") is not None and zone["dist_pct"] <= 0.15
    confirm = (
        data.get("confirm_long", False) if direction == "LONG"
        else data.get("confirm_short", False) if direction == "SHORT"
        else False
    )
    ztype = zone.get("type", "zona")
    fmt = f".{dec}f"

    if not level or direction not in ("LONG", "SHORT"):
        return {
            "valid": False,
            "direction": direction,
            "dec": dec,
            "ahora_price": price,
            "ahora_2m5": "No" if not confirm else "Sí",
            "ahora_near": near,
            "ahora_action": "ESPERAR",
            "opti_zone": "n/d",
            "opti_2m5": "n/d",
            "opti_action": "ESPERAR",
            "trigger": "Definir bias y zona S/R",
            "confirmacion": "2 velas M5 en dirección en zona ≤0.15%",
            "entry": None,
            "sl": None,
            "tp": None,
            "rr": None,
            "zone_lo": None,
            "zone_hi": None,
            "invalidacion": "n/d",
            "plan_b": "Re-scan light en 30 min si no hay retest",
        }

    if direction == "SHORT":
        zone_lo = level * (1 - 0.0015)
        zone_hi = level
        entry = level - (level - zone_lo) * 0.35
        sl = level * 1.002 if ztype == "resistencia_debil" else level * 1.003
        risk = abs(sl - entry)
        tp = entry - 2 * risk
        color_word = "rojas"
        invalidacion = f"Cierre M5 > {sl:{fmt}} o breakout > {level:{fmt}} sin rechazo"
        trigger = (
            f"Retest {zone_lo:{fmt}}–{zone_hi:{fmt}} ({ztype} @ {level:{fmt}}) "
            f"+ 2 velas M5 {color_word} consecutivas en zona"
        )
        opti_2m5 = f"Nuevas 2 {color_word} en zona tras retest (no las actuales lejos)"
    else:
        zone_lo = level
        zone_hi = level * (1 + 0.0015)
        entry = level + (zone_hi - level) * 0.35
        sl = level * 0.998 if ztype == "soporte_debil" else level * 0.997
        risk = abs(entry - sl)
        tp = entry + 2 * risk
        color_word = "verdes"
        invalidacion = f"Cierre M5 < {sl:{fmt}} o breakdown < {level:{fmt}} sin reclaim"
        trigger = (
            f"Retest {zone_lo:{fmt}}–{zone_hi:{fmt}} ({ztype} @ {level:{fmt}}) "
            f"+ 2 velas M5 {color_word} consecutivas en zona"
        )
        opti_2m5 = f"Nuevas 2 {color_word} en zona tras retest (no las actuales lejos)"

    if near and confirm:
        ahora_action = f"ENTRAR {direction}"
        opti_action = f"ENTRAR {direction} (condiciones actuales OK)"
    elif confirm and not near:
        ahora_action = f"ESPERAR {direction}"
        opti_action = f"ENTRAR {direction}"
    else:
        ahora_action = f"ESPERAR {direction}" if direction != "NONE" else "ESPERAR"
        opti_action = f"ENTRAR {direction}" if direction != "NONE" else "ESPERAR"

    dist_note = f"{zone.get('dist_pct', 0):.2f}%" if zone.get("dist_pct") is not None else "n/d"
    plan_b = (
        "Light re-scan ~30 min: si precio no retestea zona → skip trade AM; "
        "reservar PM solo si AM=ESPERAR y <2 SL"
    )

    return {
        "valid": True,
        "direction": direction,
        "dec": dec,
        "level": level,
        "ztype": ztype,
        "ahora_price": price,
        "ahora_2m5": "Sí" if confirm else "No",
        "ahora_near": near,
        "ahora_dist": dist_note,
        "ahora_action": ahora_action,
        "opti_zone": f"{zone_lo:{fmt}}–{zone_hi:{fmt}}",
        "opti_2m5": opti_2m5,
        "opti_action": opti_action,
        "trigger": trigger,
        "confirmacion": f"2 velas M5 {color_word} consecutivas con cierres en zona ≤0.15%",
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "rr": 2.0,
        "risk_pts": risk,
        "zone_lo": zone_lo,
        "zone_hi": zone_hi,
        "invalidacion": invalidacion,
        "plan_b": plan_b,
    }


def compute_optimal_entry(
    data: dict, direction: str, crt: dict, zone: dict,
    entry_override: float | None = None,
) -> dict:
    """Optimal E1 entry plan from live zone/price (TRADING_2M5_SHORT_VISUAL logic).

    If `entry_override` (or `data['entry_override']`) is set:
    - Entrada óptima (`entry`) stays system-computed on post-entry M5 context
      (pre-entry candles ignored).
    - `user_entry` holds the CLI fill; SL/TP optimize for that fill from filtered past.
    """
    _ = crt  # kept for call-site compatibility / future CRT-aware entry
    if entry_override is None and data.get("entry_override") is not None:
        entry_override = data.get("entry_override")

    if entry_override is not None:
        user_entry = float(entry_override)
        m5_full = data.get("m5") or []
        orig_touch = find_m5_index_at_user_entry(m5_full, user_entry) if m5_full else None
        filtered = data_with_m5_from_entry(data, user_entry)
        opt = _compute_optimal_entry_core(filtered, direction, zone)
        out = _apply_entry_override(opt, user_entry, direction, zone, filtered)
        out["m5_entry_touch_index"] = orig_touch
        out["m5_from_entry_len"] = len(filtered.get("m5") or [])
        out["m5_pre_entry_ignored"] = True
        return out

    return _compute_optimal_entry_core(data, direction, zone)


def format_optimal_entry_md(opt: dict, data: dict, direction: str, crt: dict) -> list[str]:
    """Markdown: AHORA vs ENTRADA OPTIMIZADA + Plan concreto (+ ilustración opcional)."""
    dec = opt.get("dec", data.get("price_decimals", 1))
    fmt = f".{dec}f"
    bias_label = _mode_bias_label(data.get("mode_bias", "auto"))
    setup_label = _mode_setup_label(data.get("mode_setup", "auto"))
    lines = [
        "## Entrada optimizada (E1)",
        "",
        f"> Bias **{bias_label}** + **{setup_label}** · CRT PD **{crt.get('pd_reading', 'n/a')}** · "
        f"Premium/Discount **{crt.get('premium_discount', 'n/a')}**",
        "",
        "### AHORA vs ENTRADA OPTIMIZADA",
        "",
        "| | **AHORA** | **ENTRADA OPTIMIZADA** |",
        "|---|-----------|-------------------------|",
        f"| Precio | **{opt['ahora_price']:{fmt}}** | Retest **{opt.get('opti_zone', 'n/d')}** |",
        f"| 2M5 {direction} | {opt['ahora_2m5']} | {opt.get('opti_2m5', 'n/d')} |",
        f"| Cerca zona | {'✅' if opt.get('ahora_near') else '❌'} ({opt.get('ahora_dist', 'n/d')}) | ✅ ≤0.15% de {opt.get('level', 0):{fmt}} |",
        f"| Acción | **{opt['ahora_action']}** | **{opt.get('opti_action', 'ESPERAR')}** |",
        "",
        "### Plan concreto",
        "",
        "| Campo | Valor |",
        "|-------|-------|",
        f"| Trigger | {opt.get('trigger', 'n/d')} |",
        f"| Confirmación | {opt.get('confirmacion', 'n/d')} |",
    ]
    if opt.get("entry") is not None or opt.get("user_entry") is not None:
        sl_src = opt.get("sl_tp_source")
        if sl_src == "past":
            sl_tag = f"estructura pasada ({opt.get('sl_label', 'swing/S-R')})"
            tp_tag = (
                f"estructura pasada ({opt.get('tp_label', 'S/R')})"
                if opt.get("tp_source") == "past_structure"
                else "1:2 desde SL past"
            )
            rr_disp = f"{opt.get('rr', 2):.1f}".rstrip("0").rstrip(".")
        elif sl_src == "fallback":
            sl_tag = "1:2 fallback (sin estructura past)"
            tp_tag = "1:2 fallback"
            rr_disp = f"{opt.get('rr', 2):.0f}"
        else:
            sl_tag = "estructural"
            tp_tag = "1:2"
            rr_disp = f"{opt.get('rr', 2):.0f}"

        if opt.get("user_entry") is not None:
            if opt.get("entry") is not None:
                lines.append(
                    f"| Entrada óptima | **{opt['entry']:{fmt}}** "
                    f"(sistema · limit retest o market al cierre 2ª vela) |"
                )
            lines.append(
                f"| Entry usuario | **{opt['user_entry']:{fmt}}** "
                f"(CLI -Entry / --entry) |"
            )
        elif opt.get("entry") is not None:
            lines.append(
                f"| Entry | **{opt['entry']:{fmt}}** "
                f"(limit retest o market al cierre 2ª vela) |"
            )

        if opt.get("sl") is not None and opt.get("tp") is not None:
            plan_tag = " · plan Entry usuario" if opt.get("user_entry") is not None else ""
            lines += [
                f"| SL | **{opt['sl']:{fmt}}** ({sl_tag}){plan_tag} · SL cuenta ~$9 (ajustar lotaje) |",
                f"| TP | **{opt['tp']:{fmt}}** ({tp_tag}){plan_tag} |",
                f"| R:R | **1:{rr_disp}** · riesgo **{opt.get('risk_pts', 0):.{dec}f}** pts |",
            ]
            if opt.get("sl_tp_note"):
                lines.append(f"| SL/TP nota | {opt['sl_tp_note']} |")
            lines += [
                f"| Invalidación | {opt.get('invalidacion', 'n/d')} |",
                f"| Plan B | {opt.get('plan_b', 'n/d')} |",
            ]
    else:
        lines.append("| Entry / SL / TP | Definir zona S/R válida primero |")
    lines += ["", "---", ""]
    if data.get("ilustrate"):
        from app.views.illustrate_high_entry import format_illustration_md
        ann = data.get("annotated_chart_file", "btc_m5_chart_annotated.png")
        abs_ann = data.get("annotated_chart_abs")
        lines += format_illustration_md(ann, absolute_path=abs_ann)
    return lines


def format_2m5_valid_invalid(data: dict, direction: str) -> list[str]:
    """Markdown: patrones 2M5 válidos vs inválidos (photo2)."""
    m5 = data.get("m5", [])
    zone = data["zone"]
    dec = data.get("price_decimals", 1)
    fmt = f".{dec}f"
    level = zone.get("level")
    ztype = zone.get("type", "S/R")
    near = zone.get("dist_pct") is not None and zone["dist_pct"] <= 0.15
    in_zone_2 = _candles_in_zone(m5, zone)
    last2 = _last_n_colors(m5, 2)
    last2_pat = f"[{']['.join(last2)}]" if len(last2) == 2 else "[?][?]"

    lines = [
        "## 2M5 — Válido vs Inválido",
        "",
        "| Patrón | Estado | Nota |",
        "|--------|--------|------|",
    ]

    if direction == "SHORT":
        zone_label = f"{ztype} @ {level:{fmt}}" if level else ztype
        ok_label = f"✅ SHORT OK: [R][R] en {zone_label}"
        if last2 == ["R", "R"] and near and in_zone_2:
            ok_note = "**VÁLIDO** — Últimas 2 rojas en zona ≤0.15%"
        elif last2 == ["R", "R"] and not near:
            ok_note = f"**ESPERAR** — [R][R] sí pero {zone.get('dist_pct', 0):.2f}% lejos; retest"
        else:
            ok_note = "Referencia — requiere 2 rojas **nuevas** en retest"
        lines.append(f"| {ok_label} | {ok_note} | Patrón válido SHORT en resistencia |")
        lines.append("| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |")
        lines.append(
            f"| ❌ NO: [R][R] … {last2_pat} | **INVÁLIDO** | "
            "2M5 válidas deben ser las **últimas 2** velas (no anteriores) |"
        )
    elif direction == "LONG":
        zone_label = f"{ztype} @ {level:{fmt}}" if level else ztype
        ok_label = f"✅ LONG OK: [G][G] en {zone_label}"
        if last2 == ["G", "G"] and near and in_zone_2:
            ok_note = "**VÁLIDO** — Últimas 2 verdes en zona ≤0.15%"
        elif last2 == ["G", "G"] and not near:
            ok_note = f"**ESPERAR** — [G][G] sí pero {zone.get('dist_pct', 0):.2f}% lejos; retest"
        else:
            ok_note = "Referencia — requiere 2 verdes **nuevas** en retest"
        lines.append(f"| {ok_label} | {ok_note} | Patrón válido LONG en soporte |")
        lines.append("| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |")
        lines.append(
            f"| ❌ NO: [G][G] … {last2_pat} | **INVÁLIDO** | "
            "2M5 válidas deben ser las **últimas 2** velas (no anteriores) |"
        )
    else:
        lines.append("| — | Sin dirección | Forzar bias (-Bullish/-Bearish) o esperar H1 |")

    lines += ["", "---", ""]
    return lines


def format_2m5_checklist(data: dict, direction: str, session: dict, crt: dict) -> list[str]:
    """Markdown: checklist 2M5 con ✅/❌ live (sesión = info, no ítem bloqueante)."""
    zone = data["zone"]
    near = zone.get("dist_pct") is not None and zone["dist_pct"] <= 0.15
    confirm = (
        data.get("confirm_long", False) if direction == "LONG"
        else data.get("confirm_short", False) if direction == "SHORT"
        else False
    )
    in_zone_2 = _candles_in_zone(data.get("m5", []), zone)
    rsi = data.get("rsi_m5")
    rsi_ok = True
    if rsi is not None and direction == "LONG" and rsi > 70:
        rsi_ok = False
    if rsi is not None and direction == "SHORT" and rsi < 30:
        rsi_ok = False

    bias_ok = (
        (direction == "LONG" and data.get("bias_h1") == "BULLISH")
        or (direction == "SHORT" and data.get("bias_h1") == "BEARISH")
        or data.get("mode_bias") in ("bullish", "bearish")
    )
    crt_ok = True
    prem = crt.get("premium_discount", "")
    if direction == "SHORT" and prem == "DISCOUNT":
        crt_ok = False
    if direction == "LONG" and prem == "PREMIUM":
        crt_ok = False

    items = [
        (f"Cerca de zona ({zone.get('type', 'S/R')} @ {zone.get('level', 0):.0f})", near),
        (
            f"2 velas M5 confirman {direction}" if direction in ("LONG", "SHORT") else "2 velas M5 confirman",
            confirm and in_zone_2 if direction in ("LONG", "SHORT") else confirm,
        ),
        ("Bias H1 alineado o bias CLI forzado", bias_ok),
        ("RSI M5 + CRT premium/discount coherentes", rsi_ok and crt_ok),
        (
            "Estructura/CRT sin contradicción dura",
            not (crt.get("fakeout_pdh") and direction == "LONG")
            and not (crt.get("fakeout_pdl") and direction == "SHORT"),
        ),
    ]
    all_ok = all(ok for _, ok in items)
    # Reloj opcional (no es ítem del checklist ni gate)
    clock = session.get("window") or session.get("ny_local") or "n/d"

    lines = [
        "## Checklist 2M5",
        "",
        f"_Reloj (info): {clock}_",
        "",
    ]
    for label, ok in items:
        mark = "✅" if ok else "❌"
        lines.append(f"- [{mark}] {label}")
    lines += [
        "",
        f"**{'Las 5 ✅ → 2M5 OK. Si falta una → ESPERAR.' if all_ok else 'Falta al menos 1 ítem → ESPERAR.'}**",
        "",
        "---",
        "",
    ]
    return lines


def compute_second_indication(
    data: dict, bias_h1: str, crt: dict, dmi: dict, struct: dict,
) -> dict:
    """Segunda indicación cuando H1 NEUTRAL — DMI, CRT PD, estructura M5."""
    if bias_h1 != "NEUTRAL":
        return {}

    hints: list[tuple[str, str, str]] = []
    dmi_bias = dmi.get("bias", "NEUTRAL")
    if dmi_bias == "BULL":
        hints.append(("DMI (momentum M5)", dmi.get("note", ""), "LONG"))
    elif dmi_bias == "BEAR":
        hints.append(("DMI (momentum M5)", dmi.get("note", ""), "SHORT"))
    else:
        hints.append(("DMI (momentum M5)", dmi.get("note", "Momentum mixto"), "NEUTRAL"))

    pd = crt.get("pd_reading", "n/a")
    prem = crt.get("premium_discount", "n/a")
    if pd == "BULLISH" or prem == "DISCOUNT":
        hints.append(("CRT PD / Premium-Discount", f"{pd} · {prem}", "LONG"))
    elif pd == "BEARISH" or prem == "PREMIUM":
        hints.append(("CRT PD / Premium-Discount", f"{pd} · {prem}", "SHORT"))
    else:
        hints.append(("CRT PD / Premium-Discount", f"{pd} · {prem}", "NEUTRAL"))

    hl, lh = struct.get("hl", "n/a"), struct.get("lh", "n/a")
    struct_read = f"{hl} · {lh}"
    if "HH" in lh and ("HL" in hl or "LL" not in hl):
        struct_hint = "LONG"
    elif "LL" in hl and ("LH" in lh or "HH" not in lh):
        struct_hint = "SHORT"
    else:
        struct_hint = "NEUTRAL"
    hints.append(("Estructura swings M5", struct_read, struct_hint))

    votes = {"LONG": 0, "SHORT": 0, "NEUTRAL": 0}
    for _, _, s in hints:
        votes[s] += 1
    if votes["LONG"] > votes["SHORT"]:
        suggested = "LONG"
    elif votes["SHORT"] > votes["LONG"]:
        suggested = "SHORT"
    else:
        suggested = "NEUTRAL"

    return {
        "hints": hints,
        "suggested": suggested,
        "explanation": (
            "Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta "
            "un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount "
            "y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no "
            "define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV."
        ),
    }


def format_second_indication_md(segunda: dict) -> list[str]:
    """Markdown: tabla segunda indicación (solo H1 NEUTRAL)."""
    if not segunda:
        return []
    lines = [
        "## Segunda indicación (H1 NEUTRAL)",
        "",
        f"> {segunda.get('explanation', '')}",
        "",
        f"**Sesgo sugerido (votos auxiliares):** **{segunda.get('suggested', 'NEUTRAL')}**",
        "",
        "| Fuente | Lectura | Sesgo sugerido |",
        "|--------|---------|----------------|",
    ]
    for fuente, lectura, sesgo in segunda.get("hints", []):
        lines.append(f"| {fuente} | {lectura} | **{sesgo}** |")
    lines += ["", "---", ""]
    return lines


def format_high_signal_extras(data: dict, ctx: dict, crt: dict) -> list[str]:
    """Entrada optimizada + 2M5 válido/inválido + checklist + segunda indicación."""
    direction = data["setup"]["direction"]
    opt = compute_optimal_entry(data, direction, crt, data["zone"])
    lines: list[str] = ["", "---", ""]
    lines += format_optimal_entry_md(opt, data, direction, crt)
    lines += format_2m5_valid_invalid(data, direction)
    lines += format_2m5_checklist(data, direction, data["session"], crt)
    segunda = ctx.get("categories", {}).get("segunda_indicacion")
    if data.get("bias_h1") == "NEUTRAL" and segunda:
        lines += format_second_indication_md(segunda)
    return lines


def build_high_context(
    data: dict,
    m5: list[dict],
    h1: list[dict],
    last_n_candle_summary,
    bias_mode: str = "auto",
    setup_mode: str = "auto",
) -> dict:
    work = apply_forced_bias(data, bias_mode) if bias_mode in ("bullish", "bearish") else dict(data)
    work["mode_bias"] = bias_mode
    work["mode_setup"] = setup_mode
    work["m5"] = m5

    crt = analyze_crt(work["price"], work.get("pdh"), work.get("pdl"), h1, m5)
    crt = adjust_crt_for_setup_mode(crt, setup_mode, work)
    div = detect_rsi_divergence(m5)
    dmi = dmi_proxy([c["close"] for c in m5])
    struct = structure_notes(work["swing_highs"], work["swing_lows"])
    e2 = analyze_turtle_soup_e2(work["price"], m5, crt, work["swing_lows"], div)
    e2 = adjust_e2_for_setup_mode(e2, setup_mode, work)
    rules_pct, rules_items = score_rules_pct(work, crt, div, dmi, e2)
    pats = match_gallery_pattern(work, crt)
    pats = adjust_gallery_for_setup_mode(pats, setup_mode, work, crt)
    mode_notes = mode_reasoning_notes(bias_mode, setup_mode, work, crt, e2)
    out = dict(work)
    out.update({
        "crt": crt, "divergence": div, "dmi": dmi, "structure": struct, "e2": e2,
        "rules_score": (rules_pct, rules_items),
        "gallery_patterns": pats,
        "last_m5_12": last_n_candle_summary(m5, 12),
        "last_h1_3": last_h1_summary(h1, 3),
        "mode_notes": mode_notes,
        "m5": m5,
    })
    return out


def write_high_signal(
    path: Path, data: dict, verdict_to_signal_fn, use_ml: bool = False, advanced: bool = False,
) -> None:
    from app.views.btc_e1_report import TIER_HIGH, build_report_context, format_e1_report
    from app.models.btc_signal_categories import (
        build_advanced_table_rows,
        build_contingency_guidance,
        compute_confluencia_setup,
        format_contingency_table_rows,
        format_entrada_optima_cell,
        format_entry_usuario_cell,
    )
    from app.views.illustrate_high_entry import format_salidas_block

    crt = data["crt"]
    div = data["divergence"]
    dmi = data["dmi"]
    struct = data["structure"]
    e2 = data["e2"]
    pats = data["gallery_patterns"]
    bias_mode = data.get("mode_bias", "auto")
    setup_mode = data.get("mode_setup", "auto")
    ctx = build_report_context(
        data, crt=crt, div=div, dmi=dmi, e2=e2, gallery_patterns=pats,
    )
    if use_ml and data.get("ml_categories"):
        ctx["categories"] = data["ml_categories"]

    if data.get("bias_h1") == "NEUTRAL":
        segunda = compute_second_indication(data, data["bias_h1"], crt, dmi, struct)
        if segunda:
            ctx["categories"]["segunda_indicacion"] = segunda
            ctx["categories"]["segunda_indicacion_sesgo"] = segunda["suggested"]

    # Enrich Categories: Precio, Entrada óptima, Confluencia (+ Advanced rows)
    cats = ctx["categories"]
    direction = data["setup"]["direction"]
    opt = compute_optimal_entry(data, direction, crt, data["zone"])
    dec = int(opt.get("dec", data.get("price_decimals", 1)))
    fmt = f".{dec}f"
    cats["precio"] = f"{data['price']:{fmt}}"
    history_mode = bool(data.get("history_mode"))
    # Historial: High append+reflexión; history_mode = solo revisión P&L (sin append)
    from app.models.signal_history import persist_and_reflect_entry
    reflection = persist_and_reflect_entry(data, opt, history_mode=history_mode)
    if history_mode:
        cats["history_mode"] = True
        cats["revision_ultima_entry"] = reflection.get(
            "cell_revision", reflection.get("cell_ultima", "—"),
        )
        cats["pnl_vs_precio"] = reflection.get("cell_pnl", "—")
        cats["ultima_senal_entrada"] = cats["revision_ultima_entry"]
        cats["calificacion_entrada"] = reflection.get(
            "cell_calificacion", reflection.get("cell_vs", "—"),
        )
        # No enfatizar Entrada óptima / señal nueva en revisión
        cats.pop("entrada_optima", None)
        cats.pop("entry_usuario", None)
    else:
        cats["entrada_optima"] = format_entrada_optima_cell(opt, data)
        user_cell = format_entry_usuario_cell(opt, data)
        if user_cell:
            cats["entry_usuario"] = user_cell
        else:
            cats.pop("entry_usuario", None)
        cats["ultima_senal_entrada"] = reflection["cell_ultima"]
        cats["calificacion_entrada"] = reflection.get(
            "cell_calificacion", reflection["cell_vs"],
        )
    cats["vs_ultima_entrada"] = cats["calificacion_entrada"]  # alias compat
    cats["vs_ultima_status"] = reflection["status"]
    cats["calificacion_grade"] = reflection.get("grade", reflection["status"])
    conf_level, conf_detail = compute_confluencia_setup(cats, data, crt=crt, e2=e2)
    cats["confluencia_setup"] = conf_level
    cats["confluencia_detalle"] = conf_detail
    if advanced:
        cats["advanced"] = True
        cats["advanced_rows"] = build_advanced_table_rows(
            cats, data, opt=opt, ext_pct=ctx.get("ext_pct"), e2=e2,
        )
    else:
        cats.pop("advanced", None)
        cats.pop("advanced_rows", None)
    # Contingencias auto-on si Recomendación ESPERAR (LONG/SHORT); no history_mode
    guidance = build_contingency_guidance(cats, data, opt=opt)
    if guidance:
        cats["contingency"] = guidance
        cats["contingency_rows"] = format_contingency_table_rows(guidance)
    else:
        cats.pop("contingency", None)
        cats.pop("contingency_rows", None)

    mode_header = ""
    if bias_mode != "auto" or setup_mode != "auto":
        parts = []
        if bias_mode != "auto":
            parts.append(_mode_bias_label(bias_mode))
        if setup_mode != "auto":
            parts.append(
                _mode_setup_label(setup_mode)
                .replace(" (breakout)", "")
                .replace(" (E2)", "")
                .replace(" (E1)", "")
                .replace(" (E2 ctx)", "")
            )
        mode_header = f"> **Modo:** {' + '.join(parts)}"
        if data.get("mode_notes"):
            mode_header += " — " + data["mode_notes"][0]

    asset = data.get("asset_label", "BTC")
    chart_file = data.get("chart_file", "btc_m5_chart.png")
    asset_refs = _high_asset_refs(asset)
    price_hdr = f"{data['price']:{fmt}}"
    lines = [
        f"# {asset} M5 High Signal — CRT + Turtle Soup (Deep Analysis)",
        "",
        f"> {data['generated']} UTC | NY {data['session'].get('ny_local', 'n/a')} | {data['session']['window']}",
        f"> Precio **{price_hdr}** | HIGH mode | PF E1=4.77 | E2 max 10%",
        f"> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6",
    ]
    if mode_header:
        lines.append(mode_header)
    if advanced:
        lines.append("> Modo **ADVANCED** — Categories ampliada + secciones A–I")
    lines += [
        "",
        "| Campo | Valor |",
        "|-------|-------|",
        f"| Modo bias | **{_mode_bias_label(bias_mode)}** |",
        f"| Modo setup | **{_mode_setup_label(setup_mode)}** |",
        "",
        "---",
        "",
    ]
    if data.get("mode_notes"):
        lines += ["### Modo CLI (bias/setup)", ""]
        for note in data["mode_notes"]:
            lines.append(f"- {note}")
        lines += ["", "---", ""]
    lines += format_e1_report(
        data, TIER_HIGH, ctx=ctx, crt=crt, div=div, dmi=dmi, e2=e2, gallery_patterns=pats,
    )
    lines += format_high_signal_extras(data, ctx, crt)
    lines += [
        "",
        "## Indicadores Legacy Pro (proxy)",
        "",
        f"| CRT | {crt['h1_state']}/{crt['pd_reading']} | Núcleo |",
        f"| RSI TORYS | {div['type']} | {div['note']} |",
        f"| DMI | {dmi['bias']} | {dmi['note']} |",
        f"| Swings | {struct['hl']} | {struct['lh']} |",
        "",
        "---",
        "",
        "## M5 detalle",
        "",
    ]
    if data.get("rsi_m5") is not None:
        rsi_h1 = data.get("rsi_h1")
        rsi_h1_s = f"{rsi_h1:.1f}" if rsi_h1 is not None else "n/a"
        lines.append(f"- RSI M5/H1: {data['rsi_m5']:.1f} / {rsi_h1_s}")
    lines += [
        f"- Zona: {data['zone'].get('type', '')} @ {data['zone'].get('level', 0):.0f}",
        f"- 2M5 LONG: {'SÍ' if data['confirm_long'] else 'NO'} | SHORT: {'SÍ' if data['confirm_short'] else 'NO'}",
        "",
        "### 12 velas M5",
        "",
    ]
    for row in data["last_m5_12"]:
        lines.append(f"- `{row}`")
    rules_pct = ctx["ext_pct"]
    lines += [
        "",
        "---",
        "",
        f"## Score reglas extendidas ({rules_pct}%)",
        "",
        "| Regla | OK | Nota |",
        "|-------|----|------|",
    ]
    for label, passed, note in ctx["ext_items"]:
        lines.append(f"| {label} | {'SÍ' if passed else 'NO'} | {note} |")
    if advanced:
        lines += format_advanced_sections(
            data, ctx, crt, e2, pats, data.get("last_h1_3", []),
        )
    lines += [
        "",
        "---",
        "",
        "## Cursor HIGH response",
    ]
    if advanced:
        lines += [
            f"Modo **ADVANCED** — usar prompt completo en `{asset_refs['protocol']}` §Modo Advanced.",
            "Leer Categories (incl. Entrada óptima + Confluencia + Advanced) y secciones A–I. **NO acortar** vs light mode.",
        ]
    else:
        lines += [
            "1. Usar **Veredicto** + tabla Categories (Precio · Entrada óptima · Confluencia setup).",
            "2. Leer **Entrada optimizada (E1)** + **Checklist 2M5** + **2M5 Válido/Inválido**.",
            "3. Citar CRT pending/completed/invalid + RSI TORYS.",
            "4. Galería WIN match. 5. E2 solo watch. 6. Confirmar TV.",
            "7. En resumen chat: **Salidas** + chart High (líneas OPTI si no `-NoChart`; anotado si Ilustrate).",
        ]
    lines += [""]
    if data.get("chart"):
        lines.append(f"![Chart]({chart_file})")
    # Salidas: paths fáciles para abrir chart/MD (sin base64)
    ann_name = data.get("annotated_chart_file") if data.get("ilustrate") else None
    lines += format_salidas_block(
        signal_md=path,
        annotated_file=ann_name,
        annotated_abs=data.get("annotated_chart_abs") if ann_name else None,
    )
    lines += ["", f"---\n*high signal | {data['generated']} UTC*\n"]
    path.write_text("\n".join(lines), encoding="utf-8")
