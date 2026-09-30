"""Generate annotated M5 chart for high-signal optimal entry (2M5 + zona + Entry/SL/TP)."""
from __future__ import annotations

import io
import os
import tempfile
import time
from pathlib import Path

CHART_DPI = 200
CHART_DPI_PLACEHOLDER = 120


def savefig_png(
    fig,
    out_path: Path | str,
    *,
    dpi: int = 140,
    facecolor: str = "#1e1e1e",
) -> Path:
    """
    Save a matplotlib figure as PNG robustly on Windows.

    Avoids common [Errno 22] Invalid argument failures by:
    - rendering via BytesIO (matplotlib never opens the final path)
    - writing a same-dir temp file then os.replace (atomic, handles locked viewers)
    - one retry after a short sleep, then fallback ``*_new.png``
    """
    out = Path(out_path)
    # Trailing/leading spaces in the filename break Win32 CreateFile
    out = out.parent / out.name.strip()
    out.parent.mkdir(parents=True, exist_ok=True)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, facecolor=facecolor)
    payload = buf.getvalue()

    def _atomic_write(target: Path) -> None:
        fd, tmp_name = tempfile.mkstemp(suffix=".png.tmp", prefix=f".{target.stem}_", dir=str(target.parent))
        try:
            with os.fdopen(fd, "wb") as fh:
                fh.write(payload)
                fh.flush()
                os.fsync(fh.fileno())
            os.replace(tmp_name, target)
        except Exception:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass
            raise

    try:
        _atomic_write(out)
        return out
    except OSError:
        time.sleep(0.2)
        try:
            _atomic_write(out)
            return out
        except OSError:
            alt = out.with_name(f"{out.stem}_new{out.suffix or '.png'}")
            _atomic_write(alt)
            return alt


def _zone_edges(opt: dict) -> tuple[float | None, float | None]:
    """Return (zone_lo, zone_hi) from optimal entry; recompute if missing."""
    lo, hi = opt.get("zone_lo"), opt.get("zone_hi")
    if lo is not None and hi is not None:
        return float(lo), float(hi)
    level = opt.get("level")
    direction = opt.get("direction")
    if not level or direction not in ("LONG", "SHORT"):
        return None, None
    if direction == "SHORT":
        return level * (1 - 0.0015), float(level)
    return float(level), level * (1 + 0.0015)



def _callout_text(opt: dict) -> str:
    """Spanish callout: ESPERAR confirmación vs ENTRAR (zona no fuerza wait)."""
    confirm = str(opt.get("ahora_2m5", "")).lower().startswith("sí") or str(
        opt.get("ahora_2m5", "")
    ).lower().startswith("si")
    action = str(opt.get("ahora_action", "ESPERAR"))
    if "ENTRAR" in action.upper() and confirm:
        return "2M5 OK → ENTRAR"
    if "ENTRAR" in action.upper():
        return "Setup listo → ENTRAR"
    if confirm:
        return "2M5 OK · revisar bias/SL"
    return "Sin 2M5 → ESPERAR confirmación"


def write_entry_overlay_charts(
    data: dict,
    optimal_entry: dict,
    *,
    asset: str = "BTC",
    main_chart_path: Path | str | None = None,
    annotated_path: Path | str | None = None,
    dpi: int | None = None,
) -> dict:
    """
    Write OPTI/SL/TP/S-R overlays onto the default High chart and/or the -Ilustrate PNG.

    - main_chart_path: live/*_m5_chart.png (when chart enabled / not -NoChart)
    - annotated_path: live/*_m5_chart_annotated.png (when -Ilustrate)
    """
    out: dict = {}
    chart_dpi = dpi if dpi is not None else CHART_DPI
    if main_chart_path is not None:
        p = create_annotated_entry_chart(
            data, optimal_entry, main_chart_path, asset=asset, dpi=chart_dpi,
        )
        out["main_chart"] = str(p.resolve())
    if annotated_path is not None:
        p = create_annotated_entry_chart(
            data, optimal_entry, annotated_path, asset=asset, dpi=chart_dpi,
        )
        out["annotated_chart"] = str(p.resolve())
        out["annotated_file"] = Path(annotated_path).name
    return out


def create_annotated_entry_chart(
    data: dict,
    optimal_entry: dict,
    out_path: Path | str,
    asset: str = "BTC",
    *,
    dpi: int = CHART_DPI,
) -> Path:
    """
    Draw M5 candles (hora real) + caja Long/Short (Entrada/SL/TP), zonas y estado ESPERAR/ENTRAR.

    Rendering lives in app.views.trade_chart (shared BTC / US30 / XAUUSD).
    Writes PNG to out_path. Uses matplotlib Agg + atomic replace (Windows-safe).
    Used for the default High chart (when chart enabled) and for -Ilustrate.
    """
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    m5 = data.get("m5") or []
    if len(m5) < 2:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        # Minimal placeholder so callers/tests still get a file
        fig, ax = plt.subplots(figsize=(8, 3), facecolor="#1e1e1e")
        try:
            ax.set_facecolor("#1e1e1e")
            ax.set_title(f"{asset} M5 — sin velas para ilustrar", color="#569cd6")
            return savefig_png(fig, out, dpi=CHART_DPI_PLACEHOLDER, facecolor="#1e1e1e")
        finally:
            plt.close(fig)

    from app.views.trade_chart import render_trade_chart

    opt = optimal_entry or {}
    return render_trade_chart(
        data, opt, out, asset=asset, dpi=dpi,
        callout=_callout_text(opt), zone_edges=_zone_edges(opt),
    )


def format_illustration_md(
    annotated_file: str,
    *,
    absolute_path: str | Path | None = None,
) -> list[str]:
    """Markdown: chart link relativo a live/ + rutas fáciles de abrir (sin base64)."""
    name = Path(annotated_file).name
    rel = f"live/{name}"
    lines = [
        "## Ilustración entrada (2M5 + óptima)",
        "",
        f"![chart]({name})",
        "",
        "### Salidas (chart)",
        "",
        f"- **Abrir (relativo):** `{rel}`",
        f"- **Markdown:** `![chart]({name})` (desde `live/`)",
    ]
    if absolute_path:
        abs_s = str(Path(absolute_path).resolve())
        lines.append(f"- **Ruta absoluta:** `{abs_s}`")
    lines += ["", "---", ""]
    return lines


def format_salidas_block(
    *,
    signal_md: str | Path | None = None,
    annotated_file: str | None = None,
    annotated_abs: str | Path | None = None,
) -> list[str]:
    """Bloque Salidas al final del reporte: paths clickable-friendly para chat/Cursor."""
    lines = [
        "## Salidas",
        "",
    ]
    if signal_md:
        sp = Path(signal_md)
        rel = f"live/{sp.name}" if sp.name else str(signal_md)
        lines.append(f"- **Reporte:** `{rel}`")
        try:
            lines.append(f"- **Reporte (abs):** `{sp.resolve()}`")
        except OSError:
            lines.append(f"- **Reporte (abs):** `{signal_md}`")
    if annotated_file:
        name = Path(annotated_file).name
        rel = f"live/{name}"
        lines.append(f"- **Chart anotado:** `{rel}`")
        lines.append(f"- **Preview:** `![chart]({name})`")
        if annotated_abs:
            try:
                lines.append(f"- **Chart (abs):** `{Path(annotated_abs).resolve()}`")
            except OSError:
                lines.append(f"- **Chart (abs):** `{annotated_abs}`")
        else:
            lines.append(f"- **Chart (abs):** _(mismo folder que el MD · `{rel}`)_")
    if len(lines) <= 2:
        return []
    lines.append("")
    return lines
