# XAUUSD — inventario OCR + visión (v_ops_apr_sep)

> Generado: 2026-09-23 15:46 UTC

## Inventario

| Fuente | Count |
|--------|------:|
| trades.csv XAUUSD | 4 |
| trades_raw (pre-dedupe) | 5 |
| Usables ML (side+entry, conf≥0.45) | 2 |
| Matched M5 (features) | 0 |
| Labeled H1 (diagnóstico) | 2 |

- Sides: `{"long": 2, "missing": 2}`
- Outcomes OCR: `{"open": 3, "unknown": 1}`
- Rango por nombre de archivo (WhatsApp): **2026-05-13 → 2026-07-02**
- Otras fuentes oro en repo: **ninguna** (solo v_ops_apr_sep + proxy GC=F).

## Screenshots móviles etiquetados XAUUSD

- `IMG-20260513-WA0001.jpg` exists=True conf=0.803 side=long entry=4692.03 ts≈2026-05-13T16:00:00+00:00
- `IMG-20260515-WA0003.jpg` exists=True conf=0.35 side=nan entry=nan ts≈2026-05-15T16:00:00+00:00
- `IMG-20260518-WA0000.jpg` exists=True conf=0.35 side=nan entry=nan ts≈2026-05-18T16:00:00+00:00
- `IMG-20260526-WA0003.jpg` exists=True conf=0.782 side=nan entry=4543.28 ts≈2026-05-26T16:00:00+00:00
- `IMG-20260702-WA0001.jpg` exists=True conf=0.817 side=long entry=4024.04 ts≈2026-07-02T16:00:00+00:00

## Neural / visión

Las capturas XAUUSD son charts TradingView/Exness (WhatsApp). Con n≈4–5 imágenes no hay masa crítica para un modelo vision dedicado de oro.

- Se reutiliza el pipeline `mobile_ops_vision_simple` / labels H1 cuando hay WIN/LOSS resoluble.
- Recomendación: acumular ≥30 ops XAUUSD cerradas (side+entry+SL/TP+timestamp) antes de esperar uplift ML/neural significativo.

## Limitaciones (honestas)

1. Yahoo M5 (GC=F) no cubre mayo–principios julio → match M5≈0 esperado.
2. OCR sin `capture_ts`; se usa fecha del filename IMG-YYYYMMDD.
3. Outcomes OCR=`open` (posiciones abiertas en screenshot) — no son W/L de cuenta.
4. Proxy GC=F ≠ cota exacta del broker.
