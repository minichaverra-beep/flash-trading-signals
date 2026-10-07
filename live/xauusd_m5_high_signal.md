# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-07 13:22 UTC | NY 2026-10-07 09:22 | NY AM 08-10
> Precio **4096.64** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-07 13:20 UTC** · hace 2 min · fuente MT5 XAUUSDm (broker, M5/H1)
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
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~49%** — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BEARISH vs LONG -6; acuerdo MEDIA -2; patron LOSS similar -12; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4066-4124; 0.5=4095 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4184 | Bull si cierre arriba |
| PDL | 4104 | Bear si cierre abajo |
| 0.5 midpoint | 4144 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ✅ | Velas confirman |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 35 OK |
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
| Precio | **4096.64** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **4092.18** |
| ICT | 4109.66→4092.18 · Refinada 4109.7→4092.2 (FVG BULLISH edge) · Sweep swing_high @ 4122.2 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 08-10 |
| Plan | Entry **4092.18** · SL **4083.60** · TP **4109.34** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **71%** · ML **29.9%** · Confluencia **MEDIA** — 52% · Rules 83%; Neural gated 64% (medium); ML 30% veto suave; 2M5 OK; Break con fricción CRT |
| Historial ref | **xauusd-033** · 2026-10-06 19:27 NY · Entry **4168.50** · **BUENA** — precio cerca de Entry actual + 2M5 OK · (MÁS CERCA) · Δ Entry -76.32 pts (-1.831%) · precio→última 71.87 pts (1.724%) · precio→actual 4.46 pts (0.109%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | -4.46 pts (0.109%) |
| Dist. a SL | -13.04 pts (0.318%) |
| Dist. a TP | +12.70 pts (0.310%) |
| Riesgo (pts) | 8.58 |
| Winrate setup | ~49% — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BEARISH vs LONG -6; acuerdo MEDIA -2; patron LOSS similar -12; 83% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +2 (zona a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **80%** |
| Estado 2M5 | VÁLIDO LONG (2M5) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 71% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **bajo** · 0.56× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist -3.014 · never trigger |
| Watchtower KZ | NY AM 08-10 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4096.64** | Retest **4092.18–4112.69** |
| 2M5 LONG | Sí | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.30% de ref | contexto entry @ 4108.99 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 4092.18 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **4092.18** (limit retest o market al cierre 2ª vela) |
| SL | **4083.60** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4109.34** (1:2) |
| R:R | **1:2** · riesgo **8.58** pts |
| Invalidación | Cierre M5 < 4101.08 o breakdown < 4108.99 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4109.7→4092.2 (FVG BULLISH edge) · Sweep swing_high @ 4122.2 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 08-10 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 4144.06 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY AM 08-10 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4122.2 + reclaim |
| FVG alineados | 5 |
| Order blocks | 0 |
| Entrada refinada | **4092.18** (antes 4109.66 · FVG BULLISH edge) |
| Nota | Refinada 4109.7→4092.2 (FVG BULLISH edge) · Sweep swing_high @ 4122.2 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 08-10 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 4108.99 | **VÁLIDO** — [G][G] (zona a 0.30% · info, no gate) | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 08-10_

- [✅] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Las 4 ✅ → 2M5 OK.**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (49/26) |
| Swings | LL 4115->4066 | HH 4122->4124 |

---

## M5 detalle

- RSI M5/H1: 34.6 / 17.5
- Zona: soporte_debil @ 4109
- 2M5 LONG: SÍ | SHORT: NO

### 12 velas M5

- `12:25 O=4112.94 H=4113.07 L=4079.97 C=4080.62 [R]`
- `12:30 O=4080.55 H=4089.33 L=4073.31 C=4080.91 [G]`
- `12:35 O=4080.97 H=4086.81 L=4077.30 C=4077.30 [R]`
- `12:40 O=4077.26 H=4080.51 L=4071.72 C=4071.82 [R]`
- `12:45 O=4071.77 H=4078.11 L=4068.49 C=4074.62 [G]`
- `12:50 O=4074.55 H=4084.26 L=4066.30 C=4080.81 [G]`
- `12:55 O=4080.76 H=4089.17 L=4079.64 C=4087.34 [G]`
- `13:00 O=4087.44 H=4095.16 L=4086.67 C=4089.46 [G]`
- `13:05 O=4089.65 H=4092.18 L=4086.93 C=4088.55 [R]`
- `13:10 O=4088.60 H=4094.45 L=4086.76 C=4094.45 [G]`
- `13:15 O=4094.24 H=4097.54 L=4092.52 C=4096.49 [G]`
- `13:20 O=4096.44 H=4098.27 L=4094.91 C=4096.64 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | SÍ | Velas confirman |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 35 OK |
| Rango coherente | NO | rango bajista |
| DMI alineado | NO | -DI domina (49/26) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4097 · reloj NY AM 08-10 · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 52%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango bajista |
| Neural galería (gated) | 71.2% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 29.9% | 18% | grade C; conf=medium; → 35% |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.03 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 52% | 38% | blend 62/38 con acuerdo MEDIA 52% |
| **Probabilidad de éxito** | **52%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4184: -87.8 pts (-2.098%)
- **PDL** 4104: -7.1 pts (-0.172%)

### Premium / Discount 0.5

- Midpoint 0.5: **4144**
- Posición precio: **DISCOUNT** (precio 4097)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-07 11:00 O=4117 H=4123 L=4115 C=4122 [G]`
- `10-07 12:00 O=4121 H=4124 L=4066 C=4087 [R]`
- `10-07 13:00 O=4087 H=4098 L=4087 C=4097 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 4066-4124; 0.5=4095

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

- **Neural galería:** 71.2% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 71% | contra-bias, LOSS |

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
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 08-10**
- **Vol relativo:** 0.56× → banda **bajo** (vol×0.56 ≤ bajo 0.7)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -3.014 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-07 13:22 UTC*
