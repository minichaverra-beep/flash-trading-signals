# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-10 16:14 UTC | NY 2026-10-10 12:14 | FUERA_NY (Lunch)
> Precio **82947.8** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- ⚠ H1 alcista vs bias forzado — confirmar en TV antes de entrar
- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Sin breakout de nivel detectado

---

## Veredicto: ENTRAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **90%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~57%** — calibrado walk-forward BTC E1 · 80%: 52–62% · n=2097 (n_eff 755) · EV +0.65R

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 82864-82992; 0.5=82928 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 83456 | Bull si cierre arriba |
| PDL | 81535 | Bear si cierre abajo |
| 0.5 midpoint | 82496 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 50 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: impacto medido walk-forward n=2097 (n_eff 755)._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓ | RSI 49.6 (SHORT: neutral) | +3.2 pts | esta zona 45% (n=528) | ponderada |
| Zona premium/discount | ✓✓ | PREMIUM (a favor) | +7.3 pts | a favor 55% / en contra 45% | ponderada |
| 2 velas M5 confirman | ~ | no | +0.2 pts | sí 43% / no 47% | ponderada |
| Rango CRT coherente | ~ | No forzar; esperar pending CRT HTF | Mod | +0.2 pts | sí 46% / no 45% | ponderada |
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

- Dirección: **Short** @ 82948
- SL estructura: **83140** | TP: **82562** (R:R 1:2)
- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos
- BE en 1:1 | Invalidación: fuera zona / CRT invalid

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **82947.8** |
| Veredicto | **Entrar** (SHORT) |
| Entrada óptima | **82950.3** |
| ICT | 82953.8→82950.3 · Refinada 82953.8→82950.3 (OB BEARISH edge) · Sweep swing_high @ 82992.3 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |
| Plan | Entry **82950.3** · SL **83010.3** · TP **82830.3** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **65%** · ML **37.3%** · Confluencia **BAJA** — 44% · Rules 83%; Neural gated 60% (medium); ML 37% veto suave; 2M5 no listo; Break operable |
| Historial ref | **btc-092** · 2026-10-10 02:05 NY · Entry **82701.1** · **BUENA** — precio cerca de Entry actual + zona OK · (MÁS CERCA) · Δ Entry +249.2 pts (+0.301%) · precio→última 246.7 pts (0.298%) · precio→actual 2.6 pts (0.003%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BULLISH** |
| R:R | 1:2 |
| Dist. a Entry | +2.6 pts (0.003%) |
| Dist. a SL | +62.6 pts (0.075%) |
| Dist. a TP | -117.4 pts (0.142%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~57% — calibrado walk-forward BTC E1 · 80%: 52–62% · n=2097 (n_eff 755) · EV +0.65R |
| Zona PD vs dirección | SHORT en PREMIUM +2 (zona a favor) |
| Bias vs dirección | H1 BULLISH vs SHORT -6 |
| Score Rules extendido | **90%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BULLISH** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **normal** · 0.90× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **en contra** · Hist 169.3 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **82947.8** | Retest **82899.9–82974.5** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.03% de ref | contexto entry @ 82974.5 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest OB BEARISH edge @ 82950.3 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **82950.3** (limit retest o market al cierre 2ª vela) |
| SL | **83010.3** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **82830.3** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 83013.8 o breakout > 82974.5 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 82953.8→82950.3 (OB BEARISH edge) · Sweep swing_high @ 82992.3 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 82495.5 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 82992.3 + reclaim |
| FVG alineados | 2 |
| Order blocks | 2 |
| Entrada refinada | **82950.3** (antes 82953.8 · OB BEARISH edge) |
| Nota | Refinada 82953.8→82950.3 (OB BEARISH edge) · Sweep swing_high @ 82992.3 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 82974.5 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | NEUTRAL | Momentum mixto |
| Swings | HL 82695->82864 | HH 82975->82992 |

---

## M5 detalle

- RSI M5/H1: 49.6 / 74.4
- Zona: resistencia_debil @ 82975
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `15:15 O=82892.7 H=82910.5 L=82877.2 C=82886.4 [R]`
- `15:20 O=82887.9 H=82901.1 L=82863.9 C=82880.0 [R]`
- `15:25 O=82881.0 H=82911.1 L=82879.8 C=82906.7 [G]`
- `15:30 O=82905.1 H=82959.1 L=82898.6 C=82939.8 [G]`
- `15:35 O=82939.8 H=82957.7 L=82935.8 C=82954.1 [G]`
- `15:40 O=82953.5 H=82965.0 L=82938.4 C=82953.4 [R]`
- `15:45 O=82953.5 H=82992.3 L=82950.3 C=82970.9 [G]`
- `15:50 O=82970.2 H=82978.9 L=82923.7 C=82923.8 [R]`
- `15:55 O=82923.8 H=82967.0 L=82906.1 C=82963.8 [G]`
- `16:00 O=82966.3 H=82973.3 L=82944.7 C=82970.8 [G]`
- `16:05 O=82969.8 H=82973.3 L=82883.2 C=82917.5 [R]`
- `16:10 O=82921.2 H=82963.3 L=82911.1 C=82947.8 [G]`

---

## Score reglas extendidas (90%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 50 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 82948 · reloj FUERA_NY (Lunch) · CRT PD=NEUTRAL · H1 bias **BULLISH**
- **Setup:** ENTRAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **BULLISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — probabilidad calibrada 57% (80%: 52–62%) · EV +0.65R
- **Fusión heurística anterior:** 57% (referencia; sin calibrar)

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | info | 83% OK |
| Rules extendidas (10) | 90% | info | meta >70% |
| CRT coherence | pass | info | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 65.0% | info | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 37.3% | info | grade C; conf=medium; → 40% |
| Penalización dirección | ×0.88 | — | penalización H1 BULLISH vs SHORT |
| Bonificación ubicación | ×1.03 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 44% | info | blend 62/38 con acuerdo BAJA 44% |
| Fusión heurística (anterior) | 57% | info | pesos fijos sin backtest |
| Capas ML/Neural en el % | ninguna (ML/Neural sin validación OOS) | — | solo si mejoran fuera de muestra |
| EV por operación | +0.65R | — | R:R 1:2 · costo 0.06R · Kelly¼ 1.0% riesgo |
| **Probabilidad de éxito** | **57%** | 80%: 52–62% | calibrado walk-forward · n=2097 (n_eff 755) |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 83456: -508.7 pts (-0.610%)
- **PDL** 81535: +1413.2 pts (+1.733%)

### Premium / Discount 0.5

- Midpoint 0.5: **82496**
- Posición precio: **PREMIUM** (precio 82948)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-10 14:00 O=82751 H=83004 L=82695 C=82917 [G]`
- `10-10 15:00 O=82918 H=82992 L=82864 C=82964 [G]`
- `10-10 16:00 O=82966 H=82973 L=82883 C=82948 [R]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 82864-82992; 0.5=82928

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
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 65% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** SHORT @ zona resistencia_debil 82975 (precio actual 82948)
- **SL estructural:** 83140 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 82562 | **BE:** mover a BE en 1:1
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
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY (Lunch)**
- **Vol relativo:** 0.90× → banda **normal** (vol×0.90 en rango normal)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 169.3 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-10 16:14 UTC*
