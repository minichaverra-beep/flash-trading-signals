# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-15 13:23 UTC | NY 2026-10-15 09:23 | NY AM 08-10
> Precio **4158.15** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-15 13:20 UTC** · hace 3 min · fuente MT5 XAUUSDm (broker, M5/H1)
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

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~72%** — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo MEDIA -2; patron WIN similar +3; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **PENDING_BEAR** | Sweep high H1 sin hold |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4171 | Bull si cierre arriba |
| PDL | 4073 | Bear si cierre abajo |
| 0.5 midpoint | 4122 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 55 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓ | RSI 55.0 (SHORT: neutral) | sin calibrar | n/d | ponderada |
| Zona premium/discount | ✓ | PREMIUM (a favor) | sin calibrar | n/d | ponderada |
| 2 velas M5 confirman | ✗ | no | sin calibrar | n/d | ponderada |
| Rango CRT coherente | ✓ | No forzar; esperar pending CRT HTF | Mod | sin calibrar | n/d | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Bajista | — | constante en histórico | info |
| R:R mínimo 1:2 | · | 1:2 | — | constante en histórico | info |

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

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4158.15** |
| Veredicto | **Esperar** (SHORT) |
| Entrada óptima | **4158.16** |
| ICT | Base 4158.2 (zona base) · Sweep swing_high @ 4159.4 + reclaim · PD PREMIUM · H1 PENDING_BEAR · killzone NY AM 08-10 |
| Plan | Entry **4158.16** · SL **4166.29** · TP **4141.89** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **50%** · ML **8.6%** · Confluencia **MEDIA** — 50% · Rules 83%; Neural débil/gating 50% conf=low; ML 9% veto suave; 2M5 no listo; Break operable |
| Historial ref | **xauusd-055** · 2026-10-14 18:56 NY · Entry **4105.94** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry +52.22 pts (+1.272%) · precio→última 52.21 pts (1.272%) · precio→actual 0.01 pts (0.000%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +0.01 pts (0.000%) |
| Dist. a SL | +8.15 pts (0.196%) |
| Dist. a TP | -16.26 pts (0.391%) |
| Riesgo (pts) | 8.13 |
| Winrate setup | ~72% — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo MEDIA -2; patron WIN similar +3; 83% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +2 (zona a favor) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **C** · conf. low · 50% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **normal** · 1.26× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist -0.2348 · never trigger |
| Watchtower KZ | NY AM 08-10 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4158.15** | Retest **4155.11–4158.85** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.02% de ref | contexto entry @ 4158.85 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 4155.11–4158.85 (resistencia_debil @ 4158.85) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **4158.16** (limit retest o market al cierre 2ª vela) |
| SL | **4166.29** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4141.89** (1:2) |
| R:R | **1:2** · riesgo **8.13** pts |
| Invalidación | Cierre M5 > 4166.29 o breakout > 4158.85 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 4158.2 (zona base) · Sweep swing_high @ 4159.4 + reclaim · PD PREMIUM · H1 PENDING_BEAR · killzone NY AM 08-10 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 4121.86 |
| H1 CRT state | **PENDING_BEAR** |
| Killzone / sesión | NY AM 08-10 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4159.4 + reclaim |
| FVG alineados | 3 |
| Order blocks | 2 |
| Entrada | **4158.16** (zona base · sin cambio) |
| Nota | Base 4158.2 (zona base) · Sweep swing_high @ 4159.4 + reclaim · PD PREMIUM · H1 PENDING_BEAR · killzone NY AM 08-10 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 4158.85 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 08-10_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **NEUTRAL**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | +DI domina (53/43) | **LONG** |
| CRT PD / Premium-Discount | NEUTRAL · PREMIUM | **SHORT** |
| Estructura swings M5 | LL 4144->4130 · HH 4159->4159 | **NEUTRAL** |

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BEAR/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (53/43) |
| Swings | LL 4144->4130 | HH 4159->4159 |

---

## M5 detalle

- RSI M5/H1: 55.0 / 69.6
- Zona: resistencia_debil @ 4159
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `12:25 O=4153.09 H=4154.14 L=4148.22 C=4153.80 [G]`
- `12:30 O=4153.59 H=4154.97 L=4130.32 C=4137.48 [R]`
- `12:35 O=4137.54 H=4159.35 L=4137.54 C=4156.42 [G]`
- `12:40 O=4156.33 H=4156.69 L=4145.97 C=4145.97 [R]`
- `12:45 O=4146.23 H=4146.45 L=4139.93 C=4142.64 [R]`
- `12:50 O=4142.73 H=4148.58 L=4141.98 C=4143.69 [G]`
- `12:55 O=4143.99 H=4153.13 L=4143.27 C=4151.85 [G]`
- `13:00 O=4152.10 H=4154.83 L=4144.15 C=4144.60 [R]`
- `13:05 O=4144.55 H=4149.68 L=4144.39 C=4146.73 [G]`
- `13:10 O=4146.79 H=4157.61 L=4146.04 C=4157.54 [G]`
- `13:15 O=4157.60 H=4168.56 L=4157.59 C=4163.75 [G]`
- `13:20 O=4163.86 H=4163.93 L=4155.77 C=4158.15 [R]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 55 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | +DI domina (53/43) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4158 · reloj NY AM 08-10 · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** ESPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score combinado 59%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 49.8% | 25% | no alineado; conf=low; gate×0.17 → 50% |
| ML tabular (gated) | 8.6% | 18% | grade C; conf=high; → 9% |
| Bonificación ubicación | ×1.03 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 50% | 38% | blend 62/38 con acuerdo MEDIA 50% |
| **Probabilidad de éxito** | **59%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4171: -12.4 pts (-0.297%)
- **PDL** 4073: +85.0 pts (+2.086%)

### Premium / Discount 0.5

- Midpoint 0.5: **4122**
- Posición precio: **PREMIUM** (precio 4158)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-15 11:00 O=4155 H=4159 L=4145 C=4145 [R]`
- `10-15 12:00 O=4145 H=4159 L=4130 C=4152 [G]`
- `10-15 13:00 O=4152 H=4169 L=4144 C=4158 [G]`

- Estado CRT H1: **PENDING_BEAR** — Sweep high H1 sin hold

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

**Acuerdo Rules/Neural:** ALIGNED

- ML y Neural apuntan misma dirección de confianza

- **Neural galería:** 49.8% WIN (grade C, conf low) · gate×0.17 → 50% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 50% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 08-10**
- **Vol relativo:** 1.26× → banda **normal** (vol×1.26 en rango normal)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -0.2348 · soft-filter vs setup: **alineado**
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

- **Reporte:** `live/xauusd_m5_high_signal.md`
- **Chart:** **Preview en navegador**


---
*high signal | 2026-10-15 13:23 UTC*
