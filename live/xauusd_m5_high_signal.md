# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-01 15:17 UTC | NY 2026-10-01 11:17 | FUERA_NY (Lunch)
> Precio **4157.70** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-01 15:07 UTC** · hace 10 min · fuente yfinance (GC=F, M5=5m) · ajustado a spot gold-api (basis +26.20)
> **Modo:** BULLISH + REVERSE — Bias CLI **BULLISH** — setup re-puntuado como LONG
> Modo **ADVANCED** — Categories ampliada + secciones A–I

| Campo | Valor |
|-------|-------|
| Modo bias | **BULLISH** |
| Modo setup | **REVERSE (E2)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BULLISH** — setup re-puntuado como LONG
- ⚠ H1 bajista vs bias forzado — confirmar en TV antes de entrar
- Setup **REVERSE** — turtle soup / PDH-PDL fakeout / sweep+reclaim
- E2: E2_NO (2/6) · operable=NO · WR ~61%

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Alcista
**Reglas:** **5 de 6** (83%) | Extendidas: **90%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~48%** — histórico E2 reversión BTC · LONG en DISCOUNT +4 (E2 a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patrones mixtos -4; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo REVERSE: turtle soup / fakeout / sweep+reclaim |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **PENDING_BEAR** | Sweep high H1 sin hold |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4225 | Bull si cierre arriba |
| PDL | 4152 | Bear si cierre abajo |
| 0.5 midpoint | 4188 | Filtro 50% |

**Nota CRT:** REVERSE: H1 PENDING_BEAR — sweep+reclaim E2 ctx

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | ✅ | Alcista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF | Mod |

### Turtle Soup E2

Score **2/6** | Operable: **NO** | Winrate: **~61%**
_Modo REVERSE: falta 2 velas M5 misma dirección del bando — no operable aún (WR E2 ~61% si se confirma)_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | NO | Sweep liquidez |
| 3. Reclaim agresivo | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | NO | Esperar 2 velas alineadas |
| 8. Winrate E2 | SÍ | ~61% |

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- CRT H1 pending bear — no entrar long contra invalid reciente

### Galería (cross-ref)

- Patrón ganador similar: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4157.70** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **4156.61** |
| ICT | Base 4156.6 (zona base) · Sweep swing_high @ 4178.6 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |
| Plan | Entry **4156.61** · SL **4150.61** · TP **4168.61** |
| E2 / Break | REVERSE / E2 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **54%** · ML **1.9%** · Confluencia **BAJA** — 27% · Rules 83%; Neural débil/gating 54% conf=low; ML 2% veto suave; 2M5 no listo; E2 no operable |
| Historial ref | **xauusd-013** · 2026-10-01 10:31 NY · Entry **4165.57** · **REGULAR** — cerca suave de última Entry; precio cerca de Entry actual; sin 2M5 · (MÁS CERCA) · Δ Entry -8.97 pts (-0.215%) · precio→última 7.87 pts (0.189%) · precio→actual 1.09 pts (0.026%) |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| R:R | 1:2 |
| Dist. a Entry | -1.09 pts (0.026%) |
| Dist. a SL | -7.09 pts (0.171%) |
| Dist. a TP | +10.91 pts (0.262%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~48% — histórico E2 reversión BTC · LONG en DISCOUNT +4 (E2 a favor); H1 BEARISH vs LONG -6; acuerdo BAJA -8; patrones mixtos -4; 83% reglas |
| Zona PD vs dirección | LONG en DISCOUNT +4 (E2 a favor) |
| Bias vs dirección | H1 BEARISH vs LONG -6 |
| Score Rules extendido | **90%** |
| Estado 2M5 | Sin 2M5 (info, no gate) |
| Bias H1 vs bando | H1 **BEARISH** · CLI **BULLISH** |
| Calidad break/reverse | REVERSE watch (E2_NO) |
| Neural grade/conf | **B** · conf. low · 54% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.00× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **OK** · Hist 5.418 · never trigger |
| Watchtower KZ | FUERA_NY (Lunch) · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **REVERSE (E2)** · CRT PD **NEUTRAL** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4157.70** | Retest **4154.60–4158.34** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.07% de ref | contexto entry @ 4154.60 |
| Acción | **ENTRAR LONG** | **ENTRAR LONG** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 4154.60–4158.34 (soporte_debil @ 4154.60) + 2 velas M5 verdes consecutivas en zona |
| Confirmación | 2 velas M5 verdes consecutivas (zona ref info) |
| Entry | **4156.61** (limit retest o market al cierre 2ª vela) |
| SL | **4150.61** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4168.61** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 < 4150.61 o breakdown < 4154.60 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Base 4156.6 (zona base) · Sweep swing_high @ 4178.6 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 4188.45 |
| H1 CRT state | **PENDING_BEAR** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4178.6 + reclaim |
| FVG alineados | 5 |
| Order blocks | 1 |
| Entrada | **4156.61** (zona base · sin cambio) |
| Nota | Base 4156.6 (zona base) · Sweep swing_high @ 4178.6 + reclaim · PD DISCOUNT · H1 PENDING_BEAR |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 4154.60 | Referencia — requiere 2 verdes **nuevas** en dirección | Patrón válido LONG en soporte |
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

| CRT | PENDING_BEAR/NEUTRAL | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 4163->4155 | HH 4170->4179 |

---

## M5 detalle

- RSI M5/H1: 50.0 / 47.4
- Zona: soporte_debil @ 4155
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:15 O=4157.20 H=4161.90 L=4157.10 C=4160.00 [G]`
- `14:20 O=4159.90 H=4165.10 L=4159.20 C=4164.10 [G]`
- `14:25 O=4164.20 H=4169.10 L=4161.50 C=4165.90 [G]`
- `14:30 O=4165.50 H=4172.30 L=4163.60 C=4170.20 [G]`
- `14:35 O=4170.40 H=4178.60 L=4168.80 C=4177.20 [G]`
- `14:40 O=4176.90 H=4178.00 L=4169.20 C=4169.90 [R]`
- `14:45 O=4170.10 H=4174.10 L=4167.20 C=4172.80 [G]`
- `14:50 O=4172.10 H=4173.50 L=4165.30 C=4167.50 [R]`
- `14:55 O=4167.30 H=4171.00 L=4163.10 C=4166.30 [R]`
- `15:00 O=4166.10 H=4166.40 L=4156.30 C=4157.40 [R]`
- `15:05 O=4157.90 H=4159.40 L=4155.40 C=4156.80 [R]`
- `15:07 O=4157.70 H=4157.70 L=4157.70 C=4157.70 [G]`

---

## Score reglas extendidas (90%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Modo REVERSE — E2 permitido |
| Tendencia H1 alineada | SÍ | Alcista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4158 · reloj FUERA_NY (Lunch) · CRT PD=NEUTRAL · H1 bias **BEARISH**
- **Setup:** NO_OPERAR LONG · dirección **LONG** · modo **REVERSE** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BULLISH** vs mercado H1 **BEARISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 45%
- **E2 contexto:** E2_NO (2/6) · operable=NO · WR ~61%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 90% | 12% | meta >70% |
| CRT coherence | pass | 12% | No forzar; esperar pending CRT HTF | Mod |
| Neural galería (gated) | 54.4% | 25% | no alineado; conf=low; gate×0.35 → 52% |
| ML tabular (gated) | 1.9% | 18% | grade C; conf=high; → 2% |
| E2 turtle | 2/6 | 5% | E2_NO |
| Penalización dirección | ×0.88 | — | penalización H1 BEARISH vs LONG |
| Bonificación ubicación | ×1.06 | — | LONG en DISCOUNT (zona a favor) |
| Acuerdo entre capas | 27% | 38% | blend 62/38 con acuerdo BAJA 27% |
| **Probabilidad de éxito** | **45%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4225: -67.2 pts (-1.591%)
- **PDL** 4152: +5.7 pts (+0.137%)

### Premium / Discount 0.5

- Midpoint 0.5: **4188**
- Posición precio: **DISCOUNT** (precio 4158)
- Lectura PD: **NEUTRAL**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-01 14:00 O=4169 H=4179 L=4155 C=4166 [R]`
- `10-01 15:00 O=4166 H=4166 L=4155 C=4157 [R]`
- `10-01 15:07 O=4158 H=4158 L=4158 C=4158 [G]`

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
| 4. Entrada zona SL original | ✅ | SÍ | Cerca pool post sweep |
| 5. SL grande E2 | ❌ | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | ❌ | NO | Confirmar bitacora |
| 7. 2 velas misma dirección | ❌ | NO | Esperar 2 velas alineadas |
| 8. Winrate E2 | ✅ | SÍ | ~61% |

**Score:** 2/6 · Veredicto: **E2_NO**

### Interpretación fakeout PDL/PDH

- Sin fakeout macro activo — E2 requiere sweep+reclaim explícito

### Decisión E2: **NO ENTRAR** — setup Reverse incompleto · WR ~61%

---

## E) Cruce Neural + Rules

**Acuerdo Rules/Neural:** NEUTRAL

- Ambos en zona media — decidir con Rules % y CRT

- **Neural galería:** 54.4% WIN (grade B, conf low) · gate×0.35 → 52% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Sweep+reclaim (BTC-11-05-26, BTC-27-07-26) | BTC-11-05-26.png | 54% | sweep+reclaim, WIN |
| 2 | LOSS: contra bias (BTC-01-06-26) | BTC-01-06-26.png | 49% | contra-bias, LOSS |

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
- **Vol relativo:** 0.00× → banda **muy_bajo** (vol×0.00 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 5.418 · soft-filter vs setup: **alineado**
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
*high signal | 2026-10-01 15:17 UTC*
