# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-03 22:37 UTC | NY 2026-09-03 18:37 | FUERA_NY
> Precio **53737.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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
**Tendencia:** Sin dirección
**Reglas:** **5 de 7** (71%) | Extendidas: **72%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~69%** — histórico E1 BTC (71% reglas OK)

## Categories

| Campo | Valor |
|-------|-------|
| Precio | **53737.0** |
| Entrada óptima | **53708.8** |
| Última señal | **us30-003** · 2026-09-03 18:23 NY · Entry **53706.8** |
| Calificación entrada | **BUENA** — precio cerca de última Entry + zona OK · (MISMA ZONA) · Δ Entry +2.0 pts (+0.004%) · precio→última 30.2 pts (0.056%) · precio→actual 28.2 pts (0.053%) |
| Bando usado | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| Recomendación | **NO_OPERAR SHORT** |
| Segunda indicación | **LONG** (H1 NEUTRAL — ver sección abajo) |
| Neural galería | **51% WIN** — grade **B** (baja similitud con galería WIN; conf. low) |
| **— Advanced —** | |
| R:R | 1:2 |
| Dist. a Entry | -28.2 pts (0.052%) |
| Dist. a SL | +161.2 pts (0.300%) |
| Dist. a TP | -407.1 pts (0.757%) |
| Riesgo (pts) | 189.4 |
| Winrate setup | ~69% — histórico E1 BTC (71% reglas OK) |
| Score Rules extendido | **72%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **NEUTRAL** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. low · 51% WIN |
| Rules E1 detalle | **5/7** (71%) |
| Confluencia setup | **MEDIA** — 50% · Rules 71%; Neural 51%; 2M5 o zona parcial; Break con fricción CRT |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 53703-53743; 0.5=53723 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 53283 | Bull si cierre arriba |
| PDL | 52720 | Bear si cierre abajo |
| 0.5 midpoint | 53002 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.000% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 54 OK |
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
| Precio | **53737.0** | Retest **53656.4–53737.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.00%) | ✅ ≤0.15% de 53737.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 53656.4–53737.0 (soporte_debil @ 53737.0) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas con cierres en zona ≤0.15% |
| Entry | **53708.8** (limit retest o market al cierre 2ª vela) |
| SL | **53898.2** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **53329.9** |
| R:R | **1:2** · riesgo **189.4** pts |
| Invalidación | Cierre M5 > 53898.2 o breakout > 53737.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 53737.0 | Referencia — requiere 2 rojas **nuevas** en retest | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Sesión: FUERA NY (FUERA_NY) — info_

- [✅] Cerca de zona (soporte_debil @ 53737)
- [❌] 2 velas M5 confirman SHORT
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
| DMI (momentum M5) | +DI domina (37/31) | **LONG** |
| CRT PD / Premium-Discount | BULLISH · PREMIUM | **LONG** |
| Estructura swings M5 | LL 53727->53703 · LH 53778->53743 | **SHORT** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BULLISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (37/31) |
| Swings | LL 53727->53703 | LH 53778->53743 |

---

## M5 detalle

- RSI M5/H1: 54.4 / 80.7
- Zona: soporte_debil @ 53737
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `20:35 O=53731.0 H=53737.0 L=53729.0 C=53731.0 [G]`
- `20:40 O=53732.0 H=53735.0 L=53728.0 C=53728.0 [R]`
- `20:45 O=53727.0 H=53730.0 L=53718.0 C=53722.0 [R]`
- `20:50 O=53720.0 H=53720.0 L=53714.0 C=53719.0 [R]`
- `20:55 O=53722.0 H=53723.0 L=53715.0 C=53720.0 [R]`
- `22:00 O=53707.0 H=53735.0 L=53703.0 C=53730.0 [G]`
- `22:05 O=53729.0 H=53729.0 L=53714.0 C=53714.0 [R]`
- `22:10 O=53717.0 H=53733.0 L=53717.0 C=53728.0 [G]`
- `22:15 O=53731.0 H=53743.0 L=53731.0 C=53736.0 [G]`
- `22:20 O=53737.0 H=53737.0 L=53732.0 C=53735.0 [R]`
- `22:25 O=53733.0 H=53737.0 L=53732.0 C=53737.0 [G]`
- `22:26 O=53737.0 H=53737.0 L=53737.0 C=53737.0 [G]`

---

## Score reglas extendidas (72%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.000% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 54 OK |
| Rango coherente | NO | rango alcista |
| DMI alineado | NO | +DI domina (37/31) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 53737 · FUERA NY (FUERA_NY) · CRT PD=BULLISH · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/7 (71%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 53%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 5/7 | 30% | 71% OK |
| Rules extendidas (10) | 72% | 15% | meta >70% |
| Neural galería | 50.9% | 30% | no alineado |
| CRT coherence | fail | 10% | rango alcista |
| **Score combinado** | **53%** | 100% |  |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 53283: +454.0 pts (+0.852%)
- **PDL** 52720: +1017.0 pts (+1.929%)

### Premium / Discount 0.5

- Midpoint 0.5: **53002**
- Posición precio: **PREMIUM** (precio 53737)
- Lectura PD: **BULLISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-03 20:00 O=53756 H=53762 L=53714 C=53720 [R]`
- `09-03 22:00 O=53707 H=53743 L=53703 C=53737 [G]`
- `09-03 22:26 O=53737 H=53737 L=53737 C=53737 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 53703-53743; 0.5=53723

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


---
*high signal | 2026-09-03 22:37 UTC*
