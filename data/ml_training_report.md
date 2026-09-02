# ML Training Report — BTC M5 E1 Signals

> Generado: 2026-09-01 14:58 UTC

## Configuración

| Parámetro | Valor |
|-----------|-------|
| Días históricos | 365 |
| Horizonte label (velas M5) | 48 (4.0 h) |
| Algoritmo | gb |
| SL referencia | $9.0 @ BTC ~$78,000 → **0.0115%** precio |
| TP objetivo | 1:2 R:R |
| Muestras totales | 876 |
| Win rate dataset | 39.2% |
| Tiempo entrenamiento | 157.2s |

## Métricas test (hold-out 25%)

- **Accuracy:** 0.6941
- **Precision:** 0.6234
- **Recall:** 0.5581
- **Win rate baseline test:** 39.3%

### Win rate por bucket de probabilidad predicha

| Bucket prob | N | Win rate real |
|-------------|---|---------------|
| 0%-45% | 133 | 24.8% |
| 45%-55% | 23 | 60.9% |
| 55%-65% | 19 | 21.1% |
| 65%-75% | 20 | 75.0% |
| 75%-101% | 24 | 83.3% |

### Classification report

```
precision    recall  f1-score   support

           0       0.73      0.78      0.76       133
           1       0.62      0.56      0.59        86

    accuracy                           0.69       219
   macro avg       0.68      0.67      0.67       219
weighted avg       0.69      0.69      0.69       219
```

## Notas

- El modelo **complementa** las 8 reglas E1; no reemplaza validación TradingView.
- Re-entrenar semanalmente o tras cambios en el plan E1.
- SL dinámico: `9 / precio_entrada` cuando no hay SL estructural.
