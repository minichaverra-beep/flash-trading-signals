# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-14 22:47 UTC | NY 2026-10-14 18:47 | FUERA_NY
> Precio **4109.96** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-14 22:45 UTC** · hace 2 min · fuente MT5 XAUUSDm (broker, M5/H1)
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
- Breakout bajista sostenido < 4147

---

## Veredicto: ENTRAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~52%** — histórico E1 BTC · SHORT en DISCOUNT -12 (chase Break); CLI BEARISH a favor +2; acuerdo BAJA -8; patron WIN similar +3; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **COMPLETED_BULL** | High H1 4105 alcanzado |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4200 | Bull si cierre arriba |
| PDL | 4147 | Bear si cierre abajo |
| 0.5 midpoint | 4174 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Breakout bajista sostenido < 4147

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 77 OK |
| Rango coherente | ✅ | Shorts E1 rechazo resistencia (premium)  |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓✓ | RSI 77.4 (SHORT: con recorrido a favor) | sin calibrar | n/d | ponderada |
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

- Dirección: **Short** @ 4110
- SL estructura: **4118** | TP: **4094** (R:R 1:2)
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
| Precio | **4109.96** |
| Veredicto | **Entrar** (SHORT) |
| Entrada óptima | **4105.94** |
| ICT | Base 4105.9 (zona base) · Sweep swing_high @ 4101.6 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL |
| Plan | Entry **4105.94** · SL **4111.94** · TP **4093.94** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **60%** · ML **5.1%** · Confluencia **BAJA** — 33% · Rules 83%; Neural débil/gating 60% conf=low; ML 5% veto suave; 2M5 no listo; Break vs DISCOUNT (chase) |
| Historial ref | **xauusd-052** · 2026-10-14 18:46 NY · Entry **4105.94** · **BUENA** — precio cerca de última Entry + zona OK · (MISMA ZONA) · Δ Entry +0.00 pts (+0.000%) · precio→última 4.03 pts (0.098%) · precio→actual 4.03 pts (0.098%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | -4.03 pts (0.098%) |
| Dist. a SL | +1.97 pts (0.048%) |
| Dist. a TP | -16.03 pts (0.390%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~52% — histórico E1 BTC · SHORT en DISCOUNT -12 (chase Break); CLI BEARISH a favor +2; acuerdo BAJA -8; patron WIN similar +3; 83% reglas |
| Zona PD vs dirección | SHORT en DISCOUNT -12 (chase Break) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. low · 60% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.37× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist -9.284 · never trigger |
| Watchtower KZ | FUERA_NY · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4109.96** | Retest **4102.91–4106.60** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.08% de ref | contexto entry @ 4106.60 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 4102.91–4106.60 (resistencia_debil @ 4106.60) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **4105.94** (limit retest o market al cierre 2ª vela) |
| SL | **4111.94** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4093.94** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 > 4111.94 o breakout > 4106.60 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 4105.9 (zona base) · Sweep swing_high @ 4101.6 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ⚠️ |
| 0.5 midpoint | 4173.56 |
| H1 CRT state | **COMPLETED_BULL** |
| Killzone / sesión | FUERA_NY (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4101.6 + reclaim |
| FVG alineados | 1 |
| Order blocks | 2 |
| Entrada | **4105.94** (zona base · sin cambio) |
| Nota | Base 4105.9 (zona base) · Sweep swing_high @ 4101.6 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 4106.60 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
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

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | +DI domina (15/4) | **LONG** |
| CRT PD / Premium-Discount | BEARISH · DISCOUNT | **LONG** |
| Estructura swings M5 | LL 4099->4097 · LH 4103->4102 | **SHORT** |

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BULL/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (15/4) |
| Swings | LL 4099->4097 | LH 4103->4102 |

---

## M5 detalle

- RSI M5/H1: 77.4 / 32.0
- Zona: resistencia_debil @ 4107
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `20:50 O=4100.01 H=4103.10 L=4099.46 C=4102.40 [G]`
- `20:55 O=4102.67 H=4105.36 L=4102.41 C=4104.65 [G]`
- `22:00 O=4105.53 H=4106.21 L=4103.67 C=4103.67 [R]`
- `22:05 O=4103.85 H=4104.56 L=4102.56 C=4103.75 [R]`
- `22:10 O=4103.68 H=4106.59 L=4102.87 C=4104.89 [G]`
- `22:15 O=4104.72 H=4105.95 L=4103.69 C=4105.78 [G]`
- `22:20 O=4105.98 H=4108.98 L=4105.58 C=4107.79 [G]`
- `22:25 O=4107.97 H=4107.97 L=4105.78 C=4107.80 [R]`
- `22:30 O=4107.99 H=4110.68 L=4106.00 C=4106.83 [R]`
- `22:35 O=4106.87 H=4108.35 L=4105.93 C=4106.54 [R]`
- `22:40 O=4106.27 H=4111.50 L=4106.27 C=4110.17 [G]`
- `22:45 O=4110.20 H=4112.04 L=4109.58 C=4109.96 [R]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 77 OK |
| Rango coherente | SÍ | Shorts E1 rechazo resistencia (premium)  |
| DMI alineado | NO | +DI domina (15/4) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4110 · reloj FUERA_NY · CRT PD=BEARISH · H1 bias **NEUTRAL**
- **Setup:** ENTRAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — score combinado 40%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | pass | 12% | Shorts E1 rechazo resistencia (premium)  |
| Neural galería (gated) | 60.3% | 25% | no alineado; conf=low; gate×0.35 → 54% |
| ML tabular (gated) | 5.1% | 18% | grade C; conf=high; → 5% |
| Penalización ubicación | ×0.72 | — | Break bajista en DISCOUNT (chase) |
| Acuerdo entre capas | 33% | 38% | blend 62/38 con acuerdo BAJA 33% |
| **Probabilidad de éxito** | **40%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4200: -90.4 pts (-2.153%)
- **PDL** 4147: -36.8 pts (-0.886%)

### Premium / Discount 0.5

- Midpoint 0.5: **4174**
- Posición precio: **DISCOUNT** (precio 4110)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-14 19:00 O=4097 H=4107 L=4093 C=4101 [G]`
- `10-14 20:00 O=4101 H=4105 L=4097 C=4105 [G]`
- `10-14 22:00 O=4106 H=4112 L=4103 C=4110 [G]`

- Estado CRT H1: **COMPLETED_BULL** — High H1 4105 alcanzado

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

- **Neural galería:** 60.3% WIN (grade B, conf low) · gate×0.35 → 54% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 60% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** SHORT @ zona resistencia_debil 4107 (precio actual 4110)
- **SL estructural:** 4118 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 4094 | **BE:** mover a BE en 1:1
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
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY**
- **Vol relativo:** 0.37× → banda **muy_bajo** (vol×0.37 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -9.284 · soft-filter vs setup: **alineado**
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

- **Reporte:** `live/xauusd_m5_high_signal.md`
- **Chart:** **Preview en navegador**


---
*high signal | 2026-10-14 22:47 UTC*
