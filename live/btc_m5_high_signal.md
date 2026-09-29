# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-28 22:29 UTC | NY 2026-09-28 18:29 | FUERA_NY
> Precio **83234.1** | HIGH mode | PF E1=4.77 | E2 max 10%
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
**Probabilidad histórica:** **~48%** — histórico E2 reversión BTC · LONG en DISCOUNT +4 (E2 a favor); H1 BEARISH vs LONG -6; acuerdo NULA -12; patrones mixtos -4; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BULL** | Sweep low H1 + reclaim |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 85159 | Bull si cierre arriba |
| PDL | 84132 | Bear si cierre abajo |
| 0.5 midpoint | 84646 | Filtro 50% |

**Nota CRT:** REVERSE: H1 PENDING_BULL — sweep+reclaim E2 ctx

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 16 OK |
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
- RSI M5 16.1 sobrevendido — filtro TORYS-like
- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **83234.1** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **83270.0** |
| ICT | 83283.5→83270.0 · Refinada 83283.5→83270.0 (soporte debil) · Sweep swing_high @ 83581.5 + reclaim · PD DISCOUNT · H1 PENDING_BULL |
| Plan | Entry **83270.0** · SL **83210.0** · TP **83390.0** |
| E2 / Break | REVERSE / E2 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **65%** · ML **29.5%** · Confluencia **NULA** — 22% · Rules 66%; Neural gated 60% (medium); ML 30% veto suave; 2M5 no listo; E2 no operable |
| Historial ref | **btc-030** · 2026-09-26 12:38 NY · Entry **84164.5** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry -894.5 pts (-1.063%) · precio→última 930.4 pts (1.105%) · precio→actual 35.9 pts (0.043%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | +35.9 pts (0.043%) |
| Dist. a SL | -24.1 pts (0.029%) |
| Dist. a TP | +155.9 pts (0.187%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~48% — histórico E2 reversión BTC · LONG en DISCOUNT +4 (E2 a favor); H1 BEARISH vs LONG -6; acuerdo NULA -12; patrones mixtos -4; 66% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +4 (E2 a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Falta 2M5 — ESPERAR |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.12× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **en contra** · Hist -140.9 · never trigger |
| Watchtower KZ | FUERA_NY · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **REVERSE (E2)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **83234.1** | Retest **83270.0–83344.9** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.04% de ref | contexto entry @ 83270.0 |
| Acción | **ESPERAR LONG** | **ENTRAR LONG (ICT retest · soporte debil)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest soporte debil @ 83270.0 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **83270.0** (limit retest o market al cierre 2ª vela) |
| SL | **83210.0** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **83390.0** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 < 83223.5 o breakdown < 83270.0 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 83283.5→83270.0 (soporte debil) · Sweep swing_high @ 83581.5 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 84645.5 |
| H1 CRT state | **PENDING_BULL** |
| Killzone / sesión | FUERA_NY (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 83581.5 + reclaim |
| FVG alineados | 5 |
| Order blocks | 5 |
| Entrada refinada | **83270.0** (antes 83283.5 · soporte debil) |
| Nota | Refinada 83283.5→83270.0 (soporte debil) · Sweep swing_high @ 83581.5 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 83270.0 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BULL/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (366/70) |
| Swings | LL 83442->83100 | HH 83582->83664 |

---

## M5 detalle

- RSI M5/H1: 16.1 / 53.3
- Zona: soporte_debil @ 83270
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `21:30 O=83468.3 H=83475.5 L=83422.0 C=83468.0 [R]`
- `21:35 O=83468.0 H=83472.0 L=83424.5 C=83424.5 [R]`
- `21:40 O=83424.5 H=83431.2 L=83400.0 C=83427.6 [G]`
- `21:45 O=83427.6 H=83439.4 L=83400.0 C=83427.7 [G]`
- `21:50 O=83427.7 H=83427.7 L=83232.1 C=83244.0 [R]`
- `21:55 O=83244.0 H=83264.0 L=83214.0 C=83218.0 [R]`
- `22:00 O=83218.0 H=83236.0 L=83100.0 C=83186.0 [R]`
- `22:05 O=83186.0 H=83186.0 L=83106.0 C=83182.0 [R]`
- `22:10 O=83182.0 H=83224.7 L=83164.0 C=83182.0 [R]`
- `22:15 O=83182.0 H=83224.7 L=83158.0 C=83224.7 [G]`
- `22:20 O=83224.7 H=83228.0 L=83194.0 C=83210.0 [R]`
- `22:25 O=83210.0 H=83242.4 L=83199.7 C=83234.1 [G]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 16 OK |
| Rango coherente | NO | rango bajista |
| DMI alineado | NO | -DI domina (366/70) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 83234 · reloj FUERA_NY · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **REVERSE** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 37%
- **E2 contexto:** E2_NO (1/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango bajista |
| Neural galería (gated) | 65.0% | 25% | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 29.5% | 18% | grade C; conf=medium; → 35% |
| E2 turtle | 1/6 | 5% | E2_NO |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.06 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 22% | 38% | blend 62/38 con acuerdo NULA 22% |
| **Probabilidad de éxito** | **37%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 85159: -1924.9 pts (-2.260%)
- **PDL** 84132: -897.9 pts (-1.067%)

### Premium / Discount 0.5

- Midpoint 0.5: **84646**
- Posición precio: **DISCOUNT** (precio 83234)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-28 20:00 O=83390 H=83614 L=83270 C=83548 [G]`
- `09-28 21:00 O=83548 H=83664 L=83214 C=83218 [R]`
- `09-28 22:00 O=83218 H=83242 L=83100 C=83234 [G]`

- Estado CRT H1: **PENDING_BULL** — Sweep low H1 + reclaim

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

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 65.0% WIN (grade B, conf medium) · gate×0.65 → 60% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26) | BTC-11-05-26.png | 65% | sweep+reclaim, WIN |
| 2 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 60% | contra-bias, LOSS |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_BTC_E1` — alto 1.7 / extremo 2.6 / bajo 0.75 / muy bajo 0.45 / período 84 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY**
- **Vol relativo:** 0.12× → banda **muy_bajo** (vol×0.12 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -140.9 · soft-filter vs setup: **en contra**
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
*high signal | 2026-09-28 22:29 UTC*
