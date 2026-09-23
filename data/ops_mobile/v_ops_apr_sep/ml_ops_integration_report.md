# ML + Neural integration — v_ops_apr_sep

> Generado: 2026-09-23 15:46 UTC
> Elapsed: 46.2s

Operaciones reales del celular enriquecen el dataset sintético (peso `ops_weight`) y generan etiquetas WIN/LOSS para visión.

## XAUUSD

| Métrica | Before | After | Δ |
|---------|--------|-------|---|
| Accuracy | 0.7119 | 0.7119 | +0.0000 |
| Precision | 0.6154 | 0.6154 | +0.0000 |
| Recall | 0.4 | 0.4 | +0.0000 |
| F1 | 0.4848 | 0.4848 | +0.0000 |

- Baseline samples: **233**
- Ops candidates / matched / feature rows: **2** / **0** / **0**
- Match summary: `{"n": 0, "winrate": null}`
- Model: `D:\Danilo\Trading\Cursor Trading\models\xauusd_signal_model.joblib`

- H1 diagnostic labels (fuera de M5 lookback): **2** / 2 ops
  `[{"trade_id": "039ed97651840a49", "source_image": "IMG-20260513-WA0001.jpg", "status": "labeled", "label": 0, "label_source": "real_sl_tp", "side": "long", "entry": 4692.03, "bar_time": "2026-05-14T15:00:00+00:00", "price_at_bar": 4691.89990234375, "price_error_pct": 0.0028, "ts": "2026-05-13T16:00:00+00:00"}, {"trade_id": "62745f1db947c362", "source_image": "IMG-20260702-WA0001.jpg", "status": "labeled", "label": 0, "label_source": "real_sl_tp", "side": "long", "entry": 4024.04, "bar_time": "20`

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
- `D:\Danilo\Trading\Cursor Trading\data\ops_mobile\v_ops_apr_sep\xauusd_ops_matched.csv`
- `D:\Danilo\Trading\Cursor Trading\data\ops_mobile\v_ops_apr_sep\xauusd_ops_h1_labels.csv`
- `D:\Danilo\Trading\Cursor Trading\data\ops_mobile\v_ops_apr_sep\mobile_vision_labels.csv`
- `D:\Danilo\Trading\Cursor Trading\data\ops_mobile\v_ops_apr_sep\ml_ops_integration_report.md`

## Notas

- Modelos previos respaldados como `*.joblib.bak_pre_ops`.
- No se inventaron trades: solo OCR + velas históricas.
- US30/XAUUSD M5 vía yfinance suele cubrir ~60–70 días → pocas matches si OCR es más viejo.
- XAUUSD usa proxy **GC=F**; etiquetas H1 son diagnósticas cuando M5 no cubre la fecha.
