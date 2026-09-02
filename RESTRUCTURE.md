# Reestructuración — Cursor Trading

**Fecha:** 2026-09-02  
**Fases:** (1) código Python → MVC `app/` · (2) docs + launchers fuera de raíz

## Estructura actual

```
Cursor Trading/
├── app/                          # MVC Python
├── scripts/
│   ├── analyze/                  # TODOS los analyze-*.ps1
│   ├── annotate_btc_m5_chart.py
│   ├── generate_winrate_images.py
│   └── measure_analyzer_tokens.py
├── docs/
│   ├── protocols/                # TRADING_LIVE_* (usados por analyzers / @ Cursor)
│   └── strategy/                 # plan, visual, indicadores, stats, ops, ML, rutina
├── live/                         # outputs generados (sin cambio)
├── data/, models/, tests/
├── analyze-btc-high.ps1          # stub opcional → scripts/analyze/
├── analyze-us30-high.ps1         # stub opcional → scripts/analyze/
├── RESTRUCTURE.md / VERSION / requirements-ml.txt / .gitignore
└── .cursor/rules/trading.mdc
```

## Comandos (post-fase docs)

```powershell
cd "D:\Danilo\Trading\Cursor Trading"

# Preferido — ruta canónica
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate

# Stubs raíz (solo high)
.\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
.\analyze-us30-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate

# Otros tiers
.\scripts\analyze\analyze-btc.ps1
.\scripts\analyze\analyze-btc-light.ps1
.\scripts\analyze\analyze-btc-superhigh.ps1
.\scripts\analyze\analyze-us30.ps1
.\scripts\analyze\analyze-us30-light.ps1
```

Invocación Python (sin cambio):

```powershell
python -m app.controllers.analyze_btc_m5 ...
python -m app.controllers.analyze_us30_m5 ...
python -m app.controllers.analyze_super_high_entry ...
python -m app.controllers.train_btc_signals
python -m app.controllers.train_us30_signals
python -m scripts.measure_analyzer_tokens
```

## Cursor @ refs

| Antes (raíz) | Ahora |
|--------------|--------|
| `@TRADING_LIVE_BTC_HIGH_SIGNAL.md` | `@docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` |
| `@TRADING_LIVE_US30_HIGH_SIGNAL.md` | `@docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md` |
| `@TRADING_STRATEGY_CONTEXT.md` | `@docs/strategy/TRADING_STRATEGY_CONTEXT.md` |
| `@live/btc_m5_high_signal.md` | sin cambio |

## Archivos movidos — fase docs/scripts (2026-09-02)

### `docs/protocols/`

| Archivo |
|---------|
| `TRADING_LIVE_BTC_HIGH_SIGNAL.md` |
| `TRADING_LIVE_US30_HIGH_SIGNAL.md` |
| `TRADING_LIVE_BTC_M5_ANALYSIS.md` |
| `TRADING_LIVE_BTC_SIGNAL_LIGHT.md` |
| `TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md` |
| `TRADING_LIVE_US30_M5_ANALYSIS.md` |
| `TRADING_LIVE_US30_SIGNAL_LIGHT.md` |

### `docs/strategy/`

| Archivo |
|---------|
| `TRADING_STRATEGY_CONTEXT.md` |
| `TRADING_VISUAL_CONTEXT.md` |
| `TRADING_OPERATIONS_DESKTOP_CONTEXT.md` |
| `TRADING_WINRATE_STATS.md` |
| `TRADING_PROFESSIONAL_STATS.md` |
| `TRADING_INDICATORS_RULES.md` |
| `TRADING_DAILY_ROUTINE_4X.md` |
| `TRADING_ANALYZER_TOKEN_USAGE.md` |
| `TRADING_ML_TRAINING.md` |
| `TRADING_2M5_SHORT_VISUAL.md` |

### `scripts/analyze/`

Todos los `analyze-*.ps1` (Set-Location → raíz del proyecto vía `$PSScriptRoot\..\..`).

## Archivos eliminados

**Ningún MD eliminado** en esta fase — todos tenían referencias (analyzers, trading.mdc, ML/neural o docs cruzados). Preferencia: mover a `docs/` sobre borrar.

### Huérfanos (fase previa MVC)

| Archivo | Motivo |
|---------|--------|
| `_parse_desktop_stats.py` | Script one-off; sin referencias |
| `_image_mapping.json` / `_image_urls.json` | Sin referencias |
| `BACKUP_LOCATION.txt` | Nota externa; no operativa |
| Wrappers raíz `analyze_*.py` / `train_*.py` / `measure_analyzer_tokens.py` | Sustituidos por `python -m` |

## Verificación

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
python -m pytest tests/test_high_signal_rules.py -v
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
.\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
```

## Notas técnicas

- `app/config.py`: `PROJECT_ROOT`, `DOCS_PROTOCOLS_DIR`, `DOCS_STRATEGY_DIR`, `TRAINING_NEURAL_DIR` → `app/services/learning/training neuronal`.
- `scripts/measure_analyzer_tokens.py` lee protocolos desde `docs/protocols/`.
- `neural_desktop_model.py` lee `docs/strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md`.
- `.cursor/rules/trading.mdc` refleja rutas `docs/` + `scripts/analyze/`.

## Cleanup health-check (2026-09-02)

WARN de docs/config/gitignore (runtime OK):

- `.gitignore`: artefactos neural bajo `app/services/learning/training neuronal/` (models/reports/data).
- `docs/protocols` + `docs/strategy`: comandos `python -m app.controllers.*` y links neural a la ruta MVC.
- `app/config.py`: `IMAGES_DIR` / `DESKTOP_OPS_DIR` / `TRAINING_ML_DIR` → `assets/` real.
- Eliminado leftover raíz `__pycache__/analyze_btc_m5.*.pyc`.

## Versionado

Ver [docs/VERSIONING.md](docs/VERSIONING.md). Baseline Git: `VERSION` = 1.1.0, tag `v1.1.0`.
