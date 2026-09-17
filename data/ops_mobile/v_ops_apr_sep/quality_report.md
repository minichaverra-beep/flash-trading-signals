# Quality report — v_ops_apr_sep

> Generado: 2026-09-17 11:32
> Fuente: `D:\Danilo\Trading\Cursor Trading\assets\images\Operaciones del celular desde 1 abril hasta 17 septiembre`

## Resumen

| Métrica | Valor |
|---------|-------|
| Imágenes escaneadas | 102 |
| Trades tras dedupe | 100 |
| Duplicados removidos | 2 |
| Alta confianza (≥0.70) | 91 (91.0%) |
| Media (0.45–0.70) | 2 |
| Baja (<0.45) | 7 |
| Con entry | 93 |
| Con side | 78 |
| Con SL | 65 |
| Con TP | 90 |
| Problemáticas | 23 |

## Símbolos

- `BTCUSDT`: 91
- `XAUUSD`: 4
- `UNKNOWN`: 3
- `US30`: 2

## Plataformas

- `TradingView`: 72
- `Exness`: 18
- `WhatsApp`: 8
- `Other`: 2

## Sides

- `long`: 47
- `short`: 31
- `None`: 22

## Campos faltantes (aprox. por imagen origen)

- `entry_price`: 9
- `side`: 24
- `stop_loss`: 37
- `take_profit`: 12
- `quantity`: 102
- `pnl`: 102

## Notas

- Quantity / PnL / fees casi nunca aparecen en capturas de chart → quedan `null`.
- `entry_time` usa timestamp del nombre de archivo (`Screenshot_YYYYMMDD-HHMMSS`).
- `outcome=open` hasta cruzar con mercado histórico en etapa ML.
- No se borró data histórica; este dataset es versión nueva bajo `data/ops_mobile/`.

## Archivos

- `trades.parquet` / `trades.csv`
- `problematic_images.csv`
- `quality_report.md` (este archivo)

## Post-check régimen de precio

- Filas BTCUSDT_REVIEW (entry <56k en mes con BTC mediana >=65k): **11**
- Revisar manualmente: pueden ser otro instrumento, demo, o chart con escala distinta.
- El OCR refleja los números del chart; el conflicto es de **inferencia de símbolo**, no de lectura.

