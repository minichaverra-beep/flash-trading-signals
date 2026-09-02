# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-02 15:43 UTC | NY 2026-09-02 11:43 | FUERA_NY
> Precio **77373.52** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> **Modo:** BEARISH + BREAK — Bias CLI **BEARISH** — setup re-puntuado como SHORT

| Campo | Valor |
|-------|-------|
| Modo bias | **BEARISH** |
| Modo setup | **BREAK (E1)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BEARISH** — setup re-puntuado como SHORT
- Setup **BREAK** — foco E1 CRT continuación; E2 despriorizado

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **6 de 8** (75%) | Extendidas: **66%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~82%** — patrón ganador similar · histórico E1 BTC

## Categories

| Campo | Valor |
|-------|-------|
| Bando usado | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| Recomendación | **NO_OPERAR — fin sesión (SHORT)** |
| Segunda indicación | **LONG** (H1 NEUTRAL — ver sección abajo) |
| Neural galería | **53% WIN** — grade **B** (baja similitud con galería WIN; conf. low) |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: priorizar continuación E1 CRT |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BULL** | Sweep low H1 + reclaim |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 79221 | Bull si cierre arriba |
| PDL | 76420 | Bear si cierre abajo |
| 0.5 midpoint | 77820 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Sesión NY | ❌ | FUERA_NY |
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.030% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Turtle Soup E2

Score **0/6** | Operable: **NO** (default NO)
_Modo BREAK: E1 continuación primario — E2 solo contexto, NO operable_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | NO | Sweep liquidez |
| 3. Reclaim agresivo | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | NO | Cerca nivel barrido |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Red flags

- Fuera ventana NY — NO_OPERAR
- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- CRT H1 pending bull — no entrar short contra invalid reciente
- Fuera de ventana NY (regla 2)
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (E1)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **77373.5** | Retest **77280.9–77397.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.03%) | ✅ ≤0.15% de 77397.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 77280.9–77397.0 (resistencia_debil @ 77397.0) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas con cierres en zona ≤0.15% |
| Entry | **77356.3** (limit retest o market al cierre 2ª vela) |
| SL | **77551.8** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **76965.5** |
| R:R | **1:2** · riesgo **195.4** pts |
| Invalidación | Cierre M5 > 77551.8 o breakout > 77397.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |

---

## Ilustración entrada (2M5 + óptima)

![annotated](btc_m5_chart_annotated.png)

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 77397.0 | Referencia — requiere 2 rojas **nuevas** en retest | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

- [❌] Sesión NY activa
- [✅] Cerca de zona (resistencia_debil @ 77397)
- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **LONG**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | +DI domina (968/804) | **LONG** |
| CRT PD / Premium-Discount | NEUTRAL · DISCOUNT | **LONG** |
| Estructura swings M5 | LL 77110->76748 · LH 77490->77397 | **SHORT** |

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BULL/NEUTRAL | Núcleo |
| RSI TORYS | BEARISH | Fondo rojo TORYS-proxy - filtro short |
| DMI | BULL | +DI domina (968/804) |
| Swings | LL 77110->76748 | LH 77490->77397 |

---

## M5 detalle

- RSI M5/H1: 54.6 / 56.1
- Zona: resistencia_debil @ 77397
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:45 O=77325.0 H=77334.2 L=77176.0 C=77224.0 [R]`
- `14:50 O=77224.0 H=77240.0 L=77091.1 C=77120.5 [R]`
- `14:55 O=77120.5 H=77212.0 L=77066.4 C=77066.4 [R]`
- `15:00 O=77066.4 H=77182.0 L=76862.9 C=77070.4 [G]`
- `15:05 O=77070.4 H=77147.7 L=76824.0 C=76852.2 [R]`
- `15:10 O=76852.2 H=76852.2 L=76748.0 C=76820.0 [R]`
- `15:15 O=76820.0 H=77142.0 L=76816.9 C=77130.3 [G]`
- `15:20 O=77130.3 H=77147.7 L=76950.0 C=77004.8 [R]`
- `15:25 O=77004.8 H=77122.0 L=76984.6 C=77039.9 [G]`
- `15:30 O=77039.9 H=77350.0 L=76994.0 C=77294.0 [G]`
- `15:35 O=77294.0 H=77338.0 L=77144.0 C=77144.0 [R]`
- `15:40 O=77144.0 H=77383.7 L=77117.6 C=77373.5 [G]`

---

## Score reglas extendidas (66%)

| Regla | OK | Nota |
|-------|----|------|
| Sesión NY | NO | FUERA_NY |
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.030% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | NO | +DI domina (968/804) |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 77374 · FUERA NY (FUERA_NY) · CRT PD=NEUTRAL · H1 bias **NEUTRAL**
- **Setup:** NO_OPERAR — fin sesión (SHORT) · dirección **SHORT** · modo **BREAK** · reglas E1 6/8 (75%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **NEUTRAL** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** ESPERAR — score 70% requiere confirmación TV

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 (8) | 6/8 | 30% | 75% OK |
| Rules extendidas (10) | 66% | 15% | meta >70% |
| Neural galería | 53.0% | 30% | no alineado |
| CRT coherence | pass | 10% | No forzar; esperar pending CRT HTF | Mod |
| **Score combinado** | **70%** | 100% |  |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 79221: -1847.1 pts (-2.332%)
- **PDL** 76420: +953.5 pts (+1.248%)

### Premium / Discount 0.5

- Midpoint 0.5: **77820**
- Posición precio: **DISCOUNT** (precio 77374)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `09-02 13:00 O=76614 H=77444 L=76614 C=77146 [G]`
- `09-02 14:00 O=77146 H=77490 L=77010 C=77066 [R]`
- `09-02 15:00 O=77066 H=77384 L=76748 C=77374 [G]`

- Estado CRT H1: **PENDING_BULL** — Sweep low H1 + reclaim

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

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 53.0% WIN (grade B)

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 53% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## G) Plan de trading

- **Entrada:** SHORT @ zona resistencia_debil 77397 (precio actual 77374)
- **SL estructural:** 77552 | **SL cuenta:** ~$9 (ajustar lotaje)
- **TP 1:2:** 77017 | **BE:** mover a BE en 1:1
- **Invalidación:** cierre M5 fuera zona / CRT invalid / fakeout contra dirección
- **Confluencias Notion sugeridas:** Continuación E1, Zona débil morada, Sesión NY, CRT alineado

### Pre-trade checklist (8 ítems)

| # | Ítem | OK |
|---|------|----|
| 1 | Sesión NY activa | ❌ |
| 2 | Bias H1 alineado | ❌ |
| 3 | Zona ≤0.15% | ✅ |
| 4 | 2 velas M5 confirmación | ❌ |
| 5 | Rules E1 ≥63% | ✅ |
| 6 | Extendidas ≥70% | ❌ |
| 7 | Sin fakeout contra | ✅ |
| 8 | SL ~$9 definido | ✅ |

---

## H) Psicología y guardas de sesión

- ⛔ Fuera ventana NY — regla dura NO_OPERAR
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
Leer secciones A–I arriba. **NO acortar** vs light mode.


---
*high signal | 2026-09-02 15:43 UTC*
