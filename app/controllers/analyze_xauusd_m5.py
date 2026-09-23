"""
Fetch live XAUUSD candles (M5 + H1) via GC=F proxy and write E1 strategy snapshots.

Usage:
  python -m app.controllers.analyze_xauusd_m5
  python -m app.controllers.analyze_xauusd_m5 --mode all --ml --no-chart
  python -m app.controllers.analyze_xauusd_m5 --ticker GC=F

Output:
  live/xauusd_m5_snapshot.md
  live/xauusd_m5_signal.md
  live/xauusd_m5_high_signal.md
  live/xauusd_m5_context.md
  live/xauusd_m5_chart.png

Data: yfinance / Yahoo Chart API — GC=F (COMEX gold futures) as XAUUSD proxy.
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

from app.config import LIVE_DIR

OUT_DIR = LIVE_DIR

SYMBOL_LABEL = "XAUUSD"
ML_SYMBOL = "xauusd"
PRICE_DECIMALS = 2
CHART_FILE = "xauusd_m5_chart.png"

from app.models.xauusd_data import DEFAULT_TICKERS, fetch_xauusd_klines


def save_chart(m5: list[dict], path: Path, title: str) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    from app.views.illustrate_high_entry import savefig_png

    fig = None
    try:
        fig, ax = plt.subplots(figsize=(12, 5), facecolor="#1e1e1e")
        ax.set_facecolor("#1e1e1e")
        show = m5[-60:]
        for i, c in enumerate(show):
            color = "#4ec9b0" if c["close"] >= c["open"] else "#f48771"
            ax.plot([i, i], [c["low"], c["high"]], color=color, linewidth=0.8)
            bottom = min(c["open"], c["close"])
            height = abs(c["close"] - c["open"]) or (c["high"] - c["low"]) * 0.01
            ax.add_patch(Rectangle((i - 0.3, bottom), 0.6, height, facecolor=color, edgecolor=color))
        ax.set_title(title, color="#dcdcaa", fontsize=12, fontweight="bold")
        ax.tick_params(colors="#e0e0e0")
        for spine in ax.spines.values():
            spine.set_color("#3e3e42")
        ax.set_ylabel(SYMBOL_LABEL, color="#e0e0e0")
        fig.tight_layout()
        savefig_png(fig, path, dpi=140, facecolor="#1e1e1e")
    finally:
        if fig is not None:
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
    ctx = build_report_context(data, crt=crt, div=div)
    if use_ml or use_neural:
        ctx["categories"] = _augment_categories(
            ctx["categories"], data, chart_path, use_ml, use_neural, crt, div, dmi,
        )
    body = format_e1_report(data, TIER_FULL, ctx=ctx, crt=crt, div=div)
    notes = data.get("data_notes") or []
    disclaimer = [
        "",
        "### Disclaimer datos oro",
        "",
        f"- Proxy mercado: **{data.get('data_source', 'GC=F')}** (no es cota Exness/spot exacta).",
        "- Ops OCR XAUUSD en v_ops_apr_sep son **pocas**; ML es mayormente sintético E1.",
        "- No auto-ejecutar. Validar con broker.",
    ]
    if notes:
        disclaimer.append(f"- Fetch notes: `{'; '.join(str(n) for n in notes[:4])}`")
    path.write_text("\n".join([f"# {SYMBOL_LABEL} M5 Snapshot", ""] + body + disclaimer), encoding="utf-8")


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
    thin = data.get("ml_thin_ops_note") or (
        "Datos OCR oro delgados — confiar más en reglas E1 que en ML."
    )

    lines = [
        f"# {SYMBOL_LABEL} M5 Signal (light)",
        "",
        f"**{ctx['verdict']}** | **{data['price']:.{dec}f}** | {clock} | H1:{data['bias_h1']}",
        format_bando_rec_line(ctx["categories"]),
        "",
    ]
    lines += format_e1_report(data, TIER_LIGHT, ctx=ctx, crt=crt, div=div)
    lines += [
        "",
        f"> **Aviso:** {thin}",
        "",
        "**Cursor (max 5 líneas):** Veredicto + dir + 1 regla clave + invalidación.",
        f"*{data['generated']} UTC · {data['symbol']} · proxy GC=F · E1 only · no auto-ejecutar*",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="XAUUSD M5 live snapshot for E1 analysis")
    parser.add_argument("--ticker", default=None, help="yfinance ticker (default GC=F)")
    parser.add_argument("--no-chart", action="store_true")
    parser.add_argument(
        "--mode",
        choices=("full", "light", "high", "context", "both", "all"),
        default="all",
        help="full | light | high | context | both | all",
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
        "--no-open",
        action="store_true",
        help="History-review: no abrir preview HTML en el navegador",
    )
    parser.add_argument(
        "--entry",
        default=None,
        help="High: user fill price (Entry usuario); keeps Entrada óptima separate",
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
        m5, h1, fetch_meta = fetch_xauusd_klines(tickers=tickers)
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
    session = session_flags(now, asset="XAUUSD")
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
        "asset_label": SYMBOL_LABEL,
        "chart_file": CHART_FILE,
        "price_decimals": PRICE_DECIMALS,
        "data_source": data_source,
        "data_notes": fetch_meta.get("notes", []),
        "sl_points_std": 8.0,
        "ml_thin_ops_note": (
            "OCR v_ops_apr_sep: ≤4 filas XAUUSD (2 con side+entry); "
            "modelo ML entrenado sobre features E1 sintéticas en GC=F."
        ),
        "entry_override": entry_override,
        "history_mode": bool(args.history_review),
        "m5": m5,
        "h1": h1,
    }
    from app.models.zentinel_presets import attach_zentinel_to_data

    attach_zentinel_to_data(data, asset="XAUUSD")

    if args.bias in ("bullish", "bearish"):
        from app.services.btc_high_analysis import apply_forced_bias
        data = apply_forced_bias(data, args.bias)

    snap = OUT_DIR / "xauusd_m5_snapshot.md"
    signal = OUT_DIR / "xauusd_m5_signal.md"
    high = OUT_DIR / "xauusd_m5_high_signal.md"
    context_md = OUT_DIR / "xauusd_m5_context.md"

    if args.mode == "context":
        from app.services.m5_context_analysis import analyze_m5_context, write_context_report

        ctx = analyze_m5_context(m5, asset="XAUUSD")
        write_context_report(context_md, data, ctx, price_decimals=PRICE_DECIMALS)
        print(f"Context: {context_md}")
        return 0

    use_ml = False
    if args.ml:
        from app.models.ml_signals import model_available
        if model_available(ML_SYMBOL):
            use_ml = True
        else:
            print("WARN --ml: model not found; run python -m app.controllers.train_xauusd_signals first")

    use_neural = False
    if args.neural:
        from app.models.btc_neural_signals import model_available as neural_available
        if neural_available():
            use_neural = True
        else:
            print("WARN --neural: desktop neural model not found")

    chart_for_neural: Path | None = None
    if use_neural:
        chart_for_neural, chart_ok = _resolve_chart_for_neural(
            m5, chart_path, chart_ok, args.no_chart, SYMBOL_LABEL, now, bias,
        )
        if chart_for_neural is None:
            use_neural = False

    if args.mode in ("full", "both", "all"):
        write_snapshot(snap, data, m5, h1, use_ml=use_ml, use_neural=use_neural,
                       chart_path=chart_for_neural)
    if args.mode in ("light", "both", "all"):
        write_signal_light(signal, data, m5, h1, use_ml=use_ml, use_neural=use_neural,
                           chart_path=chart_for_neural)
    if args.mode in ("high", "all"):
        from app.services.btc_high_analysis import build_high_context, write_high_signal
        from app.views.btc_e1_report import build_report_context as _build_report_context
        from app.models.btc_signal_categories import verdict_to_signal

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
            cats = _build_report_context(data, crt=crt, div=div)["categories"]
            high_data["ml_categories"] = _augment_categories(
                cats, data, chart_for_neural, use_ml, use_neural, crt, div, dmi, e2,
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
                    asset="XAUUSD",
                    main_chart_path=None if args.no_chart else chart_path,
                    annotated_path=(OUT_DIR / "xauusd_m5_chart_annotated.png") if args.ilustrate else None,
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
                    if args.ilustrate:
                        from app.views.history_review import finalize_history_chart
                        from app.models.signal_history import load_signal_history, history_path_for_asset
                        hist_path = history_path_for_asset("XAUUSD", OUT_DIR)
                        hist = load_signal_history(hist_path)
                        sig_id = hist[-1]["id"] if hist else None
                        finalize_history_chart(
                            high_data,
                            asset="XAUUSD",
                            annotated_abs=written["annotated_chart"],
                            signal_id=sig_id,
                            mode="history_review" if args.history_review else "high",
                        )
            except Exception as e:
                print(f"WARN chart overlays: {e}")
        use_advanced = bool(args.advanced) or (use_ml and use_neural)
        write_high_signal(
            high, high_data, verdict_to_signal,
            use_ml=use_ml or use_neural,
            advanced=use_advanced,
        )

    if args.mode in ("context", "all"):
        try:
            from app.services.m5_context_analysis import analyze_m5_context, write_context_report
            ctx = analyze_m5_context(m5, asset="XAUUSD")
            write_context_report(context_md, data, ctx, price_decimals=PRICE_DECIMALS)
        except Exception as e:
            print(f"WARN context: {e}")

    print("=" * 56)
    print(f"XAUUSD {ticker_label}  {price:.{PRICE_DECIMALS}f}  |  Bias {bias}")
    print(f"Fuente: {data_source}")
    print(f"Signal:   {signal if signal.is_file() else '(skip)'}")
    print(f"Snapshot: {snap if snap.is_file() else '(skip)'}")
    if args.mode in ("high", "all") and high.is_file():
        print(f"High:     {high}")
    print(f"ML: {use_ml}  Neural: {use_neural}")
    if chart_ok:
        print(f"Chart:    {chart_path}")
    print("=" * 56)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
