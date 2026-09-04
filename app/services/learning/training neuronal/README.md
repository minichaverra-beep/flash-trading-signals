# Training Neuronal — Índice

Módulo de **deep learning / visión por computadora** para la estrategia E1 de Danilo. Complementa el ML tabular (`train_btc_signals.py`) analizando **capturas reales** de `operaciones - desktop`.

---

## Archivos

| Archivo | Descripción |
|---------|-------------|
| [TRADING_NEURAL_STRATEGY.md](TRADING_NEURAL_STRATEGY.md) | Arquitectura, objetivos, relación con E1 y reglas inmutables |
| [TRADING_NEURAL_TRAINING.md](TRADING_NEURAL_TRAINING.md) | Instalación, entrenamiento, re-entrenamiento |
| [TRADING_NEURAL_DESKTOP_ANALYSIS.md](TRADING_NEURAL_DESKTOP_ANALYSIS.md) | Protocolo de análisis de la galería desktop |
| `train_desktop_vision.py` | Entrena clasificador WIN vs LOSS |
| `analyze_desktop_ops.py` | Inferencia sobre toda la galería + reporte |
| `neural_desktop_model.py` | Modelo CNN (ResNet18) y fallback sklearn |
| `requirements-neural.txt` | Dependencias Python |
| `data/desktop_labels.csv` | Etiquetas manuales opcionales (override) |
| `reports/` | Informes generados (gitignored) |
| `models/` | Pesos del modelo `.pt` (gitignored) |

---

## Inicio rápido

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
pip install -r "training neuronal/requirements-neural.txt"
python "training neuronal/train_desktop_vision.py" --quick
python "training neuronal/analyze_desktop_ops.py"
```

---

## Relación con ML existente

| Capa | Script | Datos | Salida |
|------|--------|-------|--------|
| **Tabular (M5 live)** | `train_btc_signals.py` | Velas Binance | `prob_win` en análisis live |
| **Visión (galería)** | `train_desktop_vision.py` | Screenshots desktop | WIN/LOSS por captura |

**Orden sugerido:** reglas E1 → galería desktop → ML tabular live → ML visión (si hay captura nueva).

**Fusión High (pesos + gating):** ver `docs/strategy/DEEP_LEARNING_SIGNALS.md`.

---

## Fuente de etiquetas

1. `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` (índice 112 capturas)
2. `data/desktop_labels.csv` (manual, prioridad mayor)
3. Heurística de nombre de archivo (`WIN` / `LOSS` en el nombre)

Carpeta `balance/` excluida del entrenamiento (historial MT, no setups).

---

*Referencias: `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md`, `docs/strategy/TRADING_ML_TRAINING.md`*
