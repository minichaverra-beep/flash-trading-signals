# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-05 14:51 UTC | NY 2026-10-05 10:51 | NY AM 10-11
> Precio **4143.50** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-05 14:50 UTC** · hace 1 min · fuente MT5 XAUUSD (broker, M5/H1)
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
- Fakeout PDH (barrido + reclaim) — NO es Break; es contexto Reverse

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~48%** — histórico E1 BTC · LONG en PREMIUM -12 (chase Break); H1 BEARISH vs LONG -6; acuerdo MEDIA -2; patron LOSS similar -12; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4131-4158; 0.5=4145 |
| Fakeout PDH | SÍ — NO LONG | CRT invalid bear |
| Fakeout PDL | SÍ — E2 watch | Turtle soup ctx |
| PDH | 4148 | Bull si cierre arriba |
| PDL | 4133 | Bear si cierre abajo |
| 0.5 midpoint | 4141 | Filtro 50% |

**Nota CRT:** Fakeout PDH: NO long E1; CRT invalid bearish | Fakeout PDL: turtle soup E2 watch | BREAK inválido: Fakeout PDH (barrido + reclaim) — NO es Break; es contexto Reverse | Fakeout ≠ Break — no tratar sweep+reclaim como breakout

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ✅ | Velas confirman |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ❌ | trampa en máximo ayer — no long |

### Turtle Soup E2

Score **3/6** | Operable: **NO**
_Modo BREAK: breakout de nivel — E2/reversión despriorizada, NO operable_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | SÍ | Fakeout PDL macro |
| 2. Rompe min/max previo | SÍ | PDL barrido |
| 3. Reclaim agresivo | SÍ | Reclaim post PDL |
| 4. Entrada zona SL original | NO | Cerca nivel barrido |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Red flags

- Fakeout PDH — NO long E1; CRT invalid bearish
- Fakeout PDL — NO chase E1; contexto E2 turtle soup
- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Patrón perdedor similar: fakeout (BTC-22-05-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4143.50** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **4140.52** |
| ICT | 4147.73→4140.52 · Refinada 4147.7→4140.5 (discount 0.5) · Sweep PDH @ 4148.2 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |
| Plan | Entry **4140.52** · SL **4134.52** · TP **4152.52** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **74%** · ML **63.6%** · Confluencia **MEDIA** — 65% · Rules 83%; Neural gated 65% (medium); ML 64% zona media; 2M5 OK; Break vs PREMIUM (chase) |
| Historial ref | **xauusd-027** · 2026-10-05 10:15 NY · Entry **4143.00** · **BUENA** — precio cerca de última Entry + 2M5 OK + zona OK · (MISMA ZONA) · Δ Entry -2.48 pts (-0.060%) · precio→última 0.50 pts (0.012%) · precio→actual 2.98 pts (0.072%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | -2.98 pts (0.072%) |
| Dist. a SL | -8.98 pts (0.217%) |
| Dist. a TP | +9.02 pts (0.218%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~48% — histórico E1 BTC · LONG en PREMIUM -12 (chase Break); H1 BEARISH vs LONG -6; acuerdo MEDIA -2; patron LOSS similar -12; 83% reglas |
| Zona PD vs dirección | LONG en PREMIUM -12 (chase Break) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **80%** |
| Estado 2M5 | VÁLIDO LONG (2M5) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 74% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.36× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist 1.243 · never trigger |
| Watchtower KZ | NY AM 10-11 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4143.50** | Retest **4140.52–4150.79** |
| 2M5 LONG | Sí | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.09% de ref | contexto entry @ 4147.06 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG (condiciones actuales OK)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest discount 0.5 @ 4140.52 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **4140.52** (limit retest o market al cierre 2ª vela) |
| SL | **4134.52** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4152.52** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 < 4141.73 o breakdown < 4147.06 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4147.7→4140.5 (discount 0.5) · Sweep PDH @ 4148.2 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ⚠️ |
| 0.5 midpoint | 4140.52 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY AM 10-11 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDH @ 4148.2 + reclaim |
| FVG alineados | 3 |
| Order blocks | 1 |
| Entrada refinada | **4140.52** (antes 4147.73 · discount 0.5) |
| Nota | Refinada 4147.7→4140.5 (discount 0.5) · Sweep PDH @ 4148.2 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 4147.06 | **VÁLIDO** — Últimas 2 verdes en zona ≤0.15% | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 10-11_

- [✅] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [❌] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | BULL | +DI domina (22/17) |
| Swings | HL 4131->4133 | LH 4166->4147 |

---

## M5 detalle

- RSI M5/H1: 56.6 / 44.3
- Zona: soporte_debil @ 4147
- 2M5 LONG: SÍ | SHORT: NO

### 12 velas M5

- `13:55 O=4139.99 H=4140.01 L=4134.37 C=4135.73 [R]`
- `14:00 O=4135.83 H=4146.48 L=4135.13 C=4138.88 [G]`
- `14:05 O=4138.84 H=4147.34 L=4138.83 C=4145.78 [G]`
- `14:10 O=4145.79 H=4146.55 L=4140.48 C=4142.50 [R]`
- `14:15 O=4142.49 H=4142.91 L=4139.00 C=4139.50 [R]`
- `14:20 O=4139.48 H=4142.36 L=4139.15 C=4140.47 [G]`
- `14:25 O=4140.48 H=4142.21 L=4137.10 C=4137.60 [R]`
- `14:30 O=4137.62 H=4137.90 L=4132.70 C=4134.31 [R]`
- `14:35 O=4134.30 H=4138.22 L=4133.83 C=4137.80 [G]`
- `14:40 O=4137.73 H=4142.44 L=4136.89 C=4140.75 [G]`
- `14:45 O=4140.77 H=4142.17 L=4137.09 C=4141.28 [G]`
- `14:50 O=4141.27 H=4144.27 L=4141.10 C=4143.50 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | SÍ | Velas confirman |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | NO | trampa en máximo ayer — no long |
| DMI alineado | SÍ | +DI domina (22/17) |
| 0.5 midpoint E1 | NO | premium — no long E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4144 · reloj NY AM 10-11 · CRT PD=NEUTRAL · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 50%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | fail | 12% | trampa en máximo ayer — no long |
| Neural galería (gated) | 73.7% | 25% | alineado WIN; conf=medium; gate×0.65 → 65% |
| ML tabular (gated) | 63.6% | 18% | grade B; conf=medium; → 60% |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Penalización ubicación | ×0.72 | — | Break alcista en PREMIUM (chase) |
| Acuerdo entre capas | 65% | 38% | blend 62/38 con acuerdo MEDIA 65% |
| **Probabilidad de éxito** | **50%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4148: -4.7 pts (-0.114%)
- **PDL** 4133: +10.7 pts (+0.259%)

### Premium / Discount 0.5

- Midpoint 0.5: **4141**
- Posición precio: **PREMIUM** (precio 4144)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

1. Wick M5 superó PDH en últimas ~18 velas
2. Precio actual **por debajo** de PDH → trampa alcista
3. **Acción:** NO long E1 · CRT invalid bearish · posible short en reclaim

### Timeline H1 (últimas 3 velas)

- `10-05 12:00 O=4156 H=4166 L=4154 C=4157 [G]`
- `10-05 13:00 O=4157 H=4158 L=4131 C=4136 [R]`
- `10-05 14:00 O=4136 H=4147 L=4133 C=4144 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 4131-4158; 0.5=4145

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar | **→** |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 | **→** |
| Fakeout PDL | Contexto E2 turtle soup | **→** |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 73.7% WIN (grade B, conf medium) · gate×0.65 → 65% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | LOSS: fakeout (BTC-22-05-26) | BTC-22-05-26.png | 74% | fakeout, LOSS |
| 2 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 69% | contra-bias, LOSS |
| 3 | LOSS: fakeout tratado como breakout — no es Break | — | 64% | continuación, fakeout, LOSS |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY AM 10-11**
- **Vol relativo:** 0.36× → banda **muy_bajo** (vol×0.36 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 1.243 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-05 14:51 UTC*
