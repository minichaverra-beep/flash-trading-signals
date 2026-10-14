# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-14 22:15 UTC | NY 2026-10-14 18:15 | FUERA_NY
> Precio **81609.4** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
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

## Veredicto: ENTRAR

**E1/E2:** E1 primario
**Tendencia:** Alcista
**Reglas:** **5 de 6** (83%) | Extendidas: **90%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~57%** — calibrado walk-forward BTC E1 · 80%: 51–62% · n=2097 (n_eff 755) · EV +0.64R

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BULL** | Sweep low H1 + reclaim |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 84068 | Bull si cierre arriba |
| PDL | 80926 | Bear si cierre abajo |
| 0.5 midpoint | 82497 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: impacto medido walk-forward n=2097 (n_eff 755)._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓ | RSI 50.8 (LONG: neutral) | +3.0 pts | esta zona 45% (n=528) | ponderada |
| Zona premium/discount | ✓✓ | DISCOUNT (a favor) | +7.3 pts | a favor 55% / en contra 45% | ponderada |
| 2 velas M5 confirman | ~ | no | +0.2 pts | sí 43% / no 47% | ponderada |
| Rango CRT coherente | ~ | No forzar; esperar pending CRT HTF | Mod | +0.2 pts | sí 46% / no 45% | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Alcista | — | constante en histórico | info |
| R:R mínimo 1:2 | · | 1:2 | — | constante en histórico | info |

### Turtle Soup E2

Score **3/6** | Operable: **NO**
_Modo BREAK: breakout de nivel — E2/reversión despriorizada, NO operable_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | SÍ | Sweep swing low + reclaim |
| 3. Reclaim agresivo | SÍ | Reclaim M5 |
| 4. Entrada zona SL original | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Plan (ENTRAR)

- Dirección: **Long** @ 81609
- SL estructura: **81410** | TP: **82008** (R:R 1:2)
- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos
- BE en 1:1 | Invalidación: fuera zona / CRT invalid

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Patrón perdedor similar: contra bias (BTC-01-06-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **81609.4** |
| Veredicto | **Entrar** (LONG) |
| Entrada óptima | **81586.9** |
| ICT | 81599.2→81586.9 · Refinada 81599.2→81586.9 (FVG BULLISH edge) · Sweep swing_high @ 81739.9 + reclaim · PD DISCOUNT · H1 PENDING_BULL |
| Plan | Entry **81586.9** · SL **81508.6** · TP **81743.6** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **65%** · ML **81.3%** · Confluencia **MEDIA** — 50% · Rules 83%; Neural gated 60% (medium); ML 81% (high); 2M5 no listo; Break operable |
| Historial ref | **btc-098** · 2026-10-14 16:31 NY · Entry **81814.1** · **BUENA** — precio cerca de Entry actual + zona OK · (MÁS CERCA) · Δ Entry -227.2 pts (-0.278%) · precio→última 204.7 pts (0.250%) · precio→actual 22.5 pts (0.028%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | -22.5 pts (0.028%) |
| Dist. a SL | -100.9 pts (0.124%) |
| Dist. a TP | +134.2 pts (0.164%) |
| Riesgo (pts) | 78.4 |
| Winrate setup | ~57% — calibrado walk-forward BTC E1 · 80%: 51–62% · n=2097 (n_eff 755) · EV +0.64R |
| Zona PD vs dirección | LONG en DISCOUNT +2 (zona a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **90%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.15× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **en contra** · Hist -168.1 · never trigger |
| Watchtower KZ | FUERA_NY · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **81609.4** | Retest **81573.4–81646.8** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.04% de ref | contexto entry @ 81573.4 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 81586.9 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **81586.9** (limit retest o market al cierre 2ª vela) |
| SL | **81508.6** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **81743.6** (1:2) |
| R:R | **1:2** · riesgo **78.4** pts |
| Invalidación | Cierre M5 < 81520.8 o breakdown < 81573.4 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 81599.2→81586.9 (FVG BULLISH edge) · Sweep swing_high @ 81739.9 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 82497.0 |
| H1 CRT state | **PENDING_BULL** |
| Killzone / sesión | FUERA_NY (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 81739.9 + reclaim |
| FVG alineados | 5 |
| Order blocks | 5 |
| Entrada refinada | **81586.9** (antes 81599.2 · FVG BULLISH edge) |
| Nota | Refinada 81599.2→81586.9 (FVG BULLISH edge) · Sweep swing_high @ 81739.9 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 81573.4 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BULL/NEUTRAL | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 81543->81542 | HH 81740->81858 |

---

## M5 detalle

- RSI M5/H1: 50.8 / 24.6
- Zona: soporte_debil @ 81573
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `21:20 O=81696.5 H=81726.2 L=81663.7 C=81724.4 [G]`
- `21:25 O=81724.1 H=81759.0 L=81697.7 C=81758.1 [G]`
- `21:30 O=81758.1 H=81858.2 L=81758.1 C=81821.6 [G]`
- `21:35 O=81822.7 H=81855.6 L=81769.4 C=81782.9 [R]`
- `21:40 O=81782.6 H=81812.6 L=81714.6 C=81726.6 [R]`
- `21:45 O=81725.8 H=81856.1 L=81725.6 C=81756.3 [G]`
- `21:50 O=81756.3 H=81775.7 L=81628.2 C=81647.2 [R]`
- `21:55 O=81647.2 H=81696.1 L=81647.0 C=81672.3 [G]`
- `22:00 O=81672.3 H=81690.5 L=81598.3 C=81664.6 [R]`
- `22:05 O=81664.6 H=81664.6 L=81524.0 C=81537.3 [R]`
- `22:10 O=81532.2 H=81653.4 L=81497.7 C=81611.8 [G]`
- `22:15 O=81611.9 H=81630.7 L=81602.9 C=81609.4 [R]`

---

## Score reglas extendidas (90%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 81609 · reloj FUERA_NY · CRT PD=NEUTRAL · H1 bias **BEARISH**
- **Setup:** ENTRAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — probabilidad calibrada 57% (80%: 51–62%) · EV +0.65R
- **Fusión heurística anterior:** 64% (referencia; sin calibrar)

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | info | 83% OK |
| Rules extendidas (10) | 90% | info | meta >70% |
| CRT coherence | pass | info | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 65.0% | info | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 81.3% | info | grade A+; conf=high; → 81% |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.03 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 50% | info | blend 62/38 con acuerdo MEDIA 50% |
| Fusión heurística (anterior) | 64% | info | pesos fijos sin backtest |
| Capas ML/Neural en el % | ninguna (ML/Neural sin validación OOS) | — | solo si mejoran fuera de muestra |
| EV por operación | +0.64R | — | R:R 1:2 · costo 0.06R · Kelly¼ 1.0% riesgo |
| **Probabilidad de éxito** | **57%** | 80%: 51–62% | calibrado walk-forward · n=2097 (n_eff 755) |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 84068: -2458.2 pts (-2.924%)
- **PDL** 80926: +683.0 pts (+0.844%)

### Premium / Discount 0.5

- Midpoint 0.5: **82497**
- Posición precio: **DISCOUNT** (precio 81609)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-14 20:00 O=81734 H=81883 L=81543 C=81675 [R]`
- `10-14 21:00 O=81676 H=81858 L=81542 C=81672 [R]`
- `10-14 22:00 O=81672 H=81690 L=81498 C=81609 [R]`

- Estado CRT H1: **PENDING_BULL** — Sweep low H1 + reclaim

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
| 1 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 65% | contra-bias, LOSS |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** LONG @ zona soporte_debil 81573 (precio actual 81609)
- **SL estructural:** 81410 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 82008 | **BE:** mover a BE en 1:1
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
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY**
- **Vol relativo:** 0.15× → banda **muy_bajo** (vol×0.15 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -168.1 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-14 22:15 UTC*
