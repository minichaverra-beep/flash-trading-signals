"""Redibujo del chart anotado con niveles reajustados (Recalcular MT5)."""
from datetime import datetime, timedelta, timezone

from app.views.chart_rerender import (
    load_render_inputs,
    main,
    render_inputs_path,
    rerender_chart,
)
from app.views.illustrate_high_entry import create_annotated_entry_chart


def _m5(n=30, start=50600.0):
    t0 = datetime(2026, 10, 1, 13, 0, tzinfo=timezone.utc)
    out = []
    for i in range(n):
        o = start + i
        out.append({"open_time": t0 + timedelta(minutes=5 * i), "open": o, "high": o + 5,
                    "low": o - 5, "close": o + 2})
    return out


def _data():
    return {"m5": _m5(), "price": 50631.0, "price_decimals": 1, "chart_verdict": "NO_OPERAR",
            "setup": {"direction": "LONG"}, "zone": {"level": 50643.4, "type": "support"},
            "generated": "2026-10-01 15:28"}


OPT = {"direction": "LONG", "entry": 50628.4, "sl": 50566.3, "tp": 50752.8, "dec": 1,
       "ahora_action": "ENTRAR"}


def test_render_writes_inputs_sidecar(tmp_path):
    out = tmp_path / "us30_m5_chart_annotated.png"
    written = create_annotated_entry_chart(_data(), OPT, out, asset="US30", dpi=60)
    side = render_inputs_path(written)
    assert side.name == "us30_m5_chart_annotated.render.json"
    inputs = load_render_inputs(side)
    assert inputs["asset"] == "US30"
    assert inputs["data"]["chart_verdict"] == "NO_OPERAR"
    assert isinstance(inputs["data"]["m5"][0]["open_time"], datetime)
    assert inputs["opt"]["entry"] == 50628.4


def test_rerender_uses_sidecar_and_keeps_it(tmp_path):
    out = tmp_path / "us30_m5_chart_annotated.png"
    create_annotated_entry_chart(_data(), OPT, out, asset="US30", dpi=60)
    side = render_inputs_path(out)
    before = side.read_text(encoding="utf-8")
    p = rerender_chart(load_render_inputs(side), out, entry=50682.4, sl=50511.9, tp=50915.7,
                       note="Reajustado con MT5")
    assert p.is_file()
    assert p.stat().st_size > 0
    assert side.read_text(encoding="utf-8") == before


def test_cli_without_sidecar_requires_asset(tmp_path, capsys):
    out = tmp_path / "x.png"
    rc = main(["--chart", str(out), "--entry", "1", "--sl", "0.5", "--tp", "2"])
    assert rc == 1
    assert "--asset" in capsys.readouterr().out


def test_align_to_broker_reemplaza_velas_y_mueve_niveles(tmp_path, monkeypatch):
    from app.models import broker_feed
    from app.views.chart_rerender import align_to_broker

    out = tmp_path / "us30_m5_chart_annotated.png"
    create_annotated_entry_chart(_data(), OPT, out, asset="US30", dpi=60)
    inputs = load_render_inputs(render_inputs_path(out))
    old_last = inputs["data"]["m5"][-1]["close"]
    seen = {}

    def fake_rates(cfg, timeframe, count, until=None):
        seen.update(symbol=cfg["symbol"], timeframe=timeframe, count=count, until=until)
        t0 = int(datetime(2026, 10, 1, 13, 0, tzinfo=timezone.utc).timestamp())
        return {"rates": [{"time": t0 + 300 * i, "open": 50700.0 + i, "high": 50706.0 + i,
                           "low": 50695.0 + i, "close": 50702.0 + i, "volume": 5} for i in range(count)]}

    monkeypatch.setenv("FS_BROKER_FEED", "on")
    monkeypatch.setenv("FS_MT5_SYMBOL_US30", "US30m")
    monkeypatch.setattr(broker_feed, "fetch_rates", fake_rates)
    until = datetime(2026, 10, 1, 15, 30, tzinfo=timezone.utc)
    aligned = align_to_broker(inputs, until)

    delta = aligned["data"]["m5"][-1]["close"] - old_last
    assert seen == {"symbol": "US30m", "timeframe": "M5", "count": len(inputs["data"]["m5"]), "until": until}
    assert aligned["data"]["price"] == aligned["data"]["m5"][-1]["close"]
    assert aligned["data"]["feed"]["label"] == "velas MT5 US30m"
    assert aligned["data"]["zone"]["level"] == 50643.4 + delta
    assert aligned["opt"]["level"] is None or aligned["opt"]["level"] == OPT.get("level", 0) + delta
    assert align_to_broker(aligned, until) is aligned  # ya son velas del broker


def test_align_to_broker_sin_puente_no_toca(tmp_path):
    from app.views.chart_rerender import align_to_broker

    out = tmp_path / "us30_m5_chart_annotated.png"
    create_annotated_entry_chart(_data(), OPT, out, asset="US30", dpi=60)
    inputs = load_render_inputs(render_inputs_path(out))
    assert align_to_broker(inputs) is inputs


def test_rerender_posicion_abierta(tmp_path):
    out = tmp_path / "us30_m5_chart_annotated.png"
    create_annotated_entry_chart(_data(), OPT, out, asset="US30", dpi=60)
    rc = main(["--chart", str(out), "--entry", "50682.4", "--sl", "50511.9", "--tp", "50915.7",
               "--order-state", "open", "--note", "Reajustado con MT5"])
    assert rc == 0
