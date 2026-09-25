# US30 M5 Live Snapshot — E1 Analysis Feed

> Generado: **2026-09-24 18:09** UTC  ·  NY local: **2026-09-24 14:09**  ·  Ventana: **NY PM 14-16**
> Símbolo: `US30`  ·  Fuente: yfinance (YM=F, M5=5m)

> **SL referencia ~$9:** ~9 pts ($1/pt) · ~90 pts ($0.10/pt micro)

---

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **3 de 6** (50%) | Extendidas: **66%**
**Calidad:** No operar
**Probabilidad histórica:** **~67%** — probabilidad histórica (~67%)

## Categories

| Campo | Valor |
|-------|-------|
| Bando usado | **AUTO** |
| Bando mercado (H1) | **NEUTRAL** |
| Recomendación | **ESPERAR (sin dirección)** |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 51630-51788; 0.5=51709 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 52371 | Bull si cierre arriba |
| PDL | 51830 | Bear si cierre abajo |
| 0.5 midpoint | 52100 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ❌ | Sin dirección |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ❌ | sin SL/TP |
| RSI no contradice | ✅ | RSI no disponible |
| Rango coherente | ✅ | Sin dirección activa |

### Red flags

- Bias H1 NEUTRAL — no forzar dirección

---

## Detalle mercado

| Campo | Valor |
|-------|-------|
| Precio spot (último close M5) | **51698.0** |
| Reloj (info) | NY PM 14-16 — NY 2026-09-24 14:09 |
| Bias H1 (EMA20/50) | **NEUTRAL** |
| RSI M5 (14) | 36.4 |
| RSI H1 (14) | 42.8 |
| PDH (aprox. día UTC anterior) | 52371.0 |
| PDL (aprox. día UTC anterior) | 51830.0 |

### Swings M5 (proxy zonas débiles)

- Swing highs: 51861.0, 51805.0, 51735.0, 51858.0, 51832.0
- Swing lows: 51670.0, 51594.0, 51479.0, 51486.0, 51630.0
- Zona más cercana: **soporte_debil** @ 51670.0 (0.054%)

### Últimas 6 velas M5

- `17:35 O=51671.0 H=51675.0 L=51640.0 C=51655.0 [R]`
- `17:40 O=51653.0 H=51679.0 L=51630.0 C=51643.0 [R]`
- `17:45 O=51641.0 H=51677.0 L=51631.0 C=51669.0 [G]`
- `17:50 O=51663.0 H=51685.0 L=51660.0 C=51678.0 [G]`
- `17:55 O=51675.0 H=51709.0 L=51672.0 C=51698.0 [G]`
- `17:58 O=51698.0 H=51698.0 L=51698.0 C=51698.0 [G]`

### Notas fuente datos

- YM=F 5m: Yahoo API OK (13597 velas)
- YM=F 1h: Yahoo API OK (13693 velas)

- Confirmación 2 verdes (LONG): ❌
- Confirmación 2 rojas (SHORT): ❌



---
*Script `analyze_us30_m5.py` · yfinance (YM=F, M5=5m) · 2026-09-24 18:09 UTC*
