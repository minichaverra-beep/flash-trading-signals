"""XAUUSD / Gold market data — yfinance with Yahoo Chart API fallback (SSL-safe).

Primary ticker: GC=F (COMEX Gold futures). Spot XAUUSD=X is often 404 on Yahoo;
GC=F tracks gold closely enough for E1 M5/H1 features and live signals.
"""
from __future__ import annotations

from app.models.us30_data import (
    INTERVAL_RANGE,
    fetch_yahoo_chart,
    fetch_us30_klines as _fetch_generic_klines,
)

DEFAULT_TICKERS = ("GC=F",)  # COMEX gold futures — reliable Yahoo proxy for XAUUSD

# Re-export helpers used by callers / tests
__all__ = [
    "DEFAULT_TICKERS",
    "INTERVAL_RANGE",
    "fetch_yahoo_chart",
    "fetch_xauusd_klines",
    "fetch_yfinance_klines",
]


def fetch_xauusd_klines(
    tickers: tuple[str, ...] = DEFAULT_TICKERS,
    m5_interval: str = "5m",
    h1_interval: str = "1h",
    m5_bars: int = 200,
    h1_bars: int = 200,
) -> tuple[list[dict], list[dict], dict]:
    """
    Download gold OHLCV via Yahoo (GC=F).

    Returns (m5_proxy, h1, meta). meta includes source / ticker notes.
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
    return m5, h1, meta


fetch_yfinance_klines = fetch_xauusd_klines
