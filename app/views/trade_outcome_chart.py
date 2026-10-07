"""Captura automática del resultado de una señal: velas M5 reales posteriores con la caja Entrada/SL/TP.

Con los niveles registrados en el historial descarga las velas M5 desde poco antes de la señal
hasta ahora (o hasta la resolución + unas velas), detecta con precio real qué se tocó primero
tras la entrada (TP o SL) y dibuja el gráfico con los helpers compartidos de `trade_chart`.

Reglas de detección (`detect_outcome`):
- La vela en curso al emitir la señal se excluye: no se sabe qué parte de su rango fue posterior.
- Entrada a mercado (cerca del precio de la señal) → ejecutada en la primera vela.
- Entrada límite/stop → ejecutada cuando una vela alcanza el nivel; si antes se toca TP o SL,
  la entrada no se ejecuta (setup cumplido/invalidado sin llenar).
- En la vela de ejecución solo cuenta un nivel situado "más allá" de la entrada en el sentido
  del recorrido; un nivel del otro lado (o ambos) es ambiguo con M5.
- TP y SL dentro de una misma vela tras la entrada → ambiguo (el orden intravela no se sabe).

Datos reales únicamente: Yahoo (GC=F, YM=F/^DJI; M5 solo ~60 días) alineado al precio de la
señal, y Binance BTCUSDT para BTC (la misma fuente que la corrida de la señal).

Con la operación real de MT5 (`--real-entry/--real-exit/--real-close-time`, opcionales
`--real-open-time/--real-sl/--real-ticket`) la caja va de la entrada real al cierre real, la salida
se dibuja en su precio real y el plan (TP/SL) queda fino y discontinuo para comparar. Con
`--trades-json` (original + duplicada de mt5-sent) se dibujan las dos operaciones y el resultado es
la suma de sus PnL. Sin MT5 la caja termina en la vela donde las velas tocan TP/SL, rotulada como
cierre estimado. La caja nunca baja de `MIN_BOX_CANDLES` velas de ancho.

CLI: `python -m app.views.trade_outcome_chart --market xauusd --signal-time ISO --entry .. --sl ..
--tp .. --out x.png [--price ..] [--direction LONG|SHORT] [--real-entry .. --real-exit ..
--real-close-time ISO]` → imprime una línea JSON.
"""
from __future__ import annotations

import json
import math
import os
import sys
import time
import traceback
from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from app.views.trade_chart import (
    BG,
    DOWN,
    ENTRY_C,
    MUTED,
    PANEL,
    SL_C,
    SL_TEXT,
    TEXT,
    TP_C,
    TP_TEXT,
    UP,
    WARN_C,
    _draw_axis_tags,
    _draw_candles,
    _draw_position_box,
    _is_limit_entry,
    _ny_tz,
    _style_axes,
    _y_limits,
    compute_position_levels,
    market_unit,
)

M5 = timedelta(minutes=5)
PRE_CANDLES = 36  # ~3 h antes de la señal
POST_EXIT_CANDLES = 12  # ~1 h tras la resolución
MAX_DISPLAY_CANDLES = 320
YAHOO_M5_MAX_DAYS = 59
BINANCE_KLINES = "https://api.binance.com/api/v3/klines"
BINANCE_MAX_PAGES = 12
MAX_SHIFT_PCT = 0.03

MARKETS: dict[str, dict[str, Any]] = {
    "xauusd": {"asset": "XAUUSD", "tickers": ("GC=F",), "dec": 2},
    "us30": {"asset": "US30", "tickers": ("YM=F", "^DJI"), "dec": 1},
    "btc": {"asset": "BTC", "binance": "BTCUSDT", "tickers": ("BTC-USD",), "dec": 1},
}

OUTCOME_LABELS = {
    "tp": "TP alcanzado",
    "sl": "SL alcanzado",
    "ambiguous": "Ambiguo: TP y SL en la misma vela M5",
    "not_filled": "Entrada no ejecutada",
    "open": "Sin resolver (ni TP ni SL todavía)",
}
OUTCOME_TITLES = {
    "tp": "TP alcanzado",
    "sl": "SL alcanzado",
    "ambiguous": "Ambiguo",
    "not_filled": "Entrada no ejecutada",
    "open": "Sin resolver",
}
OUTCOME_RESULTADO = {"tp": "ganada", "sl": "perdida"}
OUTCOME_COLORS = {"tp": TP_C, "sl": SL_C}


class OutcomeDataError(RuntimeError):
    """Sin datos reales suficientes para evaluar la señal."""


RENDER_RETRIES = 3
RENDER_RETRY_DELAY_S = 0.75
ACCESS_BLOCKED_WINERRORS = (5, 32, 33)  # acceso denegado, archivo en uso, región bloqueada
FILE_BLOCKED_CODE = "file_blocked"
FILE_BLOCKED_MSG = (
    "El antivirus bloqueó el acceso a un archivo al generar la captura "
    f"(reintentado {RENDER_RETRIES} veces)"
)


class FileAccessBlockedError(RuntimeError):
    """Acceso a archivo denegado tras los reintentos (normalmente el antivirus)."""


def is_access_blocked(exc: BaseException) -> bool:
    return isinstance(exc, PermissionError) or (
        isinstance(exc, OSError) and getattr(exc, "winerror", None) in ACCESS_BLOCKED_WINERRORS
    )


def _reset_font_path_caches() -> None:
    """Olvida las rutas de fuentes resueltas por matplotlib.

    `font_manager` resuelve cada fuente con `os.path.realpath` y lo cachea (lru_cache). Si en ese
    instante el antivirus tiene la fuente abierta, la ruta final es `\\\\.\\avgMonFltProxy\\…`,
    abrirla da Errno 13 y, sin vaciar la caché, todos los reintentos del proceso fallarían igual.
    """
    fm = sys.modules.get("matplotlib.font_manager")
    if fm is None:
        return
    font_manager_cls = getattr(fm, "FontManager", None)
    for fn in (
        getattr(fm, "_cached_realpath", None),
        getattr(fm, "_get_font", None),
        getattr(font_manager_cls, "_findfont_cached", None),
    ):
        if hasattr(fn, "cache_clear"):
            fn.cache_clear()


def render_with_retry(render, *, retries: int = RENDER_RETRIES, delay: float = RENDER_RETRY_DELAY_S,
                      sleep=time.sleep):
    """Ejecuta `render()` reintentando bloqueos transitorios de archivo (antivirus escaneando)."""
    last: OSError | None = None
    for attempt in range(retries):
        try:
            return render()
        except OSError as exc:
            if not is_access_blocked(exc):
                raise
            last = exc
            _reset_font_path_caches()
            if attempt + 1 < retries:
                sleep(delay * (attempt + 1))
    raise FileAccessBlockedError(str(last)) from last


def error_payload(exc: BaseException) -> dict[str, Any]:
    """JSON de error para la API: mensaje limpio en español + detalle técnico aparte."""
    if isinstance(exc, FileAccessBlockedError) or is_access_blocked(exc):
        return {"ok": False, "code": FILE_BLOCKED_CODE, "error": FILE_BLOCKED_MSG, "detail": str(exc)}
    return {"ok": False, "error": str(exc) or type(exc).__name__}


@dataclass(frozen=True)
class TradeOutcome:
    status: str  # tp | sl | ambiguous | not_filled | open
    fill_index: int | None = None
    exit_index: int | None = None
    reason: str = ""


@dataclass(frozen=True)
class RealExecution:
    """Operación cerrada en MT5: precios reales y horas UTC (salida = media ponderada de los cierres).

    Sin `open_time`/`close_time` (envíos sin horas guardadas y sin puente) se estiman con las velas:
    primera vela desde `sent_at` que toca la entrada y primera posterior que toca la salida.
    `label`: "" (operación única), "original" o "duplicada".
    """
    entry: float
    exit: float
    close_time: datetime | None
    open_time: datetime | None = None
    sl: float | None = None
    ticket: int | None = None
    tp: float | None = None
    label: str = ""
    pnl_usd: float | None = None
    close_reason: str | None = None
    sent_at: datetime | None = None


def infer_direction(entry: float, sl: float, tp: float) -> str | None:
    """LONG si SL < entrada < TP, SHORT si TP < entrada < SL; None si los niveles son incoherentes."""
    if sl < entry < tp:
        return "LONG"
    if tp < entry < sl:
        return "SHORT"
    return None


def _tp_hit(c: dict, direction: str, tp: float) -> bool:
    return c["high"] >= tp if direction == "LONG" else c["low"] <= tp


def _sl_hit(c: dict, direction: str, sl: float) -> bool:
    return c["low"] <= sl if direction == "LONG" else c["high"] >= sl


def _entry_reached(c: dict, entry: float, ref_price: float) -> bool:
    return c["low"] <= entry if entry <= ref_price else c["high"] >= entry


def _beyond_entry(level: float, entry: float, ref_price: float) -> bool:
    """Nivel situado más allá de la entrada según el sentido en que el precio llegó a ella."""
    return level < entry if entry <= ref_price else level > entry


def _fill_candle_outcome(
    c: dict, i: int, *, direction: str, entry: float, sl: float, tp: float, ref_price: float,
) -> TradeOutcome | None:
    tp_hit, sl_hit = _tp_hit(c, direction, tp), _sl_hit(c, direction, sl)
    if tp_hit and sl_hit:
        return TradeOutcome("ambiguous", i, i, "entrada, TP y SL en la misma vela")
    for hit, level, status in ((tp_hit, tp, "tp"), (sl_hit, sl, "sl")):
        if not hit:
            continue
        if _beyond_entry(level, entry, ref_price):
            return TradeOutcome(status, i, i, "en la vela de la entrada")
        return TradeOutcome("ambiguous", i, i, f"entrada y {status.upper()} en la misma vela")
    return None


def detect_outcome(
    candles: list[dict], *, direction: str, entry: float, sl: float, tp: float,
    ref_price: float, market_entry: bool,
) -> TradeOutcome:
    """Primer toque de TP o SL tras la entrada en `candles` (velas posteriores a la señal)."""
    start = 0
    fill: int | None = None
    if market_entry:
        fill = 0
    else:
        for i, c in enumerate(candles):
            if _entry_reached(c, entry, ref_price):
                fill = i
                done = _fill_candle_outcome(
                    c, i, direction=direction, entry=entry, sl=sl, tp=tp, ref_price=ref_price,
                )
                if done is not None:
                    return done
                start = i + 1
                break
            if _tp_hit(c, direction, tp):
                return TradeOutcome("not_filled", None, i, "TP alcanzado antes de ejecutar la entrada")
            if _sl_hit(c, direction, sl):
                return TradeOutcome("not_filled", None, i, "SL alcanzado antes de ejecutar la entrada")
        if fill is None:
            return TradeOutcome("not_filled", None, None, "el precio no llegó a la entrada")
    for i in range(start, len(candles)):
        c = candles[i]
        tp_hit, sl_hit = _tp_hit(c, direction, tp), _sl_hit(c, direction, sl)
        if tp_hit and sl_hit:
            return TradeOutcome("ambiguous", fill, i, "TP y SL en la misma vela")
        if tp_hit:
            return TradeOutcome("tp", fill, i)
        if sl_hit:
            return TradeOutcome("sl", fill, i)
    return TradeOutcome("open", fill, None, "ni TP ni SL hasta la última vela")


# --------------------------------------------------------------------------- datos


def _as_utc(t: datetime) -> datetime:
    return t.replace(tzinfo=timezone.utc) if t.tzinfo is None else t.astimezone(timezone.utc)


def _yahoo_range(age: timedelta) -> str:
    if age > timedelta(days=YAHOO_M5_MAX_DAYS):
        raise OutcomeDataError(
            f"La señal tiene {age.days} días: Yahoo solo guarda velas M5 de ~60 días"
        )
    if age < timedelta(days=4):
        return "5d"
    return "1mo" if age < timedelta(days=28) else "60d"


def _fetch_binance_since(symbol: str, since: datetime) -> list[dict]:
    rows: list[dict] = []
    start_ms = int(since.timestamp() * 1000)
    for _ in range(BINANCE_MAX_PAGES):
        url = f"{BINANCE_KLINES}?symbol={symbol}&interval=5m&startTime={start_ms}&limit=1000"
        req = Request(url, headers={"User-Agent": "CursorTrading/1.0"})
        with urlopen(req, timeout=20) as resp:
            raw = json.loads(resp.read().decode())
        for k in raw:
            rows.append({
                "open_time": datetime.fromtimestamp(k[0] / 1000, tz=timezone.utc),
                "open": float(k[1]), "high": float(k[2]), "low": float(k[3]), "close": float(k[4]),
            })
        if len(raw) < 1000:
            break
        start_ms = int(raw[-1][0]) + 1
    return rows


BROKER_MAX_BARS = 5000


def _fetch_broker_since(asset: str, since: datetime, now: datetime, notes: list[str]) -> tuple[list[dict], dict] | None:
    """Velas M5 del símbolo del broker (puente MT5): misma escala que las órdenes reales."""
    from app.models.broker_feed import bridge_config, fetch_rates, rates_to_candles

    bcfg = bridge_config(asset)
    if bcfg is None:
        return None
    count = min(BROKER_MAX_BARS, int((now - since) / M5) + 3)
    try:
        payload = fetch_rates(bcfg, "M5", count)
    except (URLError, RuntimeError, TimeoutError, OSError, ValueError, KeyError) as exc:
        notes.append(f"MT5 {bcfg['symbol']} no disponible: {exc}")
        return None
    rows = [c for c in rates_to_candles(payload.get("rates")) if c["open_time"] >= since]
    if not rows or rows[0]["open_time"] - since > timedelta(hours=2):
        notes.append(f"MT5 {bcfg['symbol']}: velas insuficientes desde la señal")
        return None
    return rows, {"source": f"MT5 {bcfg['symbol']}", "proxy": False, "notes": notes}


def fetch_m5_since(market: str, since: datetime, now: datetime | None = None) -> tuple[list[dict], dict]:
    """Velas M5 reales desde `since` → (velas, meta{source, proxy})."""
    from app.models.us30_data import fetch_yahoo_chart

    cfg = MARKETS[market]
    now = now or datetime.now(timezone.utc)
    notes: list[str] = []
    broker = _fetch_broker_since(cfg["asset"], since, now, notes)
    if broker:
        return broker
    if cfg.get("binance"):
        try:
            rows = _fetch_binance_since(cfg["binance"], since)
            if rows:
                return rows, {"source": f"Binance {cfg['binance']}", "proxy": False, "notes": notes}
        except (URLError, HTTPError, TimeoutError, ValueError) as exc:
            notes.append(f"Binance: {exc}")
    rng = _yahoo_range(now - since)
    for ticker in cfg["tickers"]:
        try:
            rows = [c for c in fetch_yahoo_chart(ticker, "5m", rng) if c["open_time"] >= since]
        except (URLError, HTTPError, RuntimeError, TimeoutError, ValueError) as exc:
            notes.append(f"{ticker}: {exc}")
            continue
        if rows:
            return rows, {"source": f"{ticker} (Yahoo)", "proxy": True, "notes": notes}
        notes.append(f"{ticker}: sin velas desde la señal")
    raise OutcomeDataError("No se pudieron obtener velas M5 reales: " + "; ".join(notes))


def align_shift(candles: list[dict], signal_time: datetime, signal_price: float | None) -> float:
    """Desplazamiento proxy→precio de la señal (basis de futuros), con la vela vigente a esa hora."""
    if signal_price is None:
        return 0.0
    ref = None
    for c in candles:
        if c["open_time"] <= signal_time:
            ref = c
        else:
            break
    if ref is None or signal_time - ref["open_time"] > timedelta(minutes=30):
        return 0.0
    shift = float(signal_price) - ref["close"]
    return shift if abs(shift) <= abs(signal_price) * MAX_SHIFT_PCT else 0.0


# --------------------------------------------------------------------------- gráfico


def _resample(candles: list[dict], factor: int, *, from_end: bool) -> list[dict]:
    """Agrupa velas de `factor` en `factor` (solo para dibujar; la detección usa M5)."""
    if factor <= 1 or not candles:
        return list(candles)
    n = len(candles)
    first = n % factor if from_end else 0
    groups = ([candles[:first]] if first else []) + [
        candles[i:i + factor] for i in range(first, n, factor)
    ]
    return [{
        "open_time": g[0]["open_time"], "open": g[0]["open"], "close": g[-1]["close"],
        "high": max(c["high"] for c in g), "low": min(c["low"] for c in g),
    } for g in groups if g]


def _display_index(i: int | None, factor: int, offset: int) -> int | None:
    return None if i is None else offset + i // factor


def _outcome_ticks(times: list[datetime]) -> tuple[list[float], list[str]]:
    """Ticks horarios UTC/NY; con más de un día añade la fecha."""
    if not times:
        return [], []
    span_h = (times[-1] - times[0]).total_seconds() / 3600
    step = next((h for h in (1, 2, 3, 6, 12, 24) if span_h / h <= 12), 48)
    multi_day = span_h > 20
    ny = _ny_tz()
    ticks, labels, last_key = [], [], None
    for i, t in enumerate(times):
        key = (t.date(), t.hour // step) if step < 24 else (t.date().toordinal() // (step // 24),)
        if key == last_key:
            continue
        last_key = key
        if i == 0 and t.minute != 0:
            continue
        top = f"{t:%d/%m %H:%M}" if multi_day else f"{t:%H:%M}"
        ticks.append(float(i))
        labels.append(f"{top}\n{t.astimezone(ny):%H:%M} NY")
    return ticks, labels


def _fmt_hm(t: datetime | None) -> str:
    return f"{t:%H:%M}" if t else "—"


def _fmt_when(t: datetime | None, signal_time: datetime) -> str:
    if t is None:
        return "—"
    return f"{t:%H:%M}" if t.date() == signal_time.date() else f"{t:%d/%m %H:%M}"


def outcome_message(outcome: TradeOutcome, post: list[dict], signal_time: datetime) -> str:
    """Mensaje corto en español (✓ TP alcanzado HH:MM / ✗ SL alcanzado HH:MM …)."""
    def at(i: int | None) -> datetime | None:
        return post[i]["open_time"] if i is not None and i < len(post) else None

    exit_t = _fmt_when(at(outcome.exit_index), signal_time)
    if outcome.status == "tp":
        return f"✓ TP alcanzado {exit_t} UTC"
    if outcome.status == "sl":
        return f"✗ SL alcanzado {exit_t} UTC"
    if outcome.status == "ambiguous":
        return f"? Ambiguo {exit_t} UTC: {outcome.reason} (M5 no muestra el orden)"
    if outcome.status == "not_filled":
        return f"Entrada no ejecutada: {outcome.reason}"
    last = _fmt_when(post[-1]["open_time"], signal_time) if post else "—"
    return f"Sin resolver: ni TP ni SL hasta {last} UTC"


@dataclass(frozen=True)
class TradeStats:
    filled: bool
    in_progress: bool = False
    duration_min: int | None = None
    exit_price: float | None = None
    r_multiple: float | None = None
    units: float | None = None
    mfe_r: float | None = None
    mae_r: float | None = None
    duration_estimated: bool = False


def compute_trade_stats(
    outcome: TradeOutcome, post: list[dict], *, direction: str, entry: float, sl: float, tp: float,
    unit_size: float, ref_price: float, market_entry: bool,
) -> TradeStats:
    """Duración, resultado (R y unidades) y MFE/MAE con las velas M5 reales tras la entrada.

    Sin resolver → hasta la última vela (flotante al cierre). Ambiguo → sin R (no se sabe la salida).
    """
    f = outcome.fill_index
    if f is None or f >= len(post):
        return TradeStats(filled=False)
    resolved = outcome.status in ("tp", "sl", "ambiguous") and outcome.exit_index is not None
    end = min(outcome.exit_index, len(post) - 1) if resolved else len(post) - 1
    duration = int((post[end]["open_time"] - post[f]["open_time"]).total_seconds() // 60)
    risk, reward = abs(entry - sl), abs(tp - entry)
    long_ = direction == "LONG"
    fav = adv = 0.0
    for i in range(f, end + 1):
        hi, lo = post[i]["high"], post[i]["low"]
        if i == f and not market_entry:
            # en la vela de ejecución solo es posterior a la entrada el lado "más allá" de ella
            hi, lo = (entry, lo) if entry <= ref_price else (hi, entry)
        up, down = max(hi - entry, 0.0), max(entry - lo, 0.0)
        fav = max(fav, up if long_ else down)
        adv = max(adv, down if long_ else up)
    fav, adv = min(fav, reward), min(adv, risk)
    exit_price = {"tp": tp, "sl": sl, "open": post[end]["close"]}.get(outcome.status)
    move = None if exit_price is None else (exit_price - entry) * (1.0 if long_ else -1.0)

    def in_r(v: float | None) -> float | None:
        return None if v is None or risk <= 1e-12 else v / risk

    return TradeStats(
        filled=True, in_progress=outcome.status == "open", duration_min=duration,
        exit_price=exit_price, r_multiple=in_r(move),
        units=None if move is None else move / unit_size, mfe_r=in_r(fav), mae_r=in_r(adv),
        duration_estimated=True,
    )


def candle_index_at(candles: list[dict], t: datetime) -> int:
    """Índice de la vela que contiene `t` (antes de la primera → 0; después de la última → última)."""
    idx = 0
    for i, c in enumerate(candles):
        if c["open_time"] > t:
            break
        idx = i
    return idx


def _first_touch(post: list[dict], start: int, price: float) -> int | None:
    for i in range(max(start, 0), len(post)):
        if post[i]["low"] <= price <= post[i]["high"]:
            return i
    return None


@dataclass(frozen=True)
class TradeSpan:
    """Velas de entrada/cierre de una operación real y sus horas (reales de MT5 o estimadas)."""
    fill: int
    exit: int
    open_time: datetime
    close_time: datetime
    open_estimated: bool = False
    close_estimated: bool = False


def trade_span(real: RealExecution, post: list[dict]) -> TradeSpan:
    """Horas reales de MT5 si las hay; si no, la primera vela que toca la entrada/salida."""
    if real.open_time:
        fill, open_t = candle_index_at(post, real.open_time), real.open_time
    else:
        start = candle_index_at(post, real.sent_at) if real.sent_at else 0
        touched = _first_touch(post, start, real.entry)
        fill = start if touched is None else touched
        open_t = max(post[fill]["open_time"], real.sent_at) if real.sent_at else post[fill]["open_time"]
    if real.close_time:
        exit_i, close_t = max(candle_index_at(post, real.close_time), fill), real.close_time
    else:
        touched = _first_touch(post, fill, real.exit)
        exit_i = fill if touched is None else touched
        close_t = max(post[exit_i]["open_time"], open_t)
    return TradeSpan(fill, exit_i, open_t, close_t, real.open_time is None, real.close_time is None)


def real_indices(real: RealExecution, post: list[dict]) -> tuple[int, int]:
    """(vela de la entrada real, vela del cierre real) en `post`."""
    span = trade_span(real, post)
    return span.fill, span.exit


def real_move(real: RealExecution, direction: str) -> float:
    """Recorrido real a favor (+) o en contra (−) de la posición."""
    return (real.exit - real.entry) * (1.0 if direction == "LONG" else -1.0)


def compute_real_stats(
    real: RealExecution, post: list[dict], *, direction: str, sl: float, unit_size: float,
) -> TradeStats:
    """Stats con la ejecución real de MT5: R realizado = recorrido real / |entrada real − SL|.

    MFE/MAE salen de las velas entre la vela de entrada y la de cierre (aproximación M5).
    """
    span = trade_span(real, post)
    f, end = span.fill, span.exit
    duration = max(int((span.close_time - span.open_time).total_seconds() // 60), 0)
    risk = abs(real.entry - sl)
    long_ = direction == "LONG"
    fav = adv = 0.0
    for c in post[f:end + 1]:
        up, down = max(c["high"] - real.entry, 0.0), max(real.entry - c["low"], 0.0)
        fav = max(fav, up if long_ else down)
        adv = max(adv, down if long_ else up)
    move = real_move(real, direction)

    def in_r(v: float) -> float | None:
        return None if risk <= 1e-12 else v / risk

    return TradeStats(
        filled=True, in_progress=False, duration_min=duration, exit_price=real.exit,
        r_multiple=in_r(move), units=move / unit_size, mfe_r=in_r(fav), mae_r=in_r(min(adv, risk)),
        duration_estimated=span.open_estimated or span.close_estimated,
    )


def _signed(v: float, dec: int = 1) -> str:
    v = round(v, dec)
    return f"{'−' if v < 0 else '+'}{abs(v):.{dec}f}"


def fmt_duration(minutes: int) -> str:
    days, rem = divmod(max(int(minutes), 0), 1440)
    h, m = divmod(rem, 60)
    if days:
        return f"{days}d {h}h {m:02d}m"
    return f"{h}h {m:02d}m" if h else f"{m}m"


def fmt_duration_label(minutes: int, *, estimated: bool) -> str:
    """Duración para el gráfico: con velas M5 no se distingue por debajo de una vela («<5m»)."""
    minutes = max(int(minutes), 0)
    if estimated and minutes < 5:
        return "<5m"
    return "<1m" if minutes < 1 else fmt_duration(minutes)


def stats_lines(
    stats: TradeStats, outcome: TradeOutcome, *, direction: str, entry: float, unit_label: str, fmt: str,
    exit_note: str | None = None,
) -> list[str]:
    """Recuadro del gráfico: duración, resultado en R/unidades, MFE/MAE y precios entrada→salida.

    `exit_note` se añade a la línea de precios (p. ej. «MT5 20:54 UTC» o «cierre estimado 21:35»).
    """
    sep = "  ·  "
    if not stats.filled:
        reason = outcome.reason[:1].upper() + outcome.reason[1:] if outcome.reason else ""
        return [f"{direction}{sep}Entrada no ejecutada"] + ([reason] if reason else [])
    duration = fmt_duration_label(stats.duration_min or 0, estimated=stats.duration_estimated)
    head = f"{direction}{sep}Duración {duration}"
    lines = [head + (f"{sep}en curso" if stats.in_progress else "")]
    parts = []
    if stats.r_multiple is not None and stats.units is not None:
        prefix = "Flotante " if stats.in_progress else ""
        parts.append(f"{prefix}{_signed(stats.r_multiple)}R · {_signed(stats.units)} {unit_label}")
    if stats.mfe_r is not None and stats.mae_r is not None:
        parts.append(f"MFE {_signed(stats.mfe_r)}R · MAE {_signed(-stats.mae_r)}R")
    if parts:
        lines.append(sep.join(parts))
    if stats.exit_price is not None:
        word = "Actual" if stats.in_progress else "Salida"
        tail = f"{sep}{exit_note}" if exit_note else ""
        lines.append(f"Entrada {entry:{fmt}} → {word} {stats.exit_price:{fmt}}{tail}")
    elif outcome.status == "ambiguous":
        lines.append(f"Entrada {entry:{fmt}}{sep}TP y SL en la misma vela M5")
    return lines


def stats_payload(stats: TradeStats, unit_label: str) -> dict[str, Any]:
    def r2(v: float | None) -> float | None:
        return None if v is None else round(v, 2)

    if not stats.filled:
        return {"filled": False}
    return {
        "filled": True, "inProgress": stats.in_progress, "durationMin": stats.duration_min,
        "exitPrice": None if stats.exit_price is None else round(stats.exit_price, 6), "rMultiple": r2(stats.r_multiple), "units": r2(stats.units),
        "unitLabel": unit_label, "mfeR": r2(stats.mfe_r), "maeR": r2(stats.mae_r),
    }


MIN_BOX_CANDLES = 6  # una operación de 0–5 min no se comprime a una sola vela
SIDE_COLORS = {"LONG": "#4fa3ff", "SHORT": "#ff6b6b"}  # flecha de entrada estilo MT5: compra azul, venta roja
SIDE_WORDS = {"LONG": "Compra", "SHORT": "Venta"}
DUP_ENTRY_C = "#c586c0"
TRADE_NAMES = {"original": "Original", "duplicada": "Duplicada"}
TRADE_SHORT = {"original": "Orig", "duplicada": "Dup"}
REASON_WORDS = {"tp": "TP", "sl": "SL", "stopout": "stop out", "manual": "manual"}
CONNECTOR_LS = (0, (4, 3))
LABEL_STEP_PT = 19


def box_span(x_fill: float, x_exit: float, *, x_start: float | None = None) -> tuple[float, float]:
    """Caja de la operación: de la vela de entrada (o `x_start`) a la de cierre, con ancho mínimo."""
    x0 = (x_fill if x_start is None else x_start) - 0.5
    return x0, max(x_exit + 0.5, x0 + MIN_BOX_CANDLES)


def _draw_entry_marker(ax, x: float, y: float, direction: str, *, hollow: bool = False) -> None:
    col = SIDE_COLORS.get(direction, ENTRY_C)
    ax.scatter([x], [y], s=110, marker="v" if direction == "SHORT" else "^", color=BG if hollow else col,
               edgecolors=col if hollow else BG, linewidths=1.6 if hollow else 1.0, zorder=11)


def _draw_exit_marker(ax, x: float, y: float, color: str, *, win: bool, hollow: bool = False) -> None:
    """Cierre: círculo si gana, aspa si pierde (color por resultado); hueco para la duplicada."""
    ax.scatter([x], [y], s=85 if win else 95, marker="o" if win else "X", color=BG if hollow else color,
               edgecolors=color if hollow else BG, linewidths=1.6 if hollow else 1.0, zorder=11)


class _LabelSlots:
    """Apila las etiquetas de los marcadores por lado (encima/debajo · izquierda/derecha) sin solaparlas."""

    def __init__(self) -> None:
        self.used: dict[tuple[bool, bool], int] = {}

    def offset(self, *, above: bool, right: bool) -> float:
        k = self.used.get((above, right), 0)
        self.used[(above, right)] = k + 1
        dy = 14 + LABEL_STEP_PT * k
        return dy if above else -dy


def _marker_label(ax, x: float, y: float, text: str, color: str, *, dx: float, dy: float) -> None:
    ax.annotate(
        text, (x, y), xytext=(dx, dy), textcoords="offset points",
        ha="left" if dx >= 0 else "right", va="center", color=color, fontsize=9, fontweight="bold",
        zorder=12, arrowprops={"arrowstyle": "-", "color": color, "linewidth": 0.8, "alpha": 0.8},
        bbox={"boxstyle": "round,pad=0.25", "facecolor": PANEL, "edgecolor": color, "alpha": 0.93},
    )


PLAN_LINESTYLE = (0, (3, 3))


def _result_color(move: float) -> str:
    if move > 0:
        return TP_C
    return SL_C if move < 0 else WARN_C


MAX_PRICE_DECIMALS = 5  # los brokers cotizan como mucho a 5 decimales; más es ruido de coma flotante


def price_decimals(dec: int, *values: float) -> int:
    """Decimales para mostrar precios del bróker sin redondearlos a la precisión del feed de velas."""
    places = (len(f"{float(v):.{MAX_PRICE_DECIMALS}f}".rstrip("0").partition(".")[2]) for v in values)
    return max(dec, *places)


def real_message(real: RealExecution, direction: str, signal_time: datetime) -> str:
    """«✓ Ganada en MT5: salida 84610.17 a las 20:54 UTC»."""
    move = real_move(real, direction)
    mark = "✓" if move > 0 else "✗"
    return f"{mark} {real_title(move)}: salida {real.exit} a las {_fmt_when(real.close_time, signal_time)} UTC"


def real_title(move: float) -> str:
    if move > 0:
        return "Ganada en MT5"
    return "Perdida en MT5" if move < 0 else "Cerrada en MT5"


def _draw_plan_levels(ax, tags: list[dict], plan: dict[str, float], drawn: dict[str, float], *,
                      x0: float, x1: float, fmt: str, dec: int) -> None:
    """Plan de la señal fino y discontinuo (TP plan / SL plan / Entrada plan) para comparar con lo real.

    SL y entrada del plan se omiten si coinciden con lo dibujado como real.
    """
    tick = 10 ** (-dec)
    for key, name, col in (("tp", "TP plan", TP_C), ("sl", "SL plan", SL_C), ("entry", "Entrada plan", ENTRY_C)):
        v = plan[key]
        if key != "tp" and abs(drawn[key] - v) < tick:
            continue
        ax.hlines(v, x0, x1, color=col, linewidth=0.8, linestyles=PLAN_LINESTYLE, alpha=0.6, zorder=2)
        tags.append({"y": v, "text": f"{name} {v:{fmt}}", "fg": col, "bg": PANEL, "edge": col, "prio": 2})


def trade_gain(real: RealExecution, direction: str) -> float:
    """Signo del resultado: PnL en $ de MT5 si existe (incluye comisiones), si no el recorrido."""
    return real.pnl_usd if real.pnl_usd is not None else real_move(real, direction)


def trade_result_text(real: RealExecution, direction: str, unit) -> str:
    if real.pnl_usd is not None:
        return f"{_signed(real.pnl_usd, 2)} $"
    return f"{_signed(real_move(real, direction) / unit.size)} {unit.label}"


def _hm_mark(t: datetime, estimated: bool) -> str:
    return ("≈" if estimated else "") + _fmt_hm(_as_utc(t))


def _time_x(fr: "_Frame", post: list[dict], i: int, t: datetime, estimated: bool) -> float:
    """X de un instante dentro de su vela (hora real de MT5); estimado → centro de la vela."""
    x = float(fr.x(i))
    if estimated or fr.factor != 1:
        return x
    frac = (_as_utc(t) - post[i]["open_time"]).total_seconds() / M5.total_seconds()
    return x - 0.5 + min(max(frac, 0.1), 0.9)


def _draw_trade(ax, tags: list[dict], fr: "_Frame", real: RealExecution, span: TradeSpan, post: list[dict], *,
                direction: str, plan_sl: float, unit, fmt: str, slots: _LabelSlots) -> None:
    """Una operación real: caja entrada→salida (ancho mínimo), flecha de entrada, marcador de cierre
    unidos por una línea discontinua y etiquetas apiladas. La duplicada va en discontinuo/hueca."""
    from matplotlib.patches import Rectangle

    e, x = real.entry, real.exit
    gain = trade_gain(real, direction)
    color = _result_color(gain)
    dup = real.label == "duplicada"
    sl = real.sl or plan_sl
    x0, x1 = box_span(fr.x(span.fill), fr.x(span.exit))
    w = x1 - x0
    edge_ls = (0, (4, 2)) if dup else "-"
    entry_c = DUP_ENTRY_C if dup else ENTRY_C

    ax.add_patch(Rectangle((x0, min(e, sl)), w, abs(sl - e), facecolor=SL_C, alpha=0.08,
                           edgecolor="none", zorder=2))
    if real.tp:
        ax.add_patch(Rectangle((x0, min(e, real.tp)), w, abs(real.tp - e), facecolor=TP_C, alpha=0.06,
                               edgecolor="none", zorder=2))
    result = Rectangle((x0, min(e, x)), w, abs(x - e), facecolor=color, alpha=0.2 if dup else 0.28,
                       edgecolor=color, linewidth=1.0, linestyle=edge_ls, zorder=3)
    result.set_gid("trade-result")
    ax.add_patch(result)
    ax.hlines(e, x0, x1, color=entry_c, linewidth=1.5, linestyles=edge_ls, zorder=5)
    ax.hlines(x, x0, x1, color=color, linewidth=1.3, linestyles=edge_ls, zorder=5)
    ax.hlines(sl, x0, x1, color=SL_C, linewidth=0.9, linestyles=edge_ls, alpha=0.8, zorder=5)
    if real.tp:
        ax.hlines(real.tp, x0, x1, color=TP_C, linewidth=0.9, linestyles=edge_ls, alpha=0.8, zorder=5)

    xe = _time_x(fr, post, span.fill, span.open_time, span.open_estimated)
    xc = _time_x(fr, post, span.exit, span.close_time, span.close_estimated)
    ax.plot([xe, xc], [e, x], color=color, linewidth=1.3, linestyle=CONNECTOR_LS, zorder=10)
    _draw_entry_marker(ax, xe, e, direction, hollow=dup)
    _draw_exit_marker(ax, xc, x, color, win=gain > 0, hollow=dup)

    short = TRADE_SHORT.get(real.label, real.label)
    who = f"{short} " if short else ""
    reason = REASON_WORDS.get(real.close_reason or "")
    reason_txt = f"{reason} " if reason in ("TP", "SL") else ""
    mark = "✓" if gain > 0 else "✗"
    exit_above = x >= e
    _marker_label(ax, xc, x, f"{mark} {who}{reason_txt}{trade_result_text(real, direction, unit)} · "
                  f"{_hm_mark(span.close_time, span.close_estimated)}",
                  TP_TEXT if gain > 0 else SL_TEXT, dx=12, dy=slots.offset(above=exit_above, right=True))
    side = SIDE_WORDS.get(direction, direction)
    _marker_label(ax, xe, e, f"{who}{side if not short else side.lower()} {_hm_mark(span.open_time, span.open_estimated)}",
                  entry_c, dx=-12, dy=slots.offset(above=not exit_above, right=False))

    entry_name = "Dup" if dup else "Entrada"
    exit_name = "Cierre Dup" if dup else "Cierre"
    tags.extend([
        {"y": x, "text": f"{exit_name} {x:{fmt}}", "fg": color, "bg": PANEL, "edge": color, "prio": 2},
        {"y": e, "text": f"{entry_name} {e:{fmt}}", "fg": BG, "bg": entry_c, "edge": entry_c, "prio": 1},
    ])
    if not dup:
        tags.append({"y": sl, "text": f"SL {sl:{fmt}}", "fg": BG, "bg": SL_C, "edge": SL_C, "prio": 1})


@dataclass(frozen=True)
class _Frame:
    """Velas visibles y posición de la señal en el eje X."""
    show: list[dict]
    factor: int
    offset: int

    def x(self, i: int | None) -> int | None:
        return _display_index(i, self.factor, self.offset)


def _frame(pre: list[dict], post: list[dict], last_i: int | None) -> _Frame:
    end = len(post) if last_i is None else min(len(post), last_i + 1 + POST_EXIT_CANDLES)
    pre_show, post_show = pre[-PRE_CANDLES:], post[:end]
    factor = max(1, math.ceil((len(pre_show) + len(post_show)) / MAX_DISPLAY_CANDLES))
    pre_d = _resample(pre_show, factor, from_end=True)
    show = pre_d + _resample(post_show, factor, from_end=False)
    if not show:
        raise OutcomeDataError("sin velas para dibujar")
    return _Frame(show, factor, len(pre_d))


def _draw_detected(ax, tags: list[dict], fr: _Frame, outcome: TradeOutcome, post: list[dict], *,
                   pos: dict, entry: float, sl: float, tp: float, market_entry: bool, fmt: str, dec: int) -> str | None:
    """Caja del plan con el resultado según las velas; devuelve la nota de cierre estimado (o None)."""
    x0 = fr.offset - 0.5
    fill_x, exit_x = fr.x(outcome.fill_index), fr.x(outcome.exit_index)
    resolved = exit_x is not None and outcome.status in ("tp", "sl", "ambiguous")
    if resolved:
        x1 = box_span(fr.offset, exit_x)[1]
    else:
        x1 = max(len(fr.show) - 0.5, x0 + MIN_BOX_CANDLES)
    word = "Entrada" if market_entry else "Entrada límite"
    _draw_position_box(ax, tags, pos, x0=x0, x1=x1, active=outcome.fill_index is not None,
                       entry_word=word, fmt=fmt, dec=dec)
    if fill_x is not None:
        _draw_entry_marker(ax, fill_x, entry, pos["direction"])
    if not resolved:
        return None
    level = sl if outcome.status == "sl" else tp
    color = OUTCOME_COLORS.get(outcome.status, WARN_C)
    when = _fmt_hm(post[outcome.exit_index]["open_time"])
    if fill_x is not None:
        ax.plot([fill_x, exit_x], [entry, level], color=color, linewidth=1.3, linestyle=CONNECTOR_LS, zorder=10)
    _draw_exit_marker(ax, exit_x, level, color, win=outcome.status == "tp")
    text = {"tp": f"✓ TP alcanzado ≈{when}", "sl": f"✗ SL alcanzado ≈{when}"}.get(
        outcome.status, f"? TP y SL {when}")
    # fuera de la caja: encima de un nivel superior, debajo de uno inferior
    _marker_label(ax, exit_x, level, text, color, dx=12, dy=16 if level > entry else -16)
    return f"cierre estimado {when}" if outcome.status in ("tp", "sl") else None


def _draw_trades(ax, tags: list[dict], fr: _Frame, trades: list[RealExecution], spans: list[TradeSpan],
                 post: list[dict], *, pos: dict, direction: str, fmt: str, dec: int) -> None:
    """Operaciones reales de MT5 (original y duplicada) sobre el plan fino y discontinuo."""
    main = trades[0]
    _draw_plan_levels(ax, tags, {"entry": pos["entry"], "sl": pos["sl"], "tp": pos["tp"]},
                      {"entry": main.entry, "sl": main.sl or pos["sl"]}, x0=fr.offset - 0.5,
                      x1=len(fr.show) - 0.5, fmt=fmt, dec=dec)
    slots = _LabelSlots()
    for real, span in zip(trades, spans):
        _draw_trade(ax, tags, fr, real, span, post, direction=direction, plan_sl=pos["sl"],
                    unit=pos["unit"], fmt=fmt, slots=slots)


def combined_pnl(trades: list[RealExecution]) -> float | None:
    """PnL total en $ (suma, como combineAnnotations del server); None si ninguna lo trae."""
    vals = [t.pnl_usd for t in trades if t.pnl_usd is not None]
    return round(sum(vals), 2) if vals else None


def multi_title(trades: list[RealExecution], direction: str, unit) -> str:
    """«+9.32 $ (original −2.42 $ · duplicada TP +11.74 $)»."""
    parts = []
    for t in trades:
        reason = REASON_WORDS.get(t.close_reason or "")
        bits = [t.label or "operación", reason if reason in ("TP", "SL") else "",
                trade_result_text(t, direction, unit)]
        parts.append(" ".join(b for b in bits if b))
    total = combined_pnl(trades)
    head = f"{_signed(total, 2)} $" if total is not None else f"{len(trades)} operaciones"
    return f"{head} ({' · '.join(parts)})"


def multi_lines(trades: list[RealExecution], spans: list[TradeSpan], *, direction: str, unit,
                fmt: str) -> list[str]:
    """Recuadro con varias operaciones: total y una línea por operación (precios, horas, duración, $)."""
    sep = "  ·  "
    total = combined_pnl(trades)
    head = f"{direction}{sep}{len(trades)} operaciones"
    lines = [head + (f"{sep}Total {_signed(total, 2)} $" if total is not None else "")]
    for t, s in zip(trades, spans):
        minutes = int((_as_utc(s.close_time) - _as_utc(s.open_time)).total_seconds() // 60)
        dur = fmt_duration_label(minutes, estimated=s.open_estimated or s.close_estimated)
        hours = f"{_hm_mark(s.open_time, s.open_estimated)}→{_hm_mark(s.close_time, s.close_estimated)} UTC"
        parts = [f"{TRADE_NAMES.get(t.label, t.label or 'Operación')}: {t.entry:{fmt}} → {t.exit:{fmt}}",
                 f"{hours} ({dur})", trade_result_text(t, direction, unit)]
        reason = REASON_WORDS.get(t.close_reason or "")
        if reason:
            parts.append(reason)
        lines.append(sep.join(parts))
    return lines


def render_outcome_chart(
    pre: list[dict], post: list[dict], outcome: TradeOutcome, out_path: Path | str, *,
    asset: str, direction: str, entry: float, sl: float, tp: float, dec: int,
    signal_time: datetime, market_entry: bool, note: str | None = None, dpi: int = 140,
    ref_price: float | None = None, real: RealExecution | None = None,
    trades: list[RealExecution] | None = None,
) -> Path:
    """Gráfico del resultado. `trades` (original + duplicada) o `real` (una sola) → operaciones de MT5;
    sin ellas, el resultado estimado con las velas."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from app.views.illustrate_high_entry import savefig_png

    trades = list(trades or ([real] if real else []))
    spans = [trade_span(t, post) for t in trades]
    fr = _frame(pre, post, max(s.exit for s in spans) if spans else outcome.exit_index)
    show = fr.show
    price = show[-1]["close"]
    pos = compute_position_levels(direction, entry, sl, tp, asset)
    trade_levels = [v for t in trades for v in (t.entry, t.exit, t.sl or sl, t.tp) if v]
    if trades:
        dec = price_decimals(dec, *trade_levels)
    fmt = f".{dec}f"
    multi = len(trades) > 1 or any(t.label for t in trades)
    interval = "M5" if fr.factor == 1 else f"M{5 * fr.factor} (detección en M5)"

    fig = None
    try:
        fig, ax = plt.subplots(figsize=(14, 7.4), facecolor=BG)
        ax.set_facecolor(BG)
        fig.subplots_adjust(left=0.025, right=0.885, top=0.865, bottom=0.12)
        _draw_candles(ax, show, price)
        ax.set_ylim(*_y_limits(show, price, (entry, sl, tp, *trade_levels)))
        ax.set_xlim(-1, len(show) + 2)

        x0 = fr.offset - 0.5
        ax.axvline(x0, color=MUTED, linewidth=0.8, linestyle=":", alpha=0.7, zorder=2)
        ymin, ymax = ax.get_ylim()
        ax.text(x0 - 0.4, ymax - (ymax - ymin) * 0.015, f"Señal {_fmt_hm(signal_time)} UTC",
                color=MUTED, fontsize=8.5, ha="right", va="top", zorder=6)
        tags: list[dict] = []
        lines: list[str] | None = None
        if trades:
            _draw_trades(ax, tags, fr, trades, spans, post, pos=pos, direction=direction, fmt=fmt, dec=dec)
        if multi:
            total = combined_pnl(trades)
            color = _result_color(total if total is not None else sum(real_move(t, direction) for t in trades))
            result = multi_title(trades, direction, pos["unit"])
            lines = multi_lines(trades, spans, direction=direction, unit=pos["unit"], fmt=fmt)
        elif trades:
            one, span = trades[0], spans[0]
            exit_note = (f"cierre estimado {_fmt_hm(span.close_time)}" if span.close_estimated
                         else f"MT5 {_fmt_hm(_as_utc(span.close_time))} UTC")
            move = real_move(one, direction)
            color, result = _result_color(move), real_title(move)
            stats = compute_real_stats(one, post, direction=direction, sl=one.sl or sl, unit_size=pos["unit"].size)
        else:
            exit_note = _draw_detected(ax, tags, fr, outcome, post, pos=pos, entry=entry, sl=sl, tp=tp,
                                       market_entry=market_entry, fmt=fmt, dec=dec)
            color, result = OUTCOME_COLORS.get(outcome.status, WARN_C), OUTCOME_TITLES[outcome.status]
            stats = compute_trade_stats(
                outcome, post, direction=direction, entry=entry, sl=sl, tp=tp, unit_size=pos["unit"].size,
                ref_price=post[0]["open"] if ref_price is None else ref_price, market_entry=market_entry,
            )

        pcol = UP if show[-1]["close"] >= show[-1]["open"] else DOWN
        ax.axhline(price, color=pcol, linewidth=0.8, linestyle=(0, (1, 2)), alpha=0.9, zorder=2)
        tags.insert(0, {"y": price, "text": f"{price:{fmt}}", "fg": BG, "bg": pcol, "edge": pcol, "prio": 0})
        _draw_axis_tags(ax, tags)

        if lines is None:
            lines = stats_lines(stats, outcome, direction=direction, entry=trades[0].entry if trades else entry,
                                unit_label=pos["unit"].label, fmt=fmt, exit_note=exit_note)
        if note:
            lines.append(note)
        ax.text(0.0, 1.012, "\n".join(lines), transform=ax.transAxes, color=color, fontsize=9.5,
                fontweight="bold", va="bottom", ha="left",
                bbox={"boxstyle": "round,pad=0.35", "facecolor": PANEL, "edgecolor": color, "alpha": 0.95})
        title = (f"{asset} {interval} · señal {signal_time:%Y-%m-%d %H:%M} UTC · "
                 f"Resultado: {result}")
        fig.suptitle(title, color=color, fontsize=13, fontweight="bold", x=0.455, y=0.985)

        _style_axes(ax, show, len(show))
        ticks, labels = _outcome_ticks([_as_utc(c["open_time"]) for c in show])
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels, fontsize=8, color=TEXT)
        ax.set_xlabel(f"Hora UTC (arriba) · Nueva York (abajo) · velas {interval}", color=MUTED, fontsize=8)
        return savefig_png(fig, out_path, dpi=dpi, facecolor=BG)
    finally:
        if fig is not None:
            plt.close(fig)


# --------------------------------------------------------------------------- orquestación


def evaluate_signal(
    market: str, *, signal_time: datetime, entry: float, sl: float, tp: float,
    out_path: Path | str, price: float | None = None, direction: str | None = None,
    now: datetime | None = None, real: RealExecution | None = None,
    trades: list[RealExecution] | None = None,
) -> dict[str, Any]:
    market = market.lower()
    if market not in MARKETS:
        raise ValueError(f"mercado no soportado: {market}")
    cfg = MARKETS[market]
    geo = infer_direction(entry, sl, tp)
    if geo is None:
        raise ValueError("Niveles incoherentes: SL y TP deben quedar a lados opuestos de la entrada")
    if direction and direction.upper() != geo:
        raise ValueError(f"La dirección {direction.upper()} no cuadra con los niveles ({geo})")
    signal_time = _as_utc(signal_time)
    now = _as_utc(now or datetime.now(timezone.utc))
    candles, meta = fetch_m5_since(market, signal_time - PRE_CANDLES * M5 - timedelta(hours=1), now)
    shift = align_shift(candles, signal_time, price) if meta["proxy"] else 0.0
    if shift:
        candles = [{**c, **{k: c[k] + shift for k in ("open", "high", "low", "close")}} for c in candles]
    pre = [c for c in candles if c["open_time"] < signal_time]
    post = [c for c in candles if c["open_time"] >= signal_time]
    if not post:
        raise OutcomeDataError("Aún no hay velas M5 posteriores a la señal")
    dec = int(cfg["dec"])
    ref_price = float(price) if price is not None else post[0]["open"]
    pos = compute_position_levels(geo, entry, sl, tp, cfg["asset"])
    market_entry = not _is_limit_entry(pos, ref_price, dec)
    outcome = detect_outcome(post, direction=geo, entry=entry, sl=sl, tp=tp,
                             ref_price=ref_price, market_entry=market_entry)
    trades = [_utc_trade(t) for t in (trades or ([real] if real is not None else []))]
    real = trades[0] if len(trades) == 1 and not trades[0].label else None
    feed_note = (f"Velas {meta['source']} (sin MT5: pueden no coincidir con los precios del broker)"
                 if meta["proxy"] else None)
    chart = render_with_retry(lambda: render_outcome_chart(
        pre, post, outcome, out_path, asset=cfg["asset"], direction=geo, entry=entry, sl=sl, tp=tp,
        dec=dec, signal_time=signal_time, market_entry=market_entry, ref_price=ref_price, trades=trades,
        note=feed_note,
    ))
    if trades:
        main = trades[0]
        stats = compute_real_stats(main, post, direction=geo, sl=main.sl or sl, unit_size=pos["unit"].size)
    else:
        stats = compute_trade_stats(outcome, post, direction=geo, entry=entry, sl=sl, tp=tp,
                                    unit_size=pos["unit"].size, ref_price=ref_price, market_entry=market_entry)

    def iso(i: int | None) -> str | None:
        return post[i]["open_time"].isoformat() if i is not None else None

    spans = [trade_span(t, post) for t in trades]
    estimated = outcome.status in ("tp", "sl") and outcome.exit_index is not None
    if trades:
        last = max(spans, key=lambda s: s.close_time)
        close_time = _as_utc(last.close_time).isoformat()
        close_source = "velas" if last.close_estimated else "mt5"
    else:
        close_time, close_source = (iso(outcome.exit_index), "velas") if estimated else (None, None)
    if real is not None:
        message = real_message(real, geo, signal_time)
    elif trades:
        message = multi_message(trades, geo, pos["unit"])
    else:
        message = outcome_message(outcome, post, signal_time)

    return {
        "ok": True,
        "outcome": outcome.status,
        "label": OUTCOME_LABELS[outcome.status],
        "message": message,
        "reason": outcome.reason or None,
        "detected": OUTCOME_RESULTADO.get(outcome.status),
        "direction": geo,
        "entryType": "mercado" if market_entry else "límite",
        "signalTime": signal_time.isoformat(),
        "fillTime": iso(outcome.fill_index),
        "exitTime": iso(outcome.exit_index),
        "lastCandle": post[-1]["open_time"].isoformat(),
        "source": meta["source"],
        "shift": round(shift, dec),
        "stats": stats_payload(stats, pos["unit"].label),
        "closeTime": close_time,
        "closeSource": close_source,
        "real": None if real is None else {
            "ticket": real.ticket, "entry": real.entry, "exit": real.exit, "sl": real.sl,
            "openTime": real.open_time.isoformat() if real.open_time else None,
            "closeTime": real.close_time.isoformat() if real.close_time else None,
        },
        "trades": [trade_payload(t, s) for t, s in zip(trades, spans)] if real is None and trades else None,
        "combinedPnlUsd": combined_pnl(trades) if real is None and trades else None,
        # abspath y no resolve(): realpath puede devolver la ruta proxy del antivirus
        "chart": os.path.abspath(chart),
    }


def _utc_trade(t: RealExecution) -> RealExecution:
    def utc(v: datetime | None) -> datetime | None:
        return _as_utc(v) if v else None

    return replace(t, close_time=utc(t.close_time), open_time=utc(t.open_time), sent_at=utc(t.sent_at))


def multi_message(trades: list[RealExecution], direction: str, unit) -> str:
    """«✓ Total en MT5: +9.32 $ (original −2.42 $ · duplicada +11.74 $)»."""
    total = combined_pnl(trades)
    gain = total if total is not None else sum(real_move(t, direction) for t in trades)
    return f"{'✓' if gain > 0 else '✗'} Total en MT5: {multi_title(trades, direction, unit)}"


def trade_payload(t: RealExecution, s: TradeSpan) -> dict[str, Any]:
    return {
        "label": t.label or None, "ticket": t.ticket, "entry": t.entry, "exit": t.exit, "pnlUsd": t.pnl_usd,
        "closeReason": t.close_reason, "openTime": _as_utc(s.open_time).isoformat(),
        "closeTime": _as_utc(s.close_time).isoformat(),
        "timesSource": "velas" if s.open_estimated or s.close_estimated else "mt5",
    }


def _parse_args(argv: list[str] | None = None):
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--market", required=True, choices=sorted(MARKETS))
    ap.add_argument("--signal-time", required=True, help="ISO 8601 de la señal (UTC)")
    ap.add_argument("--entry", type=float, required=True)
    ap.add_argument("--sl", type=float, required=True)
    ap.add_argument("--tp", type=float, required=True)
    ap.add_argument("--out", required=True, help="PNG de salida")
    ap.add_argument("--price", type=float, default=None, help="precio en la señal (alinea el proxy)")
    ap.add_argument("--direction", default=None, help="LONG|SHORT (se valida contra los niveles)")
    ap.add_argument("--real-entry", type=float, default=None, help="entrada real MT5")
    ap.add_argument("--real-exit", type=float, default=None, help="salida real MT5 (media ponderada)")
    ap.add_argument("--real-close-time", default=None, help="ISO 8601 UTC del último cierre MT5")
    ap.add_argument("--real-open-time", default=None, help="ISO 8601 UTC de la entrada MT5")
    ap.add_argument("--real-sl", type=float, default=None, help="SL con que se abrió en MT5")
    ap.add_argument("--real-ticket", type=int, default=None, help="posición MT5")
    ap.add_argument("--trades-json", default=None,
                    help="operaciones MT5 (original + duplicada) en JSON; tiene prioridad sobre --real-*")
    return ap.parse_args(argv)


def _parse_iso(raw: str) -> datetime:
    return _as_utc(datetime.fromisoformat(raw.replace("Z", "+00:00")))


def real_from_args(args) -> RealExecution | None:
    """Operación real de la CLI; incompleta (sin entrada, salida u hora de cierre) → None."""
    if args.real_entry is None or args.real_exit is None or not args.real_close_time:
        return None
    if args.real_entry <= 0 or args.real_exit <= 0:
        raise ValueError("--real-entry y --real-exit deben ser > 0")
    return RealExecution(
        entry=args.real_entry, exit=args.real_exit, close_time=_parse_iso(args.real_close_time),
        open_time=_parse_iso(args.real_open_time) if args.real_open_time else None,
        sl=args.real_sl if args.real_sl and args.real_sl > 0 else None, ticket=args.real_ticket,
    )


def _positive(v: Any) -> float | None:
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return f if f > 0 and math.isfinite(f) else None


def trades_from_json(raw: str | None) -> list[RealExecution]:
    """`--trades-json` del server: [{label, ticket, entry, exit, sl, tp, openedAt, closedAt, sentAt, pnlUsd,
    closeReason}]. Las operaciones sin entrada o salida se descartan."""
    if not raw:
        return []
    items = json.loads(raw)
    if not isinstance(items, list):
        raise ValueError("--trades-json debe ser una lista")

    def when(v: Any) -> datetime | None:
        return _parse_iso(v) if isinstance(v, str) and v else None

    trades = []
    for it in items:
        entry, exit_ = _positive(it.get("entry")), _positive(it.get("exit"))
        if entry is None or exit_ is None:
            continue
        pnl = it.get("pnlUsd")
        trades.append(RealExecution(
            entry=entry, exit=exit_, close_time=when(it.get("closedAt")), open_time=when(it.get("openedAt")),
            sl=_positive(it.get("sl")), ticket=it.get("ticket"), tp=_positive(it.get("tp")),
            label=str(it.get("label") or ""), pnl_usd=float(pnl) if isinstance(pnl, (int, float)) else None,
            close_reason=it.get("closeReason") or None, sent_at=when(it.get("sentAt")),
        ))
    return trades


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        result = evaluate_signal(
            args.market,
            signal_time=datetime.fromisoformat(args.signal_time.replace("Z", "+00:00")),
            entry=args.entry, sl=args.sl, tp=args.tp, out_path=args.out,
            price=args.price, direction=args.direction, real=real_from_args(args),
            trades=trades_from_json(args.trades_json) or None,
        )
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        result = error_payload(e)
    print(json.dumps(result))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
