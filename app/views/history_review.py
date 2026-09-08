"""Resumen tabular History-Review (consola + MD) y entradas scalp."""

from __future__ import annotations



import sys

from typing import Any



from app.models.btc_signal_categories import label_e2_verdict, label_signal

from app.services.ict_entry_scan import format_ict_scan_cell

from app.views.btc_e1_report import e1_e2_label





def resolve_scalp_decimals(data: dict) -> int:

    """Decimales para entradas scalp en history-review."""

    base = int(data.get("price_decimals", 1))

    if data.get("history_mode"):

        return max(base, 2)

    return base





def format_scalp_entries_cell(opt: dict | None, data: dict | None = None) -> str | None:

    """Celda con 1–3 micro-entradas ICT/zona para scalping."""

    if not opt:

        return None

    levels = opt.get("scalp_entries") or []

    if not levels:

        entry = opt.get("entry")

        if entry is None:

            return None

        dec = int(opt.get("dec", resolve_scalp_decimals(data or {})))

        fmt = f".{dec}f"

        src = opt.get("ict_source") or "zona"

        return f"**{entry:{fmt}}** ({src})"

    dec = int(opt.get("dec", resolve_scalp_decimals(data or {})))

    fmt = f".{dec}f"

    parts = []

    for i, row in enumerate(levels[:3], 1):

        price, src = row[0], row[1]

        parts.append(f"{i}) **{float(price):{fmt}}** ({src})")

    return " · ".join(parts)





def format_plan_high_cell(opt: dict | None, data: dict | None = None) -> str:
    """Entry / SL / TP para tabla unificada High."""
    if not opt or (opt.get("entry") is None and opt.get("user_entry") is None):
        return "n/d"
    dec = int(opt.get("dec", (data or {}).get("price_decimals", 1)))
    fmt = f".{dec}f"
    entry = opt.get("user_entry") if opt.get("user_entry") is not None else opt.get("entry")
    sl = opt.get("sl")
    tp = opt.get("tp")
    sl_s = f"{float(sl):{fmt}}" if sl is not None else "n/d"
    tp_s = f"{float(tp):{fmt}}" if tp is not None else "n/d"
    tag = " · plan usuario" if opt.get("user_entry") is not None else ""
    return f"Entry **{float(entry):{fmt}}** · SL **{sl_s}** · TP **{tp_s}**{tag}"


def format_metrics_high_cell(cats: dict) -> str:
    """Rules / Neural / ML / Confluencia / Fusion para tabla High."""
    parts: list[str] = []
    rules = cats.get("rules_pct", 0)
    parts.append(f"Rules **{rules}%**")
    if cats.get("neural_prob_win") is not None:
        nw = float(cats["neural_prob_win"]) * 100
        parts.append(f"Neural **{nw:.0f}%**")
    if cats.get("ml_prob_win") is not None:
        ml = float(cats["ml_prob_win"]) * 100
        parts.append(f"ML **{ml:.1f}%**")
    conf = cats.get("confluencia_setup", "n/d")
    detail = cats.get("confluencia_detalle", "")
    conf_part = f"Confluencia **{conf}**"
    if detail:
        conf_part += f" — {detail}"
    parts.append(conf_part)
    if cats.get("fusion_score") is not None:
        parts.append(f"Fusion **{cats['fusion_score']}%**")
    return " · ".join(parts)


def format_e2_break_cell(data: dict, e2: dict | None) -> str:
    """E2 / Break para tabla High."""
    setup_mode = (data.get("mode_setup") or "auto").lower()
    e2 = e2 or {}
    e2_txt = label_e2_verdict(e2.get("verdict", "E2_NO"))
    base = f"{e2_txt} — {e1_e2_label(e2)}"
    if setup_mode == "break":
        return f"BREAK / E1 — {base}"
    if setup_mode == "reverse":
        return f"REVERSE / E2 — {base}"
    return base


def format_historial_ref_cell(reflection: dict, cats: dict) -> str | None:
    """Última señal + calificación (referencia historial)."""
    ultima = cats.get("ultima_senal_entrada") or reflection.get("cell_ultima")
    if not ultima:
        return None
    calif = (
        cats.get("calificacion_entrada")
        or cats.get("vs_ultima_entrada")
        or reflection.get("cell_calificacion")
        or reflection.get("cell_vs")
    )
    if calif:
        return f"{ultima} · {calif}"
    return ultima


def build_high_summary_rows(
    data: dict,
    ctx: dict,
    opt: dict,
    reflection: dict,
    *,
    chart_pub: dict | None = None,
) -> list[tuple[str, str]]:
    """Filas (sección, detalle) para tabla única High (no history-review)."""
    cats = ctx.get("categories") or {}
    e2 = data.get("e2") or {}
    verdict = ctx.get("verdict", "ESPERAR")
    direction = data.get("setup", {}).get("direction", "NONE")
    dec = int(opt.get("dec", data.get("price_decimals", 1)))
    fmt = f".{dec}f"
    price = data.get("price")
    price_s = cats.get("precio") or (f"{float(price):{fmt}}" if price is not None else "n/d")

    ict = (
        format_ict_scan_cell(opt)
        or cats.get("ict_scan")
        or opt.get("ict_note")
        or "sin ICT"
    )

    rows: list[tuple[str, str]] = [
        ("Precio", f"**{price_s}**"),
        ("Veredicto", f"**{label_signal(verdict)}** ({direction})"),
        ("Entrada óptima", f"**{cats.get('entrada_optima', 'n/d')}**"),
    ]
    if cats.get("entry_usuario"):
        rows.append(("Entry usuario", f"**{cats['entry_usuario']}**"))
    rows.append(("ICT", ict))
    rows.append(("Plan", format_plan_high_cell(opt, data)))
    rows.append(("E2 / Break", format_e2_break_cell(data, e2)))
    rows.append(("Métricas", format_metrics_high_cell(cats)))

    hist_ref = format_historial_ref_cell(reflection, cats)
    if hist_ref:
        rows.append(("Historial ref", hist_ref))

    if cats.get("bando_usado"):
        rows.append(("Bando usado (lado asumido)", f"**{cats['bando_usado']}**"))
        rows.append(("Bando mercado (H1)", f"**{cats.get('bando_mercado', 'NEUTRAL')}**"))

    if cats.get("advanced") and cats.get("advanced_rows"):
        for label, value in cats["advanced_rows"]:
            rows.append((label, value))

    rows.append(("Chart", _chart_summary_cell(chart_pub, data)))
    return rows


def format_plan_scalp_cell(opt: dict | None, data: dict | None = None) -> str:

    """Entry / SL / TP referencia scalp (no señal nueva)."""

    if not opt or opt.get("entry") is None:

        return "n/d"

    dec = int(opt.get("dec", resolve_scalp_decimals(data or {})))

    fmt = f".{dec}f"

    entry = float(opt["entry"])

    sl = opt.get("sl")

    tp = opt.get("tp")

    sl_s = f"{float(sl):{fmt}}" if sl is not None else "n/d"

    tp_s = f"{float(tp):{fmt}}" if tp is not None else "n/d"

    zone = opt.get("opti_zone") or "n/d"

    return f"Entry **{entry:{fmt}}** · SL **{sl_s}** · TP **{tp_s}** · zona {zone}"





def _chart_summary_cell(

    chart_pub: dict | None,

    data: dict,

) -> str:

    """Celda Chart sin rutas de archivo (preview en navegador)."""

    if chart_pub and chart_pub.get("ok"):

        return "**Preview en navegador**"

    if data.get("annotated_chart_file") or data.get("annotated_chart_abs"):

        return "**Preview en navegador**"

    return "—"





def build_history_summary_rows(

    data: dict,

    ctx: dict,

    opt: dict,

    reflection: dict,

    *,

    chart_pub: dict | None = None,

) -> list[tuple[str, str]]:

    """Filas (sección, detalle) para tabla única History-Review.



    Unifica Categories + Resumen (sin duplicar Plan/ICT/E2/Métricas/Historial/Chart).

    """

    cats = ctx.get("categories") or {}

    e2 = data.get("e2") or {}

    verdict = ctx.get("verdict", "ESPERAR")

    direction = data.get("setup", {}).get("direction", "NONE")

    dec = int(opt.get("dec", resolve_scalp_decimals(data)))

    fmt = f".{dec}f"

    price = data.get("price")

    price_s = cats.get("precio") or (f"{float(price):{fmt}}" if price is not None else "n/d")



    ict = (

        format_ict_scan_cell(opt)

        or cats.get("ict_scan")

        or opt.get("ict_note")

        or "sin ICT"

    )

    e2_txt = label_e2_verdict(e2.get("verdict", "E2_NO")) if e2 else "n/d"

    e2_line = f"{e2_txt} — {e1_e2_label(e2)}"



    rules = cats.get("rules_pct", 0)

    conf = cats.get("confluencia_setup", "n/d")

    detail = cats.get("confluencia_detalle", "")

    metrics = f"Rules **{rules}%** · Confluencia **{conf}**"

    if detail:

        metrics += f" — {detail}"



    rev = (

        reflection.get("cell_revision")

        or cats.get("revision_ultima_entry")

        or cats.get("ultima_senal_entrada")

        or "—"

    )

    pnl = reflection.get("cell_pnl") or cats.get("pnl_vs_precio") or "—"

    calif = (

        reflection.get("cell_calificacion")

        or cats.get("calificacion_entrada")

        or cats.get("vs_ultima_entrada")

        or "—"

    )



    scalp = format_scalp_entries_cell(opt, data) or cats.get("entradas_scalp") or "n/d"

    plan = format_plan_scalp_cell(opt, data)

    if plan == "n/d" and cats.get("plan_scalp"):

        plan = cats["plan_scalp"]



    rows: list[tuple[str, str]] = [

        ("Precio", f"**{price_s}**"),

        ("Veredicto", f"**{label_signal(verdict)}** ({direction})"),

    ]



    if rev and rev != "—":

        rows.append(("Revisión última Entry", rev))

    if pnl and pnl != "—":

        rows.append(("P&L vs precio actual", pnl))

    if calif and calif != "—":

        rows.append(("Calificación Entry", calif))



    rows.extend([

        ("ICT", ict),

        ("Plan scalp (ref.)", plan),

        ("Entradas scalp", scalp),

        ("E2", e2_line),

    ])



    if cats.get("bando_usado"):

        rows.append(("Bando usado (lado asumido)", f"**{cats['bando_usado']}**"))

        rows.append(("Bando mercado (H1)", f"**{cats.get('bando_mercado', 'NEUTRAL')}**"))



    if cats.get("neural_prob_win") is not None:

        nw = float(cats["neural_prob_win"]) * 100

        align_note = (

            "alineado con patrones WIN desktop"

            if cats.get("neural_gallery_aligned")

            else "baja similitud con galería WIN"

        )

        rows.append(

            (

                "Neural galería",

                f"**{nw:.0f}% WIN** — grade **{cats.get('neural_grade', '?')}** "

                f"({align_note}; conf. {cats.get('neural_confidence', '?')})",

            )

        )



    rows.append(("Métricas", metrics))



    if cats.get("advanced") and cats.get("advanced_rows"):

        for label, value in cats["advanced_rows"]:

            rows.append((label, value))



    rows.append(("Chart", _chart_summary_cell(chart_pub, data)))

    return rows





_CONSOLE_REPLACEMENTS: tuple[tuple[str, str], ...] = (

    ("\u2192", "->"),

    ("\u2190", "<-"),

    ("\u2191", "^"),

    ("\u2193", "v"),

    ("\u2014", "-"),

    ("\u2013", "-"),

    ("\u00b7", "."),

    ("\u26a0\ufe0f", "!"),

    ("\u26a0", "!"),

    ("\u2705", "OK"),

    ("\u274c", "X"),

    ("\u2753", "?"),

)





def _console_safe(text: str) -> str:

    """Texto seguro para consola Windows (cp1252/charmap sin Unicode problemático)."""

    for old, new in _CONSOLE_REPLACEMENTS:

        text = text.replace(old, new)

    enc = getattr(sys.stdout, "encoding", None) or "utf-8"

    try:

        text.encode(enc)

    except (UnicodeEncodeError, LookupError):

        return text.encode("ascii", errors="replace").decode("ascii")

    return text





def _console_print(*parts: str, **kwargs: Any) -> None:

    print(*(_console_safe(p) for p in parts), **kwargs)





def format_history_summary_md(rows: list[tuple[str, str]]) -> list[str]:

    lines = [

        "## Resumen History-Review",

        "",

        "> Tabla única — revisión P&L + referencia scalp (no señal nueva).",

        "",

        "| Sección | Detalle |",

        "|---------|---------|",

    ]

    for label, value in rows:

        lines.append(f"| {label} | {value} |")

    lines += ["", "---", ""]

    return lines





def print_history_summary_console(rows: list[tuple[str, str]]) -> None:

    """Imprime tabla markdown unificada en consola."""

    _console_print("")

    _console_print("## Resumen History-Review")

    _console_print("")

    _console_print("| Seccion | Detalle |")

    _console_print("|---------|---------|")

    for label, value in rows:

        _console_print(f"| {label} | {value} |")

    _console_print("")





def finalize_history_chart(

    data: dict,

    *,

    asset: str,

    annotated_abs: str | None,

    signal_id: str | None = None,

    mode: str = "history_review",

) -> dict[str, Any]:

    """Publica chart a live/latest + archive y guarda meta en data."""

    if not annotated_abs:

        return {}

    from app.views.chart_archive import publish_annotated_chart



    pub = publish_annotated_chart(

        asset,

        annotated_abs,

        signal_id=signal_id,

        mode=mode,

    )

    if pub.get("ok"):

        data["chart_archive"] = pub

    return pub





def format_high_summary_md(rows: list[tuple[str, str]]) -> list[str]:
    lines = [
        "## Resumen High",
        "",
        "> Tabla única — señal High (Categories + plan + métricas).",
        "",
        "| Sección | Detalle |",
        "|---------|---------|",
    ]
    for label, value in rows:
        lines.append(f"| {label} | {value} |")
    lines += ["", "---", ""]
    return lines


def print_high_summary_console(rows: list[tuple[str, str]]) -> None:
    """Imprime tabla markdown unificada High en consola."""
    _console_print("")
    _console_print("## Resumen High")
    _console_print("")
    _console_print("| Seccion | Detalle |")
    _console_print("|---------|---------|")
    for label, value in rows:
        _console_print(f"| {label} | {value} |")
    _console_print("")


def publish_history_preview(

    data: dict,

    rows: list[tuple[str, str]],

    *,

    asset: str,

    no_open: bool = False,

    title: str | None = None,

) -> dict[str, Any]:

    """Genera HTML preview y opcionalmente abre el navegador predeterminado."""

    from app.views.chart_archive import open_preview_in_browser, write_chart_preview_html



    pub = data.get("chart_archive") or {}

    png_abs = pub.get("latest_abs") or data.get("annotated_chart_abs")

    if not png_abs:

        return {"ok": False, "error": "no chart"}



    preview_title = title or f"{asset} History-Review"

    preview = write_chart_preview_html(

        png_abs,

        rows,

        asset=asset,

        title=preview_title,

    )

    if not preview.get("ok"):

        return preview



    data["chart_preview"] = preview

    if pub.get("ok"):

        pub["preview_rel"] = preview["preview_rel"]

        pub["preview_abs"] = preview["preview_abs"]



    if not no_open:

        preview["opened"] = open_preview_in_browser(preview["preview_abs"])

    return preview





def finish_history_review_output(

    data: dict,

    rows: list[tuple[str, str]] | None,

    *,

    asset: str,

    no_open: bool = False,

) -> None:

    """Consola: tabla unificada + preview en navegador (sin rutas de archivo)."""

    if rows:

        print_history_summary_console(rows)

    has_chart = bool(

        (data.get("chart_archive") or {}).get("ok")

        or data.get("annotated_chart_abs")

        or data.get("annotated_chart_file")

    )

    if not has_chart or not rows:

        return



    preview = publish_history_preview(data, rows, asset=asset, no_open=no_open)

    if preview.get("ok") and preview.get("opened"):

        _console_print("Preview abierto en navegador.")

    elif preview.get("ok") and no_open:

        _console_print("Preview generado (sin abrir: --no-open).")

    elif preview.get("ok"):

        _console_print("Preview generado (no se pudo abrir el navegador).")





def finish_high_output(
    data: dict,
    rows: list[tuple[str, str]] | None,
    *,
    asset: str,
    no_open: bool = False,
) -> None:
    """Consola: tabla unificada High + preview en navegador (sin rutas de archivo)."""
    if rows:
        print_high_summary_console(rows)
    has_chart = bool(
        (data.get("chart_archive") or {}).get("ok")
        or data.get("annotated_chart_abs")
        or data.get("annotated_chart_file")
    )
    if not has_chart or not rows:
        return

    preview = publish_history_preview(
        data, rows, asset=asset, no_open=no_open, title=f"{asset} High",
    )
    if preview.get("ok") and preview.get("opened"):
        _console_print("Preview abierto en navegador.")
    elif preview.get("ok") and no_open:
        _console_print("Preview generado (sin abrir: --no-open).")
    elif preview.get("ok"):
        _console_print("Preview generado (no se pudo abrir el navegador).")


def print_chart_access_block(data: dict) -> None:

    """Compat: delega en finish_history_review_output sin filas (solo preview)."""

    finish_history_review_output(data, None, asset=data.get("asset_label", "BTC"))


