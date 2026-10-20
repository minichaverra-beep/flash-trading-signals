"""US30 market data — yfinance with Yahoo Chart API fallback (SSL-safe)."""
from __future__ import annotations

import json
from contextvars import ContextVar
from datetime import datetime, timedelta, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

# Si el fallback (o yfinance) vuelve a entrar aquí, se corta con error. No se reintenta HTTPS.
_YAHOO_DEPTH: ContextVar[int] = ContextVar("yahoo_klines_depth", default=0)

DEFAULT_TICKERS = ("YM=F", "^DJI")
CASH_INDEX = "^DJI"
# Basis YM=F − ^DJI fuera de este rango = dato sospechoso → no ajustar
MAX_ABS_BASIS = 1500.0

INTERVAL_RANGE = {
    "5m": "60d",
    "15m": "60d",
    "1h": "730d",
    "60m": "730d",
}

YAHOO_TIMEOUT = 10
YAHOO_CHART_HOSTS = (
    "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}",
    "https://query2.finance.yahoo.com/v8/finance/chart/{symbol}",
)
YAHOO_CHART = YAHOO_CHART_HOSTS[0]


def _ts_to_utc(ts: int) -> datetime:
    return datetime.fromtimestamp(ts, tz=timezone.utc)


def _read_yahoo_chart(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 CursorTrading/1.0"})
    with urlopen(req, timeout=YAHOO_TIMEOUT) as resp:
        return json.loads(resp.read().decode())


def fetch_yahoo_chart(
    ticker: str,
    interval: str = "5m",
    range_: str | None = None,
) -> list[dict]:
    """Yahoo chart API v8 (query1 y, si falla, query2). No es yfinance."""
    rng = range_ or INTERVAL_RANGE.get(interval, "60d")
    last: Exception | None = None
    payload = None
    result = None
    for host in YAHOO_CHART_HOSTS:
        url = f"{host.format(symbol=quote(ticker, safe=''))}?interval={interval}&range={rng}"
        try:
            payload = _read_yahoo_chart(url)
            result = (payload.get("chart") or {}).get("result")
            if not result:
                err = (payload.get("chart") or {}).get("error") or {}
                raise RuntimeError(err.get("description", "empty chart result"))
            last = None
            break
        except (URLError, HTTPError, TimeoutError, json.JSONDecodeError, OSError, ValueError, RuntimeError) as exc:
            last = exc
            result = None
    if last is not None or not result or payload is None:
        raise RuntimeError(last or "Yahoo chart sin respuesta")

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
    """yfinance no se usa en el fallback: su ``YfData.get`` llama a ``_get_cookie_and_crumb``
    y esa ruta (HTTPS de nuevo) es la que agota la pila. Se conserva por compatibilidad
    con tests que la sustituyen; ``fetch_yahoo_klines`` no la llama.
    """
    if _YAHOO_DEPTH.get():
        raise RuntimeError("recursión en Yahoo: yfinance no puede volver a HTTPS")
    import socket

    import yfinance as yf

    old = socket.getdefaulttimeout()
    socket.setdefaulttimeout(YAHOO_TIMEOUT)
    try:
        df = yf.download(
            ticker,
            period=period,
            interval=interval,
            progress=False,
            auto_adjust=True,
            threads=False,
        )
    finally:
        socket.setdefaulttimeout(old)
    if df is None or df.empty:
        return []
    return _df_to_candles(df, limit)


def fetch_yahoo_klines(
    tickers: tuple[str, ...] = DEFAULT_TICKERS,
    m5_interval: str = "5m",
    h1_interval: str = "1h",
    m5_bars: int = 200,
    h1_bars: int = 200,
) -> tuple[list[dict], list[dict], dict]:
    """
    Download OHLCV genérico (sin ajuste spot).

    HTTPS de Yahoo una vez por ticker. Si no hay velas, un solo pase al fallback
    público (Yahoo HTTP y, si hace falta, el siguiente). No llama a yfinance:
    ese cliente vuelve a HTTPS y su ``YfData.get`` se reentra hasta agotar la pila.
    Si el fallback ya respondió, el H1 se arma desde esas velas: no se repite HTTPS.

    Returns (m5_proxy, h1, meta).
    """
    if _YAHOO_DEPTH.get():
        raise RuntimeError("recursión en Yahoo: el fallback no vuelve a HTTPS")
    token = _YAHOO_DEPTH.set(_YAHOO_DEPTH.get() + 1)
    try:
        return _fetch_yahoo_klines_once(
            tickers, m5_interval, h1_interval, m5_bars, h1_bars,
        )
    except RecursionError as exc:
        raise RuntimeError("recursión en Yahoo: el fallback no vuelve a HTTPS") from exc
    finally:
        _YAHOO_DEPTH.reset(token)


def _fetch_yahoo_klines_once(
    tickers: tuple[str, ...],
    m5_interval: str,
    h1_interval: str,
    m5_bars: int,
    h1_bars: int,
) -> tuple[list[dict], list[dict], dict]:
    meta: dict = {"notes": []}
    m5: list[dict] = []
    h1: list[dict] = []
    ticker_used: str | None = None
    period_map = INTERVAL_RANGE
    limit = max(m5_bars, h1_bars) + 50

    def _try_download(ticker: str, interval: str) -> list[dict]:
        """Un pase HTTPS (query1 y, si falla, query2). No llama a yfinance."""
        period = period_map.get(interval, "60d")
        try:
            cand = fetch_yahoo_chart(ticker, interval, period)
            if len(cand) >= 80:
                meta["notes"].append(f"{ticker} {interval}: Yahoo API OK ({len(cand)} velas)")
                return cand[-limit:]
        except (URLError, HTTPError, RuntimeError, json.JSONDecodeError, TimeoutError, OSError, RecursionError) as exc:
            meta["notes"].append(f"{ticker} {interval} Yahoo API: {exc}")
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

    from app.models.free_candles import fetch_public_m5, quotes_are_live

    if m5 and not quotes_are_live(m5):
        meta["notes"].append("Yahoo sin precio real (velas quietas)")
        m5 = []
    if not m5:
        asset = _free_asset(tickers)
        if asset:
            try:
                rows, info = fetch_public_m5(asset, max(m5_bars, 80))
                m5 = rows[-m5_bars:]
                ticker_used = info["symbol"]
                meta["m5_interval"] = "5m"
                meta["provider"] = info["provider"]
                meta["public_symbol"] = info["symbol"]
                meta["source"] = info["label"]
                meta["notes"].extend(info.get("failures") or [])
                meta["notes"].append(info["label"])
            except RecursionError as exc:
                raise RuntimeError("recursión en el fallback de velas") from exc
            except Exception as exc:
                meta["notes"].append(str(exc))

    if not m5:
        raise RuntimeError(
            "No se pudieron obtener velas. "
            f"Intentos: {tickers}. Notas: {'; '.join(meta['notes'])}"
        )

    # El fallback público ya gastó su único pase. Volver a HTTPS aquí reabre el ciclo.
    if meta.get("provider") in (None, "yahoo"):
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
    # El fallback libre ya dejó su rótulo; no volver a llamarlo Yahoo.
    meta.setdefault("provider", "yahoo")
    meta.setdefault("source", "yfinance/Yahoo Chart API")
    return m5, h1, meta


def _free_asset(tickers: tuple[str, ...]) -> str | None:
    blob = " ".join(tickers).upper()
    if "BTC" in blob:
        return "BTC"
    if "GC=F" in blob or "XAU" in blob or "GOLD" in blob:
        return "XAUUSD"
    if "YM" in blob or "DJI" in blob or "US30" in blob:
        return "US30"
    return None


def shift_candles(candles: list[dict], delta: float) -> list[dict]:
    """Copia de velas con OHLC desplazado en `delta`."""
    out = []
    for c in candles:
        n = dict(c)
        for k in ("open", "high", "low", "close"):
            if n.get(k) is not None:
                n[k] = float(n[k]) + delta
        out.append(n)
    return out


def fetch_cash_quote(symbol: str = CASH_INDEX) -> tuple[float, datetime]:
    """Última cotización del índice cash (Yahoo meta): (precio, hora UTC)."""
    url = f"{YAHOO_CHART.format(symbol=quote(symbol, safe=''))}?interval=5m&range=1d"
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 CursorTrading/1.0"})
    with urlopen(req, timeout=YAHOO_TIMEOUT) as resp:
        payload = json.loads(resp.read().decode())
    result = payload.get("chart", {}).get("result")
    if not result:
        raise RuntimeError("empty chart result")
    m = result[0]["meta"]
    return float(m["regularMarketPrice"]), _ts_to_utc(int(m["regularMarketTime"]))


def futures_basis(m5: list[dict], cash_price: float, cash_time: datetime) -> float | None:
    """Futuro − cash usando la vela del futuro vigente a la hora de la cota cash."""
    ref = None
    for c in m5:
        if c["open_time"] <= cash_time:
            ref = c
        else:
            break
    if ref is None or cash_time - ref["open_time"] > timedelta(minutes=30):
        return None
    return float(ref["close"]) - cash_price


def fetch_us30_klines(
    tickers: tuple[str, ...] = DEFAULT_TICKERS,
    m5_interval: str = "5m",
    h1_interval: str = "1h",
    m5_bars: int = 200,
    h1_bars: int = 200,
    spot_adjust: bool = True,
) -> tuple[list[dict], list[dict], dict]:
    """
    Download US30 OHLCV. YM=F cotiza con premium (fair value) sobre el Dow cash;
    si `spot_adjust`, las velas se desplazan al nivel ^DJI (lo que cotiza el broker US30).

    Returns (m5_proxy, h1, meta).
    """
    m5, h1, meta = fetch_yahoo_klines(
        tickers=tickers,
        m5_interval=m5_interval,
        h1_interval=h1_interval,
        m5_bars=m5_bars,
        h1_bars=h1_bars,
    )
    meta["spot_basis"] = None
    if meta.get("provider") not in (None, "yahoo"):
        meta["notes"].append(f"Sin ajuste spot: velas de {meta.get('source')}")
        return m5, h1, meta
    if not spot_adjust or not m5 or meta.get("ticker") == CASH_INDEX:
        return m5, h1, meta
    try:
        cash_price, cash_time = fetch_cash_quote()
    except (URLError, HTTPError, RuntimeError, KeyError, ValueError, TimeoutError) as exc:
        meta["notes"].append(f"cash {CASH_INDEX}: {exc} — sin ajuste spot")
        return m5, h1, meta
    basis = futures_basis(m5, cash_price, cash_time)
    if basis is None or abs(basis) > MAX_ABS_BASIS:
        meta["notes"].append(f"Basis {CASH_INDEX} no fiable ({basis}) — sin ajuste spot")
        return m5, h1, meta
    m5 = shift_candles(m5, -basis)
    h1 = shift_candles(h1, -basis)
    meta["spot_basis"] = round(basis, 2)
    meta["spot_source"] = CASH_INDEX
    meta["notes"].append(
        f"{CASH_INDEX} {cash_price:.2f} @ {cash_time:%H:%M} UTC · basis {basis:+.2f}"
    )
    return m5, h1, meta


# Backward alias
fetch_yfinance_klines = fetch_us30_klines
