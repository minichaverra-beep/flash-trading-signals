# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-24 19:28 UTC | NY 2026-09-24 15:28 | NY PM 14-16
> Precio **84630.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- E2: E2_NO (1/6) · operable=NO · WR ~61%

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 6** (83%) | Extendidas: **70%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~61%** — histórico E2 BTC reversión (~63% E2 global)

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **COMPLETED_BULL** | High H1 84554 alcanzado |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 87279 | Bull si cierre arriba |
| PDL | 83500 | Bear si cierre abajo |
| 0.5 midpoint | 85389 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 66 OK |
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

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **84630.0** |
| Veredicto | **Esperar** (SHORT) |
| Entrada óptima | **85389.3** |
| ICT | 84540.3→85389.3 · Refinada 84540.3→85389.3 (premium 0.5) · Sweep swing_high @ 84554.0 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL · killzone NY PM 14-16 |
| Plan | Entry **85389.3** · SL **85449.3** · TP **85269.3** |
| E2 / Break | REVERSE / E2 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **65%** · ML **46.3%** · Confluencia **BAJA** — 38% · Rules 83%; Neural gated 60% (medium); ML 46% gris; 2M5 no listo; E2 no operable |
| Historial ref | **btc-026** · 2026-09-24 14:44 NY · Entry **84444.0** · **MALA** — cerca suave de última Entry; sin 2M5; zona OK · (MÁS LEJOS) · Δ Entry +945.3 pts (+1.119%) · precio→última 186.0 pts (0.220%) · precio→actual 759.3 pts (0.889%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +759.3 pts (0.897%) |
| Dist. a SL | +819.3 pts (0.968%) |
| Dist. a TP | +639.3 pts (0.755%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~61% — histórico E2 BTC reversión (~63% E2 global) |
| Score Rules extendido | **70%** |
| Estado 2M5 | Falta 2M5 — ESPERAR |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.32× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **OK** · Hist -396.8 · never trigger |
| Watchtower KZ | NY PM 14-16 · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **REVERSE (E2)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **84630.0** | Retest **84477.9–85389.3** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.09% de ref | contexto entry @ 84554.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT (ICT retest · premium 0.5)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest premium 0.5 @ 85389.3 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **85389.3** (limit retest o market al cierre 2ª vela) |
| SL | **85449.3** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **85269.3** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 84600.3 o breakout > 84554.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 84540.3→85389.3 (premium 0.5) · Sweep swing_high @ 84554.0 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL · killzone NY PM 14-16 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ⚠️ |
| 0.5 midpoint | 85389.3 |
| H1 CRT state | **COMPLETED_BULL** |
| Killzone / sesión | NY PM 14-16 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 84554.0 + reclaim |
| FVG alineados | 4 |
| Order blocks | 5 |
| Entrada refinada | **85389.3** (antes 84540.3 · premium 0.5) |
| Nota | Refinada 84540.3→85389.3 (premium 0.5) · Sweep swing_high @ 84554.0 + reclaim · PD DISCOUNT · H1 COMPLETED_BULL · killzone NY PM 14-16 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 84554.0 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY PM 14-16_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | +DI domina (550/286) | **LONG** |
| CRT PD / Premium-Discount | NEUTRAL · DISCOUNT | **LONG** |
| Estructura swings M5 | HL 84258->84298 · LH 84924->84554 | **NEUTRAL** |

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BULL/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (550/286) |
| Swings | HL 84258->84298 | LH 84924->84554 |

---

## M5 detalle

- RSI M5/H1: 65.8 / 56.3
- Zona: resistencia_debil @ 84554
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `18:30 O=84424.0 H=84506.4 L=84343.1 C=84343.3 [R]`
- `18:35 O=84343.3 H=84554.0 L=84258.0 C=84452.0 [G]`
- `18:40 O=84452.0 H=84452.0 L=84391.5 C=84423.8 [R]`
- `18:45 O=84423.8 H=84454.0 L=84367.8 C=84408.1 [R]`
- `18:50 O=84408.1 H=84518.0 L=84408.1 C=84448.0 [G]`
- `18:55 O=84448.0 H=84540.0 L=84448.0 C=84476.0 [G]`
- `19:00 O=84476.0 H=84504.0 L=84304.0 C=84316.0 [R]`
- `19:05 O=84316.0 H=84495.6 L=84298.0 C=84495.6 [G]`
- `19:10 O=84495.6 H=84629.7 L=84478.0 C=84584.0 [G]`
- `19:15 O=84584.0 H=84622.0 L=84540.0 C=84615.2 [G]`
- `19:20 O=84615.2 H=84631.5 L=84555.6 C=84631.5 [G]`
- `19:25 O=84631.5 H=84660.0 L=84617.2 C=84630.0 [R]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 66 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | +DI domina (550/286) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 84630 · reloj NY PM 14-16 · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** ESPERAR SHORT · dirección **SHORT** · modo **REVERSE** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score 68% requiere confirmación TV
- **E2 contexto:** E2_NO (1/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 70% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 65.0% | 25% | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 46.3% | 18% | grade C; conf=low; → 48% |
| E2 turtle | 1/6 | 5% | E2_NO |
| **Score combinado** | **68%** | 100% | pesos renormalizados |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 87279: -2648.5 pts (-3.035%)
- **PDL** 83500: +1130.0 pts (+1.353%)

### Premium / Discount 0.5

- Midpoint 0.5: **85389**
- Posición precio: **DISCOUNT** (precio 84630)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-24 17:00 O=84500 H=84562 L=84018 C=84110 [R]`
- `09-24 18:00 O=84110 H=84554 L=83888 C=84476 [G]`
- `09-24 19:00 O=84476 H=84660 L=84298 C=84630 [G]`

- Estado CRT H1: **COMPLETED_BULL** — High H1 84554 alcanzado

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

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 65.0% WIN (grade B, conf medium) · gate×0.65 → 60% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 65% | rechazo, WIN |

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
- **Vol relativo:** 0.32× → banda **muy_bajo** (vol×0.32 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -396.8 · soft-filter vs setup: **alineado**
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
*high signal | 2026-09-24 19:28 UTC*
