# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-01 23:26 UTC | NY 2026-10-01 19:26 | FUERA_NY (Asia)
> Precio **84722.8** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **AUTO** |
| Modo setup | **AUTO** |

---

## Veredicto: ENTRAR

**E1/E2:** E1 primario
**Tendencia:** Alcista
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~56%** — histórico E1 BTC · LONG en PREMIUM -7 (vs zona); H1 BULLISH a favor +4; acuerdo BAJA -8; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 84504-84769; 0.5=84637 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 85618 | Bull si cierre arriba |
| PDL | 82904 | Bear si cierre abajo |
| 0.5 midpoint | 84261 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 52 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF |

### Turtle Soup E2

Score **0/6** | Operable: **NO**
_E2 max 10%; PF E1=4.77; PROHIBIDO eval (TRADING_VISUAL SS7)_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | NO | Sweep liquidez |
| 3. Reclaim agresivo | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | NO | Cerca nivel barrido |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Plan (ENTRAR)

- Dirección: **Long** @ 84723
- SL estructura: **84663** | TP: **84843** (R:R 1:2)
- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos
- BE en 1:1 | Invalidación: fuera zona / CRT invalid

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **84722.8** |
| Veredicto | **Entrar** (LONG) |
| Entrada óptima | **84671.1** |
| ICT | 84722.8→84671.1 · Refinada 84722.8→84671.1 (FVG BULLISH edge) · Sweep swing_high @ 84664.2 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |
| Plan | Entry **84671.1** · SL **84611.1** · TP **84791.1** |
| E2 / Break | Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **65%** · ML **60.7%** · Confluencia **BAJA** — 46% · Rules 83%; Neural gated 60% (medium); ML 61% zona media; 2M5 no listo; Setup auto con dirección |
| Historial ref | **btc-035** · 2026-10-01 16:16 NY · Entry **84792.7** · **BUENA** — precio cerca de última Entry + zona OK + bando alineado · (MISMA ZONA) · Δ Entry -121.6 pts (-0.143%) · precio→última 69.9 pts (0.082%) · precio→actual 51.6 pts (0.061%) |
| Bando usado (lado asumido) | **AUTO** |
| Bando mercado (H1) | **BULLISH** |
| R:R | 1:2 |
| Dist. a Entry | -51.6 pts (0.061%) |
| Dist. a SL | -111.6 pts (0.132%) |
| Dist. a TP | +68.4 pts (0.081%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~56% — histórico E1 BTC · LONG en PREMIUM -7 (vs zona); H1 BULLISH a favor +4; acuerdo BAJA -8; 83% reglas |
| Zona PD vs dirección | LONG en PREMIUM -7 (vs zona) |
| Bias vs dirección | H1 BULLISH a favor +4 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BULLISH** · CLI **AUTO** |
| Calidad break/reverse | AUTO |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.24× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **OK** · Hist 147.3 · never trigger |
| Watchtower KZ | FUERA_NY (Asia) · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **AUTO** + **AUTO** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **84722.8** | Retest **84671.1–84835.2** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.04% de ref | contexto entry @ 84758.9 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 84671.1 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **84671.1** (limit retest o market al cierre 2ª vela) |
| SL | **84611.1** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **84791.1** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 < 84662.8 o breakdown < 84758.9 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 84722.8→84671.1 (FVG BULLISH edge) · Sweep swing_high @ 84664.2 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ⚠️ |
| 0.5 midpoint | 84261.0 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Asia) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 84664.2 + reclaim |
| FVG alineados | 4 |
| Order blocks | 5 |
| Entrada refinada | **84671.1** (antes 84722.8 · FVG BULLISH edge) |
| Nota | Refinada 84722.8→84671.1 (FVG BULLISH edge) · Sweep swing_high @ 84664.2 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en resistencia_debil @ 84758.9 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Asia)_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | NEUTRAL | Momentum mixto |
| Swings | HL 84465->84585 | LH 84764->84759 |

---

## M5 detalle

- RSI M5/H1: 51.8 / 73.4
- Zona: resistencia_debil @ 84759
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `22:30 O=84663.3 H=84695.5 L=84618.4 C=84645.9 [R]`
- `22:35 O=84645.9 H=84764.1 L=84645.6 C=84730.2 [G]`
- `22:40 O=84731.4 H=84739.4 L=84645.3 C=84650.3 [R]`
- `22:45 O=84650.2 H=84656.7 L=84602.7 C=84618.6 [R]`
- `22:50 O=84619.3 H=84734.9 L=84585.3 C=84724.6 [G]`
- `22:55 O=84724.1 H=84758.9 L=84688.4 C=84707.3 [R]`
- `23:00 O=84713.4 H=84713.4 L=84638.0 C=84691.4 [R]`
- `23:05 O=84691.5 H=84691.5 L=84646.2 C=84660.5 [R]`
- `23:10 O=84660.4 H=84671.1 L=84624.5 C=84638.8 [R]`
- `23:15 O=84638.8 H=84738.8 L=84602.1 C=84738.2 [G]`
- `23:20 O=84738.1 H=84740.9 L=84688.7 C=84719.2 [R]`
- `23:25 O=84719.2 H=84729.3 L=84719.2 C=84722.8 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 52 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | NO | premium — no long E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 84723 · reloj FUERA_NY (Asia) · CRT PD=NEUTRAL · H1 bias **BULLISH**
- **Setup:** ENTRAR LONG · dirección **LONG** · modo **AUTO** · reglas E1 5/6 (83%)
- **Bando:** AUTO — mercado H1 **BULLISH** guía dirección
- **Veredicto integrado:** ENTRAR — score combinado 57%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF |
| Neural galería (gated) | 65.0% | 25% | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 60.7% | 18% | grade B; conf=low; → 55% |
| Penalización ubicación | ×0.88 | — | LONG en PREMIUM |
| Acuerdo entre capas | 46% | 38% | blend 62/38 con acuerdo BAJA 46% |
| **Probabilidad de éxito** | **57%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 85618: -895.6 pts (-1.046%)
- **PDL** 82904: +1819.0 pts (+2.194%)

### Premium / Discount 0.5

- Midpoint 0.5: **84261**
- Posición precio: **PREMIUM** (precio 84723)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-01 21:00 O=84601 H=84664 L=84465 C=84506 [R]`
- `10-01 22:00 O=84504 H=84769 L=84504 C=84707 [G]`
- `10-01 23:00 O=84713 H=84741 L=84602 C=84723 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 84504-84769; 0.5=84637

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar | **→** |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 |  |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 65.0% WIN (grade B, conf medium) · gate×0.65 → 60% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | Esperar setup A+ galeria WIN | — | 65% | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** LONG @ zona resistencia_debil 84759 (precio actual 84723)
- **SL estructural:** 84663 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 84843 | **BE:** mover a BE en 1:1
- **Invalidación:** cierre M5 fuera zona / CRT invalid / fakeout contra dirección
- **Confluencias Notion sugeridas:** Continuación/Breakout E1, Zona débil morada, CRT alineado

### Pre-trade checklist (8 ítems)

| # | Ítem | OK |
|---|------|----|
| 1 | Bias H1 alineado | ✅ |
| 2 | 2 velas M5 confirmación | ❌ |
| 3 | Rules E1 ≥63% | ✅ |
| 4 | Extendidas ≥70% | ✅ |
| 5 | Sin fakeout contra | ✅ |
| 6 | SL ~$9 definido | ✅ |
| 7 | R:R 1:2 | ✅ |
| 8 | Entry/SL/TP definidos | ✅ |

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_BTC_E1` — alto 1.7 / extremo 2.6 / bajo 0.75 / muy bajo 0.45 / período 84 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY (Asia)**
- **Vol relativo:** 0.24× → banda **muy_bajo** (vol×0.24 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 147.3 · soft-filter vs setup: **alineado**
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

- **Reporte:** `live/btc_m5_high_signal.md`
- **Chart:** **Preview en navegador**


---
*high signal | 2026-10-01 23:26 UTC*
