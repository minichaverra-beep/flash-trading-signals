# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-08 20:27 UTC | NY 2026-10-08 16:27 | FUERA_NY
> Precio **51293.4** | HIGH mode | PF E1=4.77 | E2 max 10%
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

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~66%** — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo BAJA -8; patron WIN similar +3; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **COMPLETED_BULL** | High H1 51272 alcanzado |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 51588 | Bull si cierre arriba |
| PDL | 50933 | Bear si cierre abajo |
| 0.5 midpoint | 51261 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 64 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓✓ | RSI 63.8 (SHORT: con recorrido a favor) | sin calibrar | n/d | ponderada |
| Zona premium/discount | ✓ | PREMIUM (a favor) | sin calibrar | n/d | ponderada |
| 2 velas M5 confirman | ✗ | no | sin calibrar | n/d | ponderada |
| Rango CRT coherente | ✓ | No forzar; esperar pending CRT HTF | Mod | sin calibrar | n/d | ponderada |
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

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **51293.4** |
| Veredicto | **Esperar** (SHORT) |
| Entrada óptima | **51278.4** |
| ICT | 51258.2→51278.4 · Refinada 51258.2→51278.4 (OB BEARISH edge) · Sweep swing_high @ 51266.5 + reclaim · PD PREMIUM · H1 COMPLETED_BULL |
| Plan | Entry **51278.4** · SL **51338.4** · TP **51158.4** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **72%** · ML **0.0%** · Confluencia **BAJA** — 44% · Rules 83%; Neural gated 64% (medium); ML 0% veto suave; 2M5 no listo; Break operable |
| Historial ref | **us30-063** · 2026-10-08 12:14 NY · Entry **50996.3** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry +282.1 pts (+0.553%) · precio→última 297.1 pts (0.583%) · precio→actual 15.0 pts (0.029%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | -15.0 pts (0.029%) |
| Dist. a SL | +45.0 pts (0.088%) |
| Dist. a TP | -135.0 pts (0.263%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~66% — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo BAJA -8; patron WIN similar +3; 83% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +2 (zona a favor) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.09× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist -14.81 · never trigger |
| Watchtower KZ | FUERA_NY · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **51293.4** | Retest **51220.4–51278.4** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.05% de ref | contexto entry @ 51266.5 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest OB BEARISH edge @ 51278.4 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **51278.4** (limit retest o market al cierre 2ª vela) |
| SL | **51338.4** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **51158.4** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 51318.2 o breakout > 51266.5 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 51258.2→51278.4 (OB BEARISH edge) · Sweep swing_high @ 51266.5 + reclaim · PD PREMIUM · H1 COMPLETED_BULL |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 51260.6 |
| H1 CRT state | **COMPLETED_BULL** |
| Killzone / sesión | FUERA_NY (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 51266.5 + reclaim |
| FVG alineados | 3 |
| Order blocks | 4 |
| Entrada refinada | **51278.4** (antes 51258.2 · OB BEARISH edge) |
| Nota | Refinada 51258.2→51278.4 (OB BEARISH edge) · Sweep swing_high @ 51266.5 + reclaim · PD PREMIUM · H1 COMPLETED_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 51266.5 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | +DI domina (226/128) | **LONG** |
| CRT PD / Premium-Discount | NEUTRAL · PREMIUM | **SHORT** |
| Estructura swings M5 | HL 51138->51206 · HH 51266->51354 | **LONG** |

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BULL/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (226/128) |
| Swings | HL 51138->51206 | HH 51266->51354 |

---

## M5 detalle

- RSI M5/H1: 63.8 / 66.8
- Zona: resistencia_debil @ 51266
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `19:30 O=51239.5 H=51242.5 L=51216.5 C=51216.5 [R]`
- `19:35 O=51217.5 H=51235.5 L=51213.5 C=51234.5 [G]`
- `19:40 O=51233.5 H=51240.5 L=51219.5 C=51226.5 [R]`
- `19:45 O=51225.5 H=51241.5 L=51218.5 C=51235.5 [G]`
- `19:50 O=51234.5 H=51254.5 L=51205.5 C=51219.5 [R]`
- `19:55 O=51220.5 H=51272.2 L=51209.5 C=51252.5 [G]`
- `20:00 O=51252.9 H=51303.8 L=51251.9 C=51288.4 [G]`
- `20:05 O=51288.9 H=51354.3 L=51278.4 C=51341.3 [G]`
- `20:10 O=51340.3 H=51349.3 L=51263.4 C=51276.4 [R]`
- `20:15 O=51275.4 H=51306.3 L=51275.4 C=51298.4 [G]`
- `20:20 O=51299.4 H=51306.3 L=51293.4 C=51300.4 [G]`
- `20:25 O=51299.4 H=51300.4 L=51286.4 C=51293.4 [R]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 64 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | +DI domina (226/128) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 51293 · reloj FUERA_NY · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** ESPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score combinado 58%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 0.0% | 18% | grade C; conf=high; → 0% |
| Bonificación ubicación | ×1.03 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 44% | 38% | blend 62/38 con acuerdo BAJA 44% |
| **Probabilidad de éxito** | **58%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 51588: -294.9 pts (-0.572%)
- **PDL** 50933: +360.5 pts (+0.708%)

### Premium / Discount 0.5

- Midpoint 0.5: **51261**
- Posición precio: **PREMIUM** (precio 51293)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-08 18:00 O=51176 H=51218 L=51118 C=51184 [G]`
- `10-08 19:00 O=51184 H=51272 L=51138 C=51252 [G]`
- `10-08 20:00 O=51253 H=51354 L=51252 C=51293 [G]`

- Estado CRT H1: **COMPLETED_BULL** — High H1 51272 alcanzado

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
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY**
- **Vol relativo:** 0.09× → banda **muy_bajo** (vol×0.09 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -14.81 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-08 20:27 UTC*
