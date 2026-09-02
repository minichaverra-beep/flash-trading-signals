# BTC M5 Live Snapshot — E1 Analysis Feed

> Generado: **2026-09-01 22:03** UTC  ·  NY local: **2026-09-01 18:03**  ·  Ventana: **FUERA_NY**
> Símbolo: `BTCUSDT`  ·  Fuente: Binance public klines

---

## Veredicto: NO_OPERAR

**E1/E2:** E1 primario
**Tendencia:** Sin dirección
**Reglas:** **5 de 8** (62%) | Extendidas: **66%**
**Calidad:** Setup débil
**Probabilidad histórica:** **~67%** — probabilidad histórica (~67%)

## Categories

| Campo | Valor |
|-------|-------|
| Bando usado | **BULLISH** |
| Bando mercado (H1) | **BEARISH** |
| Recomendación | **NO_OPERAR — fin sesión (LONG)** |
| ML prob. win | **17.3%** — grade **C** (confianza high) |
| Neural galería | **78% WIN** — grade **B** (alineado con patrones WIN desktop; conf. medium) |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 76920-77516; 0.5=77218 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 79250 | Bull si cierre arriba |
| PDL | 77392 | Bear si cierre abajo |
| 0.5 midpoint | 78321 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Sesión NY | ❌ | FUERA_NY |
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Alcista |
| Cerca de zona clave | ✅ | a 0.023% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ✅ | RSI 44 OK |
| Rango coherente | ❌ | rango bajista |

### Red flags

- Fuera ventana NY — NO_OPERAR
- Precio < PDL — no long contra rango bajista CRT
- Fuera de ventana NY (regla 2)
- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)

---

## Detalle mercado

| Campo | Valor |
|-------|-------|
| Precio spot (último close M5) | **77286.01** |
| Sesión NY | ❌ FUERA — FUERA_NY |
| Bias H1 (EMA20/50) | **BEARISH** |
| RSI M5 (14) | 43.7 |
| RSI H1 (14) | 35.7 |
| PDH (aprox. día UTC anterior) | 79250.00 |
| PDL (aprox. día UTC anterior) | 77392.00 |

### Swings M5 (proxy zonas débiles)

- Swing highs: 77466.6, 77469.9, 77471.9, 77516.3, 77268.0
- Swing lows: 77318.0, 77416.8, 76420.0, 77200.0, 76920.4
- Zona más cercana: **resistencia_debil** @ 77268.0 (0.023%)

### Últimas 6 velas M5

- `21:35 O=77045.6 H=77166.0 L=77045.6 C=77166.0 [G]`
- `21:40 O=77166.0 H=77225.7 L=77135.0 C=77146.1 [R]`
- `21:45 O=77146.1 H=77183.6 L=77135.0 C=77171.5 [G]`
- `21:50 O=77171.5 H=77272.7 L=77163.1 C=77235.1 [G]`
- `21:55 O=77235.1 H=77271.6 L=77211.3 C=77211.3 [R]`
- `22:00 O=77211.3 H=77312.0 L=77188.0 C=77286.0 [G]`

- Confirmación 2 verdes (LONG): ❌
- Confirmación 2 rojas (SHORT): ❌



---
*Script `analyze_btc_m5.py` · Datos Binance · 2026-09-01 22:03 UTC*
