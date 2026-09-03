# Análisis Live BTC M5 — Contexto para Cursor

> Protocolo para analizar el **gráfico actual de Bitcoin** en **M5** según el plan E1 (CRT / Flopy-Scalping).
> Complementa `../strategy/TRADING_STRATEGY_CONTEXT.md`, `../strategy/TRADING_INDICATORS_RULES.md` y la galería desktop.
> **Última actualización:** 2026-08-31  
> Consumo de tokens por tier: [`../strategy/TRADING_ANALYZER_TOKEN_USAGE.md`](../strategy/TRADING_ANALYZER_TOKEN_USAGE.md)

---

## 1. Propósito

Este archivo permite que Cursor:

1. Lea un **snapshot live** generado por comando (`live/btc_m5_snapshot.md`).
2. Cruce precio, bias H1, PDH/PDL, swings y RSI con las **8 reglas inmutables**.
3. Entregue un veredicto claro: **ENTRAR / ESPERAR / NO OPERAR**.
4. **No** trate el veredicto automático del script como señal final.

---

## 2. Comandos — dos modos

### A) Full (análisis completo)

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-btc.ps1
```

Cursor:

> analiza `@live/btc_m5_snapshot.md` con mi plan E1 M5

| Salida | Contenido |
|--------|-----------|
| `live/btc_m5_snapshot.md` | **Veredicto** + CRT + checklist E1 (8 reglas) + detalle mercado, velas, PDH/PDL |
| `live/btc_m5_chart.png` | Gráfico ~60 velas M5 |

---

### B) Light (señal rápida, pocos tokens)

```powershell
.\scripts\analyze\analyze-btc-light.ps1
```

Cursor:

> `@live/btc_m5_signal.md` `@docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md`

| Salida | Contenido |
|--------|-----------|
| `live/btc_m5_signal.md` | ~25 líneas: **Veredicto** + Categories + CRT resumen + red flags |
| Sin gráfico | Más rápido, menos tokens |

---

### C) High (análisis profundo CRT + Turtle Soup, max tokens)

```powershell
.\scripts\analyze\analyze-btc-high.ps1
```

Cursor:

> `@live/btc_m5_high_signal.md` `@docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` analisis E1 CRT

| Salida | Contenido |
|--------|-----------|
| `live/btc_m5_high_signal.md` | **Veredicto** completo + CRT + E1 + E2 turtle soup + score extendido + 12 velas + galería |
| `live/btc_m5_chart.png` | Gráfico M5 |

Ver protocolo: `TRADING_LIVE_BTC_HIGH_SIGNAL.md`

---

### D) Los 3 a la vez

```powershell
.\scripts\analyze\analyze-btc.ps1 -All
```

---

### Opciones Python directas

| Comando | Efecto |
|---------|--------|
| `python -m app.controllers.analyze_btc_m5` | Full + chart |
| `python -m app.controllers.analyze_btc_m5 --mode light --no-chart` | Solo signal light |
| `python -m app.controllers.analyze_btc_m5 --mode high` | High + chart |
| `python -m app.controllers.analyze_btc_m5 --mode all` | Full + light + high + chart |
| `python -m app.controllers.analyze_btc_m5 --mode all --no-chart --ml` | Los 3 modos + ML prob en Categories |
| `python -m app.controllers.analyze_btc_m5 --mode all --no-chart --ml --neural` | Los 3 modos + ML + Neural galería |
| `python -m app.controllers.analyze_btc_m5 --no-chart` | Full sin PNG |
| `python -m app.controllers.analyze_btc_m5 --ml` | Cualquier modo con ML prob en Categories |
| `python -m app.controllers.analyze_btc_m5 --neural` | Cualquier modo con Neural galería (genera PNG si falta) |

**Fuente:** Binance public API (klines 5m + 1h). Sin API key.

---

## 3. Flujo recomendado (humano + Cursor)

```
1. Ejecutar:  .\scripts\analyze\analyze-btc.ps1
2. En Cursor:  @live/btc_m5_snapshot.md @docs/protocols/TRADING_LIVE_BTC_M5_ANALYSIS.md
               "analiza BTC M5 con mi plan E1"
3. Cursor responde: ENTRAR / ESPERAR / NO OPERAR + razones por regla
4. Si ENTRAR → validar visualmente en TradingView (CRT MTF + RSI TORYS)
5. Ejecutar solo si checklist E1 completa
```

### Prompt optimizado (copiar y pegar)

```
Analiza BTC M5 con mi plan E1 CRT/scalping.

ORDEN DE LECTURA:
1. live/btc_m5_snapshot.md — sección Categories PRIMERO (**Bando usado**, **Recomendación**)
2. Tabla "Reglas cumplidas (8)" del snapshot
3. Checklist y velas M5
4. Si hace falta contexto: TRADING_INDICATORS_RULES § CRT + RSI

REGLAS DE DECISIÓN (aplicar en orden):
| Condición | Veredicto |
| 2 SL hoy (preguntar si no consta) | NO_OPERAR — límite riesgo diario |
| 3 ops hoy | NO_OPERAR |
| Bias H1 NEUTRAL + lateral | ESPERAR |
| Bias contradice dirección | NO_OPERAR |
| Lejos de zona (>0.15%) | ESPERAR |
| Sin 2 velas M5 | ESPERAR |
| Rules <50% | NO_OPERAR |
| Rules 50–69% | ESPERAR (setup insuficiente) |
| bias + zona + 2M5 + R:R + Rules ≥70% | ENTRAR A+ — confirmar TV |

ML (si Categories incluye ML prob — flag `--ml`):
| ML prob | WR real test | Combinado con Rules % |
|---------|-------------|----------------------|
| <45% | 24.8% | **NO_OPERAR** (anula candidato ENTRAR) |
| 45–55% | 60.9% | **ESPERAR** — requiere Rules ≥75% para considerar |
| 55–65% | 21.1% | **NO_OPERAR** — bucket débil (n=19) |
| 65–75% | 75.0% | ENTRAR si Rules ≥70% + checklist E1 completa |
| >75% | 83.3% | A+ si Rules ≥70% + confirmar TV |

Re-entrenar semanal: `python -m app.controllers.train_btc_signals` · Ver [`../strategy/TRADING_ML_TRAINING.md`](../strategy/TRADING_ML_TRAINING.md)
El ML **complementa** Rules % — no reemplaza E1 ni TradingView.

Neural galería (si Categories incluye Neural — flag `--neural`):
| Neural WIN % | Sesgo |
|--------------|-------|
| <50% | **NO_OPERAR** |
| 50–70% | **ESPERAR** (salvo Rules ≥75%) |
| >70% | ENTRAR candidato si Rules ≥70% + ML ≥65% |
| >85% + Rules ≥75% | **A+** match galería desktop |

Ver [`app/services/learning/training neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md`](../../app/services/learning/training%20neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md) · Comando: `--neural` o `-Neural` en ps1

Responde en este formato:

## Veredicto: ENTRAR | ESPERAR | NO_OPERAR

**Dirección:** LONG / SHORT / —
**Calidad:** A+ / B / C / inválido
**Reloj:** (info opcional — no gate)
**Reglas:** X de 7 (XX%) — meta >70%
**ML prob:** XX% (si `--ml`) — bucket según §5.3
**Neural galería:** XX% WIN (si `--neural`) — bucket según §5.5

### Checklist E1 (7 reglas del script)
| Regla | Estado | Nota |
| Solo E1 | ✅/❌ | |
| Tendencia H1 alineada | ✅/❌ | |
| Cerca de zona clave | ✅/❌ | |
| 2 velas M5 | ✅/❌ | |
| R:R ≥ 1:2 | ✅/❌ | |
| RSI no contradice | ✅/❌ | |
| Rango CRT coherente | ✅/❌ | |

### Gestión (reglas inmutables extra)
| Regla | Estado |
| SL $9 fijo | ✅/❌ |
| <3 ops hoy | ❓ confirmar |
| <2 SL hoy | ❓ confirmar |

### ML (complemento)
| Campo | Estado | Nota |
| ML prob en Categories | ✅/❌ | Requiere `--ml` o `-ML` en ps1 |
| Bucket ML vs sesgo | ✅/❌/⚠️ | Ver tabla Rules+ML §5.3 |
| ML alineado con Rules | ✅/❌ | ML no contradice veredicto E1 |

### Plan (solo si ENTRAR)
- Entrada / zona:
- SL estructura + riesgo $9 en cuenta:
- TP 1:2:
- Invalidación:
- Confirmación TV: CRT MTF + RSI TORYS + banda morada

### Red flags
- (citar incumplimientos concretos del plan)

No trates el veredicto automático del script como señal final.
Si snapshot >30 min → pedir re-ejecutar scripts/analyze/analyze-btc.ps1.
Responde en español.
```

---

## 4. Qué mide el script (proxy)

| Dato | Cómo se calcula | Uso en E1 |
|------|-----------------|-----------|
| **Bias H1** | EMA20 vs EMA50 + pendiente | Sesgo macro — long solo BULLISH, short solo BEARISH |
| **PDH / PDL** | High/Low del día UTC anterior (desde H1) | CRT: dentro = NEUTRAL; >PDH bull; <PDL bear |
| **Swings M5** | Pivots lookback 3 | Proxy de zonas débiles (moradas en TV) |
| **RSI M5/H1** | RSI 14 clásico | Filtro TORYS-like (no entrada sola) |
| **2 velas M5** | Últimas 2 verdes o 2 rojas | Confirmación obligatoria E1 |
| **Reloj NY** | 08:00–11:00 y 14:00–17:00 (UTC-4) | Info opcional — **no** fuerza NO_OPERAR |

**Limitaciones (importante):**

- No ve indicadores TradingView (CRT Milana, RSI TORYS, BigBeluga).
- PDH/PDL es **aprox. UTC**, no necesariamente el día de tu broker.
- Zonas = swings estadísticos, no tus bandas moradas dibujadas.
- SL/TP del script es **boceto de estructura**; el riesgo real sigue siendo **~$9 en cuenta**.

---

## 5. Protocolo de respuesta de Cursor

Cuando Danilo pida análisis live, Cursor **debe**:

### 5.0 Reglas compartidas

**Inmutables del plan** (`../strategy/TRADING_VISUAL_CONTEXT.md` §4): Solo E1 90%+ · SL ~$9 · R:R 1:2 · máx. 3 ops/día · 2 SL = límite riesgo diario · BE 1:1 · Rules >70%. Sesión NY = reloj info (no gate).

**7 reglas E1 del script** (`btc_signal_categories.py`): Solo E1 · H1 alineado · zona ≤0.15% · 2 M5 · R:R 1:2 · RSI no contradice · CRT coherente.

**Jerarquía:** script refuerza → TradingView (CRT MTF + RSI TORYS) decide. Auto-veredicto **NO es señal final**. E2 solo watchlist — default NO ENTRAR E2.

### 5.1 Orden de lectura

1. `live/btc_m5_snapshot.md` — sección **Categories** primero (acción, tendencia, reglas, prob. histórica, calidad, **ML prob** si `--ml`)
2. Tabla **Reglas cumplidas (8)** del snapshot
3. Este archivo (protocolo)
4. Si hace falta: `../strategy/TRADING_INDICATORS_RULES.md` § CRT + RSI
5. Patrones WIN: `../strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1

### 5.2 Formato de respuesta (obligatorio)

Leer primero la sección **Veredicto** y **Categories** del snapshot (auto-generado por script).

```markdown
## Veredicto: ENTRAR | ESPERAR | NO_OPERAR

**Dirección:** LONG / SHORT / —
**Calidad:** A+ / B / C / inválido
**Reloj:** (info opcional — no gate)
**Reglas:** X de 7 (XX%) — meta >70%
**ML prob:** XX% (si `--ml`) — bucket según §5.3
**Neural galería:** XX% WIN (si `--neural`) — bucket según §5.5

### Checklist E1 (7 reglas del script)
| Regla | Estado | Nota |
| Solo E1 | ✅/❌ | |
| Tendencia H1 alineada | ✅/❌ | |
| Cerca de zona clave | ✅/❌ | |
| 2 velas M5 | ✅/❌ | |
| R:R ≥ 1:2 | ✅/❌ | |
| RSI no contradice | ✅/❌ | |
| Rango CRT coherente | ✅/❌ | |

### Gestión (reglas inmutables extra)
| Regla | Estado |
| SL $9 fijo | ✅/❌ |
| <3 ops hoy | ❓ confirmar |
| <2 SL hoy | ❓ confirmar |

### ML (complemento)
| Campo | Estado |
| ML prob / bucket | ✅/❌/⚠️ |
| Alineado con Rules | ✅/❌ |

### CRT
(tabla PD/H1/fakeout/0.5 del snapshot)

### Plan (solo si ENTRAR)
- Entrada / zona:
- SL (estructura) + riesgo $9:
- TP (1:2):
- Invalidación:
- Confirmación TV: CRT MTF + RSI TORYS + banda morada

### Red flags
- ...
```

Ver **Prompt optimizado** en §3 para el bloque copy-paste completo.

### 5.3 Reglas de decisión (CRT E1)

| Condición | Veredicto |
|-----------|-----------|
| 2 SL hoy | **NO_OPERAR** — límite riesgo diario |
| 3 ops hoy | **NO_OPERAR** |
| Reglas <50% | **NO_OPERAR** |
| Fakeout PDH + long | **NO_OPERAR** |
| CRT invalid / pending contra dirección | **NO_OPERAR** |
| Bias contradice dirección | **NO_OPERAR** |
| Sin 2 velas M5 | **ESPERAR** (regla dura) |
| Lejos de zona (>0.15%) | **ESPERAR** |
| PDH/PDL NEUTRAL + bias NEUTRAL | **ESPERAR** |
| Reglas 50–69% | **ESPERAR** (setup insuficiente) |
| Reglas ≥75% + bias + zona + 2 velas | **ENTRAR** (A+) — confirmar TV |
| Reglas 70–74% + resto OK | **ENTRAR** (B) — confirmar TV |
| Reglas 63–69% | **ESPERAR** (B) |

### 5.4 ML — complemento a Rules % (flag `--ml`)

El modelo GB entrenado sobre 876 muestras E1 (365 días, horizonte 48 velas M5) **augments** el scoring de reglas; **no reemplaza** las 8 reglas E1 ni la validación TradingView.

**Métricas test (hold-out 25%):** accuracy 69.4% · precision 62.3% · recall 55.8% · WR baseline 39.3%

| ML prob | N test | WR real | Sesgo operativo |
|---------|--------|---------|-----------------|
| **<45%** | 133 | **24.8%** | **NO_OPERAR** |
| **45–55%** | 23 | **60.9%** | **ESPERAR** — solo ENTRAR si Rules ≥75% |
| **55–65%** | 19 | **21.1%** | **NO_OPERAR** — bucket débil, muestra pequeña |
| **65–75%** | 20 | **75.0%** | ENTRAR candidato si Rules ≥70% + E1 completa |
| **>75%** | 24 | **83.3%** | A+ candidato si Rules ≥70% + confirmar TV |

**Tabla combinada Rules % + ML prob:**

| Rules % | ML prob | Veredicto sugerido |
|---------|---------|-------------------|
| cualquiera | <45% o 55–65% | **NO_OPERAR** (sesgo ML fuerte) |
| <50% | cualquiera | **NO_OPERAR** |
| 50–69% | 45–55% | **ESPERAR** |
| 50–69% | ≥65% | **ESPERAR** — ML no compensa Rules bajas |
| ≥70% | 45–55% | **ESPERAR** — requiere Rules ≥75% o ML ≥65% |
| ≥70% | 65–75% | **ENTRAR** (B) — confirmar TV |
| ≥70% | >75% | **ENTRAR** (A+) — confirmar TV |
| ≥75% | >75% | **ENTRAR** (A+) — máxima confluencia |

Comando: `python -m app.controllers.analyze_btc_m5 --mode all --no-chart --ml` · Re-entrenar: `python -m app.controllers.train_btc_signals` (semanal) · [`../strategy/TRADING_ML_TRAINING.md`](../strategy/TRADING_ML_TRAINING.md)

### 5.5 Neural galería — complemento visión (flag `--neural`)

ResNet18 entrenado sobre capturas `operaciones - desktop` (~80% val accuracy). Clasifica el PNG live `live/btc_m5_chart.png` como similitud WIN/LOSS vs galería histórica E1. **Augments** Rules % y ML; no reemplaza E1 ni TradingView.

| Neural WIN % | Sesgo operativo |
|--------------|-----------------|
| **<50%** | **NO_OPERAR** — baja similitud galería WIN |
| **50–70%** | **ESPERAR** — salvo Rules ≥75% |
| **>70%** | ENTRAR candidato si Rules ≥70% + ML ≥65% |
| **>85%** + Rules ≥75% | **A+** match galería desktop |

**Tabla combinada Rules % + ML prob + Neural WIN %:**

| Rules % | ML prob | Neural WIN % | Veredicto sugerido |
|---------|---------|--------------|-------------------|
| <50% | cualquiera | cualquiera | **NO_OPERAR** |
| ≥70% | ≥65% | >70% | **ENTRAR** (B+) — confirmar TV |
| ≥75% | >75% | >85% | **ENTRAR** (A+) — máxima confluencia |
| ≥70% | cualquiera | <50% | **NO_OPERAR** — neural veta |
| 50–69% | cualquiera | >70% | **ESPERAR** — neural no compensa Rules bajas |

Comando: `python -m app.controllers.analyze_btc_m5 --mode all --no-chart --ml --neural` · Re-entrenar: `python "app/services/learning/training neuronal/train_desktop_vision.py"` · [`app/services/learning/training neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md`](../../app/services/learning/training%20neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md)

---

## 6. Mapeo a indicadores TradingView

Tras el snapshot, abrir BTC M5 en TradingView y cruzar:

| Snapshot | En TradingView |
|----------|----------------|
| Bias H1 | CRT MTF HTF 1H + widget Daily Bias |
| PDH/PDL | Niveles CRT / PDH-PDL |
| Swings | Swing H/L matsu + bandas moradas |
| RSI 14 | RSI Divergence [TORYS] (color fondo) |
| 2 velas | Confirmación visual M5 |

**Regla madre:** el script **refuerza**; TradingView + zona morada **deciden**.

---

## 7. Seguridad operativa

- El análisis **no** es consejo financiero ni señal automática.
- Máx. **3 ops/día**, **2 SL = fin**.
- Solo **BTC** o **US30**, un mercado a la vez.
- Si el snapshot tiene >30 min, **re-ejecutar** el comando antes de decidir.

---

## 8. Referencias

| Recurso | Ruta |
|---------|------|
| Snapshot live | `live/btc_m5_snapshot.md` |
| Chart live | `live/btc_m5_chart.png` |
| Script | `app.controllers.analyze_btc_m5` |
| Launcher | `scripts/analyze/analyze-btc.ps1` |
| Plan E1 | `../strategy/TRADING_STRATEGY_CONTEXT.md` |
| ML training | `../strategy/TRADING_ML_TRAINING.md` |
| Neural desktop | `app/services/learning/training neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md` |
| Indicadores | `../strategy/TRADING_INDICATORS_RULES.md` |
| Galería WIN | `../strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` |

---

*Usar en Cursor: `@docs/protocols/TRADING_LIVE_BTC_M5_ANALYSIS.md` + `@live/btc_m5_snapshot.md`*
