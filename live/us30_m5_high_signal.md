# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-28 15:27 UTC | NY 2026-09-28 11:27 | FUERA_NY (Lunch)
> Precio **51794.0** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
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
**Tendencia:** Sin dirección
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~48%** — histórico E2 reversión BTC · LONG en DISCOUNT +4 (E2 a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patron LOSS similar -12; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 51744-51836; 0.5=51790 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 52080 | Bull si cierre arriba |
| PDL | 51948 | Bear si cierre abajo |
| 0.5 midpoint | 52014 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 31 OK |
| Rango coherente | ❌ | rango bajista |

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

- Precio < PDL — no long contra rango bajista CRT
- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón perdedor similar: contra bias (BTC-01-06-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **51794.0** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **51758.0** |
| Entry usuario | **51500.0 (CLI · 1:2)** |
| ICT | 51837.4→51758.0 · Refinada 51837.4→51758.0 (sweep swing_low) · Sweep swing_low @ 51758.0 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |
| Plan | Entry **51500.0** · SL **51397.0** · TP **51706.0** · plan usuario |
| E2 / Break | REVERSE / E2 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **72%** · ML **0.0%** · Confluencia **BAJA** — 27% · Rules 66%; Neural gated 64% (medium); ML 0% veto suave; 2M5 no listo; E2 no operable |
| Historial ref | **us30-034** · 2026-09-25 12:47 NY · Entry **52149.4** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry -391.4 pts (-0.751%) · precio→última 355.4 pts (0.681%) · precio→actual 36.0 pts (0.070%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entrada óptima | -36.0 pts (0.070%) |
| Dist. a Entry usuario | -294.0 pts (0.568%) |
| Dist. a SL | -397.0 pts (0.766%) |
| Dist. a TP | -88.0 pts (0.170%) |
| Riesgo (pts) | 103.0 |
| SL/TP | 1:2 fallback |
| Winrate setup | ~48% — histórico E2 reversión BTC · LONG en DISCOUNT +4 (E2 a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patron LOSS similar -12; 66% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +4 (E2 a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Falta 2M5 — ESPERAR |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.00× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist 18.74 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **REVERSE (E2)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **51794.0** | Retest **51758.0–51875.6** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.07% de ref | contexto entry @ 51829.0 |
| Acción | **ESPERAR LONG** | **ENTRAR LONG (Entry usuario)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Entry usuario CLI @ 51500.0 (LONG) |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entrada óptima | **51758.0** (sistema · limit retest o market al cierre 2ª vela) |
| Entry usuario | **51500.0** (CLI -Entry / --entry) |
| SL | **51397.0** (1:2 fallback (sin estructura past)) · plan Entry usuario · SL cuenta ~$9 (ajustar lotaje) |
| TP | **51706.0** (1:2 fallback) · plan Entry usuario |
| R:R | **1:2** · riesgo **103.0** pts |
| SL/TP nota | SL/TP 1:2 (fallback; sin estructura pasada segura post-entry) |
| Invalidación | Cierre M5 < 51397.0 o breakdown sin reclaim (Entry usuario 51500.0) |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 51837.4→51758.0 (sweep swing_low) · Sweep swing_low @ 51758.0 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 52014.0 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_low @ 51758.0 + reclaim |
| FVG alineados | 0 |
| Order blocks | 0 |
| Entrada refinada | **51758.0** (antes 51837.4 · sweep swing_low) |
| Nota | Refinada 51837.4→51758.0 (sweep swing_low) · Sweep swing_low @ 51758.0 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 51829.0 | **VÁLIDO** — Últimas 2 verdes en zona ≤0.15% | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (249/111) |
| Swings | LL 51758->51744 | HH 51946->51983 |

---

## M5 detalle

- RSI M5/H1: 30.8 / 27.1
- Zona: soporte_debil @ 51829
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:25 O=51959.0 H=51983.0 L=51952.0 C=51981.0 [G]`
- `14:30 O=51976.0 H=51979.0 L=51933.0 C=51941.0 [R]`
- `14:35 O=51940.0 H=51966.0 L=51916.0 C=51918.0 [R]`
- `14:40 O=51915.0 H=51935.0 L=51874.0 C=51882.0 [R]`
- `14:45 O=51885.0 H=51886.0 L=51806.0 C=51822.0 [R]`
- `14:50 O=51821.0 H=51857.0 L=51782.0 C=51782.0 [R]`
- `14:55 O=51783.0 H=51796.0 L=51761.0 C=51775.0 [R]`
- `15:00 O=51773.0 H=51796.0 L=51744.0 C=51784.0 [G]`
- `15:05 O=51781.0 H=51826.0 L=51762.0 C=51824.0 [G]`
- `15:10 O=51826.0 H=51836.0 L=51773.0 C=51781.0 [R]`
- `15:15 O=51783.0 H=51803.0 L=51780.0 C=51791.0 [G]`
- `15:17 O=51794.0 H=51794.0 L=51794.0 C=51794.0 [G]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 31 OK |
| Rango coherente | NO | rango bajista |
| DMI alineado | NO | -DI domina (249/111) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 51794 · reloj FUERA_NY (Lunch) · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **REVERSE** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 36%
- **E2 contexto:** E2_NO (1/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango bajista |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 0.0% | 18% | grade C; conf=high; → 0% |
| E2 turtle | 1/6 | 5% | E2_NO |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.06 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 27% | 38% | blend 62/38 con acuerdo BAJA 27% |
| **Probabilidad de éxito** | **36%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 52080: -286.0 pts (-0.549%)
- **PDL** 51948: -154.0 pts (-0.296%)

### Premium / Discount 0.5

- Midpoint 0.5: **52014**
- Posición precio: **DISCOUNT** (precio 51794)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-28 14:00 O=51920 H=51983 L=51761 C=51775 [R]`
- `09-28 15:00 O=51773 H=51836 L=51744 C=51791 [G]`
- `09-28 15:17 O=51794 H=51794 L=51794 C=51794 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 51744-51836; 0.5=51790

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar |  |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo | **→** |
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

**Acuerdo Rules/Neural:** CONFLICT

- Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual fuerte pero features ML desfavorables; priorizar Rules % + CRT

- **Neural galería:** 71.8% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 72% | contra-bias, LOSS |

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
- **Vol relativo:** 0.00× → banda **muy_bajo** (vol×0.00 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 18.74 · soft-filter vs setup: **alineado**
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
*high signal | 2026-09-28 15:27 UTC*
