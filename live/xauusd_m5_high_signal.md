# XAUUSD M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-23 16:25 UTC | NY 2026-09-23 12:25 | FUERA_NY (Lunch)
> Precio **4318.80** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6
> **Modo:** BULLISH + BREAK — Bias CLI **BULLISH** — setup re-puntuado como LONG

| Campo | Valor |
|-------|-------|
| Modo bias | **BULLISH** |
| Modo setup | **BREAK (breakout)** |

---

### Modo CLI (bias/setup)

- Bias CLI **BULLISH** — setup re-puntuado como LONG
- ⚠ H1 bajista vs bias forzado — confirmar en TV antes de entrar
- Setup **BREAK** — breakout de nivel/estructura (no reversión/fakeout)
- Sin breakout de nivel detectado

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 7** (71%) | Extendidas: **72%**
**Calidad:** Setup débil
**Probabilidad histórica:** **baja** — patrón perdedor similar — evitar

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) | Modo BREAK: breakout de nivel/estructura (no reversión) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4314-4321; 0.5=4318 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4414 | Bull si cierre arriba |
| PDL | 4328 | Bear si cierre abajo |
| 0.5 midpoint | 4371 | Filtro 50% |

**Nota CRT:** BREAK pendiente: Sin breakout de nivel detectado

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| Cerca de zona clave | ✅ | a 0.035% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 35 OK |
| Rango coherente | ❌ | rango bajista |

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

- Precio < PDL — no long contra rango bajista CRT
- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón perdedor similar: contra bias (BTC-01-06-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **4318.80** |
| Veredicto | **No operar** (LONG) |
| Entrada óptima | **4317.30** |
| ICT | 4319.57→4317.30 · Refinada 4319.6→4317.3 (soporte debil) · Sweep PDL @ 4327.6 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |
| Plan | Entry **4317.30** · SL **4308.67** · TP **4334.57** |
| E2 / Break | BREAK / E1 — Sin reversión E2 — E1 primario |
| Métricas | Rules **71%** · Confluencia **BAJA** — 41% · Rules 71%; 2M5 o zona parcial; Break con fricción CRT; CLI alineado / H1 no; Vol muy bajo |
| Historial ref | — · **SIN HISTORIAL** · live **REGULAR** — sin historial; precio cerca de Entry actual; sin 2M5; zona OK |
| Bando usado (lado asumido) | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| Chart | — |

---


---

## Entrada optimizada (E1)

> Bias **BULLISH** + **BREAK (breakout)** · CRT PD **BEARISH** · Premium/Discount **DISCOUNT**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **4318.80** | Retest **4317.30–4323.78** |
| 2M5 LONG | No | Nuevas 2 verdes en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.03%) | ✅ ≤0.15% de 4317.30 |
| Acción | **ESPERAR LONG** | **ENTRAR LONG (ICT retest · soporte debil)** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | ICT retest soporte debil @ 4317.30 + 2 velas M5 verdes en zona |
| Confirmación | 2 velas M5 verdes consecutivas con cierres en zona ≤0.15% |
| Entry | **4317.30** (limit retest o market al cierre 2ª vela) |
| SL | **4308.67** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP | **4334.57** (1:2) |
| R:R | **1:2** · riesgo **8.63** pts |
| Invalidación | Cierre M5 < 4308.67 o breakdown < 4317.30 sin reclaim |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |
| ICT nota | Refinada 4319.6→4317.3 (soporte debil) · Sweep PDL @ 4327.6 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |

---

## ICT scan (entrada)

| Concepto | Detalle |
|----------|---------|
| Premium/Discount | **DISCOUNT** ✅ |
| 0.5 midpoint | 4370.85 |
| H1 CRT state | **INSIDE_RANGE** |
| Killzone / sesión | FUERA_NY (Lunch) (info) |
| Displacement M5 | No |
| Liquidity sweep | Sweep PDL @ 4327.6 + reclaim |
| FVG alineados | 2 |
| Order blocks | 5 |
| Entrada refinada | **4317.30** (antes 4319.57 · soporte debil) |
| Nota | Refinada 4319.6→4317.3 (soporte debil) · Sweep PDL @ 4327.6 + reclaim · PD DISCOUNT · H1 INSIDE_RANGE |

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ LONG OK: [G][G] en soporte_debil @ 4317.30 | **VÁLIDO** — Últimas 2 verdes en zona ≤0.15% | Patrón válido LONG en soporte |
| ❌ NO: [R][G] | **INVÁLIDO** | 1ª vela roja invalida secuencia LONG |
| ❌ NO: [G][G] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

_Reloj (info): FUERA_NY (Lunch)_

- [✅] Cerca de zona (soporte_debil @ 4317)
- [❌] 2 velas M5 confirman LONG
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/BEARISH | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (25/13) |
| Swings | LL 4314->4313 | LH 4334->4321 |

---

## M5 detalle

- RSI M5/H1: 34.9 / 16.5
- Zona: soporte_debil @ 4317
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `15:25 O=4328.20 H=4330.20 L=4319.10 C=4319.60 [R]`
- `15:30 O=4319.70 H=4320.50 L=4316.60 C=4320.30 [G]`
- `15:35 O=4319.90 H=4322.00 L=4314.70 C=4315.90 [R]`
- `15:40 O=4315.70 H=4320.70 L=4314.90 C=4320.10 [G]`
- `15:45 O=4319.80 H=4321.30 L=4313.30 C=4314.40 [R]`
- `15:50 O=4314.20 H=4317.40 L=4313.60 C=4317.00 [G]`
- `15:55 O=4317.00 H=4318.60 L=4316.60 C=4318.30 [G]`
- `16:00 O=4318.30 H=4319.40 L=4314.90 C=4315.60 [R]`
- `16:05 O=4315.20 H=4320.60 L=4314.50 C=4318.70 [G]`
- `16:10 O=4318.80 H=4320.10 L=4318.00 C=4319.20 [G]`
- `16:15 O=4319.40 H=4320.40 L=4318.80 C=4320.20 [G]`
- `16:15 O=4318.80 H=4318.80 L=4318.80 C=4318.80 [G]`

---

## Score reglas extendidas (72%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Alcista |
| Cerca de zona clave | SÍ | a 0.035% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 35 OK |
| Rango coherente | NO | rango bajista |
| DMI alineado | NO | -DI domina (25/13) |
| 0.5 midpoint E1 | SÍ | discount OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

## Cursor HIGH response
1. Usar **Veredicto** + tabla Categories (Precio · Entrada óptima · Confluencia setup).
2. Leer **Entrada optimizada (E1)** + **Checklist 2M5** + **2M5 Válido/Inválido**.
3. Citar CRT pending/completed/invalid + RSI TORYS.
4. Galería WIN match. 5. E2 solo watch. 6. Confirmar TV.
7. En resumen chat: **Salidas** + chart High (líneas OPTI si no `-NoChart`; anotado si Ilustrate).

![Chart](xauusd_m5_chart.png)
## Salidas

- **Reporte:** `live/xauusd_m5_high_signal.md`
- **Reporte (abs):** `D:\Danilo\Trading\Cursor Trading\live\xauusd_m5_high_signal.md`


---
*high signal | 2026-09-23 16:25 UTC*
