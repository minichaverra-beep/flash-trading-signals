"""Velas del broker (MT5) vs feed externo: fuente, desfase y rótulos."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from app.models import broker_feed as bf

T0 = datetime(2026, 10, 1, 17, 0, tzinfo=timezone.utc)


def _rates(n: int, base: float) -> list[dict]:
    return [{"time": int((T0 + timedelta(minutes=5 * i)).timestamp()), "open": base, "high": base + 5,
             "low": base - 5, "close": base + 1, "volume": 10} for i in range(n)]


def _external(n: int = 100, close: float = 50929.6):
    m5 = [{"open_time": T0 + timedelta(minutes=5 * i), "open": close, "high": close + 3, "low": close - 3,
           "close": close, "volume": 1.0} for i in range(n)]
    return m5, list(m5[:60]), {"notes": ["YM=F 5m: Yahoo API OK"], "ticker": "YM=F"}


@pytest.fixture
def puente(monkeypatch):
    monkeypatch.setenv("FS_BROKER_FEED", "on")
    monkeypatch.setenv("FS_MT5_SYMBOL_US30", "US30m")
    calls = []

    def install(payload_for):
        def fake_fetch(cfg, timeframe, count, until=None):
            calls.append((cfg["symbol"], timeframe, count, until))
            out = payload_for(timeframe, count)
            if isinstance(out, Exception):
                raise out
            return out
        monkeypatch.setattr(bf, "fetch_rates", fake_fetch)
        return calls
    return install


class TestConfig:
    def test_off_desactiva(self, monkeypatch):
        monkeypatch.setenv("FS_BROKER_FEED", "off")
        assert bf.bridge_config("US30") is None

    def test_simbolos_y_token(self, monkeypatch):
        monkeypatch.setenv("FS_BROKER_FEED", "on")
        monkeypatch.setenv("FS_MT5_SYMBOL_XAUUSD", "XAUUSDm")
        monkeypatch.setenv("FS_MT5_BRIDGE_TOKEN", "t0k")
        monkeypatch.setenv("FS_MT5_BRIDGE_URL", "http://127.0.0.1:8766/")
        cfg = bf.bridge_config("GC=F")
        assert cfg == {"url": "http://127.0.0.1:8766", "token": "t0k", "symbol": "XAUUSDm", "asset": "XAUUSD"}

    @pytest.mark.parametrize("raw,key", [("BTCUSDT", "BTC"), ("YM=F", "US30"), ("us30", "US30"), ("XAU", "XAUUSD")])
    def test_asset_key(self, raw, key):
        assert bf.asset_key(raw) == key


class TestOffset:
    def test_offset_us30_medido(self):
        assert bf.broker_offset(50929.6, 51008.95) == pytest.approx(79.35)

    def test_offset_absurdo_se_descarta(self):
        assert bf.broker_offset(4181.0, 51008.0) is None

    def test_quote_mid_y_vieja(self):
        now = 1_790_896_773
        assert bf.quote_mid({"bid": 51008.3, "ask": 51009.6, "tickTime": now - 10}, now) == pytest.approx(51008.95)
        assert bf.quote_mid({"bid": 51008.3, "ask": 51009.6, "tickTime": now - 3600}, now) is None
        assert bf.quote_mid({"bid": 0, "ask": 1}, now) is None

    def test_labels(self):
        assert bf.feed_info("mt5", "US30", "US30m")["label"] == "velas MT5 US30m"
        shifted = bf.feed_info("external_shifted", "US30", "US30m", 78.4)
        assert shifted["label"] == "velas YM=F→^DJI ajustadas +78.4 pts a US30m"
        ext = bf.feed_info("external", "XAUUSD", None)
        assert ext["broker"] is False
        assert "sin MT5" in ext["label"]


class TestLoadKlines:
    def test_usa_velas_mt5_si_hay_puente(self, puente):
        def payload(tf, count):
            return {"ok": True, "bid": 51008.3, "ask": 51009.6, "rates": _rates(count, 51000.0)}
        calls = puente(payload)
        m5, h1, meta = bf.load_klines("US30", lambda: pytest.fail("no debe usar el feed externo"))
        assert len(m5) == 200 and len(h1) == 200
        assert m5[-1]["close"] == pytest.approx(51001.0)
        assert m5[-1]["open_time"].tzinfo is timezone.utc
        assert meta["feed"]["source"] == "mt5"
        assert meta["ticker"] == "US30m"
        assert [c[1] for c in calls] == ["M5", "H1"]

    def test_pocas_velas_desplaza_externo_al_mid(self, puente):
        puente(lambda tf, count: {"ok": True, "bid": 51008.3, "ask": 51009.6,
                                  "tickTime": datetime.now(timezone.utc).timestamp(), "rates": _rates(5, 51000.0)})
        m5, h1, meta = bf.load_klines("US30", _external)
        assert m5[-1]["close"] == pytest.approx(51008.95)
        assert h1[-1]["close"] == pytest.approx(51008.95)
        assert meta["feed"]["source"] == "external_shifted"
        assert meta["feed"]["offset"] == pytest.approx(79.35)
        assert "+79.3 pts a US30m" in meta["feed"]["label"] or "+79.4 pts a US30m" in meta["feed"]["label"]

    def test_sin_puente_queda_externo_rotulado(self, puente):
        puente(lambda tf, count: RuntimeError("puente MT5 503"))
        m5, _, meta = bf.load_klines("US30", _external)
        assert m5[-1]["close"] == pytest.approx(50929.6)
        assert meta["feed"]["source"] == "external"
        assert any("no disponible" in n for n in meta["notes"])

    def test_desactivado_no_llama_al_puente(self, monkeypatch):
        monkeypatch.setenv("FS_BROKER_FEED", "off")
        monkeypatch.setattr(bf, "fetch_rates", lambda *a, **k: pytest.fail("no debe llamar al puente"))
        _, _, meta = bf.load_klines("US30", _external)
        assert meta["feed"]["source"] == "external"

    def test_describe_source(self):
        assert bf.describe_source({"feed": bf.feed_info("mt5", "BTC", "BTCUSDm")}, "Binance") == "MT5 BTCUSDm (broker, M5/H1)"
        assert "sin MT5" in bf.describe_source({"feed": bf.feed_info("external", "BTC", None)}, "Binance")
