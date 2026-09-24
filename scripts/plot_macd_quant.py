"""CLI: mini-chart MACD quant (2 paneles) desde parquet → **H4**.

No hay parquet H4 nativo en data/ (solo M5 + H1). Por defecto:
  M5 → resample 4h (barras reales agregadas). Fallback: H1 → H4.

Uso:
  python -m scripts.plot_macd_quant
  python -m scripts.plot_macd_quant --symbol btc --force-refresh
  python -m scripts.plot_macd_quant --symbol us30 --days 7 --force-refresh
  python -m scripts.plot_macd_quant --symbol xauusd --bars 42
  python -m scripts.plot_macd_quant --symbol ukoil --days 7 --force-refresh

Salida por defecto: live/<symbol>_h4_macd_quant.png
Ventana por defecto: últimos ``--days`` calendario terminando en **UTC now**
(no la cola de un parquet viejo). Con ``--force-refresh`` (o cache stale)
se redescargan M5/H1 antes de plotear (Binance BTC / yfinance US30·XAU·UKOIL).
No publica métricas de backtest (WR/PF PENDING).

Estilo panel MACD: nube azul (>0) / púrpura (<0), señal blanca, dots magenta/cyan
(referencia TradingView-like; soft-filter only).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from app.config import DATA_DIR, LIVE_DIR, PROJECT_ROOT
from app.models.macd_quant import (
    MACD_FAST,
    MACD_SIGNAL,
    MACD_SLOW,
    WEEK_H4_BARS,
    calculate_macd,
    candles_to_ohlcv_df,
    generate_signals,
    resample_to_h4,
)

BINANCE = "https://api.binance.com/api/v3/klines"
# Si el último open_time del parquet tiene más de esto, se refresca solo.
STALE_MAX_AGE = timedelta(hours=6)
# Historia mínima para EMA200 en H4 (~200×4h ≈ 33d) + margen.
REFRESH_LOOKBACK_DAYS = 60

# Mapa símbolo CLI → (parquet M5 preferido, parquet H1 fallback)
SYMBOL_PARQUET: dict[str, tuple[Path, Path]] = {
    "btc": (DATA_DIR / "btcusdt_m5.parquet", DATA_DIR / "btcusdt_h1.parquet"),
    "us30": (DATA_DIR / "us30_m5.parquet", DATA_DIR / "us30_h1.parquet"),
    "xau": (DATA_DIR / "xauusd_m5.parquet", DATA_DIR / "xauusd_h1.parquet"),
    "xauusd": (DATA_DIR / "xauusd_m5.parquet", DATA_DIR / "xauusd_h1.parquet"),
    "ukoil": (DATA_DIR / "ukoil_m5.parquet", DATA_DIR / "ukoil_h1.parquet"),
}

SYMBOL_TITLE: dict[str, str] = {
    "btc": "BTCUSDT",
    "us30": "US30",
    "xau": "XAUUSD",
    "xauusd": "XAUUSD",
    "ukoil": "UKOIL",
}

# Clave de archivo live (xauusd → xau; ukoil → ukoil)
SYMBOL_FILE_KEY: dict[str, str] = {
    "btc": "btc",
    "us30": "us30",
    "xau": "xau",
    "xauusd": "xau",
    "ukoil": "ukoil",
}

BG = "#0e0e12"
PANEL = "#14141a"
TEXT = "#c8c8d0"
GRID = "#2a2a36"
ACCENT = "#7aa2ff"
EMA_C = "#c586c0"
GOLD = "#dcdcaa"
# Nube TradingView-like
BLUE_TOP = "#2962FF"
BLUE_BASE = "#1565C0"
PURPLE_TOP = "#CE93D8"
PURPLE_BASE = "#9C27B0"
SIGNAL_C = "#ffffff"
DOT_UP = "#e879f9"  # magenta picos / BUY
DOT_DOWN = "#22d3ee"  # cyan valles / SELL


def normalize_symbol(symbol: str) -> str:
    key = symbol.lower().strip()
    if key not in SYMBOL_PARQUET:
        raise ValueError(f"Símbolo no soportado: {symbol} (btc|us30|xau|xauusd|ukoil)")
    return key


def utc_now() -> pd.Timestamp:
    return pd.Timestamp.now(tz="UTC")


def _parquet_last_ts(path: Path) -> pd.Timestamp | None:
    if not path.is_file():
        return None
    try:
        df = pd.read_parquet(path, columns=["open_time"])
    except Exception:
        try:
            df = pd.read_parquet(path)
        except Exception:
            return None
    if df.empty or "open_time" not in df.columns:
        return None
    return pd.to_datetime(df["open_time"].iloc[-1], utc=True)


def cache_is_stale(symbol: str, *, max_age: timedelta = STALE_MAX_AGE) -> bool:
    """True si falta parquet o el último M5/H1 está más viejo que ``max_age`` vs UTC now."""
    key = normalize_symbol(symbol)
    m5_p, h1_p = SYMBOL_PARQUET[key]
    now = utc_now()
    for p in (m5_p, h1_p):
        last = _parquet_last_ts(p)
        if last is None:
            return True
        if now - last > max_age:
            return True
    return False


def _fetch_binance_paginated(
    symbol: str,
    interval: str,
    start: datetime,
    end: datetime,
) -> list[dict]:
    """Klines Binance paginados (igual contrato que train_btc_signals)."""
    rows: list[dict] = []
    start_ms = int(start.timestamp() * 1000)
    end_ms = int(end.timestamp() * 1000)
    current = start_ms
    while current < end_ms:
        url = (
            f"{BINANCE}?symbol={symbol}&interval={interval}"
            f"&startTime={current}&endTime={end_ms}&limit=1000"
        )
        req = Request(url, headers={"User-Agent": "CursorTrading-MacdQuant/1.0"})
        try:
            with urlopen(req, timeout=30) as resp:
                raw = json.loads(resp.read().decode())
        except (URLError, HTTPError, TimeoutError) as e:
            raise RuntimeError(f"Binance fetch failed: {e}") from e
        if not raw:
            break
        for k in raw:
            rows.append(
                {
                    "open_time": datetime.fromtimestamp(k[0] / 1000, tz=timezone.utc),
                    "open": float(k[1]),
                    "high": float(k[2]),
                    "low": float(k[3]),
                    "close": float(k[4]),
                    "volume": float(k[5]),
                    "close_time": datetime.fromtimestamp(k[6] / 1000, tz=timezone.utc),
                }
            )
        last_close = int(raw[-1][6])
        next_start = last_close + 1
        if next_start <= current:
            break
        current = next_start
        time.sleep(0.12)
    seen: set[datetime] = set()
    unique: list[dict] = []
    for r in sorted(rows, key=lambda x: x["open_time"]):
        if r["open_time"] not in seen:
            seen.add(r["open_time"])
            unique.append(r)
    return unique


def _merge_write_parquet(path: Path, new_rows: list[dict]) -> int:
    """Fusiona velas nuevas con parquet existente (dedupe por open_time) y escribe."""
    if not new_rows:
        return 0
    incoming = pd.DataFrame(new_rows)
    if path.is_file():
        old = pd.read_parquet(path)
        merged = pd.concat([old, incoming], ignore_index=True)
    else:
        merged = incoming
    merged["open_time"] = pd.to_datetime(merged["open_time"], utc=True)
    merged = (
        merged.drop_duplicates(subset=["open_time"], keep="last")
        .sort_values("open_time")
        .reset_index(drop=True)
    )
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    merged.to_parquet(path, index=False)
    return len(merged)


def refresh_symbol_parquets(
    symbol: str,
    *,
    lookback_days: int = REFRESH_LOOKBACK_DAYS,
) -> dict[str, object]:
    """Descarga M5/H1 hasta UTC now y actualiza parquet en ``data/``.

    - btc: Binance BTCUSDT (append incremental desde último cache o lookback).
    - us30 / xau / ukoil: yfinance / Yahoo (mismo fetch que train_* / analyze_*).
    """
    key = normalize_symbol(symbol)
    m5_p, h1_p = SYMBOL_PARQUET[key]
    end = datetime.now(timezone.utc)
    meta: dict[str, object] = {"symbol": key, "end_utc": end.isoformat()}

    if key == "btc":
        # Append desde último M5 si existe; si no, lookback completo.
        last = _parquet_last_ts(m5_p)
        if last is not None:
            start = last.to_pydatetime() - timedelta(hours=1)
        else:
            start = end - timedelta(days=lookback_days)
        # Asegurar historia mínima para EMA200 H4 si el cache está vacío/corto
        floor = end - timedelta(days=lookback_days)
        if start > floor and (last is None or not m5_p.is_file()):
            start = floor
        print(
            f"[refresh] BTCUSDT Binance {start.date()} -> {end.date()} UTC ...",
            flush=True,
        )
        t0 = time.time()
        m5 = _fetch_binance_paginated("BTCUSDT", "5m", start, end)
        h1 = _fetch_binance_paginated("BTCUSDT", "1h", start, end)
        n_m5 = _merge_write_parquet(m5_p, m5)
        n_h1 = _merge_write_parquet(h1_p, h1)
        meta.update(
            {
                "source": "binance",
                "m5_rows": n_m5,
                "h1_rows": n_h1,
                "m5_last": str(_parquet_last_ts(m5_p)),
                "elapsed_s": round(time.time() - t0, 1),
            }
        )
        print(
            f"[refresh] BTC OK M5={n_m5} H1={n_h1} last={meta['m5_last']} "
            f"({meta['elapsed_s']}s)",
            flush=True,
        )
        return meta

    # us30 / xau / ukoil — yfinance (misma ruta que train_*)
    if key == "us30":
        from app.models.us30_data import DEFAULT_TICKERS, fetch_us30_klines

        tickers = DEFAULT_TICKERS
        fetch_fn = fetch_us30_klines
        m5_bars = min(lookback_days * 24 * 12, 5000)
        h1_bars = min(lookback_days * 24, 2000)
        label = "US30"
    elif key == "ukoil":
        from app.models.ukoil_data import DEFAULT_TICKERS, fetch_ukoil_klines

        tickers = DEFAULT_TICKERS
        fetch_fn = fetch_ukoil_klines
        m5_bars = min(lookback_days * 24 * 12, 8000)
        h1_bars = min(lookback_days * 24, 4000)
        label = "UKOIL"
    else:
        from app.models.xauusd_data import DEFAULT_TICKERS, fetch_xauusd_klines

        tickers = DEFAULT_TICKERS
        fetch_fn = fetch_xauusd_klines
        m5_bars = min(lookback_days * 24 * 12, 8000)
        h1_bars = min(lookback_days * 24, 4000)
        label = "XAUUSD"

    print(f"[refresh] {label} yfinance/Yahoo ~{lookback_days}d -> UTC now ...", flush=True)
    t0 = time.time()
    m5, h1, ymeta = fetch_fn(tickers=tickers, m5_bars=m5_bars, h1_bars=h1_bars)
    pd.DataFrame(m5).to_parquet(m5_p, index=False)
    pd.DataFrame(h1).to_parquet(h1_p, index=False)
    meta.update(
        {
            "source": "yfinance",
            "m5_rows": len(m5),
            "h1_rows": len(h1),
            "m5_last": str(_parquet_last_ts(m5_p)),
            "ymeta": ymeta,
            "elapsed_s": round(time.time() - t0, 1),
        }
    )
    print(
        f"[refresh] {label} OK M5={len(m5)} H1={len(h1)} last={meta['m5_last']} "
        f"({meta['elapsed_s']}s)",
        flush=True,
    )
    return meta


def resolve_source(symbol: str, path: Path | None) -> tuple[Path, str]:
    """Devuelve (parquet, kind) con kind in {m5, h1, custom}."""
    if path is not None:
        p = path if path.is_absolute() else PROJECT_ROOT / path
        if not p.is_file():
            raise FileNotFoundError(f"Parquet no encontrado: {p}")
        return p, "custom"
    key = normalize_symbol(symbol)
    m5_p, h1_p = SYMBOL_PARQUET[key]
    if m5_p.is_file():
        return m5_p, "m5"
    if h1_p.is_file():
        return h1_p, "h1"
    raise FileNotFoundError(
        f"Falta data M5/H1 para {key}: esperado {m5_p.name} o {h1_p.name}"
    )


def load_ohlcv(path: Path) -> pd.DataFrame:
    df = pd.read_parquet(path)
    return candles_to_ohlcv_df(df)


def load_h4(symbol: str, path: Path | None = None) -> tuple[pd.DataFrame, Path, str]:
    """Carga parquet y resamplea a H4. Documenta fuente (m5|h1|custom)."""
    parquet, kind = resolve_source(symbol, path)
    raw = load_ohlcv(parquet)
    # custom: inferir por nombre de archivo
    name = parquet.name.lower()
    if kind == "custom":
        if "_h4" in name or "h4" in name:
            # ya H4 — no re-agregar
            return raw, parquet, "h4_native"
        if "_h1" in name or name.endswith("h1.parquet"):
            kind = "h1"
        else:
            kind = "m5"
    h4 = resample_to_h4(raw)
    note = f"{kind}_resample_h4"
    return h4, parquet, note


def slice_week_ending_now(
    df: pd.DataFrame,
    *,
    days: float,
    bars: int | None = None,
    end: pd.Timestamp | None = None,
) -> pd.DataFrame:
    """Cola visible: últimos ``days`` (o ``bars``) terminando en ``end`` (UTC now).

    Calcula indicadores sobre ``df`` completo aguas arriba; aquí solo se recorta
    la ventana a mostrar para no anclarse a la cola de un cache viejo.
    """
    end_ts = end if end is not None else utc_now()
    if "open_time" not in df.columns:
        n = bars if bars is not None else max(20, int(round(float(days) * 6)))
        return df.tail(n).copy()
    ot = pd.to_datetime(df["open_time"], utc=True)
    clipped = df.loc[ot <= end_ts].copy()
    if clipped.empty:
        return clipped
    if bars is not None:
        return clipped.tail(max(20, int(bars))).copy()
    start = end_ts - pd.Timedelta(days=float(days))
    ot2 = pd.to_datetime(clipped["open_time"], utc=True)
    window = clipped.loc[ot2 >= start].copy()
    if len(window) < 20:
        # Fin de semana / gaps: asegurar mínimo visual
        return clipped.tail(20).copy()
    return window


def _fill_macd_cloud(ax, x: np.ndarray, macd: np.ndarray) -> None:
    """Rellena nube azul (>0) / púrpura (<0) bajo la línea MACD."""
    ax.fill_between(
        x,
        macd,
        0,
        where=(macd >= 0),
        interpolate=True,
        color=BLUE_TOP,
        alpha=0.45,
        linewidth=0,
        zorder=2,
    )
    ax.fill_between(
        x,
        macd,
        0,
        where=(macd < 0),
        interpolate=True,
        color=PURPLE_TOP,
        alpha=0.45,
        linewidth=0,
        zorder=2,
    )
    pos_edge = np.where(macd >= 0, macd, np.nan)
    neg_edge = np.where(macd < 0, macd, np.nan)
    ax.plot(x, pos_edge, color=BLUE_TOP, linewidth=1.2, solid_capstyle="round", zorder=3)
    ax.plot(x, neg_edge, color=PURPLE_TOP, linewidth=1.2, solid_capstyle="round", zorder=3)
    pos = np.where(macd >= 0, macd, np.nan)
    neg = np.where(macd < 0, macd, np.nan)
    ax.fill_between(x, pos, 0, color=BLUE_BASE, alpha=0.22, interpolate=True, zorder=1)
    ax.fill_between(x, neg, 0, color=PURPLE_BASE, alpha=0.22, interpolate=True, zorder=1)


def plot_macd_quant(
    df: pd.DataFrame,
    *,
    title: str,
    out_path: Path,
    bars: int | None = None,
    days: float = 7.0,
    end: pd.Timestamp | None = None,
    source_note: str = "m5_resample_h4",
) -> Path:
    """Dibuja panel precio+EMA200 y panel nube MACD+signal; marca últimos BUY/SELL.

    ``df`` debe ser H4 (ya resampleado). Se calcula MACD sobre todo el histórico
    y se muestra la ventana de ``days`` (o ``bars``) terminando en ``end``
    (UTC now por defecto) — no la cola ciega de un parquet stale.
    """
    work = calculate_macd(df)
    work = generate_signals(work)
    end_ts = end if end is not None else utc_now()
    show = slice_week_ending_now(
        work, days=days, bars=bars, end=end_ts
    ).reset_index(drop=True)
    if show.empty:
        raise ValueError(
            f"Ventana H4 vacía tras recorte a {end_ts.isoformat()} "
            f"(days={days}, bars={bars}). ¿Cache sin datos hasta 'now'?"
        )
    n = len(show)
    x = np.arange(n)
    macd = show["macd"].astype(float).to_numpy()
    signal = show["signal_line"].astype(float).to_numpy()

    fig, (ax1, ax2) = plt.subplots(
        2,
        1,
        figsize=(11, 6.5),
        sharex=True,
        gridspec_kw={"height_ratios": [1.85, 1.35], "hspace": 0.06},
        facecolor=BG,
    )
    for ax in (ax1, ax2):
        ax.set_facecolor(PANEL)
        ax.tick_params(colors=TEXT, labelsize=8)
        ax.grid(True, color=GRID, linewidth=0.45, alpha=0.55, linestyle="--")
        for spine in ax.spines.values():
            spine.set_color(GRID)

    ax1.plot(x, show["close"].astype(float), color=ACCENT, linewidth=1.15, label="Close H4")
    ax1.plot(x, show["trend_ema"].astype(float), color=EMA_C, linewidth=1.0, label="EMA200")
    ax1.set_ylabel("Precio", color=TEXT, fontsize=9)
    ax1.legend(
        loc="upper left",
        fontsize=8,
        facecolor=BG,
        edgecolor=GRID,
        labelcolor=TEXT,
        framealpha=0.9,
    )
    ax1.set_title(
        f"{title} H4 — MACD quant ({MACD_FAST}/{MACD_SLOW}/{MACD_SIGNAL}) · "
        f"semana · soft-filter E1 (nunca trigger)",
        color=GOLD,
        fontsize=11,
        pad=8,
    )

    _fill_macd_cloud(ax2, x, macd)
    ax2.plot(
        x,
        signal,
        color=SIGNAL_C,
        linewidth=1.35,
        label="Signal",
        zorder=4,
        solid_capstyle="round",
    )
    ax2.axhline(0, color="#6b7280", linewidth=0.9, zorder=5)
    ax2.set_ylabel("MACD", color=TEXT, fontsize=9)
    ax2.legend(
        loc="upper left",
        fontsize=8,
        facecolor=BG,
        edgecolor=GRID,
        labelcolor=TEXT,
        framealpha=0.9,
    )

    buys = show.index[show["signal"] == 1].tolist()
    sells = show.index[show["signal"] == -1].tolist()
    if buys:
        i = buys[-1]
        ax1.scatter(
            [i],
            [show.loc[i, "close"]],
            marker="o",
            s=55,
            color=DOT_UP,
            zorder=6,
            edgecolors="#fff",
            linewidths=0.4,
        )
        ax2.scatter(
            [i],
            [macd[i]],
            marker="o",
            s=48,
            color=DOT_UP,
            zorder=6,
            edgecolors="#1a1a1a",
            linewidths=0.5,
        )
        ax2.annotate(
            "BUY",
            (i, macd[i]),
            textcoords="offset points",
            xytext=(5, 10),
            color=DOT_UP,
            fontsize=8,
            fontweight="bold",
        )
    if sells:
        i = sells[-1]
        ax1.scatter(
            [i],
            [show.loc[i, "close"]],
            marker="o",
            s=55,
            color=DOT_DOWN,
            zorder=6,
            edgecolors="#fff",
            linewidths=0.4,
        )
        ax2.scatter(
            [i],
            [macd[i]],
            marker="o",
            s=48,
            color=DOT_DOWN,
            zorder=6,
            edgecolors="#1a1a1a",
            linewidths=0.5,
        )
        ax2.annotate(
            "SELL",
            (i, macd[i]),
            textcoords="offset points",
            xytext=(5, -14),
            color=DOT_DOWN,
            fontsize=8,
            fontweight="bold",
        )

    if "open_time" in show.columns:
        step = max(1, n // 6)
        ticks = list(range(0, n, step))
        if ticks[-1] != n - 1:
            ticks.append(n - 1)
        labels = []
        for i in ticks:
            t = show.loc[i, "open_time"]
            try:
                labels.append(pd.Timestamp(t).strftime("%m-%d %H:%M"))
            except (TypeError, ValueError):
                labels.append(str(i))
        ax2.set_xticks(ticks)
        ax2.set_xticklabels(labels, rotation=20, ha="right", color=TEXT)

    fig.text(
        0.5,
        0.01,
        f"H4 ({source_note}) · nube MACD · Signal blanca · soft-filter only "
        f"(nunca trigger solo) · WR/PF PENDING",
        ha="center",
        va="bottom",
        fontsize=8,
        color="#7a7a88",
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=140, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close(fig)
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Mini-chart MACD quant E1 en H4 (filtro, no trigger) — "
            "semana terminando en UTC now"
        )
    )
    parser.add_argument(
        "--symbol",
        default="btc",
        choices=sorted(SYMBOL_PARQUET.keys()),
        help="Activo: btc|us30|xau|xauusd|ukoil (default btc)",
    )
    parser.add_argument(
        "--parquet",
        type=Path,
        default=None,
        help="Ruta parquet opcional (M5/H1; se resamplea a H4; no refresca)",
    )
    parser.add_argument(
        "--days",
        type=float,
        default=7.0,
        help="Días de contexto H4 a mostrar terminando en UTC now (default 7)",
    )
    parser.add_argument(
        "--bars",
        type=int,
        default=None,
        help=f"Barras H4 visibles (override de --days; default ~{WEEK_H4_BARS})",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="PNG de salida (default live/<symbol>_h4_macd_quant.png)",
    )
    parser.add_argument(
        "--force-refresh",
        action="store_true",
        help="Forzar descarga M5/H1 hasta UTC now antes de plotear",
    )
    parser.add_argument(
        "--no-refresh",
        action="store_true",
        help="No descargar aunque el cache esté stale (solo parquet local)",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=REFRESH_LOOKBACK_DAYS,
        help=f"Días a pedir al refrescar (default {REFRESH_LOOKBACK_DAYS})",
    )
    args = parser.parse_args(argv)

    sym = normalize_symbol(args.symbol)
    file_key = SYMBOL_FILE_KEY[sym]
    end_ts = utc_now()

    # Refresh: explicit --force-refresh, or auto si cache stale (salvo --no-refresh / --parquet)
    do_refresh = False
    if args.parquet is None and not args.no_refresh:
        if args.force_refresh or cache_is_stale(sym):
            do_refresh = True
    if do_refresh:
        try:
            refresh_symbol_parquets(sym, lookback_days=max(14, int(args.lookback_days)))
        except Exception as exc:
            print(f"[refresh] ERROR: {exc}", file=sys.stderr)
            if args.force_refresh:
                return 1
            print("[refresh] Continuo con cache local...", file=sys.stderr)

    h4, parquet, source_note = load_h4(sym, args.parquet)

    bars = max(20, int(args.bars)) if args.bars is not None else None
    days = float(args.days)

    out = args.out
    if out is None:
        out = LIVE_DIR / f"{file_key}_h4_macd_quant.png"
    elif not out.is_absolute():
        out = PROJECT_ROOT / out

    title = SYMBOL_TITLE.get(sym, sym.upper())
    path = plot_macd_quant(
        h4,
        title=title,
        out_path=out,
        bars=bars,
        days=days,
        end=end_ts,
        source_note=source_note,
    )

    # Timestamps para smoke / UI
    last_h4 = None
    last_m5 = _parquet_last_ts(SYMBOL_PARQUET[sym][0])
    if "open_time" in h4.columns and not h4.empty:
        last_h4 = pd.to_datetime(h4["open_time"].iloc[-1], utc=True)
    print(f"PNG: {path}")
    print(
        f"Parquet: {parquet} -> H4 ({source_note}) | {len(h4)} barras H4 | "
        f"ventana days={days}" + (f" bars={bars}" if bars else "")
    )
    print(f"Ventana termina (UTC now): {end_ts.isoformat()}")
    print(f"Última barra H4: {last_h4}")
    print(f"Última barra M5 cache: {last_m5}")
    print(
        "Nota: MACD-quant = soft-filter E1 sobre H4; entradas E1 siguen en M5; "
        "WR/PF PENDING."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
