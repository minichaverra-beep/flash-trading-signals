# ML Training — Señales BTC M5 E1

Protocolo para entrenar y usar el modelo que **complementa** (no reemplaza) las 8 reglas E1 y la validación en TradingView.

---

## Qué hace el ML

| Componente | Rol |
|------------|-----|
| `app.controllers.train_btc_signals` | Descarga ~1 año de velas, genera features + labels, entrena modelo |
| `btc_ml_signals.py` | Inferencia en vivo: `prob_win`, grade sugerido (A+/B/C), confianza |
| `--ml` en `app.controllers.analyze_btc_m5` | Añade fila **ML prob. win** en la sección Categories |

El modelo aprende de outcomes históricos: ¿el precio alcanzó TP 1:2 antes que SL dentro de N velas M5?

---

## Conversión SL ~$9

Referencia de cuenta E1:

- Riesgo fijo: **$9** por operación
- BTC referencia: **~$78,000**
- Movimiento en precio: `9 / 78000 ≈ 0.0115%` (~$9 en notional)

En entrenamiento:

- Si hay SL estructural del setup (swing), se usa ese nivel
- Si no, SL = `precio × (9 / precio_entrada)` → equivalente a $9 en ese momento

TP = entrada ± 2× riesgo (R:R 1:2).

Horizonte por defecto: **48 velas M5** (= 4 horas).

---

## Instalación

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
pip install -r requirements-ml.txt
```

---

## Comandos

### Entrenamiento completo (~1 año)

```powershell
python -m app.controllers.train_btc_signals
```

- Descarga M5 + H1 de Binance (API pública, sin keys)
- Cache en `data/btcusdt_m5.parquet` y `data/btcusdt_h1.parquet`
- Guarda modelo en `models/btc_signal_model.joblib`
- Reporte en `data/ml_training_report.md`

### Prueba rápida (30 días)

```powershell
python -m app.controllers.train_btc_signals --quick
```

### Opciones útiles

| Flag | Descripción |
|------|-------------|
| `--days 180` | Días de historial |
| `--horizon 48` | Velas M5 hacia adelante para el label |
| `--algorithm gb` | `gb` (default), `rf`, `lr` |
| `--force-download` | Ignorar cache y re-descargar |
| `--ny-only` | Entrenar solo barras en ventana NY |

### Análisis en vivo con ML

```powershell
python -m app.controllers.analyze_btc_m5 --mode all --ml
```

Si no hay modelo entrenado, el script sigue funcionando y muestra un WARN.

---

## Tiempo estimado

| Modo | Descarga | Feature + train | Total aprox. |
|------|----------|-------------------|--------------|
| `--quick` (30d) | ~15 s | ~30–60 s | **1–2 min** |
| 365 días | ~2–4 min | ~3–8 min | **5–12 min** |

La segunda ejecución usa cache local y suele tardar solo el entrenamiento.

---

## Interpretación de métricas

| Métrica | Qué significa |
|---------|---------------|
| **Accuracy** | % de aciertos win/loss en test hold-out 25% |
| **Precision** | De los predichos WIN, cuántos realmente ganaron |
| **Recall** | De los WIN reales, cuántos detectó el modelo |
| **Buckets prob** | Win rate real por rango de probabilidad predicha |

**Buckets esperados (ejemplo):**

| Bucket prob | N | Win rate real |
|-------------|---|---------------|
| 0%-45% | … | ~35% |
| 45%-55% | … | ~50% |
| 55%-65% | … | ~58% |
| 65%-75% | … | ~65% |
| 75%-100% | … | ~72% |

Si los buckets no se separan (todos ~50%), el modelo no aporta edge — revisar features o más datos.

---

## Calendario de re-entrenamiento

| Frecuencia | Cuándo |
|------------|--------|
| **Semanal** | Domingo noche o lunes pre-sesión NY |
| **Ad-hoc** | Tras cambiar reglas E1, SL, o ventanas NY |
| **Mensual mínimo** | Si no hay cambios en el plan |

Comando recomendado semanal:

```powershell
python -m app.controllers.train_btc_signals --force-download
```

---

## Relación con reglas E1 y TradingView

1. **Las 8 reglas E1 siguen siendo la base** — el ML no las sustituye
2. **ML ajusta confianza** — grade A+/B/C según prob. histórica aprendida
3. **TradingView sigue obligatorio** — confirmación visual antes de entrar
4. **Prob. histórica en Categories** (82%, 69%, etc.) viene de `TRADING_WINRATE_STATS.md`
5. **ML prob. win** es probabilidad del modelo sobre el setup actual

Flujo recomendado:

```
Reglas E1 ≥ 63% → ML prob ≥ 55% → Confirmar en TV → Entrar con SL $9
```

---

## Archivos generados (gitignored)

```
data/
  btcusdt_m5.parquet
  btcusdt_h1.parquet
  ml_training_report.md
models/
  btc_signal_model.joblib
  btc_signal_features.json
```

---

## Features (37)

Alineadas con el plan E1:

- Bias H1, RSI M5/H1, distancia a zona, PDH/PDL
- Confirmación 2 velas M5, ventana NY, R:R proxy
- CRT: fakeout PDH/PDL, PD reading, estado H1
- DMI proxy, divergencia RSI
- **8 reglas E1 como binarios** (desde `score_e1_rules_8`)

---

*Referencias: `TRADING_WINRATE_STATS.md`, `TRADING_PROFESSIONAL_STATS.md`, plan E1 M5*
