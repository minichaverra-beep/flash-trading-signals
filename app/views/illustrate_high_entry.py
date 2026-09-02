"""Generate annotated M5 chart for high-signal optimal entry (2M5 + zona + Entry/SL/TP)."""
from __future__ import annotations

from pathlib import Path


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


def _callout_text(opt: dict) -> str:
    """Spanish callout: ESPERAR retest vs ENTRAR OPTI."""
    near = bool(opt.get("ahora_near"))
    confirm = str(opt.get("ahora_2m5", "")).lower().startswith("sí") or str(
        opt.get("ahora_2m5", "")
    ).lower().startswith("si")
    action = str(opt.get("ahora_action", "ESPERAR"))
    if "ENTRAR" in action.upper() and near and confirm:
        return "2M5 OK en zona → ENTRAR"
    if confirm and not near:
        dist = opt.get("ahora_dist", "n/d")
        return f"2R lejos zona ({dist}) → ESPERAR retest"
    if near and not confirm:
        return "En zona sin 2M5 → ESPERAR confirmación"
    return "Sin setup → ESPERAR"


def _candle_label(c: dict) -> str:
    return "G" if c["close"] >= c["open"] else "R"


def create_annotated_entry_chart(
    data: dict,
    optimal_entry: dict,
    out_path: Path | str,
    asset: str = "BTC",
) -> Path:
    """
    Draw M5 candles with last-2 highlight, S/R zone, Entry/SL/TP and ESPERAR/ENTRAR callout.

    Writes PNG to out_path. Uses matplotlib (same dark style as live M5 charts).
    """
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch, Rectangle

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    m5 = data.get("m5") or []
    if len(m5) < 2:
        # Minimal placeholder so callers/tests still get a file
        fig, ax = plt.subplots(figsize=(8, 3), facecolor="#1e1e1e")
        ax.set_facecolor("#1e1e1e")
        ax.set_title(f"{asset} M5 — sin velas para ilustrar", color="#569cd6")
        fig.savefig(out, dpi=100, facecolor="#1e1e1e")
        plt.close(fig)
        return out

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

    fig, ax = plt.subplots(figsize=(12, 5.5), facecolor="#1e1e1e")
    ax.set_facecolor("#1e1e1e")

    for i, c in enumerate(show):
        color = "#4ec9b0" if c["close"] >= c["open"] else "#f48771"
        ax.plot([i, i], [c["low"], c["high"]], color=color, linewidth=0.8)
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
    yrange = (y_hi - y_lo) or abs(show[-1]["close"]) * 0.01
    off = yrange * 0.025

    if level is not None:
        ax.axhline(level, color="#c586c0", linewidth=1.5, linestyle="-", alpha=0.9)
        ax.text(
            n - 0.5, level + off,
            f"{ztype} {level:{fmt}}",
            color="#c586c0", fontsize=9, va="bottom", fontweight="bold",
        )
    if zone_lo is not None and level is not None and abs(zone_lo - level) > 1e-9:
        edge = zone_lo if direction == "SHORT" else zone_hi
        if edge is not None:
            ax.axhline(edge, color="#c586c0", linewidth=1, linestyle=":", alpha=0.7)
    if entry is not None:
        ax.axhline(entry, color="#4fc1ff", linewidth=1, linestyle="--", alpha=0.85)
        ax.text(2, entry + off, f"Entrada OPTI ~{entry:{fmt}}", color="#4fc1ff", fontsize=9, va="bottom")
    if sl is not None:
        ax.axhline(sl, color="#f44747", linewidth=1, linestyle="--", alpha=0.85)
        ax.text(2, sl + off, f"SL ~{sl:{fmt}}", color="#f44747", fontsize=9, va="bottom")
    if tp is not None:
        ax.axhline(tp, color="#6a9955", linewidth=1, linestyle="--", alpha=0.85)
        ax.text(2, tp - off, f"TP 1:2 ~{tp:{fmt}}", color="#6a9955", fontsize=9, va="top")

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
    ax.tick_params(colors="#e0e0e0")
    for spine in ax.spines.values():
        spine.set_color("#3e3e42")
    ax.set_ylabel(asset, color="#e0e0e0")
    fig.tight_layout()
    fig.savefig(out, dpi=140, facecolor="#1e1e1e")
    plt.close(fig)
    return out


def format_illustration_md(annotated_file: str) -> list[str]:
    """Markdown section with relative image link (for live/*.md)."""
    name = Path(annotated_file).name
    return [
        "## Ilustración entrada (2M5 + óptima)",
        "",
        f"![annotated]({name})",
        "",
        "---",
        "",
    ]
