"""XAUUSD / Gold market data — yfinance with Yahoo Chart API fallback (SSL-safe).

Primary ticker: GC=F (COMEX Gold futures). Spot XAUUSD=X is often 404 on Yahoo.
GC=F cotiza con premium (basis/contango, ~$20–40) sobre el spot: las velas se
desplazan al spot live (gold-api / Binance XAUT) para que precio y niveles
coincidan con el broker.
"""
from __future__ import annotations

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from app.models.us30_data import (
    INTERVAL_RANGE,
    fetch_yahoo_chart,
    fetch_yahoo_klines as _fetch_generic_klines,
    shift_candles,
)

DEFAULT_TICKERS = ("GC=F",)  # COMEX gold futures — reliable Yahoo proxy for XAUUSD

SPOT_SOURCES = (
    ("gold-api", "https://api.gold-api.com/price/XAU", lambda p: p["price"]),
    ("binance XAUTUSDT", "https://api.binance.com/api/v3/ticker/price?symbol=XAUTUSDT",
     lambda p: p["price"]),
)
# Basis GC=F − spot fuera de este rango = dato sospechoso → no ajustar
MAX_ABS_BASIS = 150.0

# Re-export helpers used by callers / tests
__all__ = [
    "DEFAULT_TICKERS",
    "INTERVAL_RANGE",
    "fetch_spot_xau",
    "fetch_yahoo_chart",
    "fetch_xauusd_klines",
    "fetch_yfinance_klines",
    "shift_candles",
]


def fetch_spot_xau() -> tuple[float | None, str | None, list[str]]:
    """Spot XAU/USD live. Returns (price, source, notes)."""
    notes: list[str] = []
    for name, url, pick in SPOT_SOURCES:
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0 CursorTrading/1.0"})
            with urlopen(req, timeout=10) as resp:
                price = float(pick(json.loads(resp.read().decode())))
            if price > 0:
                return price, name, notes
        except (URLError, HTTPError, TimeoutError, ValueError, KeyError, TypeError) as exc:
            notes.append(f"spot {name}: {exc}")
    return None, None, notes


def fetch_xauusd_klines(
    tickers: tuple[str, ...] = DEFAULT_TICKERS,
    m5_interval: str = "5m",
    h1_interval: str = "1h",
    m5_bars: int = 200,
    h1_bars: int = 200,
    spot_adjust: bool = True,
) -> tuple[list[dict], list[dict], dict]:
    """
    Download gold OHLCV via Yahoo (GC=F), ajustado a spot si `spot_adjust`.

    Returns (m5_proxy, h1, meta). meta includes source / ticker / basis notes.
    """
    # Deduplicate while preserving order
    seen: set[str] = set()
    ordered: list[str] = []
    for t in tickers:
        if t not in seen:
            seen.add(t)
            ordered.append(t)
    if not ordered:
        ordered = list(DEFAULT_TICKERS)

    m5, h1, meta = _fetch_generic_klines(
        tickers=tuple(ordered),
        m5_interval=m5_interval,
        h1_interval=h1_interval,
        m5_bars=m5_bars,
        h1_bars=h1_bars,
    )
    meta["asset"] = "XAUUSD"
    meta["proxy_note"] = "GC=F (COMEX) as XAUUSD proxy; not broker spot"
    meta["spot_basis"] = None

    if spot_adjust and m5:
        spot, src, notes = fetch_spot_xau()
        meta["notes"].extend(notes)
        if spot is not None:
            basis = float(m5[-1]["close"]) - spot
            if abs(basis) <= MAX_ABS_BASIS:
                m5 = shift_candles(m5, -basis)
                h1 = shift_candles(h1, -basis)
                meta["spot_basis"] = round(basis, 2)
                meta["spot_source"] = src
                meta["proxy_note"] = (
                    f"GC=F ajustado a spot ({src}): basis {basis:+.2f} restado a OHLC"
                )
                meta["notes"].append(f"Spot {spot:.2f} ({src}) · basis GC=F {basis:+.2f}")
            else:
                meta["notes"].append(
                    f"Basis {basis:+.2f} fuera de rango (±{MAX_ABS_BASIS:.0f}) — sin ajuste spot"
                )
    return m5, h1, meta


fetch_yfinance_klines = fetch_xauusd_klines
