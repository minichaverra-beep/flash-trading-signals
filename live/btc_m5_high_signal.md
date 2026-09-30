# BTC M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-30 14:32 UTC | NY 2026-09-30 10:32 | NY AM 10-11
> Precio **83672.0** | HIGH mode | PF E1=4.77 | E2 max 10%
> Plan refs: TRADING_VISUAL SS1.1-1.2 SS7 | TRADING_INDICATORS_RULES SS3-6

| Campo | Valor |
|-------|-------|
| Modo bias | **AUTO** |
| Modo setup | **AUTO** |

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **3 de 6** (50%) | Extendidas: **66%**
**Calidad:** No operar
**Probabilidad histórica:** **~48%** — histórico E1 BTC · acuerdo NULA -12; patron LOSS similar -12; 50% reglas

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **COMPLETED_BEAR** | Low H1 84019 alcanzado |
| Fakeout PDH | SÍ — NO LONG | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 84564 | Bull si cierre arriba |
| PDL | 82776 | Bear si cierre abajo |
| 0.5 midpoint | 83670 | Filtro 50% |

**Nota CRT:** Fakeout PDH: NO long E1; CRT invalid bearish

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ❌ | Sin dirección |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ❌ | sin SL/TP |
| RSI no contradice | ✅ | RSI no disponible |
| Rango coherente | ✅ | Sin dirección activa |

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

- Fakeout PDH — NO long E1; CRT invalid bearish
- Bias H1 NEUTRAL — no forzar dirección

### Galería (cross-ref)

- Patrón perdedor similar: fakeout (BTC-22-05-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

## Resumen High

> Tabla única — señal High (Categories + plan + métricas).

| Sección | Detalle |
|---------|---------|
| Precio | **83672.0** |
| Veredicto | **No operar** (NONE) |
| Entrada óptima | **n/d** |
| ICT | sin ICT |
| Plan | n/d |
| E2 / Break | Sin reversión E2 — E1 primario |
| Métricas | Rules **50%** · Confluencia **NULA** — 20% · Rules 50%; 2M5 no listo; Setup auto sin dirección; H1 NEUTRAL; Vol bajo |
| Historial ref | **btc-032** · 2026-09-30 09:45 NY · Entry **84402.9** · **EVITAR** — lejos y sin 2M5 · (MÁS LEJOS) · precio→última 730.9 pts (0.866%) |
| Bando usado (lado asumido) | **AUTO** |
| Bando mercado (H1) | **NEUTRAL** |
| Chart | **Preview en navegador** |

---


---

## Entrada optimizada (E1)

> Bias **AUTO** + **AUTO** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **83672.0** | Retest **n/d** |
| 2M5 NONE | No | n/d |
| Zona (info) | n/d de ref | contexto entry @ 0.0 |
| Acción | **ESPERAR** | **ESPERAR** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Definir bias y zona S/R |
| Confirmación | 2 velas M5 en dirección (zona = contexto entry, no gate) |
| Entry / SL / TP | Definir zona S/R válida primero |

---

## Ilustración entrada (2M5 + óptima)

Chart: **Preview en navegador**

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| — | Sin dirección | Forzar bias (-Bullish/-Bearish) o esperar H1 |

---

## Checklist 2M5

_Reloj (info): NY AM 10-11_

- [❌] 2 velas M5 confirman
- [❌] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes
- [✅] Estructura/CRT sin contradicción dura

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **SHORT**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (2135/479) | **SHORT** |
| CRT PD / Premium-Discount | NEUTRAL · PREMIUM | **SHORT** |
| Estructura swings M5 | HL 83768->84019 · LH 85650->85563 | **NEUTRAL** |

---


## Indicadores Legacy Pro (proxy)

| CRT | COMPLETED_BEAR/NEUTRAL | Núcleo |
| RSI TORYS | NONE | Sin divergencia M5 clara |
| DMI | BEAR | -DI domina (2135/479) |
| Swings | HL 83768->84019 | LH 85650->85563 |

---

## M5 detalle

- RSI M5/H1: 18.3 / 52.1
- Zona: soporte_debil @ 83696
- 2M5 LONG: NO | SHORT: SÍ

### 12 velas M5

- `13:35 O=85230.0 H=85230.0 L=84200.0 C=84234.7 [R]`
- `13:40 O=84234.7 H=84588.2 L=84019.4 C=84515.4 [G]`
- `13:45 O=84515.5 H=84677.5 L=84400.0 C=84615.7 [G]`
- `13:50 O=84615.7 H=84757.1 L=84522.1 C=84581.8 [R]`
- `13:55 O=84581.8 H=84670.0 L=84476.8 C=84637.7 [G]`
- `14:00 O=84637.7 H=84644.8 L=84286.1 C=84553.5 [R]`
- `14:05 O=84552.0 H=84637.7 L=84275.4 C=84394.0 [R]`
- `14:10 O=84394.0 H=84519.2 L=84138.6 C=84354.0 [R]`
- `14:15 O=84354.0 H=84358.0 L=84009.0 C=84130.9 [R]`
- `14:20 O=84130.9 H=84178.0 L=83647.3 C=83886.5 [R]`
- `14:25 O=83886.5 H=83999.4 L=83656.1 C=83768.4 [R]`
- `14:30 O=83768.4 H=83832.0 L=83672.0 C=83672.0 [R]`

---

## Score reglas extendidas (66%)

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | NO | Sin dirección |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | NO | sin SL/TP |
| RSI no contradice | SÍ | RSI n/a |
| Rango coherente | SÍ | sin dirección activa |
| DMI alineado | SÍ | -DI domina (2135/479) |
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
- **Chart:** **Preview en navegador**


---
*high signal | 2026-09-30 14:32 UTC*
