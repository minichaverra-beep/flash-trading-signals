# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-03 22:36 UTC | NY 2026-09-03 18:36 | FUERA_NY
> Precio **81094.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Breakout alcista sostenido > 77792

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **6 de 7** (85%) | Extendidas: **72%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~82%** — histórico E1 BTC (85% reglas OK)

## Categories

| Campo | Valor |
|-------|-------|
| Precio | **81094.0** |
| Entrada óptima | **81048.5** |
| Última señal | **btc-002** · 2026-09-03 18:34 NY · Entry **80861.5** |
| Calificación entrada | **REGULAR** — cerca suave de última Entry; precio cerca de Entry actual; sin 2M5 · (MÁS CERCA) · Δ Entry +187.0 pts (+0.231%) · precio→última 232.5 pts (0.287%) · precio→actual 45.5 pts (0.056%) |
| Bando usado | **BULLISH** |
| Bando mercado (H1) | **NEUTRAL** |
| Recomendación | **ESPERAR LONG** |
| Segunda indicación | **NEUTRAL** (H1 NEUTRAL — ver sección abajo) |
| Neural galería | **55% WIN** — grade **B** (baja similitud con galería WIN; conf. low) |
| **— Advanced —** | |
| R:R | 1:2 |
| Dist. a Entry | -45.5 pts (0.056%) |
| Dist. a SL | -250.0 pts (0.308%) |
| Dist. a TP | +363.6 pts (0.448%) |
| Riesgo (pts) | 204.5 |
| Winrate setup | ~82% — histórico E1 BTC (85% reglas OK) |
| Score Rules extendido | **72%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BULLISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. low · 55% WIN |
| Rules E1 detalle | **6/7** (85%) |
| Confluencia setup | **MEDIA** — 66% · Rules 85%; Neural 55%; 2M5 o zona parcial; Break operable |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **COMPLETED_BEAR** | Low H1 81288 alcanzado |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 77792 | Bull si cierre arriba |
| PDL | 76264 | Bear si cierre abajo |
| 0.5 midpoint | 77028 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Breakout alcista sostenido > 77792

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| Cerca de zona clave | ✅ | a 0.109% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 32 OK |
| Rango coherente | ✅ | Longs E1 pullback soporte debil (discoun |

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

- Fuera ventana NY (info — no bloquea checklist)
- Fuera de ventana NY (regla 2)
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **BULLISH** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **81094.0** | Retest **81006.0–81127.5** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.11%) | ✅ ≤0.15% de 81006.0 |
| Acción | **ESPERAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 81006.0–81127.5 (soporte_debil @ 81006.0) + 2 velas M5 verdes consecutivas en zona |
| Confirmación | 2 velas M5 verdes consecutivas con cierres en zona ≤0.15% |
| Entry | **81048.5** (limit retest o market al cierre 2ª vela) |
| SL | **80844.0** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **81457.6** |
| R:R | **1:2** · riesgo **204.5** pts |
| Invalidación | Cierre M5 < 80844.0 o breakdown < 81006.0 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 81006.0 | Referencia — requiere 2 verdes **nuevas** en retest | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Sesión: FUERA NY (FUERA_NY) — info_

- [✅] Cerca de zona (soporte_debil @ 81006)
- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **NEUTRAL**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (1280/612) | **SHORT** |
| CRT PD / Premium-Discount | BULLISH · PREMIUM | **LONG** |
| Estructura swings M5 | LL 81393->81288 · HH 81632->82300 | **NEUTRAL** |

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BEAR/BULLISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (1280/612) |
| Swings | LL 81393->81288 | HH 81632->82300 |

---

## M5 detalle

- RSI M5/H1: 32.3 / 77.0
- Zona: soporte_debil @ 81006
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `21:40 O=81669.9 H=81684.0 L=81522.5 C=81522.5 [R]`
- `21:45 O=81522.5 H=81673.2 L=81416.0 C=81673.2 [G]`
- `21:50 O=81673.2 H=81748.0 L=81624.0 C=81740.6 [G]`
- `21:55 O=81740.6 H=81740.6 L=81582.0 C=81590.0 [R]`
- `22:00 O=81590.0 H=81604.6 L=81381.5 C=81554.1 [R]`
- `22:05 O=81554.1 H=81589.3 L=81422.0 C=81441.7 [R]`
- `22:10 O=81441.7 H=81441.7 L=81261.0 C=81378.4 [R]`
- `22:15 O=81378.4 H=81399.4 L=81300.0 C=81300.0 [R]`
- `22:20 O=81300.0 H=81363.4 L=81256.0 C=81286.0 [R]`
- `22:25 O=81286.0 H=81286.0 L=81124.5 C=81131.8 [R]`
- `22:30 O=81131.8 H=81187.5 L=80905.1 C=81025.2 [R]`
- `22:35 O=81025.2 H=81094.0 L=81013.0 C=81094.0 [G]`

---

## Score reglas extendidas (72%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| Cerca de zona clave | SÍ | a 0.109% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 32 OK |
| Rango coherente | SÍ | Longs E1 pullback soporte debil (discoun |
| DMI alineado | NO | -DI domina (1280/612) |
| 0.5 midpoint E1 | NO | premium — no long E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 81094 · FUERA NY (FUERA_NY) · CRT PD=BULLISH · H1 bias **NEUTRAL**
- **Setup:** ESPERAR LONG · dirección **LONG** · modo **BREAK** · reglas E1 6/7 (85%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score 75% requiere confirmación TV

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 6/7 | 30% | 85% OK |
| Rules extendidas (10) | 72% | 15% | meta >70% |
| Neural galería | 55.3% | 30% | no alineado |
| CRT coherence | pass | 10% | Longs E1 pullback soporte debil (discoun |
| **Score combinado** | **75%** | 100% |  |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 77792: +3302.0 pts (+4.245%)
- **PDL** 76264: +4830.0 pts (+6.333%)

### Premium / Discount 0.5

- Midpoint 0.5: **77028**
- Posición precio: **PREMIUM** (precio 81094)
- Lectura PD: **BULLISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-03 20:00 O=81755 H=81780 L=81393 C=81473 [R]`
- `09-03 21:00 O=81473 H=82300 L=81288 C=81590 [G]`
- `09-03 22:00 O=81590 H=81605 L=80905 C=81096 [R]`

- Estado CRT H1: **COMPLETED_BEAR** — Low H1 81288 alcanzado

### Matriz acción E1 (TRADING_INDICATORS_RULES §3.2)

| Lectura CRT | Acción E1 | Estado actual |
|-------------|-----------|---------------|
| Dentro PDH/PDL | NEUTRAL — no forzar |  |
| Cierre > PDH | Sesgo alcista — long pullback | **→** |
| Cierre < PDL | Sesgo bajista — short rechazo |  |
| Fakeout PDH | NO long E1 |  |
| Fakeout PDL | Contexto E2 turtle soup |  |

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 55.3% WIN (grade B)

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | Esperar setup A+ galeria WIN | — | 55% | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** LONG @ zona soporte_debil 81006 (precio actual 81094)
- **SL estructural:** 80844 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 81594 | **BE:** mover a BE en 1:1
- **Invalidación:** cierre M5 fuera zona / CRT invalid / fakeout contra dirección
- **Confluencias Notion sugeridas:** Continuación/Breakout E1, Zona débil morada, CRT alineado

### Pre-trade checklist (8 ítems)

| # | Ítem | OK |
|---|------|----|
| 1 | Bias H1 alineado | ❌ |
| 2 | Zona ≤0.15% | ✅ |
| 3 | 2 velas M5 confirmación | ❌ |
| 4 | Rules E1 ≥63% | ✅ |
| 5 | Extendidas ≥70% | ✅ |
| 6 | Sin fakeout contra | ✅ |
| 7 | SL ~$9 definido | ✅ |
| 8 | R:R 1:2 | ✅ |

---

## H) Psicología y guardas de sesión

- ℹ️ Fuera ventana NY — informativo (no fuerza NO_OPERAR en checklist)
- ❓ ¿2 SL hoy? — confirmar trader (2 SL = fin sesión)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---

## I) Cursor — prompt ADVANCED

Usar con `@docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` sección **Modo Advanced**.

```
Análisis E1 CRT ADVANCED — BTC M5 HIGH mode.
Lee TODAS las secciones A–H de live/btc_m5_high_signal.md.
NO acortar. Responde estructurado en español con síntesis ejecutiva,
scorecard, CRT deep dive, E2 (si aplica), cruce ML×Neural, galería,
plan (si ENTRAR), red flags y guardas psicológicas.
Confirmar TradingView antes de ejecutar. 2 SL = fin sesión.
```


---

## Cursor HIGH response
Modo **ADVANCED** — usar prompt completo en `docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` §Modo Advanced.
Leer Categories (incl. Entrada óptima + Confluencia + Advanced) y secciones A–I. **NO acortar** vs light mode.

![Chart](btc_m5_chart.png)
## Salidas

- **Reporte:** `live/btc_m5_high_signal.md`
- **Reporte (abs):** `D:\Danilo\Trading\Cursor Trading\live\btc_m5_high_signal.md`


---
*high signal | 2026-09-03 22:36 UTC*
