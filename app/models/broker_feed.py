"""Velas del broker (MT5) vía el puente local de Flash Signals (mt5-bridge, ruta /rates).

Las órdenes se ejecutan en el símbolo del broker (US30m, XAUUSDm, BTCUSDm…), así que el
análisis y el chart deben usar su misma escala de precio:

1. Puente con velas suficientes → velas MT5 del símbolo del broker.
2. Puente con cotización pero sin velas suficientes → feed externo desplazado al precio
   del broker (mid bid/ask − último close externo), rotulado con el desplazamiento.
3. Sin puente → feed externo tal cual, rotulado «sin MT5».

Config por entorno (la API de Flash Signals la pasa al lanzar los .ps1):
FS_MT5_BRIDGE_URL / FS_MT5_BRIDGE_TOKEN / FS_MT5_SYMBOL_{US30,XAUUSD,BTC};
FS_BROKER_FEED=off desactiva el puente.

Modo «solo Yahoo» (Android/Termux, sin MT5): FS_DATA_SOURCE=yahoo (o FS_DISABLE_MT5=1) omite el
puente por completo (ni se intenta la conexión) y todas las velas salen de Yahoo Finance
(BTC-USD, YM=F/^DJI, GC=F/spot). Cualquier otro valor (`auto`, `mt5`, vacío) deja el
comportamiento de arriba.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_BRIDGE_URL = "http://127.0.0.1:8765"
DEFAULT_SYMBOLS = {"US30": "US30m", "XAUUSD": "XAUUSDm", "BTC": "BTCUSDm"}
EXTERNAL_LABELS = {"US30": "YM=F→^DJI", "XAUUSD": "GC=F→spot", "BTC": "Binance BTCUSDT"}
YAHOO_LABELS = {"US30": "YM=F→^DJI", "XAUUSD": "GC=F→spot", "BTC": "BTC-USD"}
YAHOO_BTC_TICKERS = ("BTC-USD",)
DATA_SOURCE_ENV = "FS_DATA_SOURCE"
DISABLE_MT5_ENV = "FS_DISABLE_MT5"
YAHOO_VALUES = ("yahoo", "yfinance", "yahoo-only")
TRUE_VALUES = ("1", "true", "yes", "on")
MIN_M5_BARS = 60
MIN_H1_BARS = 55
TIMEOUT_SEC = 8
# Desfase externo↔broker mayor que este % del precio = feed equivocado: no se desplaza.
MAX_OFFSET_PCT = 2.0
# Cotización MT5 más vieja que esto (mercado cerrado / terminal colgado) no sirve para desplazar.
MAX_QUOTE_AGE_SEC = 15 * 60
OFF_VALUES = ("0", "off", "false", "no")

Klines = tuple[list[dict], list[dict], dict]


def asset_key(asset: str | None) -> str:
    a = (asset or "").upper().strip()
    if a.startswith("BTC"):
        return "BTC"
    if a in ("XAUUSD", "XAU", "GOLD", "GC=F"):
        return "XAUUSD"
    if "US30" in a or a in ("YM=F", "^DJI", "DJI"):
        return "US30"
    return a


def yahoo_only() -> bool:
    """True con FS_DATA_SOURCE=yahoo o FS_DISABLE_MT5=1: MT5 se ignora y las velas son de Yahoo."""
    if os.environ.get(DATA_SOURCE_ENV, "").strip().lower() in YAHOO_VALUES:
        return True
    return os.environ.get(DISABLE_MT5_ENV, "").strip().lower() in TRUE_VALUES


def bridge_config(asset: str | None) -> dict | None:
    """URL, token y símbolo del broker para `asset`; None si el puente está desactivado u omitido."""
    if yahoo_only():
        return None
    if os.environ.get("FS_BROKER_FEED", "").strip().lower() in OFF_VALUES:
        return None
    key = asset_key(asset)
    symbol = (
        os.environ.get(f"FS_MT5_SYMBOL_{key}")
        or os.environ.get(f"MT5_SYMBOL_{key}")
        or DEFAULT_SYMBOLS.get(key)
    )
    if not symbol:
        return None
    url = os.environ.get("FS_MT5_BRIDGE_URL") or os.environ.get("MT5_BRIDGE_URL") or DEFAULT_BRIDGE_URL
    token = os.environ.get("FS_MT5_BRIDGE_TOKEN") or os.environ.get("MT5_BRIDGE_TOKEN") or ""
    return {"url": url.rstrip("/"), "token": token, "symbol": symbol, "asset": key}


def _post(cfg: dict, path: str, body: dict) -> dict:
    headers = {"Content-Type": "application/json"}
    if cfg.get("token"):
        headers["X-Bridge-Token"] = cfg["token"]
    req = Request(f"{cfg['url']}{path}", data=json.dumps(body).encode("utf-8"), headers=headers, method="POST")
    try:
        with urlopen(req, timeout=TIMEOUT_SEC) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        try:
            detail = json.loads(exc.read().decode("utf-8")).get("error")
        except (ValueError, OSError):
            detail = None
        raise RuntimeError(f"puente MT5 {exc.code}: {detail or exc.reason}") from None
    if not payload.get("ok"):
        raise RuntimeError(payload.get("error") or "respuesta inválida del puente MT5")
    return payload


def fetch_rates(cfg: dict, timeframe: str, count: int, until: datetime | None = None) -> dict:
    if yahoo_only():
        raise RuntimeError("MT5 deshabilitado (modo solo Yahoo: FS_DATA_SOURCE=yahoo)")
    body: dict = {"symbol": cfg["symbol"], "timeframe": timeframe, "count": int(count)}
    if until is not None:
        body["to"] = int(until.timestamp())
    return _post(cfg, "/rates", body)


def rates_to_candles(rates: list[dict]) -> list[dict]:
    out = []
    for r in rates or []:
        t = datetime.fromtimestamp(int(r["time"]), tz=timezone.utc)
        out.append({
            "open_time": t,
            "open": float(r["open"]),
            "high": float(r["high"]),
            "low": float(r["low"]),
            "close": float(r["close"]),
            "volume": float(r.get("volume") or 0),
            "close_time": t,
        })
    return out


def quote_mid(payload: dict | None, now: float | None = None) -> float | None:
    """Mid bid/ask del puente; None si falta o la cotización está vieja."""
    if not payload:
        return None
    bid, ask = payload.get("bid"), payload.get("ask")
    if not bid or not ask or bid <= 0 or ask <= 0:
        return None
    tick_time = payload.get("tickTime")
    now = datetime.now(timezone.utc).timestamp() if now is None else now
    if tick_time is not None and now - float(tick_time) > MAX_QUOTE_AGE_SEC:
        return None
    return (float(bid) + float(ask)) / 2


def broker_offset(external_close: float, broker_price: float) -> float | None:
    """broker − externo; None si el desfase es absurdo (otro instrumento / dato roto)."""
    if external_close <= 0 or broker_price <= 0:
        return None
    off = broker_price - external_close
    if abs(off) / broker_price * 100 > MAX_OFFSET_PCT:
        return None
    return off


def shift_candles(candles: list[dict], delta: float) -> list[dict]:
    out = []
    for c in candles:
        n = dict(c)
        for k in ("open", "high", "low", "close"):
            if n.get(k) is not None:
                n[k] = float(n[k]) + delta
        out.append(n)
    return out


def format_offset(asset: str, offset: float) -> str:
    key = asset_key(asset)
    if key == "US30":
        return f"{offset:+.1f} pts"
    if key == "XAUUSD":
        return f"{offset:+.2f} $"
    return f"{offset:+.0f} $"


def feed_info(source: str, asset: str, symbol: str | None, offset: float | None = None) -> dict:
    """Metadatos de la fuente de velas + rótulo para el chart/reporte."""
    key = asset_key(asset)
    ext = EXTERNAL_LABELS.get(key, key)
    if source == "yahoo":
        label = f"velas Yahoo {YAHOO_LABELS.get(key, key)} (solo Yahoo, sin MT5: precio puede diferir del broker)"
    elif source == "mt5":
        label = f"velas MT5 {symbol}"
    elif source == "external_shifted":
        label = f"velas {ext} ajustadas {format_offset(key, offset or 0.0)} a {symbol}"
    else:
        label = f"velas {ext} (sin MT5: precio puede diferir del broker)"
    return {
        "source": source, "symbol": symbol, "offset": offset, "label": label,
        "broker": source not in ("external", "yahoo"),
    }


def yahoo_klines(asset: str, m5_bars: int = 200, h1_bars: int = 200) -> Klines:
    """Velas M5/H1 solo de Yahoo para `asset` (BTC-USD, YM=F/^DJI, GC=F/spot). Lanza RuntimeError si Yahoo falla."""
    key = asset_key(asset)
    if key == "BTC":
        from app.models.us30_data import fetch_yahoo_klines

        m5, h1, meta = fetch_yahoo_klines(YAHOO_BTC_TICKERS, m5_bars=m5_bars, h1_bars=h1_bars)
        meta["asset"] = "BTC"
        return m5, h1, meta
    if key == "US30":
        from app.models.us30_data import fetch_us30_klines

        return fetch_us30_klines(m5_bars=m5_bars, h1_bars=h1_bars)
    if key == "XAUUSD":
        from app.models.xauusd_data import fetch_xauusd_klines

        return fetch_xauusd_klines(m5_bars=m5_bars, h1_bars=h1_bars)
    raise RuntimeError(f"mercado sin ticker de Yahoo: {asset!r}")


def load_broker_klines(
    cfg: dict, m5_bars: int, h1_bars: int, until: datetime | None = None,
) -> tuple[list[dict], list[dict], dict]:
    """(m5, h1, payload_m5) desde MT5; lanza si el puente falla."""
    p5 = fetch_rates(cfg, "M5", m5_bars, until)
    p1 = fetch_rates(cfg, "H1", h1_bars, until)
    return rates_to_candles(p5.get("rates")), rates_to_candles(p1.get("rates")), p5


def _load_yahoo_only(key: str, external_fetch: Callable[[], Klines], m5_bars: int, h1_bars: int) -> Klines:
    """Modo solo Yahoo: sin puente, sin reintentos. BTC pasa de Binance a Yahoo (BTC-USD); US30/XAUUSD ya son Yahoo."""
    if key == "BTC":
        m5, h1, meta = yahoo_klines(key, m5_bars, h1_bars)
    else:
        m5, h1, meta = external_fetch()
    meta = dict(meta or {})
    meta["notes"] = ["Modo solo Yahoo (FS_DATA_SOURCE=yahoo): MT5 omitido"] + list(meta.get("notes") or [])
    meta["feed"] = feed_info("yahoo", key, None)
    return m5, h1, meta


def load_klines(
    asset: str,
    external_fetch: Callable[[], Klines],
    *,
    m5_bars: int = 200,
    h1_bars: int = 200,
    until: datetime | None = None,
) -> Klines:
    """Velas M5/H1 en la escala del broker (ver docstring del módulo). meta['feed'] describe la fuente."""
    key = asset_key(asset)
    if yahoo_only():
        return _load_yahoo_only(key, external_fetch, m5_bars, h1_bars)
    cfg = bridge_config(key)
    notes: list[str] = []
    quote_payload = None
    if cfg is not None:
        try:
            m5, h1, quote_payload = load_broker_klines(cfg, m5_bars, h1_bars, until)
            if len(m5) >= MIN_M5_BARS and len(h1) >= MIN_H1_BARS:
                mid = quote_mid(quote_payload)
                notes.append(
                    f"MT5 {cfg['symbol']}: {len(m5)} velas M5 / {len(h1)} H1"
                    + (f" · bid/ask {quote_payload['bid']}/{quote_payload['ask']}" if mid else "")
                )
                meta = {
                    "notes": notes,
                    "ticker": cfg["symbol"],
                    "m5_interval": "5m",
                    "h1_interval": "1h",
                    "source": f"MT5 {cfg['symbol']}",
                    "feed": feed_info("mt5", key, cfg["symbol"]),
                    "broker_quote": {"bid": quote_payload.get("bid"), "ask": quote_payload.get("ask"), "mid": mid},
                }
                return m5, h1, meta
            notes.append(f"MT5 {cfg['symbol']}: solo {len(m5)} velas M5 / {len(h1)} H1")
        except (URLError, RuntimeError, TimeoutError, OSError, ValueError, KeyError) as exc:
            notes.append(f"MT5 {cfg['symbol']} no disponible: {exc}")

    m5, h1, meta = external_fetch()
    meta = dict(meta or {})
    meta["notes"] = list(meta.get("notes") or []) + notes
    mid = quote_mid(quote_payload) if until is None else None
    off = broker_offset(float(m5[-1]["close"]), mid) if (mid and m5) else None
    if off is not None:
        m5, h1 = shift_candles(m5, off), shift_candles(h1, off)
        meta["feed"] = feed_info("external_shifted", key, cfg["symbol"], off)
        meta["notes"].append(f"Velas desplazadas {format_offset(key, off)} al mid MT5 {mid:.2f}")
    else:
        meta["feed"] = feed_info("external", key, cfg["symbol"] if cfg else None)
    return m5, h1, meta


def describe_source(meta: dict, fallback: str) -> str:
    """Texto «Fuente» del reporte a partir de meta['feed']."""
    feed = meta.get("feed") or {}
    if feed.get("source") == "mt5":
        return f"MT5 {feed.get('symbol')} (broker, M5/H1)"
    if feed.get("source") == "yahoo":
        return f"{meta.get('ticker') or fallback} (solo Yahoo) · sin MT5 (precio puede diferir del broker)"
    if feed.get("source") == "external_shifted":
        return f"{fallback} · {feed.get('label')}"
    return f"{fallback} · sin MT5 (precio puede diferir del broker)"
