"""
Detecta la tendencia H1 actual de un mercado (misma fuente de velas que el pipeline E1).

Uso (lo invoca la API de Flash Signals antes del .ps1 con «Tendencia actual»):
  python -m app.controllers.detect_h1_bias --market us30

Salida: una línea `TREND_BIAS_JSON {...}` con el resultado de `decide_trend_bias`
más la fuente de velas. Exit 1 si no se pudieron cargar velas.
"""
from __future__ import annotations

import argparse
import json
import sys

from app.models.broker_feed import describe_source, load_klines
from app.models.trend_bias import decide_trend_bias

MARKER = "TREND_BIAS_JSON"


def _btc_external():
    from app.controllers.analyze_btc_m5 import fetch_klines

    return fetch_klines("BTCUSDT", "5m", 200), fetch_klines("BTCUSDT", "1h", 200), {"notes": []}


def _us30_external():
    from app.models.us30_data import DEFAULT_TICKERS, fetch_us30_klines

    return fetch_us30_klines(tickers=DEFAULT_TICKERS)


def _xauusd_external():
    from app.models.xauusd_data import DEFAULT_TICKERS, fetch_xauusd_klines

    return fetch_xauusd_klines(tickers=DEFAULT_TICKERS)


MARKETS = {
    "btc": ("BTC", _btc_external, "Binance BTCUSDT"),
    "us30": ("US30", _us30_external, "Yahoo US30"),
    "xauusd": ("XAUUSD", _xauusd_external, "Yahoo XAUUSD"),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Tendencia H1 actual → bias a forzar")
    parser.add_argument("--market", required=True, choices=sorted(MARKETS))
    args = parser.parse_args()

    asset, external, fallback_label = MARKETS[args.market]
    try:
        _m5, h1, meta = load_klines(asset, external)
    except Exception as e:  # noqa: BLE001 — cualquier fallo de feed se reporta igual
        print(f"{MARKER} {json.dumps({'ok': False, 'error': str(e)})}")
        return 1

    result = decide_trend_bias(h1)
    result.update({
        "ok": True,
        "market": args.market,
        "source": describe_source(meta, fallback_label),
        "last_h1": h1[-1]["open_time"].isoformat() if h1 else None,
    })
    print(f"{MARKER} {json.dumps(result, ensure_ascii=False)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
