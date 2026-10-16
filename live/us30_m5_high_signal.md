# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-16 16:13 UTC | NY 2026-10-16 12:13 | FUERA_NY (Lunch)
> Precio **52175.2** | HIGH mode | PF E1=4.77 | E2 max 10%
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
**Reglas:** **4 de 6** (66%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~48%** — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo BAJA -8; patron LOSS similar -12; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **COMPLETED_BEAR** | Low H1 52187 alcanzado |
| Fakeout PDH | SÍ — NO LONG | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 52261 | Bull si cierre arriba |
| PDL | 51542 | Bear si cierre abajo |
| 0.5 midpoint | 51901 | Filtro 50% |

**Nota CRT:** Fakeout PDH: NO long E1; CRT invalid bearish | BREAK pendiente: Sin breakout de nivel detectado | Fakeout ≠ Break — no tratar sweep+reclaim como breakout

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | RSI 17 sobrevendido |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✗✗ | RSI 17.2 (SHORT: muy extendido) | sin calibrar | n/d | ponderada |
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

- Fakeout PDH — NO long E1; CRT invalid bearish
- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar

### Galería (cross-ref)

- Patrón perdedor similar: fakeout (BTC-22-05-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **52175.2** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **52187.2** |
| ICT | 52175.2→52187.2 · Refinada 52175.2→52187.2 (FVG BEARISH edge) · Sweep PDH @ 52261.3 + reclaim · PD PREMIUM · H1 COMPLETED_BEAR |
| Plan | Entry **52187.2** · SL **52247.2** · TP **52067.2** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **72%** · ML **0.0%** · Confluencia **BAJA** — 36% · Rules 66%; Neural gated 64% (medium); ML 0% veto suave; 2M5 no listo; Break operable |
| Historial ref | **us30-073** · 2026-10-16 12:11 NY · Entry **52168.0** · **BUENA** — precio cerca de última Entry + zona OK · (MISMA ZONA) · Δ Entry +19.2 pts (+0.037%) · precio→última 7.2 pts (0.014%) · precio→actual 12.0 pts (0.023%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +12.0 pts (0.023%) |
| Dist. a SL | +72.0 pts (0.138%) |
| Dist. a TP | -108.0 pts (0.207%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~48% — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo BAJA -8; patron LOSS similar -12; 66% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +2 (zona a favor) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **bajo** · 0.70× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist 26.48 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **52175.2** | Retest **52111.1–52187.2** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.03% de ref | contexto entry @ 52158.1 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 52187.2 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **52187.2** (limit retest o market al cierre 2ª vela) |
| SL | **52247.2** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **52067.2** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 52235.2 o breakout > 52158.1 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 52175.2→52187.2 (FVG BEARISH edge) · Sweep PDH @ 52261.3 + reclaim · PD PREMIUM · H1 COMPLETED_BEAR |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 51901.4 |
| H1 CRT state | **COMPLETED_BEAR** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDH @ 52261.3 + reclaim |
| FVG alineados | 5 |
| Order blocks | 4 |
| Entrada refinada | **52187.2** (antes 52175.2 · FVG BEARISH edge) |
| Nota | Refinada 52175.2→52187.2 (FVG BEARISH edge) · Sweep PDH @ 52261.3 + reclaim · PD PREMIUM · H1 COMPLETED_BEAR |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 52158.1 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman SHORT
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
| DMI (momentum M5) | -DI domina (307/64) | **SHORT** |
| CRT PD / Premium-Discount | NEUTRAL · PREMIUM | **SHORT** |
| Estructura swings M5 | LL 52310->52266 · LH 52430->52322 | **SHORT** |

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BEAR/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (307/64) |
| Swings | LL 52310->52266 | LH 52430->52322 |

---

## M5 detalle

- RSI M5/H1: 17.2 / 46.2
- Zona: soporte_debil @ 52158
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `15:15 O=52372.3 H=52384.3 L=52326.3 C=52342.8 [R]`
- `15:20 O=52342.3 H=52361.3 L=52271.3 C=52286.3 [R]`
- `15:25 O=52287.3 H=52294.3 L=52265.8 C=52288.3 [G]`
- `15:30 O=52289.3 H=52321.3 L=52279.3 C=52309.3 [G]`
- `15:35 O=52308.8 H=52319.8 L=52298.3 C=52318.3 [G]`
- `15:40 O=52317.8 H=52322.2 L=52273.2 C=52275.2 [R]`
- `15:45 O=52274.2 H=52314.8 L=52242.3 C=52248.3 [R]`
- `15:50 O=52247.3 H=52272.8 L=52235.8 C=52238.2 [R]`
- `15:55 O=52237.2 H=52239.2 L=52187.2 C=52187.2 [R]`
- `16:00 O=52188.2 H=52191.2 L=52124.3 C=52159.2 [R]`
- `16:05 O=52161.2 H=52172.2 L=52135.3 C=52158.3 [R]`
- `16:10 O=52157.3 H=52177.2 L=52150.3 C=52175.2 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | RSI 17 sobrevendido |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | -DI domina (307/64) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 52175 · reloj FUERA_NY (Lunch) · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 51%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 0.0% | 18% | grade C; conf=high; → 0% |
| Bonificación ubicación | ×1.03 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 36% | 38% | blend 62/38 con acuerdo BAJA 36% |
| **Probabilidad de éxito** | **51%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 52261: -86.1 pts (-0.165%)
- **PDL** 51542: +633.7 pts (+1.229%)

### Premium / Discount 0.5

- Midpoint 0.5: **51901**
- Posición precio: **PREMIUM** (precio 52175)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

1. Wick M5 superó PDH en últimas ~18 velas
2. Precio actual **por debajo** de PDH → trampa alcista
3. **Acción:** NO long E1 · CRT invalid bearish · posible short en reclaim

### Timeline H1 (últimas 3 velas)

- `10-16 14:00 O=52537 H=52582 L=52310 C=52400 [R]`
- `10-16 15:00 O=52401 H=52430 L=52187 C=52187 [R]`
- `10-16 16:00 O=52188 H=52191 L=52124 C=52175 [R]`

- Estado CRT H1: **COMPLETED_BEAR** — Low H1 52187 alcanzado

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar | **→** |
| Cierre > PDH | Sesgo alcista — long pullback |  |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 | **→** |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** CONFLICT

- Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual fuerte pero features ML desfavorables; priorizar Rules % + CRT

- **Neural galería:** 71.8% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | LOSS: fakeout (BTC-22-05-26) | BTC-22-05-26.png | 72% | fakeout, LOSS |
| 2 | LOSS: fakeout tratado como breakout — no es Break | — | 67% | continuación, fakeout, LOSS |

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
- **Vol relativo:** 0.70× → banda **bajo** (vol×0.70 ≤ bajo 0.7)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 26.48 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-16 16:13 UTC*
