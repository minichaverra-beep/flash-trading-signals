"""Tests history-review: tabla unificada, preview HTML y consola segura."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from app.views.chart_archive import (
    build_chart_preview_html,
    open_preview_in_browser,
    write_chart_preview_html,
)
from app.views.history_review import (
    _console_safe,
    build_high_summary_rows,
    build_history_summary_rows,
    finish_high_output,
    finish_history_review_output,
    format_high_summary_md,
    format_history_summary_md,
    publish_history_preview,
)


def _sample_rows() -> list[tuple[str, str]]:
    return [
        ("Precio", "**100150.0**"),
        ("Veredicto", "**ESPERAR** (SHORT)"),
        ("Revisión última Entry", "**btc-001** · Entry **100000.0** · SHORT"),
        ("P&L vs precio actual", "**+150.0 pts** · **EN BENEFICIO**"),
        ("Calificación Entry", "**BUENA**"),
        ("ICT", "FVG bear 99950"),
        ("Plan scalp (ref.)", "Entry **99900.0** · SL **100050.0**"),
        ("Entradas scalp", "1) **99910.0** (ict)"),
        ("E2", "E2_NO — E1 only"),
        ("Métricas", "Rules **75%** · Confluencia **MEDIA**"),
        ("Chart", "**Preview en navegador**"),
    ]


def test_build_history_summary_rows_unified_no_paths():
    data = {
        "price": 100_150.0,
        "price_decimals": 1,
        "history_mode": True,
        "setup": {"direction": "SHORT"},
        "e2": {"verdict": "E2_NO"},
        "annotated_chart_file": "btc_m5_chart_annotated.png",
        "annotated_chart_abs": "C:/proj/live/btc_m5_chart_annotated.png",
    }
    ctx = {
        "verdict": "ESPERAR",
        "categories": {
            "precio": "100150.0",
            "rules_pct": 75,
            "confluencia_setup": "MEDIA",
            "bando_usado": "BEARISH",
            "bando_mercado": "BEARISH",
            "revision_ultima_entry": "**btc-001** · SHORT",
            "pnl_vs_precio": "**+150 pts**",
            "calificacion_entrada": "**BUENA**",
        },
    }
    opt = {"entry": 99_900.0, "sl": 100_050.0, "dec": 1}
    reflection = {
        "cell_revision": "**btc-001** · SHORT",
        "cell_pnl": "**+150 pts**",
        "cell_calificacion": "**BUENA**",
    }
    pub = {
        "ok": True,
        "latest_rel": "live/latest/btc_latest_annotated.png",
        "latest_abs": "C:/proj/live/latest/btc_latest_annotated.png",
    }

    rows = build_history_summary_rows(data, ctx, opt, reflection, chart_pub=pub)
    labels = [label for label, _ in rows]

    assert labels.count("Precio") == 1
    assert "Revisión última Entry" in labels
    assert "P&L vs precio actual" in labels
    assert "Calificación Entry" in labels
    assert "ICT" in labels
    assert "Plan scalp (ref.)" in labels
    assert "Entradas scalp" in labels
    assert "E2" in labels
    assert "Métricas" in labels
    assert "Chart" in labels
    assert "Bando usado (lado asumido)" in labels

    chart_val = dict(rows)["Chart"]
    assert "live/" not in chart_val
    assert "C:/" not in chart_val
    assert "Preview en navegador" in chart_val


def test_format_history_summary_md_single_table():
    md = "\n".join(format_history_summary_md(_sample_rows()))
    assert "## Resumen History-Review" in md
    assert "| Sección | Detalle |" in md
    assert md.count("| Sección | Detalle |") == 1
    assert "| Revisión última Entry |" in md
    assert "| Chart | **Preview en navegador** |" in md
    assert "## Categories" not in md


def test_console_safe_replaces_unicode():
    raw = "P&L +150 · EN BENEFICIO — flecha → OK ✅"
    safe = _console_safe(raw)
    assert "->" in safe
    assert "OK" in safe
    assert "→" not in safe
    assert "✅" not in safe


def test_build_chart_preview_html_embeds_summary_and_image(tmp_path):
    png = tmp_path / "btc_latest_annotated.png"
    png.write_bytes(b"fake-png")
    html = build_chart_preview_html(png, _sample_rows(), asset="BTC")
    assert "btc_latest_annotated.png" in html
    assert "Revisión última Entry" in html
    assert "Preview en navegador" in html
    assert "<table>" in html


def test_write_chart_preview_html_creates_file(tmp_path, monkeypatch):
    monkeypatch.setattr("app.views.chart_archive.LATEST_DIR", tmp_path)
    png = tmp_path / "btc_latest_annotated.png"
    png.write_bytes(b"fake-png")

    result = write_chart_preview_html(png, _sample_rows(), asset="BTC")
    assert result["ok"] is True
    preview = Path(result["preview_abs"])
    assert preview.is_file()
    assert preview.name == "btc_latest_preview.html"
    assert "btc_latest_annotated.png" in preview.read_text(encoding="utf-8")


def test_publish_history_preview_no_open(tmp_path, monkeypatch):
    monkeypatch.setattr("app.views.chart_archive.LATEST_DIR", tmp_path)
    png = tmp_path / "btc_latest_annotated.png"
    png.write_bytes(b"fake-png")
    data = {
        "asset_label": "BTC",
        "chart_archive": {"ok": True, "latest_abs": str(png)},
    }
    rows = _sample_rows()

    with patch("app.views.chart_archive.open_preview_in_browser") as mock_open:
        result = publish_history_preview(data, rows, asset="BTC", no_open=True)
        mock_open.assert_not_called()

    assert result["ok"] is True
    assert data["chart_preview"]["preview_name"] == "btc_latest_preview.html"


def test_open_preview_in_browser_uses_file_uri(tmp_path):
    html = tmp_path / "preview.html"
    html.write_text("<html></html>", encoding="utf-8")
    with patch("app.views.chart_archive.webbrowser.open", return_value=True) as mock_open:
        ok = open_preview_in_browser(html)
    assert ok is True
    mock_open.assert_called_once()
    uri = mock_open.call_args[0][0]
    assert uri.startswith("file:///")


def test_finish_history_review_output_prints_without_paths(capsys, tmp_path, monkeypatch):
    monkeypatch.setattr("app.views.chart_archive.LATEST_DIR", tmp_path)
    png = tmp_path / "btc_latest_annotated.png"
    png.write_bytes(b"fake-png")
    data = {
        "asset_label": "BTC",
        "chart_archive": {"ok": True, "latest_abs": str(png)},
    }
    rows = _sample_rows()

    with patch("app.views.chart_archive.open_preview_in_browser", return_value=True):
        finish_history_review_output(data, rows, asset="BTC", no_open=False)

    out = capsys.readouterr().out
    assert "## Resumen History-Review" in out
    assert "| Revisión última Entry |" in out
    assert "Preview abierto en navegador" in out
    assert "live/latest" not in out
    assert "C:/" not in out
    assert "latest_abs" not in out


def _high_sample_rows() -> list[tuple[str, str]]:
    return [
        ("Precio", "**100150.0**"),
        ("Veredicto", "**ESPERAR** (SHORT)"),
        ("Entrada óptima", "**99950.0**"),
        ("ICT", "FVG bear 99950"),
        ("Plan", "Entry **99900.0** · SL **100050.0** · TP **99800.0**"),
        ("E2 / Break", "E2_NO — E1 only"),
        ("Métricas", "Rules **75%** · Confluencia **MEDIA**"),
        ("Historial ref", "btc-001 · **BUENA**"),
        ("Chart", "**Preview en navegador**"),
    ]


def test_build_high_summary_rows_unified():
    data = {
        "price": 100_150.0,
        "price_decimals": 1,
        "setup": {"direction": "SHORT"},
        "mode_setup": "break",
        "e2": {"verdict": "E2_NO"},
        "annotated_chart_file": "btc_m5_chart_annotated.png",
    }
    ctx = {
        "verdict": "ESPERAR",
        "categories": {
            "precio": "100150.0",
            "entrada_optima": "99950.0",
            "rules_pct": 75,
            "confluencia_setup": "MEDIA",
            "ultima_senal_entrada": "btc-001",
            "calificacion_entrada": "**BUENA**",
            "ict_scan": "FVG bear",
        },
    }
    opt = {"entry": 99_900.0, "sl": 100_050.0, "tp": 99_800.0, "dec": 1}
    reflection = {"cell_ultima": "btc-001", "cell_calificacion": "**BUENA**"}
    pub = {"ok": True, "latest_abs": "C:/proj/live/latest/btc_latest_annotated.png"}

    rows = build_high_summary_rows(data, ctx, opt, reflection, chart_pub=pub)
    labels = [label for label, _ in rows]

    assert "Entrada óptima" in labels
    assert "Plan" in labels
    assert "E2 / Break" in labels
    assert "Métricas" in labels
    assert "Historial ref" in labels
    assert "Chart" in labels
    assert "## Categories" not in str(rows)
    e2_val = dict(rows)["E2 / Break"]
    assert "BREAK" in e2_val
    chart_val = dict(rows)["Chart"]
    assert "Preview en navegador" in chart_val
    assert "C:/" not in chart_val


def test_format_high_summary_md_single_table():
    md = "\n".join(format_high_summary_md(_high_sample_rows()))
    assert "## Resumen High" in md
    assert "| Sección | Detalle |" in md
    assert md.count("| Sección | Detalle |") == 1
    assert "| Entrada óptima |" in md
    assert "| Historial ref |" in md
    assert "## Categories" not in md


def test_finish_high_output_prints_without_paths(capsys, tmp_path, monkeypatch):
    monkeypatch.setattr("app.views.chart_archive.LATEST_DIR", tmp_path)
    png = tmp_path / "btc_latest_annotated.png"
    png.write_bytes(b"fake-png")
    data = {
        "asset_label": "BTC",
        "chart_archive": {"ok": True, "latest_abs": str(png)},
    }
    rows = _high_sample_rows()

    with patch("app.views.chart_archive.open_preview_in_browser", return_value=True):
        finish_high_output(data, rows, asset="BTC", no_open=False)

    out = capsys.readouterr().out
    assert "## Resumen High" in out
    assert "| Entrada óptima |" in out
    assert "Preview abierto en navegador" in out
    assert "live/latest" not in out
    assert "C:/" not in out
