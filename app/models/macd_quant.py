"""MACD quant — núcleo matemático + soft-filter **H4** para E1 M5.

Contrato (igual Zentinel FVG+Vol):
  - NUNCA trigger solo para E1.
  - Solo filtro de confluencia / feature candidata.
  - Evaluación en cierre de barra (sin look-ahead).

Timeframe del filtro / mini-chart:
  - **H4** (régimen / Hist / cruce Strategy A de la última H4 cerrada).
  - Entradas E1 siguen en M5 (H1/CTR + zona + 2M5) — sin cambio.
  - Si no hay parquet H4 nativo: resample limpio M5→H4 (plot) o H1→H4
    (analyze live, ~200 H1 → ~50 H4; 200 M5 solo dan ~4 H4).

Strategy A (filtro): cruce MACD × Signal + filtro precio vs EMA200 (en H4).
Strategy B (zero-line cross): variante documentada; NO es entrada E1 sola.

Ver: docs/strategy/TRADING_QUANT_MACD_E1_BACKTEST.md
"""
from __future__ import annotations

from typing import Any

import pandas as pd

# Defaults clásicos (H3 baseline a falsar en backtest — métricas PENDING).
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
TREND_EMA = 200

TIMEFRAME = "H4"
H4_RESAMPLE = "4h"
# ~7 días × 6 barras H4/día (contexto «semana de mercado» del mini-chart).
WEEK_H4_BARS = 42
# Mínimo de M5 para preferir M5→H4 frente a H1→H4 en attach (~2 días).
_MIN_M5_FOR_H4 = 48 * 12

ROLE = "confluence_filter"
NEVER_TRIGGER = True


def calculate_macd(
    df: pd.DataFrame,
    fast: int = MACD_FAST,
    slow: int = MACD_SLOW,
    signal: int = MACD_SIGNAL,
) -> pd.DataFrame:
    """Calcula MACD / Signal / Histogram / EMA200 sobre ``close`` (barra cerrada).

    Usa ``ewm(..., adjust=False)`` — equivalente recursivo estándar.
    Timeframe esperado del ``df``: H4 para soft-filter / mini-chart.
    """
    out = df.copy()
    close = out["close"].astype(float)
    fast_ema = close.ewm(span=fast, adjust=False).mean()
    slow_ema = close.ewm(span=slow, adjust=False).mean()
    out["macd"] = fast_ema - slow_ema
    out["signal_line"] = out["macd"].ewm(span=signal, adjust=False).mean()
    out["histogram"] = out["macd"] - out["signal_line"]
    out["trend_ema"] = close.ewm(span=TREND_EMA, adjust=False).mean()
    return out


def generate_signals(df: pd.DataFrame) -> pd.DataFrame:
    """Strategy A: cruce MACD×Signal filtrado por precio vs EMA200.

    Solo marca en el cierre de ``t`` usando ``shift(1)`` (sin look-ahead).
    ``signal``: 1 = BUY (long), -1 = SELL (short), 0 = sin cruce filtrado.
    En runtime E1 esto es informativo / soft-filter — nunca ENTRAR solo.
    """
    out = df.copy()
    out["signal"] = 0
    bullish_cross = (out["macd"] > out["signal_line"]) & (
        out["macd"].shift(1) <= out["signal_line"].shift(1)
    )
    bearish_cross = (out["macd"] < out["signal_line"]) & (
        out["macd"].shift(1) >= out["signal_line"].shift(1)
    )
    above_trend = out["close"] > out["trend_ema"]
    below_trend = out["close"] < out["trend_ema"]
    out.loc[bullish_cross & above_trend, "signal"] = 1
    out.loc[bearish_cross & below_trend, "signal"] = -1
    return out


def zero_line_cross_flags(df: pd.DataFrame) -> pd.DataFrame:
    """Strategy B (variante): cruce de MACD por cero — NO es entrada E1 sola.

    Añade columnas informativas ``macd_zero_up`` / ``macd_zero_down``.
    No escribe en ``signal`` (ese campo es solo Strategy A).
    """
    out = df.copy()
    m = out["macd"]
    out["macd_zero_up"] = (m > 0) & (m.shift(1) <= 0)
    out["macd_zero_down"] = (m < 0) & (m.shift(1) >= 0)
    return out


def candles_to_ohlcv_df(candles: list | pd.DataFrame) -> pd.DataFrame:
    """Normaliza lista de velas o DataFrame a columnas OHLCV + open_time."""
    if isinstance(candles, pd.DataFrame):
        df = candles.copy()
    else:
        df = pd.DataFrame(list(candles))
    cols = {str(c).lower(): c for c in df.columns}
    rename = {}
    for need in ("open", "high", "low", "close", "volume", "open_time"):
        if need in df.columns:
            continue
        if need in cols:
            rename[cols[need]] = need
    if rename:
        df = df.rename(columns=rename)
    if "close" not in df.columns:
        raise ValueError(f"Sin columna close; cols={list(df.columns)}")
    if "open_time" in df.columns:
        df = df.sort_values("open_time").reset_index(drop=True)
    return df


def resample_to_h4(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega OHLCV a H4 (4h UTC, label/closed left).

    No hay parquet H4 nativo en data/ (solo M5 + H1). Preferir M5→H4
    cuando haya historia larga; H1→H4 es válido y documentado.
    """
    work = candles_to_ohlcv_df(df)
    if "open_time" not in work.columns:
        raise ValueError("resample_to_h4 requiere open_time")
    ts = pd.to_datetime(work["open_time"], utc=True)
    work = work.set_index(ts)
    agg: dict[str, str] = {
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
    }
    if "volume" in work.columns:
        agg["volume"] = "sum"
    h4 = work.resample(H4_RESAMPLE, label="left", closed="left").agg(agg)
    h4 = h4.dropna(subset=["close"]).reset_index()
    # reset_index deja el índice temporal como primera columna
    time_col = h4.columns[0]
    if time_col != "open_time":
        h4 = h4.rename(columns={time_col: "open_time"})
    return h4


def build_h4_frame_from_data(data: dict) -> tuple[pd.DataFrame | None, str]:
    """Construye frame H4 para soft-filter desde ``data`` de analyze.

    Prioridad:
      1. ``data['h4']`` si ya viene en H4
      2. ``data['m5']`` → H4 si hay suficientes M5 (≥ ~2 días)
      3. ``data['h1']`` → H4 (caso tipico analyze: 200 H1 ≈ 50 H4)
      4. ``data['m5']`` → H4 aunque sea corto (último recurso)

    Returns:
      (df_h4 | None, source_note)
    """
    h4_raw = data.get("h4") or []
    if h4_raw:
        try:
            return candles_to_ohlcv_df(h4_raw), "h4"
        except ValueError:
            pass

    m5 = data.get("m5") or []
    h1 = data.get("h1") or []

    if len(m5) >= _MIN_M5_FOR_H4:
        try:
            return resample_to_h4(candles_to_ohlcv_df(m5)), "m5_resample_h4"
        except ValueError:
            pass

    if h1:
        try:
            return resample_to_h4(candles_to_ohlcv_df(h1)), "h1_resample_h4"
        except ValueError:
            pass

    if m5:
        try:
            return resample_to_h4(candles_to_ohlcv_df(m5)), "m5_resample_h4_short"
        except ValueError:
            pass

    return None, "sin m5/h1/h4"


def macd_soft_filter_ok(direction: str, row: Any) -> bool | None:
    """Soft-filter E1 sobre **régimen H4**: ¿Hist alineado con el setup?

    - LONG → Hist H4 > 0
    - SHORT → Hist H4 < 0
    - None si faltan datos / dirección inválida (no veta ni bonifica).

    Nunca dispara ENTRAR por sí solo; ``analyze_*`` / confluencia lo usan
    como flag Ext/filtro. La entrada sigue siendo H1/CTR + zona + 2M5.
    """
    dir_u = (direction or "").upper().strip()
    if dir_u not in ("LONG", "SHORT"):
        return None
    hist = _row_get(row, "histogram")
    if hist is None:
        return None
    try:
        h = float(hist)
    except (TypeError, ValueError):
        return None
    if h != h:  # NaN
        return None
    if dir_u == "LONG":
        return h > 0
    return h < 0


def macd_confluence_points(
    direction: str,
    row: Any,
) -> tuple[float, float, str]:
    """Puntos soft para ``compute_confluencia_setup`` (análogo a volumen Zentinel).

    max = 1.0. A favor → 1.0; en contra → 0.0; sin datos → (0, 0, "").
    No inventa pesos de fusión High.
    """
    ok = macd_soft_filter_ok(direction, row)
    if ok is None:
        return 0.0, 0.0, ""
    if ok:
        return 1.0, 1.0, "MACD H4 Hist a favor (filtro)"
    return 0.0, 1.0, "MACD H4 Hist en contra (filtro)"


def attach_macd_quant_to_data(
    data: dict,
    *,
    df: pd.DataFrame | None = None,
) -> dict:
    """Enriquece ``data`` con snapshot MACD de la última **H4** cerrada (muta).

    Si se pasa ``df`` ya con columnas MACD (se asume H4), no recalcula.
    Si no, construye H4 desde ``h4`` / ``m5`` / ``h1`` (ver ``build_h4_frame_from_data``).
    """
    source = "df"
    work = df
    if work is None:
        work, source = build_h4_frame_from_data(data)
        if work is None or work.empty:
            data["macd_quant"] = {
                "role": ROLE,
                "never_trigger": NEVER_TRIGGER,
                "available": False,
                "timeframe": TIMEFRAME,
                "note": source or "sin h4 / m5 / h1",
            }
            return data
        if "close" not in work.columns:
            data["macd_quant"] = {
                "role": ROLE,
                "never_trigger": NEVER_TRIGGER,
                "available": False,
                "timeframe": TIMEFRAME,
                "note": f"{source} sin close",
            }
            return data
        work = calculate_macd(work)
        work = generate_signals(work)

    last = work.iloc[-1]
    direction = (data.get("setup") or {}).get("direction") or data.get("direction") or ""
    soft_ok = macd_soft_filter_ok(str(direction), last)
    snap = {
        "role": ROLE,
        "never_trigger": NEVER_TRIGGER,
        "available": True,
        "timeframe": TIMEFRAME,
        "source": source,
        "macd": _safe_float(last.get("macd")),
        "signal_line": _safe_float(last.get("signal_line")),
        "histogram": _safe_float(last.get("histogram")),
        "trend_ema": _safe_float(last.get("trend_ema")),
        "signal": int(last.get("signal") or 0),
        "soft_filter_ok": soft_ok,
        "params": {
            "fast": MACD_FAST,
            "slow": MACD_SLOW,
            "signal": MACD_SIGNAL,
            "trend": TREND_EMA,
            "timeframe": TIMEFRAME,
        },
        "strategy": "A_signal_crossover",
        "strategy_b_note": "zero-line cross = variante; no entrada E1 sola",
        "bars_h4": int(len(work)),
    }
    data["macd_quant"] = snap
    return data


def macd_report_lines(data: dict | None = None) -> list[str]:
    """Bloque markdown breve para High/Advanced (filtro H4, no trigger)."""
    mq = (data or {}).get("macd_quant") or {}
    if not mq.get("available"):
        return [
            "### MACD-quant (filtro E1 · H4)",
            "",
            "- **Rol:** confluence_filter — **NUNCA trigger solo**.",
            "- Timeframe filtro: **H4** (régimen). Entrada E1 sigue en M5.",
            "- Snapshot: n/d (sin datos MACD H4 en esta corrida).",
            "",
        ]
    soft = mq.get("soft_filter_ok")
    soft_s = "alineado" if soft is True else ("en contra" if soft is False else "n/d")
    hist = mq.get("histogram")
    hist_s = f"{hist:.4g}" if isinstance(hist, (int, float)) else "n/d"
    sig = mq.get("signal", 0)
    sig_s = {1: "BUY cross", -1: "SELL cross"}.get(int(sig or 0), "sin cruce A")
    src = mq.get("source") or "h4"
    return [
        "### MACD-quant (filtro E1 · H4)",
        "",
        "- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.",
        f"- **TF filtro:** H4 · fuente `{src}` · Hist: {hist_s} · soft-filter vs setup: **{soft_s}**",
        f"- **Strategy A (última H4):** {sig_s} (EMA200 filter)",
        "- Strategy B (zero-line): variante documentada; no dispara E1 sola.",
        "- Backtest WR/PF: **PENDING** (ver TRADING_QUANT_MACD_E1_BACKTEST.md).",
        "",
    ]


def _row_get(row: Any, key: str) -> Any:
    if row is None:
        return None
    if isinstance(row, dict):
        return row.get(key)
    try:
        if hasattr(row, "index") and key in row.index:
            return row[key]
    except (TypeError, KeyError, ValueError):
        pass
    return getattr(row, key, None) if not isinstance(row, dict) else None


def _safe_float(v: Any) -> float | None:
    if v is None:
        return None
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    if f != f:
        return None
    return f
