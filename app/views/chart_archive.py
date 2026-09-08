"""Publicar charts anotados en live/latest y live/archive con índice JSON."""
from __future__ import annotations

import html
import json
import shutil
import webbrowser
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.config import LIVE_DIR

LATEST_NAMES = {
    "BTC": "btc_latest_annotated.png",
    "US30": "us30_latest_annotated.png",
}
PREVIEW_NAMES = {
    "BTC": "btc_latest_preview.html",
    "US30": "us30_latest_preview.html",
}
ARCHIVE_DIR = LIVE_DIR / "archive"
LATEST_DIR = LIVE_DIR / "latest"
INDEX_PATH = ARCHIVE_DIR / "chart_index.json"
_INDEX_CAP = 200


def _asset_key(asset: str) -> str:
    a = (asset or "BTC").upper()
    if a in ("BTC", "BTCUSDT"):
        return "BTC"
    if "US30" in a or a in ("DJI", "YM"):
        return "US30"
    return a


def publish_annotated_chart(
    asset: str,
    source: Path | str,
    *,
    signal_id: str | None = None,
    mode: str = "history_review",
) -> dict[str, Any]:
    """Copia PNG a live/latest/*_latest_annotated.png y live/archive/ con índice."""
    src = Path(source)
    if not src.is_file():
        return {"ok": False, "error": f"source missing: {src}"}

    key = _asset_key(asset)
    latest_name = LATEST_NAMES.get(key, f"{key.lower()}_latest_annotated.png")
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    archive_name = f"{key.lower()}_{ts}_annotated.png"
    latest_path = LATEST_DIR / latest_name
    archive_path = ARCHIVE_DIR / archive_name

    shutil.copy2(src, latest_path)
    shutil.copy2(src, archive_path)

    entry = {
        "id": signal_id or f"{key.lower()}-{ts}",
        "asset": key,
        "mode": mode,
        "time_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "source": src.name,
        "latest": f"live/latest/{latest_name}",
        "archive": f"live/archive/{archive_name}",
        "latest_abs": str(latest_path.resolve()),
        "archive_abs": str(archive_path.resolve()),
    }
    _append_index(entry)

    return {
        "ok": True,
        "asset": key,
        "latest_name": latest_name,
        "latest_rel": f"live/latest/{latest_name}",
        "latest_abs": str(latest_path.resolve()),
        "archive_rel": f"live/archive/{archive_name}",
        "archive_abs": str(archive_path.resolve()),
        "index_entry": entry,
    }


def _append_index(entry: dict[str, Any]) -> None:
    rows: list[dict[str, Any]] = []
    if INDEX_PATH.is_file():
        try:
            raw = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
            rows = raw.get("charts") or raw.get("entries") or []
            if not isinstance(rows, list):
                rows = []
        except (json.JSONDecodeError, OSError):
            rows = []
    rows.append(entry)
    if _INDEX_CAP > 0 and len(rows) > _INDEX_CAP:
        rows = rows[-_INDEX_CAP:]
    INDEX_PATH.write_text(
        json.dumps({"charts": rows}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _strip_md(text: str) -> str:
    """Quita markdown básico para HTML legible."""
    out = text
    for token in ("**", "`", "__"):
        out = out.replace(token, "")
    return out


def build_chart_preview_html(
    png_path: Path | str,
    rows: list[tuple[str, str]],
    *,
    asset: str = "BTC",
    title: str | None = None,
) -> str:
    """HTML minimal (tema oscuro) con resumen tabular + chart anotado."""
    png = Path(png_path)
    img_name = png.name
    key = _asset_key(asset)
    heading = title or f"{key} History-Review — Chart anotado"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    table_rows = []
    for label, value in rows:
        table_rows.append(
            "<tr>"
            f"<th>{html.escape(label)}</th>"
            f"<td>{html.escape(_strip_md(value))}</td>"
            "</tr>"
        )
    tbody = "\n".join(table_rows)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(heading)}</title>
  <style>
    :root {{ color-scheme: dark; }}
    body {{
      margin: 0; padding: 1.25rem 1.5rem 2rem;
      font: 14px/1.45 Segoe UI, system-ui, sans-serif;
      background: #0f1117; color: #e6e8ef;
    }}
    h1 {{ font-size: 1.15rem; margin: 0 0 .25rem; }}
    .meta {{ color: #8b93a7; margin-bottom: 1rem; font-size: .85rem; }}
    table {{
      width: 100%; border-collapse: collapse; margin-bottom: 1.25rem;
      background: #171a22; border: 1px solid #2a3142; border-radius: 8px;
      overflow: hidden;
    }}
    th, td {{ padding: .45rem .65rem; border-bottom: 1px solid #2a3142; vertical-align: top; }}
    th {{
      width: 11rem; text-align: left; color: #aeb6c8;
      font-weight: 600; white-space: nowrap;
    }}
    tr:last-child th, tr:last-child td {{ border-bottom: none; }}
    .chart-wrap {{
      border: 1px solid #2a3142; border-radius: 8px; overflow: hidden;
      background: #0b0d12;
    }}
    img {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <h1>{html.escape(heading)}</h1>
  <div class="meta">Generado {html.escape(ts)} · revisión P&amp;L (no señal nueva)</div>
  <table>
    <tbody>
{tbody}
    </tbody>
  </table>
  <div class="chart-wrap">
    <img src="{html.escape(img_name)}" alt="Chart anotado {html.escape(key)}">
  </div>
</body>
</html>
"""


def write_chart_preview_html(
    png_path: Path | str,
    rows: list[tuple[str, str]],
    *,
    asset: str = "BTC",
    title: str | None = None,
) -> dict[str, Any]:
    """Escribe preview HTML junto al PNG en live/latest/."""
    png = Path(png_path)
    if not png.is_file():
        return {"ok": False, "error": f"png missing: {png}"}

    key = _asset_key(asset)
    preview_name = PREVIEW_NAMES.get(key, f"{key.lower()}_latest_preview.html")
    preview_path = LATEST_DIR / preview_name
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    content = build_chart_preview_html(png, rows, asset=key, title=title)
    preview_path.write_text(content, encoding="utf-8")

    return {
        "ok": True,
        "preview_name": preview_name,
        "preview_rel": f"live/latest/{preview_name}",
        "preview_abs": str(preview_path.resolve()),
        "png_name": png.name,
    }


def open_preview_in_browser(html_path: Path | str) -> bool:
    """Abre preview HTML en el navegador predeterminado (file:///)."""
    path = Path(html_path)
    if not path.is_file():
        return False
    uri = path.resolve().as_uri()
    try:
        return bool(webbrowser.open(uri, new=2))
    except OSError:
        return False


def format_archive_md_rows(pub: dict[str, Any] | None) -> list[str]:
    """Filas markdown para tabla history cuando hay chart publicado."""
    if not pub or not pub.get("ok"):
        return []
    if pub.get("preview_rel"):
        return [f"| Chart | **Preview en navegador** |"]
    return [
        f"| Chart (latest) | `{pub['latest_rel']}` |",
        f"| Chart (archive) | `{pub['archive_rel']}` |",
        f"| Chart (abs) | `{pub['latest_abs']}` |",
    ]
