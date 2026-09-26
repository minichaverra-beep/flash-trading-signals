"""Generate annotated M5 chart for high-signal optimal entry (2M5 + zona + Entry/SL/TP)."""
from __future__ import annotations

import io
import os
import tempfile
import time
from pathlib import Path

CHART_DPI = 200
CHART_DPI_PLACEHOLDER = 120


def savefig_png(
    fig,
    out_path: Path | str,
    *,
    dpi: int = 140,
    facecolor: str = "#1e1e1e",
) -> Path:
    """
    Save a matplotlib figure as PNG robustly on Windows.

    Avoids common [Errno 22] Invalid argument failures by:
    - rendering via BytesIO (matplotlib never opens the final path)
    - writing a same-dir temp file then os.replace (atomic, handles locked viewers)
    - one retry after a short sleep, then fallback ``*_new.png``
    """
    out = Path(out_path)
    # Trailing/leading spaces in the filename break Win32 CreateFile
    out = out.parent / out.name.strip()
    out.parent.mkdir(parents=True, exist_ok=True)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, facecolor=facecolor)
    payload = buf.getvalue()

    def _atomic_write(target: Path) -> None:
        fd, tmp_name = tempfile.mkstemp(suffix=".png.tmp", prefix=f".{target.stem}_", dir=str(target.parent))
        try:
            with os.fdopen(fd, "wb") as fh:
                fh.write(payload)
                fh.flush()
                os.fsync(fh.fileno())
            os.replace(tmp_name, target)
        except Exception:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass
            raise

    try:
        _atomic_write(out)
        return out
    except OSError:
        time.sleep(0.2)
        try:
            _atomic_write(out)
            return out
        except OSError:
            alt = out.with_name(f"{out.stem}_new{out.suffix or '.png'}")
            _atomic_write(alt)
            return alt


def _zone_edges(opt: dict) -> tuple[float | None, float | None]:
    """Return (zone_lo, zone_hi) from optimal entry; recompute if missing."""
    lo, hi = opt.get("zone_lo"), opt.get("zone_hi")
    if lo is not None and hi is not None:
        return float(lo), float(hi)
    level = opt.get("level")
    direction = opt.get("direction")
    if not level or direction not in ("LONG", "SHORT"):
        return None, None
    if direction == "SHORT":
        return level * (1 - 0.0015), float(level)
    return float(level), level * (1 + 0.0015)


def _rr_tag(opt: dict, entry: float | None, sl: float | None, tp: float | None) -> str:
    """Label fragment with realized R:R (not a hard-coded 1:2 lie)."""
    from app.models.market_pips import actual_rr

    rr = actual_rr(entry, sl, tp)
    if rr is None:
        rr = opt.get("rr")
    if rr is None:
        return ""
    src = opt.get("sl_tp_source")
    if src == "past" and opt.get("tp_source") == "past_structure":
        return f"past 1:{rr:.1f}"
    if src == "past":
        return f"1:{rr:.1f} past"
    return f"1:{rr:.1f}"


def _place_level_labels(
    ax,
    levels: list[tuple[float, str, str]],
    *,
    x: float,
    yrange: float,
    fontsize: int,
) -> None:
    """Right-side labels stacked so TP/Entry/SL never sit on top of each other."""
    if not levels:
        return
    # Sort high→low; nudge label y when two prices are closer than ~3% of range
    ordered = sorted(levels, key=lambda t: t[0], reverse=True)
    min_gap = max(yrange * 0.04, 1e-6)
    placed_y: list[float] = []
    for price, text, color in ordered:
        y = float(price)
        for prev in placed_y:
            if abs(y - prev) < min_gap:
                y = prev - min_gap
        placed_y.append(y)
        ax.text(
            x, y, text,
            color=color, fontsize=fontsize, va="center", ha="left",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="#1e1e1e", edgecolor=color, alpha=0.85),
        )


def _callout_text(opt: dict) -> str:
    """Spanish callout: ESPERAR confirmación vs ENTRAR (zona no fuerza wait)."""
    confirm = str(opt.get("ahora_2m5", "")).lower().startswith("sí") or str(
        opt.get("ahora_2m5", "")
    ).lower().startswith("si")
    action = str(opt.get("ahora_action", "ESPERAR"))
    if "ENTRAR" in action.upper() and confirm:
        return "2M5 OK → ENTRAR"
    if "ENTRAR" in action.upper():
        return "Setup listo → ENTRAR"
    if confirm:
        return "2M5 OK · revisar bias/SL"
    return "Sin 2M5 → ESPERAR confirmación"


def _candle_label(c: dict) -> str:
    return "G" if c["close"] >= c["open"] else "R"


def write_entry_overlay_charts(
    data: dict,
    optimal_entry: dict,
    *,
    asset: str = "BTC",
    main_chart_path: Path | str | None = None,
    annotated_path: Path | str | None = None,
    dpi: int | None = None,
) -> dict:
    """
    Write OPTI/SL/TP/S-R overlays onto the default High chart and/or the -Ilustrate PNG.

    - main_chart_path: live/*_m5_chart.png (when chart enabled / not -NoChart)
    - annotated_path: live/*_m5_chart_annotated.png (when -Ilustrate)
    """
    out: dict = {}
    chart_dpi = dpi if dpi is not None else CHART_DPI
    if main_chart_path is not None:
        p = create_annotated_entry_chart(
            data, optimal_entry, main_chart_path, asset=asset, dpi=chart_dpi,
        )
        out["main_chart"] = str(p.resolve())
    if annotated_path is not None:
        p = create_annotated_entry_chart(
            data, optimal_entry, annotated_path, asset=asset, dpi=chart_dpi,
        )
        out["annotated_chart"] = str(p.resolve())
        out["annotated_file"] = Path(annotated_path).name
    return out


def create_annotated_entry_chart(
    data: dict,
    optimal_entry: dict,
    out_path: Path | str,
    asset: str = "BTC",
    *,
    dpi: int = CHART_DPI,
) -> Path:
    """
    Draw M5 candles with last-2 highlight, S/R zone, Entry/SL/TP and ESPERAR/ENTRAR callout.

    Writes PNG to out_path. Uses matplotlib Agg + atomic replace (Windows-safe).
    Used for the default High chart (when chart enabled) and for -Ilustrate.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch, Rectangle

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    m5 = data.get("m5") or []
    fig = None
    try:
        if len(m5) < 2:
            # Minimal placeholder so callers/tests still get a file
            fig, ax = plt.subplots(figsize=(8, 3), facecolor="#1e1e1e")
            ax.set_facecolor("#1e1e1e")
            ax.set_title(f"{asset} M5 — sin velas para ilustrar", color="#569cd6")
            return savefig_png(fig, out, dpi=CHART_DPI_PLACEHOLDER, facecolor="#1e1e1e")

        show = m5[-60:]
        n = len(show)
        opt = optimal_entry or {}
        dec = int(opt.get("dec", data.get("price_decimals", 1)))
        fmt = f".{dec}f"
        direction = opt.get("direction") or data.get("setup", {}).get("direction", "")
        level = opt.get("level")
        ztype = opt.get("ztype") or data.get("zone", {}).get("type", "zona")
        zone_lo, zone_hi = _zone_edges(opt)
        entry, sl, tp = opt.get("entry"), opt.get("sl"), opt.get("tp")
        user_entry = opt.get("user_entry")
        scalp_entries = opt.get("scalp_entries") or []

        fig_w = 14 if dpi >= 180 else 12
        fig_h = 6.5 if dpi >= 180 else 5.5
        fig, ax = plt.subplots(figsize=(fig_w, fig_h), facecolor="#1e1e1e")
        ax.set_facecolor("#1e1e1e")
        lw_candle = 1.0 if dpi >= 180 else 0.8
        lw_zone = 2.0 if dpi >= 180 else 1.5
        fs_label = 10 if dpi >= 180 else 9

        for i, c in enumerate(show):
            color = "#4ec9b0" if c["close"] >= c["open"] else "#f48771"
            ax.plot([i, i], [c["low"], c["high"]], color=color, linewidth=lw_candle)
            bottom = min(c["open"], c["close"])
            height = abs(c["close"] - c["open"]) or (c["high"] - c["low"]) * 0.01
            ax.add_patch(Rectangle((i - 0.3, bottom), 0.6, height, facecolor=color, edgecolor=color))

        # Yellow boxes on last 2 M5 candles
        for idx in (n - 2, n - 1):
            c = show[idx]
            pad = (c["high"] - c["low"]) * 0.05 or abs(c["close"]) * 0.0001
            ax.add_patch(
                Rectangle(
                    (idx - 0.42, c["low"] - pad),
                    0.84,
                    (c["high"] - c["low"]) + 2 * pad,
                    linewidth=2.5,
                    edgecolor="#ffd700",
                    facecolor="none",
                    linestyle="--",
                )
            )

        y_lo = min(c["low"] for c in show)
        y_hi = max(c["high"] for c in show)
        # Include Entry/SL/TP/zone so daytrader levels are never clipped off-chart
        for v in (level, entry, sl, tp, user_entry, zone_lo, zone_hi):
            if v is not None:
                y_lo = min(y_lo, float(v))
                y_hi = max(y_hi, float(v))
        for sc_e, _sc_src in scalp_entries[:3]:
            y_lo = min(y_lo, float(sc_e))
            y_hi = max(y_hi, float(sc_e))
        yrange = (y_hi - y_lo) or abs(show[-1]["close"]) * 0.01
        pad_y = yrange * 0.06
        ax.set_ylim(y_lo - pad_y, y_hi + pad_y)
        off = yrange * 0.025

        label_items: list[tuple[float, str, str]] = []
        label_x = n + 0.6

        if level is not None:
            ax.axhline(level, color="#c586c0", linewidth=lw_zone, linestyle="-", alpha=0.9)
            label_items.append((float(level), f"{ztype} {level:{fmt}}", "#c586c0"))
        if zone_lo is not None and level is not None and abs(zone_lo - level) > 1e-9:
            edge = zone_lo if direction == "SHORT" else zone_hi
            if edge is not None:
                ax.axhline(edge, color="#c586c0", linewidth=1, linestyle=":", alpha=0.7)
        if entry is not None:
            ax.axhline(entry, color="#4fc1ff", linewidth=1.2, linestyle="--", alpha=0.9)
            label_items.append((float(entry), f"Entrada OPTI {entry:{fmt}}", "#4fc1ff"))
        for idx, (sc_e, sc_src) in enumerate(scalp_entries[:3]):
            if entry is not None and abs(float(sc_e) - float(entry)) < 10 ** (-dec):
                continue
            ax.axhline(sc_e, color="#9cdcfe", linewidth=0.9, linestyle=":", alpha=0.75)
            label_items.append(
                (float(sc_e), f"Scalp {idx + 1} {float(sc_e):{fmt}}", "#9cdcfe"),
            )
        if user_entry is not None:
            same = entry is not None and abs(float(user_entry) - float(entry)) < 10 ** (-dec)
            if not same:
                ax.axhline(user_entry, color="#dcdcaa", linewidth=1.2, linestyle="-.", alpha=0.9)
                label_items.append(
                    (float(user_entry), f"Entry usuario {user_entry:{fmt}}", "#dcdcaa"),
                )
            elif entry is None:
                ax.axhline(user_entry, color="#dcdcaa", linewidth=1.2, linestyle="-.", alpha=0.9)
                label_items.append(
                    (float(user_entry), f"Entry usuario {user_entry:{fmt}}", "#dcdcaa"),
                )
        rr_lbl = _rr_tag(opt, entry if user_entry is None else user_entry, sl, tp)
        who = " usuario" if user_entry is not None else ""
        if sl is not None:
            ax.axhline(sl, color="#f44747", linewidth=1, linestyle="--", alpha=0.85)
            sl_txt = f"SL{who} {sl:{fmt}}" + (f" · {rr_lbl}" if rr_lbl and tp is None else "")
            label_items.append((float(sl), sl_txt, "#f44747"))
        if tp is not None:
            ax.axhline(tp, color="#6a9955", linewidth=1, linestyle="--", alpha=0.85)
            tp_txt = f"TP{who} {rr_lbl} {tp:{fmt}}".replace("  ", " ").strip()
            label_items.append((float(tp), tp_txt, "#6a9955"))

        _place_level_labels(ax, label_items, x=label_x, yrange=yrange, fontsize=fs_label)
        ax.set_xlim(-0.5, n + 8)
        callout = _callout_text(opt)
        last = show[-1]
        anchor_y = level - off * 3 if level is not None else last["close"]
        ax.add_patch(
            FancyArrowPatch(
                (n - 3, anchor_y),
                (n - 1.5, last["close"]),
                arrowstyle="->",
                color="#ffd700",
                linewidth=2,
                mutation_scale=14,
            )
        )
        ax.text(
            max(n - 10, 1),
            anchor_y - off,
            callout,
            color="#ffd700",
            fontsize=9,
            ha="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#2d2d30", edgecolor="#ffd700", alpha=0.9),
        )

        c0, c1 = show[-2], show[-1]
        t0 = c0["open_time"].strftime("%H:%M") if hasattr(c0.get("open_time"), "strftime") else "?"
        t1 = c1["open_time"].strftime("%H:%M") if hasattr(c1.get("open_time"), "strftime") else "?"
        colors = f"[{_candle_label(c0)}][{_candle_label(c1)}]"
        ax.text(
            n - 2, show[-2]["low"] - off * 2,
            f"2M5 [{t0}]+[{t1}] {colors}",
            color="#ffd700", fontsize=8, ha="center",
        )

        gen = data.get("generated", "")
        title = f"{asset} M5 · {gen} UTC · 2M5 + entrada óptima"
        ax.set_title(title, color="#569cd6", fontsize=12, fontweight="bold")

        # Nota Zentinel (killzones NY + presets) — subtítulo corto, sin saturar
        try:
            from app.models.zentinel_presets import zentinel_chart_note

            note = zentinel_chart_note(asset, data.get("session"))
            ax.text(
                0.5, 1.02, note,
                transform=ax.transAxes,
                color="#808080", fontsize=7, ha="center", va="bottom",
            )
            ses = data.get("session") or {}
            if ses.get("in_ny_window"):
                ax.text(
                    0.01, 0.98,
                    f"KZ {ses.get('window', 'NY')}",
                    transform=ax.transAxes,
                    color="#4ec9b0", fontsize=8, va="top",
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="#2d2d30", edgecolor="#4ec9b0", alpha=0.85),
                )
        except Exception:
            pass

        ax.tick_params(colors="#e0e0e0")
        for spine in ax.spines.values():
            spine.set_color("#3e3e42")
        ax.set_ylabel(asset, color="#e0e0e0")
        fig.tight_layout()
        return savefig_png(fig, out, dpi=dpi, facecolor="#1e1e1e")
    finally:
        if fig is not None:
            plt.close(fig)


def format_illustration_md(
    annotated_file: str,
    *,
    absolute_path: str | Path | None = None,
) -> list[str]:
    """Markdown: chart link relativo a live/ + rutas fáciles de abrir (sin base64)."""
    name = Path(annotated_file).name
    rel = f"live/{name}"
    lines = [
        "## Ilustración entrada (2M5 + óptima)",
        "",
        f"![chart]({name})",
        "",
        "### Salidas (chart)",
        "",
        f"- **Abrir (relativo):** `{rel}`",
        f"- **Markdown:** `![chart]({name})` (desde `live/`)",
    ]
    if absolute_path:
        abs_s = str(Path(absolute_path).resolve())
        lines.append(f"- **Ruta absoluta:** `{abs_s}`")
    lines += ["", "---", ""]
    return lines


def format_salidas_block(
    *,
    signal_md: str | Path | None = None,
    annotated_file: str | None = None,
    annotated_abs: str | Path | None = None,
) -> list[str]:
    """Bloque Salidas al final del reporte: paths clickable-friendly para chat/Cursor."""
    lines = [
        "## Salidas",
        "",
    ]
    if signal_md:
        sp = Path(signal_md)
        rel = f"live/{sp.name}" if sp.name else str(signal_md)
        lines.append(f"- **Reporte:** `{rel}`")
        try:
            lines.append(f"- **Reporte (abs):** `{sp.resolve()}`")
        except OSError:
            lines.append(f"- **Reporte (abs):** `{signal_md}`")
    if annotated_file:
        name = Path(annotated_file).name
        rel = f"live/{name}"
        lines.append(f"- **Chart anotado:** `{rel}`")
        lines.append(f"- **Preview:** `![chart]({name})`")
        if annotated_abs:
            try:
                lines.append(f"- **Chart (abs):** `{Path(annotated_abs).resolve()}`")
            except OSError:
                lines.append(f"- **Chart (abs):** `{annotated_abs}`")
        else:
            lines.append(f"- **Chart (abs):** _(mismo folder que el MD · `{rel}`)_")
    if len(lines) <= 2:
        return []
    lines.append("")
    return lines
