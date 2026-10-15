# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-10-15 14:07 UTC | NY 2026-10-15 10:07 | NY AM 10-11
> Precio **80569.2** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6

| Campo | Valor |
|-------|-------|
| Modo bias | **AUTO** |
| Modo setup | **AUTO** |

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **4 de 6** (66%) | Extendidas: **70%**
**Calidad:** Setup fuerte
**Probabilidad histórica:** **~50%** — calibrado walk-forward BTC E1 · 80%: 48–52% · n=2097 (n_eff 755) · EV +0.30R

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 79677-80687; 0.5=80182 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 84054 | Bull si cierre arriba |
| PDL | 81327 | Bear si cierre abajo |
| 0.5 midpoint | 82690 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ✅ | Shorts E1 rechazo resistencia (premium) |

### Reglas revisadas (graduadas)

_✓✓ ≥ +4 pts · ✓ +1 a +4 · ~ neutro · ✗ −1 a −4 · ✗✗ ≤ −4 o veto. Fuente: impacto medido walk-forward n=2097 (n_eff 755)._

| Regla | Estado | Valor actual | Impacto | Acierto histórico | Tipo |
|-------|--------|--------------|---------|-------------------|------|
| RSI M5 vs dirección | ✓✓ | RSI 52.2 (SHORT: neutral) | +4.3 pts | esta zona 54% (n=390) | ponderada |
| Zona premium/discount | ~ | DISCOUNT (en contra) | -0.7 pts | a favor 55% / en contra 45% | ponderada |
| 2 velas M5 confirman | ~ | no | +0.2 pts | sí 43% / no 47% | ponderada |
| Rango CRT coherente | ~ | Shorts E1 rechazo resistencia (premium) | +0.2 pts | sí 46% / no 45% | ponderada |
| Solo E1 | · | Operar solo E1 | — | constante en histórico | info |
| Tendencia H1 alineada | · | Bajista | — | constante en histórico | info |
| R:R mínimo 1:2 | · | 1:2 | — | constante en histórico | info |

### Turtle Soup E2

Score **2/6** | Operable: **NO**
_E2 max 10%; PF E1=4.77; PROHIBIDO eval (TRADING_VISUAL SS7)_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | SÍ | Sweep swing low + reclaim |
| 3. Reclaim agresivo | SÍ | Reclaim M5 |
| 4. Entrada zona SL original | NO | Cerca nivel barrido |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Red flags

- RSI TORYS en contra: Fondo verde TORYS-proxy - filtro long

### Galería (cross-ref)

- Esperar setup fuerte con patrón ganador en historial
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **80569.2** |
| Veredicto | **Esperar** (SHORT) |
| Entrada óptima | **80601.8** |
| ICT | 80569.2→80601.8 · Refinada 80569.2→80601.8 (FVG BEARISH edge) · Sweep swing_high @ 80686.6 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 10-11 |
| Plan | Entry **80601.8** · SL **80850.4** · TP **80104.7** |
| E2 / Break | Sin reversión E2 — E1 primario |
| Métricas | Rules **66%** · Confluencia **MEDIA** — 61% · Rules 66%; 2M5 no listo; Setup auto con dirección; H1 alineado; Vol normal |
| Historial ref | **btc-103** · 2026-10-15 09:56 NY · Entry **80208.4** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry +393.4 pts (+0.491%) · precio→última 360.8 pts (0.450%) · precio→actual 32.6 pts (0.040%) |
| Bando usado (lado asumido) | **AUTO** |
| Bando mercado (H1) | **BEARISH** |
| Chart | — |

---


---

## Entrada optimizada (E1)

> Bias **AUTO** + **AUTO** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **80569.2** | Retest **80388.4–80601.8** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.13% de ref | contexto entry @ 80460.8 |
| Acción | **ENTRAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 80601.8 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **80601.8** (limit retest o market al cierre 2ª vela) |
| SL | **80850.4** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **80104.7** (1:2) |
| R:R | **1:2** · riesgo **248.6** pts |
| Invalidación | Cierre M5 > 80817.7 o breakout > 80460.8 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 80569.2→80601.8 (FVG BEARISH edge) · Sweep swing_high @ 80686.6 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ⚠️ |
| 0.5 midpoint | 82690.3 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY AM 10-11 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 80686.6 + reclaim |
| FVG alineados | 5 |
| Order blocks | 1 |
| Entrada refinada | **80601.8** (antes 80569.2 · FVG BEARISH edge) |
| Nota | Refinada 80569.2→80601.8 (FVG BEARISH edge) · Sweep swing_high @ 80686.6 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en soporte_debil @ 80460.8 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 10-11_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [❌] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem (info, no bloquea entrada).**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BEARISH | Núcleo |
| RSI TORYS | BULLISH | Fondo verde TORYS-proxy - filtro long |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 80461->79977 | LH 81085->80687 |

---

## M5 detalle

- RSI M5/H1: 52.2 / 40.4
- Zona: soporte_debil @ 80461
- 2M5 LONG: SÍ | SHORT: NO

### 12 velas M5

- `13:10 O=80424.9 H=80463.1 L=80279.7 C=80454.2 [G]`
- `13:15 O=80454.6 H=80479.6 L=80350.5 C=80356.5 [R]`
- `13:20 O=80355.5 H=80355.5 L=80262.8 C=80340.2 [R]`
- `13:25 O=80340.2 H=80340.2 L=80104.4 C=80129.0 [R]`
- `13:30 O=80131.0 H=80396.6 L=79977.1 C=80277.4 [G]`
- `13:35 O=80277.3 H=80599.3 L=80028.0 C=80582.4 [G]`
- `13:40 O=80592.0 H=80662.1 L=80472.2 C=80621.1 [G]`
- `13:45 O=80620.8 H=80686.6 L=80208.4 C=80280.3 [R]`
- `13:50 O=80279.5 H=80298.7 L=79761.9 C=79786.1 [R]`
- `13:55 O=79783.3 H=80205.3 L=79676.6 C=80099.2 [G]`
- `14:00 O=80098.0 H=80459.2 L=80000.9 C=80420.5 [G]`
- `14:05 O=80414.5 H=80599.9 L=80398.1 C=80569.2 [G]`

---

## Score reglas extendidas (70%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | NO | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | SÍ | Shorts E1 rechazo resistencia (premium) |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | NO | discount — no short E1 |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

## Cursor HIGH response
1. Usar **Veredicto** + tabla Categories (Precio · Entrada óptima · Confluencia setup).
2. Leer **Entrada optimizada (E1)** + **Checklist 2M5** + **2M5 Válido/Inválido**.
3. Citar CRT pending/completed/invalid + RSI TORYS.
4. Galería WIN match. 5. E2 solo watch. 6. Confirmar TV.
7. En resumen chat: **Salidas** + chart High (líneas OPTI si no `-NoChart`; anotado si Ilustrate).

## Salidas

- **Reporte:** `live/btc_m5_high_signal.md`
- **Reporte (abs):** `D:\Danilo\Trading\Cursor Trading\live\btc_m5_high_signal.md`


---
*high signal | 2026-10-15 14:07 UTC*
