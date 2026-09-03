# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-03 23:30 UTC | NY 2026-09-03 19:30 | FUERA_NY
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
- ⚠ H1 alcista vs bias forzado — confirmar en TV antes de entrar
- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Sin breakout de nivel detectado

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 7** (71%) | Extendidas: **81%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~82%** — patrón ganador similar · histórico E1 BTC

## Categories

| Campo | Valor |
|-------|-------|
| Precio | **53737.0** |
| Entrada óptima | **53715.8** |
| Última señal | **us30-004** · 2026-09-03 18:37 NY · Entry **53708.8** |
| Calificación entrada | **BUENA** — precio cerca de última Entry + zona OK · (MISMA ZONA) · Δ Entry +7.0 pts (+0.013%) · precio→última 28.2 pts (0.053%) · precio→actual 21.2 pts (0.039%) |
| Bando usado | **BEARISH** |
| Bando mercado (H1) | **BULLISH** |
| Recomendación | **NO_OPERAR SHORT** |
| Neural galería | **81% WIN** — grade **B** (alineado con patrones WIN desktop; conf. high) |
| **— Advanced —** | |
| R:R | 1:2 |
| Dist. a Entry | -21.2 pts (0.039%) |
| Dist. a SL | +114.5 pts (0.213%) |
| Dist. a TP | -292.6 pts (0.545%) |
| Riesgo (pts) | 135.7 |
| Winrate setup | ~82% — patrón ganador similar · histórico E1 BTC |
| Score Rules extendido | **81%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **BULLISH** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. high · 81% WIN |
| Rules E1 detalle | **5/7** (71%) |
| Confluencia setup | **MEDIA** — 66% · Rules 71%; Neural 81% alineado; 2M5 o zona parcial; Break con fricción CRT |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 53733-53746; 0.5=53740 |
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
| Cerca de zona clave | ✅ | a 0.013% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 51 OK |
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

- Precio > PDH — no short contra rango alcista CRT
- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BULLISH** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **53737.0** | Retest **53663.4–53744.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.01%) | ✅ ≤0.15% de 53744.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 53663.4–53744.0 (resistencia_debil @ 53744.0) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas con cierres en zona ≤0.15% |
| Entry | **53715.8** (limit retest o market al cierre 2ª vela) |
| SL | **53851.5** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **53444.4** |
| R:R | **1:2** · riesgo **135.7** pts |
| Invalidación | Cierre M5 > 53851.5 o breakout > 53744.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 53744.0 | Referencia — requiere 2 rojas **nuevas** en retest | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY_

- [✅] Cerca de zona (resistencia_debil @ 53744)
- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BULLISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | NEUTRAL | Momentum mixto |
| Swings | HL 53703->53730 | LH 53746->53746 |

---

## M5 detalle

- RSI M5/H1: 51.4 / 85.7
- Zona: resistencia_debil @ 53744
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `22:30 O=53738.0 H=53744.0 L=53736.0 C=53743.0 [G]`
- `22:35 O=53744.0 H=53744.0 L=53740.0 C=53740.0 [R]`
- `22:40 O=53739.0 H=53739.0 L=53730.0 C=53737.0 [R]`
- `22:45 O=53739.0 H=53740.0 L=53734.0 C=53740.0 [G]`
- `22:50 O=53740.0 H=53744.0 L=53739.0 C=53744.0 [G]`
- `22:55 O=53744.0 H=53744.0 L=53739.0 C=53741.0 [R]`
- `23:00 O=53743.0 H=53746.0 L=53739.0 C=53744.0 [G]`
- `23:05 O=53743.0 H=53744.0 L=53741.0 C=53743.0 [G]`
- `23:10 O=53746.0 H=53746.0 L=53738.0 C=53739.0 [R]`
- `23:15 O=53737.0 H=53739.0 L=53733.0 C=53739.0 [G]`
- `23:20 O=53737.0 H=53737.0 L=53737.0 C=53737.0 [G]`
- `23:20 O=53737.0 H=53737.0 L=53737.0 C=53737.0 [G]`

---

## Score reglas extendidas (81%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.013% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 51 OK |
| Rango coherente | NO | rango alcista |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 53737 · reloj FUERA_NY · CRT PD=BULLISH · H1 bias **BULLISH**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/7 (71%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **BULLISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score 64% requiere confirmación TV

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 5/7 | 30% | 71% OK |
| Rules extendidas (10) | 81% | 15% | meta >70% |
| Neural galería | 80.8% | 30% | alineado WIN |
| CRT coherence | fail | 10% | rango alcista |
| **Score combinado** | **64%** | 100% |  |

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

- `09-03 22:00 O=53707 H=53744 L=53703 C=53741 [G]`
- `09-03 23:00 O=53743 H=53746 L=53733 C=53737 [R]`
- `09-03 23:20 O=53737 H=53737 L=53737 C=53737 [G]`

- Estado CRT H1: **INSIDE_RANGE** — Rango H1 53733-53746; 0.5=53740

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

**Acuerdo Rules/Neural:** CONFLICT

- Tensión: ML bajo veto vs Neural alto — típico en sesiones con setup visual fuerte pero features ML desfavorables; priorizar Rules % + CRT

- **Neural galería:** 80.8% WIN (grade B)

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 81% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)
- ⚠ Tensión ML/Neural — no entrar por galería sola

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
Confirmar TradingView antes de ejecutar. 2 SL = límite de riesgo diario.
```


---

## Cursor HIGH response
Modo **ADVANCED** — usar prompt completo en `docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md` §Modo Advanced.
Leer Categories (incl. Entrada óptima + Confluencia + Advanced) y secciones A–I. **NO acortar** vs light mode.

![Chart](us30_m5_chart.png)
## Salidas

- **Reporte:** `live/us30_m5_high_signal.md`
- **Reporte (abs):** `D:\Danilo\Trading\Cursor Trading\live\us30_m5_high_signal.md`


---
*high signal | 2026-09-03 23:30 UTC*
