"""
Fetch live BTCUSDT candles (M5 + H1) and write a snapshot for E1 strategy review.

Usage:
  python -m app.controllers.analyze_btc_m5
  python -m app.controllers.analyze_btc_m5 --no-chart
  python -m app.controllers.analyze_btc_m5 --symbol BTCUSDT

Output:
  live/btc_m5_snapshot.md      (full)
  live/btc_m5_signal.md        (light)
  live/btc_m5_high_signal.md   (high - CRT + turtle soup + checklist profundo)
  live/btc_m5_chart.png

Super High (separate script — user capture):
  python -m app.controllers.analyze_super_high_entry --ml --neural
  live/btc_super_high_signal.md  (requires live/super_high_entry.png)
"""
from __future__ import annotations

import argparse
import json
import math
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
OUT_DIR = LIVE_DIR
BINANCE = "https://api.binance.com/api/v3/klines"

# NY session windows (UTC-4 EDT approx; adjust if needed)
NY_OFFSET = timedelta(hours=-4)


def fetch_klines(symbol: str, interval: str, limit: int = 200) -> list[dict]:
    url = f"{BINANCE}?symbol={symbol}&interval={interval}&limit={limit}"
    req = Request(url, headers={"User-Agent": "CursorTrading/1.0"})
    with urlopen(req, timeout=20) as resp:
        raw = json.loads(resp.read().decode())
    rows = []
    for k in raw:
        rows.append({
            "open_time": datetime.fromtimestamp(k[0] / 1000, tz=timezone.utc),
            "open": float(k[1]),
            "high": float(k[2]),
            "low": float(k[3]),
            "close": float(k[4]),
            "volume": float(k[5]),
            "close_time": datetime.fromtimestamp(k[6] / 1000, tz=timezone.utc),
        })
    return rows


def rsi(closes: list[float], period: int = 14) -> float | None:
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
    rs = avg_g / avg_l
    return 100.0 - (100.0 / (1.0 + rs))


def ema(values: list[float], period: int) -> list[float | None]:
    out: list[float | None] = [None] * len(values)
    if len(values) < period:
        return out
    k = 2 / (period + 1)
    seed = sum(values[:period]) / period
    out[period - 1] = seed
    for i in range(period, len(values)):
        out[i] = values[i] * k + out[i - 1] * (1 - k)
    return out


def swing_levels(candles: list[dict], lookback: int = 3) -> tuple[list[float], list[float]]:
    highs, lows = [], []
    for i in range(lookback, len(candles) - lookback):
        h = candles[i]["high"]
        l = candles[i]["low"]
        if all(h >= candles[i + j]["high"] for j in range(-lookback, lookback + 1) if j != 0):
            highs.append(h)
        if all(l <= candles[i + j]["low"] for j in range(-lookback, lookback + 1) if j != 0):
            lows.append(l)
    return highs[-5:], lows[-5:]


def pdh_pdl(daily_or_h1: list[dict], now_utc: datetime) -> tuple[float | None, float | None]:
    """Approximate PDH/PDL from UTC days using H1 candles."""
    yesterday = (now_utc - timedelta(days=1)).date()
    day_bars = [c for c in daily_or_h1 if c["open_time"].date() == yesterday]
    if not day_bars:
        return None, None
    return max(c["high"] for c in day_bars), min(c["low"] for c in day_bars)


def h1_bias(h1: list[dict]) -> str:
    closes = [c["close"] for c in h1]
    e20 = ema(closes, 20)
    e50 = ema(closes, 50)
    if e20[-1] is None or e50[-1] is None:
        return "NEUTRAL"
    last = closes[-1]
    slope = closes[-1] - closes[-4] if len(closes) >= 4 else 0
    if e20[-1] > e50[-1] and last > e20[-1] and slope > 0:
        return "BULLISH"
    if e20[-1] < e50[-1] and last < e20[-1] and slope < 0:
        return "BEARISH"
    return "NEUTRAL"


def session_flags(now_utc: datetime) -> dict:
    ny = now_utc + NY_OFFSET
    h = ny.hour + ny.minute / 60
    morning = 8.0 <= h < 11.0
    afternoon = 14.0 <= h < 17.0
    return {
        "ny_local": ny.strftime("%Y-%m-%d %H:%M"),
        "utc": now_utc.strftime("%Y-%m-%d %H:%M"),
        "in_ny_window": morning or afternoon,
        "window": "NY AM 08-11" if morning else ("NY PM 14-17" if afternoon else "FUERA_NY"),
    }


def last_n_candle_summary(candles: list[dict], n: int = 6) -> list[str]:
    lines = []
    for c in candles[-n:]:
        body = c["close"] - c["open"]
        color = "G" if body >= 0 else "R"
        lines.append(
            f"{c['open_time'].strftime('%H:%M')} O={c['open']:.1f} H={c['high']:.1f} "
            f"L={c['low']:.1f} C={c['close']:.1f} [{color}]"
        )
    return lines


def two_candle_confirm(candles: list[dict], direction: str) -> bool:
    if len(candles) < 2:
        return False
    a, b = candles[-2], candles[-1]
    if direction == "LONG":
        return a["close"] > a["open"] and b["close"] > b["open"]
    if direction == "SHORT":
        return a["close"] < a["open"] and b["close"] < b["open"]
    return False


def nearest_zone(price: float, swings_h: list[float], swings_l: list[float]) -> dict:
    candidates = [(lvl, "resistencia_debil") for lvl in swings_h] + [
        (lvl, "soporte_debil") for lvl in swings_l
    ]
    if not candidates:
        return {"level": None, "type": None, "dist_pct": None}
    level, ztype = min(candidates, key=lambda x: abs(x[0] - price))
    dist = abs(level - price) / price * 100
    return {"level": level, "type": ztype, "dist_pct": dist}


def suggest_setup(price: float, bias: str, zone: dict, rsi_m5: float | None,
                  confirm_long: bool, confirm_short: bool, in_ny: bool,
                  pdh: float | None, pdl: float | None) -> dict:
    verdict = "OBSERVAR"
    direction = "NONE"
    reasons = []
    red_flags = []

    _ = in_ny  # reloj opcional; no bloquea setup ni fuerza NO_OPERAR

    if bias == "BULLISH":
        direction = "LONG"
    elif bias == "BEARISH":
        direction = "SHORT"
    else:
        red_flags.append("Bias H1 NEUTRAL — no forzar dirección")

    if pdh and pdl:
        if pdl < price < pdh:
            reasons.append(f"Precio dentro PDH/PDL ({pdl:.0f}–{pdh:.0f}) → contexto NEUTRAL posible")
        elif price > pdh:
            reasons.append(f"Precio > PDH {pdh:.0f} → sesgo alcista CRT")
        elif price < pdl:
            reasons.append(f"Precio < PDL {pdl:.0f} → sesgo bajista CRT")

    near_zone = zone["dist_pct"] is not None and zone["dist_pct"] <= 0.15
    if near_zone:
        reasons.append(f"Cerca de {zone['type']} @ {zone['level']:.1f} ({zone['dist_pct']:.3f}%)")
    else:
        red_flags.append("Lejos de swing S/R débil (>0.15%) — esperar zona")

    if rsi_m5 is not None:
        if direction == "LONG" and rsi_m5 > 70:
            red_flags.append(f"RSI M5 {rsi_m5:.1f} sobrecomprado — filtro TORYS-like")
        elif direction == "SHORT" and rsi_m5 < 30:
            red_flags.append(f"RSI M5 {rsi_m5:.1f} sobrevendido — filtro TORYS-like")
        else:
            reasons.append(f"RSI M5 {rsi_m5:.1f} no extremo contra dirección")

    if direction == "LONG" and confirm_long:
        reasons.append("2 velas M5 verdes (confirmación)")
    elif direction == "SHORT" and confirm_short:
        reasons.append("2 velas M5 rojas (confirmación)")
    elif direction != "NONE":
        red_flags.append("Sin 2 velas M5 de confirmación")

    # A+ only if NY + bias + near zone + confirmation + few red flags
    hard = [r for r in red_flags if "NEUTRAL" in r or "Lejos" in r or "Sin 2" in r]
    if direction != "NONE" and not hard and near_zone:
        verdict = "SETUP_A+"
    elif direction != "NONE" and len(hard) <= 1 and near_zone:
        verdict = "SETUP_B_ESPERAR"
    elif direction != "NONE":
        verdict = "NO_TRADE"
    else:
        verdict = "OBSERVAR"

    # Rough SL/TP from nearest swing for R:R sketch (not account $9)
    sl = tp = rr = None
    if direction == "LONG" and zone["level"]:
        sl = min(zone["level"], price) * 0.998 if zone["type"] == "soporte_debil" else price * 0.997
        risk = abs(price - sl)
        tp = price + 2 * risk
        rr = 2.0
    elif direction == "SHORT" and zone["level"]:
        sl = max(zone["level"], price) * 1.002 if zone["type"] == "resistencia_debil" else price * 1.003
        risk = abs(sl - price)
        tp = price - 2 * risk
        rr = 2.0

    return {
        "verdict": verdict,
        "direction": direction,
        "reasons": reasons,
        "red_flags": red_flags,
        "sl": sl,
        "tp": tp,
        "rr": rr,
    }


def recalc_setup_for_direction(
    price: float,
    direction: str,
    zone: dict,
    rsi_m5: float | None,
    confirm_long: bool,
    confirm_short: bool,
    in_ny: bool,
    pdh: float | None,
    pdl: float | None,
    bias_h1: str,
) -> dict:
    """Re-score setup when CLI forces LONG/SHORT direction."""
    bias = "BULLISH" if direction == "LONG" else "BEARISH" if direction == "SHORT" else "NEUTRAL"
    return suggest_setup(
        price, bias, zone, rsi_m5, confirm_long, confirm_short, in_ny, pdh, pdl,
    )


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
    ax.set_ylabel("BTCUSDT", color="#e0e0e0")
    fig.tight_layout()
    fig.savefig(path, dpi=140, facecolor="#1e1e1e")
    plt.close(fig)


def _augment_categories(categories: dict, data: dict, chart_path: Path | None,
                        use_ml: bool, use_neural: bool,
                        crt=None, div=None, dmi=None, e2=None) -> dict:
    """Apply ML and/or neural augmentation to categories dict."""
    out = categories
    if use_ml:
        from app.models.btc_ml_signals import augment_categories
        out = augment_categories(out, data, crt, div, dmi, e2)
    if use_neural and chart_path is not None:
        from app.models.btc_neural_signals import augment_categories_neural
        out = augment_categories_neural(out, chart_path)
    return out


def _resolve_chart_for_neural(
    m5: list[dict], chart_path: Path, chart_ok: bool, no_chart: bool,
    symbol: str, now: datetime, bias: str,
) -> tuple[Path | None, bool]:
    """Return chart path for neural inference; generate PNG if needed."""
    if chart_ok and chart_path.is_file():
        return chart_path, chart_ok
    if chart_path.is_file():
        return chart_path, chart_ok
    try:
        save_chart(
            m5, chart_path,
            f"{symbol} M5 · {now.strftime('%Y-%m-%d %H:%M')} UTC · Bias {bias}",
        )
        return chart_path, True if not no_chart else chart_ok
    except Exception as e:
        print(f"WARN neural chart: {e}")
        return None, chart_ok


def write_snapshot(path: Path, data: dict, m5: list[dict] | None = None, h1: list[dict] | None = None,
                   use_ml: bool = False, use_neural: bool = False, chart_path: Path | None = None) -> None:
    from app.views.btc_e1_report import TIER_FULL, build_report_context, format_e1_report
    from app.services.btc_high_analysis import analyze_crt, detect_rsi_divergence, dmi_proxy

    s = data["setup"]
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
    categories = ctx["categories"]

    lines = [
        "# BTC M5 Live Snapshot — E1 Analysis Feed",
        "",
        f"> Generado: **{data['generated']}** UTC  ·  NY local: **{data['session']['ny_local']}**  ·  Ventana: **{data['session']['window']}**",
        f"> Símbolo: `{data['symbol']}`  ·  Fuente: Binance public klines",
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
        f"| Precio spot (último close M5) | **{data['price']:.2f}** |",
        f"| Reloj (info) | {data['session']['window']} — NY {data['session'].get('ny_local', 'n/a')} |",
        f"| Bias H1 (EMA20/50) | **{data['bias_h1']}** |",
        f"| RSI M5 (14) | {data['rsi_m5']:.1f}" if data["rsi_m5"] is not None else "| RSI M5 (14) | n/a |",
        f"| RSI H1 (14) | {data['rsi_h1']:.1f}" if data["rsi_h1"] is not None else "| RSI H1 (14) | n/a |",
        f"| PDH (aprox. día UTC anterior) | {data['pdh']:.2f}" if data["pdh"] else "| PDH | n/a |",
        f"| PDL (aprox. día UTC anterior) | {data['pdl']:.2f}" if data["pdl"] else "| PDL | n/a |",
        "",
        "### Swings M5 (proxy zonas débiles)",
        "",
        f"- Swing highs: {', '.join(f'{x:.1f}' for x in data['swing_highs']) or '—'}",
        f"- Swing lows: {', '.join(f'{x:.1f}' for x in data['swing_lows']) or '—'}",
        f"- Zona más cercana: **{data['zone']['type'] or 'n/a'}** @ "
        f"{data['zone']['level']:.1f} ({data['zone']['dist_pct']:.3f}%)"
        if data["zone"]["level"] else "- Zona más cercana: n/a",
        "",
        "### Últimas 6 velas M5",
        "",
    ]
    for row in data["last_m5"]:
        lines.append(f"- `{row}`")
    lines += [
        "",
        f"- Confirmación 2 verdes (LONG): {'✅' if data['confirm_long'] else '❌'}",
        f"- Confirmación 2 rojas (SHORT): {'✅' if data['confirm_short'] else '❌'}",
        "",
        f"![Chart M5](btc_m5_chart.png)" if data.get("chart") else "",
        "",
        "---",
        f"*Script `analyze_btc_m5.py` · Datos Binance · {data['generated']} UTC*",
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


def verdict_to_signal(setup: dict) -> str:
    from app.models.btc_signal_categories import verdict_to_signal as _vts
    return _vts(setup)


def write_signal_light(path: Path, data: dict, m5: list[dict] | None = None, h1: list[dict] | None = None,
                       use_ml: bool = False, use_neural: bool = False, chart_path: Path | None = None) -> None:
    """Compact signal (~357 token budget) with Veredicto + Categories + CRT + red flags."""
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

    lines = [
        "# BTC M5 Signal (light)",
        "",
        f"**{ctx['verdict']}** | **{data['price']:.0f}** | {clock} | H1:{data['bias_h1']}",
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
    parser = argparse.ArgumentParser(description="BTC M5 live snapshot for E1 analysis")
    parser.add_argument("--symbol", default="BTCUSDT")
    parser.add_argument("--no-chart", action="store_true")
    parser.add_argument(
        "--mode",
        choices=("full", "light", "high", "both", "all"),
        default="full",
        help="full | light | high | both (full+light) | all (full+light+high)",
    )
    parser.add_argument(
        "--ml",
        action="store_true",
        help="Append ML win probability to Categories (requires trained model)",
    )
    parser.add_argument(
        "--neural",
        action="store_true",
        help="Append neural gallery WIN%% to Categories from live chart PNG",
    )
    parser.add_argument(
        "--bias",
        choices=("auto", "bullish", "bearish"),
        default="auto",
        help="Bias for all modes: auto | bullish (LONG) | bearish (SHORT)",
    )
    parser.add_argument(
        "--setup",
        choices=("auto", "break", "reverse"),
        default="auto",
        help="Setup mode for high: auto | break (breakout) | reverse (E2 turtle soup)",
    )
    parser.add_argument(
        "--advanced",
        action="store_true",
        help="High mode: deep analysis sections (auto with --ml --neural)",
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
            "(e.g. 97450, 97450.5, or European 97.450 → 97450)"
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

    try:
        m5 = fetch_klines(args.symbol, "5m", 200)
        h1 = fetch_klines(args.symbol, "1h", 200)
    except (URLError, HTTPError, TimeoutError, json.JSONDecodeError) as e:
        print(f"ERROR fetching Binance: {e}")
        return 1

    price = m5[-1]["close"]
    closes_m5 = [c["close"] for c in m5]
    closes_h1 = [c["close"] for c in h1]
    rsi_m5 = rsi(closes_m5)
    rsi_h1 = rsi(closes_h1)
    bias = h1_bias(h1)
    pdh, pdl = pdh_pdl(h1, now)
    sh, sl = swing_levels(m5)
    zone = nearest_zone(price, sh, sl)
    session = session_flags(now)
    confirm_long = two_candle_confirm(m5, "LONG")
    confirm_short = two_candle_confirm(m5, "SHORT")
    setup = suggest_setup(
        price, bias, zone, rsi_m5, confirm_long, confirm_short,
        session["in_ny_window"], pdh, pdl,
    )

    chart_path = OUT_DIR / "btc_m5_chart.png"
    chart_ok = False
    want_chart = not args.no_chart and args.mode in ("full", "both", "high", "all")
    if want_chart:
        try:
            save_chart(m5, chart_path, f"{args.symbol} M5 · {now.strftime('%Y-%m-%d %H:%M')} UTC · Bias {bias}")
            chart_ok = True
        except Exception as e:
            print(f"WARN chart: {e}")

    data = {
        "generated": now.strftime("%Y-%m-%d %H:%M"),
        "symbol": args.symbol,
        "price": price,
        "session": session,
        "bias_h1": bias,
        "rsi_m5": rsi_m5,
        "rsi_h1": rsi_h1,
        "pdh": pdh,
        "pdl": pdl,
        "swing_highs": sh,
        "swing_lows": sl,
        "zone": zone,
        "last_m5": last_n_candle_summary(m5),
        "confirm_long": confirm_long,
        "confirm_short": confirm_short,
        "setup": setup,
        "chart": chart_ok,
        "mode_bias": args.bias,
        "mode_setup": args.setup,
        "history_mode": bool(args.history_review),
        "entry_override": entry_override,
    }

    if args.bias in ("bullish", "bearish"):
        from app.services.btc_high_analysis import apply_forced_bias
        data = apply_forced_bias(data, args.bias)

    snap = OUT_DIR / "btc_m5_snapshot.md"
    signal = OUT_DIR / "btc_m5_signal.md"
    high = OUT_DIR / "btc_m5_high_signal.md"

    use_ml = False
    if args.ml:
        from app.models.btc_ml_signals import model_available
        if model_available():
            use_ml = True
        else:
            print("WARN --ml: model not found; run python -m app.controllers.train_btc_signals first")

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
            m5, chart_path, chart_ok, args.no_chart, args.symbol, now, bias,
        )
        if chart_for_neural is None:
            print("WARN --neural: no chart available for inference")
            use_neural = False
        elif not args.no_chart:
            data["chart"] = chart_ok

    if args.mode in ("full", "both", "all"):
        write_snapshot(snap, data, m5, h1, use_ml=use_ml, use_neural=use_neural,
                       chart_path=chart_for_neural)
    if args.mode in ("light", "both", "all"):
        write_signal_light(signal, data, m5, h1, use_ml=use_ml, use_neural=use_neural,
                           chart_path=chart_for_neural)
    if args.mode in ("high", "all"):
        from app.services.btc_high_analysis import build_high_context, write_high_signal
        high_data = build_high_context(
            data, m5, h1, last_n_candle_summary,
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
                    asset="BTC",
                    main_chart_path=None if args.no_chart else chart_path,
                    annotated_path=(OUT_DIR / "btc_m5_chart_annotated.png") if args.ilustrate else None,
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
        # Auto-advanced when ML+Neural (PS1 also passes --advanced; keep Python consistent)
        use_advanced = bool(args.advanced) or (use_ml and use_neural)
        write_high_signal(
            high, high_data, verdict_to_signal,
            use_ml=use_ml or use_neural,
            advanced=use_advanced,
        )

    sig_label = verdict_to_signal(data["setup"])
    print("=" * 56)
    print(f"BTC {args.symbol}  {price:.2f}  |  Bias H1: {bias}  |  {session['window']}")
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
        print("Cursor -> @live/btc_m5_signal.md @docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md")
    elif args.mode == "high":
        print("Cursor -> @live/btc_m5_high_signal.md @docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md")
    elif args.mode == "all":
        print("Cursor FULL -> @live/btc_m5_snapshot.md")
        print("Cursor LIGHT -> @live/btc_m5_signal.md @docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md")
        print("Cursor HIGH -> @live/btc_m5_high_signal.md @docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md")
    elif args.mode == "both":
        print("Cursor full  -> @live/btc_m5_snapshot.md")
        print("Cursor light -> @live/btc_m5_signal.md @docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md")
    else:
        print("Cursor -> analiza @live/btc_m5_snapshot.md con mi plan E1 M5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
