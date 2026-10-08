# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-07 18:52 UTC | NY 2026-10-07 14:52 | NY PM 14-16
> Precio **51235.5** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> **Modo:** BEARISH + BREAK — Bias CLI **BEARISH** — setup re-puntuado como SHORT
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **BEARISH** |
| Modo setup | **BREAK (breakout)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BEARISH** — setup re-puntuado como SHORT
- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Sin breakout de nivel detectado

---

## Veredicto: ENTRAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~55%** — histórico E1 BTC · SHORT en DISCOUNT -12 (chase Break); CLI BEARISH a favor +2; acuerdo MEDIA -2; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 51162-51280; 0.5=51222 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 51706 | Bull si cierre arriba |
| PDL | 51333 | Bear si cierre abajo |
| 0.5 midpoint | 51519 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 42 OK |
| Rango coherente | ✅ | Shorts E1 rechazo resistencia (premium)  |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓ | RSI 41.7 (SHORT: neutral) | sin calibrar | n/d | ponderada |
| Zona premium/discount | ✗ | DISCOUNT (en contra) | sin calibrar | n/d | ponderada |
| 2 velas M5 confirman | ✗ | no | sin calibrar | n/d | ponderada |
| Rango CRT coherente | ✓ | Shorts E1 rechazo resistencia (premium)  | sin calibrar | n/d | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Bajista | — | constante en histórico | info |
| R:R mínimo 1:2 | · | 1:2 | — | constante en histórico | info |

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

### Plan (ENTRAR)

- Dirección: **Short** @ 51236
- SL estructura: **51389** | TP: **50928** (R:R 1:2)
- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos
- BE en 1:1 | Invalidación: fuera zona / CRT invalid

### Red flags

- Ninguno detectado

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **51235.5** |
| Veredicto | **Entrar** (SHORT) |
| Entrada óptima | **51248.5** |
| ICT | 51235.5→51248.5 · Refinada 51235.5→51248.5 (FVG BEARISH edge) · Sweep swing_high @ 51258.5 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-16 |
| Plan | Entry **51248.5** · SL **51308.5** · TP **51128.5** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **72%** · ML **100.0%** · Confluencia **MEDIA** — 55% · Rules 83%; Neural gated 64% (medium); ML 100% (high); 2M5 no listo; Break vs DISCOUNT (chase) |
| Historial ref | **us30-061** · 2026-10-07 12:03 NY · Entry **51150.4** · **BUENA** — precio cerca de Entry actual + zona OK · (MÁS CERCA) · Δ Entry +98.1 pts (+0.192%) · precio→última 85.1 pts (0.166%) · precio→actual 13.0 pts (0.025%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +13.0 pts (0.025%) |
| Dist. a SL | +73.0 pts (0.142%) |
| Dist. a TP | -107.0 pts (0.209%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~55% — histórico E1 BTC · SHORT en DISCOUNT -12 (chase Break); CLI BEARISH a favor +2; acuerdo MEDIA -2; 83% reglas |
| Zona PD vs dirección | SHORT en DISCOUNT -12 (chase Break) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.27× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist -25.18 · never trigger |
| Watchtower KZ | NY PM 14-16 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **51235.5** | Retest **51177.4–51248.5** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.02% de ref | contexto entry @ 51223.5 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 51248.5 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **51248.5** (limit retest o market al cierre 2ª vela) |
| SL | **51308.5** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **51128.5** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 51295.5 o breakout > 51223.5 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 51235.5→51248.5 (FVG BEARISH edge) · Sweep swing_high @ 51258.5 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-16 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ⚠️ |
| 0.5 midpoint | 51519.4 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY PM 14-16 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 51258.5 + reclaim |
| FVG alineados | 1 |
| Order blocks | 5 |
| Entrada refinada | **51248.5** (antes 51235.5 · FVG BEARISH edge) |
| Nota | Refinada 51235.5→51248.5 (FVG BEARISH edge) · Sweep swing_high @ 51258.5 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-16 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 51223.5 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY PM 14-16_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (60/43) | **SHORT** |
| CRT PD / Premium-Discount | BEARISH · DISCOUNT | **LONG** |
| Estructura swings M5 | HL 51212->51224 · HH 51256->51258 | **LONG** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (60/43) |
| Swings | HL 51212->51224 | HH 51256->51258 |

---

## M5 detalle

- RSI M5/H1: 41.7 / 33.6
- Zona: soporte_debil @ 51224
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `17:55 O=51231.5 H=51237.5 L=51225.5 C=51234.5 [G]`
- `18:00 O=51233.5 H=51245.5 L=51211.5 C=51240.5 [G]`
- `18:05 O=51241.5 H=51256.5 L=51223.5 C=51226.5 [R]`
- `18:10 O=51225.5 H=51239.5 L=51221.5 C=51238.5 [G]`
- `18:15 O=51239.5 H=51252.5 L=51232.5 C=51249.5 [G]`
- `18:20 O=51248.5 H=51248.5 L=51231.5 C=51240.5 [R]`
- `18:25 O=51241.5 H=51258.5 L=51231.5 C=51243.5 [G]`
- `18:30 O=51244.5 H=51256.5 L=51235.5 C=51246.5 [G]`
- `18:35 O=51247.5 H=51257.5 L=51223.5 C=51234.5 [R]`
- `18:40 O=51233.5 H=51251.5 L=51223.5 C=51235.5 [G]`
- `18:45 O=51234.5 H=51239.5 L=51226.5 C=51232.5 [R]`
- `18:50 O=51231.5 H=51240.5 L=51223.5 C=51235.5 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 42 OK |
| Rango coherente | SÍ | Shorts E1 rechazo resistencia (premium)  |
| DMI alineado | SÍ | -DI domina (60/43) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 51236 · reloj NY PM 14-16 · CRT PD=BEARISH · H1 bias **NEUTRAL**
- **Setup:** ENTRAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — score combinado 58%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | Shorts E1 rechazo resistencia (premium)  |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 100.0% | 18% | grade A+; conf=high; → 100% |
| Penalización ubicación | ×0.72 | — | Break bajista en DISCOUNT (chase) |
| Acuerdo entre capas | 55% | 38% | blend 62/38 con acuerdo MEDIA 55% |
| **Probabilidad de éxito** | **58%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 51706: -470.0 pts (-0.909%)
- **PDL** 51333: -97.9 pts (-0.191%)

### Premium / Discount 0.5

- Midpoint 0.5: **51519**
- Posición precio: **DISCOUNT** (precio 51236)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-07 16:00 O=51142 H=51224 L=51108 C=51182 [G]`
- `10-07 17:00 O=51180 H=51280 L=51162 C=51234 [G]`
- `10-07 18:00 O=51234 H=51258 L=51212 C=51236 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 51162-51280; 0.5=51222

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

**Acuerdo Rules/Neural:** ALIGNED

- ML y Neural apuntan misma dirección de confianza

- **Neural galería:** 71.8% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | Esperar setup A+ galeria WIN | — | 72% | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** SHORT @ zona soporte_debil 51224 (precio actual 51236)
- **SL estructural:** 51389 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 50928 | **BE:** mover a BE en 1:1
- **Invalidación:** cierre M5 fuera zona / CRT invalid / fakeout contra dirección
- **Confluencias Notion sugeridas:** Continuación/Breakout E1, Zona débil morada, CRT alineado

### Pre-trade checklist (8 ítems)

| # | Ítem | OK |
|---|------|----|
| 1 | Bias H1 alineado | ❌ |
| 2 | 2 velas M5 confirmación | ❌ |
| 3 | Rules E1 ≥63% | ✅ |
| 4 | Extendidas ≥70% | ✅ |
| 5 | Sin fakeout contra | ✅ |
| 6 | SL ~$9 definido | ✅ |
| 7 | R:R 1:2 | ✅ |
| 8 | Entry/SL/TP definidos | ❌ |

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY PM 14-16**
- **Vol relativo:** 0.27× → banda **muy_bajo** (vol×0.27 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -25.18 · soft-filter vs setup: **alineado**
- **Strategy A (última H4):** sin cruce A (EMA200 filter)
- Strategy B (zero-line): variante documentada; no dispara E1 sola.
- Backtest WR/PF: **PENDING** (ver TRADING_QUANT_MACD_E1_BACKTEST.md).

## I) Cursor — prompt ADVANCED

Usar con `@docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md` sección **Modo Advanced**.

```
Análisis E1 CRT ADVANCED — US30 M5 HIGH mode.
Lee TODAS las secciones A–H de live/us30_m5_high_signal.md.
NO acortar. Responde estructurado en español con síntesis ejecutiva,
scorecard, CRT deep dive, E2 (si aplica), cruce ML×Neural, galería,
plan (si ENTRAR), red flags y guardas psicológicas.
Confirmar TradingView antes de ejecutar. 2 SL = límite de riesgo diario.
```


---

## Cursor HIGH response
Modo **ADVANCED** — usar prompt completo en `docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md` §Modo Advanced.
Leer Categories (incl. Entrada óptima + Confluencia + Advanced) y secciones A–I. **NO acortar** vs light mode.

## Salidas

- **Reporte:** `live/us30_m5_high_signal.md`
- **Chart:** **Preview en navegador**


---
*high signal | 2026-10-07 18:52 UTC*
