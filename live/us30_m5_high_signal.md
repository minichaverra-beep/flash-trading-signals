# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-10 18:52 UTC | NY 2026-09-10 14:52 | NY PM 14-17
> Precio **52040.0** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> **Modo:** BULLISH + BREAK — Bias CLI **BULLISH** — setup re-puntuado como LONG
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **BULLISH** |
| Modo setup | **BREAK (breakout)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BULLISH** — setup re-puntuado como LONG
- ⚠ H1 bajista vs bias forzado — confirmar en TV antes de entrar
- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Sin breakout de nivel detectado

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 7** (71%) | Extendidas: **72%**
**Calidad:** Setup débil
**Probabilidad histórica:** **baja** — patrón perdedor similar — evitar

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 52004-52097; 0.5=52050 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 52859 | Bull si cierre arriba |
| PDL | 52339 | Bear si cierre abajo |
| 0.5 midpoint | 52599 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| Cerca de zona clave | ✅ | a 0.006% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 41 OK |
| Rango coherente | ❌ | rango bajista |

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
| Precio | **52040.0** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **52027.0** |
| ICT | 52070.3→52027.0 · Refinada 52070.3→52027.0 (FVG BULLISH edge) · Sweep swing_high @ 52097.0 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-17 |
| Plan | Entry **52027.0** · SL **51938.9** · TP **52203.2** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **71%** · ML **49.0%** · Confluencia **BAJA** — 45% · Rules 71%; ML 49% gris; 2M5 o zona parcial; Break con fricción CRT |
| Historial ref | **us30-026** · 2026-09-09 22:32 NY · Entry **52115.0** · **BUENA** — precio cerca de última Entry + zona OK · (MISMA ZONA) · Δ Entry -88.0 pts (-0.169%) · precio→última 75.0 pts (0.144%) · precio→actual 13.0 pts (0.025%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | -13.0 pts (0.025%) |
| Dist. a SL | -101.1 pts (0.194%) |
| Dist. a TP | +163.2 pts (0.314%) |
| Riesgo (pts) | 88.1 |
| Winrate setup | baja — patrón perdedor similar — evitar |
| Score Rules extendido | **72%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Rules E1 detalle | **5/7** (71%) |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **52040.0** | Retest **52027.0–52121.1** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.01%) | ✅ ≤0.15% de 52043.0 |
| Acción | **ESPERAR LONG** | **ENTRAR LONG (ICT retest · FVG BULLISH edge)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 52027.0 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas con cierres en zona ≤0.15% |
| Entry | **52027.0** (limit retest o market al cierre 2ª vela) |
| SL | **51938.9** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **52203.2** (1:2) |
| R:R | **1:2** · riesgo **88.1** pts |
| Invalidación | Cierre M5 < 51938.9 o breakdown < 52043.0 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 52070.3→52027.0 (FVG BULLISH edge) · Sweep swing_high @ 52097.0 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-17 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 52599.0 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY PM 14-17 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 52097.0 + reclaim |
| FVG alineados | 2 |
| Order blocks | 5 |
| Entrada refinada | **52027.0** (antes 52070.3 · FVG BULLISH edge) |
| Nota | Refinada 52070.3→52027.0 (FVG BULLISH edge) · Sweep swing_high @ 52097.0 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY PM 14-17 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 52043.0 | **VÁLIDO** — Últimas 2 verdes en zona ≤0.15% | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY PM 14-17_

- [✅] Cerca de zona (soporte_debil @ 52043)
- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (69/48) |
| Swings | LL 52010->52004 | LH 52198->52097 |

---

## M5 detalle

- RSI M5/H1: 41.0 / 16.3
- Zona: soporte_debil @ 52043
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `17:50 O=52060.0 H=52084.0 L=52060.0 C=52081.0 [G]`
- `17:55 O=52080.0 H=52084.0 L=52065.0 C=52079.0 [R]`
- `18:00 O=52078.0 H=52097.0 L=52046.0 C=52058.0 [R]`
- `18:05 O=52057.0 H=52068.0 L=52028.0 C=52035.0 [R]`
- `18:10 O=52034.0 H=52044.0 L=52010.0 C=52032.0 [R]`
- `18:15 O=52030.0 H=52034.0 L=52015.0 C=52023.0 [R]`
- `18:20 O=52027.0 H=52052.0 L=52027.0 C=52033.0 [G]`
- `18:25 O=52032.0 H=52046.0 L=52021.0 C=52030.0 [R]`
- `18:30 O=52026.0 H=52027.0 L=52004.0 C=52027.0 [G]`
- `18:35 O=52027.0 H=52041.0 L=52023.0 C=52037.0 [G]`
- `18:40 O=52039.0 H=52042.0 L=52032.0 C=52040.0 [G]`
- `18:41 O=52040.0 H=52040.0 L=52040.0 C=52040.0 [G]`

---

## Score reglas extendidas (72%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| Cerca de zona clave | SÍ | a 0.006% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 41 OK |
| Rango coherente | NO | rango bajista |
| DMI alineado | NO | -DI domina (69/48) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 52040 · reloj NY PM 14-17 · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 5/7 (71%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 47%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 5/7 | 28% | 71% OK |
| Rules extendidas (10) | 72% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango bajista |
| Neural galería | n/d | — | omitido — sin chart/modelo (no pad 50%) |
| ML tabular (gated) | 49.0% | 18% | grade C; conf=low; → 50% |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| **Score combinado** | **47%** | 100% | pesos renormalizados |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 52859: -819.0 pts (-1.549%)
- **PDL** 52339: -299.0 pts (-0.571%)

### Premium / Discount 0.5

- Midpoint 0.5: **52599**
- Posición precio: **DISCOUNT** (precio 52040)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-10 17:00 O=52150 H=52198 L=52049 C=52079 [R]`
- `09-10 18:00 O=52078 H=52097 L=52004 C=52040 [R]`
- `09-10 18:41 O=52040 H=52040 L=52040 C=52040 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 52004-52097; 0.5=52050

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar |  |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo | **→** |
| Fakeout PDH | NO long E1 |  |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** NEUTRAL

- Solo una fuente disponible — cruzar con Rules %


---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | heurística | contra-bias, LOSS |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

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
*high signal | 2026-09-10 18:52 UTC*
