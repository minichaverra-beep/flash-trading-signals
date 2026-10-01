"""Redibuja el chart anotado (caja Entrada/SL/TP) con niveles reajustados, p.ej. tras moverlos en MT5.

Al renderizar, `create_annotated_entry_chart` guarda junto al PNG un `*.render.json` con las
velas y el contexto usados; `rerender_chart` lo reutiliza para que el gráfico sea el de la señal
(mismas velas y precio), cambiando solo los niveles. Sin ese archivo, `rebuild_inputs`
reconstruye las velas hasta la hora de la señal (sin zona S/R ni sesión).
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPT_KEYS = (
    "direction", "entry", "user_entry", "sl", "tp", "level", "ztype", "dec",
    "zone_lo", "zone_hi", "ahora_action", "ahora_2m5", "scalp_entries",
)
DATA_KEYS = (
    "price", "price_decimals", "session", "data_stale", "generated", "data_freshness",
    "pdh", "pdl", "bias_h1",
)


def render_inputs_path(chart_path: Path | str) -> Path:
    p = Path(chart_path)
    return p.with_name(f"{p.stem}.render.json")


def _candle_out(c: dict) -> dict:
    out = {k: c.get(k) for k in ("open", "high", "low", "close")}
    t = c.get("open_time")
    out["open_time"] = t.isoformat() if isinstance(t, datetime) else None
    return out


def _candle_in(c: dict) -> dict:
    out = {k: float(c[k]) for k in ("open", "high", "low", "close")}
    t = c.get("open_time")
    out["open_time"] = datetime.fromisoformat(t) if t else None
    return out


def dump_render_inputs(
    path: Path | str, data: dict, opt: dict, *, asset: str, dpi: int,
    callout: str, zone_edges: tuple, state: str, history_candles: int,
) -> Path:
    setup = data.get("setup") or {}
    zone = data.get("zone") or {}
    payload = {
        "asset": asset,
        "dpi": dpi,
        "callout": callout,
        "zone_edges": list(zone_edges),
        "data": {
            **{k: data.get(k) for k in DATA_KEYS},
            "chart_verdict": state,
            "setup": {"direction": setup.get("direction")},
            "zone": {"level": zone.get("level"), "type": zone.get("type")},
            "m5": [_candle_out(c) for c in (data.get("m5") or [])[-history_candles:]],
        },
        "opt": {k: opt.get(k) for k in OPT_KEYS},
    }
    out = Path(path)
    out.write_text(json.dumps(payload, ensure_ascii=False, default=str), encoding="utf-8")
    return out


def load_render_inputs(path: Path | str) -> dict:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    payload["data"]["m5"] = [_candle_in(c) for c in payload["data"].get("m5") or []]
    payload["zone_edges"] = tuple(payload.get("zone_edges") or (None, None))
    return payload


def _fetch_m5(asset: str) -> list[dict]:
    key = asset.upper()
    if key == "US30":
        from app.models.us30_data import fetch_us30_klines

        return fetch_us30_klines(m5_bars=300)[0]
    if key == "XAUUSD":
        from app.models.xauusd_data import fetch_xauusd_klines

        return fetch_xauusd_klines(m5_bars=300)[0]
    if key == "BTC":
        from app.controllers.analyze_btc_m5 import fetch_klines

        return fetch_klines("BTCUSDT", "5m", 300)
    raise ValueError(f"asset no soportado: {asset}")


def rebuild_inputs(
    asset: str, until: datetime, *, direction: str | None, verdict: str | None,
    price_decimals: int, price: float | None = None, history_candles: int = 84,
) -> dict:
    """Velas M5 hasta `until` (hora de la señal) cuando no hay *.render.json.

    `price` (precio de la señal) alinea la última vela: el ajuste spot del proxy cambia con el tiempo.
    """
    until = until.astimezone(timezone.utc)
    m5 = []
    for c in _fetch_m5(asset):
        t = c.get("open_time")
        if isinstance(t, datetime) and t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
        if isinstance(t, datetime) and t <= until:
            m5.append(c)
    if len(m5) < 2:
        raise RuntimeError("sin velas anteriores a la señal")
    m5 = m5[-history_candles:]
    if price is not None:
        shift = float(price) - m5[-1]["close"]
        m5 = [{**c, **{k: c[k] + shift for k in ("open", "high", "low", "close")}} for c in m5]
    return {
        "asset": asset.upper(),
        "dpi": None,
        "callout": "Setup listo → ENTRAR",
        "zone_edges": (None, None),
        "data": {
            "m5": m5,
            "price": m5[-1]["close"],
            "price_decimals": price_decimals,
            "chart_verdict": verdict,
            "setup": {"direction": direction},
            "generated": until.strftime("%Y-%m-%d %H:%M"),
        },
        "opt": {"direction": direction, "dec": price_decimals, "ahora_action": "ENTRAR"},
    }


def rerender_chart(
    inputs: dict, out_path: Path | str, *, entry: float, sl: float, tp: float,
    note: str | None = None,
) -> Path:
    from app.views.illustrate_high_entry import CHART_DPI
    from app.views.trade_chart import render_trade_chart

    opt = {**inputs["opt"], "entry": float(entry), "user_entry": None, "sl": float(sl), "tp": float(tp)}
    return render_trade_chart(
        inputs["data"], opt, out_path,
        asset=inputs["asset"], dpi=inputs.get("dpi") or CHART_DPI,
        callout=inputs.get("callout") or "", zone_edges=inputs["zone_edges"], note=note,
    )


def _parse_args(argv: list[str] | None = None):
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chart", required=True, help="PNG anotado a reescribir")
    ap.add_argument("--entry", type=float, required=True)
    ap.add_argument("--sl", type=float, required=True)
    ap.add_argument("--tp", type=float, required=True)
    ap.add_argument("--note", default=None)
    ap.add_argument("--asset", default=None, help="BTC|US30|XAUUSD (si no hay *.render.json)")
    ap.add_argument("--until", default=None, help="ISO de la señal (si no hay *.render.json)")
    ap.add_argument("--direction", default=None)
    ap.add_argument("--verdict", default=None)
    ap.add_argument("--decimals", type=int, default=1)
    ap.add_argument("--price", type=float, default=None, help="precio de la señal (si no hay *.render.json)")
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    chart = Path(args.chart)
    sidecar = render_inputs_path(chart)
    result: dict[str, Any] = {"ok": False, "chart": str(chart)}
    try:
        if sidecar.is_file():
            inputs = load_render_inputs(sidecar)
            result["source"] = "render.json"
        else:
            if not args.asset or not args.until:
                raise RuntimeError("sin *.render.json: hacen falta --asset y --until")
            until = datetime.fromisoformat(args.until.replace("Z", "+00:00"))
            inputs = rebuild_inputs(
                args.asset, until, direction=args.direction, verdict=args.verdict,
                price_decimals=args.decimals, price=args.price,
            )
            result["source"] = "rebuild"
        written = rerender_chart(inputs, chart, entry=args.entry, sl=args.sl, tp=args.tp, note=args.note)
        result.update(ok=True, chart=str(Path(written).resolve()))
    except Exception as e:
        result["error"] = str(e)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
