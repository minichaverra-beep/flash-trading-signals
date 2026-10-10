# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-09 18:31 UTC | NY 2026-10-09 14:31 | NY PM 14-16
> Precio **4193.75** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> Última vela M5 **2026-10-09 18:30 UTC** · hace 1 min · fuente MT5 XAUUSDm (broker, M5/H1)
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
**Reglas:** **5 de 6** (83%) | Extendidas: **80%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~58%** — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); H1 BULLISH vs SHORT -6; acuerdo BAJA -8; patron WIN similar +3; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BULLISH** | Longs E1 pullback soporte debil (discount) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **PENDING_BEAR** | Sweep high H1 sin hold |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4146 | Bull si cierre arriba |
| PDL | 4105 | Bear si cierre abajo |
| 0.5 midpoint | 4126 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ✅ | Velas confirman |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 55 OK |
| Rango coherente | ❌ | rango alcista |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: sin calibración — estado por zonas fijas._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓ | RSI 54.6 (SHORT: neutral) | sin calibrar | n/d | ponderada |
| Zona premium/discount | ✓ | PREMIUM (a favor) | sin calibrar | n/d | ponderada |
| 2 velas M5 confirman | ✓ | sí | sin calibrar | n/d | ponderada |
| Rango CRT coherente | ✗ | rango alcista | sin calibrar | n/d | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Bajista | — | constante en histórico | info |
| R:R mínimo 1:2 | · | 1:2 | — | constante en histórico | info |

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

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4193.75** |
| Veredicto | **No operar** (SHORT) |
| Entrada óptima | **4197.53** |
| ICT | 4193.03→4197.53 · Refinada 4193.0→4197.5 (FVG BEARISH edge) · Sweep swing_high @ 4195.6 + reclaim · PD PREMIUM · H1 PENDING_BEAR · killzone NY PM 14-16 |
| Plan | Entry **4197.53** · SL **4203.53** · TP **4185.53** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Neural **57%** · ML **15.3%** · Confluencia **BAJA** — 44% · Rules 83%; Neural débil/gating 57% conf=low; ML 15% veto suave; 2M5 OK; Break con fricción CRT |
| Historial ref | **xauusd-043** · 2026-10-09 10:15 NY · Entry **4191.64** · **BUENA** — precio cerca de última Entry + 2M5 OK + zona OK · (MISMA ZONA) · Δ Entry +5.89 pts (+0.141%) · precio→última 2.11 pts (0.050%) · precio→actual 3.78 pts (0.090%) |
| Bando usado (lado asumido) | **BEARISH** |
| Bando mercado (H1) | **BULLISH** |
| R:R | 1:2 |
| Dist. a Entry | +3.78 pts (0.090%) |
| Dist. a SL | +9.78 pts (0.233%) |
| Dist. a TP | -8.22 pts (0.196%) |
| Riesgo (pts) | 6.00 |
| Winrate setup | ~58% — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); H1 BULLISH vs SHORT -6; acuerdo BAJA -8; patron WIN similar +3; 83% reglas |
| Zona PD vs dirección | SHORT en PREMIUM +2 (zona a favor) |
| Bias vs dirección | H1 BULLISH vs SHORT -6 |
| Score Rules extendido | **80%** |
| Estado 2M5 | VÁLIDO SHORT (2M5) |
| Bias H1 vs bando | H1 **BULLISH** · CLI **BEARISH** |
| Calidad break/reverse | BREAK (continuación E1) |
| Neural grade/conf | **B** · conf. low · 57% WIN |
| Rules E1 detalle | **5/6** (83%) |
| Vol Zentinel (filtro) | **muy_bajo** · 0.26× · Zentinel_US30_E1 |
| MACD-quant (filtro) | **en contra** · Hist 8.691 · never trigger |
| Watchtower KZ | NY PM 14-16 · Watchtower_US30_E1 |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (breakout)** · CRT PD **BULLISH** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4193.75** | Retest **4189.94–4197.53** |
| 2M5 SHORT | Sí | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.00% de ref | contexto entry @ 4193.71 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT (condiciones actuales OK)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 4197.53 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **4197.53** (limit retest o market al cierre 2ª vela) |
| SL | **4203.53** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4185.53** (1:2) |
| R:R | **1:2** · riesgo **6.00** pts |
| Invalidación | Cierre M5 > 4199.03 o breakout > 4193.71 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4193.0→4197.5 (FVG BEARISH edge) · Sweep swing_high @ 4195.6 + reclaim · PD PREMIUM · H1 PENDING_BEAR · killzone NY PM 14-16 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 4125.55 |
| H1 CRT state | **PENDING_BEAR** |
| Killzone / sesión | NY PM 14-16 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 4195.6 + reclaim |
| FVG alineados | 4 |
| Order blocks | 5 |
| Entrada refinada | **4197.53** (antes 4193.03 · FVG BEARISH edge) |
| Nota | Refinada 4193.0→4197.5 (FVG BEARISH edge) · Sweep swing_high @ 4195.6 + reclaim · PD PREMIUM · H1 PENDING_BEAR · killzone NY PM 14-16 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 4193.71 | **VÁLIDO** — Últimas 2 rojas en zona ≤0.15% | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [R][R] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY PM 14-16_

- [✅] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Las 4 ✅ → 2M5 OK.**

---


## Indicadores Legacy Pro (proxy)

| CRT | PENDING_BEAR/BULLISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BULL | +DI domina (9/8) |
| Swings | HL 4185->4187 | HH 4196->4200 |

---

## M5 detalle

- RSI M5/H1: 54.6 / 57.6
- Zona: resistencia_debil @ 4194
- 2M5 LONG: NO | SHORT: SÍ

### 12 velas M5

- `17:35 O=4191.04 H=4194.29 L=4191.04 C=4193.16 [G]`
- `17:40 O=4193.20 H=4194.33 L=4192.85 C=4192.92 [R]`
- `17:45 O=4192.97 H=4195.24 L=4192.46 C=4194.23 [G]`
- `17:50 O=4194.20 H=4197.52 L=4193.59 C=4196.89 [G]`
- `17:55 O=4196.90 H=4197.38 L=4195.04 C=4195.53 [R]`
- `18:00 O=4195.40 H=4197.47 L=4195.34 C=4195.49 [G]`
- `18:05 O=4195.61 H=4199.16 L=4195.61 C=4198.94 [G]`
- `18:10 O=4198.98 H=4200.39 L=4197.53 C=4198.25 [R]`
- `18:15 O=4198.05 H=4198.05 L=4195.70 C=4196.64 [R]`
- `18:20 O=4196.62 H=4197.39 L=4195.92 C=4196.20 [R]`
- `18:25 O=4195.93 H=4196.55 L=4195.24 C=4195.59 [R]`
- `18:30 O=4195.55 H=4196.32 L=4193.23 C=4193.75 [R]`

---

## Score reglas extendidas (80%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | SÍ | Velas confirman |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 55 OK |
| Rango coherente | NO | rango alcista |
| DMI alineado | NO | +DI domina (9/8) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

> **Modo ADVANCED** — análisis profundo (ML + Neural + CRT + E2)

## A) Síntesis ejecutiva

- **Contexto macro:** Precio 4194 · reloj NY PM 14-16 · CRT PD=BULLISH · H1 bias **BULLISH**
- **Setup:** NO_OPERAR SHORT · dirección **SHORT** · modo **BREAK** · reglas E1 5/6 (83%)
- **Conflicto bando:** CLI **BEARISH** vs mercado H1 **BULLISH** — confirmar en TradingView antes de ejecutar
- **Veredicto integrado:** NO_OPERAR — score combinado 46%

---

## B) Scorecard multicapa

| Capa | Score | Peso | Nota |
|------|-------|------|------|
| Rules E1 | 5/6 | 28% | 83% OK |
| Rules extendidas (10) | 80% | 12% | meta >70% |
| CRT coherence | fail | 12% | rango alcista |
| Neural galería (gated) | 56.8% | 25% | no alineado; conf=low; gate×0.35 → 52% |
| ML tabular (gated) | 15.3% | 18% | grade C; conf=high; → 15% |
| Penalización dirección | ×0.88 | — | penalización H1 BULLISH vs SHORT |
| Bonificación ubicación | ×1.03 | — | SHORT en PREMIUM (zona a favor) |
| Acuerdo entre capas | 44% | 38% | blend 62/38 con acuerdo BAJA 44% |
| **Probabilidad de éxito** | **46%** | 100% | pesos + acuerdo entre capas |

---

## C) CRT deep dive

### Distancias PDH/PDL

- **PDH** 4146: +47.8 pts (+1.154%)
- **PDL** 4105: +88.6 pts (+2.158%)

### Premium / Discount 0.5

- Midpoint 0.5: **4126**
- Posición precio: **PREMIUM** (precio 4194)
- Lectura PD: **BULLISH**

### Fakeout — análisis paso a paso

- Sin fakeout PDH/PDL detectado en ventana M5 reciente

### Timeline H1 (últimas 3 velas)

- `10-09 16:00 O=4188 H=4194 L=4185 C=4191 [G]`
- `10-09 17:00 O=4191 H=4198 L=4187 C=4196 [G]`
- `10-09 18:00 O=4195 H=4200 L=4193 C=4194 [R]`

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

- **Neural galería:** 56.8% WIN (grade B, conf low) · gate×0.35 → 52% efectivo

---

## F) Galería WIN/LOSS match

| # | Patrón | Archivo | Similitud | Tags |
|---|--------|---------|-----------|------|
| 1 | WIN: Rechazo resistencia (BTC-02-07-26) | BTC-02-07-26.png | 57% | rechazo, WIN |

- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

---

## H) Psicología y guardas

- ❓ ¿2 SL hoy? — confirmar trader (límite de riesgo diario)

> **Frase guía:** "Si no es A+ con CRT + 2 velas M5, es ESPERAR — el mercado mañana sigue ahí." (TRADING_VISUAL §7)

---


---

### Zentinel (presets TV → stack local)

- **FVG+Vol:** `Zentinel_US30_E1` — alto 1.6 / extremo 2.8 / bajo 0.7 / muy bajo 0.4 / período 48 · **rol: filtro, nunca trigger**
- **Watchtower:** `Watchtower_US30_E1` — KZ NY only (08-10 · 10-11 · 14-16) · ahora **NY PM 14-16**
- **Vol relativo:** 0.26× → banda **muy_bajo** (vol×0.26 ≤ muy_bajo 0.4)
- **Bias table:** avg 3 · neutral 0.3%
- Checklist TV manual (stack no lee indicadores en vivo).

### MACD-quant (filtro E1 · H4)

- **Rol:** confluence_filter — **NUNCA trigger solo**. Entrada = H1/CTR + zona + 2M5.
- **TF filtro:** H4 · fuente `h1_resample_h4` · Hist: 8.691 · soft-filter vs setup: **en contra**
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
*high signal | 2026-10-09 18:31 UTC*
