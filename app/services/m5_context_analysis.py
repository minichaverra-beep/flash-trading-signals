"""
M5 market CONTEXT — structure bias + whether the move is still VIGENTE or AGOTANDO.

Distinct from Light/High (no Entry/SL/TP, no 0.15% zone, no RSI 70/30, no EMA20/50 H1).
Uses M5 structure with its own lookbacks and exhaustion metrics.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

# --- Thresholds UNIQUE to CONTEXT (do not mirror Light/High) ---
SWING_LOOKBACK = 4          # High/Light use 3
SWING_KEEP = 7              # High/Light keep last 5
EMA_FAST = 9                # not EMA20
EMA_SLOW = 21               # not EMA50
SLOPE_BARS = 6               # H1 bias uses 4
ATR_PERIOD = 14
IMPULSE_VIGENTE_MAX_ATR = 1.75   # impulse stretch still healthy
IMPULSE_AGOTA_ATR = 2.55         # overextended → agotando
RSI_BULL_EXHAUST = 68            # not 70
RSI_BEAR_EXHAUST = 32            # not 30
RSI_MID_LO = 44
RSI_MID_HI = 62
BODY_RECENT = 5
BODY_BASE = 12
BODY_SHRINK_RATIO = 0.62         # recent bodies << prior → exhaustion
WICK_REJECT_RATIO = 0.55         # rejection wick vs range on last bar
CONFIRM_BARS = 3                 # not 2-candle confirm


def _ema(values: list[float], period: int) -> list[float | None]:
    out: list[float | None] = [None] * len(values)
    if len(values) < period:
        return out
    k = 2 / (period + 1)
    seed = sum(values[:period]) / period
    out[period - 1] = seed
    for i in range(period, len(values)):
        out[i] = values[i] * k + out[i - 1] * (1 - k)
    return out


def _rsi(closes: list[float], period: int = 14) -> float | None:
    if len(closes) < period + 1:
        return None
    gains, losses = [], []
    for i in range(-period, 0):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    avg_g = sum(gains) / period
    avg_l = sum(losses) / period
    if avg_l == 0:
        return 100.0
    return 100.0 - (100.0 / (1.0 + avg_g / avg_l))


def _atr(candles: list[dict], period: int = ATR_PERIOD) -> float | None:
    if len(candles) < period + 1:
        return None
    trs: list[float] = []
    for i in range(1, len(candles)):
        h, l, pc = candles[i]["high"], candles[i]["low"], candles[i - 1]["close"]
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    window = trs[-period:]
    if len(window) < period:
        return None
    return sum(window) / period


def context_swing_levels(candles: list[dict]) -> tuple[list[float], list[float]]:
    """Swings with CONTEXT lookback (≠ Light/High swing_levels)."""
    lb = SWING_LOOKBACK
    highs, lows = [], []
    for i in range(lb, len(candles) - lb):
        h = candles[i]["high"]
        l = candles[i]["low"]
        if all(h >= candles[i + j]["high"] for j in range(-lb, lb + 1) if j != 0):
            highs.append(h)
        if all(l <= candles[i + j]["low"] for j in range(-lb, lb + 1) if j != 0):
            lows.append(l)
    return highs[-SWING_KEEP:], lows[-SWING_KEEP:]


def _structure_labels(sh: list[float], sl: list[float]) -> dict[str, str]:
    hl = lh = "n/a"
    if len(sl) >= 2:
        hl = f"HL {sl[-2]:.2f}->{sl[-1]:.2f}" if sl[-1] > sl[-2] else f"LL {sl[-2]:.2f}->{sl[-1]:.2f}"
    if len(sh) >= 2:
        lh = f"HH {sh[-2]:.2f}->{sh[-1]:.2f}" if sh[-1] > sh[-2] else f"LH {sh[-2]:.2f}->{sh[-1]:.2f}"
    return {"lows": hl, "highs": lh}


def _m5_structure_bias(sh: list[float], sl: list[float], closes: list[float]) -> str:
    """Primary bias from M5 HH/HL vs LH/LL + EMA9/21 (not H1 EMA20/50)."""
    bull_struct = len(sh) >= 2 and len(sl) >= 2 and sh[-1] > sh[-2] and sl[-1] > sl[-2]
    bear_struct = len(sh) >= 2 and len(sl) >= 2 and sh[-1] < sh[-2] and sl[-1] < sl[-2]

    e_fast = _ema(closes, EMA_FAST)
    e_slow = _ema(closes, EMA_SLOW)
    ema_bull = (
        e_fast[-1] is not None and e_slow[-1] is not None
        and e_fast[-1] > e_slow[-1] and closes[-1] > e_fast[-1]
    )
    ema_bear = (
        e_fast[-1] is not None and e_slow[-1] is not None
        and e_fast[-1] < e_slow[-1] and closes[-1] < e_fast[-1]
    )
    slope = closes[-1] - closes[-SLOPE_BARS] if len(closes) >= SLOPE_BARS else 0.0

    score = 0
    if bull_struct:
        score += 2
    if bear_struct:
        score -= 2
    if ema_bull:
        score += 1
    if ema_bear:
        score -= 1
    if slope > 0:
        score += 1
    elif slope < 0:
        score -= 1

    if score >= 2:
        return "BULLISH"
    if score <= -2:
        return "BEARISH"
    return "NEUTRAL"


def _impulse_extent_atr(candles: list[dict], bias: str, atr: float | None) -> float | None:
    """How far price has run from the impulse origin in ATR units."""
    if atr is None or atr <= 0 or len(candles) < 20:
        return None
    window = candles[-24:]
    if bias == "BULLISH":
        origin = min(c["low"] for c in window)
        return (candles[-1]["close"] - origin) / atr
    if bias == "BEARISH":
        origin = max(c["high"] for c in window)
        return (origin - candles[-1]["close"]) / atr
    mid = (max(c["high"] for c in window) + min(c["low"] for c in window)) / 2
    return abs(candles[-1]["close"] - mid) / atr


def _body_shrink(candles: list[dict]) -> float | None:
    if len(candles) < BODY_BASE + BODY_RECENT:
        return None
    recent = candles[-BODY_RECENT:]
    base = candles[-(BODY_BASE + BODY_RECENT):-BODY_RECENT]
    avg_r = sum(abs(c["close"] - c["open"]) for c in recent) / len(recent)
    avg_b = sum(abs(c["close"] - c["open"]) for c in base) / len(base)
    if avg_b <= 0:
        return None
    return avg_r / avg_b


def _rejection_wick(candle: dict, bias: str) -> bool:
    rng = candle["high"] - candle["low"]
    if rng <= 0:
        return False
    upper = candle["high"] - max(candle["open"], candle["close"])
    lower = min(candle["open"], candle["close"]) - candle["low"]
    if bias == "BULLISH":
        return upper / rng >= WICK_REJECT_RATIO
    if bias == "BEARISH":
        return lower / rng >= WICK_REJECT_RATIO
    return max(upper, lower) / rng >= WICK_REJECT_RATIO


def _failed_continuation(sh: list[float], sl: list[float], bias: str) -> bool:
    """Last swing failed to print HH (bull) or LL (bear)."""
    if bias == "BULLISH" and len(sh) >= 2:
        return sh[-1] <= sh[-2]
    if bias == "BEARISH" and len(sl) >= 2:
        return sl[-1] >= sl[-2]
    return False


def _momentum_confirm(candles: list[dict], bias: str) -> bool:
    if len(candles) < CONFIRM_BARS:
        return False
    last = candles[-CONFIRM_BARS:]
    if bias == "BULLISH":
        return all(c["close"] >= c["open"] for c in last)
    if bias == "BEARISH":
        return all(c["close"] <= c["open"] for c in last)
    return False


def _classify_vigencia(
    bias: str,
    impulse_atr: float | None,
    rsi_v: float | None,
    body_ratio: float | None,
    reject: bool,
    failed_swing: bool,
) -> tuple[str, list[str]]:
    """
    VIGENTE  — trend structure still pushing in bias direction
    AGOTANDO — extension / rejection / failed swing / RSI extreme
    TRANSICION — mixed or neutral bias
    """
    reasons: list[str] = []
    if bias == "NEUTRAL":
        return "TRANSICION", ["Estructura M5 mixta — sin bando claro"]

    exhaustion = 0
    vigor = 0

    if impulse_atr is not None:
        if impulse_atr >= IMPULSE_AGOTA_ATR:
            exhaustion += 2
            reasons.append(f"Impulso estirado {impulse_atr:.2f}×ATR (≥{IMPULSE_AGOTA_ATR})")
        elif impulse_atr <= IMPULSE_VIGENTE_MAX_ATR:
            vigor += 1
            reasons.append(f"Impulso sano {impulse_atr:.2f}×ATR (≤{IMPULSE_VIGENTE_MAX_ATR})")
        else:
            reasons.append(f"Impulso intermedio {impulse_atr:.2f}×ATR")

    if rsi_v is not None:
        if bias == "BULLISH" and rsi_v >= RSI_BULL_EXHAUST:
            exhaustion += 1
            reasons.append(f"RSI M5 {rsi_v:.1f} en zona de agotamiento alcista (≥{RSI_BULL_EXHAUST})")
        elif bias == "BEARISH" and rsi_v <= RSI_BEAR_EXHAUST:
            exhaustion += 1
            reasons.append(f"RSI M5 {rsi_v:.1f} en zona de agotamiento bajista (≤{RSI_BEAR_EXHAUST})")
        elif RSI_MID_LO <= rsi_v <= RSI_MID_HI:
            vigor += 1
            reasons.append(f"RSI M5 {rsi_v:.1f} en banda media de tendencia")
        else:
            reasons.append(f"RSI M5 {rsi_v:.1f}")

    if body_ratio is not None and body_ratio <= BODY_SHRINK_RATIO:
        exhaustion += 1
        reasons.append(f"Cuerpos recientes contraídos ({body_ratio:.2f}× base)")
    elif body_ratio is not None and body_ratio >= 0.9:
        vigor += 1
        reasons.append(f"Cuerpos mantienen energía ({body_ratio:.2f}× base)")

    if reject:
        exhaustion += 1
        reasons.append("Mecha de rechazo en extremo del impulso")

    if failed_swing:
        exhaustion += 2
        reasons.append("Último swing falló continuación (sin HH/LL nuevo)")

    if exhaustion >= 2 and exhaustion > vigor:
        return "AGOTANDO", reasons
    if vigor >= 1 and exhaustion <= 1:
        return "VIGENTE", reasons
    if exhaustion >= vigor and exhaustion >= 1:
        return "AGOTANDO", reasons
    return "VIGENTE", reasons or ["Estructura aún alineada con el bando"]


def analyze_m5_context(m5: list[dict], *, asset: str = "BTC") -> dict[str, Any]:
    closes = [c["close"] for c in m5]
    price = closes[-1]
    sh, sl = context_swing_levels(m5)
    labels = _structure_labels(sh, sl)
    bias = _m5_structure_bias(sh, sl, closes)
    atr = _atr(m5)
    rsi_v = _rsi(closes)
    impulse = _impulse_extent_atr(m5, bias, atr)
    body_ratio = _body_shrink(m5)
    reject = _rejection_wick(m5[-1], bias)
    failed = _failed_continuation(sh, sl, bias)
    confirm = _momentum_confirm(m5, bias)
    estado, reasons = _classify_vigencia(bias, impulse, rsi_v, body_ratio, reject, failed)

    e_fast = _ema(closes, EMA_FAST)
    e_slow = _ema(closes, EMA_SLOW)

    return {
        "asset": asset,
        "price": price,
        "bias_m5": bias,
        "estado": estado,  # VIGENTE | AGOTANDO | TRANSICION
        "structure": labels,
        "swing_highs": sh,
        "swing_lows": sl,
        "rsi_m5": rsi_v,
        "atr_m5": atr,
        "impulse_atr": impulse,
        "body_ratio": body_ratio,
        "rejection_wick": reject,
        "failed_swing": failed,
        "momentum_confirm": confirm,
        "ema_fast": e_fast[-1],
        "ema_slow": e_slow[-1],
        "reasons": reasons,
        "params_note": (
            f"lookback={SWING_LOOKBACK} swings={SWING_KEEP} "
            f"EMA{EMA_FAST}/{EMA_SLOW} ATR×{IMPULSE_VIGENTE_MAX_ATR}/{IMPULSE_AGOTA_ATR} "
            f"RSI exh {RSI_BEAR_EXHAUST}/{RSI_BULL_EXHAUST}"
        ),
    }


def write_context_report(
    path: Path,
    data: dict,
    ctx: dict[str, Any],
    *,
    price_decimals: int = 1,
) -> None:
    """Write compact MD: bias + vigencia (not a trade signal)."""
    fmt = f".{price_decimals}f"
    price = data.get("price", ctx["price"])
    rsi_s = f"{ctx['rsi_m5']:.1f}" if ctx.get("rsi_m5") is not None else "—"
    atr_s = f"{ctx['atr_m5']:{fmt}}" if ctx.get("atr_m5") is not None else "—"
    imp_s = f"{ctx['impulse_atr']:.2f}×ATR" if ctx.get("impulse_atr") is not None else "—"
    ema_f = f"{ctx['ema_fast']:{fmt}}" if ctx.get("ema_fast") is not None else "—"
    ema_s = f"{ctx['ema_slow']:{fmt}}" if ctx.get("ema_slow") is not None else "—"
    body_s = f"{ctx['body_ratio']:.2f}" if ctx.get("body_ratio") is not None else "—"

    estado = ctx["estado"]
    bias = ctx["bias_m5"]
    if estado == "VIGENTE" and bias in ("BULLISH", "BEARISH"):
        headline = f"Mercado **{bias}** — movimiento **VIGENTE**"
    elif estado == "AGOTANDO" and bias in ("BULLISH", "BEARISH"):
        headline = f"Mercado **{bias}** — movimiento **AGOTANDO** (cuidado con continuación ciega)"
    else:
        headline = "Mercado en **TRANSICIÓN** — sin bando M5 dominante"

    lines = [
        f"# {ctx['asset']} M5 CONTEXT — estructura / vigencia",
        "",
        f"**{headline}**",
        "",
        f"- Generado: `{data.get('generated', '')}` UTC",
        f"- Precio: `{price:{fmt}}`",
        f"- Bias estructura M5: **{bias}**",
        f"- Estado del impulso: **{estado}**",
        f"- Swings lows: `{ctx['structure']['lows']}`",
        f"- Swings highs: `{ctx['structure']['highs']}`",
        f"- EMA{EMA_FAST}/{EMA_SLOW}: `{ema_f}` / `{ema_s}`",
        f"- RSI M5: `{rsi_s}` · ATR: `{atr_s}` · Extensión: `{imp_s}`",
        f"- Ratio cuerpos: `{body_s}` · Rechazo mecha: `{ctx['rejection_wick']}` · "
        f"Swing fallido: `{ctx['failed_swing']}` · Confirm {CONFIRM_BARS} velas: `{ctx['momentum_confirm']}`",
        "",
        "## Lectura",
    ]
    for r in ctx.get("reasons") or []:
        lines.append(f"- {r}")

    lines += [
        "",
        "## Cómo usar",
        "- Esto **no es señal de entrada** (sin Entry/SL/TP).",
        "- **VIGENTE** → el bando estructural aún tiene recorrido; prioriza setups a favor.",
        "- **AGOTANDO** → el impulso se debilita; espera pullback/reversión o confirmación nueva.",
        "- **TRANSICION** → rango o mezcla HH/HL; no forzar dirección.",
        f"- Params CONTEXT (≠ Light/High): `{ctx.get('params_note', '')}`",
        "",
        f"*{ctx['asset']} M5 CONTEXT · solo lectura de estructura · no auto-ejecutar*",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
