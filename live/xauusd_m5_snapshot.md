# XAUUSD M5 Snapshot

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
| H1 state | **INSIDE_RANGE** | Rango H1 4293-4313; 0.5=4303 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4408 | Bull si cierre arriba |
| PDL | 4311 | Bear si cierre abajo |
| 0.5 midpoint | 4359 | Filtro 50% |

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


### Disclaimer datos oro

- Proxy mercado: **yfinance (GC=F, M5=5m)** (no es cota Exness/spot exacta).
- Ops OCR XAUUSD en v_ops_apr_sep son **pocas**; ML es mayormente sintético E1.
- No auto-ejecutar. Validar con broker.
- Fetch notes: `GC=F 5m: Yahoo API OK (13600 velas); GC=F 1h: Yahoo API OK (13736 velas)`