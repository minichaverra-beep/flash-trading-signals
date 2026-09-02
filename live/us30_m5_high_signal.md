# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-02 16:54 UTC | NY 2026-09-02 12:54 | FUERA_NY
> Precio **53043.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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
- Breakout bajista sostenido < 53049

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **6 de 7** (85%) | Extendidas: **81%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~82%** — histórico E1 BTC (85% reglas OK)

## Categories

| Campo | Valor |
|-------|-------|
| Precio | **53043.0** |
| Entrada óptima | **53021.1** |
| Bando usado | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| Recomendación | **ESPERAR SHORT** |
| Segunda indicación | **SHORT** (H1 NEUTRAL — ver sección abajo) |
| **— Advanced —** | |
| R:R | 1:2 |
| Dist. a Entry | -21.9 pts (0.041%) |
| Dist. a SL | +165.1 pts (0.311%) |
| Dist. a TP | -395.8 pts (0.746%) |
| Riesgo (pts) | 187.0 |
| Winrate setup | ~82% — histórico E1 BTC (85% reglas OK) |
| Score Rules extendido | **81%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Rules E1 detalle | **6/7** (85%) |
| Confluencia setup | **ALTA** — 77% · Rules 85%; 2M5 o zona parcial; Break operable; CLI alineado / H1 no |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 53015-53119; 0.5=53067 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 53343 | Bull si cierre arriba |
| PDL | 52747 | Bear si cierre abajo |
| 0.5 midpoint | 53045 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Breakout bajista sostenido < 53049

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.011% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 40 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

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
- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- Fuera de ventana NY (regla 2)
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **53043.0** | Retest **52969.4–53049.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.01%) | ✅ ≤0.15% de 53049.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 52969.4–53049.0 (soporte_debil @ 53049.0) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas con cierres en zona ≤0.15% |
| Entry | **53021.1** (limit retest o market al cierre 2ª vela) |
| SL | **53208.1** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **52647.2** |
| R:R | **1:2** · riesgo **187.0** pts |
| Invalidación | Cierre M5 > 53208.1 o breakout > 53049.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 53049.0 | Referencia — requiere 2 rojas **nuevas** en retest | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Sesión: FUERA NY (FUERA_NY) — info_

- [✅] Cerca de zona (soporte_debil @ 53049)
- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **SHORT**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (186/122) | **SHORT** |
| CRT PD / Premium-Discount | NEUTRAL · DISCOUNT | **LONG** |
| Estructura swings M5 | LL 53049->53015 · LH 53283->53122 | **SHORT** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (186/122) |
| Swings | LL 53049->53015 | LH 53283->53122 |

---

## M5 detalle

- RSI M5/H1: 39.6 / 61.6
- Zona: soporte_debil @ 53049
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `15:50 O=53058.0 H=53098.0 L=53057.0 C=53084.0 [G]`
- `15:55 O=53083.0 H=53122.0 L=53075.0 C=53119.0 [G]`
- `16:00 O=53119.0 H=53119.0 L=53083.0 C=53093.0 [R]`
- `16:05 O=53094.0 H=53103.0 L=53081.0 C=53093.0 [R]`
- `16:10 O=53093.0 H=53112.0 L=53079.0 C=53107.0 [G]`
- `16:15 O=53107.0 H=53108.0 L=53072.0 C=53081.0 [R]`
- `16:20 O=53085.0 H=53085.0 L=53039.0 C=53039.0 [R]`
- `16:25 O=53039.0 H=53051.0 L=53015.0 C=53022.0 [R]`
- `16:30 O=53021.0 H=53058.0 L=53018.0 C=53051.0 [G]`
- `16:35 O=53052.0 H=53068.0 L=53045.0 C=53062.0 [G]`
- `16:40 O=53063.0 H=53063.0 L=53036.0 C=53036.0 [R]`
- `16:44 O=53043.0 H=53043.0 L=53043.0 C=53043.0 [G]`

---

## Score reglas extendidas (81%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.011% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 40 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | -DI domina (186/122) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 53043 · FUERA NY (FUERA_NY) · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** ESPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 6/7 (85%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score 75% requiere confirmación TV

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 6/7 | 30% | 85% OK |
| Rules extendidas (10) | 81% | 15% | meta >70% |
| Neural galería | n/d | 30% | sin modelo — neutral 50% |
| CRT coherence | pass | 10% | No forzar; esperar pending CRT HTF | Mod |
| **Score combinado** | **75%** | 100% |  |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 53343: -300.0 pts (-0.562%)
- **PDL** 52747: +296.0 pts (+0.561%)

### Premium / Discount 0.5

- Midpoint 0.5: **53045**
- Posición precio: **DISCOUNT** (precio 53043)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-02 15:00 O=53237 H=53249 L=53049 C=53119 [R]`
- `09-02 16:00 O=53119 H=53119 L=53015 C=53036 [R]`
- `09-02 16:44 O=53043 H=53043 L=53043 C=53043 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 53015-53119; 0.5=53067

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

- Sin datos ML/Neural


---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | Esperar setup A+ galeria WIN | — | heurística | general |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** SHORT @ zona soporte_debil 53049 (precio actual 53043)
- **SL estructural:** 53202 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 52725 | **BE:** mover a BE en 1:1
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


---
*high signal | 2026-09-02 16:54 UTC*
