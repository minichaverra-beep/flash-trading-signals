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
    "pdh", "pdl", "bias_h1", "feed",
)
ORDER_STATES = ("pending", "open", "closed", "canceled", "expired")


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
    from app.views.trade_chart import verdict_reasons

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
            "state_reasons": verdict_reasons(data, state),
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


def _shift_level(v, delta: float):
    return None if v is None else float(v) + delta


def align_to_broker(inputs: dict, until: datetime | None = None) -> dict:
    """Si las velas no son del broker, las reemplaza por las M5 de MT5 hasta `until`.

    Los niveles reajustados vienen de MT5: dibujarlos sobre velas de otro feed (YM=F, GC=F,
    Binance) los desplaza respecto al precio. Zona S/R y PDH/PDL se mueven con el mismo
    desfase. Sin puente MT5 se devuelve `inputs` sin tocar (el chart rotula la fuente).
    """
    data = inputs["data"]
    old = data.get("m5") or []
    if (data.get("feed") or {}).get("source") == "mt5" or len(old) < 2:
        return inputs
    from app.models.broker_feed import bridge_config, feed_info, fetch_rates, rates_to_candles

    cfg = bridge_config(inputs.get("asset"))
    if cfg is None:
        return inputs
    if until is None and data.get("generated"):
        until = datetime.strptime(str(data["generated"])[:16], "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
    try:
        m5 = rates_to_candles(fetch_rates(cfg, "M5", len(old), until).get("rates"))
    except Exception as e:
        print(f"WARN velas MT5 no disponibles: {e}", flush=True)
        return inputs
    if len(m5) < 2:
        return inputs
    delta = m5[-1]["close"] - float(old[-1]["close"])
    new_data = {
        **data,
        "m5": m5,
        "price": m5[-1]["close"],
        "pdh": _shift_level(data.get("pdh"), delta),
        "pdl": _shift_level(data.get("pdl"), delta),
        "zone": {**(data.get("zone") or {}), "level": _shift_level((data.get("zone") or {}).get("level"), delta)},
        "feed": feed_info("mt5", cfg["asset"], cfg["symbol"]),
    }
    opt = dict(inputs.get("opt") or {})
    for k in ("level", "zone_lo", "zone_hi"):
        opt[k] = _shift_level(opt.get(k), delta)
    if opt.get("scalp_entries"):
        opt["scalp_entries"] = [[float(e) + delta, src] for e, src in opt["scalp_entries"]]
    edges = tuple(_shift_level(v, delta) for v in (inputs.get("zone_edges") or (None, None)))
    return {**inputs, "data": new_data, "opt": opt, "zone_edges": edges, "broker_delta": delta}


def rerender_chart(
    inputs: dict, out_path: Path | str, *, entry: float, sl: float, tp: float,
    note: str | None = None, order_state: str | None = None,
) -> Path:
    from app.views.illustrate_high_entry import CHART_DPI
    from app.views.trade_chart import render_trade_chart

    opt = {**inputs["opt"], "entry": float(entry), "user_entry": None, "sl": float(sl), "tp": float(tp)}
    data = {**inputs["data"], "order_state": order_state}
    return render_trade_chart(
        data, opt, out_path,
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
    ap.add_argument("--order-state", choices=ORDER_STATES, default=None, help="estado real de la orden en MT5")
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    chart = Path(args.chart)
    sidecar = render_inputs_path(chart)
    result: dict[str, Any] = {"ok": False, "chart": str(chart)}
    try:
        until = datetime.fromisoformat(args.until.replace("Z", "+00:00")) if args.until else None
        if sidecar.is_file():
            inputs = load_render_inputs(sidecar)
            result["source"] = "render.json"
        else:
            if not args.asset or until is None:
                raise RuntimeError("sin *.render.json: hacen falta --asset y --until")
            inputs = rebuild_inputs(
                args.asset, until, direction=args.direction, verdict=args.verdict,
                price_decimals=args.decimals, price=args.price,
            )
            result["source"] = "rebuild"
        inputs = align_to_broker(inputs, until)
        result["feed"] = (inputs["data"].get("feed") or {}).get("label")
        written = rerender_chart(
            inputs, chart, entry=args.entry, sl=args.sl, tp=args.tp, note=args.note,
            order_state=args.order_state,
        )
        result.update(ok=True, chart=str(Path(written).resolve()))
    except Exception as e:
        result["error"] = str(e)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
