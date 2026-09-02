# Informe Estadístico Profesional — Plan de Trading Danilo

**Fecha de consolidación:** 2026-08-28  
**Fuentes analizadas:** 5 archivos MD del stack Cursor Trading  
**Alcance operativo:** BTC · US30 · Sesión NY · E1 (CRT/Scalping) · E2 (Turtle Soup)

---

## 1. Resumen ejecutivo

| KPI | Valor | Fuente | Interpretación |
|-----|-------|--------|----------------|
| **Win Rate global (Notion)** | **67.0%** | `TRADING_WINRATE_STATS.md` | 349 trades — muestra estadísticamente robusta (n > 300) |
| **Win Rate E1 (Continuación)** | **75.0%** | Notion (proxy confluencias) | Edge principal confirmado |
| **Win Rate E2 (Reversión)** | **63.1%** | Notion | Inferior; E2 US30 **48.3%** |
| **Profit Factor (9 meses, todo)** | **3.16** | `TRADING_VISUAL_CONTEXT.md` | Excelente (>2.0 = sistema rentable) |
| **Profit Factor (solo E1)** | **4.77** | Visual Context | Nivel profesional / eval-ready |
| **P&L neto 9 meses** | **+$2,843** | Visual Context | 272 trades |
| **P&L neto solo E1** | **+$3,287** | Visual Context | E2 restó ~$444 |
| **Day Win Rate (E1)** | **~84%** | Visual Context | Días positivos en sesión |
| **WR Desktop (abr–ago 2026)** | **71.2%** | `TRADING_OPERATIONS_DESKTOP_CONTEXT.md` | 74W / 30L / 3 OPEN |
| **Cumplimiento plan (desktop)** | **~74%** | Análisis cruce reglas | Disciplina = cuello de botella |

**Veredicto:** Sistema **estadísticamente rentable y listo para escalar E1**. El riesgo principal no es el análisis técnico, sino la **disciplina** (bias contrario, sobreoperar, sesión fuera de NY).

![KPI Dashboard](images/winrate/winrate-kpi-dashboard.png)

---

## 2. Metodología y fuentes

| # | Archivo | Rol en este informe |
|---|---------|---------------------|
| 1 | `TRADING_WINRATE_STATS.md` | WR por activo, estrategia, comparación Notion vs Desktop |
| 2 | `TRADING_VISUAL_CONTEXT.md` | PF mensual, P&L 9 meses, E1 vs E2, day win, protocolo drawdown |
| 3 | `TRADING_OPERATIONS_DESKTOP_CONTEXT.md` | 112 capturas, patrones WIN/LOSS, cumplimiento reglas, WR por mes |
| 4 | `TRADING_STRATEGY_CONTEXT.md` | Parámetros del plan (R:R, riesgo, sesión, activos) |
| 5 | `TRADING_INDICATORS_RULES.md` | Stack Legacy Pro (CRT MTF + RSI TORYS = núcleo) |

**Definiciones estándar:**

- **WR** = WIN ÷ (WIN + LOSS) × 100 — excluye BE y OPEN
- **PF (Profit Factor)** = Ganancias brutas ÷ Pérdidas brutas
- **E1** = Continuación CRT / Flopy-Scalping en zonas débiles (M5, bias H1)
- **E2** = Turtle Soup / reversión macro (SL grande, ≤10% uso objetivo)
- **Expectativa (R)** = (WR × R:R) − ((1 − WR) × 1) — asumiendo R:R fijo 1:2

---

## 3. Rendimiento por fuente de datos

### 3.1 Notion — Historial completo

| Métrica | WIN | LOSS | Total | WR |
|---------|-----|------|-------|-----|
| **Global** | 234 | 115 | 349 | **67.0%** |
| BTC | 49 | 22 | 71 | 69.0% |
| US30 | 51 | 28 | 79 | 64.6% |
| BTC + US30 | 100 | 50 | 150 | 66.7% |
| Período jul 2025+ | 208 | 107 | 315 | 66.0% |

### 3.2 Estrategia — Proxy por confluencias (Notion)

| Estrategia | WIN | LOSS | Total | WR | Expectativa @ 1:2 |
|------------|-----|------|-------|-----|-------------------|
| **E1 Continuación** | 129 | 43 | 172 | **75.0%** | **+1.25 R/trade** |
| **E2 Reversión** | 70 | 41 | 111 | 63.1% | +0.89 R/trade |
| E2 BTC | 11 | 7 | 18 | 61.1% | +0.83 R/trade |
| E2 US30 | 14 | 15 | 29 | **48.3%** | +0.45 R/trade |

### 3.3 Visual Context — 9 meses (Notion analytics)

| Escenario | Trades | WR | PF | P&L neto |
|-----------|--------|-----|-----|----------|
| E1 + E2 (todo) | 272 | 65.1% | 3.16 | +$2,843 |
| **Solo E1** | 242 | **73.1%** | **4.77** | **+$3,287** |
| E2 (30 trades) | 30 | — | — | **−$444** |

### 3.4 Desktop — Galería abr–ago 2026 (112 capturas)

| Métrica | Valor |
|---------|-------|
| Capturas indexadas | 112 (105 BTC + 5 US30/6k + 2 balance) |
| Trades cerrados | 104 (74 WIN + 30 LOSS) |
| Trades OPEN | 3 |
| **Win Rate** | **71.2%** |
| Long / Short | ~75% / ~25% |
| Wins en sesión NY | ~78% del total de wins |
| Losses con bias contrario | ~40% de losses |
| Adherencia E1 | ~95% (1 turtle soup documentado) |

### 3.5 Convergencia entre fuentes

| Fuente | Período | WR | Rango confianza |
|--------|---------|-----|-----------------|
| Notion global | Histórico | 67.0% | Referencia principal (n=349) |
| Notion reciente | Jul 2025+ | 66.0% | Estabilidad temporal |
| Visual 9m (E1) | 9 meses | 73.1% | Mejor escenario (solo continuaciones) |
| Desktop | Abr–Ago 2026 | 71.2% | Período más reciente, visual |

**Rango WR consolidado:** **65% – 75%** según estrategia y adherencia al plan.

---

## 4. Rentabilidad y profit factor

### 4.1 Evolución mensual (9 meses — Visual Context)

| Mes | Trades | WR | PF | P&L |
|-----|--------|-----|-----|------|
| Jul 2025 | 37 | 59.5% | 1.85 | +$172 |
| Ago 2025 | 44 | 63.6% | 3.40 | +$410 |
| Sep 2025 | 23 | 82.6% | 5.89 | +$384 |
| Oct 2025 | 41 | 63.4% | 2.55 | +$299 |
| Nov 2025 | 41 | 68.3% | 4.84 | +$933 |
| Dic–Mar 2026 | 86 | 62.8% | 2.51 | +$645 |
| **Total 9m** | **272** | **65.1%** | **3.16** | **+$2,843** |

**Mejor mes ($):** Noviembre +$933 (PF 4.84)  
**Mes más limpio:** Septiembre PF 5.89 (E1 PF 9.83, 11/11 wins)  
**Peor mes (aprendizaje):** Julio 2025 PF 1.85 (mezcla E2 temprana)

![PF y P&L Mensual](images/winrate/winrate-pf-mensual.png)

### 4.2 Desktop — Win Rate por mes (2026)

| Mes | WIN | LOSS | OPEN | WR | Tendencia |
|-----|-----|------|------|-----|-----------|
| Abr 2026 | 8 | 1 | 0 | **88.9%** | Arranque fuerte |
| May 2026 | 23 | 16 | 0 | **59.0%** | Peor mes — disciplina |
| Jun 2026 | 20 | 9 | 3 | **69.0%** | Recuperación parcial |
| Jul 2026 | 21 | 4 | 0 | **84.0%** | Mejor mes desktop |
| Ago 2026 | 2 | 0 | 0 | **100%** | Muestra pequeña (n=2) |

![WR Mensual Desktop](images/winrate/winrate-desktop-mensual.png)

### 4.3 Impacto de escenarios (Visual Context)

| Escenario | PF estimado | Notas |
|-----------|-------------|-------|
| Solo E1 en eval fondeo | ~4.0 | Objetivo operativo |
| E1 + E2 mezclado | ~2.57 | Arrastra rendimiento |
| E1 + gestión 85% rules | ~3.2–3.5 | Sin cambiar entradas |
| Rules < 60% | ~2.5 | London, E2, SL expandido |

---

## 5. Parámetros del plan vs evidencia

### 5.1 Kit — 8 reglas inmutables

| # | Regla | Plan | Evidencia cumplimiento | Impacto en WR |
|---|-------|------|------------------------|---------------|
| 1 | Solo E1 (90%+) | 90%+ | **~95%** desktop | Alto — E1 WR 75% vs E2 63% |
| 2 | Sesión NY | NY only | **~70–78%** trades en NY | Wins NY ~75–78% |
| 3 | SL ~$9 fijo | No expandir | ~85% (visual) | Losses ↑ si SL movido |
| 4 | R:R ≥ 1:2 | Obligatorio | ~90% en wins desktop | Base del edge |
| 5 | Máx. 3 ops/día | 3 | **~92%** — 2 días con 4.ª op | Violación → sobreoperar |
| 6 | 2 SL = fin | Hard stop | **~75%** — días BTC-3/4 en rojo | Clave psicología |
| 7 | BE en 1:1 | Si precio respira | No verificable en capturas | — |
| 8 | Rules >70% | Siempre | WR global 67–73% | PF 4.77 cuando E1 puro |

### 5.2 Gestión de riesgo (Strategy Context)

| Parámetro | Plan | Estadística / nota |
|-----------|------|-------------------|
| R:R objetivo | 1:2 | Confirmado en galería WIN |
| Riesgo ideal | 0.25% – 2% | Evitar 10%+ (histórico) |
| Riesgo máximo | 10% | Solo registro histórico |
| SL E1 | ~$9 USD cuenta | Distinto a ticks en gráfico BTC |
| Máx. ops/día | 3 | En drawdown: máx. 2 |
| Activos | BTC, US30 | UKOIL 1 captura histórica |
| VIX | >16 = S/R débiles no respetadas | Filtro cualitativo |

### 5.3 Expectativa matemática (R:R 1:2)

| WR | Expectativa por trade | Breakeven WR |
|----|----------------------|--------------|
| 67.0% (Notion global) | **+1.01 R** | 33.3% |
| 75.0% (E1 Notion) | **+1.25 R** | 33.3% |
| 71.2% (Desktop 2026) | **+1.14 R** | 33.3% |
| 73.1% (E1 visual 9m) | **+1.19 R** | 33.3% |
| 48.3% (E2 US30) | +0.45 R | Marginal — evitar |

---

## 6. Análisis de activos

| Activo | WR Notion | WR Desktop | Observación |
|--------|-----------|------------|-------------|
| **BTC** | 69.0% | ~70%+ (mayoría capturas) | Activo principal; rango $58k–$82k en período |
| **US30** | 64.6% | 4/5 wins en 6k fondeo | Misma plantilla E1; E2 US30 débil (48.3%) |
| **UKOIL** | — | 1 WIN histórico | Fuera de plan actual |

**Long vs Short (desktop):** ~75% long / ~25% short. Shorts julio 2.º trade: **7W / 1L (87.5%)** — patrón de rechazo en resistencia NY.

---

## 7. Patrones estadísticos — WIN vs LOSS

### 7.1 Patrones ganadores (frecuencia alta en desktop)

| Patrón | WR relativo | Ejemplos |
|--------|-------------|----------|
| Sweep + reclaim + 2 velas M5 | Alto | BTC-11-05-26, BTC-27-07-26 |
| Bias Daily alineado | Alto | BTC-11-05-26, BTC-22-06-26 |
| NY 08:00–11:00 | **~75%** de wins | Ventana óptima |
| Breakout + retest | Alto | BTC-01-07-26, BTC-2-18-06-26 |
| Short rechazo máximo + señal D | **87.5%** (jul) | BTC-2-02-07 a BTC-2-27-07 |

### 7.2 Patrones perdedores (causa raíz)

| Patrón | % losses aprox. | Regla rota |
|--------|-----------------|------------|
| Long con bias BEAR / Daily SELL | **~40%** | Sesgo H1 + E1 |
| Cuchillo cayendo / sin 2 velas M5 | ~25% | Confirmación |
| Sobreoperar (3.ª/4.ª op tras SL) | ~15% | Reglas 5 y 6 |
| Fuera de NY (Asia/London) | ~20% | Regla 2 |
| Fakeout / retest fallido | ~15% | Confirmación |

### 7.3 Motivos de pérdida (Strategy Context — etiquetas Notion)

Top etiquetas esperadas según evidencia desktop:

1. `Contratendencia` / `Pelee contra tendencia macro`
2. `No esperé retroceso`
3. `Mal plan aplicado` (sobreoperar)
4. `Sin confirmación`
5. `Zona-enemiga`

---

## 8. Indicadores — correlación con plan

| Indicador | Prioridad | Rol estadístico |
|-----------|-----------|-----------------|
| **CRT MTF + HTF Candles** | ★★★ Núcleo | Sesgo + timing; alinea con WR E1 |
| **RSI Divergence [TORYS]** | ★★★ Núcleo | Filtro; ~40% losses = RSI/bias contradictorio |
| DMI Adaptive (AlgoAlpha) | ★★ Soporte | Momentum A+ |
| Swing H/L (matsu) | ★★ Soporte | Ancla SL |
| Swing Profile (BigBeluga) | ★★ Soporte | PoC + volumen |

**Regla madre (indicadores):** Refuerzan edge; no sustituyen zona + 2 velas M5. PF E1 (4.77) demuestra que el setup base funciona sin sobre-indicar.

---

## 9. Psicología y drawdown (cuantificado)

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Psicología = % del éxito | ~70% | Strategy Context |
| 1 SL E1 ≈ | ~$15 | Visual Context |
| 2 SL seguidos ≈ | ~$30 | Visual Context |
| Día malo E1 promedio | ~−$15 | Visual Context |
| E2 costo 9 meses | −$444 (~13% profit) | Visual Context |
| Day win E1 | ~84% | Visual Context |
| Protocolo 2 SL | Fin sesión | 25% incumplimiento desktop |

**Impacto PF por gestión:**

| Rules compliance | PF aprox. |
|------------------|-----------|
| >70% + solo E1 | **4.77** |
| Mezcla E1/E2 | 3.16 |
| <60% (London, E2, SL expand) | **~2.5** |

---

## 10. Benchmarks profesionales

| Métrica | Tu sistema | Referencia industria | Estado |
|---------|------------|---------------------|--------|
| Win Rate | 67–75% | 50–60% típico retail | ✅ Superior |
| Profit Factor | 3.16 – 4.77 | >1.5 bueno, >2 excelente | ✅ Excelente |
| Expectativa R | +1.0 – 1.25 R | >0 rentable | ✅ Fuerte |
| Muestra (n) | 349 (Notion) | >100 significativo | ✅ Robusto |
| Day Win Rate E1 | ~84% | >60% sostenible | ✅ Muy bueno |
| Drawdown control | Protocolo 4 niveles | — | ⚠️ Mejorar cumplimiento |
| E2 US30 WR | 48.3% | >50% mínimo | ❌ Reducir / eliminar |

---

## 11. Proyecciones (modelo conservador)

Asumiendo **E1 only**, WR **75%**, R:R **1:2**, riesgo **$9/trade**:

| Trades/mes | R esperado/mes | USD esperado/mes* |
|------------|----------------|-------------------|
| 20 | +25 R | ~$225 |
| 40 | +50 R | ~$450 |
| 60 | +75 R | ~$675 |

\*Riesgo fijo $9 por trade perdedor; ganador ≈ $18.

Asumiendo **3 ops/día × 20 días = 60 trades/mes** con 75% WR:

- Wins: 45 × $18 = **+$810**
- Losses: 15 × $9 = **−$135**
- **Neto estimado: +$675/mes** (sin contar BE, comisiones, slippage)

---

## 12. Recomendaciones basadas en datos

| Prioridad | Acción | Impacto esperado |
|-----------|--------|------------------|
| 🔴 Alta | Operar **solo E1** en eval fondeo | PF ~4.0 vs 2.57 |
| 🔴 Alta | Hard stop: Daily BEAR → solo shorts | −40% losses por bias |
| 🔴 Alta | **2 SL = apagar** plataforma | Evitar mayo 59% WR |
| 🟡 Media | NY 08:00–11:00 trade #1 obligatorio | +5–10 pp WR |
| 🟡 Media | Eliminar E2 US30 (WR 48.3%) | +expectativa global |
| 🟢 Baja | Shorts 2.º trade julio como playbook | 87.5% WR documentado |
| 🟢 Baja | Regenerar stats con `generate_winrate_images.py` | Mantener Notion al día |

---

## 13. Limitaciones del análisis

1. **Notion BTC/US30 parcial:** WR global 349 incluye más activos que la tabla BTC+US30 (150).
2. **E1/E2 en Notion:** Clasificación por proxy de confluencias, no etiqueta explícita 100%.
3. **Desktop:** 112 capturas ≠ todos los trades Notion; período abr–ago 2026.
4. **BE y SL $9:** No siempre verificables en captura; riesgo en USD vs ticks BTC.
5. **P&L:** Cifras de Visual Context provienen de analytics Notion (imágenes); no re-calculadas aquí.

---

## 14. Archivos de referencia

| Archivo | Uso |
|---------|-----|
| [TRADING_WINRATE_STATS.md](TRADING_WINRATE_STATS.md) | WR detallado + gráficos |
| [TRADING_VISUAL_CONTEXT.md](TRADING_VISUAL_CONTEXT.md) | PF mensual, drawdown, academia |
| [TRADING_OPERATIONS_DESKTOP_CONTEXT.md](TRADING_OPERATIONS_DESKTOP_CONTEXT.md) | Galería 112 capturas |
| [TRADING_STRATEGY_CONTEXT.md](TRADING_STRATEGY_CONTEXT.md) | Reglas operativas |
| [TRADING_INDICATORS_RULES.md](TRADING_INDICATORS_RULES.md) | Stack TradingView |
| `images/winrate/*.png` | Gráficos WR y KPI (ver abajo) |
| `generate_winrate_images.py` | Script regeneración de gráficos |

### Gráficos disponibles (`images/winrate/`)

| Archivo | Contenido |
|---------|-----------|
| `winrate-global.png` | WR global Notion + por activo |
| `winrate-estrategia.png` | E1 vs E2 + expectativa R |
| `winrate-fuentes.png` | Comparación Notion / Desktop / Visual |
| `winrate-kpi-dashboard.png` | **KPI consolidado** + barras WR |
| `winrate-desktop-mensual.png` | WR mensual desktop 2026 |
| `winrate-pf-mensual.png` | PF y P&L mensual 9 meses |
| `winrate-e1-e2-pf.png` | Impacto E1 vs E2 en rentabilidad |

---

## 15. Dashboard KPI — una página

```
┌─────────────────────────────────────────────────────────────┐
│  PLAN TRADING DANILO — KPI CONSOLIDADO (2026-08-28)         │
├─────────────────────────────────────────────────────────────┤
│  Trades (Notion)      │ 349        │  WR Global    │ 67.0%  │
│  Trades (9 meses)     │ 272        │  PF Global    │ 3.16   │
│  Trades (E1 only)     │ 242        │  PF E1        │ 4.77   │
│  P&L 9 meses          │ +$2,843    │  P&L E1       │ +$3,287│
│  Day Win E1           │ ~84%       │  Desktop WR   │ 71.2%  │
├─────────────────────────────────────────────────────────────┤
│  E1 WR                │ 75.0%      │  E2 WR        │ 63.1%  │
│  BTC WR               │ 69.0%      │  US30 WR      │ 64.6%  │
│  E2 US30 WR           │ 48.3%      │  Expectativa  │ +1.25R │
├─────────────────────────────────────────────────────────────┤
│  Mejor mes WR (desk)  │ Jul 84%    │  Peor (desk)  │ May 59%│
│  Cumplimiento plan    │ ~74%       │  Edge         │ E1 NY  │
└─────────────────────────────────────────────────────────────┘
```

---

*Consolidado automáticamente desde el stack MD. Actualizar cuando cambien datos en Notion o se añadan capturas desktop.*
