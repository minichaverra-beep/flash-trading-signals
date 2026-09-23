# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-18 17:24 UTC | NY 2026-09-18 13:24 | FUERA_NY (Lunch)
> Precio **51953.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- Setup **REVERSE** — turtle soup / PDH-PDL fakeout / sweep+reclaim
- E2: E2_NO (1/6) · operable=NO · WR ~61%

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 7** (71%) | Extendidas: **81%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~61%** — histórico E2 BTC reversión (~63% E2 global)

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BEAR** | Sweep high H1 sin hold |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 52580 | Bull si cierre arriba |
| PDL | 52044 | Bear si cierre abajo |
| 0.5 midpoint | 52312 | Filtro 50% |

**Nota CRT:** REVERSE: H1 PENDING_BEAR — sweep+reclaim E2 ctx

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Alcista |
| Cerca de zona clave | ✅ | a 0.019% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 50 OK |
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
- CRT H1 pending bear — no entrar long contra invalid reciente
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **51953.0** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **51944.0** |
| ICT | 51990.3→51944.0 · Refinada 51990.3→51944.0 (FVG BULLISH edge) · Sweep swing_high @ 51963.0 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |
| Plan | Entry **51944.0** · SL **51807.1** · TP **52217.8** |
| E2 / Break | REVERSE / E2 — Sin reversión E2 — E1 primario |
| Métricas | Rules **71%** · ML **100.0%** · Confluencia **BAJA** — 42% · Rules 71%; ML 100% (high); 2M5 o zona parcial; E2 no operable; CLI alineado / H1 no |
| Historial ref | **us30-031** · 2026-09-18 13:21 NY · Entry **51944.0** · **REGULAR** — precio cerca de última Entry; sin 2M5; zona OK · (MISMA ZONA) · Δ Entry +0.0 pts (+0.000%) · precio→última 9.0 pts (0.017%) · precio→actual 9.0 pts (0.017%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | -9.0 pts (0.017%) |
| Dist. a SL | -145.9 pts (0.281%) |
| Dist. a TP | +264.8 pts (0.510%) |
| Riesgo (pts) | 136.9 |
| Winrate setup | ~61% — histórico E2 BTC reversión (~63% E2 global) |
| Score Rules extendido | **81%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BULLISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Rules E1 detalle | **5/7** (71%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.00× · Zentinel_US30_E1 |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **REVERSE (E2)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **51953.0** | Retest **51944.0–52040.9** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.02%) | ✅ ≤0.15% de 51963.0 |
| Acción | **ESPERAR LONG** | **ENTRAR LONG (ICT retest · FVG BULLISH edge)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 51944.0 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas con cierres en zona ≤0.15% |
| Entry | **51944.0** (limit retest o market al cierre 2ª vela) |
| SL | **51807.1** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **52217.8** (1:2) |
| R:R | **1:2** · riesgo **136.9** pts |
| Invalidación | Cierre M5 < 51807.1 o breakdown < 51963.0 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 51990.3→51944.0 (FVG BULLISH edge) · Sweep swing_high @ 51963.0 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 52312.0 |
| H1 CRT state | **PENDING_BEAR** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 51963.0 + reclaim |
| FVG alineados | 3 |
| Order blocks | 3 |
| Entrada refinada | **51944.0** (antes 51990.3 · FVG BULLISH edge) |
| Nota | Refinada 51990.3→51944.0 (FVG BULLISH edge) · Sweep swing_high @ 51963.0 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en resistencia_debil @ 51963.0 | Referencia — requiere 2 verdes **nuevas** en retest | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [✅] Cerca de zona (resistencia_debil @ 51963)
- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **NEUTRAL**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | Momentum mixto | **NEUTRAL** |
| CRT PD / Premium-Discount | BEARISH · DISCOUNT | **LONG** |
| Estructura swings M5 | LL 51919->51888 · LH 52009->52009 | **SHORT** |

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BEAR/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 51919->51888 | LH 52009->52009 |

---

## M5 detalle

- RSI M5/H1: 50.0 / 21.3
- Zona: resistencia_debil @ 51963
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `16:20 O=51941.0 H=51948.0 L=51897.0 C=51906.0 [R]`
- `16:25 O=51905.0 H=51948.0 L=51888.0 C=51937.0 [G]`
- `16:30 O=51935.0 H=51972.0 L=51922.0 C=51957.0 [G]`
- `16:35 O=51958.0 H=51964.0 L=51941.0 C=51953.0 [R]`
- `16:40 O=51954.0 H=51978.0 L=51948.0 C=51964.0 [G]`
- `16:45 O=51966.0 H=51978.0 L=51943.0 C=51976.0 [G]`
- `16:50 O=51976.0 H=52009.0 L=51976.0 C=52005.0 [G]`
- `16:55 O=52005.0 H=52009.0 L=51992.0 C=51997.0 [R]`
- `17:00 O=51998.0 H=51998.0 L=51974.0 C=51981.0 [R]`
- `17:05 O=51980.0 H=51995.0 L=51966.0 C=51969.0 [R]`
- `17:10 O=51970.0 H=51970.0 L=51941.0 C=51953.0 [R]`
- `17:14 O=51953.0 H=51953.0 L=51953.0 C=51953.0 [G]`

---

## Score reglas extendidas (81%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Alcista |
| Cerca de zona clave | SÍ | a 0.019% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 50 OK |
| Rango coherente | NO | rango bajista |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 51953 · reloj FUERA_NY (Lunch) · CRT PD=BEARISH · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **REVERSE** · reglas E1 5/7 (71%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score 65% requiere confirmación TV
- **E2 contexto:** E2_NO (1/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 5/7 | 28% | 71% OK |
| Rules extendidas (10) | 81% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango bajista |
| Neural galería | n/d | — | omitido — sin chart/modelo (no pad 50%) |
| ML tabular (gated) | 100.0% | 18% | grade A+; conf=high; → 100% |
| E2 turtle | 1/6 | 5% | E2_NO |
| **Score combinado** | **65%** | 100% | pesos renormalizados |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 52580: -627.0 pts (-1.192%)
- **PDL** 52044: -91.0 pts (-0.175%)

### Premium / Discount 0.5

- Midpoint 0.5: **52312**
- Posición precio: **DISCOUNT** (precio 51953)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-18 16:00 O=51942 H=52009 L=51888 C=51997 [G]`
- `09-18 17:00 O=51998 H=51998 L=51941 C=51953 [R]`
- `09-18 17:14 O=51953 H=51953 L=51953 C=51953 [G]`

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

- Solo una fuente disponible — cruzar con Rules %


---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26) | BTC-11-05-26.png | heurística | sweep+reclaim, WIN |
| 2 | Esperar setup A+ galeria WIN | — | heurística | general |

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
*high signal | 2026-09-18 17:24 UTC*
