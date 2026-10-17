"""Últimas velas M5 cuando Yahoo no puede dibujar la captura.

Sin clave: Binance (BTC y oro), OKX (oro) y Gate.io (Dow y oro).
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

TIMEOUT = 20


def _get_json(url: str):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 FlashSignals/1.0", "Accept": "application/json"})
    with urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode())


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
        f"https://www.okx.com/api/v5/market/candles?instId={inst}&bar=5m&limit={int(bars)}"
    )
    if str(payload.get("code")) != "0":
        raise RuntimeError(payload.get("msg") or "OKX sin velas")
    return parse_okx(payload.get("data"))


def _gate(contract: str, bars: int) -> list[dict]:
    return parse_gate(_get_json(
        "https://api.gateio.ws/api/v4/futures/usdt/candlesticks"
        f"?contract={contract}&interval=5m&limit={int(bars)}"
    ))


def _coinbase(bars: int) -> list[dict]:
    rows = parse_coinbase(_get_json(
        "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=300"
    ))
    return rows[-int(bars):]


def fetch_free_m5(asset: str, bars: int = 300) -> tuple[list[dict], str]:
    """(velas M5, rótulo). Lanza RuntimeError si ningún endpoint libre responde."""
    key = (asset or "").upper()
    if key.startswith("BTC"):
        key = "BTC"
    elif key in ("XAU", "GOLD", "GC=F"):
        key = "XAUUSD"
    elif "US30" in key or key in ("YM=F", "^DJI", "DJI"):
        key = "US30"
    n = max(10, min(int(bars), 300))
    attempts: list[tuple[str, object]] = []
    if key == "BTC":
        attempts = [
            ("velas Binance BTCUSDT (Yahoo no pudo la captura)",
             lambda: _binance(f"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&limit={n}")),
            ("velas Coinbase BTC-USD (Yahoo no pudo la captura)", lambda: _coinbase(n)),
        ]
    elif key == "XAUUSD":
        attempts = [
            ("velas Binance XAUUSDT (Yahoo no pudo la captura)",
             lambda: _binance(f"https://fapi.binance.com/fapi/v1/klines?symbol=XAUUSDT&interval=5m&limit={n}")),
            ("velas OKX XAU-USDT (Yahoo no pudo la captura)", lambda: _okx("XAU-USDT-SWAP", n)),
            ("velas Gate.io XAU (Yahoo no pudo la captura)", lambda: _gate("XAU_USDT", n)),
        ]
    elif key == "US30":
        attempts = [
            ("velas Gate.io US30 (Yahoo no pudo la captura)", lambda: _gate("US30_USDT", n)),
        ]
    else:
        raise RuntimeError(f"sin endpoint libre para {asset!r}")

    notes: list[str] = []
    for label, fetch in attempts:
        try:
            rows = fetch()
            if len(rows) < 2:
                raise RuntimeError(f"solo {len(rows)} velas")
            if not quotes_are_live(rows):
                raise RuntimeError("sin precio real de mercado")
            return rows[-n:], label
        except (URLError, HTTPError, TimeoutError, OSError, RuntimeError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            notes.append(f"{label.split('(')[0].strip()}: {exc}")
    raise RuntimeError("ningún endpoint libre devolvió velas (" + "; ".join(notes) + ")")
