# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-07 15:17 UTC | NY 2026-10-07 11:17 | FUERA_NY (Lunch)
> Precio **83062.5** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **AUTO** |
| Modo setup | **AUTO** |

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario | E2 watch only
**Tendencia:** Bajista
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~46%** — calibrado walk-forward BTC E1 · 80%: 44–48% · n=2097 (n_eff 755) · EV +0.18R

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BULL** | Sweep low H1 + reclaim |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 86687 | Bull si cierre arriba |
| PDL | 85088 | Bear si cierre abajo |
| 0.5 midpoint | 85888 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ✅ | Shorts E1 rechazo resistencia (premium) |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: impacto medido walk-forward n=2097 (n_eff 755)._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ~ | RSI 42.7 (SHORT: neutral) | +0.4 pts | esta zona 45% (n=528) | ponderada |
| Zona premium/discount | ~ | DISCOUNT (en contra) | -0.7 pts | a favor 55% / en contra 45% | ponderada |
| 2 velas M5 confirman | ~ | no | +0.2 pts | sí 43% / no 47% | ponderada |
| Rango CRT coherente | ~ | Shorts E1 rechazo resistencia (premium) | +0.2 pts | sí 46% / no 45% | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Bajista | — | constante en histórico | info |
| R:R mínimo 1:2 | · | 1:2 | — | constante en histórico | info |

### Turtle Soup E2

Score **3/6** | Operable: **NO**
_E2 max 10%; PF E1=4.77; PROHIBIDO eval (TRADING_VISUAL SS7)_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | SÍ | Sweep swing low + reclaim |
| 3. Reclaim agresivo | SÍ | Reclaim M5 |
| 4. Entrada zona SL original | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Red flags

- CRT H1 pending bull — no entrar short contra invalid reciente
- RSI TORYS en contra: Fondo verde TORYS-proxy - filtro long

### Galería (cross-ref)

- Patrón ganador similar: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **83062.5** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **83062.5** |
| ICT | Base 83062.5 (zona base) · Sweep swing_high @ 83353.4 + reclaim · PD DISCOUNT · H1 PENDING_BULL |
| Plan | Entry **83062.5** · SL **83190.4** · TP **82806.8** |
| E2 / Break | Vigilar reversión E2 — E1 primario | E2 watch only |
| Métricas | Rules **66%** · Confluencia **MEDIA** — 50% · Rules 66%; 2M5 no listo; Setup auto con dirección; H1 alineado; Vol bajo |
| Historial ref | **btc-074** · 2026-10-07 09:45 NY · Entry **83076.0** · **BUENA** — precio cerca de última Entry + zona OK + bando alineado · (MISMA ZONA) · Δ Entry -13.5 pts (-0.016%) · precio→última 13.5 pts (0.016%) · precio→actual 0.0 pts (0.000%) |
| Bando usado (lado asumido) | **AUTO** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | +0.0 pts (0.000%) |
| Dist. a SL | +127.9 pts (0.154%) |
| Dist. a TP | -255.8 pts (0.308%) |
| Riesgo (pts) | 127.9 |
| Winrate setup | ~46% — calibrado walk-forward BTC E1 · 80%: 44–48% · n=2097 (n_eff 755) · EV +0.18R |
| Zona PD vs dirección | SHORT en DISCOUNT -7 (vs zona) |
| Bias vs dirección | H1 BEARISH a favor +4 |
| Score Rules extendido | **70%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **AUTO** |
| Calidad break/reverse | AUTO |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **bajo** · 0.63× · Zentinel_BTC_E1 |
| MACD-quant (filtro) | **OK** · Hist -330.1 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_BTC_E1 |
| Chart | — |

---


---

## Entrada optimizada (E1)

> Bias **AUTO** + **AUTO** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **83062.5** | Retest **82864.4–82939.1** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.15% de ref | contexto entry @ 82939.1 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 82864.4–82939.1 (soporte_debil @ 82939.1) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **83062.5** (limit retest o market al cierre 2ª vela) |
| SL | **83190.4** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **82806.8** (1:2) |
| R:R | **1:2** · riesgo **127.9** pts |
| Invalidación | Cierre M5 > 83190.4 o breakout > 82939.1 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 83062.5 (zona base) · Sweep swing_high @ 83353.4 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ⚠️ |
| 0.5 midpoint | 85887.9 |
| H1 CRT state | **PENDING_BULL** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 83353.4 + reclaim |
| FVG alineados | 3 |
| Order blocks | 5 |
| Entrada | **83062.5** (zona base · sin cambio) |
| Nota | Base 83062.5 (zona base) · Sweep swing_high @ 83353.4 + reclaim · PD DISCOUNT · H1 PENDING_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 82939.1 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BULL/BEARISH | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | BEAR | -DI domina (622/463) |
| Swings | HL 82709->82939 | LH 83527->83353 |

---

## M5 detalle

- RSI M5/H1: 42.7 / 24.0
- Zona: soporte_debil @ 82939
- 2M5 LONG: SÍ | SHORT: NO

### 12 velas M5

- `14:20 O=83000.1 H=83153.1 L=82975.9 C=83145.1 [G]`
- `14:25 O=83144.1 H=83216.8 L=82966.0 C=83027.4 [R]`
- `14:30 O=83021.0 H=83140.1 L=82985.8 C=83098.0 [G]`
- `14:35 O=83109.1 H=83165.1 L=82968.4 C=82987.6 [R]`
- `14:40 O=83003.2 H=83029.1 L=82911.8 C=82935.7 [R]`
- `14:45 O=82935.4 H=83024.4 L=82903.3 C=82955.0 [G]`
- `14:50 O=82954.3 H=83007.3 L=82913.0 C=82993.0 [G]`
- `14:55 O=82993.9 H=82997.7 L=82881.8 C=82974.7 [R]`
- `15:00 O=82974.6 H=82974.6 L=82845.1 C=82874.9 [R]`
- `15:05 O=82861.5 H=82938.3 L=82773.1 C=82884.1 [G]`
- `15:10 O=82883.0 H=83118.0 L=82883.0 C=83036.0 [G]`
- `15:15 O=83036.1 H=83131.5 L=83020.7 C=83062.5 [G]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | SÍ | Shorts E1 rechazo resistencia (premium) |
| DMI alineado | SÍ | -DI domina (622/463) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 83063 · reloj FUERA_NY (Lunch) · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **AUTO** · reglas E1 4/6 (66%)
- **Bando:** AUTO — mercado H1 **BEARISH** guía dirección
- **Veredicto integrado:** NO_OPERAR — probabilidad calibrada 46% (80%: 44–48%) · EV +0.18R
- **Fusión heurística anterior:** 60% (referencia; sin calibrar)

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | info | 66% OK |
| Rules extendidas (10) | 70% | info | meta >70% |
| CRT coherence | pass | info | Shorts E1 rechazo resistencia (premium) |
| Neural galería | n/d | — | omitido — sin chart/modelo (no pad 50%) |
| ML tabular | n/d | — | omitido — sin --ml o modelo |
| Penalización ubicación | ×0.88 | — | SHORT en DISCOUNT |
| Acuerdo entre capas | 50% | info | blend 62/38 con acuerdo MEDIA 50% |
| Fusión heurística (anterior) | 60% | info | pesos fijos sin backtest |
| Capas ML/Neural en el % | ninguna (ML/Neural sin validación OOS) | — | solo si mejoran fuera de muestra |
| EV por operación | +0.18R | — | R:R 1:2 · costo 0.21R · Kelly¼ 2.0% riesgo |
| **Probabilidad de éxito** | **46%** | 80%: 44–48% | calibrado walk-forward · n=2097 (n_eff 755) |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 86687: -3624.8 pts (-4.182%)
- **PDL** 85088: -2025.9 pts (-2.381%)

### Premium / Discount 0.5

- Midpoint 0.5: **85888**
- Posición precio: **DISCOUNT** (precio 83063)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-07 13:00 O=83460 H=83527 L=82709 C=83140 [R]`
- `10-07 14:00 O=83137 H=83275 L=82882 C=82975 [R]`
- `10-07 15:00 O=82975 H=83131 L=82773 C=83060 [G]`

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

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** NEUTRAL

- Sin datos ML/Neural


---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26) | BTC-11-05-26.png | heurística | sweep+reclaim, WIN |

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
- **Vol relativo:** 0.63× → banda **bajo** (vol×0.63 ≤ bajo 0.75)
- **Bias table:** avg 3 · neutral 0.5%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -330.1 · soft-filter vs setup: **alineado**
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
- **Reporte (abs):** `D:\Danilo\Trading\Cursor Trading\live\btc_m5_high_signal.md`


---
*high signal | 2026-10-07 15:17 UTC*
