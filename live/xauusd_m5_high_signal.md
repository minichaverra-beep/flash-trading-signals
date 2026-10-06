# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-06 17:44 UTC | NY 2026-10-06 13:44 | FUERA_NY (Lunch)
> Precio **4164.98** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-06 17:40 UTC** · hace 4 min · fuente MT5 XAUUSDm (broker, M5/H1)
> **Modo:** BEARISH + REVERSE — Bias CLI **BEARISH** — setup re-puntuado como SHORT
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **BEARISH** |
| Modo setup | **REVERSE (E2)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BEARISH** — setup re-puntuado como SHORT
- ⚠ H1 alcista vs bias forzado — confirmar en TV antes de entrar
- Setup **REVERSE** — turtle soup / PDH-PDL fakeout / sweep+reclaim
- E2: E2_NO (1/6) · operable=NO · WR ~61%

---

## Veredicto: ENTRAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~51%** — histórico E2 reversión BTC · SHORT en PREMIUM +4 (E2 a favor); H1 BULLISH vs SHORT -6; acuerdo BAJA -8; patron WIN similar +3; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4154-4166; 0.5=4160 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4170 | Bull si cierre arriba |
| PDL | 4123 | Bear si cierre abajo |
| 0.5 midpoint | 4147 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

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

### Plan (ENTRAR)

- Dirección: **Short** @ 4165
- SL estructura: **4173** | TP: **4148** (R:R 1:2)
- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos
- BE en 1:1 | Invalidación: fuera zona / CRT invalid

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4164.98** |
| Veredicto | **Entrar** (SHORT) |
| Entrada óptima | **4170.40** |
| ICT | 4163.95→4170.40 · Refinada 4164.0→4170.4 (sweep PDH) · Sweep PDH @ 4170.4 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |
| Plan | Entry **4170.40** · SL **4176.40** · TP **4158.40** |
| E2 / Break | REVERSE / E2 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **47%** · ML **4.1%** · Confluencia **BAJA** — 25% · Rules 83%; Neural débil/gating 47% conf=low; ML 4% veto suave; 2M5 no listo; E2 no operable |
| Historial ref | **xauusd-030** · 2026-10-06 13:43 NY · Entry **4164.89** · **BUENA** — precio cerca de última Entry + zona OK · (MISMA ZONA) · Δ Entry +5.51 pts (+0.132%) · precio→última 0.09 pts (0.002%) · precio→actual 5.41 pts (0.130%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BULLISH** |
| R:R | 1:2 |
| Dist. a Entry | +5.41 pts (0.130%) |
| Dist. a SL | +11.41 pts (0.274%) |
| Dist. a TP | -6.59 pts (0.158%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~51% — histórico E2 reversión BTC · SHORT en PREMIUM +4 (E2 a favor); H1 BULLISH vs SHORT -6; acuerdo BAJA -8; patron WIN similar +3; 83% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +4 (E2 a favor) |
| Bias vs dirección | H1 BULLISH vs SHORT -6 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BULLISH** · CLI **BEARISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Neural grade/conf | **C** · conf. low · 47% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **bajo** · 0.51× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist 4.14 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **REVERSE (E2)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4164.98** | Retest **4160.88–4170.40** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.01% de ref | contexto entry @ 4164.63 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest sweep PDH @ 4170.40 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **4170.40** (limit retest o market al cierre 2ª vela) |
| SL | **4176.40** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4158.40** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 > 4169.95 o breakout > 4164.63 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4164.0→4170.4 (sweep PDH) · Sweep PDH @ 4170.4 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 4146.74 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | Sí |
| Liquidity sweep | Sweep PDH @ 4170.4 + reclaim |
| FVG alineados | 5 |
| Order blocks | 1 |
| Entrada refinada | **4170.40** (antes 4163.95 · sweep PDH) |
| Nota | Refinada 4164.0→4170.4 (sweep PDH) · Sweep PDH @ 4170.4 + reclaim · PD PREMIUM · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 4164.63 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
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
| RSI TORYS | BEARISH | Fondo rojo TORYS-proxy - filtro short |
| DMI | BULL | +DI domina (14/9) |
| Swings | HL 4154->4158 | LH 4171->4165 |

---

## M5 detalle

- RSI M5/H1: 60.8 / 65.7
- Zona: resistencia_debil @ 4165
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `16:45 O=4160.41 H=4161.44 L=4155.90 C=4156.90 [R]`
- `16:50 O=4156.69 H=4157.56 L=4154.93 C=4155.84 [R]`
- `16:55 O=4155.67 H=4157.11 L=4154.14 C=4156.97 [G]`
- `17:00 O=4156.75 H=4159.42 L=4156.31 C=4159.31 [G]`
- `17:05 O=4159.48 H=4163.70 L=4159.30 C=4163.39 [G]`
- `17:10 O=4163.55 H=4164.63 L=4161.86 C=4162.29 [R]`
- `17:15 O=4162.35 H=4164.24 L=4160.90 C=4161.24 [R]`
- `17:20 O=4161.21 H=4162.51 L=4157.73 C=4159.82 [R]`
- `17:25 O=4159.73 H=4161.25 L=4158.01 C=4160.72 [G]`
- `17:30 O=4160.67 H=4163.61 L=4160.05 C=4162.80 [G]`
- `17:35 O=4162.97 H=4163.75 L=4162.14 C=4162.14 [R]`
- `17:40 O=4162.36 H=4165.59 L=4161.91 C=4164.98 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | +DI domina (14/9) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4165 · reloj FUERA_NY (Lunch) · CRT PD=NEUTRAL · H1 bias **BULLISH**
- **Setup:** ENTRAR SHORT · dirección **SHORT** · modo **REVERSE** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **BULLISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — score combinado 43%
- **E2 contexto:** E2_NO (1/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 47.1% | 25% | no alineado; conf=low; gate×0.17 → 50% |
| ML tabular (gated) | 4.1% | 18% | grade C; conf=high; → 4% |
| E2 turtle | 1/6 | 5% | E2_NO |
| Penalización dirección | ×0.88 | — | penalización H1 BULLISH vs SHORT |
| Bonificación ubicación | ×1.06 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 25% | 38% | blend 62/38 con acuerdo BAJA 25% |
| **Probabilidad de éxito** | **43%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4170: -5.4 pts (-0.130%)
- **PDL** 4123: +41.9 pts (+1.016%)

### Premium / Discount 0.5

- Midpoint 0.5: **4147**
- Posición precio: **PREMIUM** (precio 4165)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-06 15:00 O=4156 H=4171 L=4156 C=4165 [G]`
- `10-06 16:00 O=4165 H=4166 L=4154 C=4157 [R]`
- `10-06 17:00 O=4157 H=4166 L=4156 C=4165 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 4154-4166; 0.5=4160

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar | **→** |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 |  |
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

- Sin fakeout macro activo — E2 requiere sweep+reclaim explícito

### Decisión E2: **NO ENTRAR** — setup Reverse incompleto · WR ~61%

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** ALIGNED

- ML y Neural apuntan misma dirección de confianza

- **Neural galería:** 47.1% WIN (grade C, conf low) · gate×0.17 → 50% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 47% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** SHORT @ zona resistencia_debil 4165 (precio actual 4165)
- **SL estructural:** 4173 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 4148 | **BE:** mover a BE en 1:1
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
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY (Lunch)**
- **Vol relativo:** 0.51× → banda **bajo** (vol×0.51 ≤ bajo 0.7)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 4.14 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-06 17:44 UTC*
