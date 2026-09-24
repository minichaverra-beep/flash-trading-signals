"""UKOIL / Brent crude — yfinance with Yahoo Chart API fallback (SSL-safe).

Primary ticker: BZ=F (ICE Brent Crude Oil futures). Broker CFDs labelled UKOIL
track Brent; CL=F is WTI and is not used as default.

Same fetch path as US30/XAU (``us30_data._fetch_generic_klines``).
"""
from __future__ import annotations

from app.models.us30_data import (
    INTERVAL_RANGE,
    fetch_yahoo_chart,
    fetch_us30_klines as _fetch_generic_klines,
)

# ICE Brent — Yahoo proxy for UK Oil / UKOIL CFD (not WTI CL=F)
DEFAULT_TICKERS = ("BZ=F",)

__all__ = [
    "DEFAULT_TICKERS",
    "INTERVAL_RANGE",
    "fetch_yahoo_chart",
    "fetch_ukoil_klines",
    "fetch_yfinance_klines",
]


def fetch_ukoil_klines(
    tickers: tuple[str, ...] = DEFAULT_TICKERS,
    m5_interval: str = "5m",
    h1_interval: str = "1h",
    m5_bars: int = 200,
    h1_bars: int = 200,
) -> tuple[list[dict], list[dict], dict]:
    """
    Download Brent OHLCV via Yahoo (BZ=F).

    Returns (m5_proxy, h1, meta). meta includes source / ticker notes.
    """
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
    meta["asset"] = "UKOIL"
    meta["proxy_note"] = "BZ=F (ICE Brent) as UKOIL proxy; not broker CFD spot; not WTI CL=F"
    return m5, h1, meta


fetch_yfinance_klines = fetch_ukoil_klines
