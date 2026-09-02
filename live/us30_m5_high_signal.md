# US30 M5 High Signal — CRT + Turtle Soup (Deep Analysis)

> 2026-09-02 15:39 UTC | NY 2026-09-02 11:39 | FUERA_NY
> Precio **53129.00** | HIGH mode | PF E1=4.77 | E2 max 10%
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
**Tendencia:** Bajista
**Reglas:** **6 de 8** (75%) | Extendidas: **83%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~82%** — patrón ganador similar · histórico E1 BTC

## Categories

| Campo | Valor |
|-------|-------|
| Bando usado | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| Recomendación | **NO_OPERAR — fin sesión (SHORT)** |
| Segunda indicación | **SHORT** (H1 NEUTRAL — ver sección abajo) |
| Neural galería | **53% WIN** — grade **B** (baja similitud con galería WIN; conf. low) |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **NEUTRAL** | No forzar; esperar pending CRT HTF | Modo BREAK: priorizar continuación E1 CRT |
| Premium/Discount | PREMIUM | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 53111-53249; 0.5=53180 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 53343 | Bull si cierre arriba |
| PDL | 52747 | Bear si cierre abajo |
| 0.5 midpoint | 53045 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Sesión NY | ❌ | FUERA_NY |
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.036% |
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
- Fuera de ventana NY (regla 2)
- Sin 2 velas M5 — ESPERAR (regla dura)

### Galería (cross-ref)

- Patrón ganador similar: Rechazo resistencia (BTC-02-07-26)
- Cruzar con `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1


---

## Entrada optimizada (E1)

> Bias **BEARISH** + **BREAK (E1)** · CRT PD **NEUTRAL** · Premium/Discount **PREMIUM**

### AHORA vs ENTRADA OPTIMIZADA

| | **AHORA** | **ENTRADA OPTIMIZADA** |
|---|-----------|-------------------------|
| Precio | **53129.0** | Retest **53030.3–53110.0** |
| 2M5 SHORT | No | Nuevas 2 rojas en zona tras retest (no las actuales lejos) |
| Cerca zona | ✅ (0.04%) | ✅ ≤0.15% de 53110.0 |
| Acción | **ESPERAR SHORT** | **ENTRAR SHORT** |

### Plan concreto

| Campo | Valor |
|-------|-------|
| Trigger | Retest 53030.3–53110.0 (resistencia_debil @ 53110.0) + 2 velas M5 rojas consecutivas en zona |
| Confirmación | 2 velas M5 rojas consecutivas con cierres en zona ≤0.15% |
| Entry | **53082.1** (limit retest o market al cierre 2ª vela) |
| SL | **53216.2** (estructural) · SL cuenta ~$9 (ajustar lotaje) |
| TP 1:2 | **52813.9** |
| R:R | **1:2** · riesgo **134.1** pts |
| Invalidación | Cierre M5 > 53216.2 o breakout > 53110.0 sin rechazo |
| Plan B | Light re-scan ~30 min: si precio no retestea zona → skip trade AM; reservar PM solo si AM=ESPERAR y <2 SL |

---

## Ilustración entrada (2M5 + óptima)

![annotated](us30_m5_chart_annotated.png)

---

## 2M5 — Válido vs Inválido

| Patrón | Estado | Nota |
|--------|--------|------|
| ✅ SHORT OK: [R][R] en resistencia_debil @ 53110.0 | Referencia — requiere 2 rojas **nuevas** en retest | Patrón válido SHORT en resistencia |
| ❌ NO: [G][R] | **INVÁLIDO** | 1ª vela verde invalida secuencia SHORT |
| ❌ NO: [R][R] … [G][G] | **INVÁLIDO** | 2M5 válidas deben ser las **últimas 2** velas (no anteriores) |

---

## Checklist 2M5

- [❌] Sesión NY activa
- [✅] Cerca de zona (resistencia_debil @ 53110)
- [❌] 2 velas M5 confirman SHORT
- [✅] Bias H1 alineado o bias CLI forzado
- [✅] RSI M5 + CRT premium/discount coherentes

**Falta al menos 1 ítem → ESPERAR.**

---

## Segunda indicación (H1 NEUTRAL)

> Cuando el **bando mercado (H1) es NEUTRAL**, la **segunda indicación** aporta un sesgo operativo auxiliar desde DMI (momentum M5), lectura CRT premium/discount y estructura de swings. **No sustituye** el bias H1 — orienta mientras H1 no define dirección clara. Usar con `-Bullish`/`-Bearish` solo tras confirmar en TV.

**Sesgo sugerido (votos auxiliares):** **SHORT**

| Fuente | Lectura | Sesgo sugerido |
|--------|---------|----------------|
| DMI (momentum M5) | -DI domina (166/104) | **SHORT** |
| CRT PD / Premium-Discount | NEUTRAL · PREMIUM | **SHORT** |
| Estructura swings M5 | HL 52720->52907 · HH 53110->53283 | **LONG** |

---


## Indicadores Legacy Pro (proxy)

| CRT | INSIDE_RANGE/NEUTRAL | Núcleo |
| RSI TORYS | BEARISH | Fondo rojo TORYS-proxy - filtro short |
| DMI | BEAR | -DI domina (166/104) |
| Swings | HL 52720->52907 | HH 53110->53283 |

---

## M5 detalle

- RSI M5/H1: 38.5 / 65.5
- Zona: resistencia_debil @ 53110
- 2M5 LONG: NO | SHORT: NO

### 12 velas M5

- `14:35 O=53195.0 H=53254.0 L=53191.0 C=53252.0 [G]`
- `14:40 O=53251.0 H=53283.0 L=53244.0 C=53276.0 [G]`
- `14:45 O=53274.0 H=53278.0 L=53252.0 C=53264.0 [R]`
- `14:50 O=53263.0 H=53263.0 L=53237.0 C=53257.0 [R]`
- `14:55 O=53253.0 H=53261.0 L=53230.0 C=53238.0 [R]`
- `15:00 O=53237.0 H=53249.0 L=53193.0 C=53194.0 [R]`
- `15:05 O=53193.0 H=53207.0 L=53157.0 C=53162.0 [R]`
- `15:10 O=53162.0 H=53193.0 L=53141.0 C=53160.0 [R]`
- `15:15 O=53158.0 H=53166.0 L=53138.0 C=53155.0 [R]`
- `15:20 O=53156.0 H=53161.0 L=53124.0 C=53124.0 [R]`
- `15:25 O=53123.0 H=53148.0 L=53111.0 C=53139.0 [G]`
- `15:29 O=53129.0 H=53129.0 L=53129.0 C=53129.0 [G]`

---

## Score reglas extendidas (83%)

| Regla | OK | Nota |
|-------|----|------|
| Sesión NY | NO | FUERA_NY |
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.036% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | Fondo rojo TORYS-proxy - filtro short |
| Rango coherente | SÍ | No forzar; esperar pending CRT HTF | Mod |
| DMI alineado | SÍ | -DI domina (166/104) |
| 0.5 midpoint E1 | SÍ | premium OK |
| 2 SL / 3 ops hoy | SÍ | Confirmar trader |
| SL ~$9 cuenta | SÍ | Ajustar lotaje |

---

## Cursor HIGH response
1. Usar **Veredicto** + tablas CRT/E1/E2 arriba.
2. Leer **Entrada optimizada (E1)** + **Checklist 2M5** + **2M5 Válido/Inválido**.
3. Citar CRT pending/completed/invalid + RSI TORYS.
4. Galería WIN match. 5. E2 solo watch. 6. Confirmar TV.


---
*high signal | 2026-09-02 15:39 UTC*
