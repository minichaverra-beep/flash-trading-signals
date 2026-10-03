# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-03 18:45 UTC | NY 2026-10-03 14:45 | NY PM 14-16
> Precio **84919.5** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> **Modo:** BREAK — Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **AUTO** |
| Modo setup | **BREAK (breakout)** |

---

### Modo CLI (bias/setup)

- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Sin breakout de nivel detectado

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Alcista
**Reglas:** **4 de 6** (66%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~57%** — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BULLISH a favor +4; acuerdo BAJA -8; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 84820-85007; 0.5=84913 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 87261 | Bull si cierre arriba |
| PDL | 83849 | Bear si cierre abajo |
| 0.5 midpoint | 85555 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | Fondo rojo TORYS-proxy - filtro short |
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

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- RSI TORYS en contra: Fondo rojo TORYS-proxy - filtro short

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **84919.5** |
| Veredicto | **Esperar** (LONG) |
| Entrada óptima | **84871.8** |
| ICT | 84919.5→84871.8 · Refinada 84919.5→84871.8 (FVG BULLISH edge) · Sweep swing_high @ 84942.2 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-16 |
| Plan | Entry **84871.8** · SL **84811.8** · TP **84991.8** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **65%** · ML **51.6%** · Confluencia **BAJA** — 44% · Rules 66%; Neural gated 60% (medium); ML 52% gris; 2M5 no listo; Break operable |
| Historial ref | **btc-058** · 2026-10-03 14:37 NY · Entry **84939.4** · **BUENA** — precio cerca de última Entry + zona OK + bando alineado · (MISMA ZONA) · Δ Entry -67.6 pts (-0.080%) · precio→última 19.9 pts (0.023%) · precio→actual 47.7 pts (0.056%) |
| Bando usado (lado asumido) | **AUTO** |
| Bando mercado (H1) | **BULLISH** |
| R:R | 1:2 |
| Dist. a Entry | -47.7 pts (0.056%) |
| Dist. a SL | -107.7 pts (0.127%) |
| Dist. a TP | +72.3 pts (0.085%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~57% — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BULLISH a favor +4; acuerdo BAJA -8; 66% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +2 (zona a favor) |
| Bias vs dirección | H1 BULLISH a favor +4 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BULLISH** · CLI **AUTO** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.09× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **en contra** · Hist -19.93 · never trigger |
| Watchtower KZ | NY PM 14-16 · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **AUTO** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **84919.5** | Retest **84871.8–85018.6** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.03% de ref | contexto entry @ 84942.2 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 84871.8 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **84871.8** (limit retest o market al cierre 2ª vela) |
| SL | **84811.8** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **84991.8** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 < 84859.5 o breakdown < 84942.2 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 84919.5→84871.8 (FVG BULLISH edge) · Sweep swing_high @ 84942.2 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-16 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 85555.3 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY PM 14-16 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 84942.2 + reclaim |
| FVG alineados | 4 |
| Order blocks | 2 |
| Entrada refinada | **84871.8** (antes 84919.5 · FVG BULLISH edge) |
| Nota | Refinada 84919.5→84871.8 (FVG BULLISH edge) · Sweep swing_high @ 84942.2 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-16 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en resistencia_debil @ 84942.2 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY PM 14-16_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | BEARISH | Fondo rojo TORYS-proxy - filtro short |
| DMI | NEUTRAL | Momentum mixto |
| Swings | HL 84773->84820 | HH 84942->85024 |

---

## M5 detalle

- RSI M5/H1: 52.8 / 72.7
- Zona: resistencia_debil @ 84942
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `17:50 O=84923.6 H=84978.6 L=84923.6 C=84963.8 [G]`
- `17:55 O=84963.8 H=85006.7 L=84945.7 C=84983.2 [G]`
- `18:00 O=84984.2 H=84999.5 L=84962.2 C=84996.4 [G]`
- `18:05 O=84996.9 H=85023.7 L=84973.1 C=84998.3 [G]`
- `18:10 O=84997.4 H=85009.3 L=84945.2 C=84969.3 [R]`
- `18:15 O=84969.4 H=84998.9 L=84923.9 C=84938.9 [R]`
- `18:20 O=84938.4 H=84953.2 L=84922.0 C=84952.1 [G]`
- `18:25 O=84952.4 H=84976.2 L=84947.9 C=84967.6 [G]`
- `18:30 O=84965.9 H=84968.7 L=84934.3 C=84940.6 [R]`
- `18:35 O=84937.5 H=84946.6 L=84899.6 C=84903.6 [R]`
- `18:40 O=84899.1 H=84929.2 L=84899.1 C=84923.3 [G]`
- `18:45 O=84922.9 H=84924.3 L=84917.9 C=84919.5 [R]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 84919 · reloj NY PM 14-16 · CRT PD=NEUTRAL · H1 bias **BULLISH**
- **Setup:** ESPERAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 4/6 (66%)
- **Bando:** AUTO — mercado H1 **BULLISH** guía dirección
- **Veredicto integrado:** ESPERAR — score combinado 60%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 65.0% | 25% | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 51.6% | 18% | grade C; conf=low; → 51% |
| Bonificación ubicación | ×1.03 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 44% | 38% | blend 62/38 con acuerdo BAJA 44% |
| **Probabilidad de éxito** | **60%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 87261: -2341.7 pts (-2.684%)
- **PDL** 83849: +1070.0 pts (+1.276%)

### Premium / Discount 0.5

- Midpoint 0.5: **85555**
- Posición precio: **DISCOUNT** (precio 84919)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-03 16:00 O=84851 H=84866 L=84773 C=84847 [R]`
- `10-03 17:00 O=84847 H=85007 L=84820 C=84983 [G]`
- `10-03 18:00 O=84984 H=85024 L=84899 C=84919 [R]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 84820-85007; 0.5=84913

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
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY PM 14-16**
- **Vol relativo:** 0.09× → banda **muy_bajo** (vol×0.09 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -19.93 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-03 18:45 UTC*
