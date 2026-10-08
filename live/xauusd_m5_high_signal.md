# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-08 13:25 UTC | NY 2026-10-08 09:25 | NY AM 08-10
> Precio **4123.87** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-08 13:25 UTC** · hace 0 min · fuente MT5 XAUUSDm (broker, M5/H1)
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
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **90%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~72%** — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo MEDIA -2; patron WIN similar +3; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4113-4132; 0.5=4123 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4170 | Bull si cierre arriba |
| PDL | 4066 | Bear si cierre abajo |
| 0.5 midpoint | 4118 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 48 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓ | RSI 48.3 (SHORT: neutral) | sin calibrar | n/d | ponderada |
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
| Precio | **4123.87** |
| Veredicto | **Esperar** (SHORT) |
| Entrada óptima | **4125.69** |
| ICT | 4122.59→4125.69 · Refinada 4122.6→4125.7 (FVG BEARISH edge) · Sweep swing_high @ 4129.3 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 08-10 |
| Plan | Entry **4125.69** · SL **4131.69** · TP **4113.69** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **66%** · ML **14.2%** · Confluencia **MEDIA** — 50% · Rules 83%; Neural gated 60% (medium); ML 14% veto suave; 2M5 no listo; Break operable |
| Historial ref | **xauusd-040** · 2026-10-07 16:15 NY · Entry **4102.67** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry +23.02 pts (+0.561%) · precio→última 21.20 pts (0.517%) · precio→actual 1.82 pts (0.044%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +1.82 pts (0.044%) |
| Dist. a SL | +7.82 pts (0.190%) |
| Dist. a TP | -10.18 pts (0.247%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~72% — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo MEDIA -2; patron WIN similar +3; 83% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +2 (zona a favor) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **90%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 66% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.04× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist -0.243 · never trigger |
| Watchtower KZ | NY AM 08-10 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4123.87** | Retest **4119.54–4125.69** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.02% de ref | contexto entry @ 4123.26 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 4125.69 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **4125.69** (limit retest o market al cierre 2ª vela) |
| SL | **4131.69** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4113.69** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 > 4128.59 o breakout > 4123.26 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4122.6→4125.7 (FVG BEARISH edge) · Sweep swing_high @ 4129.3 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 08-10 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 4117.99 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY AM 08-10 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4129.3 + reclaim |
| FVG alineados | 5 |
| Order blocks | 2 |
| Entrada refinada | **4125.69** (antes 4122.59 · FVG BEARISH edge) |
| Nota | Refinada 4122.6→4125.7 (FVG BEARISH edge) · Sweep swing_high @ 4129.3 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 08-10 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 4123.26 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 08-10_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **SHORT**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | Momentum mixto | **NEUTRAL** |
| CRT PD / Premium-Discount | NEUTRAL · PREMIUM | **SHORT** |
| Estructura swings M5 | LL 4119->4113 · LH 4132->4129 | **SHORT** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 4119->4113 | LH 4132->4129 |

---

## M5 detalle

- RSI M5/H1: 48.3 / 60.1
- Zona: resistencia_debil @ 4123
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `12:30 O=4131.20 H=4131.38 L=4120.95 C=4121.53 [R]`
- `12:35 O=4121.69 H=4125.60 L=4120.39 C=4122.53 [G]`
- `12:40 O=4122.52 H=4123.95 L=4118.12 C=4119.39 [R]`
- `12:45 O=4119.19 H=4119.66 L=4117.09 C=4117.96 [R]`
- `12:50 O=4117.90 H=4118.39 L=4113.15 C=4118.10 [G]`
- `12:55 O=4118.05 H=4118.97 L=4115.95 C=4118.59 [G]`
- `13:00 O=4118.53 H=4121.14 L=4115.21 C=4119.19 [G]`
- `13:05 O=4119.25 H=4127.89 L=4118.48 C=4125.49 [G]`
- `13:10 O=4125.55 H=4129.34 L=4124.58 C=4126.33 [G]`
- `13:15 O=4126.43 H=4126.92 L=4122.53 C=4123.33 [R]`
- `13:20 O=4123.31 H=4127.32 L=4122.68 C=4124.10 [G]`
- `13:25 O=4124.16 H=4124.51 L=4123.47 C=4123.87 [R]`

---

## Score reglas extendidas (90%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 48 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4124 · reloj NY AM 08-10 · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** ESPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score combinado 62%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 90% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 66.0% | 25% | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 14.2% | 18% | grade C; conf=high; → 14% |
| Bonificación ubicación | ×1.03 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 50% | 38% | blend 62/38 con acuerdo MEDIA 50% |
| **Probabilidad de éxito** | **62%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4170: -45.8 pts (-1.099%)
- **PDL** 4066: +57.6 pts (+1.416%)

### Premium / Discount 0.5

- Midpoint 0.5: **4118**
- Posición precio: **PREMIUM** (precio 4124)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-08 11:00 O=4122 H=4131 L=4115 C=4125 [G]`
- `10-08 12:00 O=4125 H=4132 L=4113 C=4119 [R]`
- `10-08 13:00 O=4119 H=4129 L=4115 C=4124 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 4113-4132; 0.5=4123

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

- **Neural galería:** 66.0% WIN (grade B, conf medium) · gate×0.65 → 60% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 66% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 08-10**
- **Vol relativo:** 0.04× → banda **muy_bajo** (vol×0.04 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -0.243 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-08 13:25 UTC*
