# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-30 14:31 UTC | NY 2026-09-30 10:31 | NY AM 10-11
> Precio **51790.0** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6

| Campo | Valor |
|-------|-------|
| Modo bias | **AUTO** |
| Modo setup | **AUTO** |

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 6** (83%) | Extendidas: **90%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~74%** — histórico E1 BTC · SHORT en PREMIUM +2 (zona a favor); H1 BEARISH a favor +4; acuerdo MEDIA -2; patron WIN similar +3; 83% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 51685-51806; 0.5=51746 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 52002 | Bull si cierre arriba |
| PDL | 51459 | Bear si cierre abajo |
| 0.5 midpoint | 51730 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 48 OK |
| Rango coherente | ✅ | No forzar; esperar pending CRT HTF |

### Turtle Soup E2

Score **0/6** | Operable: **NO**
_E2 max 10%; PF E1=4.77; PROHIBIDO eval (TRADING_VISUAL SS7)_

| Check | OK | Detalle |
|-------|----|---------|
| 1. Reversion MACRO | NO | Barrido pool/PDL-PDH |
| 2. Rompe min/max previo | NO | Sweep liquidez |
| 3. Reclaim agresivo | NO | Cierre M5 reclaim |
| 4. Entrada zona SL original | NO | Cerca nivel barrido |
| 5. SL grande E2 | NO | No SL $9 E1 |
| 6. Max 1/sem NO eval | NO | Confirmar bitacora |

### Red flags

- Precio dentro PDH/PDL — contexto NEUTRAL, no forzar
- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **51790.0** |
| Veredicto | **Esperar** (SHORT) |
| Entrada óptima | **51825.0** |
| ICT | 51793.4→51825.0 · Refinada 51793.4→51825.0 (FVG BEARISH edge) · Sweep swing_high @ 51806.0 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |
| Plan | Entry **51825.0** · SL **51885.0** · TP **51705.0** |
| E2 / Break | Sin reversión E2 — E1 primario |
| Métricas | Rules **83%** · Confluencia **MEDIA** — 53% · Rules 83%; 2M5 no listo; Setup auto con dirección; H1 alineado; Vol muy bajo |
| Historial ref | **us30-036** · 2026-09-29 14:09 NY · Entry **51572.0** · **REGULAR** — precio cerca de Entry actual; sin 2M5; zona OK · (MÁS CERCA) · Δ Entry +253.0 pts (+0.491%) · precio→última 218.0 pts (0.423%) · precio→actual 35.0 pts (0.068%) |
| Bando usado (lado asumido) | **AUTO** |
| Bando mercado (H1) | **BEARISH** |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **AUTO** + **AUTO** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **51790.0** | Retest **51759.4–51825.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Zona (info) | 0.03% de ref | contexto entry @ 51806.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT (ICT retest · FVG BEARISH edge)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest FVG BEARISH edge @ 51825.0 + 2 velas M5 rojas en zona |
| Confirmación | 2 velas M5 rojas consecutivas (zona ref info) |
| Entry | **51825.0** (limit retest o market al cierre 2ª vela) |
| SL | **51885.0** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **51705.0** (1:2) |
| R:R | **1:2** · riesgo **60.0** pts |
| Invalidación | Cierre M5 > 51853.4 o breakout > 51806.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 51793.4→51825.0 (FVG BEARISH edge) · Sweep swing_high @ 51806.0 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **PREMIUM** ✅ |
| 0.5 midpoint | 51730.5 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | NY AM 10-11 ✅ |
| Displacement M5 | No |
| Liquidity sweep | Sweep swing_high @ 51806.0 + reclaim |
| FVG alineados | 5 |
| Order blocks | 3 |
| Entrada refinada | **51825.0** (antes 51793.4 · FVG BEARISH edge) |
| Nota | Refinada 51793.4→51825.0 (FVG BEARISH edge) · Sweep swing_high @ 51806.0 + reclaim · PD PREMIUM · H1 INSIDE_RANGE · killzone NY AM 10-11 |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 51806.0 | Referencia — requiere 2 rojas **nuevas** en dirección | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): NY AM 10-11_

- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | NEUTRAL | Momentum mixto |
| Swings | LL 51670->51642 | LH 51894->51806 |

---

## M5 detalle

- RSI M5/H1: 47.8 / 45.4
- Zona: resistencia_debil @ 51806
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `13:30 O=51808.0 H=51832.0 L=51694.0 C=51721.0 [R]`
- `13:35 O=51719.0 H=51767.0 L=51699.0 C=51732.0 [G]`
- `13:40 O=51731.0 H=51746.0 L=51664.0 C=51677.0 [R]`
- `13:45 O=51677.0 H=51723.0 L=51642.0 C=51718.0 [G]`
- `13:50 O=51719.0 H=51750.0 L=51685.0 C=51724.0 [G]`
- `13:55 O=51726.0 H=51734.0 L=51666.0 C=51712.0 [R]`
- `14:00 O=51716.0 H=51738.0 L=51685.0 C=51735.0 [G]`
- `14:05 O=51736.0 H=51806.0 L=51731.0 C=51738.0 [G]`
- `14:10 O=51741.0 H=51799.0 L=51722.0 C=51752.0 [G]`
- `14:15 O=51754.0 H=51782.0 L=51740.0 C=51763.0 [G]`
- `14:20 O=51762.0 H=51793.0 L=51754.0 C=51778.0 [G]`
- `14:21 O=51790.0 H=51790.0 L=51790.0 C=51790.0 [G]`

---

## Score reglas extendidas (90%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 48 OK |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF |
| DMI alineado | SÍ | Momentum mixto |
| 0.5 midpoint E1 | SÍ | premium OK |
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

- **Reporte:** `live/us30_m5_high_signal.md`
- **Chart:** **Preview en navegador**


---
*high signal | 2026-09-30 14:31 UTC*
