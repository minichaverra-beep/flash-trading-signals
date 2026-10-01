# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-01 23:26 UTC | NY 2026-10-01 19:26 | FUERA_NY (Asia)
> Precio **4179.89** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-01 23:25 UTC** · hace 1 min · fuente MT5 XAUUSDm (broker, M5/H1)
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **AUTO** |
| Modo setup | **AUTO** |

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Alcista
**Reglas:** **4 de 6** (66%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~63%** — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BULLISH a favor +4; acuerdo MEDIA -2; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **COMPLETED_BULL** | High H1 4179 alcanzado |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4219 | Bull si cierre arriba |
| PDL | 4147 | Bear si cierre abajo |
| 0.5 midpoint | 4183 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | RSI 77 sobrecomprado |
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

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- RSI M5 77.5 sobrecomprado — filtro TORYS-like

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4179.89** |
| Veredicto | **Esperar** (LONG) |
| Entrada óptima | **4177.11** |
| ICT | 4179.89→4177.11 · Refinada 4179.9→4177.1 (FVG BULLISH edge) · Sweep swing_high @ 4178.9 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL |
| Plan | Entry **4177.11** · SL **4171.11** · TP **4189.11** |
| E2 / Break | Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **72%** · ML **91.6%** · Confluencia **MEDIA** — 50% · Rules 66%; Neural gated 64% (medium); ML 92% (high); 2M5 no listo; Setup auto con dirección |
| Historial ref | **xauusd-015** · 2026-10-01 12:51 NY · Entry **4163.90** · **BUENA** — precio cerca de Entry actual + zona OK + bando alineado · (MÁS CERCA) · Δ Entry +13.21 pts (+0.317%) · precio→última 15.99 pts (0.384%) · precio→actual 2.79 pts (0.067%) |
| Bando usado (lado asumido) | **AUTO** |
| Bando mercado (H1) | **BULLISH** |
| R:R | 1:2 |
| Dist. a Entry | -2.79 pts (0.067%) |
| Dist. a SL | -8.79 pts (0.210%) |
| Dist. a TP | +9.21 pts (0.220%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~63% — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BULLISH a favor +4; acuerdo MEDIA -2; 66% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +2 (zona a favor) |
| Bias vs dirección | H1 BULLISH a favor +4 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BULLISH** · CLI **AUTO** |
| Calidad break/reverse | AUTO |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.20× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist 6.673 · never trigger |
| Watchtower KZ | FUERA_NY (Asia) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **AUTO** + **AUTO** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4179.89** | Retest **4177.11–4183.71** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.00% de ref | contexto entry @ 4179.95 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 4177.11 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **4177.11** (limit retest o market al cierre 2ª vela) |
| SL | **4171.11** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4189.11** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 < 4173.89 o breakdown < 4179.95 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4179.9→4177.1 (FVG BULLISH edge) · Sweep swing_high @ 4178.9 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 4183.39 |
| H1 CRT state | **COMPLETED_BULL** |
| Killzone / sesión | FUERA_NY (Asia) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4178.9 + reclaim |
| FVG alineados | 5 |
| Order blocks | 3 |
| Entrada refinada | **4177.11** (antes 4179.89 · FVG BULLISH edge) |
| Nota | Refinada 4179.9→4177.1 (FVG BULLISH edge) · Sweep swing_high @ 4178.9 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en resistencia_debil @ 4179.95 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

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

| CRT | COMPLETED_BULL/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (11/3) |
| Swings | LL 4173->4172 | LH 4180->4179 |

---

## M5 detalle

- RSI M5/H1: 77.5 / 66.2
- Zona: resistencia_debil @ 4180
- 2M5 LONG: NO | SHORT: SÍ

### 12 velas M5

- `22:30 O=4172.08 H=4175.48 L=4171.63 C=4175.25 [G]`
- `22:35 O=4175.26 H=4176.18 L=4174.80 C=4175.45 [G]`
- `22:40 O=4175.31 H=4176.23 L=4175.15 C=4175.89 [G]`
- `22:45 O=4175.86 H=4176.57 L=4175.34 C=4175.34 [R]`
- `22:50 O=4175.43 H=4176.70 L=4175.23 C=4176.70 [G]`
- `22:55 O=4176.48 H=4178.96 L=4176.23 C=4178.64 [G]`
- `23:00 O=4178.63 H=4179.36 L=4177.98 C=4178.99 [G]`
- `23:05 O=4179.10 H=4179.13 L=4177.58 C=4178.65 [R]`
- `23:10 O=4178.41 H=4180.70 L=4178.40 C=4179.81 [G]`
- `23:15 O=4179.81 H=4182.16 L=4179.35 C=4182.02 [G]`
- `23:20 O=4182.08 H=4182.98 L=4179.97 C=4180.25 [R]`
- `23:25 O=4180.37 H=4181.02 L=4179.71 C=4179.89 [R]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | RSI 77 sobrecomprado |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF |
| DMI alineado | SÍ | +DI domina (11/3) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4180 · reloj FUERA_NY (Asia) · CRT PD=NEUTRAL · H1 bias **BULLISH**
- **Setup:** ESPERAR LONG · dirección **LONG** · modo **AUTO** · reglas E1 4/6 (66%)
- **Bando:** AUTO — mercado H1 **BULLISH** guía dirección
- **Veredicto integrado:** ESPERAR — score 68% requiere confirmación TV

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF |
| Neural galería (gated) | 72.0% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 91.6% | 18% | grade A+; conf=high; → 92% |
| Bonificación ubicación | ×1.03 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 50% | 38% | blend 62/38 con acuerdo MEDIA 50% |
| **Probabilidad de éxito** | **68%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4219: -39.5 pts (-0.937%)
- **PDL** 4147: +32.6 pts (+0.785%)

### Premium / Discount 0.5

- Midpoint 0.5: **4183**
- Posición precio: **DISCOUNT** (precio 4180)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-01 20:00 O=4176 H=4180 L=4173 C=4177 [G]`
- `10-01 22:00 O=4176 H=4179 L=4172 C=4179 [G]`
- `10-01 23:00 O=4179 H=4183 L=4178 C=4180 [G]`

- Estado CRT H1: **COMPLETED_BULL** — High H1 4179 alcanzado

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

**Acuerdo Rules/Neural:** ALIGNED

- ML y Neural apuntan misma dirección de confianza

- **Neural galería:** 72.0% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | Esperar setup A+ galeria WIN | — | 72% | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY (Asia)**
- **Vol relativo:** 0.20× → banda **muy_bajo** (vol×0.20 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 6.673 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-01 23:26 UTC*
