"""Respaldo público si Yahoo falla: orden, símbolos y cero MT5 / cero recursión."""
from __future__ import annotations

import json
from urllib.parse import quote

import pytest

from app.models import broker_feed as bf
from app.models import free_candles as fc


class _Resp:
    def __init__(self, raw: bytes):
        self._raw = raw

    def read(self):
        return self._raw

    def __enter__(self):
        return self

    def __exit__(self, *_a):
        return False


def _klines(n=4, price="100"):
    rows = []
    for i in range(n):
        px = str(100 + i)
        rows.append([1_700_000_000_000 + i * 300_000, px, str(float(px) + 2), str(float(px) - 1), px, "3"])
    return rows


STOOQ = (
    "Date,Time,Open,High,Low,Close,Volume\n"
    "2026-10-01,16:00:00,42000,42100,41900,42050,10\n"
    "2026-10-01,16:05:00,42050,42200,42000,42100,11\n"
)


def _yahoo_payload(n=6, close0=42000.0):
    return {
        "chart": {
            "result": [{
                "timestamp": [1_700_000_000 + i * 300 for i in range(n)],
                "indicators": {"quote": [{
                    "open": [close0 + i for i in range(n)],
                    "high": [close0 + i + 2 for i in range(n)],
                    "low": [close0 + i - 1 for i in range(n)],
                    "close": [close0 + i for i in range(n)],
                    "volume": [1] * n,
                }]},
            }],
        }
    }


def test_mapeo_por_simbolo():
    btc = fc.sources_for("BTC")
    assert btc[0]["symbol"] == "BTCUSDT" and btc[0]["kind"] == "binance-spot"
    assert btc[1] == {"provider": "yahoohttp", "symbol": "BTC-USD", "kind": "yahoo-http"}
    assert btc[2]["symbol"] == "BTC-USDT"
    xau = fc.sources_for("GC=F")
    assert xau[0] == {"provider": "binance", "symbol": "XAUUSDT", "kind": "binance-futures"}
    assert xau[1] == {"provider": "yahoohttp", "symbol": "GC=F", "kind": "yahoo-http"}
    assert xau[2]["symbol"] == "XAU-USDT-SWAP"
    us = fc.sources_for("US30")
    assert us[0] == {"provider": "yahoohttp", "symbol": "^DJI", "kind": "yahoo-http"}
    assert us[1]["symbol"] == "^dji" and us[1]["kind"] == "stooq"
    assert all(s["provider"] not in ("binance", "okx", "gate") for s in us)
    assert all(not s["symbol"] or "BTC" not in s["symbol"].upper() for s in us)


def test_stooq_html_no_es_csv():
    with pytest.raises(RuntimeError, match="HTML"):
        fc.parse_stooq("<html>verify your browser</html>")
    rows = fc.parse_stooq(STOOQ)
    assert len(rows) == 2 and rows[-1]["close"] == 42100


def test_us30_no_pide_binance_y_yahoo_http_responde(monkeypatch):
    urls = []

    def open_url(req, timeout=10):
        url = req.full_url
        urls.append(url)
        assert "BTC" not in url.upper()
        assert "binance" not in url and "okx.com" not in url and "gateio" not in url
        assert timeout <= 12
        assert url.startswith("http://query1.finance.yahoo.com")
        assert "%5EDJI" in url or "^DJI" in url
        return _Resp(json.dumps(_yahoo_payload(6, 52500)).encode())

    monkeypatch.setattr(fc, "urlopen", open_url)
    rows, info = fc.fetch_public_m5("US30", 4)
    assert info["provider"] == "yahoohttp" and info["symbol"] == "^DJI"
    assert "Yahoo HTTP" in info["label"]
    assert info["failures"] == []
    assert len(rows) == 6 and rows[-1]["close"] == 52505
    assert {"open_time", "open", "high", "low", "close"} <= set(rows[-1])
    assert len(urls) == 1


def test_btc_y_oro_usan_yahoo_http_si_binance_falla(monkeypatch):
    def run(asset, symbol, close0, banned):
        urls = []

        def open_url(req, timeout=10):
            url = req.full_url
            urls.append(url)
            assert timeout <= 12
            if "binance.com" in url:
                raise TimeoutError("binance caido")
            if url.startswith("http://query1.finance.yahoo.com") and quote(symbol, safe="") in url:
                return _Resp(json.dumps(_yahoo_payload(5, close0)).encode())
            raise TimeoutError(url)

        monkeypatch.setattr(fc, "urlopen", open_url)
        rows, info = fc.fetch_public_m5(asset, 3)
        assert info["provider"] == "yahoohttp" and info["symbol"] == symbol
        assert rows[-1]["close"] == close0 + 4
        assert any("binance.com" in u for u in urls)
        assert urls[-1].startswith("http://query1.finance.yahoo.com")
        assert banned not in info["symbol"]

    run("BTC", "BTC-USD", 80000, "US30")
    run("XAUUSD", "GC=F", 4100, "BTC")


def test_us30_yahoo_http_escribe_el_png(monkeypatch, tmp_path):
    """Sin velas de Yahoo HTTPS, el PNG de entrada de US30 sale de Yahoo HTTP."""
    def open_url(req, timeout=10):
        url = req.full_url
        assert "binance" not in url and "okx.com" not in url
        assert timeout <= 12
        return _Resp(json.dumps(_yahoo_payload(40, 52000)).encode())

    monkeypatch.setattr(fc, "urlopen", open_url)
    from app.views.illustrate_high_entry import write_entry_overlay_charts

    out = tmp_path / "us30_m5_chart_annotated.png"
    written = write_entry_overlay_charts(
        {"m5": [], "price": 52039, "price_decimals": 1, "setup": {"direction": "SHORT"}},
        {
            "direction": "SHORT",
            "entry": 52020,
            "sl": 52080,
            "tp": 51940,
            "dec": 1,
            "ahora_action": "ESPERAR",
        },
        asset="US30",
        main_chart_path=None,
        annotated_path=out,
        dpi=50,
    )
    assert written["annotated_chart"] and out.is_file() and out.stat().st_size > 2000


def test_yahoo_falla_btc_cae_a_binance_sin_mt5_ni_recursion(monkeypatch):
    monkeypatch.setenv("FS_DATA_SOURCE", "yahoo")
    monkeypatch.setattr(bf, "_post", lambda *_a, **_k: pytest.fail("no debe llamar MT5"))
    monkeypatch.setattr(bf, "urlopen", lambda *_a, **_k: pytest.fail("no debe abrir el puente"))
    monkeypatch.setattr("app.models.us30_data.urlopen", lambda *_a, **_k: (_ for _ in ()).throw(TimeoutError("yahoo")))
    monkeypatch.setattr("app.models.us30_data._download_yfinance", lambda *_a, **_k: [])
    seen = []

    def open_url(req, timeout=10):
        url = req.full_url
        seen.append(url)
        assert "8765" not in url and "8766" not in url
        assert timeout <= 12
        if "api.binance.com" in url and "symbol=BTCUSDT" in url and "interval=5m" in url:
            return _Resp(json.dumps(_klines()).encode())
        raise TimeoutError(url)

    monkeypatch.setattr(fc, "urlopen", open_url)
    _m5, _h1, meta = bf.load_klines("BTC", lambda: pytest.fail("el loader de Binance no debe reentrar"))
    assert meta["feed"]["source"] == "binance"
    assert "Binance (Yahoo falló)" in meta["feed"]["label"]
    assert "solo Yahoo" not in bf.describe_source(meta, "Binance BTCUSDT")
    assert seen.count(seen[0]) == 1
    assert all("BTCUSDT" in u for u in seen)


def test_yahoo_falla_binance_escribe_el_png_con_ese_precio(monkeypatch, tmp_path):
    """La corrida sin MT5: si Yahoo no responde, Binance deja velas, precio y el PNG de la tarjeta."""
    monkeypatch.setenv("FS_DATA_SOURCE", "yahoo")
    monkeypatch.setenv("FS_DISABLE_MT5", "1")
    monkeypatch.setattr(bf, "_post", lambda *_a, **_k: pytest.fail("no debe llamar MT5"))
    monkeypatch.setattr(bf, "urlopen", lambda *_a, **_k: pytest.fail("no debe abrir el puente"))
    monkeypatch.setattr("app.models.us30_data.urlopen", lambda *_a, **_k: (_ for _ in ()).throw(TimeoutError("yahoo")))
    monkeypatch.setattr("app.models.us30_data._download_yfinance", lambda *_a, **_k: [])

    def open_url(req, timeout=10):
        url = req.full_url
        assert timeout <= 12
        assert "8765" not in url and "8766" not in url
        if "api.binance.com" in url and "symbol=BTCUSDT" in url:
            return _Resp(json.dumps(_klines(40)).encode())
        raise TimeoutError("yahoo")

    monkeypatch.setattr(fc, "urlopen", open_url)
    m5, _h1, meta = bf.load_klines("BTC", lambda: pytest.fail("el loader de Binance no debe reentrar"))
    price = float(m5[-1]["close"])
    assert meta["feed"]["source"] == "binance"
    assert price == 139.0
    from app.views.illustrate_high_entry import write_entry_overlay_charts

    out = tmp_path / "btc_m5_chart_annotated.png"
    written = write_entry_overlay_charts(
        {
            "m5": m5,
            "price": price,
            "price_decimals": 1,
            "feed": meta["feed"],
            "setup": {"direction": "SHORT"},
        },
        {
            "direction": "SHORT",
            "entry": price - 10,
            "sl": price + 20,
            "tp": price - 40,
            "dec": 1,
            "ahora_action": "ESPERAR",
        },
        asset="BTC",
        main_chart_path=None,
        annotated_path=out,
        dpi=50,
    )
    png = written["annotated_chart"]
    assert png and out.is_file() and out.stat().st_size > 2000


def test_todo_falla_error_en_espanol(monkeypatch):
    def down(req, timeout=10):
        raise TimeoutError("timeout")

    monkeypatch.setattr(fc, "urlopen", down)
    with pytest.raises(RuntimeError, match="Fuentes probadas") as exc:
        fc.fetch_public_m5("US30", 20)
    msg = str(exc.value)
    assert "US30" in msg and "Yahoo HTTP" in msg and "Stooq" in msg
    assert "Binance" not in msg and "OKX" not in msg and "BTCUSDT" not in msg


def test_sin_recursion(monkeypatch):
    def reenter(req, timeout=10):
        fc.fetch_public_m5("BTC", 20)

    monkeypatch.setattr(fc, "urlopen", reenter)
    with pytest.raises(RuntimeError, match="recursión"):
        fc.fetch_public_m5("BTC", 20)


def test_stooq_html_no_repite_el_fetch(monkeypatch):
    """HTML de Stooq cierra ese proveedor. No se relanza la cadena completa."""
    runs = {"n": 0}
    real = fc._run

    def wrapped(asset, fetch_of):
        runs["n"] += 1
        if runs["n"] > 1:
            raise AssertionError("el fallback se llamó otra vez")
        return real(asset, fetch_of)

    per_provider: dict[str, int] = {}

    def open_url(req, timeout=10):
        url = req.full_url
        kind = "yahoohttp" if url.startswith("http://query1.finance.yahoo.com") else "stooq" if "stooq.com" in url else url
        per_provider[kind] = per_provider.get(kind, 0) + 1
        if per_provider[kind] > 1:
            raise AssertionError(f"{kind} se consultó más de una vez")
        if "stooq.com" in url:
            return _Resp(b"<html>verify your browser</html>")
        raise TimeoutError("yahoo http")

    monkeypatch.setattr(fc, "_run", wrapped)
    monkeypatch.setattr(fc, "urlopen", open_url)
    with pytest.raises(RuntimeError, match="HTML"):
        fc.fetch_public_m5("US30", 20)
    assert runs["n"] == 1
    assert per_provider == {"yahoohttp": 1, "stooq": 1}
    assert "binance" not in per_provider


def test_https_falla_un_http_y_no_vuelve_a_https(monkeypatch):
    """Yahoo HTTPS cae: un HTTP ^DJI. yfinance no reentra, y el H1 no repite HTTPS."""
    from app.models import us30_data as ud

    https = {"n": 0}

    def chart(*_a, **_k):
        https["n"] += 1
        raise TimeoutError("UNABLE_TO_VERIFY_LEAF_SIGNATURE")

    def yfinance_no(*_a, **_k):
        raise AssertionError("yfinance no debe volver a Yahoo HTTPS")

    def open_url(req, timeout=10):
        url = req.full_url
        assert url.startswith("http://query1.finance.yahoo.com")
        assert "%5EDJI" in url or "^DJI" in url
        assert "binance" not in url and "okx.com" not in url and "gateio" not in url
        return _Resp(json.dumps(_yahoo_payload(8, 52500)).encode())

    monkeypatch.setattr(ud, "fetch_yahoo_chart", chart)
    monkeypatch.setattr(ud, "_download_yfinance", yfinance_no)
    monkeypatch.setattr(fc, "urlopen", open_url)
    _m5, _h1, meta = ud.fetch_yahoo_klines(("YM=F", "^DJI"), m5_bars=8, h1_bars=4)
    assert meta["provider"] == "yahoohttp"
    assert meta["public_symbol"] == "^DJI"
    # 2 tickers × 3 marcos M5. El H1 no suma otro HTTPS.
    assert https["n"] == 6
    assert "H1 resampleado" in " ".join(meta["notes"])


def test_reporte_local_escribe_png_sin_red(monkeypatch, tmp_path):
    monkeypatch.setattr(fc, "urlopen", lambda *_a, **_k: pytest.fail("no debe haber red"))
    lines = [
        f"- `19:{i:02d} O={52000 + i}.0 H={52010 + i}.0 L={51990 + i}.0 C={52005 + i}.0 [G]`"
        for i in range(4)
    ]
    report = tmp_path / "us30_m5_high_signal.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    out = tmp_path / "us30_m5_chart_annotated.png"
    from app.views.illustrate_high_entry import ensure_local_entry_png

    path = ensure_local_entry_png(out, asset="US30", report_path=report, decimals=1)
    assert path and out.is_file() and out.stat().st_size > 800
