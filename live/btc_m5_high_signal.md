# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-16 15:35 UTC | NY 2026-10-16 11:35 | FUERA_NY (Lunch)
> Precio **81637.9** | HIGH mode | PF E1=4.77 | E2 max 10%
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
**Tendencia:** Sin dirección
**Reglas:** **5 de 6** (83%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~59%** — calibrado walk-forward BTC E1 · 80%: 56–62% · n=2097 (n_eff 755) · EV +0.69R

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **COMPLETED_BEAR** | Low H1 81829 alcanzado |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 82611 | Bull si cierre arriba |
| PDL | 79737 | Bear si cierre abajo |
| 0.5 midpoint | 81174 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 27 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: impacto medido walk-forward n=2097 (n_eff 755)._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓✓ | RSI 26.6 (LONG: con recorrido a favor) | +12.9 pts | esta zona 55% (n=210) | ponderada |
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

### Plan (ENTRAR)

- Dirección: **Long** @ 81638
- SL estructura: **81475** | TP: **81964** (R:R 1:2)
- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos
- BE en 1:1 | Invalidación: fuera zona / CRT invalid

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- RSI M5 26.6 sobrevendido — filtro TORYS-like

### Galería (cross-ref)

- Patrón perdedor similar: contra bias (BTC-01-06-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **81637.9** |
| Veredicto | **Entrar** (LONG) |
| Entrada óptima | **81667.9** |
| ICT | Base 81667.9 (zona base) · Sweep swing_high @ 82043.9 + reclaim · PD PREMIUM · H1 COMPLETED_BEAR |
| Plan | Entry **81667.9** · SL **81525.8** · TP **81952.1** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **65%** · ML **81.5%** · Confluencia **MEDIA** — 50% · Rules 83%; Neural gated 60% (medium); ML 81% (high); 2M5 no listo; Break vs PREMIUM (chase) |
| Historial ref | **btc-112** · 2026-10-16 11:11 NY · Entry **81799.5** · **BUENA** — precio cerca de Entry actual + zona OK · (MÁS CERCA) · Δ Entry -131.7 pts (-0.161%) · precio→última 161.7 pts (0.198%) · precio→actual 30.0 pts (0.037%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | +30.0 pts (0.037%) |
| Dist. a SL | -112.1 pts (0.137%) |
| Dist. a TP | +314.2 pts (0.385%) |
| Riesgo (pts) | 142.1 |
| Winrate setup | ~59% — calibrado walk-forward BTC E1 · 80%: 56–62% · n=2097 (n_eff 755) · EV +0.69R |
| Zona PD vs dirección | LONG en PREMIUM -12 (chase Break) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.23× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **OK** · Hist 13.27 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **81637.9** | Retest **81654.6–81728.1** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.02% de ref | contexto entry @ 81654.6 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 81654.6–81728.1 (soporte_debil @ 81654.6) + 2 velas M5 verdes consecutivas en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **81667.9** (limit retest o market al cierre 2ª vela) |
| SL | **81525.8** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **81952.1** (1:2) |
| R:R | **1:2** · riesgo **142.1** pts |
| Invalidación | Cierre M5 < 81525.8 o breakdown < 81654.6 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 81667.9 (zona base) · Sweep swing_high @ 82043.9 + reclaim · PD PREMIUM · H1 COMPLETED_BEAR |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ⚠️ |
| 0.5 midpoint | 81174.0 |
| H1 CRT state | **COMPLETED_BEAR** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 82043.9 + reclaim |
| FVG alineados | 2 |
| Order blocks | 2 |
| Entrada | **81667.9** (zona base · sin cambio) |
| Nota | Base 81667.9 (zona base) · Sweep swing_high @ 82043.9 + reclaim · PD PREMIUM · H1 COMPLETED_BEAR |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 81654.6 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BEAR/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (1063/385) |
| Swings | LL 81829->81417 | HH 82044->82459 |

---

## M5 detalle

- RSI M5/H1: 26.6 / 40.4
- Zona: soporte_debil @ 81655
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:40 O=82330.3 H=82347.4 L=82257.0 C=82281.9 [R]`
- `14:45 O=82281.9 H=82380.8 L=82254.6 C=82340.2 [G]`
- `14:50 O=82339.7 H=82339.7 L=81964.1 C=81964.1 [R]`
- `14:55 O=81961.7 H=82065.7 L=81916.0 C=81943.5 [R]`
- `15:00 O=81943.5 H=81950.2 L=81799.5 C=81817.9 [R]`
- `15:05 O=81817.9 H=81818.0 L=81450.0 C=81546.4 [R]`
- `15:10 O=81546.2 H=81800.5 L=81545.4 C=81692.1 [G]`
- `15:15 O=81692.1 H=81738.9 L=81586.1 C=81588.2 [R]`
- `15:20 O=81588.2 H=81663.6 L=81417.3 C=81550.4 [R]`
- `15:25 O=81550.4 H=81657.7 L=81538.8 C=81549.1 [R]`
- `15:30 O=81549.4 H=81683.2 L=81549.3 C=81663.6 [G]`
- `15:35 O=81663.5 H=81672.3 L=81631.1 C=81637.9 [R]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 27 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | -DI domina (1063/385) |
| 0.5 midpoint E1 | NO | premium — no long E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 81638 · reloj FUERA_NY (Lunch) · CRT PD=NEUTRAL · H1 bias **BEARISH**
- **Setup:** ENTRAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — probabilidad calibrada 59% (80%: 56–62%) · EV +0.69R
- **Fusión heurística anterior:** 49% (referencia; sin calibrar)

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | info | 83% OK |
| Rules extendidas (10) | 70% | info | meta >70% |
| CRT coherence | pass | info | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 65.0% | info | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 81.5% | info | grade A+; conf=high; → 81% |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Penalización ubicación | ×0.72 | — | Break alcista en PREMIUM (chase) |
| Acuerdo entre capas | 50% | info | blend 62/38 con acuerdo MEDIA 50% |
| Fusión heurística (anterior) | 49% | info | pesos fijos sin backtest |
| Capas ML/Neural en el % | ninguna (ML/Neural sin validación OOS) | — | solo si mejoran fuera de muestra |
| EV por operación | +0.69R | — | R:R 1:2 · costo 0.08R · Kelly¼ 1.0% riesgo |
| **Probabilidad de éxito** | **59%** | 80%: 56–62% | calibrado walk-forward · n=2097 (n_eff 755) |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 82611: -972.8 pts (-1.178%)
- **PDL** 79737: +1900.4 pts (+2.383%)

### Premium / Discount 0.5

- Midpoint 0.5: **81174**
- Posición precio: **PREMIUM** (precio 81638)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-16 13:00 O=82009 H=82149 L=81655 C=81991 [R]`
- `10-16 14:00 O=81990 H=82459 L=81829 C=81943 [R]`
- `10-16 15:00 O=81943 H=81950 L=81417 C=81638 [R]`

- Estado CRT H1: **COMPLETED_BEAR** — Low H1 81829 alcanzado

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

- **Entrada:** LONG @ zona soporte_debil 81655 (precio actual 81638)
- **SL estructural:** 81475 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 81964 | **BE:** mover a BE en 1:1
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
- **Vol relativo:** 0.23× → banda **muy_bajo** (vol×0.23 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 13.27 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-16 15:35 UTC*
