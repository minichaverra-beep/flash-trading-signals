# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-05 13:56 UTC | NY 2026-10-05 09:56 | NY AM 08-10
> Precio **86347.9** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- ⚠ H1 alcista vs bias forzado — confirmar en TV antes de entrar
- Setup **REVERSE** — turtle soup / PDH-PDL fakeout / sweep+reclaim
- E2: E2_NO (1/6) · operable=NO · WR ~61%

---

## Veredicto: ENTRAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~51%** — histórico E2 reversión BTC · SHORT en PREMIUM +4 (E2 a favor); H1 BULLISH vs SHORT -6; acuerdo BAJA -8; patron WIN similar +3; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **COMPLETED_BULL** | High H1 86187 alcanzado |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 86787 | Bull si cierre arriba |
| PDL | 84696 | Bear si cierre abajo |
| 0.5 midpoint | 85741 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 69 OK |
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

- Dirección: **Short** @ 86348
- SL estructura: **86521** | TP: **86003** (R:R 1:2)
- Riesgo cuenta: **~$9** — ajustar lotaje, no puntos
- BE en 1:1 | Invalidación: fuera zona / CRT invalid

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Patrón ganador similar: REVERSE 2 velas alineadas al bando
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **86347.9** |
| Veredicto | **Entrar** (SHORT) |
| Entrada óptima | **86082.6** |
| ICT | 86236.6→86082.6 · Refinada 86236.6→86082.6 (FVG BEARISH edge) · Sweep swing_high @ 86192.8 + reclaim · PD PREMIUM · H1 COMPLETED_BULL · killzone NY AM 08-10 |
| Plan | Entry **86082.6** · SL **86228.4** · TP **85790.9** |
| E2 / Break | REVERSE / E2 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **65%** · ML **17.1%** · Confluencia **BAJA** — 33% · Rules 83%; Neural gated 60% (medium); ML 17% veto suave; 2M5 no listo; E2 no operable |
| Historial ref | **btc-060** · 2026-10-05 09:41 NY · Entry **85898.5** · **REGULAR** — cerca suave de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry +184.1 pts (+0.214%) · precio→última 449.4 pts (0.523%) · precio→actual 265.3 pts (0.308%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BULLISH** |
| R:R | 1:2 |
| Dist. a Entry | -265.3 pts (0.307%) |
| Dist. a SL | -119.5 pts (0.138%) |
| Dist. a TP | -557.0 pts (0.645%) |
| Riesgo (pts) | 145.8 |
| Winrate setup | ~51% — histórico E2 reversión BTC · SHORT en PREMIUM +4 (E2 a favor); H1 BULLISH vs SHORT -6; acuerdo BAJA -8; patron WIN similar +3; 83% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +4 (E2 a favor) |
| Bias vs dirección | H1 BULLISH vs SHORT -6 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BULLISH** · CLI **BEARISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.35× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **en contra** · Hist 113.9 · never trigger |
| Watchtower KZ | NY AM 08-10 · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **REVERSE (E2)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **86347.9** | Retest **86082.6–86250.5** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.11% de ref | contexto entry @ 86250.5 |
| Acción | **ENTRAR SHORT** | **ESPERAR SHORT (ICT limit · no chase)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 86082.6 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **86082.6** (limit retest o market al cierre 2ª vela) |
| SL | **86228.4** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **85790.9** (1:2) |
| R:R | **1:2** · riesgo **145.8** pts |
| Invalidación | Cierre M5 > 86382.4 o breakout > 86250.5 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 86236.6→86082.6 (FVG BEARISH edge) · Sweep swing_high @ 86192.8 + reclaim · PD PREMIUM · H1 COMPLETED_BULL · killzone NY AM 08-10 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 85741.4 |
| H1 CRT state | **COMPLETED_BULL** |
| Killzone / sesión | NY AM 08-10 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 86192.8 + reclaim |
| FVG alineados | 3 |
| Order blocks | 4 |
| Entrada refinada | **86082.6** (antes 86236.6 · FVG BEARISH edge) |
| Nota | Refinada 86236.6→86082.6 (FVG BEARISH edge) · Sweep swing_high @ 86192.8 + reclaim · PD PREMIUM · H1 COMPLETED_BULL · killzone NY AM 08-10 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 86250.5 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 08-10_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BULL/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (866/386) |
| Swings | LL 85809->85776 | LH 86217->86193 |

---

## M5 detalle

- RSI M5/H1: 69.2 / 47.8
- Zona: resistencia_debil @ 86251
- 2M5 LONG: SÍ | SHORT: NO

### 12 velas M5

- `13:00 O=85861.1 H=86074.7 L=85860.1 C=86051.8 [G]`
- `13:05 O=86054.6 H=86092.3 L=86000.7 C=86084.4 [G]`
- `13:10 O=86085.7 H=86123.8 L=86069.2 C=86092.4 [G]`
- `13:15 O=86089.9 H=86192.8 L=86058.4 C=86138.3 [G]`
- `13:20 O=86138.2 H=86160.1 L=86026.7 C=86041.4 [R]`
- `13:25 O=86044.0 H=86107.8 L=85992.7 C=86085.0 [G]`
- `13:30 O=86088.5 H=86104.2 L=85775.9 C=85958.8 [R]`
- `13:35 O=85958.6 H=86130.4 L=85894.7 C=86091.4 [G]`
- `13:40 O=86091.1 H=86110.7 L=85893.0 C=85949.2 [R]`
- `13:45 O=85952.4 H=86401.6 L=85849.1 C=86272.8 [G]`
- `13:50 O=86275.1 H=86425.8 L=86236.1 C=86322.5 [G]`
- `13:55 O=86320.2 H=86353.2 L=86260.3 C=86347.9 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 69 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | +DI domina (866/386) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 86348 · reloj NY AM 08-10 · CRT PD=NEUTRAL · H1 bias **BULLISH**
- **Setup:** ENTRAR SHORT · dirección **SHORT** · modo **REVERSE** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **BULLISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ENTRAR — score combinado 49%
- **E2 contexto:** E2_NO (1/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 65.0% | 25% | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 17.1% | 18% | grade C; conf=high; → 17% |
| E2 turtle | 1/6 | 5% | E2_NO |
| Penalización dirección | ×0.88 | — | penalización H1 BULLISH vs SHORT |
| Bonificación ubicación | ×1.06 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 33% | 38% | blend 62/38 con acuerdo BAJA 33% |
| **Probabilidad de éxito** | **49%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 86787: -438.7 pts (-0.505%)
- **PDL** 84696: +1651.6 pts (+1.950%)

### Premium / Discount 0.5

- Midpoint 0.5: **85741**
- Posición precio: **PREMIUM** (precio 86348)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-05 11:00 O=86100 H=86251 L=85887 C=86189 [G]`
- `10-05 12:00 O=86187 H=86187 L=85809 C=85862 [R]`
- `10-05 13:00 O=85861 H=86426 L=85776 C=86348 [G]`

- Estado CRT H1: **COMPLETED_BULL** — High H1 86187 alcanzado

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
| 1 | WIN: REVERSE 2 velas alineadas al bando | — | 65% | WIN |
| 2 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 60% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** SHORT @ zona resistencia_debil 86251 (precio actual 86348)
- **SL estructural:** 86521 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 86003 | **BE:** mover a BE en 1:1
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

- **FVG+Vol:** `Zentinel_BTC_E1` — alto 1.7 / extremo 2.6 / bajo 0.75 / muy bajo 0.45 / período 84 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 08-10**
- **Vol relativo:** 0.35× → banda **muy_bajo** (vol×0.35 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 113.9 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-05 13:56 UTC*
