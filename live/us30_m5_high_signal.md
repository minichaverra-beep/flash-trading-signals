# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-03 22:01 UTC | NY 2026-09-03 18:01 | FUERA_NY
> Precio **53720.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- Breakout bajista sostenido < 53725

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **4 de 7** (57%) | Extendidas: **72%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~67%** — probabilidad histórica (~67%)

## Categories

| Campo | Valor |
|-------|-------|
| **— Revisión última Entry —** | *(no es señal nueva)* |
| Revisión última Entry | **us30-002** · 2026-09-03 17:16 NY · Entry **53696.8** · SHORT (lado CLI -Bearish) |
| P&L vs precio actual | **-23.2 pts (-0.043%)** · **NEUTRO** · SHORT |
| Calificación Entry | **CERCA_BE** — Entry SHORT neutro; aún cerca de zona; precio cerca de Entry previa |
| Precio actual | **53720.0** |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| Neural galería | **51% WIN** — grade **B** (baja similitud con galería WIN; conf. low) |
| **— Advanced —** | |
| R:R | 1:2 |
| Dist. a Entry | -23.2 pts (0.043%) |
| Dist. a SL | +166.2 pts (0.309%) |
| Dist. a TP | -402.0 pts (0.748%) |
| Riesgo (pts) | 189.4 |
| Winrate setup | ~67% — probabilidad histórica (~67%) |
| Score Rules extendido | **72%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. low · 51% WIN |
| Rules E1 detalle | **4/7** (57%) |
| Confluencia setup | **BAJA** — 41% · Rules 57%; Neural 51%; 2M5 o zona parcial; Break con fricción CRT |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 53714-53762; 0.5=53738 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 53283 | Bull si cierre arriba |
| PDL | 52720 | Bear si cierre abajo |
| 0.5 midpoint | 53002 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Breakout bajista sostenido < 53725

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.009% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | RSI 17 sobrevendido |
| Rango coherente | ❌ | rango alcista |

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
- Precio > PDH — no short contra rango alcista CRT
- Fuera de ventana NY (regla 2)
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BULLISH** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **53720.0** | Retest **53644.4–53725.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.01%) | ✅ ≤0.15% de 53725.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 53644.4–53725.0 (soporte_debil @ 53725.0) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas con cierres en zona ≤0.15% |
| Entry | **53696.8** (limit retest o market al cierre 2ª vela) |
| SL | **53886.2** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **53318.0** |
| R:R | **1:2** · riesgo **189.4** pts |
| Invalidación | Cierre M5 > 53886.2 o breakout > 53725.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |

---

## Ilustración entrada (2M5 + óptima)

![chart](us30_m5_chart_annotated.png)

### Salidas (chart)

- **Abrir (relativo):** `live/us30_m5_chart_annotated.png`
- **Markdown:** `![chart](us30_m5_chart_annotated.png)` (desde `live/`)
- **Ruta absoluta:** `D:\Danilo\Trading\Cursor Trading\live\us30_m5_chart_annotated.png`

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 53725.0 | Referencia — requiere 2 rojas **nuevas** en retest | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Sesión: FUERA NY (FUERA_NY) — info_

- [✅] Cerca de zona (soporte_debil @ 53725)
- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (39/8) | **SHORT** |
| CRT PD / Premium-Discount | BULLISH · PREMIUM | **LONG** |
| Estructura swings M5 | HL 53725->53727 · HH 53763->53778 | **LONG** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BULLISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (39/8) |
| Swings | HL 53725->53727 | HH 53763->53778 |

---

## M5 detalle

- RSI M5/H1: 17.0 / 80.9
- Zona: soporte_debil @ 53725
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `20:05 O=53751.0 H=53757.0 L=53746.0 C=53749.0 [R]`
- `20:10 O=53750.0 H=53753.0 L=53745.0 C=53750.0 [G]`
- `20:15 O=53751.0 H=53753.0 L=53731.0 C=53731.0 [R]`
- `20:20 O=53732.0 H=53739.0 L=53728.0 C=53731.0 [R]`
- `20:25 O=53733.0 H=53734.0 L=53728.0 C=53729.0 [R]`
- `20:30 O=53730.0 H=53731.0 L=53725.0 C=53730.0 [G]`
- `20:35 O=53731.0 H=53737.0 L=53729.0 C=53731.0 [G]`
- `20:40 O=53732.0 H=53735.0 L=53728.0 C=53728.0 [R]`
- `20:45 O=53727.0 H=53730.0 L=53718.0 C=53722.0 [R]`
- `20:50 O=53720.0 H=53720.0 L=53714.0 C=53719.0 [R]`
- `20:55 O=53722.0 H=53723.0 L=53715.0 C=53720.0 [R]`
- `20:59 O=53720.0 H=53720.0 L=53720.0 C=53720.0 [G]`

---

## Score reglas extendidas (72%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.009% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | RSI 17 sobrevendido |
| Rango coherente | NO | rango alcista |
| DMI alineado | SÍ | -DI domina (39/8) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 53720 · FUERA NY (FUERA_NY) · CRT PD=BULLISH · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 4/7 (57%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 48%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 4/7 | 30% | 57% OK |
| Rules extendidas (10) | 72% | 15% | meta >70% |
| Neural galería | 50.9% | 30% | no alineado |
| CRT coherence | fail | 10% | rango alcista |
| **Score combinado** | **48%** | 100% |  |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 53283: +437.0 pts (+0.820%)
- **PDL** 52720: +1000.0 pts (+1.897%)

### Premium / Discount 0.5

- Midpoint 0.5: **53002**
- Posición precio: **PREMIUM** (precio 53720)
- Lectura PD: **BULLISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-03 19:00 O=53753 H=53778 L=53725 C=53755 [G]`
- `09-03 20:00 O=53756 H=53762 L=53714 C=53720 [R]`
- `09-03 20:59 O=53720 H=53720 L=53720 C=53720 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 53714-53762; 0.5=53738

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

- **Neural galería:** 50.9% WIN (grade B)

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | Esperar setup A+ galeria WIN | — | 51% | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas de sesión

- ℹ️ Fuera ventana NY — informativo (no fuerza NO_OPERAR en checklist)
- ❓ ¿2 SL hoy? — confirmar trader (2 SL = fin sesión)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---

## I) Cursor — prompt ADVANCED

Usar con `@docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md` sección **Modo Advanced**.

```
Análisis E1 CRT ADVANCED — US30 M5 HIGH mode.
Lee TODAS las secciones A–H de live/us30_m5_high_signal.md.
NO acortar. Responde estructurado en español con síntesis ejecutiva,
scorecard, CRT deep dive, E2 (si aplica), cruce ML×Neural, galería,
plan (si ENTRAR), red flags y guardas psicológicas.
Confirmar TradingView antes de ejecutar. 2 SL = fin sesión.
```


---

## Cursor HIGH response
Modo **ADVANCED** — usar prompt completo en `docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md` §Modo Advanced.
Leer Categories (incl. Entrada óptima + Confluencia + Advanced) y secciones A–I. **NO acortar** vs light mode.

## Salidas

- **Reporte:** `live/us30_m5_high_signal.md`
- **Reporte (abs):** `D:\Danilo\Trading\Cursor Trading\live\us30_m5_high_signal.md`
- **Chart anotado:** `live/us30_m5_chart_annotated.png`
- **Preview:** `![chart](us30_m5_chart_annotated.png)`
- **Chart (abs):** `D:\Danilo\Trading\Cursor Trading\live\us30_m5_chart_annotated.png`


---
*high signal | 2026-09-03 22:01 UTC*
