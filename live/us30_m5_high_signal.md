# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-02 16:29 UTC | NY 2026-10-02 12:29 | FUERA_NY (Lunch)
> Precio **51110.5** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> **Modo:** BEARISH + REVERSE — Bias CLI **BEARISH** — setup re-puntuado como SHORT
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **BEARISH** |
| Modo setup | **REVERSE (E2)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BEARISH** — setup re-puntuado como SHORT
- Setup **REVERSE** — turtle soup / PDH-PDL fakeout / sweep+reclaim
- E2: E2_WATCH (4/6) · operable=NO · WR ~61%

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario | E2 watch only
**Tendencia:** Sin dirección
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~51%** — histórico E2 reversión BTC · SHORT en PREMIUM +4 (E2 a favor); H1 BEARISH a favor +4; acuerdo BAJA -8; patrones mixtos -4; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 50972-51243; 0.5=51107 |
| Fakeout PDH | SÍ — NO LONG | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 51237 | Bull si cierre arriba |
| PDL | 50578 | Bear si cierre abajo |
| 0.5 midpoint | 50908 | Filtro 50% |

**Nota CRT:** Fakeout PDH: NO long E1; CRT invalid bearish | REVERSE: fakeout PDH — turtle soup bajista posible

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Turtle Soup E2

Score **4/6** | Operable: **NO** | Winrate: **~61%**
_Modo REVERSE: falta 2 velas M5 misma dirección del bando — no operable aún (WR E2 ~61% si se confirma)_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | SÍ | Sweep swing low + reclaim |
| 3. Reclaim agresivo | SÍ | Reclaim M5 |
| 4. Entrada zona SL original | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | NO | Esperar 2 velas alineadas |
| 8. Winrate E2 | SÍ | ~61% |

### Red flags

- Fakeout PDH — NO long E1; CRT invalid bearish
- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- RSI TORYS en contra: Fondo verde TORYS-proxy - filtro long

### Galería (cross-ref)

- Patrón ganador similar: REVERSE turtle soup PDH sweep
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **51110.5** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **51126.9** |
| ICT | 51110.5→51126.9 · Refinada 51110.5→51126.9 (FVG BEARISH edge) · Sweep PDH @ 51236.8 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |
| Plan | Entry **51126.9** · SL **51186.9** · TP **51006.9** |
| E2 / Break | REVERSE / E2 — Vigilar reversión E2 — E1 primario | E2 watch only |
| Métricas | Rules **66%** · Neural **72%** · ML **0.0%** · Confluencia **BAJA** — 36% · Rules 66%; Neural gated 64% (medium); ML 0% veto suave; 2M5 no listo; E2 watch |
| Historial ref | **us30-045** · 2026-10-02 09:43 NY · Entry **51390.4** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry -263.5 pts (-0.513%) · precio→última 279.9 pts (0.545%) · precio→actual 16.4 pts (0.032%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | +16.4 pts (0.032%) |
| Dist. a SL | +76.4 pts (0.149%) |
| Dist. a TP | -103.6 pts (0.203%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~51% — histórico E2 reversión BTC · SHORT en PREMIUM +4 (E2 a favor); H1 BEARISH a favor +4; acuerdo BAJA -8; patrones mixtos -4; 66% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +4 (E2 a favor) |
| Bias vs dirección | H1 BEARISH a favor +4 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BEARISH** |
| Calidad break/reverse | REVERSE watch (E2_WATCH) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **bajo** · 0.61× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist 21.63 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **REVERSE (E2)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **51110.5** | Retest **51069.9–51126.9** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.01% de ref | contexto entry @ 51115.9 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 51126.9 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **51126.9** (limit retest o market al cierre 2ª vela) |
| SL | **51186.9** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **51006.9** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 51170.5 o breakout > 51115.9 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 51110.5→51126.9 (FVG BEARISH edge) · Sweep PDH @ 51236.8 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 50907.7 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDH @ 51236.8 + reclaim |
| FVG alineados | 5 |
| Order blocks | 2 |
| Entrada refinada | **51126.9** (antes 51110.5 · FVG BEARISH edge) |
| Nota | Refinada 51110.5→51126.9 (FVG BEARISH edge) · Sweep PDH @ 51236.8 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 51115.9 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | BULL | +DI domina (218/130) |
| Swings | HL 50972->51096 | LH 51162->51160 |

---

## M5 detalle

- RSI M5/H1: 62.7 / 53.0
- Zona: soporte_debil @ 51116
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `15:30 O=51090.5 H=51128.5 L=51047.5 C=51126.5 [G]`
- `15:35 O=51125.5 H=51158.5 L=51113.5 C=51146.5 [G]`
- `15:40 O=51147.5 H=51162.5 L=51113.5 C=51121.2 [R]`
- `15:45 O=51120.2 H=51139.2 L=51107.9 C=51118.2 [R]`
- `15:50 O=51117.2 H=51142.2 L=51101.2 C=51113.2 [R]`
- `15:55 O=51112.2 H=51130.2 L=51096.2 C=51125.5 [G]`
- `16:00 O=51126.5 H=51160.5 L=51101.5 C=51131.5 [G]`
- `16:05 O=51132.5 H=51150.5 L=51104.5 C=51144.5 [G]`
- `16:10 O=51145.5 H=51152.5 L=51099.5 C=51121.5 [R]`
- `16:15 O=51120.5 H=51155.5 L=51105.5 C=51138.5 [G]`
- `16:20 O=51137.5 H=51147.5 L=51095.5 C=51104.5 [R]`
- `16:25 O=51103.5 H=51131.5 L=51091.5 C=51110.5 [G]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | +DI domina (218/130) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 51110 · reloj FUERA_NY (Lunch) · CRT PD=NEUTRAL · H1 bias **BEARISH**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **REVERSE** · reglas E1 4/6 (66%)
- **Bando:** CLI y H1 alineados (**BEARISH**)
- **Veredicto integrado:** NO_OPERAR — score combinado 52%
- **E2 contexto:** E2_WATCH (4/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 0.0% | 18% | grade C; conf=high; → 0% |
| E2 turtle | 4/6 | 5% | E2_WATCH |
| Bonificación ubicación | ×1.06 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 36% | 38% | blend 62/38 con acuerdo BAJA 36% |
| **Probabilidad de éxito** | **52%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 51237: -126.3 pts (-0.247%)
- **PDL** 50578: +532.0 pts (+1.052%)

### Premium / Discount 0.5

- Midpoint 0.5: **50908**
- Posición precio: **PREMIUM** (precio 51110)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

1. Wick M5 superó PDH en últimas ~18 velas
2. Precio actual **por debajo** de PDH → trampa alcista
3. **Acción:** NO long E1 · CRT invalid bearish · posible short en reclaim

### Timeline H1 (últimas 3 velas)

- `10-02 14:00 O=51206 H=51308 L=51138 C=51228 [G]`
- `10-02 15:00 O=51229 H=51243 L=50972 C=51126 [R]`
- `10-02 16:00 O=51126 H=51160 L=51092 C=51110 [R]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 50972-51243; 0.5=51107

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
| 2. Rompe min/max previo | ✅ | SÍ | Sweep swing low + reclaim |
| 3. Reclaim agresivo | ✅ | SÍ | Reclaim M5 |
| 4. Entrada zona SL original | ✅ | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | ❌ | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | ❌ | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | ❌ | NO | Esperar 2 velas alineadas |
| 8. Winrate E2 | ✅ | SÍ | ~61% |

**Score:** 4/6 · Veredicto: **E2_WATCH**

### Interpretación fakeout PDL/PDH

- **Fakeout PDH:** sweep sobre máximo ayer sin hold → watchlist turtle soup SHORT (solo demo)

### Decisión E2: **Observar** — falta confirmación 2 velas o checklist incompleto · WR ~61%

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** CONFLICT

- Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual fuerte pero features ML desfavorables; priorizar Rules % + CRT

- **Neural galería:** 71.8% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: REVERSE turtle soup PDH sweep | — | 72% | sweep+reclaim, WIN |
| 2 | LOSS: fakeout (BTC-22-05-26) | BTC-22-05-26.png | 67% | fakeout, LOSS |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY (Lunch)**
- **Vol relativo:** 0.61× → banda **bajo** (vol×0.61 ≤ bajo 0.7)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 21.63 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-02 16:29 UTC*
