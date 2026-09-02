# Entrenamiento neuronal — Protocolo

> Cómo instalar, entrenar y mantener el clasificador visual WIN/LOSS de la galería desktop.

---

## 1. Requisitos

- Python 3.10+
- **GPU opcional** (CUDA acelera ResNet18; CPU funciona más lento)
- Carpeta fuente: `D:\Danilo\Trading\Cursor Trading\operaciones - desktop`
- Etiquetas: `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` (+ CSV manual opcional)

---

## 2. Instalación

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
pip install -r "training neuronal/requirements-neural.txt"
```

Si `torch` falla en tu sistema, usa el modo ligero:

```powershell
pip install scikit-learn pillow numpy pandas joblib tqdm
python "training neuronal/train_desktop_vision.py" --simple --quick
```

---

## 3. Entrenamiento

### Prueba rápida (~2–5 min CPU)

```powershell
python "training neuronal/train_desktop_vision.py" --quick
```

- Subconjunto de ~24 imágenes etiquetadas
- 2–3 épocas, ResNet18, imagen 160px
- Salida: `training neuronal/models/desktop_vision_model.pt`
- Reporte: `training neuronal/reports/training_report.md`

### Entrenamiento completo

```powershell
python "training neuronal/train_desktop_vision.py" --epochs 8 --architecture resnet18
```

### MobileNet (más rápido, menos VRAM)

```powershell
python "training neuronal/train_desktop_vision.py" --architecture mobilenet_v3_small
```

### Modo sklearn (sin PyTorch)

```powershell
python "training neuronal/train_desktop_vision.py" --simple
```

---

## 4. Análisis de la galería

```powershell
python "training neuronal/analyze_desktop_ops.py"
```

Genera `training neuronal/reports/desktop_analysis_report.md` con:

- Resumen WIN/LOSS predichos
- Tabla por archivo (confianza, alineación con etiqueta conocida)
- % rentabilidad estimada de la carpeta
- Notas de cumplimiento E1

---

## 5. Flags útiles

| Flag | Script | Descripción |
|------|--------|-------------|
| `--quick` | train | Subconjunto + pocas épocas |
| `--simple` | train / analyze | sklearn sin torch |
| `--cpu` | train | Forzar CPU |
| `--epochs N` | train | Épocas (default 8) |
| `--limit N` | analyze | Analizar solo N imágenes |

---

## 6. Etiquetas manuales (override)

Si una captura nueva no está en el context MD, crea o edita:

`training neuronal/data/desktop_labels.csv`

```csv
filename,label
BTC-nueva-fecha.png,WIN
captura-dudosa.png,LOSS
```

Prioridad: **CSV > context MD > heurística nombre**.

---

## 7. Cuándo re-entrenar

| Evento | Acción |
|--------|--------|
| Nuevas capturas en `operaciones - desktop` | `train_desktop_vision.py` |
| Cambio en reglas E1 / checklist visual | Revisar docs + re-entrenar |
| Accuracy baja en reporte | Añadir etiquetas CSV + más épocas |
| Mensual (mínimo) | Entrenamiento completo si hubo trades nuevos |

---

## 8. Tiempo estimado

| Modo | CPU | GPU |
|------|-----|-----|
| `--quick` | 2–8 min | 1–3 min |
| Completo 8 épocas | 15–40 min | 5–12 min |
| `--simple` | 30–90 s | n/a |

---

## 9. Archivos generados (gitignored)

```
training neuronal/
  models/desktop_vision_model.pt
  reports/training_report.md
  reports/desktop_analysis_report.md
  data/desktop_image_list.json
```

---

## 10. Relación con `docs/strategy/TRADING_ML_TRAINING.md`

- **Tabular:** velas M5 → `train_btc_signals.py` → live `--ml`
- **Visión:** capturas → `train_desktop_vision.py` → `analyze_desktop_ops.py`

Ambos **complementan** las reglas E1; ninguno sustituye TradingView.

---

*Índice: `training neuronal/README.md`*
