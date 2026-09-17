# ML + Neural integration — v_ops_apr_sep

> Generado: 2026-09-17 17:52 UTC
> Elapsed: 519.9s

Operaciones reales del celular enriquecen el dataset sintético (peso `ops_weight`) y generan etiquetas WIN/LOSS para visión.

## BTCUSDT

| Métrica | Before | After | Δ |
|---------|--------|-------|---|
| Accuracy | 0.5083 | 0.5639 | +0.0556 |
| Precision | 0.4667 | 0.5484 | +0.0817 |
| Recall | 0.375 | 0.5312 | +0.1562 |
| F1 | 0.4158 | 0.5397 | +0.1239 |

- Baseline samples: **479**
- Ops candidates / matched / feature rows: **63** / **53** / **53**
- Match summary: `{"n": 53, "wins": 33, "losses": 20, "winrate": 0.6226, "by_label_source": {"real_sl_tp": 36, "fixed_rr": 17}, "mean_price_error_pct": 0.0263}`
- Model: `D:\Danilo\Trading\Cursor Trading\models\btc_signal_model.joblib`

## US30

| Métrica | Before | After | Δ |
|---------|--------|-------|---|
| Accuracy | 0.625 | 0.625 | +0.0000 |
| Precision | 0.5 | 0.5 | +0.0000 |
| Recall | 0.3333 | 0.3333 | +0.0000 |
| F1 | 0.4 | 0.4 | +0.0000 |

- Baseline samples: **31**
- Ops candidates / matched / feature rows: **2** / **0** / **0**
- Match summary: `{"n": 0, "winrate": null}`
- Model: `D:\Danilo\Trading\Cursor Trading\models\us30_signal_model.joblib`

## Neural / visión

```json
{
  "labels_dst": "D:\\Danilo\\Trading\\Cursor Trading\\app\\services\\learning\\training neuronal\\data\\mobile_ops_labels.csv",
  "trained": true,
  "metrics": {
    "accuracy": 0.8,
    "precision": 1.0,
    "recall": 0.3333,
    "f1": 0.5,
    "n": 40,
    "val_n": 10
  },
  "model": "D:\\Danilo\\Trading\\Cursor Trading\\app\\services\\learning\\training neuronal\\models\\mobile_ops_vision_simple.joblib",
  "mode": "mobile_simple"
}
```

## Archivos

- `D:\Danilo\Trading\Cursor Trading\data\ops_mobile\v_ops_apr_sep\btc_ops_matched.csv`
- `D:\Danilo\Trading\Cursor Trading\data\ops_mobile\v_ops_apr_sep\us30_ops_matched.csv`
- `D:\Danilo\Trading\Cursor Trading\data\ops_mobile\v_ops_apr_sep\mobile_vision_labels.csv`
- `D:\Danilo\Trading\Cursor Trading\data\ops_mobile\v_ops_apr_sep\ml_ops_integration_report.md`

## Notas

- Modelos previos respaldados como `*.joblib.bak_pre_ops`.
- No se inventaron trades: solo OCR + velas históricas.
- US30 M5 vía yfinance suele cubrir ~60 días → pocas matches esperables.
