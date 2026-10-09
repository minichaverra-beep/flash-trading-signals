# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-09 14:15 UTC | NY 2026-10-09 10:15 | NY AM 10-11
> Precio **4188.24** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-09 14:15 UTC** · hace 0 min · fuente MT5 XAUUSDm (broker, M5/H1)
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

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~50%** — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); H1 BULLISH vs SHORT -6; acuerdo BAJA -8; patron WIN similar +3; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4174-4196; 0.5=4185 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4146 | Bull si cierre arriba |
| PDL | 4105 | Bear si cierre abajo |
| 0.5 midpoint | 4126 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 67 OK |
| Rango coherente | ❌ | rango alcista |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓✓ | RSI 66.6 (SHORT: con recorrido a favor) | sin calibrar | n/d | ponderada |
| Zona premium/discount | ✓ | PREMIUM (a favor) | sin calibrar | n/d | ponderada |
| 2 velas M5 confirman | ✗ | no | sin calibrar | n/d | ponderada |
| Rango CRT coherente | ✗ | rango alcista | sin calibrar | n/d | ponderada |
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

- Precio > PDH — no short contra rango alcista CRT

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4188.24** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **4191.64** |
| ICT | 4185.80→4191.64 · Refinada 4185.8→4191.6 (sweep swing_high) · Sweep swing_high @ 4192.6 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |
| Plan | Entry **4191.64** · SL **4197.64** · TP **4179.64** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **73%** · ML **7.2%** · Confluencia **BAJA** — 38% · Rules 66%; Neural gated 65% (medium); ML 7% veto suave; 2M5 no listo; Break con fricción CRT |
| Historial ref | **xauusd-042** · 2026-10-08 11:36 NY · Entry **4115.41** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry +76.23 pts (+1.852%) · precio→última 72.83 pts (1.770%) · precio→actual 3.40 pts (0.081%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BULLISH** |
| R:R | 1:2 |
| Dist. a Entry | +3.40 pts (0.081%) |
| Dist. a SL | +9.40 pts (0.224%) |
| Dist. a TP | -8.60 pts (0.205%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~50% — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); H1 BULLISH vs SHORT -6; acuerdo BAJA -8; patron WIN similar +3; 66% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +2 (zona a favor) |
| Bias vs dirección | H1 BULLISH vs SHORT -6 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BULLISH** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 73% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.03× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist 8.457 · never trigger |
| Watchtower KZ | NY AM 10-11 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BULLISH** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4188.24** | Retest **4182.72–4191.64** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.04% de ref | contexto entry @ 4186.48 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest sweep swing_high @ 4191.64 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **4191.64** (limit retest o market al cierre 2ª vela) |
| SL | **4197.64** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4179.64** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 > 4191.80 o breakout > 4186.48 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4185.8→4191.6 (sweep swing_high) · Sweep swing_high @ 4192.6 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 4125.55 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY AM 10-11 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4192.6 + reclaim |
| FVG alineados | 2 |
| Order blocks | 1 |
| Entrada refinada | **4191.64** (antes 4185.80 · sweep swing_high) |
| Nota | Refinada 4185.8→4191.6 (sweep swing_high) · Sweep swing_high @ 4192.6 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 4186.48 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 10-11_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BULLISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (22/11) |
| Swings | HL 4168->4183 | HH 4193->4196 |

---

## M5 detalle

- RSI M5/H1: 66.6 / 72.8
- Zona: resistencia_debil @ 4186
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `13:20 O=4183.94 H=4187.25 L=4180.15 C=4187.08 [G]`
- `13:25 O=4187.09 H=4189.99 L=4186.49 C=4189.07 [G]`
- `13:30 O=4188.77 H=4192.55 L=4185.14 C=4186.28 [R]`
- `13:35 O=4186.34 H=4190.68 L=4183.56 C=4186.65 [G]`
- `13:40 O=4186.79 H=4191.76 L=4182.60 C=4184.82 [R]`
- `13:45 O=4185.05 H=4191.47 L=4184.84 C=4190.27 [G]`
- `13:50 O=4190.32 H=4196.25 L=4189.40 C=4191.92 [G]`
- `13:55 O=4191.97 H=4196.41 L=4189.79 C=4190.48 [R]`
- `14:00 O=4190.36 H=4191.29 L=4185.48 C=4185.70 [R]`
- `14:05 O=4185.69 H=4189.85 L=4184.76 C=4185.63 [R]`
- `14:10 O=4185.76 H=4189.09 L=4184.94 C=4188.10 [G]`
- `14:15 O=4188.41 H=4188.61 L=4187.84 C=4188.24 [R]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 67 OK |
| Rango coherente | NO | rango alcista |
| DMI alineado | NO | +DI domina (22/11) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4188 · reloj NY AM 10-11 · CRT PD=BULLISH · H1 bias **BULLISH**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **BULLISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 41%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango alcista |
| Neural galería (gated) | 73.1% | 25% | alineado WIN; conf=medium; gate×0.65 → 65% |
| ML tabular (gated) | 7.2% | 18% | grade C; conf=high; → 7% |
| Penalización dirección | ×0.88 | — | penalización H1 BULLISH vs SHORT |
| Bonificación ubicación | ×1.03 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 38% | 38% | blend 62/38 con acuerdo BAJA 38% |
| **Probabilidad de éxito** | **41%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4146: +42.3 pts (+1.021%)
- **PDL** 4105: +83.1 pts (+2.023%)

### Premium / Discount 0.5

- Midpoint 0.5: **4126**
- Posición precio: **PREMIUM** (precio 4188)
- Lectura PD: **BULLISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-09 12:00 O=4183 H=4192 L=4168 C=4175 [R]`
- `10-09 13:00 O=4175 H=4196 L=4174 C=4190 [G]`
- `10-09 14:00 O=4190 H=4191 L=4185 C=4188 [R]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 4174-4196; 0.5=4185

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar |  |
| Cierre > PDH | Sesgo alcista — long pullback | **→** |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 |  |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** CONFLICT

- Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual fuerte pero features ML desfavorables; priorizar Rules % + CRT

- **Neural galería:** 73.1% WIN (grade B, conf medium) · gate×0.65 → 65% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 73% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)
- ⚠ Tensión ML/Neural — no entrar por galería sola

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 10-11**
- **Vol relativo:** 0.03× → banda **muy_bajo** (vol×0.03 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 8.457 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-09 14:15 UTC*
