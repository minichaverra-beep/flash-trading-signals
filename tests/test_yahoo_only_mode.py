"""Modo «solo Yahoo» (FS_DATA_SOURCE=yahoo / FS_DISABLE_MT5=1): Android sin MT5.

Garantías: no se intenta ninguna conexión al puente MT5, no hay recursión entre loaders y los
errores de Yahoo salen claros (mensaje + traceback acotado), no como «maximum recursion depth».
"""
from __future__ import annotations

import inspect
import json
from datetime import datetime, timedelta, timezone

import pytest

from app.models import broker_feed as bf
from app.views import chart_rerender as cr
from app.views import trade_outcome_chart as toc

T0 = datetime(2026, 10, 1, 16, 55, tzinfo=timezone.utc)


def _candles(n: int = 120, base: float = 100.0, start: datetime = T0) -> list[dict]:
    out = []
    for i in range(n):
        t = start + timedelta(minutes=5 * i)
        out.append({"open_time": t, "open": base, "high": base + 3, "low": base - 3, "close": base + 1,
                    "volume": 1.0, "close_time": t})
    return out


def _external(depths: list[int] | None = None):
    def fetch():
        if depths is not None:
            depths.append(len(inspect.stack(0)))
        m5 = _candles()
        return m5, list(m5[:60]), {"notes": ["YM=F 5m: Yahoo API OK"], "ticker": "YM=F"}
    return fetch


@pytest.fixture
def sin_mt5(monkeypatch):
    """Modo yahoo + cualquier contacto con MT5 (puente, sockets) falla el test."""
    monkeypatch.setenv("FS_DATA_SOURCE", "yahoo")
    monkeypatch.setenv("FS_BROKER_FEED", "on")
    monkeypatch.setenv("FS_MT5_BRIDGE_URL", "http://127.0.0.1:1")

    def boom(*_a, **_k):
        pytest.fail("no debe tocar el puente MT5 en modo solo Yahoo")

    monkeypatch.setattr(bf, "_post", boom)
    monkeypatch.setattr(bf, "urlopen", boom)


class TestMode:
    @pytest.mark.parametrize("name,value", [
        ("FS_DATA_SOURCE", "yahoo"), ("FS_DATA_SOURCE", " YAHOO "), ("FS_DISABLE_MT5", "1"), ("FS_DISABLE_MT5", "true"),
    ])
    def test_activa(self, monkeypatch, name, value):
        monkeypatch.setenv(name, value)
        assert bf.yahoo_only() is True
        assert bf.bridge_config("US30") is None

    @pytest.mark.parametrize("value", ["", "auto", "mt5"])
    def test_auto_y_mt5_no_desactivan(self, monkeypatch, value):
        monkeypatch.delenv("FS_DISABLE_MT5", raising=False)
        monkeypatch.setenv("FS_DATA_SOURCE", value)
        monkeypatch.setenv("FS_BROKER_FEED", "on")
        assert bf.yahoo_only() is False
        assert bf.bridge_config("US30")["symbol"] == "US30m"

    def test_fetch_rates_se_niega(self, sin_mt5):
        with pytest.raises(RuntimeError, match="solo Yahoo"):
            bf.fetch_rates({"url": "http://127.0.0.1:1", "token": "", "symbol": "US30m"}, "M5", 10)


class TestLoadKlines:
    def test_us30_usa_yahoo_sin_tocar_mt5_ni_recursar(self, sin_mt5):
        depths: list[int] = []
        base = len(inspect.stack(0))
        m5, h1, meta = bf.load_klines("US30", _external(depths))
        assert len(m5) == 120 and len(h1) == 60
        assert meta["feed"]["source"] == "yahoo" and meta["feed"]["broker"] is False
        assert "solo Yahoo" in meta["feed"]["label"] and "sin MT5" in meta["feed"]["label"]
        assert meta["notes"][0].startswith("Modo solo Yahoo")
        assert "YM=F 5m: Yahoo API OK" in meta["notes"]
        # el feed se invoca a pocos frames de la llamada: nada de loaders que se llamen entre sí
        assert depths and depths[0] - base < 6

    def test_btc_pasa_de_binance_a_yahoo_btc_usd(self, sin_mt5, monkeypatch):
        seen = {}

        def fake_yahoo(tickers, m5_interval="5m", h1_interval="1h", m5_bars=200, h1_bars=200):
            seen["tickers"] = tickers
            return _candles(), _candles(60), {"notes": [], "ticker": tickers[0]}

        monkeypatch.setattr("app.models.us30_data.fetch_yahoo_klines", fake_yahoo)
        m5, _h1, meta = bf.load_klines("BTC", lambda: pytest.fail("Binance no se usa en modo Yahoo"))
        assert seen["tickers"] == ("BTC-USD",)
        assert meta["feed"]["source"] == "yahoo" and "BTC-USD" in meta["feed"]["label"]
        assert bf.describe_source(meta, "Binance BTCUSDT") == "BTC-USD (solo Yahoo) · sin MT5 (precio puede diferir del broker)"
        assert len(m5) == 120

    def test_yahoo_caido_error_claro_sin_recursion(self, sin_mt5, monkeypatch):
        def down(*_a, **_k):
            raise RuntimeError("No se pudieron obtener velas. Intentos: ('BTC-USD',)")

        monkeypatch.setattr("app.models.us30_data.fetch_yahoo_klines", down)
        with pytest.raises(RuntimeError, match="No se pudieron obtener velas"):
            bf.load_klines("BTC", lambda: pytest.fail("no"))

    def test_sin_modo_yahoo_sigue_intentando_mt5(self, monkeypatch):
        monkeypatch.delenv("FS_DATA_SOURCE", raising=False)
        monkeypatch.delenv("FS_DISABLE_MT5", raising=False)
        monkeypatch.setenv("FS_BROKER_FEED", "on")
        calls = []

        def down(cfg, timeframe, count, until=None):
            calls.append(timeframe)
            raise RuntimeError("puente MT5 503")

        monkeypatch.setattr(bf, "fetch_rates", down)
        _, _, meta = bf.load_klines("US30", _external())
        assert calls == ["M5"] and meta["feed"]["source"] == "external"


class TestOutcomeChart:
    def _patch_yahoo(self, monkeypatch, rows):
        monkeypatch.setattr("app.models.us30_data.fetch_yahoo_chart", lambda *_a, **_k: rows)
        monkeypatch.setattr(toc, "_fetch_binance_since", lambda *_a, **_k: pytest.fail("Binance no en modo Yahoo"))

    def test_fetch_m5_since_btc_solo_yahoo(self, sin_mt5, monkeypatch):
        self._patch_yahoo(monkeypatch, _candles(40, 100.0))
        rows, meta = toc.fetch_m5_since("btc", T0, T0 + 40 * toc.M5)
        assert meta["source"] == "BTC-USD (Yahoo)" and meta["yahoo_only"] is True
        assert any("MT5 omitido" in n for n in meta["notes"]) and len(rows) == 40

    def test_fetch_m5_since_yahoo_caido_mensaje_claro(self, sin_mt5, monkeypatch):
        def down(*_a, **_k):
            raise OSError("sin red")

        monkeypatch.setattr("app.models.us30_data.fetch_yahoo_chart", down)
        with pytest.raises(toc.OutcomeDataError, match="No se pudieron obtener velas M5 reales.*sin red"):
            toc.fetch_m5_since("xauusd", T0, T0 + toc.M5)

    def test_evaluate_signal_genera_png_con_velas_yahoo(self, sin_mt5, monkeypatch, tmp_path):
        # señal en T0, el precio sube hasta tocar el TP: resultado «tp» con velas de Yahoo
        rows = _candles(60, 100.0, T0 - 40 * toc.M5)
        for c in rows:
            if c["open_time"] >= T0 + 3 * toc.M5:
                c.update(high=106.0, low=99.0, close=105.0)
            else:
                c.update(high=101.0, low=99.0)
        self._patch_yahoo(monkeypatch, rows)
        out = tmp_path / "o.png"
        res = toc.evaluate_signal("xauusd", signal_time=T0, entry=101.0, sl=97.0, tp=104.0, out_path=out,
                                  price=101.0, now=T0 + 30 * toc.M5)
        assert res["ok"] and res["outcome"] == "tp" and res["dataSource"] == "yahoo"
        assert out.is_file() and out.stat().st_size > 5000
        assert any("MT5 omitido" in n for n in res["feedNotes"])

    def test_cli_error_yahoo_json_limpio_y_traceback(self, sin_mt5, monkeypatch, tmp_path, capsys):
        monkeypatch.setattr("app.models.us30_data.fetch_yahoo_chart", lambda *_a, **_k: [])
        rc = toc.main(["--market", "us30", "--signal-time", "2026-10-01T16:55:00Z", "--entry", "100",
                       "--sl", "98", "--tp", "104", "--out", str(tmp_path / "x.png")])
        out, err = capsys.readouterr()
        payload = json.loads(out.strip().splitlines()[-1])
        assert rc == 1 and payload["ok"] is False and "recursion" not in payload.get("code", "")
        assert "No se pudieron obtener velas M5 reales" in payload["error"]
        assert "Traceback" in err and "OutcomeDataError" in err


class TestRerender:
    def test_fetch_m5_btc_usa_yahoo(self, sin_mt5, monkeypatch):
        monkeypatch.setattr("app.models.us30_data.fetch_yahoo_klines",
                            lambda tickers, **_k: (_candles(5), _candles(5), {"notes": [], "ticker": tickers[0]}))
        monkeypatch.setattr("app.controllers.analyze_btc_m5.fetch_klines",
                            lambda *_a, **_k: pytest.fail("Binance no en modo Yahoo"))
        assert len(cr._fetch_m5("BTC")) == 5

    def test_align_to_broker_no_toca_mt5(self, sin_mt5):
        inputs = {"asset": "US30", "data": {"m5": _candles(5), "feed": {"source": "yahoo"}}, "opt": {}}
        assert cr.align_to_broker(inputs) is inputs

    def test_cli_recursion_json_con_codigo_y_traceback(self, monkeypatch, tmp_path, capsys):
        def boom(*_a, **_k):
            raise RecursionError("maximum recursion depth exceeded")

        monkeypatch.setattr(cr, "rebuild_inputs", boom)
        rc = cr.main(["--chart", str(tmp_path / "c.png"), "--entry", "1", "--sl", "0.5", "--tp", "2",
                      "--asset", "US30", "--until", "2026-10-01T16:55:00Z"])
        out, err = capsys.readouterr()
        payload = json.loads(out.strip().splitlines()[-1])
        assert rc == 1 and payload["code"] == "recursion"
        assert "maximum recursion" not in payload["error"] and payload["detail"].startswith("maximum recursion")
        assert "Traceback" in err
