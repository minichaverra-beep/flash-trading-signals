import pytest


@pytest.fixture(autouse=True)
def _sin_puente_mt5(monkeypatch):
    """Los tests no dependen del puente MT5 local (velas del broker)."""
    monkeypatch.setenv("FS_BROKER_FEED", "off")
