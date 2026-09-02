"""US30 market data — yfinance with Yahoo Chart API fallback (SSL-safe)."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

DEFAULT_TICKERS = ("YM=F", "^DJI")

INTERVAL_RANGE = {
    "5m": "60d",
    "15m": "60d",
    "1h": "730d",
    "60m": "730d",
}

YAHOO_CHART = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"


def _ts_to_utc(ts: int) -> datetime:
    return datetime.fromtimestamp(ts, tz=timezone.utc)


def fetch_yahoo_chart(
    ticker: str,
    interval: str = "5m",
    range_: str | None = None,
) -> list[dict]:
    """Direct Yahoo chart API (no curl) — fallback when yfinance SSL fails."""
    rng = range_ or INTERVAL_RANGE.get(interval, "60d")
    url = f"{YAHOO_CHART.format(symbol=quote(ticker, safe=''))}?interval={interval}&range={rng}"
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 CursorTrading/1.0"})
    with urlopen(req, timeout=25) as resp:
        payload = json.loads(resp.read().decode())

    result = payload.get("chart", {}).get("result")
    if not result:
        err = payload.get("chart", {}).get("error", {})
        raise RuntimeError(err.get("description", "empty chart result"))

    block = result[0]
    timestamps = block.get("timestamp") or []
    qdata = (block.get("indicators") or {}).get("quote", [{}])[0]
    opens = qdata.get("open") or []
    highs = qdata.get("high") or []
    lows = qdata.get("low") or []
    closes = qdata.get("close") or []
    volumes = qdata.get("volume") or []

    rows: list[dict] = []
    for i, ts in enumerate(timestamps):
        if ts is None:
            continue
        o, h, l, c = opens[i], highs[i], lows[i], closes[i]
        if None in (o, h, l, c):
            continue
        ot = _ts_to_utc(int(ts))
        rows.append({
            "open_time": ot,
            "open": float(o),
            "high": float(h),
            "low": float(l),
            "close": float(c),
            "volume": float(volumes[i] or 0),
            "close_time": ot,
        })
    return rows


def _df_to_candles(df, limit: int) -> list[dict]:
    if df is None or df.empty:
        return []
    if hasattr(df.columns, "levels"):
        df = df.copy()
        df.columns = [c[-1] if isinstance(c, tuple) else c for c in df.columns]
    df = df.tail(limit)
    rows = []
    for ts, row in df.iterrows():
        ot = ts.to_pydatetime()
        if ot.tzinfo is None:
            ot = ot.replace(tzinfo=timezone.utc)
        else:
            ot = ot.astimezone(timezone.utc)
        rows.append({
            "open_time": ot,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": float(row.get("Volume", 0) or 0),
            "close_time": ot,
        })
    return rows


def _download_yfinance(ticker: str, interval: str, period: str, limit: int) -> list[dict]:
    import yfinance as yf

    df = yf.download(
        ticker,
        period=period,
        interval=interval,
        progress=False,
        auto_adjust=True,
        threads=False,
    )
    if df is None or df.empty:
        return []
    return _df_to_candles(df, limit)


def fetch_us30_klines(
    tickers: tuple[str, ...] = DEFAULT_TICKERS,
    m5_interval: str = "5m",
    h1_interval: str = "1h",
    m5_bars: int = 200,
    h1_bars: int = 200,
) -> tuple[list[dict], list[dict], dict]:
    """
    Download US30 OHLCV. Tries yfinance first, then Yahoo Chart API per ticker/interval.

    Returns (m5_proxy, h1, meta).
    """
    meta: dict = {"notes": []}
    m5: list[dict] = []
    h1: list[dict] = []
    ticker_used: str | None = None
    period_map = INTERVAL_RANGE
    limit = max(m5_bars, h1_bars) + 50

    def _try_download(ticker: str, interval: str) -> list[dict]:
        period = period_map.get(interval, "60d")
        # 1) Yahoo chart API (SSL-safe via urllib)
        try:
            cand = fetch_yahoo_chart(ticker, interval, period)
            if len(cand) >= 80:
                meta["notes"].append(f"{ticker} {interval}: Yahoo API OK ({len(cand)} velas)")
                return cand[-limit:]
        except (URLError, HTTPError, RuntimeError, json.JSONDecodeError, TimeoutError) as exc:
            meta["notes"].append(f"{ticker} {interval} Yahoo API: {exc}")
        # 2) yfinance fallback
        try:
            cand = _download_yfinance(ticker, interval, period, limit)
            if len(cand) >= 80:
                meta["notes"].append(f"{ticker} {interval}: yfinance OK ({len(cand)} velas)")
                return cand
        except Exception as exc:
            meta["notes"].append(f"{ticker} {interval} yfinance: {exc}")
        return []

    for ticker in tickers:
        for interval in (m5_interval, "15m", "1h"):
            cand = _try_download(ticker, interval)
            if len(cand) < 80:
                meta["notes"].append(f"{ticker} {interval}: solo {len(cand)} velas")
                continue
            m5 = cand[-m5_bars:]
            ticker_used = ticker
            meta["m5_interval"] = interval if interval != m5_interval else m5_interval
            if interval != m5_interval:
                meta["notes"].append(f"M5 solicitado no disponible — usando {interval} como proxy")
            break
        if m5:
            break

    if not m5:
        raise RuntimeError(
            "No se pudieron obtener velas US30. "
            f"Intentos: {tickers}. Notas: {'; '.join(meta['notes'])}"
        )

    for ticker in tickers:
        cand = _try_download(ticker, h1_interval)
        if len(cand) >= 55:
            h1 = cand[-h1_bars:]
            if ticker_used is None:
                ticker_used = ticker
            meta["h1_interval"] = h1_interval
            break

    if not h1:
        bucket: dict = {}
        for c in m5:
            key = c["open_time"].replace(minute=0, second=0, microsecond=0)
            if key not in bucket:
                bucket[key] = dict(c)
            else:
                b = bucket[key]
                b["high"] = max(b["high"], c["high"])
                b["low"] = min(b["low"], c["low"])
                b["close"] = c["close"]
                b["volume"] += c["volume"]
        h1 = list(bucket.values())[-h1_bars:]
        meta["notes"].append("H1 resampleado desde velas intraday")

    meta["ticker"] = ticker_used
    meta["source"] = "yfinance/Yahoo Chart API"
    return m5, h1, meta

# Backward alias
fetch_yfinance_klines = fetch_us30_klines
