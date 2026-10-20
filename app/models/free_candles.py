"""Velas públicas cuando Yahoo HTTPS no responde. Sin clave y sin MT5.

BTC y oro: Binance sigue primero; si cae, Yahoo Chart por HTTP.
US30: Yahoo HTTP primero. Binance, OKX y Gate no listan el Dow y no se consultan.
Stooq queda el último. Cada HTTP corta a los 10 s.
Este módulo no importa broker_feed ni los loaders de Yahoo: no hay recursión.

Yahoo Chart API por HTTP (query1), sin clave y sin verificación de navegador.
Símbolos: ^DJI (Dow), GC=F (oro), BTC-USD (bitcoin).
"""
from __future__ import annotations

import json
from contextvars import ContextVar
from datetime import datetime, timedelta, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

TIMEOUT = 10
_DEPTH: ContextVar[int] = ContextVar("public_candles_depth", default=0)

PRETTY = {
    "yahoohttp": "Yahoo HTTP (Yahoo falló)",
    "binance": "Binance (Yahoo falló)",
    "okx": "OKX (Yahoo falló)",
    "stooq": "Stooq (Yahoo falló)",
    "gate": "Gate.io (Yahoo falló)",
    "coinbase": "Coinbase (Yahoo falló)",
}

# http://query1.finance.yahoo.com — el mismo chart v8, sin crumb. HTTPS ya se intentó antes.
YAHOO_HTTP = "http://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

# kind vacío + skip = no hay instrumento; no se fabrica un símbolo.
_CATALOG = {
    "BTC": [
        {"provider": "binance", "symbol": "BTCUSDT", "kind": "binance-spot"},
        {"provider": "yahoohttp", "symbol": "BTC-USD", "kind": "yahoo-http"},
        {"provider": "okx", "symbol": "BTC-USDT", "kind": "okx"},
        {"provider": "stooq", "symbol": "btcusd", "kind": "stooq"},
        {"provider": "coinbase", "symbol": "BTC-USD", "kind": "coinbase"},
    ],
    "XAUUSD": [
        {"provider": "binance", "symbol": "XAUUSDT", "kind": "binance-futures"},
        {"provider": "yahoohttp", "symbol": "GC=F", "kind": "yahoo-http"},
        {"provider": "okx", "symbol": "XAU-USDT-SWAP", "kind": "okx"},
        {"provider": "stooq", "symbol": "xauusd", "kind": "stooq"},
        {"provider": "gate", "symbol": "XAU_USDT", "kind": "gate"},
    ],
    "US30": [
        {"provider": "yahoohttp", "symbol": "^DJI", "kind": "yahoo-http"},
        {"provider": "stooq", "symbol": "^dji", "kind": "stooq"},
    ],
}


def _asset_key(asset: str) -> str:
    key = (asset or "").upper().strip()
    if key.startswith("BTC"):
        return "BTC"
    if key in ("XAU", "GOLD", "GC=F") or "XAU" in key:
        return "XAUUSD"
    if "US30" in key or key in ("YM=F", "^DJI", "DJI"):
        return "US30"
    return key


def sources_for(asset: str) -> list[dict]:
    """Orden de respaldo para `asset` (copias, sin funciones)."""
    key = _asset_key(asset)
    if key not in _CATALOG:
        raise RuntimeError(f"sin endpoint libre para {asset!r}")
    return [dict(item) for item in _CATALOG[key]]


def _reject_wrong_symbol(key: str, symbol: str | None) -> None:
    if not symbol:
        return
    up = symbol.upper()
    btc = up in ("BTCUSDT", "BTC-USDT", "BTC-USD", "BTCUSD") or up.startswith("BTC")
    if key != "BTC" and btc:
        raise RuntimeError(f"{key} no usa velas de BTC ({symbol})")


def _get_json(url: str):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 FlashSignals/1.0", "Accept": "application/json"})
    with urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode())


def _get_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 FlashSignals/1.0", "Accept": "text/csv,*/*"})
    with urlopen(req, timeout=TIMEOUT) as resp:
        raw = resp.read().decode("utf-8", "replace")
    head = raw.lstrip()[:80].lower()
    if head.startswith("<") or "verify your browser" in raw.lower() or "<html" in head:
        raise RuntimeError("Stooq devolvió HTML (verificación del navegador), no CSV")
    return raw


def _candle(ts_ms: int, o, h, l, c, volume=0) -> dict:
    ot = datetime.fromtimestamp(int(ts_ms) / 1000, tz=timezone.utc)
    return {
        "open_time": ot,
        "open": float(o),
        "high": float(h),
        "low": float(l),
        "close": float(c),
        "volume": float(volume or 0),
        "close_time": ot,
    }


def parse_binance(rows) -> list[dict]:
    """Klines de Binance: [openTime, open, high, low, close, volume, ...]."""
    out = []
    for r in rows or []:
        if r is None or len(r) < 6 or r[0] is None:
            continue
        out.append(_candle(int(r[0]), r[1], r[2], r[3], r[4], r[5]))
    return out


def parse_okx(rows) -> list[dict]:
    """Velas OKX, de la más nueva a la más vieja: [ts, o, h, l, c, vol, ...]."""
    out = []
    for r in rows or []:
        if r is None or len(r) < 6:
            continue
        out.append(_candle(int(r[0]), r[1], r[2], r[3], r[4], r[5]))
    out.sort(key=lambda c: c["open_time"])
    return out


def parse_gate(rows) -> list[dict]:
    """Velas Gate.io: {t, o, h, l, c, v} con t en segundos."""
    out = []
    for r in rows or []:
        if not isinstance(r, dict) or r.get("t") is None:
            continue
        out.append(_candle(int(r["t"]) * 1000, r["o"], r["h"], r["l"], r["c"], r.get("v")))
    out.sort(key=lambda c: c["open_time"])
    return out


def parse_coinbase(rows) -> list[dict]:
    """Velas Coinbase, de la más nueva a la más vieja: [time, low, high, open, close, volume]."""
    out = []
    for r in rows or []:
        if r is None or len(r) < 6:
            continue
        out.append(_candle(int(r[0]) * 1000, r[3], r[2], r[1], r[4], r[5]))
    out.sort(key=lambda c: c["open_time"])
    return out


def _stooq_time(date_s: str, time_s: str | None) -> datetime:
    date_s = (date_s or "").strip()
    time_s = (time_s or "").strip()
    if time_s:
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y%m%d %H%M%S", "%Y-%m-%d %H:%M", "%Y%m%d %H%M"):
            try:
                return datetime.strptime(f"{date_s} {time_s}", fmt).replace(tzinfo=timezone.utc)
            except ValueError:
                continue
    for fmt in ("%Y-%m-%d", "%Y%m%d"):
        try:
            return datetime.strptime(date_s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    raise ValueError(f"fecha Stooq no reconocida: {date_s!r} {time_s!r}")


def parse_stooq(text: str) -> list[dict]:
    """CSV de Stooq (diario o intradía). Rechaza HTML y 'No data'."""
    if text is None:
        raise RuntimeError("Stooq vacío")
    raw = text.lstrip("\ufeff").strip()
    if not raw or raw.lower().startswith("no data"):
        raise RuntimeError("Stooq sin datos")
    if raw.startswith("<") or "<html" in raw[:80].lower():
        raise RuntimeError("Stooq devolvió HTML (verificación del navegador), no CSV")
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    header = [h.strip().lower() for h in lines[0].split(",")]
    start = 1 if "open" in header or "date" in header else 0
    if start == 0:
        idx = {"date": 0, "time": None, "open": 1, "high": 2, "low": 3, "close": 4, "volume": 5}
    else:
        def col(name, fallback=None):
            return header.index(name) if name in header else fallback
        idx = {
            "date": col("date", 0),
            "time": col("time"),
            "open": col("open"),
            "high": col("high"),
            "low": col("low"),
            "close": col("close"),
            "volume": col("volume"),
        }
    if None in (idx["open"], idx["high"], idx["low"], idx["close"]):
        raise RuntimeError("Stooq CSV sin OHLC")
    out = []
    for ln in lines[start:]:
        cells = [c.strip() for c in ln.split(",")]
        if len(cells) <= idx["close"]:
            continue
        try:
            ot = _stooq_time(cells[idx["date"]], cells[idx["time"]] if idx["time"] is not None else None)
            vol = cells[idx["volume"]] if idx["volume"] is not None and idx["volume"] < len(cells) else 0
            out.append({
                "open_time": ot,
                "open": float(cells[idx["open"]]),
                "high": float(cells[idx["high"]]),
                "low": float(cells[idx["low"]]),
                "close": float(cells[idx["close"]]),
                "volume": float(vol or 0),
                "close_time": ot,
            })
        except (TypeError, ValueError):
            continue
    out.sort(key=lambda c: c["open_time"])
    return out


def quotes_are_live(candles: list[dict], sample: int = 8) -> bool:
    """True si hay un precio de mercado de verdad, no una cotización clavada."""
    if not candles or len(candles) < 2:
        return False
    tail = candles[-sample:]
    closes = []
    for c in tail:
        try:
            close = float(c["close"])
            high = float(c["high"])
            low = float(c["low"])
        except (KeyError, TypeError, ValueError):
            return False
        if close <= 0 or high <= 0 or low <= 0:
            return False
        closes.append(close)
        if high > low:
            return True
    return len({round(v, 8) for v in closes}) >= 2


def align_last_close(candles: list[dict], price) -> list[dict]:
    """Mueve las velas para que el último cierre coincida con el precio de la señal."""
    if not candles or price is None:
        return candles
    try:
        target = float(price)
    except (TypeError, ValueError):
        return candles
    if target <= 0:
        return candles
    delta = target - float(candles[-1]["close"])
    if abs(delta) < 1e-8:
        return candles
    out = []
    for c in candles:
        n = dict(c)
        for k in ("open", "high", "low", "close"):
            n[k] = float(n[k]) + delta
        out.append(n)
    return out


def _binance(url: str) -> list[dict]:
    payload = _get_json(url)
    if isinstance(payload, dict):
        raise RuntimeError(payload.get("msg") or "Binance sin velas")
    return parse_binance(payload)


def _okx(inst: str, bars: int) -> list[dict]:
    payload = _get_json(
        f"https://www.okx.com/api/v5/market/candles?instId={quote(inst, safe='')}&bar=5m&limit={int(bars)}"
    )
    if str(payload.get("code")) != "0":
        raise RuntimeError(payload.get("msg") or "OKX sin velas")
    return parse_okx(payload.get("data"))


def _gate(contract: str, bars: int) -> list[dict]:
    return parse_gate(_get_json(
        "https://api.gateio.ws/api/v4/futures/usdt/candlesticks"
        f"?contract={quote(contract, safe='')}&interval=5m&limit={int(bars)}"
    ))


def parse_yahoo_chart(payload) -> list[dict]:
    """Chart v8 de Yahoo: timestamp + quote OHLC. Descarta huecos y una serie plana."""
    block = (((payload or {}).get("chart") or {}).get("result") or [None])[0]
    if not block:
        err = ((payload or {}).get("chart") or {}).get("error") or {}
        raise RuntimeError(err.get("description") or "Yahoo HTTP sin velas")
    quote = (((block.get("indicators") or {}).get("quote") or [{}])[0]) or {}
    out = []
    timestamps = block.get("timestamp") or []
    for i, ts in enumerate(timestamps):
        if ts is None:
            continue
        try:
            o, h, l, c = quote.get("open", [])[i], quote.get("high", [])[i], quote.get("low", [])[i], quote.get("close", [])[i]
        except IndexError:
            continue
        if None in (o, h, l, c):
            continue
        vol = 0
        vols = quote.get("volume") or []
        if i < len(vols) and vols[i]:
            vol = vols[i]
        out.append(_candle(int(ts) * 1000, o, h, l, c, vol))
    return out


def _yahoo_http(symbol: str, bars: int) -> list[dict]:
    url = (
        f"{YAHOO_HTTP.format(symbol=quote(symbol, safe=''))}"
        "?interval=5m&range=5d"
    )
    return parse_yahoo_chart(_get_json(url))[-int(bars):]


def _coinbase(bars: int) -> list[dict]:
    rows = parse_coinbase(_get_json(
        "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=300"
    ))
    return rows[-int(bars):]


def _stooq(symbol: str, minutes: int) -> list[dict]:
    return parse_stooq(_get_text(f"https://stooq.com/q/d/l/?s={quote(symbol, safe='')}&i={int(minutes)}"))


def _latest(item: dict, bars: int) -> list[dict]:
    kind, sym, n = item["kind"], item["symbol"], int(bars)
    if kind == "binance-spot":
        return _binance(f"https://api.binance.com/api/v3/klines?symbol={sym}&interval=5m&limit={n}")
    if kind == "binance-futures":
        return _binance(f"https://fapi.binance.com/fapi/v1/klines?symbol={sym}&interval=5m&limit={n}")
    if kind == "okx":
        return _okx(sym, n)
    if kind == "stooq":
        return _stooq(sym, 5)[-n:]
    if kind == "gate":
        return _gate(sym, n)
    if kind == "coinbase":
        return _coinbase(n)
    if kind == "yahoo-http":
        return _yahoo_http(sym, n)
    raise RuntimeError(f"fuente desconocida: {kind}")


def _binance_since(symbol: str, since: datetime, futures: bool) -> list[dict]:
    rows: list[dict] = []
    start_ms = int(since.timestamp() * 1000)
    base = "https://fapi.binance.com/fapi/v1/klines" if futures else "https://api.binance.com/api/v3/klines"
    for _ in range(12):
        payload = _get_json(f"{base}?symbol={symbol}&interval=5m&startTime={start_ms}&limit=1000")
        if isinstance(payload, dict):
            raise RuntimeError(payload.get("msg") or "Binance sin velas")
        parsed = parse_binance(payload)
        if not parsed:
            break
        rows.extend(parsed)
        if len(payload) < 1000:
            break
        start_ms = int(payload[-1][0]) + 1
    return rows


def _okx_since(inst: str, since: datetime) -> list[dict]:
    rows: list[dict] = []
    after = int(datetime.now(timezone.utc).timestamp() * 1000) + 60_000
    since_ms = int(since.timestamp() * 1000)
    for _ in range(12):
        payload = _get_json(
            "https://www.okx.com/api/v5/market/history-candles"
            f"?instId={quote(inst, safe='')}&bar=5m&after={after}&limit=100"
        )
        if str(payload.get("code")) != "0":
            raise RuntimeError(payload.get("msg") or "OKX sin velas")
        data = payload.get("data") or []
        batch = parse_okx(data)
        if not batch:
            break
        rows.extend(batch)
        oldest = min(int(r[0]) for r in data)
        if oldest <= since_ms:
            break
        after = oldest
    rows.sort(key=lambda c: c["open_time"])
    return rows


def _coinbase_since(since: datetime) -> list[dict]:
    rows: list[dict] = []
    start = since.astimezone(timezone.utc)
    end_limit = datetime.now(timezone.utc)
    for _ in range(12):
        if start >= end_limit:
            break
        end = min(start + timedelta(minutes=5 * 300), end_limit)
        url = (
            "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=300"
            f"&start={quote(start.strftime('%Y-%m-%dT%H:%M:%SZ'))}"
            f"&end={quote(end.strftime('%Y-%m-%dT%H:%M:%SZ'))}"
        )
        rows.extend(parse_coinbase(_get_json(url)))
        if end >= end_limit:
            break
        start = end
    rows.sort(key=lambda c: c["open_time"])
    return rows


def _since(item: dict, since: datetime) -> list[dict]:
    kind, sym = item["kind"], item["symbol"]
    if kind == "binance-spot":
        return _binance_since(sym, since, False)
    if kind == "binance-futures":
        return _binance_since(sym, since, True)
    if kind == "okx":
        return _okx_since(sym, since)
    if kind == "stooq":
        return [c for c in _stooq(sym, 5) if c["open_time"] >= since]
    if kind == "gate":
        return [c for c in _gate(sym, 300) if c["open_time"] >= since]
    if kind == "coinbase":
        return [c for c in _coinbase_since(since) if c["open_time"] >= since]
    if kind == "yahoo-http":
        return [c for c in _yahoo_http(sym, 300) if c["open_time"] >= since]
    raise RuntimeError(f"fuente desconocida: {kind}")


def _run(asset: str, fetch_of) -> tuple[list[dict], dict]:
    if _DEPTH.get():
        raise RuntimeError("recursión en el fallback de velas")
    token = _DEPTH.set(_DEPTH.get() + 1)
    key = _asset_key(asset)
    failures: list[str] = []
    tried_providers: set[str] = set()
    try:
        for item in sources_for(key):
            provider = item["provider"]
            if provider in tried_providers:
                raise RuntimeError("recursión en el fallback de velas")
            tried_providers.add(provider)
            pretty = PRETTY[item["provider"]]
            if item.get("skip"):
                line = f"{pretty}: {item['skip']}"
                failures.append(line)
                print(f"[datos] {key}: {line}", flush=True)
                continue
            _reject_wrong_symbol(key, item.get("symbol"))
            shown = f"{pretty} {item['symbol']}".strip()
            try:
                rows = fetch_of(item)
                if len(rows) < 2:
                    raise RuntimeError(f"solo {len(rows)} velas")
                if not quotes_are_live(rows):
                    raise RuntimeError("sin precio real de mercado")
                info = {
                    "provider": item["provider"],
                    "symbol": item["symbol"],
                    "label": shown,
                    "failures": list(failures),
                }
                print(f"[datos] Velas {key}: {shown}", flush=True)
                return rows, info
            except (URLError, HTTPError, TimeoutError, OSError, RuntimeError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
                if "recursión en el fallback" in str(exc):
                    raise
                line = f"{shown}: {exc}"
                failures.append(line)
                print(f"[datos] {key}: {line}", flush=True)
        raise RuntimeError(
            f"No se pudieron obtener velas de {key}. Fuentes probadas: " + "; ".join(failures)
        )
    finally:
        _DEPTH.reset(token)


def fetch_public_m5(asset: str, bars: int = 300) -> tuple[list[dict], dict]:
    """(velas M5, info). Info: provider, symbol, label, failures. Lanza si nadie responde."""
    n = max(10, min(int(bars), 300))
    rows, info = _run(asset, lambda item: _latest(item, n))
    return rows[-n:], info


def fetch_public_since(asset: str, since: datetime, now: datetime | None = None) -> tuple[list[dict], dict]:
    """Velas M5 desde `since`. `now` se acepta por compatibilidad con el gráfico de resultado."""
    del now
    if since.tzinfo is None:
        since = since.replace(tzinfo=timezone.utc)
    rows, info = _run(asset, lambda item: _since(item, since))
    return [c for c in rows if c["open_time"] >= since], info


def fetch_free_m5(asset: str, bars: int = 300) -> tuple[list[dict], str]:
    """(velas M5, rótulo). Lanza RuntimeError si ningún endpoint libre responde."""
    rows, info = fetch_public_m5(asset, bars)
    return rows, info["label"]
