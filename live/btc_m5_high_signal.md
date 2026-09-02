# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-02 16:56 UTC | NY 2026-09-02 12:56 | FUERA_NY
> Precio **77232.0** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> **Modo:** BULLISH + REVERSE — Bias CLI **BULLISH** — setup re-puntuado como LONG
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **BULLISH** |
| Modo setup | **REVERSE (E2)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BULLISH** — setup re-puntuado como LONG
- Setup **REVERSE** — turtle soup / PDH-PDL fakeout / sweep+reclaim
- E2: E2_NO (1/6) · operable=NO · WR ~61%

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Alcista
**Reglas:** **5 de 7** (71%) | Extendidas: **81%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~61%** — histórico E2 BTC reversión (~63% E2 global)

## Categories

| Campo | Valor |
|-------|-------|
| Precio | **77232.0** |
| Entrada óptima | **77150.5** |
| Bando usado | **BULLISH** |
| Bando mercado (H1) | **NEUTRAL** |
| Recomendación | **NO_OPERAR LONG** |
| Segunda indicación | **LONG** (H1 NEUTRAL — ver sección abajo) |
| Neural galería | **53% WIN** — grade **B** (baja similitud con galería WIN; conf. low) |
| **— Advanced —** | |
| R:R | 1:2 |
| Dist. a Entry | -81.5 pts (0.106%) |
| Dist. a SL | -276.2 pts (0.358%) |
| Dist. a TP | +307.9 pts (0.399%) |
| Riesgo (pts) | 194.7 |
| Winrate setup | ~61% — histórico E2 BTC reversión (~63% E2 global) |
| Score Rules extendido | **81%** |
| Estado 2M5 | Inválido / esperar |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BULLISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Neural grade/conf | **B** · conf. low · 53% WIN |
| Rules E1 detalle | **5/7** (71%) |
| Confluencia setup | **BAJA** — 33% · Rules 71%; Neural 53%; 2M5/zona no listos; E2 no operable |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BEAR** | Sweep high H1 sin hold |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 79221 | Bull si cierre arriba |
| PDL | 76420 | Bear si cierre abajo |
| 0.5 midpoint | 77820 | Filtro 50% |

**Nota CRT:** REVERSE: H1 PENDING_BEAR — sweep+reclaim E2 ctx

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Alcista |
| Cerca de zona clave | ❌ | Lejos de la zona |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 53 OK |
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

### Red flags

- Fuera ventana NY (info — no bloquea checklist)
- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- CRT H1 pending bear — no entrar long contra invalid reciente
- Fuera de ventana NY (regla 2)
- Lejos de swing S/R débil (>0.15%) — esperar zona
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: REVERSE 2 velas alineadas al bando
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **REVERSE (E2)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **77232.0** | Retest **77110.0–77225.7** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Cerca zona | ❌ (0.16%) | ✅ ≤0.15% de 77110.0 |
| Acción | **ESPERAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 77110.0–77225.7 (soporte_debil @ 77110.0) + 2 velas M5 verdes consecutivas en zona |
| Confirmación | 2 velas M5 verdes consecutivas con cierres en zona ≤0.15% |
| Entry | **77150.5** (limit retest o market al cierre 2ª vela) |
| SL | **76955.8** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **77539.9** |
| R:R | **1:2** · riesgo **194.7** pts |
| Invalidación | Cierre M5 < 76955.8 o breakdown < 77110.0 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |

---

## Ilustración entrada (2M5 + óptima)

![chart](btc_m5_chart_annotated.png)

### Salidas (chart)

- **Abrir (relativo):** `live/btc_m5_chart_annotated.png`
- **Markdown:** `![chart](btc_m5_chart_annotated.png)` (desde `live/`)
- **Ruta absoluta:** `D:\Danilo\Trading\Cursor Trading\live\btc_m5_chart_annotated.png`

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 77110.0 | Referencia — requiere 2 verdes **nuevas** en retest | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [R][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Sesión: FUERA NY (FUERA_NY) — info_

- [❌] Cerca de zona (soporte_debil @ 77110)
- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | Momentum mixto | **NEUTRAL** |
| CRT PD / Premium-Discount | NEUTRAL · DISCOUNT | **LONG** |
| Estructura swings M5 | LL 77110->76748 · HH 77386->77582 | **NEUTRAL** |

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BEAR/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 77110->76748 | HH 77386->77582 |

---

## M5 detalle

- RSI M5/H1: 52.7 / 48.1
- Zona: soporte_debil @ 77110
- 2M5 LONG: NO | SHORT: SÍ

### 12 velas M5

- `16:00 O=77289.0 H=77296.0 L=77210.0 C=77296.0 [G]`
- `16:05 O=77296.0 H=77329.2 L=77244.0 C=77303.4 [G]`
- `16:10 O=77303.4 H=77396.0 L=77264.4 C=77356.0 [G]`
- `16:15 O=77356.0 H=77500.0 L=77332.7 C=77482.8 [G]`
- `16:20 O=77482.8 H=77579.8 L=77438.0 C=77549.8 [G]`
- `16:25 O=77549.8 H=77582.0 L=77443.1 C=77464.0 [R]`
- `16:30 O=77464.0 H=77567.4 L=77464.0 C=77530.7 [G]`
- `16:35 O=77530.7 H=77530.7 L=77392.0 C=77409.6 [R]`
- `16:40 O=77409.6 H=77409.6 L=77264.3 C=77264.3 [R]`
- `16:45 O=77264.3 H=77330.0 L=77232.0 C=77292.4 [G]`
- `16:50 O=77292.4 H=77303.1 L=77254.8 C=77265.2 [R]`
- `16:55 O=77265.3 H=77286.3 L=77232.0 C=77232.0 [R]`

---

## Score reglas extendidas (81%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Alcista |
| Cerca de zona clave | NO | lejos |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 53 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 77232 · FUERA NY (FUERA_NY) · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **REVERSE** · reglas E1 5/7 (71%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score 69% requiere confirmación TV
- **E2 contexto:** E2_NO (1/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 5/7 | 30% | 71% OK |
| Rules extendidas (10) | 81% | 15% | meta >70% |
| Neural galería | 53.0% | 30% | no alineado |
| CRT coherence | pass | 10% | No forzar; esperar pending CRT HTF | Mod |
| E2 turtle | 1/6 | 5% | E2_NO |
| **Score combinado** | **69%** | 100% |  |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 79221: -1988.6 pts (-2.510%)
- **PDL** 76420: +812.0 pts (+1.063%)

### Premium / Discount 0.5

- Midpoint 0.5: **77820**
- Posición precio: **DISCOUNT** (precio 77232)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-02 14:00 O=77146 H=77490 L=77010 C=77066 [R]`
- `09-02 15:00 O=77066 H=77386 L=76748 C=77289 [G]`
- `09-02 16:00 O=77289 H=77582 L=77210 C=77232 [R]`

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

- **Neural galería:** 53.0% WIN (grade B)

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: REVERSE 2 velas alineadas al bando | — | 53% | WIN |
| 2 | WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26) | BTC-11-05-26.png | 48% | sweep+reclaim, WIN |
| 3 | Esperar setup A+ galeria WIN | — | 43% | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

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

## Salidas

- **Reporte:** `live/btc_m5_high_signal.md`
- **Reporte (abs):** `D:\Danilo\Trading\Cursor Trading\live\btc_m5_high_signal.md`
- **Chart anotado:** `live/btc_m5_chart_annotated.png`
- **Preview:** `![chart](btc_m5_chart_annotated.png)`
- **Chart (abs):** `D:\Danilo\Trading\Cursor Trading\live\btc_m5_chart_annotated.png`


---
*high signal | 2026-09-02 16:56 UTC*
