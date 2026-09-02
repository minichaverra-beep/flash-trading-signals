# BTC M5 Signal Light — Protocolo mínimo (tokens)

> Usar con `@live/btc_m5_signal.md` tras `.\scripts\analyze\analyze-btc-light.ps1`
> **No** cargar otros MD salvo que el usuario pida análisis completo.

---

## Comando

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-btc-light.ps1
.\scripts\analyze\analyze-btc-light.ps1 -Bearish
.\scripts\analyze\analyze-btc-light.ps1 -Bullish -ML -Neural
```

Cursor:

```
@live/btc_m5_signal.md @docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md
```

---

## Qué incluye el live Light (auto-generado)

El script escribe **Veredicto + Categories compacto + CRT resumen + red flags** (sin tablas E1/E2 completas).

| Sección live | Contenido |
|--------------|-----------|
| **Veredicto** | ENTRAR / ESPERAR / NO_OPERAR (reglas CRT E1) |
| **Categories** | **Bando usado**, **Bando mercado (H1)**, **Recomendación**, acción, tendencia, reglas 8, calidad, prob. histórica, **ML prob** (con `--ml`), **Neural galería** (con `--neural`) |
| **CRT** | PD/H1, 0.5, fakeout, acción E1 (3–5 líneas) |
| **Red flags** | Top 4 flags ordenados por severidad |

**Orden de lectura:** sección **Categories** primero — **Bando usado**, **Recomendación**, acción, tendencia, reglas X/8, prob. histórica, calidad.

---

## Reglas compartidas (memoria mínima)

### 8 inmutables del plan (`../strategy/TRADING_VISUAL_CONTEXT.md` §4)

1. Solo E1 (90%+) — E2 solo watchlist/demo, ≤10%
2. Sesión NY (08–11 y 14–17 UTC-4) — fuera = NO_OPERAR
3. SL ~$9 fijo — nunca expandir
4. R:R mínimo 1:2
5. Máx. 3 ops/día
6. **2 SL = fin de sesión** — sin excepciones
7. BE en 1:1 si el precio respiró
8. **Rules ≥70%** siempre (ideal A+ con ≥75%)

### 8 reglas E1 del script (`btc_signal_categories.py`)

1. Sesión NY
2. Solo E1 (no E2)
3. Tendencia H1 alineada
4. Cerca de zona clave (≤0.15%)
5. 2 velas M5 confirman
6. R:R mínimo 1:2
7. RSI no contradice
8. Rango CRT coherente

**Jerarquía:** el auto-veredicto del script **NO es señal final** — TradingView (CRT MTF + RSI TORYS) decide.

---

## Reglas E1 CRT (memoria mínima)

1. **PDH/PDL first** — dentro rango = NEUTRAL, no forzar
2. **Pending vs Invalid** — NO entrar contra CRT invalid reciente
3. **0.5 midpoint** — LONG discount, SHORT premium
4. **Fakeout PDH** → NO long E1
5. **Fakeout PDL** → NO chase E1; E2 turtle soup context
6. **Sin 2 velas M5** → ESPERAR (regla dura)
7. **RSI TORYS** = filtro only
8. **Fuera NY** → NO_OPERAR

### Tabla de decisión (Rules %)

| Rules % | Veredicto |
|---------|-----------|
| **<50%** | **NO_OPERAR** |
| **50–69%** | **ESPERAR** |
| **≥70%** + NY + bias + zona + 2M5 | **ENTRAR** — confirmar TV |
| **2 SL hoy** | **NO_OPERAR** — fin sesión (sin importar setup) |

Scoring histórico: ≥75% → A+ (~82% WR) · 63–74% → B (~67%) · <50% → NO_OPERAR

### ML (complemento — no reemplaza E1 ni TradingView)

Con `--ml` aparece **ML prob** en Categories. El modelo **augments** Rules %; no sustituye las 8 reglas E1 ni la validación TV.

| ML prob | WR real test | Sesgo decisión |
|---------|-------------|----------------|
| **<45%** | 24.8% (n=133) | **NO_OPERAR** |
| **45–55%** | 60.9% (n=23) | **ESPERAR** |
| **55–65%** | 21.1% (n=19) | **NO_OPERAR** — muestra pequeña, tratar con cautela |
| **65–75%** | 75.0% (n=20) | ENTRAR solo si Rules ≥70% + E1 OK |
| **>75%** | 83.3% (n=24) | A+ si Rules ≥70% + confirmar TV |

Comando: `python -m app.controllers.analyze_btc_m5 --mode light --no-chart --ml --neural` · Re-entrenar semanal: `python -m app.controllers.train_btc_signals` · Ver [`../strategy/TRADING_ML_TRAINING.md`](../strategy/TRADING_ML_TRAINING.md)

### Neural galería (complemento visión — flag `--neural`)

Con `--neural` aparece **Neural galería** en Categories. ResNet18 entrenado sobre `operaciones - desktop` (~80% val accuracy) compara el PNG live `live/btc_m5_chart.png` con patrones WIN/LOSS históricos. Ver [`app/services/learning/training neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md`](../../app/services/learning/training%20neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md).

| Neural WIN % | Sesgo decisión |
|--------------|----------------|
| **<50%** | **NO_OPERAR** — baja similitud con galería WIN |
| **50–70%** | **ESPERAR** — salvo Rules ≥75% |
| **>70%** | Candidato **ENTRAR** si Rules ≥70% + ML ≥65% |
| **>85%** + Rules ≥75% | **A+** match galería desktop |

Comando: `python -m app.controllers.analyze_btc_m5 --mode light --no-chart --neural` · Re-entrenar: `python "app/services/learning/training neuronal/train_desktop_vision.py"`

### Tabla combinada Rules % + ML + Neural

| Rules % | ML prob | Neural WIN % | Veredicto sugerido |
|---------|---------|--------------|-------------------|
| <50% | cualquiera | cualquiera | **NO_OPERAR** |
| ≥70% | ≥65% | >70% | **ENTRAR** (B+) — confirmar TV |
| ≥75% | >75% | >85% | **ENTRAR** (A+) — máxima confluencia |
| ≥70% | cualquiera | <50% | **NO_OPERAR** — neural veta |
| 50–69% | cualquiera | >70% | **ESPERAR** — neural no compensa Rules bajas |

---

## Prompt optimizado (copiar y pegar)

```
Señal E1 BTC M5 — análisis light.

Lee PRIMERO la sección Categories del signal file (**Bando usado**, **Recomendación**, acción, tendencia, reglas X/8, prob. histórica, calidad, ML prob y Neural galería si están).

Aplica estas reglas del plan (sin repetir el plan completo):
- NY only · E1 only · Bias H1 alineado · Zona ≤0.15% · 2 velas M5 · R:R 1:2 · SL $9
- Rules ≥70% para ENTRAR · <70% → ESPERAR · <50% → NO_OPERAR
- ML prob (si presente): <45% o 55–65% → sesgo NO_OPERAR · 45–55% → ESPERAR · ≥65% + Rules ≥70% → refuerza ENTRAR · >75% → candidato A+
- Neural galería (si presente): <50% WIN → NO_OPERAR · 50–70% → ESPERAR salvo Rules ≥75% · >70% + Rules ≥70% + ML ≥65% → refuerza ENTRAR · >85% + Rules ≥75% → A+ galería
- Fuera NY / H1 NEUTRAL / sin 2M5 / 2 SL hoy → NO_OPERAR o ESPERAR según tabla del protocolo
- El auto-veredicto del script NO es señal final — confirmar en TradingView

Responde EXACTAMENTE en este formato (máx 5 líneas, sin tablas):

VEREDICTO: ENTRAR | ESPERAR | NO_OPERAR
BANDO: AUTO | BULLISH | BEARISH (del live file — Bando usado)
REC: (copiar Recomendación del live — ej. ENTRAR SHORT, ESPERAR LONG, NO_OPERAR — fin sesión)
DIR: LONG | SHORT | —
CLAVE: (1 regla que decide — citar regla concreta del plan)
INVALID: (precio/nivel que invalida)
NOTA: (opcional, 1 frase — incluir ML prob y/o Neural galería si están y "confirmar TV" si ENTRAR)

No inventes datos. No expliques CRT ni Turtle Soup aquí. Responde en español.
```

---

## Formato respuesta (obligatorio, max 5 líneas)

```
VEREDICTO: ENTRAR | ESPERAR | NO_OPERAR
BANDO: AUTO | BULLISH | BEARISH (del live file — Bando usado)
REC: (copiar Recomendación del live — ej. ENTRAR SHORT, ESPERAR LONG, NO_OPERAR — fin sesión)
DIR: LONG | SHORT | —
CLAVE: (1 regla CRT que decide)
INVALID: (precio/nivel)
NOTA: (opcional, 1 frase)
```

**No** repetir tablas ni explicar el plan completo. **No** inventar datos fuera del signal file.

---

## Mapeo rápido

| Signal | Acción |
|--------|--------|
| Veredicto NO_OPERAR | NO_OPERAR |
| Fuera NY / Fakeout PDH long | NO_OPERAR |
| Sin 2M5 | ESPERAR |
| H1 NEUTRAL + PD NEUTRAL | ESPERAR |
| Rules <50% | NO_OPERAR |
| Rules 50–69% | ESPERAR |
| Rules ≥70% + NY OK + 2M5 | ENTRAR — confirmar TV |
| ML prob <45% o 55–65% | NO_OPERAR (sesgo ML) |
| ML prob 45–55% | ESPERAR |
| ML prob ≥65% + Rules ≥70% | Refuerza ENTRAR |
| ML prob >75% + Rules ≥70% | Candidato A+ |
| Neural <50% WIN | NO_OPERAR (sesgo neural) |
| Neural 50–70% WIN | ESPERAR (salvo Rules ≥75%) |
| Neural >70% + Rules ≥70% + ML ≥65% | Refuerza ENTRAR |
| Neural >85% + Rules ≥75% | A+ match galería |
| 2 SL hoy | NO_OPERAR — fin sesión |

---

*Par completo: `scripts/analyze/analyze-btc.ps1` + `@live/btc_m5_snapshot.md`*
