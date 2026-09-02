# Análisis Live US30 M5 — Contexto para Cursor

> Protocolo para analizar el **Dow Jones (US30)** en **M5** según el plan E1 (CRT / Flopy-Scalping).
> Paralelo a `TRADING_LIVE_BTC_M5_ANALYSIS.md` — mismas 8 reglas inmutables y ventanas NY.
> **Última actualización:** 2026-09-01

---

## 1. Propósito

Este archivo permite que Cursor:

1. Lea un **snapshot live** generado por comando (`live/us30_m5_snapshot.md`).
2. Cruce precio, bias H1, PDH/PDL, swings y RSI con las **8 reglas inmutables**.
3. Entregue veredicto: **ENTRAR / ESPERAR / NO OPERAR**.
4. **No** trate el veredicto automático del script como señal final.

---

## 2. Fuente de datos

| Campo | Detalle |
|-------|---------|
| **Proveedor** | `yfinance` (sin API key) |
| **Ticker primario** | `YM=F` (futuros Dow mini) |
| **Fallback** | `^DJI` (índice cash) |
| **Intervalos** | M5 preferido; si no hay 5m → **15m** con nota en snapshot |
| **H1** | `1h` nativo o resample desde intraday |

> **Limitación vs BTC:** Binance ofrece M5 ilimitado 24/7; yfinance limita intraday a ~60 días y puede faltar data fuera de horario cash/futuros.

---

## 3. SL ~$9 en puntos US30

| Contrato | Valor/punto | SL ~$9 ≈ |
|----------|-------------|----------|
| Estándar ($5/pt) | $5 | ~2 pts |
| Mini ($1/pt) | $1 | **~9 pts** |
| Micro ($0.10/pt) | $0.10 | **~90 pts** |

El script documenta **~9 pts ($1/pt)** y **~90 pts (micro)** en cada snapshot. Ajusta según tu broker antes de operar.

---

## 4. Comandos

### A) Full

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-us30.ps1
```

Cursor:

> analiza `@live/us30_m5_snapshot.md` con mi plan E1 M5

| Salida | Contenido |
|--------|-----------|
| `live/us30_m5_snapshot.md` | Veredicto + CRT + checklist E1 + detalle mercado |
| `live/us30_m5_chart.png` | Gráfico ~60 velas M5 |

### B) Light

```powershell
.\scripts\analyze\analyze-us30-light.ps1
```

Cursor: `@live/us30_m5_signal.md` `@docs/protocols/TRADING_LIVE_US30_SIGNAL_LIGHT.md`

### C) High

```powershell
.\scripts\analyze\analyze-us30-high.ps1
```

Cursor: `@live/us30_m5_high_signal.md` `@docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md`

### D) Los 3 a la vez

```powershell
.\scripts\analyze\analyze-us30.ps1 -All -NoChart -ML -Neural
```

---

## 5. Flags CLI

| Flag | Efecto |
|------|--------|
| `--mode light\|full\|high\|all` | Tier de salida |
| `--ml` | ML prob en Categories (`models/us30_signal_model.joblib`) |
| `--neural` | Neural galería desde `live/us30_m5_chart.png` |
| `--no-chart` | Sin PNG (neural genera chart interno si hace falta) |
| `--bias bullish\|bearish` | Sesgo forzado (todos los tiers: `-Bullish`/`-Bearish` en PS1) |
| `--setup break\|reverse` | Modo E1 continuación vs E2 reversión |
| `--ticker YM=F` | Ticker yfinance alternativo |

---

## 6. ML US30

Entrenar modelo (primera vez o semanal):

```powershell
python -m app.controllers.train_us30_signals
python -m app.controllers.train_us30_signals --quick   # smoke test ~30d
```

Salida: `models/us30_signal_model.joblib` + `data/us30_ml_training_report.md`

---

## 7. Jerarquía de decisión

1. **8 reglas inmutables** + sesión NY
2. **Rules %** del script (8 reglas E1)
3. **CRT / PDH-PDL** en TradingView
4. **ML prob** (complemento)
5. **Neural galería** (complemento visual — entrenado en capturas BTC desktop; usar con cautela en US30)

---

## 8. Cuándo usar US30 vs BTC

| Situación | Activo |
|-----------|--------|
| Rutina diaria 4× | **BTC** (por defecto) |
| Día operando índice / plan US30 | **US30** — usar scripts `analyze-us30-*` |
| Máx. 1 mercado a la vez | Nunca BTC + US30 simultáneo |

Ver también: `../strategy/TRADING_DAILY_ROUTINE_4X.md` § US30 on-demand.

---

*Script `analyze_us30_m5` (módulo `app.controllers`) · Datos yfinance · Mismas reglas E1 que BTC*
