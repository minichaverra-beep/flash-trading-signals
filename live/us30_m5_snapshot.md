# US30 M5 Live Snapshot — E1 Analysis Feed

> Generado: **2026-09-01 21:17** UTC  ·  NY local: **2026-09-01 17:17**  ·  Ventana: **FUERA_NY**
> Símbolo: `US30`  ·  Fuente: yfinance (YM=F, M5=5m)

> **SL referencia ~$9:** ~9 pts ($1/pt) · ~90 pts ($0.10/pt micro)

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **6 de 8** (75%) | Extendidas: **66%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~82%** — histórico E1 BTC (75% reglas OK)

## Categories

| Campo | Valor |
|-------|-------|
| Bando usado | **BEARISH** |
| Bando mercado (H1) | **NEUTRAL** |
| Recomendación | **NO_OPERAR — fin sesión (SHORT)** |
| ML prob. win | **62.6%** — grade **B** (confianza medium) |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 52798-52855; 0.5=52826 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 53547 | Bull si cierre arriba |
| PDL | 53149 | Bear si cierre abajo |
| 0.5 midpoint | 53348 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Sesión NY | ❌ | FUERA_NY |
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.011% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 68 OK |
| Rango coherente | ✅ | Shorts E1 rechazo resistencia (premium) |

### Red flags

- Fuera ventana NY — NO_OPERAR
- Fuera de ventana NY (regla 2)
- Sin 2 velas M5 — ESPERAR (regla dura)

---

## Detalle mercado

| Campo | Valor |
|-------|-------|
| Precio spot (último close M5) | **52847.0** |
| Sesión NY | ❌ FUERA — FUERA_NY |
| Bias H1 (EMA20/50) | **NEUTRAL** |
| RSI M5 (14) | 68.3 |
| RSI H1 (14) | 27.8 |
| PDH (aprox. día UTC anterior) | 53547.0 |
| PDL (aprox. día UTC anterior) | 53149.0 |

### Swings M5 (proxy zonas débiles)

- Swing highs: 52855.0, 52864.0, 52863.0, 52855.0, 52841.0
- Swing lows: 52796.0, 52763.0, 52803.0, 52747.0, 52774.0
- Zona más cercana: **resistencia_debil** @ 52841.0 (0.011%)

### Últimas 6 velas M5

- `20:35 O=52830.0 H=52834.0 L=52829.0 C=52832.0 [G]`
- `20:40 O=52832.0 H=52850.0 L=52831.0 C=52840.0 [G]`
- `20:45 O=52838.0 H=52842.0 L=52833.0 C=52838.0 [G]`
- `20:50 O=52839.0 H=52850.0 L=52839.0 C=52850.0 [G]`
- `20:55 O=52848.0 H=52852.0 L=52840.0 C=52846.0 [R]`
- `21:00 O=52847.0 H=52847.0 L=52847.0 C=52847.0 [G]`

### Notas fuente datos

- YM=F 5m: Yahoo API OK (13773 velas)
- YM=F 1h: Yahoo API OK (13701 velas)

- Confirmación 2 verdes (LONG): ❌
- Confirmación 2 rojas (SHORT): ❌



---
*Script `analyze_us30_m5.py` · yfinance (YM=F, M5=5m) · 2026-09-01 21:17 UTC*
