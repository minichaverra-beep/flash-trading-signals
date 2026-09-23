# XAUUSD M5 Snapshot

## Veredicto: ESPERAR

**E1/E2:** E1 primario
**Tendencia:** Bajista
**Reglas:** **5 de 7** (71%) | Extendidas: **72%**
**Calidad:** Setup medio
**Probabilidad histórica:** **~69%** — histórico E1 BTC (71% reglas OK)

## Categories

| Campo | Valor |
|-------|-------|
| Bando usado | **AUTO** |
| Bando mercado (H1) | **BEARISH** |
| Recomendación | **ESPERAR SHORT** |
| ML prob. win | **10.4%** — grade **C** (confianza high) |

### CRT

| Item | Valor | Acción E1 |
|------|-------|-----------|
| PD reading | **BEARISH** | Shorts E1 rechazo resistencia (premium) |
| Premium/Discount | DISCOUNT | Long discount / Short premium |
| H1 state | **INSIDE_RANGE** | Rango H1 4317-4334; 0.5=4325 |
| Fakeout PDH | NO | CRT invalid bear |
| Fakeout PDL | NO | Turtle soup ctx |
| PDH | 4414 | Bull si cierre arriba |
| PDL | 4328 | Bear si cierre abajo |
| 0.5 midpoint | 4371 | Filtro 50% |

### Checklist E1

| Regla | OK | Nota |
|-------|----|------|
| Solo E1 | ✅ | Operar solo E1 |
| Tendencia H1 alineada | ✅ | Bajista |
| Cerca de zona clave | ✅ | a 0.056% |
| 2 velas M5 confirman | ❌ | Falta confirmación |
| R:R mínimo 1:2 | ✅ | 1:2 |
| RSI no contradice | ❌ | Fondo verde TORYS-proxy - filtro long |
| Rango coherente | ✅ | Shorts E1 rechazo resistencia (premium) |

### Red flags

- Sin 2 velas M5 de confirmación
- Sin 2 velas M5 — ESPERAR (regla dura)
- RSI TORYS en contra: Fondo verde TORYS-proxy - filtro long


### Disclaimer datos oro

- Proxy mercado: **yfinance (GC=F, M5=5m)** (no es cota Exness/spot exacta).
- Ops OCR XAUUSD en v_ops_apr_sep son **pocas**; ML es mayormente sintético E1.
- No auto-ejecutar. Validar con broker.
- Fetch notes: `GC=F 5m: Yahoo API OK (13571 velas); GC=F 1h: Yahoo API OK (13733 velas)`