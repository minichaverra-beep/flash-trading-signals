# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-02 16:11 UTC | NY 2026-10-02 12:11 | FUERA_NY (Lunch)
> Precio **4134.43** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-02 16:10 UTC** · hace 1 min · fuente MT5 XAUUSDm (broker, M5/H1)
> **Modo:** BULLISH + BREAK — Bias CLI **BULLISH** — setup re-puntuado como LONG
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **BULLISH** |
| Modo setup | **BREAK (breakout)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BULLISH** — setup re-puntuado como LONG
- ⚠ H1 bajista vs bias forzado — confirmar en TV antes de entrar
- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Sin breakout de nivel detectado

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~48%** — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patron LOSS similar -12; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4125-4160; 0.5=4143 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4193 | Bull si cierre arriba |
| PDL | 4139 | Bear si cierre abajo |
| 0.5 midpoint | 4166 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 33 OK |
| Rango coherente | ❌ | rango bajista |

### Turtle Soup E2

Score **0/6** | Operable: **NO**
_Modo BREAK: breakout de nivel — E2/reversión despriorizada, NO operable_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | NO | Sweep liquidez |
| 3. Reclaim agresivo | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | NO | Cerca nivel barrido |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Red flags

- Precio < PDL — no long contra rango bajista CRT

### Galería (cross-ref)

- Patrón perdedor similar: contra bias (BTC-01-06-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4134.43** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **4131.64** |
| ICT | 4134.28→4131.64 · Refinada 4134.3→4131.6 (FVG BULLISH edge) · Sweep PDH @ 4192.9 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |
| Plan | Entry **4131.64** · SL **4125.50** · TP **4143.91** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **74%** · ML **6.8%** · Confluencia **BAJA** — 38% · Rules 66%; Neural gated 65% (medium); ML 7% veto suave; 2M5 no listo; Break con fricción CRT |
| Historial ref | **xauusd-024** · 2026-10-02 12:10 NY · Entry **4131.64** · **BUENA** — precio cerca de última Entry + zona OK · (MISMA ZONA) · Δ Entry +0.00 pts (+0.000%) · precio→última 2.79 pts (0.068%) · precio→actual 2.79 pts (0.068%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | -2.79 pts (0.068%) |
| Dist. a SL | -8.93 pts (0.216%) |
| Dist. a TP | +9.48 pts (0.229%) |
| Riesgo (pts) | 6.13 |
| Winrate setup | ~48% — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patron LOSS similar -12; 66% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +2 (zona a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 74% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.15× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist 0.5512 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4134.43** | Retest **4131.64–4137.15** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.02% de ref | contexto entry @ 4133.43 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 4131.64 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **4131.64** (limit retest o market al cierre 2ª vela) |
| SL | **4125.50** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4143.91** (1:2) |
| R:R | **1:2** · riesgo **6.13** pts |
| Invalidación | Cierre M5 < 4128.15 o breakdown < 4133.43 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4134.3→4131.6 (FVG BULLISH edge) · Sweep PDH @ 4192.9 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 4166.00 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDH @ 4192.9 + reclaim |
| FVG alineados | 4 |
| Order blocks | 4 |
| Entrada refinada | **4131.64** (antes 4134.28 · FVG BULLISH edge) |
| Nota | Refinada 4134.3→4131.6 (FVG BULLISH edge) · Sweep PDH @ 4192.9 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 4133.43 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (35/18) |
| Swings | LL 4133->4125 | LH 4197->4148 |

---

## M5 detalle

- RSI M5/H1: 33.4 / 40.9
- Zona: soporte_debil @ 4133
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `15:15 O=4145.35 H=4147.09 L=4139.12 C=4142.61 [R]`
- `15:20 O=4142.73 H=4144.93 L=4136.80 C=4136.88 [R]`
- `15:25 O=4137.25 H=4144.83 L=4133.43 C=4142.48 [G]`
- `15:30 O=4142.55 H=4147.56 L=4139.40 C=4146.55 [G]`
- `15:35 O=4146.50 H=4147.40 L=4138.56 C=4139.17 [R]`
- `15:40 O=4139.09 H=4141.20 L=4134.03 C=4134.85 [R]`
- `15:45 O=4134.88 H=4138.38 L=4131.31 C=4135.32 [G]`
- `15:50 O=4135.21 H=4137.16 L=4128.38 C=4130.15 [R]`
- `15:55 O=4130.10 H=4131.71 L=4125.10 C=4127.13 [R]`
- `16:00 O=4127.44 H=4131.64 L=4125.57 C=4129.94 [G]`
- `16:05 O=4129.99 H=4135.46 L=4127.48 C=4134.62 [G]`
- `16:10 O=4134.56 H=4135.27 L=4132.86 C=4134.43 [R]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 33 OK |
| Rango coherente | NO | rango bajista |
| DMI alineado | NO | -DI domina (35/18) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4134 · reloj FUERA_NY (Lunch) · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 41%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango bajista |
| Neural galería (gated) | 73.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 65% |
| ML tabular (gated) | 6.8% | 18% | grade C; conf=high; → 7% |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.03 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 38% | 38% | blend 62/38 con acuerdo BAJA 38% |
| **Probabilidad de éxito** | **41%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4193: -58.5 pts (-1.395%)
- **PDL** 4139: -4.6 pts (-0.112%)

### Premium / Discount 0.5

- Midpoint 0.5: **4166**
- Posición precio: **DISCOUNT** (precio 4134)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-02 14:00 O=4191 H=4197 L=4155 C=4159 [R]`
- `10-02 15:00 O=4159 H=4160 L=4125 C=4127 [R]`
- `10-02 16:00 O=4127 H=4135 L=4126 C=4134 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 4125-4160; 0.5=4143

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar |  |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo | **→** |
| Fakeout PDH | NO long E1 |  |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** CONFLICT

- Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual fuerte pero features ML desfavorables; priorizar Rules % + CRT

- **Neural galería:** 73.8% WIN (grade B, conf medium) · gate×0.65 → 65% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 74% | contra-bias, LOSS |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)
- ⚠ Tensión ML/Neural — no entrar por galería sola

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY (Lunch)**
- **Vol relativo:** 0.15× → banda **muy_bajo** (vol×0.15 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 0.5512 · soft-filter vs setup: **alineado**
- **Strategy A (última H4):** sin cruce A (EMA200 filter)
- Strategy B (zero-line): variante documentada; no dispara E1 sola.
- Backtest WR/PF: **PENDING** (ver TRADING_QUANT_MACD_E1_BACKTEST.md).

## I) Cursor — prompt ADVANCED

Usar con `@docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` sección **Modo Advanced**.

```
Análisis E1 CRT ADVANCED — BTC M5 HIGH mode.
Lee TODAS las secciones A–H de live/btc_m5_high_signal.md.
NO acortar. Responde estructurado en español con síntesis ejecutiva,
scorecard, CRT deep dive, E2 (si aplica), cruce ML×Neural, galería,
plan (si ENTRAR), red flags y guardas psicológicas.
Confirmar TradingView antes de ejecutar. 2 SL = límite de riesgo diario.
```


---

## Cursor HIGH response
Modo **ADVANCED** — usar prompt completo en `docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` §Modo Advanced.
Leer Categories (incl. Entrada óptima + Confluencia + Advanced) y secciones A–I. **NO acortar** vs light mode.

## Salidas

- **Reporte:** `live/xauusd_m5_high_signal.md`
- **Chart:** **Preview en navegador**


---
*high signal | 2026-10-02 16:11 UTC*
