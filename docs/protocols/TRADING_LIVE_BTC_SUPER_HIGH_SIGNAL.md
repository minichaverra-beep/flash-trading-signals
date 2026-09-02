# BTC Super High Signal — Protocolo análisis captura entry/SL/TP

> Usar con `@live/btc_super_high_signal.md` tras `.\scripts\analyze\analyze-btc-superhigh.ps1`
> **Tier más profundo** — el usuario aporta su captura TradingView con entry, SL y TP dibujados.
> Alineado a: `../strategy/TRADING_STRATEGY_CONTEXT.md`, `../strategy/TRADING_VISUAL_CONTEXT.md`, `../strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` §5.1,
> `TRADING_LIVE_BTC_HIGH_SIGNAL.md` (base CRT + ML + Neural)

---

## Comando

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-btc-superhigh.ps1
```

Cursor:

```
@live/btc_super_high_signal.md @docs/protocols/TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md
```

Genera: `live/btc_super_high_signal.md` (analiza `live/super_high_entry.png`)

---

## Cuándo usar Super High

| Situación | Usar Super High |
|-----------|-----------------|
| Ya dibujaste **entry + SL + TP** en TradingView y quieres **probabilidad de éxito** antes de ejecutar | **SÍ** |
| Quieres cruzar tu setup visual con **neural galería + ML + reglas E1 live** | **SÍ** |
| Chequeo rápido de sesión sin captura propia | **NO** — usar Light |
| Análisis CRT general del mercado sin plan concreto | **NO** — usar High |
| Rutina 4× diaria automática | **NO** — on-demand cuando tengas captura |

---

## Jerarquía de comandos (tokens)

| Nivel | Script | Archivo Cursor | Tokens (~) | Captura usuario |
|-------|--------|----------------|------------|-----------------|
| Light | `scripts/analyze/analyze-btc-light.ps1` | `@live/btc_m5_signal.md` | ~612 | No |
| Full | `scripts/analyze/analyze-btc.ps1` | `@live/btc_m5_snapshot.md` | ~1 912 | No |
| High | `scripts/analyze/analyze-btc-high.ps1` | `@live/btc_m5_high_signal.md` | ~1 769 | No (auto chart) |
| **Super High** | `scripts/analyze/analyze-btc-superhigh.ps1` | `@live/btc_super_high_signal.md` | **~2 508** | **SÍ (obligatorio)** |

`.\scripts\analyze\analyze-btc.ps1 -All` genera Light + Full + High; **Super High solo si existe** `live/super_high_entry.png`.

---

## Paso 1 — Guardar captura (OBLIGATORIO)

Antes de ejecutar el script, **debes** guardar tu captura TradingView:

1. **Timeframe:** M5 BTCUSDT
2. **Indicadores visibles:** moradas (S/R), CRT MTF, RSI TORYS si aplica
3. **Dibujar en el chart:**
   - Línea **entrada** (precio exacto)
   - Línea **SL** (~$9 cuenta según plan)
   - Línea **TP** (R:R mínimo 1:2)
4. **Exportar screenshot** → guardar como:

```
live/super_high_entry.png
```

También acepta: `.jpg`, `.jpeg`, `.webp` o cualquier imagen en `live/super_high_captures/` (usa la más reciente).

### Notas manuales (opcional)

Si prefieres escribir los números en lugar de confiar en OCR:

```markdown
# live/super_high_entry.md
direction: LONG
entry: 78250
sl: 78241
tp: 78268
Notas: sweep PDL + reclaim, 2 velas M5 verdes
```

---

## Paso 2 — Ejecutar analizador

```powershell
.\scripts\analyze\analyze-btc-superhigh.ps1
# Equivalente:
python -m app.controllers.analyze_super_high_entry --ml --neural
```

Pipeline interno:

| Paso | Módulo | Peso | Fallback |
|------|--------|------|----------|
| a | **Neural vision** — `predict_chart_similarity()` vs galería desktop (104 ops, ~80% val) | **50%** | Omitido si no hay torch/modelo |
| b | **ML tabular** — `predict_signal_quality()` con datos live BTC M5 | **30%** | Omitido si no hay modelo |
| c | **OCR** — pytesseract extrae precios (opcional) | info | Skip si no instalado |
| d | **Heurísticas visuales** — zonas verde/rojo, líneas horizontales proxy | info | Skip si no PIL |
| e | **Reglas E1** — cross-check live (NY, bias, 8 reglas) | **20%** | Omitido si no hay red |

**Probabilidad combinada:** ponderada y renormalizada si falta alguna fuente.

---

## Grados y umbrales

| Probabilidad éxito | Grado | Acción sugerida |
|--------------------|-------|-----------------|
| **>80%** | **A+** | ENTRAR si Rules ≥6/8 + TV confirma |
| **65–80%** | **B** | ENTRAR cauteloso o ESPERAR 1 vela M5 |
| **50–65%** | **C** | ESPERAR — setup insuficiente |
| **<50%** | **NO_OPERAR** | No ejecutar |

---

## Tabla de decisión combinada (Rules + ML + Neural)

Tier más profundo — cruce de las 3 fuentes:

| Rules E1 | ML prob | Neural WIN % | Prob. combinada | Veredicto |
|----------|---------|--------------|-----------------|-----------|
| ≥6/8 (75%+) | >75% | >85% | >80% | **ENTRAR (A+)** |
| ≥6/8 | 65–75% | >70% | 65–80% | **ENTRAR (B)** |
| ≥5/8 | 45–55% | 50–70% | 50–65% | **ESPERAR** |
| <4/8 | cualquiera | cualquiera | <50% | **NO_OPERAR** |
| ≥6/8 | <45% | cualquiera | — | **NO_OPERAR** — ML veta |
| ≥6/8 | cualquiera | <50% | — | **NO_OPERAR** — neural veta |
| <5/8 | >75% | >85% | — | **ESPERAR** — rules insuficientes |

**Jerarquía:** reglas inmutables > Rules E1 > Neural > ML > opinión Cursor.

---

## Prompt optimizado (copiar y pegar)

```
Análisis Super High — probabilidad de éxito de MI captura entry/SL/TP.

Lee PRIMERO live/btc_super_high_signal.md (**Bando usado**, **Recomendación**, probabilidad combinada, neural, ML, rules).

CONTEXTO:
- Yo dibujé entry, SL y TP en TradingView M5 antes de ejecutar
- El script comparó mi captura vs galería WIN desktop (neural ResNet18)
- ML tabular y reglas E1 live cruzan el setup actual del mercado

APLICAR:
1. PROBABILIDAD ÉXITO y GRADO del live file — no inventar cifras
2. Si Neural <50% WIN → sesgo NO_OPERAR salvo Rules ≥75% + extendidas OK
3. Si ML <45% → veto fuerte (WR histórico 24.8%)
4. Rules <5/8 → ESPERAR aunque neural sea alto
5. Confirmar en TradingView: 2 velas M5, sesión NY, SL ~$9, R:R 1:2
6. Comparar visualmente con TRADING_OPERATIONS_DESKTOP_CONTEXT §5.1

Responde EXACTAMENTE en este formato:

PROBABILIDAD ÉXITO: XX%
GRADO: A+ | B | C | NO_OPERAR
NEURAL: XX% similar WIN galería
ML: XX% (si disponible)
RULES: X/8
VEREDICTO: ENTRAR | ESPERAR | NO_OPERAR
BANDO USADO: AUTO | BULLISH | BEARISH
RECOMENDACIÓN: ENTRAR LONG | ENTRAR SHORT | ESPERAR | NO_OPERAR (del live file)
RAZÓN CLAVE: ...
INVALIDACIÓN: ...

Luego añade:
- ¿Mi entry/SL/TP respetan plan E1 ($9 SL, 1:2 R:R)?
- Match galería WIN: (BTC-xx-xx-xx o "sin match claro")
- Red flags concretos de la captura vs reglas inmutables

Recuerda: 2 SL = fin sesión · 3 ops max · Super High complementa, no reemplaza tu criterio.
Responde en español.
```

---

## Formato respuesta Cursor (Super High)

```markdown
PROBABILIDAD ÉXITO: XX%
GRADO: A+ | B | C | NO_OPERAR
NEURAL: XX% similar WIN galería
ML: XX% (si disponible)
RULES: X/8
VEREDICTO: ENTRAR | ESPERAR | NO_OPERAR
BANDO USADO: AUTO | BULLISH | BEARISH
RECOMENDACIÓN: ENTRAR LONG | ENTRAR SHORT | ESPERAR | NO_OPERAR (del live file)
RAZÓN CLAVE: ...
INVALIDACIÓN: ...

### Validación captura
- Entry / SL / TP coherente con plan E1
- Match galería: BTC-xx-xx-xx

### Red flags
- ...
```

---

## Limitaciones

1. **El modelo neural aprende de screenshots históricos** — no del precio en vivo directamente.
2. **OCR es opcional** — usar `super_high_entry.md` para precios exactos.
3. **La captura debe mostrar entry/SL/TP** — sin líneas dibujadas el análisis pierde precisión.
4. **Super High no sustituye** confirmación manual en TradingView ni las 8 reglas inmutables.
5. **Confirmar siempre con tu plan** antes de ejecutar en cuenta real.

---

## Comparativa vs High

| Aspecto | High | Super High |
|---------|------|------------|
| Chart fuente | Auto-generado (`btc_m5_chart.png`) | **Captura usuario TV** |
| Entry/SL/TP | Sugerido por script | **Dibujado por trader** |
| Neural | Similitud chart auto | Similitud **tu setup** |
| Probabilidad éxito | Rules + ML + Neural separados | **Combinada ponderada** |
| Cuándo | Rutina 4× / ambigüedad CRT | **Pre-ejecución con plan listo** |
| Tokens | ~1 769 | ~2 100 |

---

## Referencias

| Archivo | Uso |
|---------|-----|
| `live/super_high_entry.png` | Captura TradingView (input) |
| `live/super_high_entry.md` | Notas manuales opcionales |
| `live/btc_super_high_signal.md` | Output analizado |
| `TRADING_LIVE_BTC_HIGH_SIGNAL.md` | Base CRT + ML + Neural |
| `../strategy/TRADING_OPERATIONS_DESKTOP_CONTEXT.md` | Patrones WIN §5.1 |
| `app/services/learning/training neuronal/TRADING_NEURAL_DESKTOP_ANALYSIS.md` | Protocolo neural |

---

*Super High > High > Full > Light en profundidad pre-ejecución. Requiere captura usuario.*
