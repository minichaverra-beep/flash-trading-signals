# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-08 15:49 UTC | NY 2026-09-08 11:49 | FUERA_NY
> Precio **52873.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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
**Reglas:** **6 de 7** (85%) | Extendidas: **80%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~82%** — histórico E1 BTC (85% reglas OK)

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **n/a** | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | n/a | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 52864-52943; 0.5=52904 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.017% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 67 OK |
| Rango coherente | ✅ | Modo BREAK: breakout de nivel/estructura |

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

- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **52873.0** |
| Veredicto | **Esperar** (SHORT) |
| Entrada óptima | **52911.0** |
| ICT | 52836.2→52911.0 · Refinada 52836.2→52911.0 (FVG BEARISH edge) · Sweep swing_high @ 52943.0 + reclaim · H1 INSIDE_RANGE |
| Plan | Entry **52911.0** · SL **53022.6** · TP **52687.8** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **85%** · Neural **72%** · ML **28.5%** · Confluencia **MEDIA** — 64% · Rules 85%; Neural gated 64% (medium); ML 29% veto suave; 2M5 o zona parcial |
| Historial ref | **us30-022** · 2026-09-08 11:40 NY · Entry **52852.0** · **BUENA** — precio cerca de última Entry + zona OK + bando alineado · (MISMA ZONA) · Δ Entry +59.0 pts (+0.112%) · precio→última 21.0 pts (0.040%) · precio→actual 38.0 pts (0.072%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | +38.0 pts (0.072%) |
| Dist. a SL | +149.6 pts (0.283%) |
| Dist. a TP | -185.2 pts (0.350%) |
| Riesgo (pts) | 111.6 |
| Winrate setup | ~82% — histórico E1 BTC (85% reglas OK) |
| Score Rules extendido | **80%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **6/7** (85%) |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **n/a** · Premium/Discount **n/a**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **52873.0** | Retest **52784.7–52911.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.02%) | ✅ ≤0.15% de 52864.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT (ICT retest · FVG BEARISH edge)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 52911.0 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas con cierres en zona ≤0.15% |
| Entry | **52911.0** (limit retest o market al cierre 2ª vela) |
| SL | **53022.6** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **52687.8** (1:2) |
| R:R | **1:2** · riesgo **111.6** pts |
| Invalidación | Cierre M5 > 53022.6 o breakout > 52864.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 52836.2→52911.0 (FVG BEARISH edge) · Sweep swing_high @ 52943.0 + reclaim · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **n/a** ✅ |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 52943.0 + reclaim |
| FVG alineados | 5 |
| Order blocks | 3 |
| Entrada refinada | **52911.0** (antes 52836.2 · FVG BEARISH edge) |
| Nota | Refinada 52836.2→52911.0 (FVG BEARISH edge) · Sweep swing_high @ 52943.0 + reclaim · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 52864.0 | Referencia — requiere 2 rojas **nuevas** en retest | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY_

- [✅] Cerca de zona (soporte_debil @ 52864)
- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/n/a | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (163/82) |
| Swings | HL 52758->52864 | HH 52828->52943 |

---

## M5 detalle

- RSI M5/H1: 66.5 / 21.2
- Zona: soporte_debil @ 52864
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:45 O=52811.0 H=52852.0 L=52778.0 C=52851.0 [G]`
- `14:50 O=52850.0 H=52890.0 L=52843.0 C=52871.0 [G]`
- `14:55 O=52868.0 H=52902.0 L=52865.0 C=52883.0 [G]`
- `15:00 O=52885.0 H=52925.0 L=52876.0 C=52905.0 [G]`
- `15:05 O=52904.0 H=52919.0 L=52895.0 C=52918.0 [G]`
- `15:10 O=52918.0 H=52941.0 L=52903.0 C=52903.0 [R]`
- `15:15 O=52904.0 H=52937.0 L=52902.0 C=52909.0 [G]`
- `15:20 O=52910.0 H=52911.0 L=52864.0 C=52898.0 [R]`
- `15:25 O=52899.0 H=52943.0 L=52898.0 C=52914.0 [G]`
- `15:30 O=52917.0 H=52937.0 L=52908.0 C=52920.0 [G]`
- `15:35 O=52919.0 H=52920.0 L=52869.0 C=52872.0 [R]`
- `15:39 O=52873.0 H=52873.0 L=52873.0 C=52873.0 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.017% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 67 OK |
| Rango coherente | SÍ | Modo BREAK: breakout de nivel/estructura |
| DMI alineado | NO | +DI domina (163/82) |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 52873 · reloj FUERA_NY · CRT PD=n/a · H1 bias **BEARISH**
- **Setup:** ESPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 6/7 (85%)
- **Bando:** CLI y H1 alineados (**BEARISH**)
- **Veredicto integrado:** ESPERAR — score 71% requiere confirmación TV

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 6/7 | 28% | 85% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | Modo BREAK: breakout de nivel/estructura |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 28.5% | 18% | grade C; conf=medium; → 34% |
| **Score combinado** | **71%** | 100% | pesos renormalizados |

---

## C) CRT deep dive

### Distancias PDH/PDL


### Premium / Discount 0.5

- Midpoint: n/d
- Posición precio: **n/a** (precio 52873)
- Lectura PD: **n/a**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-08 14:00 O=52918 H=52945 L=52758 C=52883 [R]`
- `09-08 15:00 O=52885 H=52943 L=52864 C=52872 [R]`
- `09-08 15:39 O=52873 H=52873 L=52873 C=52873 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 52864-52943; 0.5=52904

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar |  |
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
| 1 | Esperar setup A+ galeria WIN | — | 72% | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** SHORT @ zona soporte_debil 52864 (precio actual 52873)
- **SL estructural:** 53032 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 52556 | **BE:** mover a BE en 1:1
- **Invalidación:** cierre M5 fuera zona / CRT invalid / fakeout contra dirección
- **Confluencias Notion sugeridas:** Continuación/Breakout E1, Zona débil morada, CRT alineado

### Pre-trade checklist (8 ítems)

| # | Ítem | OK |
|---|------|----|
| 1 | Bias H1 alineado | ✅ |
| 2 | Zona ≤0.15% | ✅ |
| 3 | 2 velas M5 confirmación | ❌ |
| 4 | Rules E1 ≥63% | ✅ |
| 5 | Extendidas ≥70% | ✅ |
| 6 | Sin fakeout contra | ✅ |
| 7 | SL ~$9 definido | ✅ |
| 8 | R:R 1:2 | ✅ |

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)
- ⚠ Tensión ML/Neural — no entrar por galería sola

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---

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
*high signal | 2026-09-08 15:49 UTC*
