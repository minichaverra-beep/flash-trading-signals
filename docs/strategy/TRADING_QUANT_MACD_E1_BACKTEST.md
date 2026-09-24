# Quant brief — Mini-indicador MACD-like calibrado a E1 M5

> **Estado:** diseño + inventario de datos reales. **Backtest MACD: PENDING** (sin curvas ni PF inventados).  
> **Fecha inventario:** 2026-09-24  
> **Contrato:** mismo que Zentinel FVG+Vol — **filtro de confluencia, nunca trigger solo**.  
> Complementa: `TRADING_ML_TRAINING.md`, `DEEP_LEARNING_SIGNALS.md`, `ZENTINEL_TV_PRESETS.md`, plan E1.

---

## 1. Propósito y no-objetivos

### Propósito

Diseñar un **mini-oscilador tipo MACD** (histograma + cruce + z-score) calibrado a **continuaciones E1 en M5**, sesión NY, activos operativos **BTC / US30**, que:

1. Aporte **features** al pipeline ML tabular existente (`train_btc_signals` / `train_us30_signals`).
2. Actúe como **filtro soft** en High/Advanced (análogo a `zentinel_volume` en `compute_confluencia_setup`).
3. Se valide solo con **backtesting walk-forward** sobre parquets + ops matched OCR — métricas reales o marcadas **PENDING**.

### No-objetivos

| No es… | Por qué |
|--------|---------|
| Señal de entrada sola | Viola reglas E1 (zona + 2M5 + CRT); igual que RSI TORYS / FVG+Vol |
| Sustituto de las 8 reglas o del scorecard High | Fusión actual: Rules 28% + Ext 12% + CRT 12% + Neural 25% + ML 18% |
| Sistema E2 turtle soup | E2 ≤10%; este brief es **solo E1 continuación** |
| Equity curve / PF “demostrado” sin correr código | Prohibido inventar números |
| Reemplazo de TradingView | Checklist TV + presets Zentinel siguen obligatorios |

---

## 2. Hipótesis cuantificables falsables (H1–H4)

Todas se evalúan con el **mismo label** que el ML actual: TP 1:2 antes que SL en **48 velas M5** (ver §4).

| ID | Hipótesis | Criterio de falsación (a priori) |
|----|-----------|----------------------------------|
| **H1** | Tras confirmación **2M5** a favor, `Hist > 0` (long) / `Hist < 0` (short) mejora precision vs baseline sin filtro MACD | Si Δ precision ≤ 0 **y** Δ F1 ≤ 0 en hold-out / walk-forward NY → **rechazar H1** |
| **H2** | Divergencia precio–MACD (precio hace HH, Hist hace LH, o viceversa) predice **fakeout** / skip, no continuación E1 | Si WR en subset “divergencia” ≥ WR sin divergencia (misma dirección setup) → **rechazar H2** |
| **H3** | Periodos clásicos **12/26/9** son subóptimos en M5 E1; grid walk-forward de `fast/slow/signal` mejora OOS | Si best OOS F1 ≤ F1(12/26/9) en ≥2/3 folds NY → **mantener 12/26/9** o abandonar retune |
| **H4** | `z(Hist)` (z-score del histograma) discrimina mejor que cruce crudo MACD–Signal | Si AUC/F1 de features z ≤ AUC/F1 de `macd_cross` solo → **preferir cruce crudo** |

**PENDING:** ninguna H1–H4 tiene resultado numérico hasta ejecutar el plan §8.

---

## 3. Definición matemática + variantes

### 3.1 Núcleo (EMA)

Sea \(C_t\) el cierre M5.

\[
\begin{aligned}
EMA_n(t) &= \alpha C_t + (1-\alpha)\,EMA_n(t-1),\quad \alpha=\frac{2}{n+1}\\
MACD_t &= EMA_{fast}(t) - EMA_{slow}(t)\\
Signal_t &= EMA_{signal}(MACD)_t\\
Hist_t &= MACD_t - Signal_t
\end{aligned}
\]

Baseline candidato a falsar (H3): \(fast=12,\ slow=26,\ signal=9\).

**Implementación runtime:** `app/models/macd_quant.py` — `pandas.Series.ewm(span=…, adjust=False)`. Strategy A = cruce MACD×Signal + filtro precio vs EMA200; Strategy B (zero-line) solo como variante (`zero_line_cross_flags`), no como entrada E1.

### 3.2 Variantes de suavizado

| Variante | Definición | Uso propuesto |
|----------|------------|---------------|
| SMA-MACD | Sustituir EMA por SMA en fast/slow/signal | Control de sensibilidad |
| TEMA-MACD | Triple EMA sobre close | Menos lag en M5 |
| Zero-lag | EMA “zero-lag” aproximada (error-corrected) | Test lag vs ruido |
| Hist/ATR | \(Hist^{ATR}_t = Hist_t / ATR_k(t)\) | Escala por volatilidad (k candidato: 14 o periodo Zentinel vol BTC=84) |
| z(Hist) | \(z_t = (Hist_t - \mu_W)/\sigma_W\) ventana W causal | H4; W alineada a sesión (~78–96 barras M5) |

**Look-ahead:** EMA/SMA/ATR/z solo con datos \(≤ t\) (barra cerrada). Prohibido usar barra incompleta en training.

### 3.3 Features ML candidatas (añadir a las 37 actuales)

El joblib BTC actual (`models/btc_signal_features.json`, entrenado 2026-09-17) tiene **37 features** y **cero MACD**. Candidatas:

| Feature | Tipo | Notas |
|---------|------|-------|
| `macd_hist` | float | raw o /ATR |
| `macd_hist_z` | float | z-score W |
| `macd_hist_slope` | float | \(Hist_t - Hist_{t-1}\) |
| `macd_hist_accel` | float | Δ slope |
| `macd_cross_up` / `macd_cross_down` | bin | cruce en barra t o t−1 |
| `bars_since_macd_cross` | int | capped (ej. 24) |
| `macd_dist_zero` | float | \|MACD\| o Hist normalizado |
| `macd_h1_align` | bin | signo Hist M5 == signo Hist H1 (bias) |
| `macd_div_bull` / `macd_div_bear` | bin | para H2 |

---

## 4. Pipeline de entrenamiento con backtesting (núcleo)

### 4.1 Joins de datos (fuentes reales)

```
M5 OHLC  ──┐
H1 OHLC  ──┼── features E1 existentes (37) + MACD* ──┐
ops matched ┤  (peso ops_weight, ya en integrate_*)   ├── label 48b 1:2
vision labels┘  (evaluación / gating Neural, no label tabular) ──┘
```

| Capa | Ruta verificada 2026-09-24 | Conteos reales |
|------|----------------------------|----------------|
| BTC M5 | `data/btcusdt_m5.parquet` | **51 840** filas · `2026-03-21 17:15` → `2026-09-17 17:10` UTC |
| BTC H1 | `data/btcusdt_h1.parquet` | **4 320** filas · mismo tramo |
| US30 M5 | `data/us30_m5.parquet` | **5 000** filas · `2026-08-06` → `2026-09-01` |
| US30 H1 | `data/us30_h1.parquet` | **720** filas · `2026-07-20` → `2026-09-01` |
| XAU M5/H1 | `data/xauusd_*.parquet` | 8 000 / 2 160 (fuera del edge E1 primario; solo referencia) |
| OCR trades | `data/ops_mobile/v_ops_apr_sep/trades.csv` | **100** tras dedupe (`meta.json`: 102 imgs, 2 dup) |
| BTC matched | `…/btc_ops_matched.csv` | **53** · label 1=**33** · 0=**20** → **WR 62.3%** |
| US30 matched | `…/us30_ops_matched.csv` | **VACÍO** (size 2 B) |
| XAU matched M5 | `…/xauusd_ops_matched.csv` | **0 filas** (header only) |
| Mobile vision | `…/mobile_vision_labels.csv` (+ copia neuronal) | **55** · WIN 33 / LOSS 22 |
| Desktop labels | `app/services/learning/training neuronal/data/desktop_labels.csv` | **0 filas** (solo header) |
| Modelo BTC | `models/btc_signal_model.joblib` + `btc_signal_features.json` | samples **532** · ops_matched **53** · alg **gb** · horizon **48** |

**Discrepancia vs `ARTIFACTS.md`:** el cash-mgmt narraba OCR filtrado «98 ops, matched BTC **51 · WR 64,7%** (33W/18L)». En disco hoy: `trades` dedupe **100**, matched BTC **53 · WR 62.3%** (33W/20L). **Usar siempre el CSV**, no el número del artefacto.

### 4.2 Label (alineado con ML existente)

De `train_btc_signals.label_outcome` / `TRADING_ML_TRAINING.md`:

- Horizonte: **48** M5 (= 4 h).
- TP = entrada ± **2×** riesgo; SL estructural o \(9 / precio\).
- Si TP y SL en la misma barra → **0** (conservador).
- Si ninguno toca → muestra **excluida** (`None`).

Ops matched usan `label_source`: `real_sl_tp` (36) o `fixed_rr` (17) — ver columnas en `btc_ops_matched.csv`.

### 4.3 Protocolo train / val / walk-forward

| Fase | Protocolo | Notas |
|------|-----------|-------|
| Baseline | Hold-out 25% temporal (como train actual) | No shuffle aleatorio de barras |
| Walk-forward | Ventanas expansivas o rolling por semana NY | Solo barras `in_ny_window` si `--ny-only` |
| Ops | Peso `ops_weight` (actual **5.0** en features.json) | No leak: features en `bar_time` de match |
| MACD grid | fast/slow/signal en folds **internos** al train fold | Elegir por F1 OOS, no in-sample |

### 4.4 Cómo entra MACD en el stack

| Modo | Descripción | Estado |
|------|-------------|--------|
| **A — Features joblib** | Extender `_default_feature_names()` + vector en train/infer | **PENDING** implementación |
| **B — Filtro soft** | Como `volume_confluence_points` / Zentinel: puntos en confluencia, nunca ENTRAR solo | Diseño: §6 |
| **C — Panel mini-chart** | Serie Hist en illustrate / export TV | Tras A+B validados |

### 4.5 Métricas (reportar solo tras run)

Precision · Recall · F1 · Accuracy · WR por bucket de score · Profit factor **solo** si se simula R fijo 1R/−1R con el label (no inventar P&L USD OCR: `pnl` es null en OCR).

### 4.6 Resultados MACD actuales

| Experimento | Resultado |
|-------------|-----------|
| Grid 12/26/9 vs retune | **PENDING** |
| H1–H4 tests | **PENDING** |
| Equity curve | **NO GENERADA** (no inventar) |

Métricas ML **ya existentes** (contexto, no MACD):

| Fuente | Accuracy | Precision | Recall | F1 | Samples |
|--------|----------|-----------|--------|-----|---------|
| `btc_signal_features.json` metrics_after (2026-09-17, +ops) | 0.5639 | 0.5484 | 0.5312 | 0.5397 | 532 (ops 53) |
| `data/ml_training_report.md` (2026-09-01, **stale** vs joblib) | 0.6941 | 0.6234 | 0.5581 | — | 876 |
| US30 features.json | 0.625 | 0.5 | 0.3333 | 0.4 | 31 · ops_matched **0** |
| Neural mobile simple (`ml_ops_integration_report.md`) | 0.8 | 1.0 | 0.3333 | 0.5 | n=40 val_n=10 |

### 4.7 Comandos exactos (regen / baseline — sin inventar runs)

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
pip install -r requirements-ml.txt

# Regenerar parquets BTC + modelo tabular (label 48, 1:2)
python -m app.controllers.train_btc_signals --force-download
python -m app.controllers.train_btc_signals --ny-only

# US30 (yfinance M5 ~60d — matches OCR antiguos suelen fallar)
python -m app.controllers.train_us30_signals --force-download

# Re-integrar ops OCR → matched + peso en joblib
python -m scripts.integrate_mobile_ops_ml
python -m scripts.integrate_mobile_ops_ml --quick

# Inferencia live (sin MACD aún)
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -ML -Neural -Advanced
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -ML -Advanced
```

**Cuando exista** el script de backtest MACD (propuesto `scripts/backtest_macd_e1.py` — **aún no en repo**):

```powershell
# PROPUESTO — crear antes de citar métricas
python -m scripts.backtest_macd_e1 --asset btc --ny-only --horizon 48 --grid
python -m scripts.backtest_macd_e1 --asset btc --ny-only --params 8,21,5 --walk-forward
```

Hasta que ese módulo exista, cualquier número de PF/WR “MACD” es **inválido**.

---

## 5. Hiperparámetros candidatos (anclados al inventario)

No se eligen “porque sí”: anclas en datos y en el plan.

| Ancla empírica | Implicación para grid |
|----------------|----------------------|
| Confirmación E1 = **2 velas M5** (10 min) | `fast` corto: **5, 6, 8, 10, 12** |
| Horizonte label **48** M5 | `slow` no ≫ 48; candidatos **13, 17, 21, 26, 34** |
| Signal clásico 9 | **5, 7, 9** (menos lag en scalping) |
| Zentinel vol period BTC **84** / US30 **48** | Ventana z(Hist) o ATR: **48, 78, 84, 96** |
| Killzones NY ON: 08–10, 10–11, 14–16 ET | Evaluar OOS **solo** esas ventanas (`--ny-only` + flags Watchtower) |
| Ops BTC matched **53** (pequeño) | Grid fino → overfitting; máx. ~12–20 combos, 1 elección OOS |
| US30 matched **0** | No tunear hiperparámetros US30 hasta regenerar matches |

**Baseline fijo a reportar siempre:** `(12, 26, 9)` + hist raw + hist/ATR14 + z_84.

---

## 6. Contrato Zentinel / E1 (filter-only)

Idéntico a `config/zentinel_presets.yaml` → `role: confluence_filter`:

> **MACD-quant = filtro de confluencia. NUNCA trigger.**  
> Entrada = H1/CTR + zona + **2M5** (+ R:R 1:2, SL ~$9).

| Regla | Comportamiento |
|-------|----------------|
| Hist a favor + setup E1 OK | Soft bonus en confluencia / feature ML ↑ |
| Hist en contra | Soft malus o skip A+ estricto (post 1 SL) |
| Solo cruce MACD | **NO_OPERAR** / no ENTRAR |
| Divergencia (H2) | Advertencia fakeout — no entrada E2 automática |
| Post 2 SL | Indicador irrelevante (fin de sesión) |

### Slot de fusión sugerido

Pesos High actuales (`DEEP_LEARNING_SIGNALS.md`):

`Rules 28% | Ext 12% | CRT 12% | Neural 25% | ML 18% | (E2 5% Reverse)`

**Fase 1 (recomendada):** sin nuevo peso — MACD entra como **features dentro de ML 18%** + soft points en `compute_confluencia_setup` (como volumen Zentinel).  
**Fase 2 (solo si H1/H4 OOS OK):** soft weight ≤ **5%** renormalizando Ext/CRT, documentado en scorecard — no tocar Rules 28% ni Neural gating.

### Soft-filter wiring (implementado — sin métricas inventadas)

| Pieza | Ruta / contrato |
|-------|-----------------|
| Timeframe filtro / chart | **H4** (régimen). Entradas E1 **siguen en M5** (H1/CTR + zona + 2M5) — sin cambio |
| Datos H4 | No hay `*_h4.parquet` nativo. Plot: **M5→H4** (`resample 4h`). Analyze live (~200 M5 ≈ 4 H4): preferir **H1→H4** (~50 H4) |
| Núcleo EMA + Strategy A | `app/models/macd_quant.py` → `calculate_macd` / `generate_signals` sobre **closes H4** (`ewm adjust=False`) |
| Strategy B zero-line | `zero_line_cross_flags` — **variante solo**; no escribe `signal` ni dispara E1 |
| Soft-filter | `macd_soft_filter_ok(direction, row)` sobre **última H4 cerrada** → `True` si Hist a favor (LONG>0 / SHORT<0), `False` en contra, `None` sin datos |
| Confluencia | `macd_confluence_points` + cable en `compute_confluencia_setup` (max 1.0 pts; flag `categories['macd_soft_filter_ok']`) |
| Attach analyze | `attach_macd_quant_to_data` → `build_h4_frame_from_data` en `analyze_*_m5` + High |
| Mini-chart PNG | `python -m scripts.plot_macd_quant` → `live/btc_h4_macd_quant.png` (ventana ~7 días / ~42 H4; también `--symbol us30\|xau\|xauusd`) |
| UI «Nuevo análisis» | Flash Signals `POST /api/signals/macd-quant/analyze` → regenera PNG H4 semana |
| Ref visual | [live/btc_h4_macd_quant.png](../../live/btc_h4_macd_quant.png) |

**Contrato H4 (soft-filter):** el histograma / cruce Strategy A de la **última barra H4 cerrada** alinea o veta suavemente el setup E1. **Nunca** es el trigger. Sin setup E1 (H1/CTR + zona + 2M5) → ignore o soft note.

**Regla dura:** cruce MACD / Hist **nunca** produce ENTRAR por sí solo.

**Backtest WR/PF:** sigue **PENDING** (§4.6 / checklist §10). Este wiring no publica curvas ni inventa precision.

---

## 7. Integración con el stack

| Superficie | Cómo |
|------------|------|
| Train | Extender features en `app/models/ml_signals.py` + `train_*_signals` |
| Inferencia | `btc_ml_signals` / flag `--ml` ya existente |
| High / Advanced | Bloque markdown “MACD-quant (filter)” junto a `zentinel_report_lines` |
| Confluencia | `macd_confluence_points` en `compute_confluencia_setup` (soft; max 1.0) |
| Panel / illustrate | Mini-chart 2 paneles **H4**: `python -m scripts.plot_macd_quant` → `live/*_h4_macd_quant.png` |
| Flash Signals UI | Ruta `/macd-quant` · PNG `/api/signals/macd-chart` · **Nuevo análisis** `POST /api/signals/macd-quant/analyze` · artifact Wiki |
| TradingView | Export manual de periodos OOS ganadores a preset; **TV no se lee en vivo** |
| Scripts | `analyze-btc-high.ps1 -ML -Advanced`; plot MACD H4: `python -m scripts.plot_macd_quant [--symbol btc\|us30\|xau] [--days 7]` |
| Live refs | Filtros vs `live/btc_m5_high_signal.md` / `us30_…` (entradas M5); PNG MACD: `live/btc_h4_macd_quant.png` |

---

## 8. Plan de experimentos walk-forward (sesión NY)

Orden estricto; no saltar a UI antes de OOS.

1. **E0 — Sanity:** calcular MACD 12/26/9 en `btcusdt_m5.parquet`; verificar longitudes y NaN warm-up.
2. **E1 — Baseline filter:** setups con `confirm_2m5` + Hist signo alineado vs sin filtro → precision/F1 (**H1**).
3. **E2 — Divergence skip:** subset divergencia → WR (**H2**).
4. **E3 — Grid WF:** {(f,s,sig)} × {hist, hist/ATR, z} en folds semanales NY; elegir 1 combo OOS (**H3/H4**).
5. **E4 — Ops stress:** solo filas `btc_ops_matched` (n=53) — reportar con IC amplio; no afirmar edge fuerte.
6. **E5 — Ablation joblib:** modelo 37 feats vs 37+MACD; Δ F1 OOS.
7. **E6 — US30:** solo tras `us30_ops_matched` no vacío + parquet extendido.

Criterio de aceptación de un combo: Δ F1 OOS ≥ **+0.03** vs baseline sin MACD **y** no empeorar precision del bucket alta confianza — si no, **no merge**.

---

## 9. Riesgos / overfitting / look-ahead

| Riesgo | Mitigación |
|--------|------------|
| n_ops BTC = 53 | Peso acotado; no grid sobre ops solos |
| US30/XAU matched vacíos | No generalizar hiperparámetros cross-asset |
| `desktop_labels.csv` vacío | Neural desktop no aporta ground truth; no mezclar |
| Parquet BTC termina 2026-09-17 | Live 2026-09-24 puede estar fuera de cache → `--force-download` |
| Warm-up EMA | Drop primeras `slow+signal` barras |
| Label overlap 48 barras | Stride ≥ 1 documentado; preferir stride que reduzca solape en WF |
| OCR `outcome=open` (93/100) | Labels reales solo vía match a velas, no PnL screenshot |
| Confundir `ml_training_report.md` (Sep 1) con joblib Sep 17 | Citar `btc_signal_features.json` como fuente de métricas actuales |

---

## 10. Checklist de aceptación

- [ ] Script `backtest_macd_e1` (o equivalente) existe y lee solo parquets/CSV citados
- [ ] H1–H4 reportadas con N, precision, recall, F1, WR (o **REJECTED** explícito)
- [ ] Ninguna equity curve sin trade list reproducible
- [x] Contrato filter-only cableado (no ENTRAR por MACD solo) — soft points + `macd_soft_filter_ok`; PNG mini-chart **H4** en `live/`
- [ ] Features MACD en `*_signal_features.json` si se mergea a joblib
- [ ] Docs/HTML actualizados con números del run (no de este brief PENDING)
- [ ] Discrepancia ARTIFACTS vs CSV documentada o ARTIFACTS corregido
- [ ] US30: o matches regenerados, o explícitamente out-of-scope

**Hecho (2026-09-24, sin métricas):** módulo `macd_quant` + plot.  
**Hecho (H4):** soft-filter + mini-chart en **H4** (M5/H1 resample); UI «Nuevo análisis» regenera PNG semana. Backtest WR/PF PENDING.
---

## 11. Datos faltantes y comandos de regeneración

| Qué falta / débil | Acción |
|-------------------|--------|
| `us30_ops_matched.csv` vacío | Ampliar lookback US30 M5 + `python -m scripts.integrate_mobile_ops_ml` (hoy OCR US30=2 en `trades`) |
| `xauusd_ops_matched` 0 filas M5 | Esperado si fechas OCR fuera de M5; H1 labels diagnósticas ya en `xauusd_ops_h1_labels.csv` (2 LOSS) |
| `desktop_labels.csv` 0 filas | Etiquetar galería desktop o entrenar solo con `mobile_ops_labels.csv` (55) |
| Parquet BTC desfasado vs live | `python -m app.controllers.train_btc_signals --force-download` |
| Backtest MACD script | **Crear** `scripts/backtest_macd_e1.py` antes de publicar métricas |
| Métricas MACD | **PENDING** — no hay archivo de resultados |

---

## 12. Referencias citadas (abiertas en este brief)

| Recurso | Ruta |
|---------|------|
| ML training | `docs/strategy/TRADING_ML_TRAINING.md` |
| Fusión High | `docs/strategy/DEEP_LEARNING_SIGNALS.md` |
| Plan E1/E2 | `docs/strategy/TRADING_STRATEGY_CONTEXT.md` |
| Visual / kit 8 reglas | `docs/strategy/TRADING_VISUAL_CONTEXT.md` |
| Indicadores + Zentinel nota | `docs/strategy/TRADING_INDICATORS_RULES.md` |
| Presets Zentinel | `docs/strategy/ZENTINEL_TV_PRESETS.md`, `config/zentinel_presets.yaml` |
| Artefactos / cash-mgmt refs | `ARTIFACTS.md` |
| Ops meta / quality | `data/ops_mobile/v_ops_apr_sep/meta.json`, `quality_report.md`, `ml_ops_integration_report.md` |
| Matched / labels | `btc_ops_matched.csv`, `mobile_vision_labels.csv`, `trades.csv` |
| Features / modelo | `models/btc_signal_features.json`, `btc_signal_model.joblib` |
| Live | `live/btc_m5_high_signal.md`, `live/us30_m5_high_signal.md` |
| Mini-chart MACD H4 | `live/btc_h4_macd_quant.png` (script `scripts/plot_macd_quant.py` · M5→H4 · ~7d) |
| HTML hermano | `D:\Danilo\Trading\flash-signals-angular\docs\Artifacts\2026-09-24-quant-macd-e1-backtest.html` |

---

*Brief quant — solo números verificados en disco el 2026-09-24. Todo resultado MACD marcado PENDING hasta ejecutar el pipeline.*
