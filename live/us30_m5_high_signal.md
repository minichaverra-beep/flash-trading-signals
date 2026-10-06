# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-06 18:28 UTC | NY 2026-10-06 14:28 | NY PM 14-16
> Precio **51545.5** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- E2: E2_WATCH (2/6) · operable=SÍ · WR ~61%

---

## Veredicto: NO_OPERAR

**E1/E2:** E2 REVERSE operable
**Tendencia:** Sin dirección
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~62%** — histórico E2 reversión BTC · SHORT en PREMIUM +4 (E2 a favor); CLI BEARISH a favor +2; acuerdo MEDIA -2; patron WIN similar +3; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 51490-51582; 0.5=51536 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 51440 | Bull si cierre arriba |
| PDL | 50888 | Bear si cierre abajo |
| 0.5 midpoint | 51164 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ✅ | Velas confirman |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ❌ | rango alcista |

### Turtle Soup E2

Score **2/6** | Operable: **SÍ** | Winrate: **~61%**
_Modo REVERSE operable — 2 velas M5 alineadas (SHORT); WR histórico E2 ~61% BTC / ~63% global_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | NO | Sweep liquidez |
| 3. Reclaim agresivo | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | SÍ | SHORT confirmado |
| 8. Winrate E2 | SÍ | ~61% |

### Red flags

- Precio > PDH — no short contra rango alcista CRT
- RSI TORYS en contra: Fondo verde TORYS-proxy - filtro long

### Galería (cross-ref)

- Patrón ganador similar: REVERSE 2 velas alineadas al bando
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **51545.5** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **51591.5** |
| ICT | 51545.1→51591.5 · Refinada 51545.1→51591.5 (FVG BEARISH edge) · Sweep swing_high @ 51553.5 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY PM 14-16 |
| Plan | Entry **51591.5** · SL **51651.5** · TP **51471.5** |
| E2 / Break | REVERSE / E2 — Vigilar reversión E2 — E2 REVERSE operable |
| Métricas | Rules **66%** · Neural **72%** · ML **0.0%** · Confluencia **MEDIA** — 50% · Rules 66%; Neural gated 64% (medium); ML 0% veto suave; 2M5 OK; E2 operable |
| Historial ref | **us30-055** · 2026-10-06 14:12 NY · Entry **51591.5** · **BUENA** — precio cerca de última Entry + 2M5 OK + zona OK · (MISMA ZONA) · Δ Entry +0.0 pts (+0.000%) · precio→última 46.0 pts (0.089%) · precio→actual 46.0 pts (0.089%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +46.0 pts (0.089%) |
| Dist. a SL | +106.0 pts (0.206%) |
| Dist. a TP | -74.0 pts (0.144%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~62% — histórico E2 reversión BTC · SHORT en PREMIUM +4 (E2 a favor); CLI BEARISH a favor +2; acuerdo MEDIA -2; patron WIN similar +3; 66% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +4 (E2 a favor) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **70%** |
| Estado 2M5 | VÁLIDO SHORT (2M5) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | REVERSE operable (2/6) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.37× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist 58.43 · never trigger |
| Watchtower KZ | NY PM 14-16 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **REVERSE (E2)** · CRT PD **BULLISH** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **51545.5** | Retest **51507.1–51591.5** |
| 2M5 SHORT | Sí | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.02% de ref | contexto entry @ 51553.5 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT (condiciones actuales OK)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 51591.5 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **51591.5** (limit retest o market al cierre 2ª vela) |
| SL | **51651.5** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **51471.5** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 51605.1 o breakout > 51553.5 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 51545.1→51591.5 (FVG BEARISH edge) · Sweep swing_high @ 51553.5 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY PM 14-16 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 51164.0 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY PM 14-16 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 51553.5 + reclaim |
| FVG alineados | 5 |
| Order blocks | 5 |
| Entrada refinada | **51591.5** (antes 51545.1 · FVG BEARISH edge) |
| Nota | Refinada 51545.1→51591.5 (FVG BEARISH edge) · Sweep swing_high @ 51553.5 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY PM 14-16 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 51553.5 | **VÁLIDO** — Últimas 2 rojas en zona ≤0.15% | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY PM 14-16_

- [✅] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Las 4 ✅ → 2M5 OK.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | +DI domina (78/65) | **LONG** |
| CRT PD / Premium-Discount | BULLISH · PREMIUM | **LONG** |
| Estructura swings M5 | HL 51490->51522 · LH 51678->51554 | **NEUTRAL** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BULLISH | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | BULL | +DI domina (78/65) |
| Swings | HL 51490->51522 | LH 51678->51554 |

---

## M5 detalle

- RSI M5/H1: 54.5 / 62.2
- Zona: resistencia_debil @ 51554
- 2M5 LONG: NO | SHORT: SÍ

### 12 velas M5

- `17:30 O=51536.5 H=51543.5 L=51517.5 C=51541.5 [G]`
- `17:35 O=51540.5 H=51553.5 L=51534.5 C=51537.5 [R]`
- `17:40 O=51538.5 H=51548.5 L=51526.5 C=51528.5 [R]`
- `17:45 O=51527.5 H=51538.5 L=51522.5 C=51536.5 [G]`
- `17:50 O=51535.5 H=51552.5 L=51523.5 C=51526.5 [R]`
- `17:55 O=51527.5 H=51540.5 L=51522.5 C=51540.5 [G]`
- `18:00 O=51541.5 H=51567.5 L=51540.5 C=51556.5 [G]`
- `18:05 O=51555.5 H=51560.5 L=51546.5 C=51558.5 [G]`
- `18:10 O=51559.5 H=51574.5 L=51554.5 C=51573.5 [G]`
- `18:15 O=51574.5 H=51580.5 L=51555.5 C=51555.5 [R]`
- `18:20 O=51556.5 H=51557.5 L=51539.5 C=51555.2 [R]`
- `18:25 O=51554.2 H=51560.5 L=51544.5 C=51545.5 [R]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | SÍ | Velas confirman |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | NO | rango alcista |
| DMI alineado | NO | +DI domina (78/65) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 51546 · reloj NY PM 14-16 · CRT PD=BULLISH · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **REVERSE** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 48%
- **E2 contexto:** E2_WATCH (2/6) · operable=SÍ · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango alcista |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 0.0% | 18% | grade C; conf=high; → 0% |
| E2 turtle | 2/6 | 5% | E2_WATCH |
| Bonificación ubicación | ×1.06 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 50% | 38% | blend 62/38 con acuerdo MEDIA 50% |
| **Probabilidad de éxito** | **48%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 51440: +105.0 pts (+0.204%)
- **PDL** 50888: +658.0 pts (+1.293%)

### Premium / Discount 0.5

- Midpoint 0.5: **51164**
- Posición precio: **PREMIUM** (precio 51546)
- Lectura PD: **BULLISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-06 16:00 O=51640 H=51678 L=51558 C=51572 [R]`
- `10-06 17:00 O=51572 H=51582 L=51490 C=51540 [R]`
- `10-06 18:00 O=51542 H=51580 L=51540 C=51546 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 51490-51582; 0.5=51536

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar |  |
| Cierre > PDH | Sesgo alcista — long pullback | **→** |
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
| 4. Entrada zona SL original | ✅ | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | ❌ | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | ❌ | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | ✅ | SÍ | SHORT confirmado |
| 8. Winrate E2 | ✅ | SÍ | ~61% |

**Score:** 2/6 · Veredicto: **E2_WATCH**

### Interpretación fakeout PDL/PDH

- Sin fakeout macro activo — E2 requiere sweep+reclaim explícito

### Decisión E2: **OPERABLE** — 2 velas alineadas al bando · WR ~61%

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** CONFLICT

- Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual fuerte pero features ML desfavorables; priorizar Rules % + CRT

- **Neural galería:** 71.8% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: REVERSE 2 velas alineadas al bando | — | 72% | WIN |
| 2 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 67% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY PM 14-16**
- **Vol relativo:** 0.37× → banda **muy_bajo** (vol×0.37 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 58.43 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-06 18:28 UTC*
