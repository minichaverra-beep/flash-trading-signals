"""Gráfico M5 estilo "Long/Short Position" (TradingView), compartido por BTC / US30 / XAUUSD.

- Eje X en hora real (UTC + hora Nueva York), ventana intradía + espacio a la derecha.
- Caja de posición desde la vela actual: verde entrada→TP, roja entrada→SL.
- Etiquetas de precio en el borde derecho (TP / Entrada / SL / precio actual / zonas).
- Señal ESPERAR / NO_OPERAR → caja punteada semitransparente (niveles pendientes).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

BG = "#1e1e1e"
PANEL = "#2d2d30"
GRID = "#2a2a2e"
SPINE = "#3e3e42"
TEXT = "#e0e0e0"
MUTED = "#808080"
UP = "#4ec9b0"
DOWN = "#f48771"
ENTRY_C = "#4fc1ff"
SL_C = "#f44747"
TP_C = "#6a9955"
TP_TEXT = "#9fd89f"
SL_TEXT = "#ff9c9c"
ZONE_C = "#c586c0"
WARN_C = "#ffd700"
STATE_COLORS = {"ENTRAR": "#4ec9b0", "ESPERAR": "#ffd700", "NO_OPERAR": "#f44747"}

HISTORY_CANDLES = 84  # ~7 h de M5
FUTURE_CANDLES = 32  # ~2.7 h de proyección a la derecha
BOX_CANDLES = 28
M5 = timedelta(minutes=5)


@dataclass(frozen=True)
class MarketUnit:
    size: float
    label: str
    kind: str  # "pips" | "pts" | "usd"


def market_unit(asset: str | None) -> MarketUnit:
    """Unidad de distancia por mercado (convención de market_pips)."""
    from app.models.market_pips import normalize_asset, pip_size

    key = normalize_asset(asset)
    if key in ("XAUUSD", "GOLD", "GC=F"):
        return MarketUnit(pip_size(key), "pips", "pips")
    if key in ("BTC", "BTCUSDT"):
        return MarketUnit(1.0, "$", "usd")
    return MarketUnit(pip_size(key), "pts", "pts")


def compute_position_levels(
    direction: str | None,
    entry: float | None,
    sl: float | None,
    tp: float | None,
    asset: str | None = None,
) -> dict[str, Any] | None:
    """Distancias, unidades y R:R de la posición; None si falta dirección/niveles.

    `sl_ok` / `tp_ok` indican si cada nivel está del lado correcto
    (LONG: SL < entrada < TP · SHORT: TP < entrada < SL).
    """
    if direction not in ("LONG", "SHORT") or entry is None or sl is None or tp is None:
        return None
    entry, sl, tp = float(entry), float(sl), float(tp)
    unit = market_unit(asset)
    if direction == "LONG":
        sl_ok, tp_ok = sl < entry, tp > entry
    else:
        sl_ok, tp_ok = sl > entry, tp < entry
    risk = abs(entry - sl)
    reward = abs(tp - entry)
    return {
        "direction": direction,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "risk": risk,
        "reward": reward,
        "rr": reward / risk if risk > 1e-12 else None,
        "sl_ok": sl_ok,
        "tp_ok": tp_ok,
        "valid": sl_ok and tp_ok and risk > 1e-12,
        "tp_delta": tp - entry,
        "sl_delta": sl - entry,
        "tp_units": (tp - entry) / unit.size,
        "sl_units": (sl - entry) / unit.size,
        "unit": unit,
    }


def position_box_rects(
    pos: dict[str, Any], x0: float, x1: float,
) -> dict[str, tuple[float, float, float, float]]:
    """Rectángulos (x, y, ancho, alto) de las zonas TP (entrada→TP) y SL (entrada→SL)."""
    e, s_, t_ = pos["entry"], pos["sl"], pos["tp"]
    w = x1 - x0
    return {
        "tp": (x0, min(e, t_), w, abs(t_ - e)),
        "sl": (x0, min(e, s_), w, abs(s_ - e)),
    }


def _sign(v: float) -> str:
    return "+" if v >= 0 else "−"


def format_distance(delta: float, unit: MarketUnit, dec: int, entry: float) -> str:
    """'+17.27 · +172.7 pips' (XAU) · '+60.0 pts' (US30) · '+$572 (+0.68%)' (BTC)."""
    s = _sign(delta)
    d = abs(delta)
    if unit.kind == "pips":
        return f"{s}{d:.{dec}f} · {s}{d / unit.size:.1f} pips"
    if unit.kind == "pts":
        return f"{s}{d / unit.size:.1f} pts"
    pct = d / entry * 100 if entry else 0.0
    usd = f"{d:,.0f}" if d >= 100 else f"{d:,.2f}"
    return f"{s}${usd} ({s}{pct:.2f}%)"


def format_rr(rr: float | None) -> str:
    if rr is None:
        return "R:R n/d"
    if abs(rr - round(rr)) < 0.05:
        return f"R:R 1:{round(rr):d}"
    return f"R:R 1:{rr:.1f}"


def resolve_signal_state(data: dict, opt: dict) -> str:
    """ENTRAR | ESPERAR | NO_OPERAR para decidir caja activa vs pendiente."""
    if data.get("data_stale"):
        return "NO_OPERAR"
    verdict = data.get("chart_verdict") or data.get("signal_e1")
    if not verdict and data.get("crt") is not None and data.get("setup"):
        try:
            from app.views.btc_e1_report import build_report_context

            verdict = build_report_context(
                data,
                crt=data.get("crt"),
                div=data.get("divergence"),
                dmi=data.get("dmi"),
                e2=data.get("e2"),
                gallery_patterns=data.get("gallery_patterns"),
            )["verdict"]
        except Exception:
            verdict = None
    if verdict in STATE_COLORS:
        return str(verdict)
    action = str(opt.get("ahora_action", "ESPERAR")).upper()
    return "ENTRAR" if action.startswith("ENTRAR") else "ESPERAR"


def _to_utc(t: Any) -> datetime | None:
    if not isinstance(t, datetime):
        return None
    return t.replace(tzinfo=timezone.utc) if t.tzinfo is None else t.astimezone(timezone.utc)


def _ny_tz():
    try:
        from zoneinfo import ZoneInfo

        return ZoneInfo("America/New_York")
    except Exception:
        return timezone(timedelta(hours=-4), "NY")


def _time_ticks(times: list[datetime | None], total: int) -> tuple[list[float], list[str]]:
    """Ticks horarios 'HH:MM UTC / HH:MM NY' para velas reales y proyección futura."""
    n = len(times)
    if n == 0 or times[-1] is None:
        return [], []
    last = times[-1].replace(second=0, microsecond=0)
    last -= timedelta(minutes=last.minute % 5)
    ny = _ny_tz()
    span_h = total * 5 / 60
    step_min = 60 if span_h <= 12 else 120
    ticks: list[float] = []
    labels: list[str] = []
    for i in range(total):
        t = times[i] if i < n else last + (i - n + 1) * M5
        if t is None:
            continue
        if t.minute == 0 and (t.hour * 60) % step_min == 0:
            ticks.append(float(i))
            labels.append(f"{t:%H:%M}\n{t.astimezone(ny):%H:%M} NY")
    return ticks, labels


def _stack_tags(tags: list[dict], min_gap: float, y_min: float, y_max: float) -> None:
    """Separa verticalmente las etiquetas del eje derecho sin salirse de [y_min, y_max]."""
    ordered = sorted(tags, key=lambda t: t["y"], reverse=True)
    prev = None
    for tag in ordered:
        y = min(tag["y"], y_max - min_gap / 2)
        if prev is not None and prev - y < min_gap:
            y = prev - min_gap
        tag["y_draw"] = y
        prev = y
    nxt = None
    for tag in reversed(ordered):
        y = max(tag["y_draw"], y_min + min_gap / 2)
        if nxt is not None and y - nxt < min_gap:
            y = nxt + min_gap
        tag["y_draw"] = y
        nxt = y


def _zone_short(ztype: str | None) -> str:
    z = (ztype or "").lower()
    if z.startswith("soporte"):
        return "S"
    if z.startswith("resistencia"):
        return "R"
    return "Zona"


def _is_limit_entry(pos: dict[str, Any] | None, price: float, dec: int) -> bool:
    """Entrada alejada del precio actual (orden límite), no ejecutable a mercado."""
    if pos is None:
        return False
    tick = 10 ** (-dec)
    return abs(pos["entry"] - price) > max(0.25 * pos["risk"], 2 * tick)


def _entry_word(user_entry: float | None, is_limit: bool) -> str:
    """Rótulo de la entrada en la caja."""
    if user_entry is not None:
        return "Entrada usuario"
    if is_limit:
        return "Entrada límite"
    return "Entrada"


def _draw_candles(ax, show: list[dict], price: float) -> None:
    from matplotlib.patches import Rectangle

    for i, c in enumerate(show):
        color = UP if c["close"] >= c["open"] else DOWN
        ax.plot([i, i], [c["low"], c["high"]], color=color, linewidth=0.9, zorder=3)
        bottom = min(c["open"], c["close"])
        height = abs(c["close"] - c["open"]) or (c["high"] - c["low"]) * 0.02 or price * 1e-6
        ax.add_patch(Rectangle(
            (i - 0.32, bottom), 0.64, height, facecolor=color, edgecolor=color, zorder=4,
        ))


def _y_limits(show: list[dict], price: float, levels: tuple) -> tuple[float, float]:
    """Rango Y: velas + niveles de la operación (PDH/PDL solo si ya caben)."""
    y_lo = min(c["low"] for c in show)
    y_hi = max(c["high"] for c in show)
    for v in levels:
        if v is not None:
            y_lo, y_hi = min(y_lo, float(v)), max(y_hi, float(v))
    yrange = (y_hi - y_lo) or abs(price) * 0.01
    return y_lo - yrange * 0.07, y_hi + yrange * 0.07


def _draw_key_zones(
    ax, tags: list[dict], data: dict, level: float | None, ztype: str | None,
    zone_edges: tuple[float | None, float | None], fmt: str,
) -> None:
    """Zona S/R como banda sutil + PDH/PDL si caen dentro del rango visible."""
    ymin, ymax = ax.get_ylim()
    zone_lo, zone_hi = zone_edges
    if level is not None:
        band = abs(zone_hi - zone_lo) if zone_lo is not None and zone_hi is not None else 0.0
        if 1e-12 < band <= (ymax - ymin) * 0.05:
            ax.axhspan(zone_lo, zone_hi, color=ZONE_C, alpha=0.09, zorder=1, linewidth=0)
        ax.axhline(level, color=ZONE_C, linewidth=0.8, linestyle=":", alpha=0.7, zorder=2)
        tags.append({"y": float(level), "text": f"{_zone_short(ztype)} {level:{fmt}}",
                     "fg": ZONE_C, "bg": PANEL, "edge": ZONE_C, "prio": 3})
    for key, name in (("pdh", "PDH"), ("pdl", "PDL")):
        v = data.get(key)
        if v is not None and ymin < float(v) < ymax:
            ax.axhline(float(v), color=MUTED, linewidth=0.7, linestyle="--", alpha=0.45, zorder=2)
            tags.append({"y": float(v), "text": f"{name} {float(v):{fmt}}",
                         "fg": MUTED, "bg": PANEL, "edge": MUTED, "prio": 4})


def _draw_position_box(
    ax, tags: list[dict], pos: dict[str, Any], *,
    x0: float, x1: float, active: bool, entry_word: str, fmt: str, dec: int,
) -> None:
    """Caja Long/Short: verde entrada→TP, roja entrada→SL, con distancias y R:R."""
    from matplotlib.patches import Rectangle

    e, s_, t_ = pos["entry"], pos["sl"], pos["tp"]
    fill_a = 0.26 if active else 0.11
    edge_ls = "-" if active else (0, (4, 3))
    rects = position_box_rects(pos, x0, x1)
    for key, col in (("tp", TP_C), ("sl", SL_C)):
        rx, ry, rw, rh = rects[key]
        ax.add_patch(Rectangle(
            (rx, ry), rw, rh, facecolor=col, alpha=fill_a, edgecolor="none", zorder=2,
        ))
        ax.add_patch(Rectangle(
            (rx, ry), rw, rh, facecolor="none", edgecolor=col,
            linewidth=1.0, linestyle=edge_ls, alpha=0.9, zorder=2,
        ))
    ax.hlines(e, x0, x1, color=ENTRY_C, linewidth=1.6, linestyles=edge_ls, zorder=5)
    ax.hlines(t_, x0, x1, color=TP_C, linewidth=1.3, linestyles=edge_ls, zorder=5)
    ax.hlines(s_, x0, x1, color=SL_C, linewidth=1.3, linestyles=edge_ls, zorder=5)

    unit = pos["unit"]
    long_ = pos["direction"] == "LONG"
    tx = x0 + 0.8
    ax.text(tx, t_, f"TP {t_:{fmt}}   {format_distance(pos['tp_delta'], unit, dec, e)}",
            color=TP_TEXT, fontsize=9, fontweight="bold",
            va="top" if long_ else "bottom", ha="left", zorder=6)
    ax.text(tx, s_, f"SL {s_:{fmt}}   {format_distance(pos['sl_delta'], unit, dec, e)}",
            color=SL_TEXT, fontsize=9, fontweight="bold",
            va="bottom" if long_ else "top", ha="left", zorder=6)
    ax.text(tx, e, f"{entry_word} {e:{fmt}} · {format_rr(pos['rr'])}",
            color=ENTRY_C, fontsize=9, fontweight="bold",
            va="bottom" if long_ else "top", ha="left", zorder=6)

    tags.extend([
        {"y": t_, "text": f"TP {t_:{fmt}}", "fg": BG, "bg": TP_C, "edge": TP_C, "prio": 1},
        {"y": e, "text": f"Entrada {e:{fmt}}", "fg": BG, "bg": ENTRY_C, "edge": ENTRY_C, "prio": 1},
        {"y": s_, "text": f"SL {s_:{fmt}}", "fg": BG, "bg": SL_C, "edge": SL_C, "prio": 1},
    ])


def _draw_opti_entry(
    ax, tags: list[dict], user_entry: float | None, sys_entry: float | None, entry: float, *,
    x0: float, x1: float, fmt: str, dec: int,
) -> None:
    """Entrada óptima del sistema cuando el usuario fijó otra distinta."""
    if user_entry is None or sys_entry is None or abs(float(sys_entry) - entry) < 10 ** (-dec):
        return
    ax.hlines(float(sys_entry), x0, x1, color="#9cdcfe", linewidth=0.9, linestyles=":", zorder=5)
    tags.append({"y": float(sys_entry), "text": f"OPTI {float(sys_entry):{fmt}}",
                 "fg": "#9cdcfe", "bg": PANEL, "edge": "#9cdcfe", "prio": 2})


def _draw_pending_levels(
    ax, tags: list[dict], data: dict, levels: tuple, *,
    x0: float, x1: float, total: int, fmt: str,
) -> None:
    """Sin posición completa: niveles sueltos punteados o aviso «Sin niveles de entrada»."""
    sys_entry, sl, tp = levels
    ymin, ymax = ax.get_ylim()
    if sys_entry is None and sl is None and tp is None:
        bias = data.get("bias_h1")
        why = f"Bias H1 {bias}" if bias else "sin dirección"
        ax.text((x0 + total) / 2, (ymin + ymax) / 2, f"Sin niveles de entrada\n({why})",
                color=MUTED, fontsize=10, ha="center", va="center", style="italic", zorder=6)
    for v, name, col in ((sys_entry, "Entrada", ENTRY_C), (sl, "SL", SL_C), (tp, "TP", TP_C)):
        if v is not None:
            ax.hlines(float(v), x0, x1, color=col, linewidth=1.1, linestyles=(0, (4, 3)), zorder=5)
            tags.append({"y": float(v), "text": f"{name} {float(v):{fmt}}", "fg": BG, "bg": col,
                         "edge": col, "prio": 1})


def _draw_scalps(
    ax, tags: list[dict], opt: dict, entry: float | None, *,
    x0: float, x1: float, dec: int, fmt: str,
) -> None:
    for idx, (sc_e, _src) in enumerate((opt.get("scalp_entries") or [])[:3]):
        if entry is not None and abs(float(sc_e) - float(entry)) < 10 ** (-dec):
            continue
        ax.hlines(float(sc_e), x0, x1, color="#9cdcfe", linewidth=0.8, linestyles=":", zorder=5)
        tags.append({"y": float(sc_e), "text": f"Scalp{idx + 1} {float(sc_e):{fmt}}",
                     "fg": "#9cdcfe", "bg": PANEL, "edge": "#9cdcfe", "prio": 2})


def _draw_2m5(ax, show: list[dict], span: float) -> None:
    """Recuadro sobre las dos últimas velas M5."""
    from matplotlib.patches import Rectangle

    n = len(show)
    if n < 2:
        return
    lo2 = min(c["low"] for c in show[-2:])
    hi2 = max(c["high"] for c in show[-2:])
    pad2 = span * 0.01
    ax.add_patch(Rectangle(
        (n - 2 - 0.5, lo2 - pad2), 2.0, (hi2 - lo2) + 2 * pad2,
        facecolor="none", edgecolor=WARN_C, linewidth=1.2, linestyle="--", alpha=0.8, zorder=5,
    ))
    ax.text(n - 1.5, hi2 + pad2 * 1.5, "2M5", color=WARN_C, fontsize=7.5,
            ha="center", va="bottom", zorder=6)


def _draw_axis_tags(ax, tags: list[dict]) -> None:
    """Etiquetas de precio en el borde derecho, apiladas sin solaparse."""
    from matplotlib.transforms import blended_transform_factory

    ymin, ymax = ax.get_ylim()
    _stack_tags(tags, min_gap=(ymax - ymin) * 0.036, y_min=ymin, y_max=ymax)
    tr = blended_transform_factory(ax.transAxes, ax.transData)
    for tag in tags:
        main = tag["prio"] <= 1
        ax.text(
            1.004, tag["y_draw"], tag["text"], transform=tr, clip_on=False,
            color=tag["fg"], fontsize=8.5 if main else 7.5,
            fontweight="bold" if main else "normal", va="center", ha="left", zorder=10,
            bbox={"boxstyle": "round,pad=0.25", "facecolor": tag["bg"], "edgecolor": tag["edge"],
                  "alpha": 0.95 if main else 0.85},
        )


def _state_lines(
    state: str, direction: str | None, callout: str, pos: dict[str, Any] | None, *,
    active: bool, is_limit: bool, session: dict, note: str | None = None,
) -> list[str]:
    dir_txt = f" {direction}" if direction in ("LONG", "SHORT") else ""
    lines = [f"{state}{dir_txt}  ·  {callout}"]
    if pos is not None and not pos["valid"]:
        lines.append("! Niveles incoherentes (SL/TP del lado equivocado)")
    elif pos is not None and not active:
        lines.append("Niveles planificados (pendiente, no es entrada activa)"
                     + (" · entrada límite" if is_limit else ""))
    if session.get("in_ny_window"):
        lines[-1] += f"  ·  KZ {session.get('window', 'NY')}"
    if note:
        lines.append(note)
    return lines


def _draw_state_box(ax, state: str, lines: list[str]) -> None:
    """Estado arriba a la izquierda, fuera del área de velas."""
    scol = STATE_COLORS.get(state, WARN_C)
    ax.text(
        0.0, 1.012, "\n".join(lines), transform=ax.transAxes, color=scol, fontsize=9.5,
        fontweight="bold", va="bottom", ha="left",
        bbox={"boxstyle": "round,pad=0.35", "facecolor": PANEL, "edgecolor": scol, "alpha": 0.95},
    )


def _chart_title(asset: str, data: dict) -> tuple[str, str]:
    """Título con la frescura de datos (última vela) y su color."""
    gen = data.get("generated", "")
    title = f"{asset} M5 · {gen} UTC · 2M5 + entrada óptima"
    fresh = data.get("data_freshness") or {}
    if fresh.get("last_candle_utc"):
        title = f"{asset} M5 · vela {fresh['last_candle_utc']} UTC · 2M5 + entrada óptima"
        if fresh.get("stale"):
            title += " · DATOS DESACTUALIZADOS"
    return title, SL_C if fresh.get("stale") else "#569cd6"


def _style_axes(ax, show: list[dict], total: int) -> None:
    """Eje X en hora real (UTC / NY), eje Y a la derecha, grid y bordes."""
    times = [_to_utc(c.get("open_time")) for c in show]
    ticks, labels = _time_ticks(times, total)
    if ticks:
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels, fontsize=8)
        ax.set_xlabel("Hora UTC (arriba) · Nueva York (abajo) · velas M5", color=MUTED, fontsize=8)
    ax.yaxis.tick_right()
    ax.tick_params(axis="both", colors=TEXT, labelsize=8)
    ax.tick_params(axis="y", colors=MUTED)
    ax.grid(True, color=GRID, linewidth=0.6, zorder=0)
    for spine in ax.spines.values():
        spine.set_color(SPINE)


def _draw_zentinel_note(fig, asset: str, session: dict | None) -> None:
    try:
        from app.models.zentinel_presets import zentinel_chart_note

        fig.text(0.025, 0.012, zentinel_chart_note(asset, session),
                 color=MUTED, fontsize=7, ha="left", va="bottom")
    except Exception:
        pass


def render_trade_chart(
    data: dict,
    opt: dict,
    out_path: Path | str,
    *,
    asset: str,
    dpi: int,
    callout: str,
    zone_edges: tuple[float | None, float | None],
    note: str | None = None,
) -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from app.views.illustrate_high_entry import savefig_png

    m5 = data.get("m5") or []
    show = m5[-HISTORY_CANDLES:]
    n = len(show)
    total = n + FUTURE_CANDLES
    dec = int(opt.get("dec", data.get("price_decimals", 1)))
    fmt = f".{dec}f"
    direction = opt.get("direction") or (data.get("setup") or {}).get("direction", "")
    price = float(data.get("price") or show[-1]["close"])
    user_entry = opt.get("user_entry")
    sys_entry = opt.get("entry")
    entry = user_entry if user_entry is not None else sys_entry
    sl, tp = opt.get("sl"), opt.get("tp")
    pos = compute_position_levels(direction, entry, sl, tp, asset)
    state = resolve_signal_state(data, opt)
    level = opt.get("level") or (data.get("zone") or {}).get("level")
    ztype = opt.get("ztype") or (data.get("zone") or {}).get("type")
    zone_lo, zone_hi = zone_edges

    is_limit = _is_limit_entry(pos, price, dec)
    active = pos is not None and pos["valid"] and state == "ENTRAR" and not is_limit

    fig = None
    try:
        fig, ax = plt.subplots(figsize=(14, 7.4), facecolor=BG)
        ax.set_facecolor(BG)
        fig.subplots_adjust(left=0.025, right=0.885, top=0.865, bottom=0.12)

        _draw_candles(ax, show, price)
        ax.set_ylim(*_y_limits(show, price, (entry, sys_entry, sl, tp, level, zone_lo, zone_hi)))
        ax.set_xlim(-1, total)
        ymin, ymax = ax.get_ylim()

        tags: list[dict] = []
        _draw_key_zones(ax, tags, data, level, ztype, zone_edges, fmt)

        x0 = n - 0.5
        x1 = x0 + BOX_CANDLES
        ax.axvline(x0, color=MUTED, linewidth=0.7, linestyle=":", alpha=0.5, zorder=2)
        if pos is not None:
            _draw_position_box(ax, tags, pos, x0=x0, x1=x1, active=active,
                               entry_word=_entry_word(user_entry, is_limit), fmt=fmt, dec=dec)
            _draw_opti_entry(ax, tags, user_entry, sys_entry, pos["entry"],
                             x0=x0, x1=x1, fmt=fmt, dec=dec)
        else:
            _draw_pending_levels(ax, tags, data, (sys_entry, sl, tp),
                                 x0=x0, x1=x1, total=total, fmt=fmt)
        _draw_scalps(ax, tags, opt, entry, x0=x0, x1=x1, dec=dec, fmt=fmt)

        # --- precio actual
        last = show[-1]
        pcol = UP if last["close"] >= last["open"] else DOWN
        ax.axhline(price, color=pcol, linewidth=0.8, linestyle=(0, (1, 2)), alpha=0.9, zorder=2)
        tags.insert(0, {"y": price, "text": f"{price:{fmt}}", "fg": BG, "bg": pcol, "edge": pcol, "prio": 0})

        _draw_2m5(ax, show, ymax - ymin)
        _draw_axis_tags(ax, tags)
        _draw_state_box(ax, state, _state_lines(
            state, direction, callout, pos,
            active=active, is_limit=is_limit, session=data.get("session") or {}, note=note,
        ))
        title, title_color = _chart_title(asset, data)
        fig.suptitle(title, color=title_color, fontsize=13, fontweight="bold", x=0.455, y=0.985)
        _style_axes(ax, show, total)
        _draw_zentinel_note(fig, asset, data.get("session"))

        return savefig_png(fig, out_path, dpi=dpi, facecolor=BG)
    finally:
        if fig is not None:
            plt.close(fig)
