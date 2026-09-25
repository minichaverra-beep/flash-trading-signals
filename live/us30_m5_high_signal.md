# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-25 16:47 UTC | NY 2026-09-25 12:47 | FUERA_NY (Lunch)
> Precio **52119.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~82%** — patrón ganador similar · histórico E1 BTC

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 51998-52195; 0.5=52096 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 51861 | Bull si cierre arriba |
| PDL | 51479 | Bear si cierre abajo |
| 0.5 midpoint | 51670 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 68 OK |
| Rango coherente | ❌ | rango alcista |

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

- Precio > PDH — no short contra rango alcista CRT
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **52119.0** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **52149.4** |
| Entry usuario | **51753.0 (CLI · past)** |
| ICT | Base 52149.4 (zona base) · Sweep PDH @ 51861.0 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |
| Plan | Entry **51753.0** · SL **52016.6** · TP **51225.8** · plan usuario |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **72%** · ML **0.0%** · Confluencia **BAJA** — 27% · Rules 66%; Neural gated 64% (medium); ML 0% veto suave; 2M5 no listo; Break con fricción CRT |
| Historial ref | **us30-033** · 2026-09-24 11:25 NY · Entry **51716.0** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry +433.4 pts (+0.838%) · precio→última 403.0 pts (0.779%) · precio→actual 30.4 pts (0.058%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entrada óptima | +30.4 pts (0.058%) |
| Dist. a Entry usuario | -366.0 pts (0.702%) |
| Dist. a SL | -102.4 pts (0.197%) |
| Dist. a TP | -893.2 pts (1.714%) |
| Riesgo (pts) | 263.6 |
| SL/TP | estructura pasada (past) |
| Winrate setup | ~82% — patrón ganador similar · histórico E1 BTC |
| Score Rules extendido | **70%** |
| Estado 2M5 | Falta 2M5 — ESPERAR |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.00× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist 39.39 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BULLISH** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **52119.0** | Retest **52148.0–52195.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.15% de ref | contexto entry @ 52195.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT (Entry usuario · SL/TP past)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Entry usuario CLI @ 51753.0 (SHORT) · SL/TP desde estructura post-entry |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entrada óptima | **52149.4** (sistema · limit retest o market al cierre 2ª vela) |
| Entry usuario | **51753.0** (CLI -Entry / --entry) |
| SL | **52016.6** (estructura pasada (PDH)) · plan Entry usuario · SL cuenta ~$9 (ajustar lotaje) |
| TP | **51225.8** (1:2 desde SL past) · plan Entry usuario |
| R:R | **1:2** · riesgo **263.6** pts |
| SL/TP nota | SL/TP desde estructura pasada (SL=PDH @ 51861.0; TP=1:2 desde SL estructural) |
| Invalidación | Cierre M5 > 52016.6 o breakout sin rechazo (Entry usuario 51753.0; SL past=PDH) |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 52149.4 (zona base) · Sweep PDH @ 51861.0 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 51670.0 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDH @ 51861.0 + reclaim |
| FVG alineados | 0 |
| Order blocks | 1 |
| Entrada | **52149.4** (zona base · sin cambio) |
| Nota | Base 52149.4 (zona base) · Sweep PDH @ 51861.0 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 52195.0 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | +DI domina (428/204) | **LONG** |
| CRT PD / Premium-Discount | BULLISH · PREMIUM | **LONG** |
| Estructura swings M5 | HL 51787->51808 · HH 51936->52195 | **LONG** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BULLISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (428/204) |
| Swings | HL 51787->51808 | HH 51936->52195 |

---

## M5 detalle

- RSI M5/H1: 67.7 / 75.8
- Zona: resistencia_debil @ 52195
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `15:45 O=51827.0 H=51864.0 L=51808.0 C=51855.0 [G]`
- `15:50 O=51858.0 H=51913.0 L=51819.0 C=51896.0 [G]`
- `15:55 O=51896.0 H=52011.0 L=51893.0 C=52009.0 [G]`
- `16:00 O=52008.0 H=52138.0 L=51998.0 C=52134.0 [G]`
- `16:05 O=52128.0 H=52175.0 L=52116.0 C=52162.0 [G]`
- `16:10 O=52167.0 H=52195.0 L=52134.0 C=52154.0 [R]`
- `16:15 O=52151.0 H=52174.0 L=52102.0 C=52130.0 [R]`
- `16:20 O=52133.0 H=52136.0 L=52084.0 C=52101.0 [R]`
- `16:25 O=52104.0 H=52171.0 L=52098.0 C=52166.0 [G]`
- `16:30 O=52169.0 H=52184.0 L=52071.0 C=52090.0 [R]`
- `16:35 O=52093.0 H=52147.0 L=52093.0 C=52119.0 [G]`
- `16:37 O=52119.0 H=52119.0 L=52119.0 C=52119.0 [G]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 68 OK |
| Rango coherente | NO | rango alcista |
| DMI alineado | NO | +DI domina (428/204) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 52119 · reloj FUERA_NY (Lunch) · CRT PD=BULLISH · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 45%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango alcista |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 0.0% | 18% | grade C; conf=high; → 0% |
| **Score combinado** | **45%** | 100% | pesos renormalizados |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 51861: +258.0 pts (+0.497%)
- **PDL** 51479: +640.0 pts (+1.243%)

### Premium / Discount 0.5

- Midpoint 0.5: **51670**
- Posición precio: **PREMIUM** (precio 52119)
- Lectura PD: **BULLISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-25 15:00 O=51841 H=52011 L=51804 C=52009 [G]`
- `09-25 16:00 O=52008 H=52195 L=51998 C=52119 [G]`
- `09-25 16:37 O=52119 H=52119 L=52119 C=52119 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 51998-52195; 0.5=52096

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar |  |
| Cierre > PDH | Sesgo alcista — long pullback | **→** |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 |  |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** CONFLICT

- Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual fuerte pero features ML desfavorables; priorizar Rules % + CRT

- **Neural galería:** 71.8% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 72% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY (Lunch)**
- **Vol relativo:** 0.00× → banda **muy_bajo** (vol×0.00 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 39.39 · soft-filter vs setup: **en contra**
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
*high signal | 2026-09-25 16:47 UTC*
