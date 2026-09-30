# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-30 14:36 UTC | NY 2026-09-30 10:36 | NY AM 10-11
> Precio **4204.00** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-09-30 14:26 UTC** · hace 10 min · fuente yfinance (GC=F, M5=5m)
> **Modo:** BULLISH + REVERSE — Bias CLI **BULLISH** — setup re-puntuado como LONG
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **BULLISH** |
| Modo setup | **REVERSE (E2)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BULLISH** — setup re-puntuado como LONG
- ⚠ H1 bajista vs bias forzado — confirmar en TV antes de entrar
- Setup **REVERSE** — turtle soup / PDH-PDL fakeout / sweep+reclaim
- E2: E2_NO (1/6) · operable=NO · WR ~61%

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **4 de 6** (66%) | Extendidas: **60%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~48%** — histórico E2 reversión BTC · LONG en PREMIUM -7 (E2 vs zona); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patrones mixtos -4; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4201-4215; 0.5=4208 |
| Fakeout PDH | SÍ — NO LONG | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4220 | Bull si cierre arriba |
| PDL | 4145 | Bear si cierre abajo |
| 0.5 midpoint | 4182 | Filtro 50% |

**Nota CRT:** Fakeout PDH: NO long E1; CRT invalid bearish | REVERSE: fakeout PDH — turtle soup bajista posible

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 18 OK |
| Rango coherente | ❌ | trampa en máximo ayer — no long |

### Turtle Soup E2

Score **1/6** | Operable: **NO** | Winrate: **~61%**
_Modo REVERSE: falta 2 velas M5 misma dirección del bando — no operable aún (WR E2 ~61% si se confirma)_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | NO | Sweep liquidez |
| 3. Reclaim agresivo | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | NO | Cerca nivel barrido |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | NO | Esperar 2 velas alineadas |
| 8. Winrate E2 | SÍ | ~61% |

### Red flags

- Fakeout PDH — NO long E1; CRT invalid bearish
- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- RSI M5 18.4 sobrevendido — filtro TORYS-like
- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: REVERSE turtle soup PDH sweep
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4204.00** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **4208.48** |
| ICT | Base 4208.5 (zona base) · Sweep PDH @ 4219.7 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |
| Plan | Entry **4208.48** · SL **4202.48** · TP **4220.48** |
| E2 / Break | REVERSE / E2 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **64%** · ML **72.1%** · Confluencia **BAJA** — 36% · Rules 66%; Neural débil/gating 64% conf=low; ML 72% (medium); 2M5 no listo; E2 no operable |
| Historial ref | **xauusd-009** · 2026-09-30 10:32 NY · Entry **4207.50** · **REGULAR** — precio cerca de última Entry; sin 2M5; zona OK · (MISMA ZONA) · Δ Entry +0.98 pts (+0.023%) · precio→última 3.50 pts (0.083%) · precio→actual 4.48 pts (0.106%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | +4.48 pts (0.107%) |
| Dist. a SL | -1.52 pts (0.036%) |
| Dist. a TP | +16.48 pts (0.392%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~48% — histórico E2 reversión BTC · LONG en PREMIUM -7 (E2 vs zona); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patrones mixtos -4; 66% reglas |
| Zona PD vs dirección | LONG en PREMIUM -7 (E2 vs zona) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **60%** |
| Estado 2M5 | Falta 2M5 — ESPERAR |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Neural grade/conf | **B** · conf. low · 64% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.00× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist 8.026 · never trigger |
| Watchtower KZ | NY AM 10-11 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **REVERSE (E2)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4204.00** | Retest **4207.80–4211.59** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.09% de ref | contexto entry @ 4207.80 |
| Acción | **ESPERAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 4207.80–4211.59 (soporte_debil @ 4207.80) + 2 velas M5 verdes consecutivas en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **4208.48** (limit retest o market al cierre 2ª vela) |
| SL | **4202.48** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4220.48** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 < 4202.48 o breakdown < 4207.80 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 4208.5 (zona base) · Sweep PDH @ 4219.7 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ⚠️ |
| 0.5 midpoint | 4182.45 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY AM 10-11 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDH @ 4219.7 + reclaim |
| FVG alineados | 5 |
| Order blocks | 2 |
| Entrada | **4208.48** (zona base · sin cambio) |
| Nota | Base 4208.5 (zona base) · Sweep PDH @ 4219.7 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 4207.80 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 10-11_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [❌] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (27/6) |
| Swings | HL 4208->4214 | HH 4226->4251 |

---

## M5 detalle

- RSI M5/H1: 18.4 / 50.2
- Zona: soporte_debil @ 4208
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `13:35 O=4224.10 H=4225.20 L=4215.10 C=4217.70 [R]`
- `13:40 O=4217.80 H=4219.60 L=4213.10 C=4214.80 [R]`
- `13:45 O=4214.50 H=4216.50 L=4208.60 C=4211.90 [R]`
- `13:50 O=4211.90 H=4214.20 L=4207.50 C=4213.90 [G]`
- `13:55 O=4213.90 H=4215.40 L=4208.40 C=4208.60 [R]`
- `14:00 O=4208.80 H=4210.60 L=4205.40 C=4209.90 [G]`
- `14:05 O=4210.00 H=4214.60 L=4206.70 C=4212.70 [G]`
- `14:10 O=4212.60 H=4215.00 L=4209.60 C=4211.50 [R]`
- `14:15 O=4211.40 H=4214.10 L=4204.30 C=4208.30 [R]`
- `14:20 O=4208.40 H=4211.40 L=4203.40 C=4204.80 [R]`
- `14:25 O=4205.00 H=4205.20 L=4201.00 C=4204.30 [R]`
- `14:26 O=4204.00 H=4204.00 L=4204.00 C=4204.00 [G]`

---

## Score reglas extendidas (60%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 18 OK |
| Rango coherente | NO | trampa en máximo ayer — no long |
| DMI alineado | NO | -DI domina (27/6) |
| 0.5 midpoint E1 | NO | premium — no long E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4204 · reloj NY AM 10-11 · CRT PD=NEUTRAL · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **REVERSE** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 39%
- **E2 contexto:** E2_NO (1/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 60% | 12% | meta >70% |
| CRT coherence | fail | 12% | trampa en máximo ayer — no long |
| Neural galería (gated) | 63.9% | 25% | no alineado; conf=low; gate×0.35 → 55% |
| ML tabular (gated) | 72.1% | 18% | grade A+; conf=medium; → 67% |
| E2 turtle | 1/6 | 5% | E2_NO |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Penalización ubicación | ×0.88 | — | LONG en PREMIUM |
| Acuerdo entre capas | 36% | 38% | blend 62/38 con acuerdo BAJA 36% |
| **Probabilidad de éxito** | **39%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4220: -15.7 pts (-0.372%)
- **PDL** 4145: +58.8 pts (+1.419%)

### Premium / Discount 0.5

- Midpoint 0.5: **4182**
- Posición precio: **PREMIUM** (precio 4204)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

1. Wick M5 superó PDH en últimas ~18 velas
2. Precio actual **por debajo** de PDH → trampa alcista
3. **Acción:** NO long E1 · CRT invalid bearish · posible short en reclaim

### Timeline H1 (últimas 3 velas)

- `09-30 13:00 O=4240 H=4246 L=4208 C=4209 [R]`
- `09-30 14:00 O=4209 H=4215 L=4201 C=4204 [R]`
- `09-30 14:26 O=4204 H=4204 L=4204 C=4204 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 4201-4215; 0.5=4208

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar | **→** |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 | **→** |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## D) E2 Turtle Soup expandido

| # | Check | OK | Evidencia |
|---|-------|----|-----------|
| 1. Reversion MACRO | ❌ | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | ❌ | NO | Sweep liquidez |
| 3. Reclaim agresivo | ❌ | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | ❌ | NO | Cerca nivel barrido |
| 5. SL grande E2 | ❌ | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | ❌ | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | ❌ | NO | Esperar 2 velas alineadas |
| 8. Winrate E2 | ✅ | SÍ | ~61% |

**Score:** 1/6 · Veredicto: **E2_NO**

### Interpretación fakeout PDL/PDH

- **Fakeout PDH:** sweep sobre máximo ayer sin hold → watchlist turtle soup SHORT (solo demo)

### Decisión E2: **NO ENTRAR** — setup Reverse incompleto · WR ~61%

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 63.9% WIN (grade B, conf low) · gate×0.35 → 55% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: REVERSE turtle soup PDH sweep | — | 64% | sweep+reclaim, WIN |
| 2 | LOSS: fakeout (BTC-22-05-26) | BTC-22-05-26.png | 59% | fakeout, LOSS |
| 3 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 54% | contra-bias, LOSS |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 10-11**
- **Vol relativo:** 0.00× → banda **muy_bajo** (vol×0.00 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 8.026 · soft-filter vs setup: **alineado**
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
*high signal | 2026-09-30 14:36 UTC*
