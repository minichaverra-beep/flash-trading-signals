# Análisis desktop — Protocolo Cursor

> Cómo ejecutar e interpretar el análisis automático de `operaciones - desktop` con el módulo neuronal.

---

## 1. Objetivo

Responder: **¿esta captura (o toda la galería) se alinea con setups WIN o LOSS documentados en E1?**

El script `analyze_desktop_ops.py` recorre cada PNG, predice WIN/LOSS y compara con la etiqueta conocida del índice en `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md`.

---

## 2. Ejecución en Cursor

### Paso 1 — Entrenar (si no hay modelo)

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
pip install -r "training neuronal/requirements-neural.txt" -q
python "training neuronal/train_desktop_vision.py" --quick
```

### Paso 2 — Analizar galería

```powershell
python "training neuronal/analyze_desktop_ops.py"
```

### Paso 3 — Leer reporte

Abrir en Cursor:

`training neuronal/reports/desktop_analysis_report.md`

O pedir al asistente:

> Analiza `@training neuronal/reports/desktop_analysis_report.md` y dime qué capturas están desalineadas con E1.

---

## 3. Qué significa "profitable" aquí

En este módulo, **profitable / WIN** no es P&L de cuenta en tiempo real. Significa:

| Término | Significado |
|---------|-------------|
| **WIN** | La captura coincide con patrones ganadores §5.1 (sweep, 2 velas, bias, NY, zona morada) |
| **LOSS** | Patrones perdedores §5.2 (bias contrario, momentum contra, fakeout, sobreoperar) |
| **Confianza** | Probabilidad del modelo (0–100%) |
| **Alineado** | Predicción = etiqueta del context MD |
| **Desalineado** | Modelo discrepa — revisar manualmente |

La **rentabilidad estimada %** del reporte = `predicciones WIN / total analizado`. Es un proxy visual sobre la galería histórica (~73% WIN real según §8 del context MD).

---

## 4. Interpretación del reporte

### Resumen

- **Imágenes analizadas:** total PNG de trades (excluye `balance/`)
- **Predicción WIN/LOSS:** conteos del modelo
- **Alineación:** cuántas coinciden con etiqueta documentada

### Tabla por imagen

| Columna | Uso |
|---------|-----|
| Etiqueta conocida | WIN/LOSS del índice MD (ground truth) |
| Predicción | Salida del modelo |
| Confianza | >70% = señal fuerte; <55% = dudoso |
| Alineación | `alineado` / `desalineado` / `sin etiqueta conocida` |

### Cumplimiento E1

Notas automáticas que citan §5.1 / §5.2 y recuerdan que el modelo no ve precio live.

---

## 5. Validar una captura nueva (flujo manual)

1. Guardar PNG en `operaciones - desktop` con nombre `BTC-DD-MM-YY.png`
2. Añadir fila en `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` o `data/desktop_labels.csv`
3. Re-entrenar: `train_desktop_vision.py --quick`
4. Analizar: `analyze_desktop_ops.py`
5. Cruzar con checklist §7.1 del context MD:
   - Daily Bias alineado
   - 2 velas M5
   - Ventana NY
   - R:R ≥ 1:2
   - Trade #1–3 del día

---

## 6. Limitaciones

| Limitación | Mitigación |
|------------|------------|
| No lee texto del Bias widget | Validar bias manualmente en TV |
| Dataset pequeño (~110 trades) | Usar como segunda opinión |
| Screenshots ≠ mercado live | Combinar con `analyze_btc_m5.py --ml` |
| Balance/MT excluidos | Correcto — no son setups |

---

## 7. Prompts sugeridos para Cursor

```
@docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md @training neuronal/reports/desktop_analysis_report.md
¿Qué capturas desalineadas violan reglas E1 (bias, NY, 2 velas)?
```

```
@operaciones - desktop/BTC-06-08-26.png @TRADING_NEURAL_STRATEGY.md
¿Este setup visual cumple patrones WIN §5.1?
```

---

## 8. Integración con reglas inmutables

Antes de confiar en una predicción WIN:

1. **8 reglas** (`docs/strategy/TRADING_VISUAL_CONTEXT.md`) — obligatorio
2. **Galería desktop** — comparación visual humana
3. **ML visión** — este reporte
4. **ML tabular live** — `prob_win` si hay setup M5 activo

> *"E1 es mi edge. Solo ejecuto."* — el modelo no anula las reglas.

---

*Entrenamiento: `TRADING_NEURAL_TRAINING.md` · Estrategia: `TRADING_NEURAL_STRATEGY.md`*
