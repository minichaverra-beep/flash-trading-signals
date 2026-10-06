# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-06 17:41 UTC | NY 2026-10-06 13:41 | FUERA_NY (Lunch)
> Precio **85558.8** | HIGH mode | PF E1=4.77 | E2 max 10%
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

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~55%** — histórico E1 BTC · SHORT en DISCOUNT -12 (chase Break); CLI BEARISH a favor +2; acuerdo MEDIA -2; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BULL** | Sweep low H1 + reclaim |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 86984 | Bull si cierre arriba |
| PDL | 84937 | Bear si cierre abajo |
| 0.5 midpoint | 85960 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ✅ | Velas confirman |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Turtle Soup E2

Score **1/6** | Operable: **NO**
_Modo BREAK: breakout de nivel — E2/reversión despriorizada, NO operable_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | NO | Sweep liquidez |
| 3. Reclaim agresivo | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- CRT H1 pending bull — no entrar short contra invalid reciente
- RSI TORYS en contra: Fondo verde TORYS-proxy - filtro long

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **85558.8** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **85558.8** |
| ICT | Base 85558.8 (zona base) · Sweep swing_high @ 85653.6 + reclaim · PD DISCOUNT · H1 PENDING_BULL |
| Plan | Entry **85558.8** · SL **85638.4** · TP **85399.5** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **65%** · ML **83.3%** · Confluencia **MEDIA** — 61% · Rules 83%; Neural gated 60% (medium); ML 83% (high); 2M5 OK; Break vs DISCOUNT (chase) |
| Historial ref | **btc-067** · 2026-10-06 11:13 NY · Entry **86477.8** · **BUENA** — precio cerca de Entry actual + 2M5 OK + zona OK · (MÁS CERCA) · Δ Entry -918.9 pts (-1.063%) · precio→última 918.9 pts (1.063%) · precio→actual 0.0 pts (0.000%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +0.0 pts (0.000%) |
| Dist. a SL | +79.6 pts (0.093%) |
| Dist. a TP | -159.3 pts (0.186%) |
| Riesgo (pts) | 79.6 |
| Winrate setup | ~55% — histórico E1 BTC · SHORT en DISCOUNT -12 (chase Break); CLI BEARISH a favor +2; acuerdo MEDIA -2; 83% reglas |
| Zona PD vs dirección | SHORT en DISCOUNT -12 (chase Break) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **80%** |
| Estado 2M5 | VÁLIDO SHORT (2M5) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 65% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.23× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **OK** · Hist -59.13 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_BTC_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **85558.8** | Retest **85474.7–85551.7** |
| 2M5 SHORT | Sí | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.01% de ref | contexto entry @ 85551.7 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT (condiciones actuales OK)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 85474.7–85551.7 (soporte_debil @ 85551.7) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **85558.8** (limit retest o market al cierre 2ª vela) |
| SL | **85638.4** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **85399.5** (1:2) |
| R:R | **1:2** · riesgo **79.6** pts |
| Invalidación | Cierre M5 > 85638.4 o breakout > 85551.7 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 85558.8 (zona base) · Sweep swing_high @ 85653.6 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ⚠️ |
| 0.5 midpoint | 85960.5 |
| H1 CRT state | **PENDING_BULL** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 85653.6 + reclaim |
| FVG alineados | 5 |
| Order blocks | 4 |
| Entrada | **85558.8** (zona base · sin cambio) |
| Nota | Base 85558.8 (zona base) · Sweep swing_high @ 85653.6 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 85551.7 | **VÁLIDO** — Últimas 2 rojas en zona ≤0.15% | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [✅] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **SHORT**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (437/373) | **SHORT** |
| CRT PD / Premium-Discount | NEUTRAL · DISCOUNT | **LONG** |
| Estructura swings M5 | LL 85552->85464 · LH 86687->85654 | **SHORT** |

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BULL/NEUTRAL | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | BEAR | -DI domina (437/373) |
| Swings | LL 85552->85464 | LH 86687->85654 |

---

## M5 detalle

- RSI M5/H1: 46.0 / 51.1
- Zona: soporte_debil @ 85552
- 2M5 LONG: NO | SHORT: SÍ

### 12 velas M5

- `16:45 O=85699.0 H=85741.2 L=85628.1 C=85630.1 [R]`
- `16:50 O=85640.2 H=85723.9 L=85638.9 C=85652.6 [G]`
- `16:55 O=85653.5 H=85672.1 L=85573.5 C=85583.1 [R]`
- `17:00 O=85574.1 H=85627.3 L=85508.3 C=85530.8 [R]`
- `17:05 O=85529.3 H=85649.9 L=85529.3 C=85648.9 [G]`
- `17:10 O=85648.1 H=85649.6 L=85493.4 C=85543.4 [R]`
- `17:15 O=85541.3 H=85561.7 L=85490.0 C=85495.9 [R]`
- `17:20 O=85497.6 H=85542.8 L=85463.5 C=85538.0 [G]`
- `17:25 O=85538.7 H=85653.6 L=85538.7 C=85615.6 [G]`
- `17:30 O=85615.4 H=85642.7 L=85545.4 C=85637.8 [G]`
- `17:35 O=85635.0 H=85639.8 L=85533.6 C=85577.5 [R]`
- `17:40 O=85577.5 H=85580.7 L=85558.3 C=85558.8 [R]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | SÍ | Velas confirman |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | -DI domina (437/373) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 85559 · reloj FUERA_NY (Lunch) · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 58%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 65.0% | 25% | no alineado; conf=medium; gate×0.65 → 60% |
| ML tabular (gated) | 83.3% | 18% | grade A+; conf=high; → 83% |
| Penalización ubicación | ×0.72 | — | Break bajista en DISCOUNT (chase) |
| Acuerdo entre capas | 61% | 38% | blend 62/38 con acuerdo MEDIA 61% |
| **Probabilidad de éxito** | **58%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 86984: -1424.9 pts (-1.638%)
- **PDL** 84937: +621.5 pts (+0.732%)

### Premium / Discount 0.5

- Midpoint 0.5: **85960**
- Posición precio: **DISCOUNT** (precio 85559)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-06 15:00 O=86583 H=86687 L=85710 C=85710 [R]`
- `10-06 16:00 O=85716 H=85848 L=85552 C=85583 [R]`
- `10-06 17:00 O=85574 H=85654 L=85464 C=85559 [R]`

- Estado CRT H1: **PENDING_BULL** — Sweep low H1 + reclaim

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar | **→** |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 |  |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 65.0% WIN (grade B, conf medium) · gate×0.65 → 60% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | Esperar setup A+ galeria WIN | — | 65% | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_BTC_E1` — alto 1.7 / extremo 2.6 / bajo 0.75 / muy bajo 0.45 / período 84 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_BTC_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **FUERA_NY (Lunch)**
- **Vol relativo:** 0.23× → banda **muy_bajo** (vol×0.23 ≤ muy_bajo 0.45)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -59.13 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-06 17:41 UTC*
