# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-03 21:57 UTC | NY 2026-09-03 17:57 | FUERA_NY
> Precio **81610.0** | HIGH mode | PF E1=4.77 | E2 max 10%
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
| **— Revisión última Entry —** | *(no es señal nueva)* |
| Revisión última Entry | **btc-001** · 2026-09-03 17:20 NY · Entry **81589.1** · SHORT (lado CLI -Bearish) |
| P&L vs precio actual | **-20.9 pts (-0.026%)** · **NEUTRO** · SHORT |
| Calificación Entry | **CERCA_BE** — Entry SHORT neutro; aún cerca de zona; precio cerca de Entry previa |
| Precio actual | **81610.0** |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BULLISH** |
| Neural galería | **53% WIN** — grade **B** (baja similitud con galería WIN; conf. low) |
| **— Advanced —** | |
| R:R | 1:2 |
| Dist. a Entry | -20.9 pts (0.026%) |
| Dist. a SL | +185.3 pts (0.227%) |
| Dist. a TP | -433.1 pts (0.531%) |
| Riesgo (pts) | 206.1 |
| Winrate setup | ~82% — patrón ganador similar · histórico E1 BTC |
| Score Rules extendido | **81%** |
| Estado 2M5 | En zona · falta 2M5 |
| Bias H1 vs bando | H1 **BULLISH** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. low · 53% WIN |
| Rules E1 detalle | **5/7** (71%) |
| Confluencia setup | **MEDIA** — 50% · Rules 71%; Neural 53%; 2M5 o zona parcial; Break con fricción CRT |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **PENDING_BEAR** | Sweep high H1 sin hold |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 77792 | Bull si cierre arriba |
| PDL | 76264 | Bear si cierre abajo |
| 0.5 midpoint | 77028 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.027% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | Fondo rojo TORYS-proxy - filtro short |
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
| Precio | **81610.0** | Retest **81509.6–81632.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.03%) | ✅ ≤0.15% de 81632.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 81509.6–81632.0 (resistencia_debil @ 81632.0) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas con cierres en zona ≤0.15% |
| Entry | **81589.1** (limit retest o market al cierre 2ª vela) |
| SL | **81795.3** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **81176.9** |
| R:R | **1:2** · riesgo **206.1** pts |
| Invalidación | Cierre M5 > 81795.3 o breakout > 81632.0 sin rechazo |
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
| ✅ SHORT OK: [R][R] en resistencia_debil @ 81632.0 | Referencia — requiere 2 rojas **nuevas** en retest | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Sesión: FUERA NY (FUERA_NY) — info_

- [✅] Cerca de zona (resistencia_debil @ 81632)
- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BEAR/BULLISH | Núcleo |
| RSI TORYS | BEARISH | Fondo rojo TORYS-proxy - filtro short |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 81393->81288 | HH 81632->82300 |

---

## M5 detalle

- RSI M5/H1: 52.2 / 84.5
- Zona: resistencia_debil @ 81632
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `21:00 O=81473.0 H=81487.1 L=81351.2 C=81377.4 [R]`
- `21:05 O=81377.4 H=81399.4 L=81288.0 C=81384.6 [G]`
- `21:10 O=81384.6 H=81620.7 L=81384.6 C=81598.0 [G]`
- `21:15 O=81598.0 H=81668.0 L=81506.6 C=81565.5 [R]`
- `21:20 O=81565.5 H=81636.3 L=81510.5 C=81536.1 [R]`
- `21:25 O=81536.1 H=81777.8 L=81516.9 C=81762.0 [G]`
- `21:30 O=81762.0 H=82300.0 L=81762.0 C=82087.2 [G]`
- `21:35 O=82087.2 H=82087.2 L=81646.6 C=81669.9 [R]`
- `21:40 O=81669.9 H=81684.0 L=81522.5 C=81522.5 [R]`
- `21:45 O=81522.5 H=81673.2 L=81416.0 C=81673.2 [G]`
- `21:50 O=81673.2 H=81748.0 L=81624.0 C=81740.6 [G]`
- `21:55 O=81740.6 H=81740.6 L=81610.0 C=81610.0 [R]`

---

## Score reglas extendidas (81%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.027% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | NO | rango alcista |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 81610 · FUERA NY (FUERA_NY) · CRT PD=BULLISH · H1 bias **BULLISH**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/7 (71%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **BULLISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 55%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 5/7 | 30% | 71% OK |
| Rules extendidas (10) | 81% | 15% | meta >70% |
| Neural galería | 53.0% | 30% | no alineado |
| CRT coherence | fail | 10% | rango alcista |
| **Score combinado** | **55%** | 100% |  |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 77792: +3818.0 pts (+4.908%)
- **PDL** 76264: +5346.0 pts (+7.010%)

### Premium / Discount 0.5

- Midpoint 0.5: **77028**
- Posición precio: **PREMIUM** (precio 81610)
- Lectura PD: **BULLISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-03 19:00 O=81254 H=81790 L=81172 C=81755 [G]`
- `09-03 20:00 O=81755 H=81780 L=81393 C=81473 [R]`
- `09-03 21:00 O=81473 H=82300 L=81288 C=81610 [G]`

- Estado CRT H1: **PENDING_BEAR** — Sweep high H1 sin hold

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

- **Neural galería:** 53.0% WIN (grade B)

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 53% | rechazo, WIN |

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
*high signal | 2026-09-03 21:57 UTC*
