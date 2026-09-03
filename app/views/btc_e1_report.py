"""Formateo compartido E1 CRT para tiers Light / Full / High."""

from __future__ import annotations

from app.models.btc_signal_categories import (
    E1_RULES_TOTAL,
    build_categories,
    enrich_categories_bando,
    format_augmented_categories_md,
    format_categories_md,
    format_rules_cell,
    label_crt_h1,
    label_crt_pd,
    label_direction,
    label_dmi,
    label_e2_verdict,
    label_gallery,
    label_grade,
    label_rule_note,
    label_session,
    label_setup_direction,
    label_signal,
    score_e1_rules_8,
    setup_grade,
    winrate_estimate,
)

TIER_LIGHT = "light"
TIER_FULL = "full"
TIER_HIGH = "high"


def score_extended_rules(
    data: dict,
    crt: dict | None = None,
    div: dict | None = None,
    dmi: dict | None = None,
    e2: dict | None = None,
) -> tuple[int, int, list[tuple[str, bool, str]]]:
    """10 reglas extendidas (8 E1 + DMI + 2SL/3ops + SL $9 proxy)."""
    _, _, _, items8 = score_e1_rules_8(data, crt, div, dmi, e2)
    s = data["setup"]
    direction = s["direction"]
    dmi = dmi or {"bias": "n/a", "note": "n/a"}
    dmi_ok = (
        (direction == "LONG" and dmi.get("bias") != "BEAR")
        or (direction == "SHORT" and dmi.get("bias") != "BULL")
        or direction == "NONE"
    )
    mid_ok = True
    mid_note = "n/d"
    if crt and crt.get("midpoint") and direction != "NONE":
        pd_zone = crt.get("premium_discount", "n/a")
        if direction == "LONG":
            mid_ok = pd_zone in ("DISCOUNT", "EQUILIBRIO 0.5")
            mid_note = "discount OK" if mid_ok else "premium — no long E1"
        elif direction == "SHORT":
            mid_ok = pd_zone in ("PREMIUM", "EQUILIBRIO 0.5")
            mid_note = "premium OK" if mid_ok else "discount — no short E1"
    items = list(items8) + [
        ("DMI alineado", dmi_ok, dmi.get("note", "n/a")),
        ("2 SL / 3 ops hoy", True, "Confirmar trader"),
        ("SL ~$9 cuenta", s.get("rr") is not None or direction == "NONE", "Ajustar lotaje"),
    ]
    if crt and crt.get("midpoint") and direction != "NONE":
        items.insert(-2, ("0.5 midpoint E1", mid_ok, mid_note))
    ok = sum(1 for _, passed, _ in items if passed)
    total = len(items)
    pct = int(ok / total * 100) if total else 0
    return pct, total, items


def collect_red_flags(
    data: dict,
    crt: dict | None = None,
    div: dict | None = None,
) -> list[str]:
    """Red flags CRT E1 — ordenadas por severidad.

    La sesión NY no se lista aquí: es reloj informativo, no condición de trade.
    """
    flags: list[str] = []
    s = data["setup"]
    direction = s["direction"]

    if crt:
        if crt.get("fakeout_pdh"):
            flags.append("Fakeout PDH — NO long E1; CRT invalid bearish")
        if crt.get("fakeout_pdl"):
            flags.append("Fakeout PDL — NO chase E1; contexto E2 turtle soup")
        pd = crt.get("pd_reading", "n/a")
        if pd == "NEUTRAL" and direction != "NONE":
            flags.append("Precio dentro PDH/PDL — contexto NEUTRAL, no forzar")
        if direction == "LONG" and pd == "BEARISH":
            flags.append("Precio < PDL — no long contra rango bajista CRT")
        if direction == "SHORT" and pd == "BULLISH":
            flags.append("Precio > PDH — no short contra rango alcista CRT")
        h1 = crt.get("h1_state", "")
        if direction == "LONG" and h1 == "PENDING_BEAR":
            flags.append("CRT H1 pending bear — no entrar long contra invalid reciente")
        if direction == "SHORT" and h1 == "PENDING_BULL":
            flags.append("CRT H1 pending bull — no entrar short contra invalid reciente")

    for rf in s.get("red_flags", []):
        if rf not in flags:
            flags.append(rf)

    if direction != "NONE":
        confirm = data["confirm_long"] if direction == "LONG" else data["confirm_short"]
        if not confirm:
            flags.append("Sin 2 velas M5 — ESPERAR (regla dura)")

    if div and direction != "NONE":
        if direction == "LONG" and div.get("type") == "BEARISH":
            flags.append(f"RSI TORYS en contra: {div.get('note', 'divergencia bajista')}")
        if direction == "SHORT" and div.get("type") == "BULLISH":
            flags.append(f"RSI TORYS en contra: {div.get('note', 'divergencia alcista')}")

    return flags


def derive_e1_verdict(
    data: dict,
    categories: dict,
    crt: dict | None = None,
    div: dict | None = None,
    e2: dict | None = None,
) -> str:
    """ENTRAR | ESPERAR | NO_OPERAR según reglas CRT E1.

    La sesión NY ya no fuerza NO_OPERAR aquí (info en header/Categories).
    """
    rules_pct = categories["rules_pct"]
    if rules_pct < 50:
        return "NO_OPERAR"

    s = data["setup"]
    direction = s["direction"]
    flags = collect_red_flags(data, crt, div)

    hard_no = any(
        k in f.lower()
        for f in flags
        for k in ("fakeout pdh", "no long contra", "no short contra", "pending bear", "pending bull")
    )
    if hard_no:
        return "NO_OPERAR"

    if direction != "NONE":
        confirm = data["confirm_long"] if direction == "LONG" else data["confirm_short"]
        if not confirm:
            return "ESPERAR"

    if crt:
        if crt.get("fakeout_pdh") and direction == "LONG":
            return "NO_OPERAR"
        if crt.get("fakeout_pdl") and direction == "SHORT":
            return "ESPERAR"
        if crt.get("pd_reading") == "NEUTRAL" and data["bias_h1"] == "NEUTRAL":
            return "ESPERAR"

    if direction == "NONE" or data["bias_h1"] == "NEUTRAL":
        return "ESPERAR"

    if rules_pct >= 75 and s.get("verdict") == "SETUP_A+":
        return "ENTRAR"
    if rules_pct >= 63:
        return "ESPERAR"
    return "NO_OPERAR" if rules_pct < 50 else "ESPERAR"


def e1_e2_label(e2: dict | None) -> str:
    if e2 and e2.get("verdict") in ("E2_WATCH", "E2_READY"):
        if e2.get("mode_setup") == "reverse" and e2.get("eligible"):
            return "E2 REVERSE operable"
        return "E1 primario | E2 watch only"
    return "E1 primario"


def format_bando_rec_line(categories: dict) -> str:
    """Línea compacta BANDO | REC para tier Light."""
    return (
        f"**BANDO:** {categories.get('bando_usado', 'AUTO')} | "
        f"**REC:** {categories.get('recomendacion', 'n/d')}"
    )


def format_verdict_block(
    verdict: str,
    categories: dict,
    ext_pct: int | None = None,
    e2: dict | None = None,
) -> list[str]:
    sig = label_signal(verdict)
    grade = label_grade(categories["setup_grade"])
    rules = format_rules_cell(
        categories["rules_ok"], categories["rules_total"], categories["rules_pct"], compact=True,
    )
    ext = f" | Extendidas: **{ext_pct}%**" if ext_pct is not None else ""
    return [
        f"## Veredicto: {verdict}",
        "",
        f"**E1/E2:** {e1_e2_label(e2)}",
        f"**Tendencia:** {label_direction(categories['signal_direction'])}",
        f"**Reglas:** {rules}{ext}",
        f"**Calidad:** {grade}",
        f"**Probabilidad histórica:** **{categories['winrate']}** — {categories['winrate_source']}",
        "",
    ]


def format_crt_block(crt: dict | None, data: dict, tier: str) -> list[str]:
    if not crt:
        pdh, pdl, price = data.get("pdh"), data.get("pdl"), data["price"]
        lines = ["### CRT", ""]
        if pdh and pdl:
            if pdl < price < pdh:
                lines.append(f"- PD: dentro rango ({pdl:.0f}–{pdh:.0f}) → **NEUTRAL**, no forzar")
            elif price > pdh:
                lines.append(f"- PD: por encima PDH {pdh:.0f} → sesgo alcista")
            else:
                lines.append(f"- PD: por debajo PDL {pdl:.0f} → sesgo bajista")
        else:
            lines.append("- PD: n/d")
        lines.append("")
        return lines

    if tier == TIER_LIGHT:
        pd_txt = label_crt_pd(crt.get("pd_reading", "n/a"))
        h1_txt = label_crt_h1(crt.get("h1_state", "n/a"))
        fake = []
        if crt.get("fakeout_pdh"):
            fake.append("PDH fakeout — NO long")
        if crt.get("fakeout_pdl"):
            fake.append("PDL fakeout — E2 ctx")
        fake_txt = "; ".join(fake) if fake else "ninguno"
        mid = f"{crt['midpoint']:.0f}" if crt.get("midpoint") else "n/d"
        return [
            "### CRT",
            "",
            f"- PD: {pd_txt} | H1: {h1_txt}",
            f"- 0.5: {crt.get('premium_discount', 'n/a')} (mid {mid}) | Fakeout: {fake_txt}",
            f"- Acción E1: {crt.get('crt_action_e1', 'n/d')}",
            "",
        ]

    lines = [
        "### CRT",
        "",
        "| Item | Valor | Acción E1 |",
        "|------|-------|-----------|",
        f"| PD reading | **{crt['pd_reading']}** | {crt.get('crt_action_e1', '')} |",
        f"| Premium/Discount | {crt.get('premium_discount', 'n/a')} | Long discount / Short premium |",
        f"| H1 state | **{crt.get('h1_state', 'n/a')}** | {crt.get('h1_detail', '')} |",
        f"| Fakeout PDH | {'SÍ — NO LONG' if crt.get('fakeout_pdh') else 'NO'} | CRT invalid bear |",
        f"| Fakeout PDL | {'SÍ — E2 watch' if crt.get('fakeout_pdl') else 'NO'} | Turtle soup ctx |",
    ]
    if data.get("pdh"):
        lines.append(f"| PDH | {data['pdh']:.0f} | Bull si cierre arriba |")
    if data.get("pdl"):
        lines.append(f"| PDL | {data['pdl']:.0f} | Bear si cierre abajo |")
    if crt.get("midpoint"):
        lines.append(f"| 0.5 midpoint | {crt['midpoint']:.0f} | Filtro 50% |")
    if crt.get("fakeout_note"):
        lines += ["", f"**Nota CRT:** {crt['fakeout_note']}", ""]
    else:
        lines.append("")
    return lines


def format_checklist_e1(rules_items: list[tuple[str, bool, str]], tier: str) -> list[str]:
    if tier == TIER_LIGHT:
        return []
    lines = ["### Checklist E1", ""]
    if tier == TIER_FULL:
        lines += ["| Regla | OK | Nota |", "|-------|----|------|"]
        for label, passed, note in rules_items:
            lines.append(f"| {label} | {'✅' if passed else '❌'} | {label_rule_note(note)} |")
    else:
        lines += ["| Regla | OK | Nota |", "|-------|----|------|"]
        for label, passed, note in rules_items:
            lines.append(f"| {label} | {'✅' if passed else '❌'} | {label_rule_note(note)} |")
    lines.append("")
    return lines


def format_e2_block(e2: dict | None, tier: str) -> list[str]:
    if not e2 or tier == TIER_LIGHT:
        return []
    eligible = bool(e2.get("eligible"))
    setup_mode = e2.get("mode_setup", "auto")
    if setup_mode == "reverse":
        operable = "SÍ" if eligible else "NO"
    else:
        operable = "SÍ demo only" if eligible else "NO"
    wr = e2.get("winrate")
    wr_line = f" | Winrate: **{wr}**" if wr else ""
    lines = [
        "### Turtle Soup E2",
        "",
        f"Score **{e2.get('score', 0)}/{e2.get('max', 6)}** | Operable: **{operable}**{wr_line}",
        f"_{e2.get('note', 'E2 watchlist only')}_",
        "",
    ]
    if tier == TIER_HIGH:
        lines += ["| Check | OK | Detalle |", "|-------|----|---------|"]
        for label, ok, detail in e2.get("checks", []):
            lines.append(f"| {label} | {'SÍ' if ok else 'NO'} | {detail} |")
        lines.append("")
    return lines


def format_plan_block(data: dict, verdict: str, tier: str) -> list[str]:
    if verdict != "ENTRAR" or tier == TIER_LIGHT:
        return []
    s = data["setup"]
    lines = ["### Plan (ENTRAR)", ""]
    lines.append(f"- Dirección: **{label_setup_direction(s['direction'])}** @ {data['price']:.0f}")
    if s.get("sl") and s.get("tp"):
        lines += [
            f"- SL estructura: **{s['sl']:.0f}** | TP: **{s['tp']:.0f}** (R:R 1:2)",
            "- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos",
            "- BE en 1:1 | Invalidación: fuera zona / CRT invalid",
        ]
    lines.append("")
    return lines


def format_red_flags_block(flags: list[str], tier: str, max_items: int | None = None) -> list[str]:
    if not flags:
        return ["### Red flags", "", "- Ninguno detectado", ""]
    show = flags if max_items is None else flags[:max_items]
    lines = ["### Red flags", ""]
    lines += [f"- {f}" for f in show]
    if max_items and len(flags) > max_items:
        lines.append(f"- _(+{len(flags) - max_items} más en tier Full/High)_")
    lines.append("")
    return lines


def format_gallery_hint(patterns: list[str] | None, tier: str) -> list[str]:
    if tier != TIER_HIGH or not patterns:
        return []
    return [
        "### Galería (cross-ref)",
        "",
        f"- {label_gallery(patterns[0])}",
        "- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1",
        "",
    ]


def build_report_context(
    data: dict,
    sig: str | None = None,
    crt: dict | None = None,
    div: dict | None = None,
    dmi: dict | None = None,
    e2: dict | None = None,
    gallery_patterns: list[str] | None = None,
) -> dict:
    """Contexto unificado: categories, verdict, flags, extended score."""
    if sig is None:
        from app.models.btc_signal_categories import verdict_to_signal
        sig = verdict_to_signal(data["setup"])
    categories = build_categories(
        data, sig, crt=crt, div=div, dmi=dmi, e2=e2, gallery_patterns=gallery_patterns,
    )
    verdict = derive_e1_verdict(data, categories, crt, div, e2)
    categories["signal_e1"] = verdict
    enrich_categories_bando(categories, data, verdict)
    wr_val, wr_src = winrate_estimate(
        categories["rules_pct"],
        gallery_patterns,
        setup_mode=data.get("mode_setup", "auto"),
    )
    categories["winrate"] = wr_val
    categories["winrate_source"] = wr_src
    if e2 and e2.get("winrate") and data.get("mode_setup") == "reverse":
        categories["winrate"] = e2["winrate"]
        categories["winrate_source"] = e2.get("winrate_source", "histórico E2 reversión")
    ext_pct, _, ext_items = score_extended_rules(data, crt, div, dmi, e2)
    flags = collect_red_flags(data, crt, div)
    _, _, _, rules_items = score_e1_rules_8(data, crt, div, dmi, e2)
    return {
        "categories": categories,
        "verdict": verdict,
        "flags": flags,
        "ext_pct": ext_pct,
        "ext_items": ext_items,
        "rules_items": rules_items,
    }


def format_e1_report(
    data: dict,
    tier: str,
    ctx: dict | None = None,
    crt: dict | None = None,
    div: dict | None = None,
    dmi: dict | None = None,
    e2: dict | None = None,
    gallery_patterns: list[str] | None = None,
) -> list[str]:
    """Genera bloque markdown E1 unificado según tier."""
    if ctx is None:
        ctx = build_report_context(data, crt=crt, div=div, dmi=dmi, e2=e2, gallery_patterns=gallery_patterns)
    categories = ctx["categories"]
    verdict = ctx["verdict"]
    lines: list[str] = []
    lines += format_verdict_block(verdict, categories, ctx["ext_pct"], e2)
    if tier == TIER_LIGHT:
        lines += format_categories_md(categories, compact=True)
    elif tier == TIER_HIGH:
        lines += format_augmented_categories_md(categories, hide_ml=True)
    else:
        lines += format_augmented_categories_md(categories)
    lines += format_crt_block(crt, data, tier)
    lines += format_checklist_e1(ctx["rules_items"], tier)
    lines += format_e2_block(e2, tier)
    lines += format_plan_block(data, verdict, tier)
    max_rf = 4 if tier == TIER_LIGHT else None
    lines += format_red_flags_block(ctx["flags"], tier, max_items=max_rf)
    lines += format_gallery_hint(gallery_patterns, tier)
    return lines
