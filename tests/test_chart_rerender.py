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
    assert p.is_file() and p.stat().st_size > 0
    assert side.read_text(encoding="utf-8") == before


def test_cli_without_sidecar_requires_asset(tmp_path, capsys):
    out = tmp_path / "x.png"
    rc = main(["--chart", str(out), "--entry", "1", "--sl", "0.5", "--tp", "2"])
    assert rc == 1
    assert "--asset" in capsys.readouterr().out
