# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-16 16:15 UTC | NY 2026-10-16 12:15 | FUERA_NY (Lunch)
> Precio **4168.98** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-16 16:15 UTC** · hace 0 min · fuente MT5 XAUUSD (broker, M5/H1)
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
- Breakout bajista sostenido < 4171

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **4 de 6** (66%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~51%** — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo BAJA -8; patrones mixtos -4; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **PENDING_BULL** | Sweep low H1 + reclaim |
| Fakeout PDH | SÍ — NO LONG | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4177 | Bull si cierre arriba |
| PDL | 4111 | Bear si cierre abajo |
| 0.5 midpoint | 4144 | Filtro 50% |

**Nota CRT:** Fakeout PDH: NO long E1; CRT invalid bearish | BREAK pendiente: Breakout bajista sostenido < 4171 | Fakeout ≠ Break — no tratar sweep+reclaim como breakout

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | RSI 22 sobrevendido |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✗ | RSI 22.0 (SHORT: extendido) | sin calibrar | n/d | ponderada |
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
- CRT H1 pending bull — no entrar short contra invalid reciente

### Galería (cross-ref)

- Patrón ganador similar: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4168.98** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **4172.89** |
| ICT | 4168.98→4172.89 · Refinada 4169.0→4172.9 (FVG BEARISH edge) · Sweep PDH @ 4177.2 + reclaim · PD PREMIUM · H1 PENDING_BULL |
| Plan | Entry **4172.89** · SL **4178.89** · TP **4160.89** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **68%** · ML **66.7%** · Confluencia **BAJA** — 41% · Rules 66%; Neural gated 62% (medium); ML 67% (medium); 2M5 no listo; Break operable |
| Historial ref | **xauusd-077** · 2026-10-16 11:10 NY · Entry **4191.11** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry -18.22 pts (-0.435%) · precio→última 22.13 pts (0.528%) · precio→actual 3.91 pts (0.094%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| R:R | 1:2 |
| Dist. a Entry | +3.91 pts (0.094%) |
| Dist. a SL | +9.91 pts (0.238%) |
| Dist. a TP | -8.09 pts (0.194%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~51% — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); CLI BEARISH a favor +2; acuerdo BAJA -8; patrones mixtos -4; 66% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +2 (zona a favor) |
| Bias vs dirección | CLI BEARISH a favor +2 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 68% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.02× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist 3.524 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4168.98** | Retest **4167.59–4172.89** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.06% de ref | contexto entry @ 4171.34 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 4172.89 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **4172.89** (limit retest o market al cierre 2ª vela) |
| SL | **4178.89** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4160.89** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 > 4174.98 o breakout > 4171.34 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4169.0→4172.9 (FVG BEARISH edge) · Sweep PDH @ 4177.2 + reclaim · PD PREMIUM · H1 PENDING_BULL |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 4144.18 |
| H1 CRT state | **PENDING_BULL** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDH @ 4177.2 + reclaim |
| FVG alineados | 5 |
| Order blocks | 5 |
| Entrada refinada | **4172.89** (antes 4168.98 · FVG BEARISH edge) |
| Nota | Refinada 4169.0→4172.9 (FVG BEARISH edge) · Sweep PDH @ 4177.2 + reclaim · PD PREMIUM · H1 PENDING_BULL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 4171.34 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
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

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **SHORT**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (23/7) | **SHORT** |
| CRT PD / Premium-Discount | NEUTRAL · PREMIUM | **SHORT** |
| Estructura swings M5 | HL 4155->4160 · HH 4181->4199 | **LONG** |

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BULL/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (23/7) |
| Swings | HL 4155->4160 | HH 4181->4199 |

---

## M5 detalle

- RSI M5/H1: 22.0 / 46.2
- Zona: soporte_debil @ 4171
- 2M5 LONG: SÍ | SHORT: NO

### 12 velas M5

- `15:20 O=4179.93 H=4180.21 L=4174.91 C=4176.64 [R]`
- `15:25 O=4176.60 H=4177.11 L=4173.52 C=4175.47 [R]`
- `15:30 O=4175.46 H=4177.09 L=4174.40 C=4176.49 [G]`
- `15:35 O=4176.52 H=4178.47 L=4175.18 C=4177.51 [G]`
- `15:40 O=4177.54 H=4177.68 L=4172.89 C=4173.06 [R]`
- `15:45 O=4173.08 H=4175.98 L=4170.94 C=4171.70 [R]`
- `15:50 O=4171.75 H=4172.50 L=4170.00 C=4171.08 [R]`
- `15:55 O=4170.97 H=4172.14 L=4167.42 C=4167.70 [R]`
- `16:00 O=4167.87 H=4169.58 L=4159.98 C=4166.26 [R]`
- `16:05 O=4166.27 H=4167.88 L=4163.50 C=4164.52 [R]`
- `16:10 O=4164.76 H=4169.62 L=4164.31 C=4168.73 [G]`
- `16:15 O=4168.50 H=4168.98 L=4168.27 C=4168.98 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | RSI 22 sobrevendido |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | -DI domina (23/7) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4169 · reloj FUERA_NY (Lunch) · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 68.4% | 25% | no alineado; conf=medium; gate×0.65 → 62% |
| ML tabular (gated) | 66.7% | 18% | grade B; conf=medium; → 63% |
| Bonificación ubicación | ×1.03 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 41% | 38% | blend 62/38 con acuerdo BAJA 41% |
| **Probabilidad de éxito** | **61%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4177: -8.2 pts (-0.197%)
- **PDL** 4111: +57.8 pts (+1.407%)

### Premium / Discount 0.5

- Midpoint 0.5: **4144**
- Posición precio: **PREMIUM** (precio 4169)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

1. Wick M5 superó PDH en últimas ~18 velas
2. Precio actual **por debajo** de PDH → trampa alcista
3. **Acción:** NO long E1 · CRT invalid bearish · posible short en reclaim

### Timeline H1 (últimas 3 velas)

- `10-16 14:00 O=4185 H=4199 L=4181 C=4185 [G]`
- `10-16 15:00 O=4185 H=4187 L=4167 C=4168 [R]`
- `10-16 16:00 O=4168 H=4170 L=4160 C=4169 [G]`

- Estado CRT H1: **PENDING_BULL** — Sweep low H1 + reclaim

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

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 68.4% WIN (grade B, conf medium) · gate×0.65 → 62% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26) | BTC-11-05-26.png | 68% | sweep+reclaim, WIN |
| 2 | LOSS: fakeout (BTC-22-05-26) | BTC-22-05-26.png | 63% | fakeout, LOSS |
| 3 | LOSS: fakeout tratado como breakout — no es Break | — | 58% | continuación, fakeout, LOSS |

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
- **Vol relativo:** 0.02× → banda **muy_bajo** (vol×0.02 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 3.524 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-16 16:15 UTC*
