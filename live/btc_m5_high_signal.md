# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-08 14:56 UTC | NY 2026-10-08 10:56 | NY AM 10-11
> Precio **82603.4** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- Breakout bajista sostenido < 82709

---

## Veredicto: ENTRAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 6** (83%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~59%** — calibrado walk-forward BTC E1 · 80%: 56–63% · n=2097 (n_eff 755) · EV +0.69R

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **COMPLETED_BULL** | High H1 82570 alcanzado |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 85594 | Bull si cierre arriba |
| PDL | 82709 | Bear si cierre abajo |
| 0.5 midpoint | 84152 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Breakout bajista sostenido < 82709

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 74 OK |
| Rango coherente | ✅ | Shorts E1 rechazo resistencia (premium)  |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: impacto medido walk-forward n=2097 (n_eff 755)._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓✓ | RSI 73.8 (SHORT: con recorrido a favor) | +13.1 pts | esta zona 55% (n=210) | ponderada |
| Zona premium/discount | ~ | DISCOUNT (en contra) | -0.7 pts | a favor 55% / en contra 45% | ponderada |
| 2 velas M5 confirman | ~ | no | +0.2 pts | sí 43% / no 47% | ponderada |
| Rango CRT coherente | ~ | Shorts E1 rechazo resistencia (premium)  | +0.2 pts | sí 46% / no 45% | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Bajista | — | constante en histórico | info |
| R:R mínimo 1:2 | · | 1:2 | — | constante en histórico | info |

### Turtle Soup E2

Score **2/6** | Operable: **NO**
_Modo BREAK: breakout de nivel — E2/reversión despriorizada, NO operable_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | SÍ | Sweep swing low + reclaim |
| 3. Reclaim agresivo | SÍ | Reclaim M5 |
| 4. Entrada zona SL original | NO | Cerca nivel barrido |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Plan (ENTRAR)

- Dirección: **Short** @ 82603
- SL estructura: **82778** | TP: **82254** (R:R 1:2)
- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos
- BE en 1:1 | Invalidación: fuera zona / CRT invalid

### Red flags

- Ninguno detectado

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **82603.4** |
| Veredicto | **Entrar** (SHORT) |
| Entrada óptima | **82612.7** |
| ICT | 82599.3→82612.7 · Refinada 82599.3→82612.7 (resistencia debil) · Sweep PDL @ 82709.4 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL · killzone NY AM 10-11 |
| Plan | Entry **82612.7** · SL **82759.5** · TP **82319.0** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **65%** · ML **30.4%** · Confluencia **BAJA** — 44% · Rules 83%; Neural gated 60% (medium); ML 30% veto suave; 2M5 no listo; Break vs DISCOUNT (chase) |
| Historial ref | **btc-080** · 2026-10-07 17:29 NY · Entry **83323.0** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry -710.3 pts (-0.852%) · precio→última 719.6 pts (0.864%) · precio→actual 9.3 pts (0.011%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +9.3 pts (0.011%) |
| Dist. a SL | +156.1 pts (0.189%) |
| Dist. a TP | -284.4 pts (0.344%) |
| Riesgo (pts) | 146.9 |
| Winrate setup | ~59% — calibrado walk-forward BTC E1 · 80%: 56–63% · n=2097 (n_eff 755) · EV +0.69R |
| Zona PD vs dirección | SHORT en DISCOUNT -12 (chase Break) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.36× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **OK** · Hist -284.8 · never trigger |
| Watchtower KZ | NY AM 10-11 · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **82603.4** | Retest **82538.3–82612.7** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.01% de ref | contexto entry @ 82612.7 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest resistencia debil @ 82612.7 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **82612.7** (limit retest o market al cierre 2ª vela) |
| SL | **82759.5** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **82319.0** (1:2) |
| R:R | **1:2** · riesgo **146.9** pts |
| Invalidación | Cierre M5 > 82746.2 o breakout > 82612.7 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 82599.3→82612.7 (resistencia debil) · Sweep PDL @ 82709.4 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL · killzone NY AM 10-11 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ⚠️ |
| 0.5 midpoint | 84151.7 |
| H1 CRT state | **COMPLETED_BULL** |
| Killzone / sesión | NY AM 10-11 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDL @ 82709.4 + reclaim |
| FVG alineados | 5 |
| Order blocks | 2 |
| Entrada refinada | **82612.7** (antes 82599.3 · resistencia debil) |
| Nota | Refinada 82599.3→82612.7 (resistencia debil) · Sweep PDL @ 82709.4 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL · killzone NY AM 10-11 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 82612.7 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 10-11_

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
| DMI (momentum M5) | +DI domina (863/306) | **LONG** |
| CRT PD / Premium-Discount | BEARISH · DISCOUNT | **LONG** |
| Estructura swings M5 | HL 81693->82437 · HH 82570->82726 | **LONG** |

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BULL/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (863/306) |
| Swings | HL 81693->82437 | HH 82570->82726 |

---

## M5 detalle

- RSI M5/H1: 73.8 / 38.0
- Zona: resistencia_debil @ 82613
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:00 O=82108.1 H=82247.6 L=82051.6 C=82220.3 [G]`
- `14:05 O=82223.5 H=82404.4 L=82206.4 C=82347.3 [G]`
- `14:10 O=82349.4 H=82549.3 L=82349.4 C=82471.1 [G]`
- `14:15 O=82470.0 H=82529.2 L=82369.1 C=82501.4 [G]`
- `14:20 O=82502.7 H=82659.4 L=82413.8 C=82457.7 [R]`
- `14:25 O=82457.7 H=82688.1 L=82446.6 C=82660.5 [G]`
- `14:30 O=82660.6 H=82726.2 L=82539.5 C=82636.3 [R]`
- `14:35 O=82636.1 H=82653.8 L=82470.4 C=82493.7 [R]`
- `14:40 O=82494.9 H=82556.0 L=82436.7 C=82503.8 [G]`
- `14:45 O=82506.7 H=82626.6 L=82490.2 C=82608.6 [G]`
- `14:50 O=82610.8 H=82667.6 L=82507.5 C=82564.2 [R]`
- `14:55 O=82562.1 H=82657.4 L=82536.0 C=82603.4 [G]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 74 OK |
| Rango coherente | SÍ | Shorts E1 rechazo resistencia (premium)  |
| DMI alineado | NO | +DI domina (863/306) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 82603 · reloj NY AM 10-11 · CRT PD=BEARISH · H1 bias **NEUTRAL**
- **Setup:** ENTRAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — probabilidad calibrada 59% (80%: 56–63%) · EV +0.69R
- **Fusión heurística anterior:** 47% (referencia; sin calibrar)

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | info | 83% OK |
| Rules extendidas (10) | 70% | info | meta >70% |
| CRT coherence | pass | info | Shorts E1 rechazo resistencia (premium)  |
| Neural galería (gated) | 65.0% | info | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 30.4% | info | grade C; conf=medium; → 35% |
| Penalización ubicación | ×0.72 | — | Break bajista en DISCOUNT (chase) |
| Acuerdo entre capas | 44% | info | blend 62/38 con acuerdo BAJA 44% |
| Fusión heurística (anterior) | 47% | info | pesos fijos sin backtest |
| Capas ML/Neural en el % | ninguna (ML/Neural sin validación OOS) | — | solo si mejoran fuera de muestra |
| EV por operación | +0.69R | — | R:R 1:2 · costo 0.07R · Kelly¼ 1.0% riesgo |
| **Probabilidad de éxito** | **59%** | 80%: 56–63% | calibrado walk-forward · n=2097 (n_eff 755) |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 85594: -2990.6 pts (-3.494%)
- **PDL** 82709: -106.0 pts (-0.128%)

### Premium / Discount 0.5

- Midpoint 0.5: **84152**
- Posición precio: **DISCOUNT** (precio 82603)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-08 12:00 O=82422 H=82444 L=81866 C=82253 [R]`
- `10-08 13:00 O=82253 H=82570 L=81693 C=82107 [R]`
- `10-08 14:00 O=82108 H=82726 L=82052 C=82603 [G]`

- Estado CRT H1: **COMPLETED_BULL** — High H1 82570 alcanzado

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

- **Entrada:** SHORT @ zona resistencia_debil 82613 (precio actual 82603)
- **SL estructural:** 82778 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 82254 | **BE:** mover a BE en 1:1
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

- **FVG+Vol:** `Zentinel_BTC_E1` — alto 1.7 / extremo 2.6 / bajo 0.75 / muy bajo 0.45 / período 84 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 10-11**
- **Vol relativo:** 0.36× → banda **muy_bajo** (vol×0.36 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -284.8 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-08 14:56 UTC*
