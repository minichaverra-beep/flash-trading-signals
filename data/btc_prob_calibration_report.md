# Calibración Probabilidad de éxito — BTC E1

> Generado: 2026-10-07 15:17 UTC · `python -m app.controllers.calibrate_signals --asset btc`

| Parámetro | Valor |
|-----------|-------|
| Periodo | 2026-03-24 → 2026-10-07 |
| Etiqueta | TP 1:2 antes que SL en 48 velas M5 |
| Señales con resultado | 2097 (n_eff sin solape 755) |
| Timeouts excluidos | 10 |
| Tasa base real | 46.1% |
| Riesgo SL mediano | 0.08675% del precio |
| Costo supuesto | 0.015% del precio por operación |
| ¿Ventaja fuera de muestra? | **SÍ** (Brier skill +1.6%) |

## Métricas fuera de muestra (walk-forward, purga 48 velas)

| Predictor | Brier | Log-loss | ECE |
|-----------|-------|----------|-----|
| Modelo calibrado | 0.24637 | 0.68588 | 0.02456 |
| Constante (tasa base) | 0.2503 | 0.69378 | 0.02752 |
| Heurística anterior | 0.27891 | 0.75446 | 0.17279 |

_Menor es mejor. La heurística anterior se mide sin acuerdo entre capas ni galería (no reproducibles en replay)._

## Coeficientes (log-odds)

| Variable | Coef | Media |
|----------|------|-------|
| RSI M5 vs dirección (`rsi_ext`) | -0.164 | 0.825 |
| Zona premium/discount (`pd_favor`) | +0.162 | -0.816 |
| 2 velas M5 confirman (`confirm_2m5`) | -0.034 | 0.284 |
| Rango CRT coherente (`crt_coherent`) | +0.101 | 0.918 |
| Intercepto | +0.027 | — |

## Curva de calibración — modelo

| Bucket | N | Predicho | Real |
|--------|---|----------|------|
| 0-35% | 58 | 32.6% | 41.4% |
| 35-40% | 296 | 38.1% | 39.2% |
| 40-45% | 563 | 42.7% | 44.6% |
| 45-50% | 457 | 47.4% | 50.3% |
| 50-55% | 222 | 52.0% | 54.9% |
| 55-60% | 63 | 56.9% | 58.7% |
| 60-65% | 16 | 61.8% | 56.2% |
| 65-70% | 1 | 65.2% | 100.0% |
| 70-75% | 2 | 71.6% | 100.0% |

## Curva de calibración — heurística anterior

| Bucket | N | Predicho | Real |
|--------|---|----------|------|
| 45-50% | 14 | 49.0% | 50.0% |
| 55-60% | 271 | 56.0% | 43.2% |
| 60-65% | 977 | 64.0% | 46.6% |
| 65-70% | 14 | 65.0% | 42.9% |
| 70-75% | 402 | 71.8% | 51.5% |

## Reglas — acierto real cuando cumple / no cumple

| Regla | Cumple | Acierto si cumple | Acierto si no |
|-------|--------|-------------------|---------------|
| 2 velas M5 confirman | 28.4% | 43.3% (n=596) | 47.2% (n=1501) |
| Rango CRT coherente | 91.8% | 46.2% (n=1925) | 45.4% (n=172) |

| Zona premium/discount | N | Acierto |
|---|---|---|
| a favor | 193 | 54.9% |
| en contra | 1904 | 45.2% |

| RSI M5 (LONG · SHORT) | N | Acierto |
|---|---|---|
| LONG <40 · SHORT 60+ | 210 | 55.2% |
| LONG 40–50 · SHORT 50–60 | 390 | 54.4% |
| LONG 50–60 · SHORT 40–50 | 528 | 44.9% |
| LONG 60–70 · SHORT 30–40 | 514 | 44.8% |
| LONG 70–80 · SHORT 20–30 | 326 | 39.3% |
| LONG 80+ · SHORT <20 | 129 | 34.1% |

## Capas ML / Neural

- **ml:** no entra — sin predicciones ML fuera de muestra registradas
- **neural:** no entra — galería sin histórico de predicciones con resultado
