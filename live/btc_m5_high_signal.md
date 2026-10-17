# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-16 21:56 UTC | NY 2026-10-16 17:56 | FUERA_NY
> Precio **81559.4** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Sin breakout de nivel detectado

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **4 de 6** (66%) | Extendidas: **60%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~53%** — calibrado walk-forward BTC E1 · 80%: 51–55% · n=2097 (n_eff 755) · EV +0.53R

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 81434-81674; 0.5=81554 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 82550 | Bull si cierre arriba |
| PDL | 79700 | Bear si cierre abajo |
| 0.5 midpoint | 81125 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: impacto medido walk-forward n=2097 (n_eff 755)._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓✓ | RSI 41.4 (LONG: neutral) | +6.9 pts | esta zona 54% (n=390) | ponderada |
| Zona premium/discount | ~ | PREMIUM (en contra) | -0.7 pts | a favor 55% / en contra 45% | ponderada |
| 2 velas M5 confirman | ~ | no | +0.2 pts | sí 43% / no 47% | ponderada |
| Rango CRT coherente | ~ | No forzar; esperar pending CRT HTF | Mod | +0.2 pts | sí 46% / no 45% | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Alcista | — | constante en histórico | info |
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

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- RSI TORYS en contra: Fondo rojo TORYS-proxy - filtro short

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **81559.4** |
| Veredicto | **Esperar** (LONG) |
| Entrada óptima | **81530.2** |
| ICT | 81559.4→81530.2 · Refinada 81559.4→81530.2 (FVG BULLISH edge) · Sweep swing_high @ 81619.8 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |
| Plan | Entry **81530.2** · SL **81470.2** · TP **81650.2** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **65%** · ML **22.1%** · Confluencia **BAJA** — 27% · Rules 66%; Neural gated 60% (medium); ML 22% veto suave; 2M5 no listo; Break vs PREMIUM (chase) |
| Historial ref | **btc-120** · 2026-10-16 17:39 NY · Entry **81581.6** · **BUENA** — precio cerca de última Entry + zona OK · (MISMA ZONA) · Δ Entry -51.5 pts (-0.063%) · precio→última 22.2 pts (0.027%) · precio→actual 29.2 pts (0.036%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | -29.2 pts (0.036%) |
| Dist. a SL | -89.2 pts (0.109%) |
| Dist. a TP | +90.8 pts (0.111%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~53% — calibrado walk-forward BTC E1 · 80%: 51–55% · n=2097 (n_eff 755) · EV +0.53R |
| Zona PD vs dirección | LONG en PREMIUM -12 (chase Break) |
| Bias vs dirección | CLI BULLISH a favor +2 |
| Score Rules extendido | **60%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.00× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **en contra** · Hist -43.36 · never trigger |
| Watchtower KZ | FUERA_NY · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **81559.4** | Retest **81530.2–81693.2** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.07% de ref | contexto entry @ 81619.8 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 81530.2 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **81530.2** (limit retest o market al cierre 2ª vela) |
| SL | **81470.2** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **81650.2** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 < 81499.4 o breakdown < 81619.8 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 81559.4→81530.2 (FVG BULLISH edge) · Sweep swing_high @ 81619.8 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ⚠️ |
| 0.5 midpoint | 81124.8 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 81619.8 + reclaim |
| FVG alineados | 5 |
| Order blocks | 5 |
| Entrada refinada | **81530.2** (antes 81559.4 · FVG BULLISH edge) |
| Nota | Refinada 81559.4→81530.2 (FVG BULLISH edge) · Sweep swing_high @ 81619.8 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en resistencia_debil @ 81619.8 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **SHORT**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (222/157) | **SHORT** |
| CRT PD / Premium-Discount | NEUTRAL · PREMIUM | **SHORT** |
| Estructura swings M5 | HL 81217->81434 · HH 81673->81674 | **LONG** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | BEARISH | Fondo rojo TORYS-proxy - filtro short |
| DMI | BEAR | -DI domina (222/157) |
| Swings | HL 81217->81434 | HH 81673->81674 |

---

## M5 detalle

- RSI M5/H1: 41.4 / 40.9
- Zona: resistencia_debil @ 81620
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `21:05 O=81527.4 H=81570.5 L=81510.6 C=81552.9 [G]`
- `21:10 O=81563.6 H=81607.1 L=81556.4 C=81605.7 [G]`
- `21:15 O=81605.7 H=81652.0 L=81605.7 C=81628.1 [G]`
- `21:20 O=81608.0 H=81673.0 L=81604.1 C=81662.0 [G]`
- `21:25 O=81662.0 H=81674.2 L=81608.2 C=81617.1 [R]`
- `21:30 O=81614.4 H=81660.1 L=81614.4 C=81656.1 [G]`
- `21:35 O=81643.9 H=81643.9 L=81589.6 C=81589.6 [R]`
- `21:40 O=81589.6 H=81608.8 L=81581.5 C=81583.1 [R]`
- `21:45 O=81585.5 H=81592.2 L=81577.3 C=81592.2 [G]`
- `21:50 O=81611.0 H=81613.5 L=81563.9 C=81563.9 [R]`
- `21:55 O=81563.9 H=81563.9 L=81561.3 C=81561.3 [R]`
- `21:56 O=81559.4 H=81559.4 L=81559.4 C=81559.4 [G]`

---

## Score reglas extendidas (60%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | -DI domina (222/157) |
| 0.5 midpoint E1 | NO | premium — no long E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 81559 · reloj FUERA_NY · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** ESPERAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — probabilidad calibrada 53% (80%: 50–55%) · EV +0.53R
- **Fusión heurística anterior:** 37% (referencia; sin calibrar)

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | info | 66% OK |
| Rules extendidas (10) | 60% | info | meta >70% |
| CRT coherence | pass | info | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 65.0% | info | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 22.1% | info | grade C; conf=high; → 22% |
| Penalización ubicación | ×0.72 | — | Break alcista en PREMIUM (chase) |
| Acuerdo entre capas | 27% | info | blend 62/38 con acuerdo BAJA 27% |
| Fusión heurística (anterior) | 37% | info | pesos fijos sin backtest |
| Capas ML/Neural en el % | ninguna (ML/Neural sin validación OOS) | — | solo si mejoran fuera de muestra |
| EV por operación | +0.53R | — | R:R 1:2 · costo 0.05R · Kelly¼ 1.0% riesgo |
| **Probabilidad de éxito** | **53%** | 80%: 51–55% | calibrado walk-forward · n=2097 (n_eff 755) |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 82550: -990.2 pts (-1.200%)
- **PDL** 79700: +1859.4 pts (+2.333%)

### Premium / Discount 0.5

- Midpoint 0.5: **81125**
- Posición precio: **PREMIUM** (precio 81559)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-16 20:00 O=81469 H=81673 L=81400 C=81611 [G]`
- `10-16 21:00 O=81611 H=81674 L=81434 C=81561 [R]`
- `10-16 21:56 O=81559 H=81559 L=81559 C=81559 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 81434-81674; 0.5=81554

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

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_BTC_E1` — alto 1.7 / extremo 2.6 / bajo 0.75 / muy bajo 0.45 / período 84 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY**
- **Vol relativo:** 0.00× → banda **muy_bajo** (vol×0.00 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -43.36 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-16 21:56 UTC*
