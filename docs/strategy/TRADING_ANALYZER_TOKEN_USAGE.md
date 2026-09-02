# Consumo de tokens — Analizadores BTC M5

> Evaluación de los **4 tiers** generados por `.\scripts\analyze\analyze-btc.ps1 -All` (modo `--no-chart`) + Super High on-demand.
> Medición: **2026-09-01 15:58 UTC**
> Regenerar stats: `python measure_analyzer_tokens.py`

---

## Resumen ejecutivo

| Tier | Archivos @ en Cursor | Bytes | Líneas | Palabras | Chars | Tokens (÷4) | Tokens (×1.3) | **Costo prompt típico** |
|------|----------------------|------:|-------:|---------:|------:|------------:|--------------:|------------------------:|
| **Light** | `live/btc_m5_signal.md` + `../protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` | 8 603 | 228 | 1 379 | 8 074 | **~2 019** | **~1 793** | **Medio** |
| **Full** | `live/btc_m5_snapshot.md` + `../protocols/TRADING_LIVE_BTC_M5_ANALYSIS.md` | 18 225 | 509 | 2 943 | 17 226 | **~4 307** | **~3 826** | **Alto** |
| **High** | `live/btc_m5_high_signal.md` + `../protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` | 16 251 | 443 | 2 593 | 15 488 | **~3 872** | **~3 371** | **Alto (live)** |
| **High Advanced** | mismo + secciones A–I (`--advanced` o `-ML -Neural`) | ~22 000 | ~580 | ~3 600 | ~21 000 | **~5 250** | **~4 680** | **Muy alto** |
| **Super High** | `live/btc_super_high_signal.md` + `../protocols/TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md` | 10 574 | 322 | 1 613 | 10 032 | **~2 508** | **~2 097** | **Alto (captura usuario)** |

### Hallazgos clave

1. **Live Light** (~216 tokens) incluye ahora **Veredicto CRT + Categories + CRT resumen + red flags** (antes ~136 tokens solo veredicto compacto).
2. **Protocolo Light** creció (+CRT E1 rules) → prompt total Light ~712 tokens (antes ~426). Live solo sigue dentro del objetivo ~357 (+ margen).
3. **Full live** bajó (~589 vs ~722) al reemplazar bloque Categories duplicado por template unificado Veredicto/CRT/E1.
4. **High live** (~939 tokens) incluye template completo: Veredicto, CRT, E1, E2, galería hint + detalle extendido.

---

## Desglose por archivo

### Tier Light

| Archivo | Rol | Bytes | Líneas | Palabras | Chars | ÷4 | ×1.3 |
|---------|-----|------:|-------:|---------:|------:|---:|-----:|
| `live/btc_m5_signal.md` | Datos live | 917 | 30 | 146 | 864 | 216 | 190 |
| `../protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` | Protocolo | 2 110 | 77 | 325 | 1 986 | 496 | 422 |
| **Total prompt** | | **3 027** | **107** | **471** | **2 850** | **712** | **612** |

### Tier Full

| Archivo | Rol | Bytes | Líneas | Palabras | Chars | ÷4 | ×1.3 |
|---------|-----|------:|-------:|---------:|------:|---:|-----:|
| `live/btc_m5_snapshot.md` | Datos live | 2 492 | 81 | 428 | 2 356 | 589 | 556 |
| `../protocols/TRADING_LIVE_BTC_M5_ANALYSIS.md` | Protocolo | 6 998 | 232 | 1 043 | 6 691 | 1 673 | 1 356 |
| **Total prompt** | | **9 490** | **313** | **1 471** | **9 047** | **2 262** | **1 912** |

### Tier High

| Archivo | Rol | Bytes | Líneas | Palabras | Chars | ÷4 | ×1.3 |
|---------|-----|------:|-------:|---------:|------:|---:|-----:|
| `live/btc_m5_high_signal.md` | Datos live | 4 374 | 138 | 787 | 4 178 | 1 044 | 1 023 |
| `../protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` | Protocolo | 11 877 | 305 | 1 806 | 11 310 | 2 828 | 2 348 |
| **Total prompt** | | **16 251** | **443** | **2 593** | **15 488** | **3 872** | **3 371** |

### Tier Super High

| Archivo | Rol | Bytes | Líneas | Palabras | Chars | ÷4 | ×1.3 |
|---------|-----|------:|-------:|---------:|------:|---:|-----:|
| `live/btc_super_high_signal.md` | Datos live | 2 420 | 86 | 409 | 2 282 | 570 | 532 |
| `../protocols/TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md` | Protocolo | 8 154 | 236 | 1 204 | 7 750 | 1 938 | 1 565 |
| **Total prompt** | | **10 574** | **322** | **1 613** | **10 032** | **2 508** | **2 097** |

---

## Comparativa visual (markdown)

### Costo de prompt por tier (chars ÷ 4)

```
Light       ███████░░░░░░░░░░░░░  ~2 019 tokens
Super High  ████████████░░░░░░░░  ~2 508 tokens
High        █████████████████░░░  ~3 872 tokens
Full        ██████████████████████  ~4 307 tokens
```

### Live only (sin protocolo)

| Tier | Live file | Líneas | Tokens (÷4) | Contenido principal |
|------|-----------|-------:|------------:|---------------------|
| Light | `btc_m5_signal.md` | 30 | ~216 | Veredicto + Categories + CRT resumen + red flags |
| Full | `btc_m5_snapshot.md` | 81 | ~589 | Veredicto + CRT tabla + Checklist E1 + detalle mercado |
| High | `btc_m5_high_signal.md` | 138 | ~1 044 | Template completo + E2 + score extendido + 12 velas |
| High Advanced | `btc_m5_high_signal.md` (--advanced) | ~280 | ~1 600 | + secciones A–I: scorecard, CRT deep, ML×Neural, galería, plan |
| Super High | `btc_super_high_signal.md` | 86 | ~570 | Prob. combinada Neural+ML+Rules + captura usuario |

### Ratio vs Light live (÷4)

| Tier | Live tokens | vs Light live |
|------|------------:|--------------:|
| Light | ~216 | 1,0× |
| Full | ~589 | 2,7× |
| High | ~939 | 4,3× |

---

## Cuándo usar cada tier

| Tier | Usar cuando… | Evitar cuando… |
|------|--------------|----------------|
| **Light** | Chequeo rápido NY; Veredicto + CRT resumen auto-generado | Necesitas tablas E2, score extendido 10 ítems o 12 velas |
| **Full** | Análisis E1 estándar con Veredicto + CRT + checklist 8 reglas | Solo quieres sí/no (Light) o setup ambiguo CRT (High) |
| **High** | Análisis CRT pending/completed, Turtle Soup, galería WIN | Operación obvia A+ donde Light basta |
| **High Advanced** | Pre-decisión con ML+Neural: scorecard, cruce tensiones, plan completo | Sin modelos ML/Neural entrenados |
| **Super High** | **Pre-ejecución** con captura entry/SL/TP propia; probabilidad combinada Neural+ML+Rules | Sin captura TradingView dibujada |

---

## Referencia de comandos

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-btc.ps1 -All -NoChart
.\scripts\analyze\analyze-btc-superhigh.ps1 -ML -Neural   # on-demand si hay captura
python measure_analyzer_tokens.py
```

---

*Documento actualizado tras refactor `btc_e1_report.py` · 2026-09-01*
