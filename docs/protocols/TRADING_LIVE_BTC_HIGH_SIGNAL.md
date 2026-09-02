# BTC M5 High Signal - Protocolo analisis profundo (CRT + Turtle Soup)

> Usar con `@live/btc_m5_high_signal.md` tras `.\scripts\analyze\analyze-btc-high.ps1`
> **Mas tokens que snapshot** - analisis CRT completo, E2 watchlist, score reglas, galeria WIN.
> Alineado a: `../strategy/TRADING_STRATEGY_CONTEXT.md`, `../strategy/TRADING_VISUAL_CONTEXT.md` SS1.1-1.2 SS7,
> `../strategy/TRADING_INDICATORS_RULES.md` SS3-6, `../strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` SS5.1

---

## Comando

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-btc-high.ps1
.\scripts\analyze\analyze-btc-high.ps1 -NoChart
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -ML -Neural
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
```

### Flags bias / setup (opcionales, mutuamente excluyentes)

Disponibles en **todos los launchers** (`scripts/analyze/analyze-btc-light.ps1`, `scripts/analyze/analyze-btc-high.ps1`, `scripts/analyze/analyze-btc.ps1`, `scripts/analyze/analyze-us30-*.ps1`). Aparecen en Categories como **Bando usado** y **Recomendación**.

| Flag PS | Efecto | Python |
|---------|--------|--------|
| `-Bullish` | Sesgo alcista forzado — re-puntúa setup como **LONG** | `--bias bullish` |
| `-Bearish` | Sesgo bajista forzado — re-puntúa setup como **SHORT** | `--bias bearish` |
| `-Break` | Modo **breakout** — ruptura de nivel/estructura sostenida (no fakeout/reversión) | `--setup break` |
| `-Reverse` | Modo **reversión E2** — turtle soup, PDH/PDL fakeout, sweep+reclaim; operable con 2 velas alineadas + winrate | `--setup reverse` |
| `-Ilustrate` / `-Illustrate` | PNG anotado 2M5 + zona + Entry/SL/TP (`live/btc_m5_chart_annotated.png`); **sí se genera aunque uses `-NoChart`** | `--ilustrate` |

Sin flags → `bias=auto` y `setup=auto` (comportamiento anterior).

**Ejemplos:**

```powershell
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bullish -Reverse
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
```

El high signal incluye tabla **Modo bias** / **Modo setup** y sección **Modo CLI** cuando aplica. Con `-Ilustrate` añade **Ilustración entrada (2M5 + óptima)** y el PNG anotado.

Cursor:

```
@live/btc_m5_high_signal.md @docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md
```

Genera: `live/btc_m5_high_signal.md` + `live/btc_m5_chart.png`  
Con `-Ilustrate`: también `live/btc_m5_chart_annotated.png` (aunque `-NoChart`).

---

## Jerarquia de comandos (tokens)

| Nivel | Script | Archivo Cursor | Tokens |
|-------|--------|----------------|--------|
| Light | `scripts/analyze/analyze-btc-light.ps1` | `@live/btc_m5_signal.md` | Minimo |
| Full | `scripts/analyze/analyze-btc.ps1` | `@live/btc_m5_snapshot.md` | Medio |
| **High** | `scripts/analyze/analyze-btc-high.ps1` | `@live/btc_m5_high_signal.md` | Alto |
| **Super High** | `scripts/analyze/analyze-btc-superhigh.ps1` | `@live/btc_super_high_signal.md` | **Maximo (captura usuario)** |

`.\scripts\analyze\analyze-btc.ps1 -All` genera Light + Full + High; **Super High solo si existe** `live/super_high_entry.png`.

Ver protocolo completo: [`TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md`](TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md)

---

## Que incluye HIGH vs snapshot

| Seccion | Snapshot | High |
|---------|----------|------|
| **Categories** (acción, tendencia, reglas, prob. hist., calidad, **Neural galería**; ML oculto en high) | SI compacto | **SI completo** |
| **Entrada optimizada (E1)** — AHORA vs OPTI + Plan concreto | NO | **SI** |
| **Ilustración entrada** (`-Ilustrate`) — PNG 2M5+OPTI anotado | NO | **SI (opcional)** |
| **2M5 Válido vs Inválido** | NO | **SI** |
| **Checklist 2M5** (5 ítems ✅/❌) | NO | **SI** |
| **Segunda indicación** (solo H1 NEUTRAL) | NO | **SI** |
| Precio + NY + bias | SI | SI |
| PDH/PDL basico | SI | SI + premium/discount 0.5 |
| CRT H1 pending/completed/invalid | NO | **SI** |
| Fakeout PDH/PDL | parcial | **SI + accion E1** |
| Turtle Soup E2 checklist 6 pts | NO | **SI** |
| RSI TORYS divergencia proxy | NO | **SI** |
| DMI AlgoAlpha proxy | NO | **SI** |
| Swing HL/LH estructura | parcial | **SI** |
| Score reglas 8/8 (Categories) | SI | **SI + detalle 10 ext.** |
| 12 velas M5 | 6 | **12** |
| Match galeria WIN/LOSS | NO | **SI** |
| Plan Notion confluencias | NO | **SI** |

**Orden de lectura:** sección **Categories** → **Entrada optimizada (E1)** → **Checklist 2M5** → CRT/E2.

### Entrada optimizada + 2M5 (nuevo en high)

| Sección | Contenido |
|---------|-----------|
| **Entrada optimizada (E1)** | Tabla AHORA vs ENTRADA OPTIMIZADA (precio, 2M5, acción) + Plan concreto (Trigger, Confirmación, Entry, SL, TP 1:2, R:R, Invalidación, Plan B) |
| **2M5 — Válido vs Inválido** | Patrones válidos (ej. ✅ SHORT OK: [R][R] en resistencia) vs inválidos ([G][R], [R][R]…[G][R]) |
| **Checklist 2M5** | 5 ítems live (NY, zona, 2M5, bias, RSI/CRT) — *Las 5 ✅ → 2M5 OK. Si falta una → ESPERAR.* |
| **Segunda indicación** | Solo si **Bando mercado (H1) = NEUTRAL** — sesgo auxiliar desde DMI, CRT PD y estructura M5 |

> **ML prob:** el flag `-ML`/`--ml` sigue ejecutando el modelo internamente, pero **no se muestra** en Categories ni scorecard del high signal. **Neural galería** sí se muestra con `-Neural`.

---

## Reglas compartidas (resumen)

### 8 inmutables del plan

Solo E1 90%+ · NY only · SL ~$9 · R:R 1:2 · máx. 3 ops/día · **2 SL = fin sesión** · BE 1:1 · **Rules >70%**

### 7 reglas E1 del script (checklist / status signal)

Solo E1 · H1 alineado · zona ≤0.15% · 2 M5 · R:R 1:2 · RSI no contradice · CRT coherente

> **Sesión NY** ya no es fila de la tabla de status signal ni fuerza `NO_OPERAR` en la recomendación ligada a esa tabla. Sigue como info en header/Categories.

**Jerarquía:** script refuerza → TradingView (CRT MTF + RSI TORYS) decide. Auto-veredicto **NO es señal final**.

**E2:** solo watchlist en High — default **NO ENTRAR E2**.

---

## Best practices CRT (E1) - aplicar en respuesta

1. **PDH/PDL first** - TRADING_VISUAL SS1.1: dentro=rango NEUTRAL; no forzar.
2. **Pending vs Invalid** - TRADING_INDICATORS SS3: no entrar contra CRT invalid reciente.
3. **0.5 midpoint** - Long en discount, short en premium (H1 range).
4. **Fakeout PDH** - NO long E1; posible trampa bajista.
5. **Fakeout PDL** - NO E1 chase; contexto E2 turtle soup si reclaim.
6. **2 velas M5** - Sin confirmacion = ESPERAR (regla dura).
7. **RSI TORYS** - Filtro a favor; nunca entrada sola por divergencia.
8. **Sesión NY** — informativa en header/Categories; **no** bloquea el checklist de status signal ni fuerza `NO_OPERAR` por sí sola.

---

## Best practices Turtle Soup (E2) - solo watchlist

Referencia: TRADING_VISUAL SS1.2, SS7 | PF E1=4.77 vs mixto 3.16

1. Solo reversion **macro** - no scalping M5 aislado.
2. Barrido liquidez (pool / PDL / swing low) + **reclaim**.
3. Entrada donde iba SL original del setup fallido.
4. SL **grande** - no regla $9 E1.
5. Max **1/semana** - checklist 6 puntos completo.
6. **PROHIBIDO en eval fondeo** hasta pasar.
7. Si E2_WATCH en high signal: decir "observar demo" - **no ENTRAR E2** por defecto.

---

## Score y umbrales

| Rules % | Calidad | Acción |
|---------|---------|--------|
| **≥75%** | **A+** | ENTRAR si resto OK — ~82% WR histórico E1 |
| **63–74%** | **B** | ESPERAR — ~67% WR global |
| **50–62%** | **C** | ESPERAR — setup insuficiente |
| **<50%** | inválido | **NO_OPERAR** |

Score extendido (High): 7 reglas E1 + extendidas (DMI, 2SL/3ops, SL $9) — meta **>70%** en extendidas.

**Galería WIN:** cruzar siempre con `../strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1 cuando aplique — citar match `BTC-xx-xx-xx` o "sin match".

---

## ML — interpretación por bucket (flag `--ml`)

El modelo GB **complementa** Rules % y score extendido; **no reemplaza** E1 ni TradingView.

**Dataset entrenamiento:** 876 muestras · WR global 39.2% · test accuracy 69.4% · precision 62.3% · recall 55.8%

| ML prob | N test | WR real | Interpretación |
|---------|--------|---------|----------------|
| **<45%** | 133 | **24.8%** | **NO_OPERAR** — sesgo fuerte contra entrada |
| **45–55%** | 23 | **60.9%** | **ESPERAR** — zona gris, muestra pequeña |
| **55–65%** | 19 | **21.1%** | **NO_OPERAR** — anomalía (n=19), tratar como veto |
| **65–75%** | 20 | **75.0%** | Confluencia positiva si Rules ≥70% + extendidas ≥70% |
| **>75%** | 24 | **83.3%** | A+ si Rules ≥70% + extendidas ≥70% + TV OK |

### Cruce ML × score extendido (10 reglas)

| Extendidas | ML prob | Veredicto sugerido |
|------------|---------|-------------------|
| <70% | cualquiera | **ESPERAR** o **NO_OPERAR** |
| ≥70% | <45% o 55–65% | **NO_OPERAR** — ML veta |
| ≥70% | 45–55% | **ESPERAR** — requiere Rules ≥75% |
| ≥70% | 65–75% | **ENTRAR** (B) — confirmar TV + galería |
| ≥75% | >75% | **ENTRAR** (A+) — máxima confluencia |

Comando: `python -m app.controllers.analyze_btc_m5 --mode high --ml` · Re-entrenar semanal: `python -m app.controllers.train_btc_signals` · [`../strategy/TRADING_ML_TRAINING.md`](../strategy/TRADING_ML_TRAINING.md)

---

## Neural galería — interpretación (flag `--neural`)

ResNet18 sobre `operaciones - desktop` (~80% val accuracy). Compara el chart live con patrones WIN/LOSS de la galería desktop. **Complementa** Rules %, ML y score extendido; **no reemplaza** E1 ni TradingView.

| Neural WIN % | Interpretación |
|--------------|----------------|
| **<50%** | **NO_OPERAR** — baja similitud galería WIN |
| **50–70%** | **ESPERAR** — salvo Rules ≥75% + extendidas ≥70% |
| **>70%** | Confluencia positiva si Rules ≥70% + ML ≥65% |
| **>85%** + Rules ≥75% | **A+** match galería desktop |

### Cruce Neural × ML × extendidas (10 reglas)

| Extendidas | ML prob | Neural WIN % | Veredicto sugerido |
|------------|---------|--------------|-------------------|
| <70% | cualquiera | cualquiera | **ESPERAR** o **NO_OPERAR** |
| ≥70% | ≥65% | >70% | **ENTRAR** (B+) — confirmar TV + galería |
| ≥75% | >75% | >85% | **ENTRAR** (A+) — máxima confluencia |
| ≥70% | cualquiera | <50% | **NO_OPERAR** — neural veta |

Comando: `python -m app.controllers.analyze_btc_m5 --mode high --ml --neural` · Re-entrenar: `python "app/services/learning/training neuronal/train_desktop_vision.py"` · [`app/services/learning/training neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md`](../../app/services/learning/training%20neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md)

---

## Modo Advanced (análisis profundo)

### Cuándo se activa

| Condición | Efecto |
|-----------|--------|
| `-Advanced` en `scripts/analyze/analyze-btc-high.ps1` | Fuerza modo advanced |
| `-ML` **y** `-Neural` juntos | **Auto-activa** advanced (sin flag explícito) |
| Sin `--advanced` | Output high estándar (sin cambios) |

```powershell
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bullish -Reverse -ML -Neural   # auto Advanced
.\scripts\analyze\analyze-btc-high.ps1 -NoChart -Advanced -ML -Neural            # explícito
```

Python: `--advanced` → secciones **A–I** en `live/btc_m5_high_signal.md`:

| Sección | Contenido |
|---------|-----------|
| **A** | Síntesis ejecutiva (3–5 bullets español) |
| **B** | Scorecard multicapa (E1, extendidas, ML, Neural, CRT, E2) |
| **C** | CRT deep dive (PDH/PDL %, 0.5, fakeout, H1×3, matriz §3.2) |
| **D** | E2 Turtle Soup expandido (si `-Reverse`) |
| **E** | Cruce ML × Neural (ALIGNED/CONFLICT/NEUTRAL) |
| **F** | Galería top 3 WIN/LOSS + tags |
| **G** | Plan trading + checklist 8 ítems (si candidato ENTRAR) |
| **H** | Psicología y guardas sesión |
| **I** | Bloque prompt Cursor ADVANCED |

**Tokens estimados:** live advanced ~1 500–1 800 (÷4) vs ~1 044 high estándar — ver `../strategy/TRADING_ANALYZER_TOKEN_USAGE.md`.

Cursor:

```
@live/btc_m5_high_signal.md @docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md analisis ADVANCED E1 CRT
```

---

## Prompt optimizado ADVANCED (copiar y pegar)

```
Análisis E1 CRT ADVANCED — BTC M5 HIGH mode (máximo contexto).

INSTRUCCIÓN PRINCIPAL: Lee TODAS las secciones del live file (Veredicto, Categories,
secciones A–I). NO acortar vs light mode. Responde en español estructurado.

PASO 1 — Categories + Veredicto
- Bando usado, Recomendación, acción, tendencia, reglas 8/8, prob. histórica, calidad
- ML prob y Neural galería si presentes
- Scorecard multicapa (sección B): citar score combinado %

PASO 2 — Síntesis ejecutiva (sección A)
- Contexto macro, setup, conflicto bando CLI vs H1, veredicto integrado
- Si CONFLICT ML×Neural: explicar tensión y priorizar Rules % + CRT

PASO 3 — CRT deep dive (sección C)
- PDH/PDL distancias % y puntos
- Premium/discount 0.5 y posición precio
- Fakeout paso a paso si activo
- Timeline H1 (últimas 3 velas)
- Matriz acción E1 §3.2 — qué fila aplica HOY

PASO 4 — Checklist E1 (7 reglas) + extendidas
- Tabla completa con ✅/❌
- Meta extendidas >70%

PASO 5 — Turtle Soup E2 (sección D, si REVERSE)
- Cada check 1–6 con evidencia
- Fakeout PDL/PDH interpretación
- "Observar demo" vs "NO ENTRAR" según TRADING_VISUAL §7

PASO 6 — Cruce ML × Neural (sección E)
- Acuerdo: ALIGNED / CONFLICT / NEUTRAL
- Bucket ML según ml_training_report.md
- Si ML bajo + Neural alto: explicar por qué NO entrar solo por galería

PASO 7 — Galería (sección F)
- Top 3 patrones WIN/LOSS con archivo BTC-xx-xx-xx
- Tags: continuación, fakeout, contra-bias, sweep+reclaim
- Cruzar TRADING_OPERATIONS_DESKTOP_CONTEXT §5.1

PASO 8 — Plan (sección G, solo si ENTRAR candidato)
- Zona entrada, SL $9 cuenta + SL estructural, TP 1:2, BE 1:1
- Invalidación, confluencias Notion
- Pre-trade checklist 8 ítems

PASO 9 — Red flags + Psicología (sección H)
- Fuera NY, 2 SL hoy (preguntar), FOMO risk
- Frase guía del plan

FORMATO RESPUESTA (completo, sin omitir secciones):

## Veredicto: ENTRAR | ESPERAR | NO_OPERAR

**E1/E2:** E1 primario | E2 watch only
**Tendencia:** Alcista | Bajista | Sin dirección
**Reglas:** X de 8 (XX%) | Extendidas: XX% | Score combinado: XX%
**ML prob:** XX% — bucket y cruce
**Neural galería:** XX% WIN — acuerdo ALIGNED/CONFLICT/NEUTRAL
**Calidad:** Setup fuerte / medio / débil
**Probabilidad histórica:** ~XX%

### Síntesis ejecutiva
(3–5 bullets del contexto actual)

### CRT deep dive
(PDH/PDL, 0.5, fakeout, H1 timeline, matriz acción)

### Checklist E1
(tabla 8 reglas)

### Turtle Soup E2
(Score X/6 | solo si REVERSE)

### Plan (si ENTRAR)
(entrada, SL, TP, checklist)

### Red flags y psicología
(incumplimientos + guardas sesión)

Recuerda: 2 SL = fin sesión · 3 ops max · confirmar TradingView antes de ejecutar.
No inventes datos fuera del high signal file.
```

---

## Prompt optimizado (copiar y pegar)

```
Análisis E1 CRT completo — BTC M5 HIGH mode.

Lee PRIMERO Categories en live/btc_m5_high_signal.md (**Bando usado**, **Recomendación**, acción, tendencia, reglas 8/8, prob. histórica, calidad, sesión, ML prob y Neural galería si `--ml` / `--neural`).

APLICAR BEST PRACTICES CRT (E1):
1. PDH/PDL first — dentro rango = NEUTRAL, no forzar dirección
2. Pending vs Invalid — NO entrar contra CRT invalid reciente
3. 0.5 midpoint — LONG en discount, SHORT en premium (rango H1)
4. Fakeout PDH → NO long E1 (trampa bajista)
5. Fakeout PDL → NO chase E1; contexto E2 turtle soup si reclaim
6. Sin 2 velas M5 → ESPERAR (regla dura)
7. RSI TORYS = filtro a favor, nunca entrada sola
8. Fuera NY → NO_OPERAR

TURTLE SOUP (E2) — SOLO WATCHLIST:
- Score X/6 del high signal
- E2 operable default: NO
- Si E2_WATCH: "observar demo" — PROHIBIDO en eval fondeo
- E2 = reversión macro, SL grande, max 1/semana — NO mezclar con E1 $9

SCORE:
- 7 reglas E1 (Categories) + reglas extendidas (DMI, 2SL/3ops, SL $9)
- Rules ≥75% → setup A+ histórico E1 (~82% WR)
- Rules 63-74% → B, WR global ~67%
- Rules <50% → NO_OPERAR

ML (si presente en Categories):
- <45% o 55-65% → sesgo NO_OPERAR (WR real 24.8% / 21.1%)
- 45-55% → ESPERAR (WR real 60.9%, n=23)
- 65-75% + extendidas ≥70% → candidato ENTRAR (WR real 75.0%)
- >75% + Rules ≥70% → A+ (WR real 83.3%)

Neural galería (si presente en Categories):
- <50% WIN → NO_OPERAR
- 50-70% WIN → ESPERAR (salvo Rules ≥75%)
- >70% WIN + Rules ≥70% + ML ≥65% → refuerza ENTRAR
- >85% WIN + Rules ≥75% → A+ match galería desktop

CRUZAR con galería WIN en TRADING_OPERATIONS_DESKTOP_CONTEXT §5.1 cuando aplique.

Responde SIN acortar vs light:

## Veredicto: ENTRAR | ESPERAR | NO_OPERAR

**E1/E2:** E1 primario | E2 watch only
**Tendencia:** Alcista | Bajista | Sin dirección | Sin setup
**Reglas:** X de 8 (XX%) | Extendidas: XX% (meta >70%)
**ML prob:** XX% — bucket y cruce con extendidas según protocolo
**Neural galería:** XX% WIN — bucket y cruce según protocolo §Neural
**Calidad:** Setup fuerte / medio / débil / No operar
**Probabilidad histórica:** ~XX% (según Categories)

### CRT
- PD reading / H1 state / fakeout / premium-discount 0.5

### Checklist E1 (tabla 7 reglas)
| Regla | OK | Nota |

### Turtle Soup E2
- Score X/6 | Operable: NO (default)

### Plan (si ENTRAR)
- Entrada / SL $9 cuenta / TP 1:2 / invalidación
- Galería WIN match: (BTC-xx-xx-xx o "sin match")
- Confluencias Notion sugeridas: (Continuación, Resistencia débil, etc.)

### Red flags
- (incumplimientos concretos + psicología si aplica: FOMO, contra macro, zona enemiga)

Recuerda: 2 SL = fin sesión · 3 ops max · confirmar en TradingView antes de ejecutar.
Responde en español. No inventes datos fuera del high signal file.
```

---

## Formato respuesta Cursor (HIGH)

Leer primero **Veredicto** y **Categories** en `live/btc_m5_high_signal.md` (auto-generado con reglas CRT E1).

El live file ya incluye: Veredicto, CRT tabla, Checklist E1 (8), Turtle Soup E2, Plan, Red flags, Galería hint.

Cursor debe **confirmar y sintetizar** — no acortar vs light mode:

```markdown
## Veredicto: ENTRAR | ESPERAR | NO_OPERAR

**E1/E2:** E1 primario | E2 watch only
**Tendencia:** Alcista | Bajista | Sin dirección
**Reglas:** X de 8 (XX%) | Extendidas: XX%
**ML prob:** XX% — bucket según protocolo
**Neural galería:** XX% WIN — bucket según protocolo §Neural
**Calidad:** Setup fuerte / medio / No operar
**Probabilidad histórica:** ~XX%

### CRT
(copiar/ampliar tabla del snapshot)

### Checklist E1
(tabla 8 reglas)

### Turtle Soup E2
Score X/6 | Operable: NO (default)

### Plan (si ENTRAR)
- Entrada / SL $9 / TP 1:2 / invalidación
- Galería WIN match: BTC-xx-xx-xx

### Red flags
- ...
```

**No acortar** vs light mode. Cruzar con galería desktop §5.1 cuando aplique.

---

## Referencias

| Archivo | Uso |
|---------|-----|
| `live/btc_m5_high_signal.md` | Datos live generados |
| `../strategy/TRADING_INDICATORS_RULES.md` | Flujo SS6.1, matriz SS8 |
| `../strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` | Patrones WIN SS5.1 |
| `../strategy/TRADING_VISUAL_CONTEXT.md` | CRT SS1.1, Turtle SS1.2 |
| `../strategy/TRADING_ML_TRAINING.md` | Entrenamiento y re-entrenamiento ML |
| `app/services/learning/training neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md` | Protocolo neural galería desktop |

---

*Super High > High > Full > Light en profundidad. Super High = on-demand con captura entry/SL/TP. Ejecutar comando antes de analizar.*
