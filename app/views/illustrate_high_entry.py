"""Generate annotated M5 chart for high-signal optimal entry (2M5 + zona + Entry/SL/TP)."""
from __future__ import annotations

import io
import json
import os
import re
import tempfile
import time
from datetime import datetime, timedelta, timezone
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
                try:
                    os.fsync(fh.fileno())
                except OSError:
                    # En el proot de Android fsync puede devolver EINVAL y abortar el PNG.
                    pass
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
    return "Sin 2M5 · revisar bias/SL"


def write_entry_overlay_charts(
    data: dict,
    optimal_entry: dict,
    *,
    asset: str = "BTC",
    main_chart_path: Path | str | None = None,
    annotated_path: Path | str | None = None,
    dpi: int | None = None,
    _free: bool = True,
) -> dict:
    """
    Write OPTI/SL/TP/S-R overlays onto the default High chart and/or the -Ilustrate PNG.

    - main_chart_path: live/*_m5_chart.png (when chart enabled / not -NoChart)
    - annotated_path: live/*_m5_chart_annotated.png (when -Ilustrate)

    Si no hay velas, se pide el respaldo público una sola vez y se dibuja.
    Un RecursionError no vuelve a pedir velas: el fallo se convierte en error.
    """
    if _free and len(data.get("m5") or []) < 2:
        return _capture_from_free_candles(
            data, optimal_entry, asset=asset, main_chart_path=main_chart_path,
            annotated_path=annotated_path, dpi=dpi, reason="Yahoo no dejó velas para la captura",
        )
    try:
        return _paint_entry_charts(
            data, optimal_entry, asset=asset, main_chart_path=main_chart_path,
            annotated_path=annotated_path, dpi=dpi,
        )
    except RecursionError as exc:
        raise RuntimeError("recursión al dibujar el gráfico; no se vuelven a pedir velas") from exc
    except Exception as exc:
        if not _free:
            raise
        return _capture_from_free_candles(
            data, optimal_entry, asset=asset, main_chart_path=main_chart_path,
            annotated_path=annotated_path, dpi=dpi, reason=str(exc),
        )


def _capture_from_free_candles(
    data: dict,
    optimal_entry: dict,
    *,
    asset: str,
    main_chart_path,
    annotated_path,
    dpi,
    reason: str,
) -> dict:
    from app.models.free_candles import align_last_close, fetch_free_m5

    try:
        candles, label = fetch_free_m5(asset, 300)
    except RecursionError as exc:
        raise RuntimeError("recursión en el fallback de velas") from exc
    except Exception as exc:
        print(f"WARN captura: {reason}. Endpoint libre: {exc}", flush=True)
        # Velas que la señal ya trae, o el aviso «sin velas». No se reintenta la red.
        return _paint_entry_charts(
            data, optimal_entry, asset=asset, main_chart_path=main_chart_path,
            annotated_path=annotated_path, dpi=dpi,
        )
    print(f"Captura: {label} ({reason})", flush=True)
    fresh = dict(data)
    fresh["m5"] = align_last_close(candles, data.get("price"))
    fresh["feed"] = {"source": "free", "broker": False, "label": label}
    return write_entry_overlay_charts(
        fresh, optimal_entry, asset=asset, main_chart_path=main_chart_path,
        annotated_path=annotated_path, dpi=dpi, _free=False,
    )


def _paint_entry_charts(
    data: dict,
    optimal_entry: dict,
    *,
    asset: str,
    main_chart_path,
    annotated_path,
    dpi,
) -> dict:
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
        from app.views.mpl_safe import disable_mathtext

        disable_mathtext()
        import matplotlib.pyplot as plt

        # Minimal placeholder so callers/tests still get a file
        fig, ax = plt.subplots(figsize=(8, 3), facecolor="#1e1e1e")
        try:
            ax.set_facecolor("#1e1e1e")
            ax.set_title(f"{asset} M5 — sin velas para ilustrar", color="#569cd6")
            return savefig_png(fig, out, dpi=CHART_DPI_PLACEHOLDER, facecolor="#1e1e1e")
        finally:
            plt.close(fig)

    from app.views.chart_rerender import dump_render_inputs, render_inputs_path
    from app.views.trade_chart import HISTORY_CANDLES, render_trade_chart, resolve_signal_state

    opt = optimal_entry or {}
    callout, zone_edges = _callout_text(opt), _zone_edges(opt)
    written = render_trade_chart(
        data, opt, out, asset=asset, dpi=dpi, callout=callout, zone_edges=zone_edges,
    )
    try:
        dump_render_inputs(
            render_inputs_path(written), data, opt, asset=asset, dpi=dpi, callout=callout,
            zone_edges=zone_edges, state=resolve_signal_state(data, opt),
            history_candles=HISTORY_CANDLES,
        )
    except Exception as e:
        print(f"WARN render inputs: {e}")
    return written


def log_chart_failure(asset: str, exc: BaseException) -> None:
    """Stdout/stderr del job. Sin esta línea la tarjeta omite el PNG y no dice por qué."""
    from app.views.mpl_safe import print_compact_traceback

    print(f"ERROR chart: no se escribió el PNG de entrada de {asset}: {exc}", flush=True)
    print_compact_traceback(exc)


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


_OHLC_RE = re.compile(
    r"O=([0-9]+(?:\.[0-9]+)?)\s+H=([0-9]+(?:\.[0-9]+)?)\s+"
    r"L=([0-9]+(?:\.[0-9]+)?)\s+C=([0-9]+(?:\.[0-9]+)?)"
)


def candles_from_report_text(text: str) -> list[dict]:
    """OHLC ya escrito en el reporte (`O= H= L= C=`). No inventa precios."""
    rows = []
    base = datetime(2020, 1, 1, tzinfo=timezone.utc)
    for i, match in enumerate(_OHLC_RE.finditer(text or "")):
        o, h, l, c = (float(match.group(k)) for k in range(1, 5))
        if min(o, h, l, c) <= 0:
            continue
        ot = base + timedelta(minutes=5 * i)
        rows.append({
            "open_time": ot, "close_time": ot,
            "open": o, "high": h, "low": l, "close": c, "volume": 0.0,
        })
    return rows


def _candles_from_render_json(path: Path) -> tuple[list[dict], dict]:
    from app.views.chart_rerender import load_render_inputs

    payload = load_render_inputs(path)
    data = payload.get("data") or {}
    return list(data.get("m5") or []), payload


def ensure_local_entry_png(
    out_path: Path | str,
    *,
    asset: str,
    report_path: Path | str | None = None,
    decimals: int = 1,
) -> str | None:
    """PNG de entrada para la tarjeta, sin red.

    Orden: el PNG que ya existe, el ``*.render.json`` de esa captura, o el OHLC
    del reporte. Cero velas → None (la tarjeta puede decir que no hay gráfico).
    """
    out = Path(out_path)
    if out.is_file() and out.stat().st_size > 800:
        return str(out.resolve())

    candles: list[dict] = []
    opt: dict = {"dec": decimals, "ahora_action": "ESPERAR"}
    data: dict = {"price_decimals": decimals, "setup": {}}
    render_path = out.with_name(f"{out.stem}.render.json")
    if render_path.is_file():
        try:
            candles, payload = _candles_from_render_json(render_path)
            data = dict(payload.get("data") or data)
            opt = dict(payload.get("opt") or opt)
        except (OSError, ValueError, KeyError, json.JSONDecodeError):
            candles = []
    if len(candles) < 2 and report_path:
        try:
            candles = candles_from_report_text(Path(report_path).read_text(encoding="utf-8"))
        except OSError:
            candles = []
        if candles:
            data = {
                "m5": candles,
                "price": candles[-1]["close"],
                "price_decimals": decimals,
                "setup": {"direction": opt.get("direction") or "LONG"},
            }
    if len(candles) < 2:
        return None
    data["m5"] = candles
    written = write_entry_overlay_charts(
        data, opt, asset=asset, main_chart_path=None, annotated_path=out, dpi=80, _free=False,
    )
    path = written.get("annotated_chart")
    return path if path and Path(path).is_file() else None


def main(argv: list[str] | None = None) -> int:
    """Dibuja el PNG de la tarjeta con velas locales. Una línea JSON en stdout."""
    import argparse
    import sys

    ap = argparse.ArgumentParser(description="PNG de velas de la tarjeta, sin red")
    ap.add_argument("--out", required=True)
    ap.add_argument("--asset", required=True)
    ap.add_argument("--report", default=None)
    ap.add_argument("--decimals", type=int, default=1)
    args = ap.parse_args(argv)
    try:
        path = ensure_local_entry_png(
            args.out, asset=args.asset, report_path=args.report, decimals=args.decimals,
        )
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), flush=True)
        return 1
    print(json.dumps({"ok": bool(path), "path": path}), flush=True)
    return 0 if path else 1


if __name__ == "__main__":
    raise SystemExit(main())
