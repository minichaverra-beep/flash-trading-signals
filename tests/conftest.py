import pytest


@pytest.fixture(autouse=True)
def _sin_puente_mt5(monkeypatch):
    """Los tests no dependen del puente MT5 local (velas del broker)."""
    monkeypatch.setenv("FS_BROKER_FEED", "off")


@pytest.fixture(autouse=True)
def _sin_calibracion_real(monkeypatch):
    """Tests usan la heurística salvo que activen un artefacto de prueba."""
    monkeypatch.setenv("TRADING_PROB_CALIBRATION", "off")
