# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-07 15:31 UTC | NY 2026-10-07 11:31 | FUERA_NY (Lunch)
> Precio **51010.9** | HIGH mode | PF E1=4.77 | E2 max 10%
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
**Reglas:** **4 de 6** (66%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~48%** — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patron LOSS similar -12; 66% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 50933-51062; 0.5=50997 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 51706 | Bull si cierre arriba |
| PDL | 51333 | Bear si cierre abajo |
| 0.5 midpoint | 51519 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ❌ | rango bajista |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓ | RSI 52.8 (LONG: neutral) | sin calibrar | n/d | ponderada |
| Zona premium/discount | ✓ | DISCOUNT (a favor) | sin calibrar | n/d | ponderada |
| 2 velas M5 confirman | ✗ | no | sin calibrar | n/d | ponderada |
| Rango CRT coherente | ✗ | rango bajista | sin calibrar | n/d | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Alcista | — | constante en histórico | info |
| R:R mínimo 1:2 | · | 1:2 | — | constante en histórico | info |

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

- Precio < PDL — no long contra rango bajista CRT

### Galería (cross-ref)

- Patrón perdedor similar: contra bias (BTC-01-06-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **51010.9** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **50957.5** |
| ICT | 51010.9→50957.5 · Refinada 51010.9→50957.5 (FVG BULLISH edge) · Sweep swing_high @ 51045.5 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |
| Plan | Entry **50957.5** · SL **50897.5** · TP **51077.5** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Neural **72%** · ML **100.0%** · Confluencia **BAJA** — 38% · Rules 66%; Neural gated 64% (medium); ML 100% (high); 2M5 no listo; Break con fricción CRT |
| Historial ref | **us30-059** · 2026-10-06 18:53 NY · Entry **51596.3** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry -638.8 pts (-1.238%) · precio→última 585.4 pts (1.135%) · precio→actual 53.4 pts (0.105%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | -53.4 pts (0.105%) |
| Dist. a SL | -113.4 pts (0.222%) |
| Dist. a TP | +66.6 pts (0.131%) |
| Riesgo (pts) | 60.0 |
| Winrate setup | ~48% — histórico E1 BTC · LONG en DISCOUNT +2 (zona a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patron LOSS similar -12; 66% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +2 (zona a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **80%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. medium · 72% WIN |
| Rules E1 detalle | **4/6** (66%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.26× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist -26.57 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **51010.9** | Retest **50957.5–51081.8** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.05% de ref | contexto entry @ 51035.9 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BULLISH edge @ 50957.5 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **50957.5** (limit retest o market al cierre 2ª vela) |
| SL | **50897.5** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **51077.5** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 < 50950.9 o breakdown < 51035.9 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 51010.9→50957.5 (FVG BULLISH edge) · Sweep swing_high @ 51045.5 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 51519.4 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 51045.5 + reclaim |
| FVG alineados | 1 |
| Order blocks | 1 |
| Entrada refinada | **50957.5** (antes 51010.9 · FVG BULLISH edge) |
| Nota | Refinada 51010.9→50957.5 (FVG BULLISH edge) · Sweep swing_high @ 51045.5 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en resistencia_debil @ 51035.9 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BEARISH | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 50972->50933 | HH 51036->51046 |

---

## M5 detalle

- RSI M5/H1: 52.8 / 13.2
- Zona: resistencia_debil @ 51036
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:35 O=51009.9 H=51035.9 L=50995.9 C=51016.9 [G]`
- `14:40 O=51017.9 H=51020.9 L=50937.9 C=50941.9 [R]`
- `14:45 O=50942.9 H=50957.5 L=50932.9 C=50953.5 [G]`
- `14:50 O=50954.5 H=50983.5 L=50944.5 C=50979.5 [G]`
- `14:55 O=50978.5 H=51011.5 L=50978.5 C=51004.5 [G]`
- `15:00 O=51005.5 H=51007.5 L=50956.5 C=50964.5 [R]`
- `15:05 O=50965.5 H=50998.5 L=50965.5 C=50984.5 [G]`
- `15:10 O=50985.5 H=51045.5 L=50973.5 C=51007.9 [G]`
- `15:15 O=51008.9 H=51017.9 L=50978.9 C=50996.9 [R]`
- `15:20 O=50995.9 H=51000.9 L=50964.9 C=50995.9 [G]`
- `15:25 O=50996.9 H=51007.9 L=50980.9 C=50991.9 [R]`
- `15:30 O=50992.9 H=51010.9 L=50989.9 C=51010.9 [G]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | NO | rango bajista |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 51011 · reloj FUERA_NY (Lunch) · CRT PD=BEARISH · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 4/6 (66%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 51%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 4/6 | 28% | 66% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango bajista |
| Neural galería (gated) | 71.8% | 25% | alineado WIN; conf=medium; gate×0.65 → 64% |
| ML tabular (gated) | 100.0% | 18% | grade A+; conf=high; → 100% |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.03 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 38% | 38% | blend 62/38 con acuerdo BAJA 38% |
| **Probabilidad de éxito** | **51%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 51706: -694.6 pts (-1.343%)
- **PDL** 51333: -322.5 pts (-0.628%)

### Premium / Discount 0.5

- Midpoint 0.5: **51519**
- Posición precio: **DISCOUNT** (precio 51011)
- Lectura PD: **BEARISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-07 13:00 O=51160 H=51251 L=51022 C=51034 [R]`
- `10-07 14:00 O=51034 H=51062 L=50933 C=51004 [R]`
- `10-07 15:00 O=51006 H=51046 L=50956 C=51011 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 50933-51062; 0.5=50997

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

**Acuerdo Rules/Neural:** ALIGNED

- ML y Neural apuntan misma dirección de confianza

- **Neural galería:** 71.8% WIN (grade B, conf medium) · gate×0.65 → 64% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 72% | contra-bias, LOSS |

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
- **Vol relativo:** 0.26× → banda **muy_bajo** (vol×0.26 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: -26.57 · soft-filter vs setup: **en contra**
- **Strategy A (última H4):** SELL cross (EMA200 filter)
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
*high signal | 2026-10-07 15:31 UTC*
