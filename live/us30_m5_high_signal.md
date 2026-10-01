# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-01 15:28 UTC | NY 2026-10-01 11:28 | FUERA_NY (Lunch)
> Precio **50661.4** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- E2: E2_WATCH (4/6) · operable=NO · WR ~61%

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario | E2 watch only
**Tendencia:** Sin dirección
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~48%** — histórico E2 reversión BTC · LONG en DISCOUNT +4 (E2 a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patrones mixtos -4; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BEAR** | Sweep high H1 sin hold |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 51685 | Bull si cierre arriba |
| PDL | 50906 | Bear si cierre abajo |
| 0.5 midpoint | 51296 | Filtro 50% |

**Nota CRT:** REVERSE: H1 PENDING_BEAR — sweep+reclaim E2 ctx

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ❌ | rango bajista |

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

- Precio < PDL — no long contra rango bajista CRT
- CRT H1 pending bear — no entrar long contra invalid reciente

### Galería (cross-ref)

- Patrón ganador similar: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **50661.4** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **50628.4** |
| ICT | 50657.0→50628.4 · Refinada 50657.0→50628.4 (FVG BULLISH edge) · Sweep swing_high @ 51158.4 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |
| Plan | Entry **50628.4** · SL **50566.3** · TP **50752.8** |
| E2 / Break | REVERSE / E2 — Vigilar reversión E2 — E1 primario | E2 watch only |
| Métricas | Rules **66%** · Neural **72%** · ML **100.0%** · Confluencia **BAJA** — 38% · Rules 66%; Neural gated 64% (medium); ML 100% (high); 2M5 no listo; E2 watch |
| Historial ref | **us30-038** · 2026-09-30 11:23 NY · Entry **51677.0** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry -1048.6 pts (-2.029%) · precio→última 1015.6 pts (1.965%) · precio→actual 33.0 pts (0.065%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | -33.0 pts (0.065%) |
| Dist. a SL | -95.2 pts (0.188%) |
| Dist. a TP | +91.3 pts (0.180%) |
| Riesgo (pts) | 62.2 |
| Winrate setup | ~48% — histórico E2 reversión BTC · LONG en DISCOUNT +4 (E2 a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patrones mixtos -4; 66% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +4 (E2 a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | REVERSE watch (E2_WATCH) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.00× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist -62.55 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **REVERSE (E2)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **50661.4** | Retest **50628.4–50689.0** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.04% de ref | contexto entry @ 50643.4 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 50628.4 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **50628.4** (limit retest o market al cierre 2ª vela) |
| SL | **50566.3** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **50752.8** (1:2) |
| R:R | **1:2** · riesgo **62.2** pts |
| Invalidación | Cierre M5 < 50594.9 o breakdown < 50643.4 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 50657.0→50628.4 (FVG BULLISH edge) · Sweep swing_high @ 51158.4 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 51295.9 |
| H1 CRT state | **PENDING_BEAR** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 51158.4 + reclaim |
| FVG alineados | 5 |
| Order blocks | 2 |
| Entrada refinada | **50628.4** (antes 50657.0 · FVG BULLISH edge) |
| Nota | Refinada 50657.0→50628.4 (FVG BULLISH edge) · Sweep swing_high @ 51158.4 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 50643.4 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BEAR/BEARISH | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | BEAR | -DI domina (275/231) |
| Swings | HL 50623->50643 | LH 51184->50789 |

---

## M5 detalle

- RSI M5/H1: 45.7 / 37.6
- Zona: soporte_debil @ 50643
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:25 O=50698.4 H=50717.4 L=50643.4 C=50665.4 [R]`
- `14:30 O=50663.4 H=50750.4 L=50658.4 C=50750.4 [G]`
- `14:35 O=50748.4 H=50783.4 L=50719.4 C=50771.4 [G]`
- `14:40 O=50766.4 H=50789.4 L=50706.4 C=50719.4 [R]`
- `14:45 O=50718.4 H=50771.4 L=50683.4 C=50716.4 [R]`
- `14:50 O=50713.4 H=50729.4 L=50647.4 C=50657.4 [R]`
- `14:55 O=50656.4 H=50729.4 L=50640.4 C=50675.4 [G]`
- `15:00 O=50678.4 H=50692.4 L=50570.4 C=50572.4 [R]`
- `15:05 O=50577.4 H=50603.4 L=50555.4 C=50582.4 [G]`
- `15:10 O=50581.4 H=50628.4 L=50547.4 C=50620.4 [G]`
- `15:15 O=50621.4 H=50664.4 L=50600.4 C=50608.4 [R]`
- `15:18 O=50661.4 H=50661.4 L=50661.4 C=50661.4 [G]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | NO | rango bajista |
| DMI alineado | NO | -DI domina (275/231) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 50661 · reloj FUERA_NY (Lunch) · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **REVERSE** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 52%
- **E2 contexto:** E2_WATCH (4/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango bajista |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 100.0% | 18% | grade A+; conf=high; → 100% |
| E2 turtle | 4/6 | 5% | E2_WATCH |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.06 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 38% | 38% | blend 62/38 con acuerdo BAJA 38% |
| **Probabilidad de éxito** | **52%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 51685: -1024.0 pts (-1.981%)
- **PDL** 50906: -245.0 pts (-0.481%)

### Premium / Discount 0.5

- Midpoint 0.5: **51296**
- Posición precio: **DISCOUNT** (precio 50661)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-01 14:00 O=50813 H=50818 L=50623 C=50675 [R]`
- `10-01 15:00 O=50678 H=50692 L=50547 C=50608 [R]`
- `10-01 15:18 O=50657 H=50657 L=50657 C=50657 [G]`

- Estado CRT H1: **PENDING_BEAR** — Sweep high H1 sin hold

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
| 2. Rompe min/max previo | ✅ | SÍ | Sweep swing low + reclaim |
| 3. Reclaim agresivo | ✅ | SÍ | Reclaim M5 |
| 4. Entrada zona SL original | ✅ | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | ❌ | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | ❌ | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | ❌ | NO | Esperar 2 velas alineadas |
| 8. Winrate E2 | ✅ | SÍ | ~61% |

**Score:** 4/6 · Veredicto: **E2_WATCH**

### Interpretación fakeout PDL/PDH

- Sin fakeout macro activo — E2 requiere sweep+reclaim explícito

### Decisión E2: **Observar** — falta confirmación 2 velas o checklist incompleto · WR ~61%

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** ALIGNED

- ML y Neural apuntan misma dirección de confianza

- **Neural galería:** 71.8% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26) | BTC-11-05-26.png | 72% | sweep+reclaim, WIN |
| 2 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 67% | contra-bias, LOSS |

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
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -62.55 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-01 15:28 UTC*
