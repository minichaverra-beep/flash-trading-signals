# BTC Super High Signal — Probabilidad de éxito (captura usuario)

> 2026-09-01 22:04 UTC | Tier **Super High** | Captura: `super_high_entry.png`
> Pipeline: Neural 50% · ML 30% · Rules 20% (renormalizado si falta fuente)

---

## Resumen ejecutivo

| Campo | Valor |
|-------|-------|
| **PROBABILIDAD ÉXITO** | **67%** |
| **GRADO** | **B** |
| **NEURAL** | 78% similar WIN galería |
| **ML** | 42% |
| **RULES** | 6/8 (75%) |
| **VEREDICTO** | **ESPERAR** |
| **Bando usado** | **BULLISH** |
| **Bando mercado (H1)** | **BEARISH** |
| **Recomendación** | **NO_OPERAR — fin sesión (LONG)** |
| **RAZÓN CLAVE** | Neural 78% similitud WIN galería · ML 42% calidad señal · Reglas E1 6/8 (75%) · Dirección manual: LONG |
| **INVALIDACIÓN** | Reglas fallidas: Sesión NY, 2 velas M5 confirman · ML <45% — sesgo histórico contra entrada · Invalidación técnica: cierre M5 más allá de SL 77662.67 |

---

## Captura analizada

![Captura entrada](super_high_entry.png)

### Notas manuales (`super_high_entry.md`)

- Entrada: 77928.16
- SL: 77662.67
- TP: 78433.59
- Dirección: LONG

## Neural galería (50% peso)

- Prob WIN: **78.4%** | Prob LOSS: 21.6%
- Grado neural: B | Confianza: medium
- Etiqueta predicha: WIN
- Alineado galería WIN: SÍ

## ML tabular (30% peso)

- Prob win: **41.9%** | Grado: C
- Confianza: low | Features: 37

## Reglas E1 live (20% peso)

- Precio live: **77248.99** | Bias H1: BEARISH
- Sesión: FUERA_NY | Setup auto: SHORT
- CRT: INSIDE_RANGE | 

| Regla | OK | Nota |
|-------|----|------|
| Sesión NY | NO | FUERA_NY |
| Solo E1 | SÍ | Operar solo E1 |
| Tendencia H1 alineada | SÍ | Bajista |
| Cerca de zona clave | SÍ | a 0.025% |
| 2 velas M5 confirman | NO | Falta confirmación |
| R:R mínimo 1:2 | SÍ | 1:2 |
| RSI no contradice | SÍ | RSI 41 OK |
| Rango coherente | SÍ | Shorts E1 rechazo resistencia (premium) |

## OCR (opcional)

- Disponible: NO
- Nota: pytesseract/PIL no instalados — omitido

## Heurísticas visuales

- Bias hint: BEARISH
- Verde/rojo: 0.0054 / 0.0276
- Líneas horizontales proxy: 49
- Score visual: 0.7445

---

## Cursor Super High response

Usar formato del protocolo `TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md`:

```
PROBABILIDAD ÉXITO: 67%
GRADO: B
NEURAL: 78% similar WIN galería
ML: 42%
RULES: 6/8 (75%)
VEREDICTO: ESPERAR
BANDO USADO: BULLISH
RECOMENDACIÓN: NO_OPERAR — fin sesión (LONG)
RAZÓN CLAVE: Neural 78% similitud WIN galería · ML 42% calidad señal · Reglas E1 6/8 (75%) · Dirección manual: LONG
INVALIDACIÓN: Reglas fallidas: Sesión NY, 2 velas M5 confirman · ML <45% — sesgo histórico contra entrada · Invalidación técnica: cierre M5 más allá de SL 77662.67
```

---
*Super High signal | 2026-09-01 22:04 UTC*
