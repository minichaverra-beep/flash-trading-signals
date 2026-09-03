"""Categorías estructuradas compartidas para los 3 tiers BTC M5."""

from __future__ import annotations



E1_RULES_TOTAL = 7  # sin Sesión NY (info en header/Categories, no bloquea checklist)



# TRADING_WINRATE_STATS.md — E1 continuación / E2 reversión

WR_BTC_E1 = 82.0

WR_BTC_GLOBAL = 69.0

WR_GLOBAL = 67.0

WR_BTC_E2 = 61.1  # E2 BTC proxy

WR_E2_GLOBAL = 63.1  # E2 global proxy





def verdict_to_signal(setup: dict) -> str:
    v = setup["verdict"]
    if v == "SETUP_A+":
        return "ENTRAR"
    if v == "SETUP_B_ESPERAR":
        return "ESPERAR"
    if v == "NO_TRADE":
        return "NO_OPERAR"
    return "ESPERAR"


def bando_usado_label(mode_bias: str | None) -> str:
    """CLI bias flag: AUTO | BULLISH | BEARISH."""
    return {"auto": "AUTO", "bullish": "BULLISH", "bearish": "BEARISH"}.get(
        (mode_bias or "auto").lower(), (mode_bias or "AUTO").upper(),
    )


def format_recomendacion(
    verdict: str,
    direction: str,
    *,
    session_in_ny: bool = True,
) -> str:
    """Recomendación legible con dirección explícita (ENTRAR SHORT, ESPERAR LONG, etc.).

    session_in_ny se acepta por compatibilidad pero ya no fuerza NO_OPERAR;
    la sesión es informativa (header/Categories), no bloquea la recomendación.
    """
    _ = session_in_ny  # info-only; no altera recomendación
    dir_u = direction if direction in ("LONG", "SHORT") else None

    if verdict == "ENTRAR":
        if dir_u == "LONG":
            return "ENTRAR LONG"
        if dir_u == "SHORT":
            return "ENTRAR SHORT"
        return "ENTRAR (sin dirección)"
    if verdict == "ESPERAR":
        if dir_u == "LONG":
            return "ESPERAR LONG"
        if dir_u == "SHORT":
            return "ESPERAR SHORT"
        return "ESPERAR (sin dirección)"
    if verdict == "NO_OPERAR":
        if dir_u == "LONG":
            return "NO_OPERAR LONG"
        if dir_u == "SHORT":
            return "NO_OPERAR SHORT"
        return "NO_OPERAR"
    return verdict


def enrich_categories_bando(categories: dict, data: dict, verdict: str) -> None:
    """Añade Bando usado, Bando mercado y Recomendación a categories (in-place)."""
    categories["bando_usado"] = bando_usado_label(data.get("mode_bias", "auto"))
    categories["bando_mercado"] = data.get("bias_h1", "NEUTRAL")
    categories["recomendacion"] = format_recomendacion(
        verdict,
        data["setup"]["direction"],
    )


def format_entrada_optima_cell(opt: dict | None, data: dict | None = None) -> str:
    """Valor de celda Entrada óptima: preferir Entry numérico; si falta, zona retest."""
    if not opt:
        return "n/d"
    dec = int(opt.get("dec", (data or {}).get("price_decimals", 1)))
    fmt = f".{dec}f"
    entry = opt.get("entry")
    if entry is not None:
        return f"{entry:{fmt}}"
    zone = opt.get("opti_zone")
    if zone and zone != "n/d":
        return f"Retest {zone}"
    return "n/d"


def compute_confluencia_setup(
    categories: dict,
    data: dict,
    crt: dict | None = None,
    e2: dict | None = None,
) -> tuple[str, str]:
    """Confluencia setup: ALTA / MEDIA / BAJA / NULA.

    Alinea Rules %, Neural (si hay), validez 2M5, operabilidad Break/Reverse
    y bias H1 vs bando CLI. Score normalizado sobre puntos disponibles.
    """
    score = 0.0
    max_pts = 0.0
    notes: list[str] = []

    rules_pct = int(categories.get("rules_pct", 0) or 0)
    max_pts += 3
    if rules_pct >= 75:
        score += 3
        notes.append(f"Rules {rules_pct}%")
    elif rules_pct >= 63:
        score += 2
        notes.append(f"Rules {rules_pct}%")
    elif rules_pct >= 50:
        score += 1
        notes.append(f"Rules {rules_pct}%")
    else:
        notes.append(f"Rules {rules_pct}% bajo")

    if "neural_prob_win" in categories and categories.get("neural_prob_win") is not None:
        max_pts += 3
        nw = float(categories["neural_prob_win"])
        aligned = bool(categories.get("neural_gallery_aligned"))
        if nw >= 0.70 and aligned:
            score += 3
            notes.append(f"Neural {nw * 100:.0f}% alineado")
        elif nw >= 0.70:
            score += 2
            notes.append(f"Neural {nw * 100:.0f}%")
        elif nw >= 0.50:
            score += 1
            notes.append(f"Neural {nw * 100:.0f}%")
        else:
            notes.append(f"Neural {nw * 100:.0f}% débil")

    direction = data.get("setup", {}).get("direction", "NONE")
    near = (
        data.get("zone", {}).get("dist_pct") is not None
        and data["zone"]["dist_pct"] <= 0.15
    )
    confirm = (
        data.get("confirm_long", False) if direction == "LONG"
        else data.get("confirm_short", False) if direction == "SHORT"
        else False
    )
    max_pts += 2
    if confirm and near:
        score += 2
        notes.append("2M5+zona OK")
    elif confirm or near:
        score += 1
        notes.append("2M5 o zona parcial")
    else:
        notes.append("2M5/zona no listos")

    setup_mode = (data.get("mode_setup") or "auto").lower()
    max_pts += 2
    if setup_mode == "reverse":
        if e2 and e2.get("eligible"):
            score += 2
            notes.append("E2 operable")
        elif e2 and e2.get("verdict") in ("E2_WATCH", "E2_READY"):
            score += 1
            notes.append("E2 watch")
        else:
            notes.append("E2 no operable")
    elif setup_mode == "break":
        hard = False
        if crt:
            if direction == "LONG" and (crt.get("fakeout_pdh") or crt.get("pd_reading") == "BEARISH"):
                hard = True
            if direction == "SHORT" and (crt.get("fakeout_pdl") or crt.get("pd_reading") == "BULLISH"):
                hard = True
        if direction in ("LONG", "SHORT") and not hard:
            score += 2
            notes.append("Break operable")
        elif direction in ("LONG", "SHORT"):
            score += 1
            notes.append("Break con fricción CRT")
        else:
            notes.append("Break sin dirección")
    else:
        if direction in ("LONG", "SHORT"):
            score += 1
            notes.append("Setup auto con dirección")
        else:
            notes.append("Setup auto sin dirección")

    max_pts += 2
    bias = data.get("bias_h1", "NEUTRAL")
    mode_bias = (data.get("mode_bias") or "auto").lower()
    aligned_h1 = (
        (direction == "LONG" and bias == "BULLISH")
        or (direction == "SHORT" and bias == "BEARISH")
    )
    aligned_cli = (
        (direction == "LONG" and mode_bias == "bullish")
        or (direction == "SHORT" and mode_bias == "bearish")
    )
    if aligned_h1:
        score += 2
        notes.append("H1 alineado")
    elif aligned_cli:
        score += 1
        notes.append("CLI alineado / H1 no")
    elif bias == "NEUTRAL":
        notes.append("H1 NEUTRAL")
    else:
        notes.append("Bias vs bando en conflicto")

    pct = int(score / max_pts * 100) if max_pts else 0
    if pct >= 75:
        level = "ALTA"
    elif pct >= 50:
        level = "MEDIA"
    elif pct >= 25:
        level = "BAJA"
    else:
        level = "NULA"
    detail = f"{pct}% · " + "; ".join(notes[:4])
    return level, detail


def build_advanced_table_rows(
    categories: dict,
    data: dict,
    opt: dict | None = None,
    ext_pct: int | None = None,
    e2: dict | None = None,
) -> list[tuple[str, str]]:
    """Filas extra (español) para Categories cuando advanced=True. Solo métricas reales."""
    rows: list[tuple[str, str]] = []
    dec = int((opt or {}).get("dec", data.get("price_decimals", 1)))
    fmt = f".{dec}f"
    price = data.get("price")
    direction = data.get("setup", {}).get("direction", "NONE")

    if opt and opt.get("rr") is not None:
        rows.append(("R:R", f"1:{opt['rr']:.0f}"))
    elif data.get("setup", {}).get("rr") is not None:
        rows.append(("R:R", f"1:{data['setup']['rr']:.0f}"))

    if opt and price is not None and opt.get("entry") is not None:
        entry = float(opt["entry"])
        dist = entry - float(price)
        dist_pct = abs(dist) / float(price) * 100 if price else 0.0
        rows.append(
            ("Dist. a Entry", f"{dist:+{fmt}} pts ({dist_pct:.3f}%)"),
        )
    if opt and price is not None and opt.get("sl") is not None:
        sl = float(opt["sl"])
        dist = sl - float(price)
        dist_pct = abs(dist) / float(price) * 100 if price else 0.0
        rows.append(("Dist. a SL", f"{dist:+{fmt}} pts ({dist_pct:.3f}%)"))
    if opt and price is not None and opt.get("tp") is not None:
        tp = float(opt["tp"])
        dist = tp - float(price)
        dist_pct = abs(dist) / float(price) * 100 if price else 0.0
        rows.append(("Dist. a TP", f"{dist:+{fmt}} pts ({dist_pct:.3f}%)"))

    if opt and opt.get("risk_pts") is not None:
        rows.append(("Riesgo (pts)", f"{opt['risk_pts']:{fmt}}"))

    wr = categories.get("winrate")
    if wr:
        rows.append(("Winrate setup", f"{wr} — {categories.get('winrate_source', '')}".rstrip(" —")))

    if ext_pct is not None:
        rows.append(("Score Rules extendido", f"**{ext_pct}%**"))

    near = (
        data.get("zone", {}).get("dist_pct") is not None
        and data["zone"]["dist_pct"] <= 0.15
    )
    confirm = (
        data.get("confirm_long", False) if direction == "LONG"
        else data.get("confirm_short", False) if direction == "SHORT"
        else False
    )
    if direction in ("LONG", "SHORT"):
        if confirm and near:
            m5_state = f"VÁLIDO {direction} (2M5+zona)"
        elif confirm:
            m5_state = f"2M5 sí · lejos zona ({data.get('zone', {}).get('dist_pct', 0):.2f}%)"
        elif near:
            m5_state = "En zona · falta 2M5"
        else:
            m5_state = "Inválido / esperar"
        rows.append(("Estado 2M5", m5_state))

    rows.append((
        "Bias H1 vs bando",
        f"H1 **{categories.get('bando_mercado', data.get('bias_h1', 'n/d'))}** · "
        f"CLI **{categories.get('bando_usado', 'AUTO')}**",
    ))

    setup_mode = (data.get("mode_setup") or "auto").lower()
    if setup_mode == "reverse":
        if e2 and e2.get("eligible"):
            br_q = f"REVERSE operable ({e2.get('score', 0)}/{e2.get('max', 6)})"
        else:
            br_q = f"REVERSE watch ({(e2 or {}).get('verdict', 'E2_NO')})"
    elif setup_mode == "break":
        br_q = "BREAK (continuación E1)"
    else:
        br_q = "AUTO"
    rows.append(("Calidad break/reverse", br_q))

    if "neural_prob_win" in categories:
        nw = categories["neural_prob_win"] * 100
        rows.append((
            "Neural grade/conf",
            f"**{categories.get('neural_grade', '?')}** · "
            f"conf. {categories.get('neural_confidence', '?')} · {nw:.0f}% WIN",
        ))

    rules_ok = categories.get("rules_ok")
    rules_total = categories.get("rules_total")
    if rules_ok is not None and rules_total is not None:
        rows.append((
            "Rules E1 detalle",
            f"**{rules_ok}/{rules_total}** ({categories.get('rules_pct', 0)}%)",
        ))

    return rows


def label_signal(sig: str) -> str:

    return {

        "ENTRAR": "Entrar",

        "ESPERAR": "Esperar",

        "NO_OPERAR": "No operar",

        "OBSERVAR": "Esperar",

    }.get(sig, sig)





def label_direction(d: str) -> str:

    return {

        "BULLISH": "Alcista",

        "BEARISH": "Bajista",

        "NEUTRAL": "Sin dirección",

        "NONE": "Sin setup",

    }.get(d, d)





def label_setup_direction(d: str) -> str:

    return {"LONG": "Long", "SHORT": "Short", "NONE": "Ninguna"}.get(d, d)





def label_auto_verdict(v: str) -> str:

    return {

        "SETUP_A+": "Setup fuerte",

        "SETUP_B_ESPERAR": "Esperar confirmación",

        "NO_TRADE": "No operar",

        "OBSERVAR": "Esperar",

    }.get(v, v)





def label_grade(g: str) -> str:

    return {

        "A+": "Setup fuerte",

        "B": "Setup medio",

        "C": "Setup débil",

        "SKIP": "No operar",

    }.get(g, g)





def label_session(s: str) -> str:

    return {"NY AM": "Mañana NY", "NY PM": "Tarde NY", "FUERA": "Fuera NY"}.get(s, s)





def label_crt_pd(pd: str) -> str:

    return {

        "NEUTRAL": "En rango (PDH–PDL)",

        "BULLISH": "Por encima del máximo ayer",

        "BEARISH": "Por debajo del mínimo ayer",

        "n/a": "n/d",

    }.get(pd, pd)





def label_crt_h1(state: str) -> str:

    return {

        "COMPLETED_BULL": "Alcista confirmada (H1)",

        "COMPLETED_BEAR": "Bajista confirmada (H1)",

        "PENDING_BULL": "Posible giro alcista (H1)",

        "PENDING_BEAR": "Posible giro bajista (H1)",

        "INSIDE_RANGE": "Dentro del rango H1",

        "n/a": "n/d",

    }.get(state, state)





def label_dmi(bias: str) -> str:

    return {

        "BULL": "Compradores dominan",

        "BEAR": "Vendedores dominan",

        "NEUTRAL": "Equilibrado",

        "n/a": "n/d",

    }.get(bias, bias)





def label_e2_verdict(v: str) -> str:

    return {

        "E2_NO": "Sin reversión E2",

        "E2_WATCH": "Vigilar reversión E2",

        "E2_READY": "Reversión E2 posible",

    }.get(v, v.replace("_", " "))





def label_gallery(text: str) -> str:

    if text.startswith("WIN:"):

        return "Patrón ganador similar: " + text[4:].strip()

    if text.startswith("LOSS:"):

        return "Patrón perdedor similar: " + text[5:].strip()

    if text == "sin match galería":

        return "Sin patrón similar en historial"

    if "Esperar setup A+" in text:

        return "Esperar setup fuerte con patrón ganador en historial"

    return (
        text.replace("galeria", "historial")
        .replace("galería", "historial")
        .replace("WIN", "ganador")
        .replace("LOSS", "perdedor")
    )





def label_rule_note(note: str) -> str:

    return {

        "NEUTRAL": "Sin dirección",

        "BULLISH": "Alcista",

        "BEARISH": "Bajista",
        "lejos": "Lejos de la zona",

        "sin dirección activa": "Sin dirección activa",

        "E1 primario": "Operar solo E1",

        "RSI n/a": "RSI no disponible",

    }.get(note, note)





def format_rules_cell(ok: int, total: int, pct: int, *, compact: bool = False) -> str:

    if compact:

        return f"**{ok} de {total}** ({pct}%)"

    return f"Reglas cumplidas: **{ok} de {total}** ({pct}%)"





def derive_signal_direction(

    data: dict,

    crt: dict | None = None,

    dmi: dict | None = None,

) -> str:

    """BULLISH / BEARISH / NEUTRAL / NONE desde bias, setup, CRT y DMI."""

    s = data["setup"]

    direction = s["direction"]

    forced = data.get("forced_bias")
    if forced == "bullish":
        bias = "BULLISH"
    elif forced == "bearish":
        bias = "BEARISH"
    else:
        bias = data["bias_h1"]



    if direction == "LONG":

        signal = "BULLISH"

    elif direction == "SHORT":

        signal = "BEARISH"

    elif bias in ("BULLISH", "BEARISH"):

        signal = bias

    else:

        signal = "NEUTRAL"



    if crt:

        pd = crt.get("pd_reading", "n/a")

        if signal == "BULLISH" and pd == "BEARISH":

            signal = "NEUTRAL"

        elif signal == "BEARISH" and pd == "BULLISH":

            signal = "NEUTRAL"

        if direction == "LONG" and crt.get("fakeout_pdh"):

            signal = "BEARISH"

        if direction == "SHORT" and crt.get("fakeout_pdl"):

            signal = "BULLISH"



    if dmi and direction != "NONE":

        if direction == "LONG" and dmi.get("bias") == "BEAR":

            signal = "NEUTRAL" if signal == "BULLISH" else signal

        if direction == "SHORT" and dmi.get("bias") == "BULL":

            signal = "NEUTRAL" if signal == "BEARISH" else signal



    if s["verdict"] == "OBSERVAR" and direction == "NONE" and bias == "NEUTRAL":

        return "NEUTRAL"

    if direction == "NONE" and signal in ("BULLISH", "BEARISH"):

        return signal

    if direction == "NONE":

        return "NONE"

    return signal





def _crt_coherent(data: dict, crt: dict | None) -> tuple[bool, str]:

    s = data["setup"]

    direction = s["direction"]

    if direction == "NONE":

        return True, "sin dirección activa"

    if crt:

        if direction == "LONG" and crt.get("fakeout_pdh"):

            return False, "trampa en máximo ayer — no long"

        if direction == "SHORT" and crt.get("fakeout_pdl"):

            return False, "trampa en mínimo ayer — no short"

        pd = crt.get("pd_reading", "n/a")

        if direction == "LONG" and pd == "BEARISH":

            return False, "rango bajista"

        if direction == "SHORT" and pd == "BULLISH":

            return False, "rango alcista"

        return True, crt.get("crt_action_e1", "Rango coherente")[:40]

    price = data["price"]

    pdh, pdl = data.get("pdh"), data.get("pdl")

    if pdh and pdl:

        if direction == "LONG" and price < pdl:

            return False, f"precio < mínimo ayer {pdl:.0f}"

        if direction == "SHORT" and price > pdh:

            return False, f"precio > máximo ayer {pdh:.0f}"

        if pdl < price < pdh:

            return True, "dentro del rango de ayer"

        if direction == "LONG" and price > pdh:

            return True, "por encima del máximo ayer"

        if direction == "SHORT" and price < pdl:

            return True, "por debajo del mínimo ayer"

    return True, "Rango ayer OK"





def _rsi_favor(data: dict, div: dict | None) -> tuple[bool, str]:

    s = data["setup"]

    direction = s["direction"]

    if div and direction != "NONE":

        if direction == "LONG" and div.get("type") == "BEARISH":

            return False, div.get("note", "divergencia bajista")

        if direction == "SHORT" and div.get("type") == "BULLISH":

            return False, div.get("note", "divergencia alcista")

        if div.get("type") != "NONE":

            return True, div.get("note", "RSI a favor")

    rsi_m5 = data.get("rsi_m5")

    if rsi_m5 is None or direction == "NONE":

        return True, "RSI n/a"

    if direction == "LONG" and rsi_m5 > 70:

        return False, f"RSI {rsi_m5:.0f} sobrecomprado"

    if direction == "SHORT" and rsi_m5 < 30:

        return False, f"RSI {rsi_m5:.0f} sobrevendido"

    return True, f"RSI {rsi_m5:.0f} OK"





def score_e1_rules_8(

    data: dict,

    crt: dict | None = None,

    div: dict | None = None,

    dmi: dict | None = None,

    e2: dict | None = None,

) -> tuple[int, int, int, list[tuple[str, bool, str]]]:

    """Reglas E1 evaluables por script (8). Retorna (ok, total, pct, items)."""

    s = data["setup"]

    direction = s["direction"]

    confirm = (

        data["confirm_long"] if direction == "LONG"

        else data["confirm_short"] if direction == "SHORT"

        else False

    )

    near = data["zone"].get("dist_pct") is not None and data["zone"]["dist_pct"] <= 0.15

    forced = data.get("forced_bias")
    if forced == "bullish":
        effective_bias = "BULLISH"
    elif forced == "bearish":
        effective_bias = "BEARISH"
    else:
        effective_bias = data["bias_h1"]

    bias_ok = (

        (direction == "LONG" and effective_bias == "BULLISH")

        or (direction == "SHORT" and effective_bias == "BEARISH")

    )

    e2_eligible = e2["eligible"] if e2 else False

    crt_ok, crt_note = _crt_coherent(data, crt)

    rsi_ok, rsi_note = _rsi_favor(data, div)

    setup_mode = (data.get("mode_setup") or "auto").lower()
    if setup_mode == "reverse":
        solo_ok, solo_note = True, "Modo REVERSE — E2 permitido"
    else:
        solo_ok, solo_note = (not e2_eligible), "Operar solo E1"

    items = [

        ("Solo E1", solo_ok, solo_note),

        ("Tendencia H1 alineada", bias_ok, label_direction(effective_bias)),

        ("Cerca de zona clave", near, f"a {data['zone'].get('dist_pct', 0):.3f}%" if near else "lejos"),

        ("2 velas M5 confirman", confirm, "Velas confirman" if confirm else "Falta confirmación"),

        ("R:R mínimo 1:2", s.get("rr") is not None, "1:2" if s.get("rr") else "sin SL/TP"),

        ("RSI no contradice", rsi_ok, rsi_note),

        ("Rango coherente", crt_ok, crt_note),

    ]

    total = len(items)

    ok = sum(1 for _, passed, _ in items if passed)

    pct = int(ok / total * 100) if total else 0

    return ok, total, pct, items





def setup_grade(verdict: str) -> str:

    return {

        "SETUP_A+": "A+",

        "SETUP_B_ESPERAR": "B",

        "NO_TRADE": "C",

        "OBSERVAR": "SKIP",

    }.get(verdict, "SKIP")





def session_category(window: str) -> str:

    if "NY AM" in window:

        return "NY AM"

    if "NY PM" in window:

        return "NY PM"

    return "FUERA"





def winrate_estimate(

    rules_pct: int,

    gallery_patterns: list[str] | None = None,

    setup_mode: str = "auto",

) -> tuple[str, str]:

    """Retorna (valor mostrado, fuente/nota). No inventa WR sin base."""

    reverse = (setup_mode or "auto").lower() == "reverse"
    wr_top = WR_BTC_E2 if reverse else WR_BTC_E1
    wr_mid = WR_E2_GLOBAL if reverse else WR_BTC_GLOBAL
    src_tag = "E2 reversión BTC" if reverse else "E1 BTC"

    if gallery_patterns:

        wins = [p for p in gallery_patterns if p.startswith("WIN:")]

        losses = [p for p in gallery_patterns if p.startswith("LOSS:")]

        if wins and not losses:

            return f"~{wr_top:.0f}%", f"patrón ganador similar · histórico {src_tag}"

        if losses and not wins:

            return "baja", "patrón perdedor similar — evitar"

        if wins and losses:

            return "mixta", "patrones mixtos — revisar en TV"



    if rules_pct >= 75:

        return f"~{wr_top:.0f}%", f"histórico {src_tag} ({rules_pct}% reglas OK)"

    if rules_pct >= 63:

        return f"~{wr_mid:.0f}%", f"histórico {src_tag} ({rules_pct}% reglas OK)"

    if rules_pct >= 50:

        return f"~{WR_GLOBAL:.0f}%", f"probabilidad histórica (~{WR_GLOBAL:.0f}%)"

    return "N/A", f"solo {rules_pct}% reglas — setup insuficiente"





def build_categories(

    data: dict,

    sig: str,

    crt: dict | None = None,

    div: dict | None = None,

    dmi: dict | None = None,

    e2: dict | None = None,

    gallery_patterns: list[str] | None = None,

) -> dict:

    rules_ok, rules_total, rules_pct, rules_items = score_e1_rules_8(

        data, crt, div, dmi, e2,

    )

    s = data["setup"]

    signal_dir = derive_signal_direction(data, crt, dmi)

    wr_val, wr_src = winrate_estimate(
        rules_pct, gallery_patterns, setup_mode=data.get("mode_setup", "auto"),
    )

    mode_bias = data.get("mode_bias", "auto")

    cats = {

        "signal_e1": sig,

        "signal_direction": signal_dir,

        "direction": s["direction"],

        "bando_usado": bando_usado_label(mode_bias),

        "bando_mercado": data.get("bias_h1", "NEUTRAL"),

        "rules_ok": rules_ok,

        "rules_total": rules_total,

        "rules_pct": rules_pct,

        "rules_items": rules_items,

        "winrate": wr_val,

        "winrate_source": wr_src,

        "setup_grade": setup_grade(s["verdict"]),

        "session": session_category(data["session"]["window"]),

        "session_in_ny": data["session"]["in_ny_window"],

        "auto_verdict": s["verdict"],

        "gallery": gallery_patterns[0] if gallery_patterns else "sin match galería",

    }

    if crt:

        cats["crt_pd"] = crt.get("pd_reading", "n/a")

        cats["crt_h1"] = crt.get("h1_state", "n/a")

    if e2:

        cats["e2_verdict"] = e2.get("verdict", "E2_NO")

        cats["e2_score"] = f"{e2.get('score', 0)}/{e2.get('max', 6)}"

    if dmi:

        cats["dmi"] = dmi.get("bias", "n/a")

    return cats





def format_categories_md(categories: dict, *, compact: bool = False) -> list[str]:

    """Bloque Markdown ## Categories (texto en español claro)."""

    c = categories

    sig = label_signal(c["signal_e1"])

    direction = label_direction(c["signal_direction"])

    grade = label_grade(c["setup_grade"])

    session = label_session(c["session"])

    rules = format_rules_cell(c["rules_ok"], c["rules_total"], c["rules_pct"], compact=compact)

    wr = f"**{c['winrate']}** — {c['winrate_source']}"



    rec = c.get("recomendacion", format_recomendacion(c["signal_e1"], c["direction"]))

    if compact:

        lines = [

            "## Categories",

            "",

            f"| Bando usado | **{c.get('bando_usado', 'AUTO')}** | Bando mercado (H1) | **{c.get('bando_mercado', 'NEUTRAL')}** |",

            f"| Recomendación | **{rec}** |",

            f"| Acción | {sig} | Tendencia | **{direction}** |",

            f"| Reglas | {rules} | Calidad | **{grade}** |",

            f"| Prob. hist. | {wr} | Sesión | **{session}** |",

        ]

        if "ml_prob_win" in c:

            ml_pct = c["ml_prob_win"] * 100

            lines.append(

                f"| ML prob. win | **{ml_pct:.1f}%** ({c.get('ml_grade', '?')}, "

                f"conf. {c.get('ml_confidence', '?')}) |"

            )

        if "neural_prob_win" in c:

            nw = c["neural_prob_win"] * 100

            align = "✓ galería" if c.get("neural_gallery_aligned") else "—"

            lines.append(

                f"| Neural galería | **{nw:.0f}% WIN** ({c.get('neural_grade', '?')}, {align}) |"

            )

        lines.append("")

        return lines



    auto = label_auto_verdict(c["auto_verdict"])

    auto_suffix = f" ({auto})" if auto != sig else ""

    setup_dir = label_setup_direction(c["direction"])

    ny_flag = "✅ en ventana NY" if c["session_in_ny"] else "❌ fuera de NY"

    gallery = label_gallery(c["gallery"])



    lines = [

        "## Categories",

        "",

        "| Campo | Valor |",

        "|-------|-------|",

        f"| Bando usado | **{c.get('bando_usado', 'AUTO')}** |",

        f"| Bando mercado (H1) | **{c.get('bando_mercado', 'NEUTRAL')}** |",

        f"| Recomendación | **{rec}** |",

        f"| Acción recomendada | **{sig}**{auto_suffix} |",

        f"| Tendencia del setup | **{direction}** (operación: {setup_dir}) |",

        f"| Reglas del plan | {rules} |",

        f"| Probabilidad histórica | {wr} |",

        f"| Calidad del setup | **{grade}** |",

        f"| Sesión | **{session}** ({ny_flag}) |",

        f"| Patrones similares | {gallery} |",

    ]

    if "ml_prob_win" in c:

        ml_pct = c["ml_prob_win"] * 100

        lines.append(

            f"| ML prob. win | **{ml_pct:.1f}%** — grade **{c.get('ml_grade', '?')}** "

            f"(confianza {c.get('ml_confidence', '?')}) |"

        )

    if "neural_prob_win" in c:

        nw = c["neural_prob_win"] * 100

        align_note = (

            "alineado con patrones WIN desktop"

            if c.get("neural_gallery_aligned")

            else "baja similitud con galería WIN"

        )

        lines.append(

            f"| Neural galería | **{nw:.0f}% WIN** — grade **{c.get('neural_grade', '?')}** "

            f"({align_note}; conf. {c.get('neural_confidence', '?')}) |"

        )

    if "crt_pd" in c:

        lines.append(

            f"| Rango ayer / H1 | {label_crt_pd(c['crt_pd'])} / {label_crt_h1(c['crt_h1'])} |"

        )

    if "dmi" in c:

        lines.append(f"| Fuerza del movimiento | {label_dmi(c['dmi'])} |")

    if "e2_verdict" in c:

        lines.append(

            f"| Reversión E2 | {label_e2_verdict(c['e2_verdict'])} ({c['e2_score']} pts) |"

        )

    lines += ["", f"### Reglas cumplidas ({c['rules_total']})", "", "| Regla | OK | Detalle |", "|-------|----|---------|"]

    for label, passed, note in c["rules_items"]:

        lines.append(f"| {label} | {'✅' if passed else '❌'} | {label_rule_note(note)} |")

    lines.append("")

    return lines





def format_augmented_categories_md(categories: dict, *, hide_ml: bool = False) -> list[str]:
    """Bloque Categories: Precio → Entrada óptima → bando/Neural → Advanced → Confluencia.

    Orden fijo (High): Precio e Entrada óptima justo al inicio; Confluencia setup siempre última.
    history_mode: Revisión última Entry + P&L (no señal nueva; sin Entrada óptima / ENTRAR).
    Con advanced=True (categories['advanced']) se insertan stats trader antes de Confluencia.
    """
    history_mode = bool(categories.get("history_mode"))
    has_ml = "ml_prob_win" in categories and not hide_ml
    has_neural = "neural_prob_win" in categories
    has_bando = "bando_usado" in categories
    has_precio = "precio" in categories or "entrada_optima" in categories
    has_conf = "confluencia_setup" in categories
    has_review = bool(
        categories.get("revision_ultima_entry")
        or categories.get("pnl_vs_precio")
        or categories.get("calificacion_entrada")
        or categories.get("ultima_senal_entrada")
    )
    if (
        not has_ml and not has_neural and not has_bando
        and "segunda_indicacion_sesgo" not in categories
        and not has_precio and not has_conf and not has_review
    ):
        return []
    lines = [
        "## Categories",
        "",
        "| Campo | Valor |",
        "|-------|-------|",
    ]

    if history_mode:
        # Revisión P&L — no es señal de entrada
        lines.append("| **— Revisión última Entry —** | *(no es señal nueva)* |")
        if categories.get("revision_ultima_entry") or categories.get("ultima_senal_entrada"):
            rev = categories.get("revision_ultima_entry") or categories["ultima_senal_entrada"]
            lines.append(f"| Revisión última Entry | {rev} |")
        if categories.get("pnl_vs_precio"):
            lines.append(f"| P&L vs precio actual | {categories['pnl_vs_precio']} |")
        calif = categories.get("calificacion_entrada") or categories.get("vs_ultima_entrada")
        if calif:
            lines.append(f"| Calificación Entry | {calif} |")
        if "precio" in categories:
            lines.append(f"| Precio actual | **{categories['precio']}** |")
        if has_bando:
            lines.append(f"| Bando usado (lado asumido) | **{categories['bando_usado']}** |")
            lines.append(f"| Bando mercado (H1) | **{categories.get('bando_mercado', 'NEUTRAL')}** |")
        if has_neural:
            nw = categories["neural_prob_win"] * 100
            align_note = (
                "alineado con patrones WIN desktop"
                if categories.get("neural_gallery_aligned")
                else "baja similitud con galería WIN"
            )
            lines.append(
                f"| Neural galería | **{nw:.0f}% WIN** — grade **{categories.get('neural_grade', '?')}** "
                f"({align_note}; conf. {categories.get('neural_confidence', '?')}) |"
            )
        if categories.get("advanced"):
            adv_rows = categories.get("advanced_rows") or []
            if adv_rows:
                lines.append("| **— Advanced —** | |")
            for label, value in adv_rows:
                lines.append(f"| {label} | {value} |")
        if "confluencia_setup" in categories:
            conf = categories["confluencia_setup"]
            detail = categories.get("confluencia_detalle", "")
            suffix = f" — {detail}" if detail else ""
            lines.append(f"| Confluencia setup | **{conf}**{suffix} |")
        lines.append("")
        return lines

    # Precio + Entrada óptima inmediatamente después (contrato UX high)
    if "precio" in categories:
        lines.append(f"| Precio | **{categories['precio']}** |")
    if "entrada_optima" in categories:
        lines.append(f"| Entrada óptima | **{categories['entrada_optima']}** |")
    # Reflexión: última Entry del mismo par + calificación (High)
    if categories.get("ultima_senal_entrada"):
        lines.append(f"| Última señal | {categories['ultima_senal_entrada']} |")
    calif = categories.get("calificacion_entrada") or categories.get("vs_ultima_entrada")
    if calif:
        lines.append(f"| Calificación entrada | {calif} |")
    if has_bando:
        rec = categories.get(
            "recomendacion",
            format_recomendacion(categories.get("signal_e1", "ESPERAR"), categories.get("direction", "NONE")),
        )
        lines.append(f"| Bando usado | **{categories['bando_usado']}** |")
        lines.append(f"| Bando mercado (H1) | **{categories.get('bando_mercado', 'NEUTRAL')}** |")
        lines.append(f"| Recomendación | **{rec}** |")
    if categories.get("bando_mercado") == "NEUTRAL" and categories.get("segunda_indicacion_sesgo"):
        lines.append(
            f"| Segunda indicación | **{categories['segunda_indicacion_sesgo']}** "
            f"(H1 NEUTRAL — ver sección abajo) |"
        )
    if has_ml:
        ml_pct = categories["ml_prob_win"] * 100
        lines.append(
            f"| ML prob. win | **{ml_pct:.1f}%** — grade **{categories.get('ml_grade', '?')}** "
            f"(confianza {categories.get('ml_confidence', '?')}) |"
        )
    if has_neural:
        nw = categories["neural_prob_win"] * 100
        align_note = (
            "alineado con patrones WIN desktop"
            if categories.get("neural_gallery_aligned")
            else "baja similitud con galería WIN"
        )
        lines.append(
            f"| Neural galería | **{nw:.0f}% WIN** — grade **{categories.get('neural_grade', '?')}** "
            f"({align_note}; conf. {categories.get('neural_confidence', '?')}) |"
        )
    # Advanced: stats trader en español (solo si flag activo)
    if categories.get("advanced"):
        adv_rows = categories.get("advanced_rows") or []
        if adv_rows:
            lines.append("| **— Advanced —** | |")
        for label, value in adv_rows:
            lines.append(f"| {label} | {value} |")
    # Última fila de status: Confluencia setup
    if "confluencia_setup" in categories:
        conf = categories["confluencia_setup"]
        detail = categories.get("confluencia_detalle", "")
        suffix = f" — {detail}" if detail else ""
        lines.append(f"| Confluencia setup | **{conf}**{suffix} |")
    lines.append("")
    return lines


