# Cursor Trading

Sistema de señales **BTC / US30** (estrategia E1) para trabajar en **Cursor**.

**Owner:** Danilo (minichaverra@gmail.com)

**Estrategia:** https://app.notion.com/p/jolunto/Bit-cora-trading-v2-1ee58354488080d0af44e687146f2838?source=copy_link

**Versión:** [1.1.0](VERSION) · tag `v1.1.0`

## Qué hace

Genera reportes live (markdown + opcionales PNG) para decidir entradas según el plan E1:

| Tier | Uso |
|------|-----|
| **Light** | Chequeo rápido |
| **Full** | Snapshot completo (solo excepcional) |
| **High** | Recomendado para decidir entrada (CRT + 2M5) |
| **Super High** | Validación con captura TradingView ya anotada |

Flags opcionales: **`-ML`** (modelo tabular), **`-Neural`** (similitud galería WIN), **`-Ilustrate`** (PNG anotado 2M5 + entrada óptima).

## Estructura

```
Cursor Trading/
├── app/                 # MVC Python (controllers, models, services, views)
├── scripts/analyze/     # Launchers analyze-*.ps1 (ruta canónica)
├── docs/
│   ├── protocols/       # TRADING_LIVE_* (@ Cursor)
│   └── strategy/        # Plan E1, visual, stats, ML
├── live/                # Outputs generados
├── data/, models/, tests/
├── analyze-*-high.ps1   # Stubs raíz (solo High)
└── .cursor/rules/       # trading.mdc · signals.mdc
```

## Requisitos

- Python 3
- PowerShell
- Dependencias ML: `requirements-ml.txt`
- Neural (opcional): `app/services/learning/training neuronal/requirements-neural.txt`

## Cómo usar

```powershell
cd "D:\Danilo\Trading\Cursor Trading"

# BTC High (recomendado)
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate

# US30 High (recomendado)
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
```

Cambia `-Bearish`/`-Bullish` y `-Break`/`-Reverse` según tu plan. Preferí siempre `scripts\analyze\...`; los stubs raíz solo cubren High.

Guía completa (Light / Full / Super High, Categories, reglas de sesión): [how_to_use.txt](how_to_use.txt).

## Cursor

Tras el script, en un chat nuevo:

- BTC High: `@live/btc_m5_high_signal.md` + `@docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md`
- US30 High: `@live/us30_m5_high_signal.md` + `@docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md`

La estrategia E1 carga sola vía `.cursor/rules/` (**Trading — Danilo** / **Señales live — BTC / US30**). No hace falta `@` del plan en cada chat.

## Versionado

Semver en `VERSION` + tags `vMAJOR.MINOR.PATCH`. Detalle: [docs/VERSIONING.md](docs/VERSIONING.md).

## Calidad y SonarQube

- Prácticas Git/tests/history vs High: [docs/QUALITY.md](docs/QUALITY.md)
- Config scanner: `sonar-project.properties` · tests/coverage: `pyproject.toml` · deps: `requirements-dev.txt`
- CI (opcional): `.github/workflows/sonarcloud.yml` — secret `SONAR_TOKEN` en GitHub; crear el proyecto en SonarCloud antes del primer scan

```powershell
pip install -r requirements-dev.txt
pytest tests/test_high_signal_rules.py
pytest --cov=app --cov-report=xml tests/
```

## Licencia

Licencia: [CC BY-NC-ND 4.0](LICENSE) — Copyright (c) 2026 Danilo.

En resumen:

- Uso personal / no comercial del código original (copias intactas OK).
- Prohibido uso comercial.
- Prohibido modificar o redistribuir versiones modificadas (atribución al compartir copias intactas).

Detalle y texto oficial: [LICENSE](LICENSE) · [creativecommons.org/licenses/by-nc-nd/4.0/](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**Aviso:** no es consejo financiero. Operar implica riesgo de pérdida; usá el sistema bajo tu propia responsabilidad.
