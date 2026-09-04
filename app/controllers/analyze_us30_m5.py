"""
Fetch live US30 candles (M5 + H1) via yfinance and write E1 strategy snapshots.

Usage:
  python -m app.controllers.analyze_us30_m5
  python -m app.controllers.analyze_us30_m5 --mode all --ml --no-chart
  python -m app.controllers.analyze_us30_m5 --ticker YM=F

Output:
  live/us30_m5_snapshot.md
  live/us30_m5_signal.md
  live/us30_m5_high_signal.md
  live/us30_m5_chart.png

Data: yfinance / Yahoo Chart API — primary YM=F (Dow futures), fallback ^DJI.
SL ~$9 → ~9 pts ($1/pt) or ~90 pts ($0.10/pt micro) — ver TRADING_LIVE_US30_M5_ANALYSIS.md
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from app.models.market_analysis_core import (
    h1_bias,
    last_n_candle_summary,
    nearest_zone,
    pdh_pdl,
    rsi,
    session_flags,
    suggest_setup,
    swing_levels,
    two_candle_confirm,
)

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
OUT_DIR = LIVE_DIR

SYMBOL_LABEL = "US30"
ML_SYMBOL = "us30"
PRICE_DECIMALS = 1
CHART_FILE = "us30_m5_chart.png"

from app.models.us30_data import DEFAULT_TICKERS, fetch_us30_klines


def save_chart(m5: list[dict], path: Path, title: str) -> None:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    fig, ax = plt.subplots(figsize=(12, 5), facecolor="#1e1e1e")
    ax.set_facecolor("#1e1e1e")
    show = m5[-60:]
    for i, c in enumerate(show):
        color = "#4ec9b0" if c["close"] >= c["open"] else "#f48771"
        ax.plot([i, i], [c["low"], c["high"]], color=color, linewidth=0.8)
        bottom = min(c["open"], c["close"])
        height = abs(c["close"] - c["open"]) or (c["high"] - c["low"]) * 0.01
        ax.add_patch(Rectangle((i - 0.3, bottom), 0.6, height, facecolor=color, edgecolor=color))
    ax.set_title(title, color="#569cd6", fontsize=12, fontweight="bold")
    ax.tick_params(colors="#e0e0e0")
    for spine in ax.spines.values():
        spine.set_color("#3e3e42")
    ax.set_ylabel(SYMBOL_LABEL, color="#e0e0e0")
    fig.tight_layout()
    fig.savefig(path, dpi=140, facecolor="#1e1e1e")
    plt.close(fig)


def _augment_categories(categories: dict, data: dict, chart_path: Path | None,
                        use_ml: bool, use_neural: bool,
                        crt=None, div=None, dmi=None, e2=None) -> dict:
    out = categories
    if use_ml:
        from app.models.ml_signals import augment_categories
        out = augment_categories(out, data, ML_SYMBOL, crt, div, dmi, e2)
    if use_neural and chart_path is not None:
        from app.models.btc_neural_signals import augment_categories_neural
        out = augment_categories_neural(out, chart_path)
    return out


def _resolve_chart_for_neural(
    m5: list[dict], chart_path: Path, chart_ok: bool, no_chart: bool,
    label: str, now: datetime, bias: str,
) -> tuple[Path | None, bool]:
    if chart_ok and chart_path.is_file():
        return chart_path, chart_ok
    if chart_path.is_file():
        return chart_path, chart_ok
    try:
        save_chart(m5, chart_path, f"{label} M5 · {now.strftime('%Y-%m-%d %H:%M')} UTC · Bias {bias}")
        return chart_path, True if not no_chart else chart_ok
    except Exception as e:
        print(f"WARN neural chart: {e}")
        return None, chart_ok


def write_snapshot(path: Path, data: dict, m5: list[dict] | None = None, h1: list[dict] | None = None,
                   use_ml: bool = False, use_neural: bool = False, chart_path: Path | None = None) -> None:
    from app.views.btc_e1_report import TIER_FULL, build_report_context, format_e1_report
    from app.services.btc_high_analysis import analyze_crt, detect_rsi_divergence, dmi_proxy

    m5 = m5 or []
    h1 = h1 or []
    crt = analyze_crt(data["price"], data.get("pdh"), data.get("pdl"), h1, m5) if h1 and m5 else None
    div = detect_rsi_divergence(m5) if m5 else None
    dmi = dmi_proxy([c["close"] for c in m5]) if m5 else None
    ctx = build_report_context(data, crt=crt, div=div, dmi=dmi)
    if use_ml or use_neural:
        ctx["categories"] = _augment_categories(
            ctx["categories"], data, chart_path, use_ml, use_neural, crt, div, dmi,
        )

    dec = PRICE_DECIMALS
    src = data.get("data_source", "yfinance")
    lines = [
        f"# {SYMBOL_LABEL} M5 Live Snapshot — E1 Analysis Feed",
        "",
        f"> Generado: **{data['generated']}** UTC  ·  NY local: **{data['session']['ny_local']}**  ·  Ventana: **{data['session']['window']}**",
        f"> Símbolo: `{data['symbol']}`  ·  Fuente: {src}",
        "",
        f"> **SL referencia ~$9:** ~{data.get('sl_points_std', 9):.0f} pts ($1/pt) · "
        f"~{data.get('sl_points_micro', 90):.0f} pts ($0.10/pt micro)",
        "",
        "---",
        "",
    ]
    lines += format_e1_report(data, TIER_FULL, ctx=ctx, crt=crt, div=div, dmi=dmi)
    lines += [
        "---",
        "",
        "## Detalle mercado",
        "",
        "| Campo | Valor |",
        "|-------|-------|",
        f"| Precio spot (último close M5) | **{data['price']:.{dec}f}** |",
        f"| Reloj (info) | {data['session']['window']} — NY {data['session'].get('ny_local', 'n/a')} |",
        f"| Bias H1 (EMA20/50) | **{data['bias_h1']}** |",
        f"| RSI M5 (14) | {data['rsi_m5']:.1f}" if data["rsi_m5"] is not None else "| RSI M5 (14) | n/a |",
        f"| RSI H1 (14) | {data['rsi_h1']:.1f}" if data["rsi_h1"] is not None else "| RSI H1 (14) | n/a |",
        f"| PDH (aprox. día UTC anterior) | {data['pdh']:.{dec}f}" if data["pdh"] else "| PDH | n/a |",
        f"| PDL (aprox. día UTC anterior) | {data['pdl']:.{dec}f}" if data["pdl"] else "| PDL | n/a |",
        "",
        "### Swings M5 (proxy zonas débiles)",
        "",
        f"- Swing highs: {', '.join(f'{x:.{dec}f}' for x in data['swing_highs']) or '—'}",
        f"- Swing lows: {', '.join(f'{x:.{dec}f}' for x in data['swing_lows']) or '—'}",
        f"- Zona más cercana: **{data['zone']['type'] or 'n/a'}** @ "
        f"{data['zone']['level']:.{dec}f} ({data['zone']['dist_pct']:.3f}%)"
        if data["zone"]["level"] else "- Zona más cercana: n/a",
        "",
        "### Últimas 6 velas M5",
        "",
    ]
    for row in data["last_m5"]:
        lines.append(f"- `{row}`")
    if data.get("data_notes"):
        lines += ["", "### Notas fuente datos", ""]
        for n in data["data_notes"]:
            lines.append(f"- {n}")
    lines += [
        "",
        f"- Confirmación 2 verdes (LONG): {'✅' if data['confirm_long'] else '❌'}",
        f"- Confirmación 2 rojas (SHORT): {'✅' if data['confirm_short'] else '❌'}",
        "",
        f"![Chart M5]({CHART_FILE})" if data.get("chart") else "",
        "",
        "---",
        f"*Script `analyze_us30_m5.py` · {src} · {data['generated']} UTC*",
        "",
    ]
    fixed = []
    for line in lines:
        if line.startswith("| RSI") and not line.endswith("|"):
            fixed.append(line + " |")
        elif line.startswith("| PDH") and not line.rstrip().endswith("|"):
            fixed.append(line + " |")
        elif line.startswith("| PDL") and not line.rstrip().endswith("|"):
            fixed.append(line + " |")
        else:
            fixed.append(line)
    path.write_text("\n".join(fixed), encoding="utf-8")


def write_signal_light(path: Path, data: dict, m5: list[dict] | None = None, h1: list[dict] | None = None,
                       use_ml: bool = False, use_neural: bool = False, chart_path: Path | None = None) -> None:
    from app.views.btc_e1_report import TIER_LIGHT, build_report_context, format_bando_rec_line, format_e1_report
    from app.services.btc_high_analysis import analyze_crt, detect_rsi_divergence

    m5 = m5 or []
    h1 = h1 or []
    crt = analyze_crt(data["price"], data.get("pdh"), data.get("pdl"), h1, m5) if h1 and m5 else None
    div = detect_rsi_divergence(m5) if m5 else None
    ctx = build_report_context(data, crt=crt, div=div)
    if use_ml or use_neural:
        ctx["categories"] = _augment_categories(
            ctx["categories"], data, chart_path, use_ml, use_neural, crt, div,
        )
    ses = data["session"]
    clock = ses.get("window", "n/d")
    dec = PRICE_DECIMALS

    lines = [
        f"# {SYMBOL_LABEL} M5 Signal (light)",
        "",
        f"**{ctx['verdict']}** | **{data['price']:.{dec}f}** | {clock} | H1:{data['bias_h1']}",
        format_bando_rec_line(ctx["categories"]),
        "",
    ]
    lines += format_e1_report(data, TIER_LIGHT, ctx=ctx, crt=crt, div=div)
    lines += [
        "**Cursor (max 5 líneas):** Veredicto + dir + 1 regla clave + invalidación.",
        f"*{data['generated']} UTC · {data['symbol']} · E1 only · no auto-ejecutar*",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="US30 M5 live snapshot for E1 analysis")
    parser.add_argument("--ticker", default=None, help="yfinance ticker (default YM=F then ^DJI)")
    parser.add_argument("--no-chart", action="store_true")
    parser.add_argument(
        "--mode",
        choices=("full", "light", "high", "both", "all"),
        default="full",
    )
    parser.add_argument("--ml", action="store_true")
    parser.add_argument("--neural", action="store_true")
    parser.add_argument("--bias", choices=("auto", "bullish", "bearish"), default="auto")
    parser.add_argument("--setup", choices=("auto", "break", "reverse"), default="auto")
    parser.add_argument(
        "--advanced",
        action="store_true",
        help="High mode: Categories stats + deep sections (auto with --ml --neural)",
    )
    parser.add_argument(
        "--ilustrate",
        action="store_true",
        help="High mode: annotated PNG (2M5 + zona + Entry/SL/TP); works with --no-chart",
    )
    parser.add_argument(
        "--history-review",
        action="store_true",
        help="High: review P&L of last Entry only (no new signal framing; do not append history)",
    )
    parser.add_argument(
        "--entry",
        default=None,
        help=(
            "High: user fill price (Entry usuario); keeps Entrada óptima separate "
            "(e.g. 53128, 53128.0, or European 53.12.800 → 53128.0)"
        ),
    )
    args = parser.parse_args()

    entry_override = None
    if args.entry is not None:
        from app.services.btc_high_analysis import parse_entry_price
        try:
            entry_override = parse_entry_price(args.entry)
        except (ValueError, TypeError) as e:
            print(f"ERROR --entry inválido: {args.entry!r} ({e})")
            return 1
        if entry_override is None:
            print(f"ERROR --entry vacío: {args.entry!r}")
            return 1
        print(f"Entry override: {entry_override} (manual; raw={args.entry!r})")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    tickers = (args.ticker,) if args.ticker else DEFAULT_TICKERS

    try:
        m5, h1, fetch_meta = fetch_us30_klines(tickers=tickers)
    except Exception as e:
        print(f"ERROR fetching yfinance: {e}")
        return 1

    price = m5[-1]["close"]
    closes_m5 = [c["close"] for c in m5]
    closes_h1 = [c["close"] for c in h1]
    rsi_m5 = rsi(closes_m5)
    rsi_h1 = rsi(closes_h1)
    bias = h1_bias(h1)
    pdh, pdl = pdh_pdl(h1, now)
    sh, slv = swing_levels(m5)
    zone = nearest_zone(price, sh, slv)
    session = session_flags(now)
    confirm_long = two_candle_confirm(m5, "LONG")
    confirm_short = two_candle_confirm(m5, "SHORT")
    setup = suggest_setup(
        price, bias, zone, rsi_m5, confirm_long, confirm_short,
        session["in_ny_window"], pdh, pdl, price_decimals=PRICE_DECIMALS,
    )

    chart_path = OUT_DIR / CHART_FILE
    chart_ok = False
    want_chart = not args.no_chart and args.mode in ("full", "both", "high", "all")
    if want_chart:
        try:
            save_chart(m5, chart_path, f"{SYMBOL_LABEL} M5 · {now.strftime('%Y-%m-%d %H:%M')} UTC · Bias {bias}")
            chart_ok = True
        except Exception as e:
            print(f"WARN chart: {e}")

    ticker_label = fetch_meta.get("ticker", tickers[0])
    m5_iv = fetch_meta.get("m5_interval", "5m")
    data_source = f"yfinance ({ticker_label}, M5={m5_iv})"

    data = {
        "generated": now.strftime("%Y-%m-%d %H:%M"),
        "symbol": SYMBOL_LABEL,
        "yf_ticker": ticker_label,
        "price": price,
        "session": session,
        "bias_h1": bias,
        "rsi_m5": rsi_m5,
        "rsi_h1": rsi_h1,
        "pdh": pdh,
        "pdl": pdl,
        "swing_highs": sh,
        "swing_lows": slv,
        "zone": zone,
        "last_m5": last_n_candle_summary(m5, price_decimals=PRICE_DECIMALS),
        "confirm_long": confirm_long,
        "confirm_short": confirm_short,
        "setup": setup,
        "chart": chart_ok,
        "mode_bias": args.bias,
        "mode_setup": args.setup,
        "history_mode": bool(args.history_review),
        "asset_label": SYMBOL_LABEL,
        "chart_file": CHART_FILE,
        "price_decimals": PRICE_DECIMALS,
        "data_source": data_source,
        "data_notes": fetch_meta.get("notes", []),
        "sl_points_std": 9.0,
        "sl_points_micro": 90.0,
        "entry_override": entry_override,
    }

    if args.bias in ("bullish", "bearish"):
        from app.services.btc_high_analysis import apply_forced_bias
        data = apply_forced_bias(data, args.bias)

    snap = OUT_DIR / "us30_m5_snapshot.md"
    signal = OUT_DIR / "us30_m5_signal.md"
    high = OUT_DIR / "us30_m5_high_signal.md"

    use_ml = False
    if args.ml:
        from app.models.ml_signals import model_available
        if model_available(ML_SYMBOL):
            use_ml = True
        else:
            print("WARN --ml: model not found; run python -m app.controllers.train_us30_signals first")

    use_neural = False
    if args.neural:
        from app.models.btc_neural_signals import model_available as neural_available
        if neural_available():
            use_neural = True
        else:
            print('WARN --neural: model not found; run app/services/learning/training neuronal/train_desktop_vision.py first')

    chart_for_neural: Path | None = None
    if use_neural:
        chart_for_neural, chart_ok = _resolve_chart_for_neural(
            m5, chart_path, chart_ok, args.no_chart, SYMBOL_LABEL, now, bias,
        )
        if chart_for_neural is None:
            print("WARN --neural: no chart available for inference")
            use_neural = False
        elif not args.no_chart:
            data["chart"] = chart_ok

    from app.models.btc_signal_categories import verdict_to_signal

    if args.mode in ("full", "both", "all"):
        write_snapshot(snap, data, m5, h1, use_ml=use_ml, use_neural=use_neural,
                       chart_path=chart_for_neural)
    if args.mode in ("light", "both", "all"):
        write_signal_light(signal, data, m5, h1, use_ml=use_ml, use_neural=use_neural,
                           chart_path=chart_for_neural)
    if args.mode in ("high", "all"):
        from app.services.btc_high_analysis import build_high_context, write_high_signal
        high_data = build_high_context(
            data, m5, h1,
            lambda c, n=6: last_n_candle_summary(c, n, price_decimals=PRICE_DECIMALS),
            bias_mode=args.bias, setup_mode=args.setup,
        )
        if use_ml or use_neural:
            crt = high_data.get("crt")
            div = high_data.get("divergence")
            dmi = high_data.get("dmi")
            e2 = high_data.get("e2")
            from app.views.btc_e1_report import build_report_context
            ctx = build_report_context(
                data, crt=crt, div=div, dmi=dmi, e2=e2,
                gallery_patterns=high_data.get("gallery_patterns"),
            )
            high_data["ml_categories"] = _augment_categories(
                ctx["categories"], data, chart_for_neural, use_ml, use_neural,
                crt, div, dmi, e2,
            )
        # Chart High: overlays OPTI/SL/TP/S-R when chart enabled; -Ilustrate → PNG aparte
        want_entry_chart = (not args.no_chart) or args.ilustrate
        if want_entry_chart:
            from app.services.btc_high_analysis import compute_optimal_entry
            from app.views.illustrate_high_entry import write_entry_overlay_charts

            opt = compute_optimal_entry(
                high_data, high_data["setup"]["direction"],
                high_data["crt"], high_data["zone"],
            )
            try:
                written = write_entry_overlay_charts(
                    high_data,
                    opt,
                    asset="US30",
                    main_chart_path=None if args.no_chart else chart_path,
                    annotated_path=(OUT_DIR / "us30_m5_chart_annotated.png") if args.ilustrate else None,
                )
                if written.get("main_chart"):
                    high_data["chart"] = True
                    data["chart"] = True
                    chart_ok = True
                    print(f"Chart OPTI: {written['main_chart']}")
                if written.get("annotated_chart"):
                    high_data["ilustrate"] = True
                    high_data["annotated_chart_file"] = written["annotated_file"]
                    high_data["annotated_chart_abs"] = written["annotated_chart"]
                    print(f"Ilustrate: {written['annotated_chart']}")
            except Exception as e:
                print(f"WARN chart overlays: {e}")
        use_advanced = bool(args.advanced) or (use_ml and use_neural)
        write_high_signal(
            high, high_data, verdict_to_signal,
            use_ml=use_ml or use_neural,
            advanced=use_advanced,
        )

    sig_label = verdict_to_signal(data["setup"])
    print("=" * 56)
    print(f"US30 {ticker_label}  {price:.{PRICE_DECIMALS}f}  |  Bias H1: {bias}  |  {session['window']}")
    print(f"Fuente: {data_source}")
    if fetch_meta.get("notes"):
        for n in fetch_meta["notes"]:
            print(f"  NOTE: {n}")
    print(f"Bando: {data.get('mode_bias', 'auto').upper()} | Senal: {sig_label}  ({data['setup']['direction']})  |  Auto: {data['setup']['verdict']}")
    if args.mode in ("full", "both", "all"):
        print(f"Snapshot: {snap}")
    if args.mode in ("light", "both", "all"):
        print(f"Light:    {signal}")
    if args.mode in ("high", "all"):
        print(f"High:     {high}")
        if args.bias != "auto" or args.setup != "auto":
            print(f"Modo:     bias={args.bias} setup={args.setup}")
        if args.advanced or (use_ml and use_neural):
            print("Modo:     ADVANCED (análisis profundo)")
        if args.history_review:
            print("Modo:     HISTORY-REVIEW (P&L última Entry; sin append)")
        if entry_override is not None:
            print(f"Entry:    {entry_override} (manual / user-provided)")
        print("Salidas:")
        print(f"  Reporte:  {high.resolve()}")
        print(f"  Relativo: live/{high.name}")
        if high_data.get("ilustrate") and high_data.get("annotated_chart_file"):
            ann_abs = high_data.get("annotated_chart_abs") or str(
                (OUT_DIR / high_data["annotated_chart_file"]).resolve()
            )
            print(f"  Chart:    {ann_abs}")
            print(f"  Chart rel: live/{high_data['annotated_chart_file']}")
            print(f"  Preview:  ![chart]({high_data['annotated_chart_file']})")
    if chart_ok:
        print(f"Chart:    {chart_path}")
    print("=" * 56)
    if args.mode == "light":
        print("Cursor -> @live/us30_m5_signal.md @docs/protocols/TRADING_LIVE_US30_SIGNAL_LIGHT.md")
    elif args.mode == "high":
        print("Cursor -> @live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md")
    elif args.mode == "all":
        print("Cursor FULL -> @live/us30_m5_snapshot.md")
        print("Cursor LIGHT -> @live/us30_m5_signal.md @docs/protocols/TRADING_LIVE_US30_SIGNAL_LIGHT.md")
        print("Cursor HIGH -> @live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md")
    else:
        print("Cursor -> analiza @live/us30_m5_snapshot.md con mi plan E1 M5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
