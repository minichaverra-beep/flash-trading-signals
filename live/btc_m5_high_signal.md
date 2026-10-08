# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-07 21:29 UTC | NY 2026-10-07 17:29 | FUERA_NY
> Precio **83289.2** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- Precio < 83293 pero sin hold de 2 cierres — no chase

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~41%** — calibrado walk-forward BTC E1 · 80%: 38–43% · n=2097 (n_eff 755) · EV +0.18R

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BULL** | Sweep low H1 + reclaim |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 86687 | Bull si cierre arriba |
| PDL | 85088 | Bear si cierre abajo |
| 0.5 midpoint | 85888 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Precio < 83293 pero sin hold de 2 cierres — no chase

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | RSI 30 sobrevendido |
| Rango coherente | ✅ | Shorts E1 rechazo resistencia (premium)  |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: impacto medido walk-forward n=2097 (n_eff 755)._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✗✗ | RSI 29.5 (SHORT: extendido) | -4.9 pts | esta zona 39% (n=326) | ponderada |
| Zona premium/discount | ~ | DISCOUNT (en contra) | -0.7 pts | a favor 55% / en contra 45% | ponderada |
| 2 velas M5 confirman | ~ | no | +0.2 pts | sí 43% / no 47% | ponderada |
| Rango CRT coherente | ~ | Shorts E1 rechazo resistencia (premium)  | +0.2 pts | sí 46% / no 45% | ponderada |
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

- CRT H1 pending bull — no entrar short contra invalid reciente
- RSI M5 29.5 sobrevendido — filtro TORYS-like

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **83289.2** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **83323.0** |
| ICT | 83289.2→83323.0 · Refinada 83289.2→83323.0 (FVG BEARISH edge) · Sweep swing_high @ 83406.3 + reclaim · PD DISCOUNT · H1 PENDING_BULL |
| Plan | Entry **83323.0** · SL **83383.0** · TP **83203.0** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **65%** · ML **64.2%** · Confluencia **BAJA** — 45% · Rules 66%; Neural gated 60% (medium); ML 64% zona media; 2M5 no listo; Break vs DISCOUNT (chase) |
| Historial ref | **btc-079** · 2026-10-07 15:37 NY · Entry **83365.6** · **BUENA** — precio cerca de última Entry + zona OK + bando alineado · (MISMA ZONA) · Δ Entry -42.6 pts (-0.051%) · precio→última 76.4 pts (0.092%) · precio→actual 33.8 pts (0.041%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | +33.8 pts (0.041%) |
| Dist. a SL | +93.8 pts (0.113%) |
| Dist. a TP | -86.2 pts (0.104%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~41% — calibrado walk-forward BTC E1 · 80%: 38–43% · n=2097 (n_eff 755) · EV +0.18R |
| Zona PD vs dirección | SHORT en DISCOUNT -12 (chase Break) |
| Bias vs dirección | H1 BEARISH a favor +4 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **bajo** · 0.61× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **OK** · Hist -324.9 · never trigger |
| Watchtower KZ | FUERA_NY · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **83289.2** | Retest **83217.6–83323.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.00% de ref | contexto entry @ 83292.5 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 83323.0 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **83323.0** (limit retest o market al cierre 2ª vela) |
| SL | **83383.0** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **83203.0** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 83349.2 o breakout > 83292.5 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 83289.2→83323.0 (FVG BEARISH edge) · Sweep swing_high @ 83406.3 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ⚠️ |
| 0.5 midpoint | 85887.9 |
| H1 CRT state | **PENDING_BULL** |
| Killzone / sesión | FUERA_NY (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 83406.3 + reclaim |
| FVG alineados | 4 |
| Order blocks | 5 |
| Entrada refinada | **83323.0** (antes 83289.2 · FVG BEARISH edge) |
| Nota | Refinada 83289.2→83323.0 (FVG BEARISH edge) · Sweep swing_high @ 83406.3 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 83292.5 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BULL/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (401/168) |
| Swings | LL 83277->83273 | LH 83567->83406 |

---

## M5 detalle

- RSI M5/H1: 29.5 / 32.0
- Zona: soporte_debil @ 83293
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `20:30 O=83515.8 H=83525.1 L=83331.6 C=83360.2 [R]`
- `20:35 O=83358.7 H=83360.1 L=83276.6 C=83309.5 [R]`
- `20:40 O=83309.9 H=83357.0 L=83291.6 C=83345.5 [G]`
- `20:45 O=83345.5 H=83350.6 L=83308.3 C=83324.1 [R]`
- `20:50 O=83324.1 H=83357.7 L=83319.8 C=83348.9 [G]`
- `20:55 O=83348.9 H=83402.4 L=83342.5 C=83378.2 [G]`
- `21:00 O=83377.5 H=83406.3 L=83310.4 C=83336.4 [R]`
- `21:05 O=83335.6 H=83336.1 L=83313.5 C=83319.9 [R]`
- `21:10 O=83319.9 H=83325.0 L=83272.7 C=83325.0 [G]`
- `21:15 O=83325.6 H=83341.1 L=83310.6 C=83328.8 [G]`
- `21:20 O=83328.8 H=83350.9 L=83327.9 C=83346.5 [G]`
- `21:25 O=83346.9 H=83348.5 L=83283.4 C=83289.2 [R]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | RSI 30 sobrevendido |
| Rango coherente | SÍ | Shorts E1 rechazo resistencia (premium)  |
| DMI alineado | SÍ | -DI domina (401/168) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 83289 · reloj FUERA_NY · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 4/6 (66%)
- **Bando:** CLI y H1 alineados (**BEARISH**)
- **Veredicto integrado:** NO_OPERAR — probabilidad calibrada 41% (80%: 38–43%) · EV +0.17R
- **Fusión heurística anterior:** 48% (referencia; sin calibrar)

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | info | 66% OK |
| Rules extendidas (10) | 70% | info | meta >70% |
| CRT coherence | pass | info | Shorts E1 rechazo resistencia (premium)  |
| Neural galería (gated) | 65.0% | info | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 64.2% | info | grade B; conf=medium; → 61% |
| Penalización ubicación | ×0.72 | — | Break bajista en DISCOUNT (chase) |
| Acuerdo entre capas | 45% | info | blend 62/38 con acuerdo BAJA 45% |
| Fusión heurística (anterior) | 48% | info | pesos fijos sin backtest |
| Capas ML/Neural en el % | ninguna (ML/Neural sin validación OOS) | — | solo si mejoran fuera de muestra |
| EV por operación | +0.18R | — | R:R 1:2 · costo 0.05R · Kelly¼ 1.0% riesgo |
| **Probabilidad de éxito** | **41%** | 80%: 38–43% | calibrado walk-forward · n=2097 (n_eff 755) |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 86687: -3398.2 pts (-3.920%)
- **PDL** 85088: -1799.3 pts (-2.115%)

### Premium / Discount 0.5

- Midpoint 0.5: **85888**
- Posición precio: **DISCOUNT** (precio 83289)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-07 19:00 O=83359 H=83471 L=83258 C=83390 [G]`
- `10-07 20:00 O=83391 H=83567 L=83277 C=83378 [R]`
- `10-07 21:00 O=83377 H=83406 L=83273 C=83289 [R]`

- Estado CRT H1: **PENDING_BULL** — Sweep low H1 + reclaim

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
- **Vol relativo:** 0.61× → banda **bajo** (vol×0.61 ≤ bajo 0.75)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -324.9 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-07 21:29 UTC*
