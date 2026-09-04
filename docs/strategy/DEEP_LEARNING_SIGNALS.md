# Deep Learning + fusión High (Rules × ML × Neural)

Cómo High combina reglas E1, ML tabular y visión ResNet, y cómo re-entrenar.

---

## 1. Hallazgos del scan (señales High)

| Debilidad | Impacto |
|-----------|---------|
| Scorecard rellenaba Neural ausente con **50% × 30%** | Inflaba/deflaba el score combinado sin chart |
| Neural low-conf / grade C sumaba igual que high-conf | Empujaba Confluencia / ENTRAR sin evidencia sólida |
| ML tabular no entraba en el scorecard High | Solo Rules+Neural; ML quedaba “invisible” en fusión |
| `gallery_aligned` solo miraba `prob_win ≥ 70%` | Ignoraba softmax débil del modelo |
| ML = P(win) del setup, no dirección pura | Hay que cruzar con H1 / bando; ahora hay penalización de conflicto |

E1 (8 reglas) **no se toca**. History P&L y SuperHigh/TvCapture siguen aparte.

---

## 2. Pesos de fusión High (`compute_advanced_scorecard`)

Base (se **renormalizan** si falta una fuente; **nunca** se rellena Neural con 50%):

| Capa | Peso base | Notas |
|------|-----------|--------|
| Rules E1 (8) | **28%** | `%` de reglas OK |
| Rules extendidas (10) | **12%** | meta >70% |
| CRT coherence | **12%** | pass/fail |
| Neural galería (gated) | **25%** | solo si hay chart + modelo |
| ML tabular (gated) | **18%** | solo con `--ml` + modelo |
| E2 turtle | **5%** | solo modo Reverse |

**Gating Neural:** `effective = 0.5 + (prob − 0.5) × gate_factor`  
- conf high → ×1.0 · medium → ×0.65 · low → ×0.35 · grade C → ×0.5 extra  
**Gating ML:** same shrink; conf low → ×0.45  
**Penalización dirección:** H1 vs bando en conflicto → score × **0.88**

Campos en Categories: `fusion_score`, `fusion_weights`, `neural_gate_factor`, `neural_effective_prob_win`.

Confluencia (`compute_confluencia_setup`) usa Neural/ML **gated** y puede restar 1 pt si H1 contradice el bando.

---

## 3. Pipeline DL (visión ResNet)

```
live/*_m5_chart.png  →  btc_neural_signals.predict_chart_similarity
                     →  Categories (neural_*) + scorecard Advanced
```

- Código: `app/services/learning/training neuronal/`
- Modelo: `.../models/desktop_vision_model.pt` (`TRAINING_NEURAL_DIR`)
- Docs internas: `TRADING_NEURAL_STRATEGY.md`, `TRADING_NEURAL_TRAINING.md`

### Re-entrenar Neural (visión)

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
pip install -r "app/services/learning/training neuronal/requirements-neural.txt"
python "app/services/learning/training neuronal/train_desktop_vision.py"
# rápido / smoke:
python "app/services/learning/training neuronal/train_desktop_vision.py" --quick
python "app/services/learning/training neuronal/analyze_desktop_ops.py"
```

Etiquetas: galería `assets/images/operaciones - desktop` + opcional `data/desktop_labels.csv`.

### Re-entrenar ML tabular (no DL profundo)

```powershell
pip install -r requirements-ml.txt
python -m app.controllers.train_btc_signals
python -m app.controllers.train_us30_signals
```

No hay MLP/LSTM tabular en producción aún: el camino DL útil hoy es **ResNet WIN/LOSS** + gating en High.

---

## 4. Cómo usarlo en High

```powershell
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate -Advanced
```

- `-Neural` necesita chart PNG (se genera si hace falta; sin chart → Neural omitido, no pad).
- `-ML` alimenta fusión aunque Categories High oculte la fila ML (scorecard Advanced sí la muestra gated).
- Mirar **Score combinado**, **Confluencia**, `neural_confidence` / gate antes de ENTRAR.

SuperHigh (captura TV) usa pesos propios 50/30/20 — no confundir con High live.

---

## 5. Límites honestos

- Visión depende de calidad/cantidad de la galería WIN/LOSS; re-entrenar tras añadir capturas etiquetadas.
- ML tabular es RF/LR sobre features M5; no sustituye confirmación TV ni 2M5.
- Gating reduce falsos ENTRAR por Neural débil; no inventa edge si Rules/CRT fallan.
- Un MLP/LSTM sobre features cacheadas sería el siguiente paso **solo** con dataset etiquetado estable y validación walk-forward.

*Refs: `how_to_use.txt`, `docs/strategy/TRADING_ML_TRAINING.md`, `app/services/learning/training neuronal/README.md`*
