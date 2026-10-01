# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-01 14:31 UTC | NY 2026-10-01 10:31 | NY AM 10-11
> Precio **4163.50** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-01 14:21 UTC** · hace 10 min · fuente yfinance (GC=F, M5=5m) · ajustado a spot gold-api (basis +23.90)
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
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~48%** — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patron LOSS similar -12; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4157-4172; 0.5=4165 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4227 | Bull si cierre arriba |
| PDL | 4154 | Bear si cierre abajo |
| 0.5 midpoint | 4191 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 32 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

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

- Dirección: **Long** @ 4164
- SL estructura: **4155** | TP: **4180** (R:R 1:2)
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
| Precio | **4163.50** |
| Veredicto | **Entrar** (LONG) |
| Entrada óptima | **4165.57** |
| ICT | Base 4165.6 (zona base) · Sweep swing_high @ 4172.4 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 10-11 |
| Plan | Entry **4165.57** · SL **4159.57** · TP **4177.57** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **55%** · ML **45.6%** · Confluencia **BAJA** — 44% · Rules 83%; Neural débil/gating 55% conf=low; ML 46% gris; 2M5 no listo; Break operable |
| Historial ref | **xauusd-012** · 2026-10-01 10:19 NY · Entry **4190.32** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry -24.74 pts (-0.590%) · precio→última 26.82 pts (0.640%) · precio→actual 2.07 pts (0.050%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | +2.07 pts (0.050%) |
| Dist. a SL | -3.93 pts (0.094%) |
| Dist. a TP | +14.07 pts (0.338%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~48% — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patron LOSS similar -12; 83% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +2 (zona a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. low · 55% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.00× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist 5.641 · never trigger |
| Watchtower KZ | NY AM 10-11 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4163.50** | Retest **4164.90–4168.65** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.03% de ref | contexto entry @ 4164.90 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 4164.90–4168.65 (soporte_debil @ 4164.90) + 2 velas M5 verdes consecutivas en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **4165.57** (limit retest o market al cierre 2ª vela) |
| SL | **4159.57** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4177.57** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 < 4159.57 o breakdown < 4164.90 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 4165.6 (zona base) · Sweep swing_high @ 4172.4 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 4190.75 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY AM 10-11 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4172.4 + reclaim |
| FVG alineados | 5 |
| Order blocks | 1 |
| Entrada | **4165.57** (zona base · sin cambio) |
| Nota | Base 4165.6 (zona base) · Sweep swing_high @ 4172.4 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 4164.90 | **VÁLIDO** — Últimas 2 verdes en zona ≤0.15% | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 10-11_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (32/15) |
| Swings | LL 4165->4157 | LH 4194->4172 |

---

## M5 detalle

- RSI M5/H1: 32.1 / 50.5
- Zona: soporte_debil @ 4165
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `13:30 O=4173.40 H=4178.50 L=4172.00 C=4174.10 [G]`
- `13:35 O=4173.80 H=4174.50 L=4169.80 C=4169.80 [R]`
- `13:40 O=4169.70 H=4170.30 L=4164.90 C=4168.70 [R]`
- `13:45 O=4168.80 H=4171.40 L=4167.50 C=4167.60 [R]`
- `13:50 O=4167.50 H=4171.50 L=4167.10 C=4169.30 [G]`
- `13:55 O=4169.30 H=4171.70 L=4166.10 C=4171.20 [G]`
- `14:00 O=4171.50 H=4172.40 L=4159.80 C=4160.00 [R]`
- `14:05 O=4160.20 H=4168.10 L=4157.30 C=4166.70 [G]`
- `14:10 O=4166.80 H=4166.90 L=4156.90 C=4159.70 [R]`
- `14:15 O=4159.50 H=4164.20 L=4159.40 C=4162.30 [G]`
- `14:20 O=4162.20 H=4164.80 L=4161.50 C=4162.30 [G]`
- `14:21 O=4163.50 H=4163.50 L=4163.50 C=4163.50 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 32 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | -DI domina (32/15) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4164 · reloj NY AM 10-11 · CRT PD=NEUTRAL · H1 bias **BEARISH**
- **Setup:** ENTRAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — score combinado 56%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 54.5% | 25% | no alineado; conf=low; gate×0.35 → 52% |
| ML tabular (gated) | 45.6% | 18% | grade C; conf=low; → 48% |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.03 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 44% | 38% | blend 62/38 con acuerdo BAJA 44% |
| **Probabilidad de éxito** | **56%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4227: -63.7 pts (-1.507%)
- **PDL** 4154: +9.2 pts (+0.221%)

### Premium / Discount 0.5

- Midpoint 0.5: **4191**
- Posición precio: **DISCOUNT** (precio 4164)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-01 13:00 O=4185 H=4188 L=4165 C=4171 [R]`
- `10-01 14:00 O=4172 H=4172 L=4157 C=4162 [R]`
- `10-01 14:21 O=4164 H=4164 L=4164 C=4164 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 4157-4172; 0.5=4165

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

- **Neural galería:** 54.5% WIN (grade B, conf low) · gate×0.35 → 52% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 55% | contra-bias, LOSS |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** LONG @ zona soporte_debil 4165 (precio actual 4164)
- **SL estructural:** 4155 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 4180 | **BE:** mover a BE en 1:1
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

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 10-11**
- **Vol relativo:** 0.00× → banda **muy_bajo** (vol×0.00 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 5.641 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-01 14:31 UTC*
