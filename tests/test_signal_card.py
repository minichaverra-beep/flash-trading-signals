"""Tarjeta de señal compuesta en el servidor (app.views.signal_card)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from app.views.signal_card import W, normalize_spec, render_signal_card

PIL = pytest.importorskip("PIL")
from PIL import Image  # noqa: E402

SPEC = {
    "symbol": "btc", "timeframe": "M5", "tier": "HIGH", "price": "81319.7", "direction": "Alcista",
    "odds": {"compra": 65, "venta": 35},
    "pills": [
        {"kicker": "Tendencia / sesgo", "title": "Alcista"},
        {"kicker": "Probabilidad de éxito", "title": "65%"},
        {"kicker": "Si es Esperar", "title": "2 velas M5 a favor", "detail": "Hay que esperar a que salgan"},
    ],
    "action": {"state": "ESPERAR", "reason": "Tokio · Sídney"},
    "levels": [
        {"label": "Entrada", "value": "81318.3", "tone": "text"},
        {"label": "SL", "value": "81258.3", "tone": "loss"},
        {"label": "TP", "value": "81438.3", "tone": "gain"},
    ],
    "primary": {"title": "Escenario alcista", "tone": "gain", "bullets": ["Veredicto: No operar"]},
    "pullback": {"title": "Escenario de retroceso", "tone": "loss", "bullets": ["Invalidación: cierre M5 < 81259.4"]},
    "risk": 60, "riskFill": 55, "riskNote": "Si el riesgo es alto, el SL pasa el soporte",
}


def _chart_png(path: Path, size=(1400, 1120)) -> Path:
    im = Image.new("RGBA", size, (30, 30, 30, 255))
    # Una «vela» verde bien visible para comprobar que el gráfico quedó dentro.
    for x in range(600, 800):
        for y in range(200, 900):
            im.putpixel((x, y), (62, 207, 142, 255))
    im.save(path)
    return path


def test_normalize_spec_descarta_lo_invalido_y_acota():
    spec = normalize_spec({
        **SPEC, "direction": "Lateral", "action": {"state": "YOLO"}, "footer": "x" * 1000,
        "levels": [{"label": "TP", "value": "  "}, {"label": "SL", "value": "1", "tone": "raro"}],
    })
    assert spec["symbol"] == "BTC"
    assert spec["direction"] is None
    assert spec["action"] is None
    assert len(spec["footer"]) == 400
    assert spec["levels"] == [{"label": "SL", "value": "1", "tone": "text"}]
    assert spec["odds"] == {"compra": 65, "venta": 35}


def test_render_con_grafico_lo_incluye(tmp_path):
    chart = _chart_png(tmp_path / "btc_m5_chart_annotated.png")
    out = tmp_path / "card.png"
    result = render_signal_card({**SPEC, "chart": str(chart)}, out)
    assert result["ok"] is True
    assert result["chart"] is True
    assert result["chart_error"] is None
    im = Image.open(out).convert("RGB")
    assert im.width == W
    # Con gráfico la tarjeta es más alta que sin él.
    sin = render_signal_card(SPEC, tmp_path / "sin.png")
    assert im.height > sin["height"]
    # Un píxel del centro del gráfico es la vela verde (no el fondo del panel).
    px = im.getpixel((W // 2, 420 + 350))
    assert px[1] > 150 and px[0] < 120, px


def test_render_sin_png_dice_por_que(tmp_path):
    out = tmp_path / "card.png"
    result = render_signal_card({**SPEC, "chart": str(tmp_path / "no_existe.png")}, out)
    assert result["ok"] is True
    assert result["chart"] is False
    assert "no_existe.png" in (result["chart_error"] or "")
    assert out.is_file()


def test_spec_minimo_sigue_generando_png(tmp_path):
    result = render_signal_card({"symbol": "US30", "price": "47000"}, tmp_path / "min.png")
    assert result["ok"] is True
    assert Image.open(tmp_path / "min.png").height > 100


def test_cli_imprime_json(tmp_path):
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(SPEC), encoding="utf-8")
    out = tmp_path / "cli.png"
    proc = subprocess.run(
        [sys.executable, "-m", "app.views.signal_card", "--spec", str(spec_path), "--out", str(out)],
        capture_output=True, text=True, cwd=str(Path(__file__).resolve().parents[1]),
    )
    assert proc.returncode == 0, proc.stderr
    payload = json.loads(proc.stdout.strip().splitlines()[-1])
    assert payload["ok"] is True and payload["chart"] is False
    assert out.is_file()
