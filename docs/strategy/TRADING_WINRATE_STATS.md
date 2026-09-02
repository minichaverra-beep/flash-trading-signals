# Estadísticas de Win Rate — Trading

**Fecha de análisis:** 2026-08-28  
**Alcance:** BTC, US30 — Estrategias E1 (Continuación) y E2 (Reversión)

---

## Metodología

Este documento consolida el análisis de win rate (WR) a partir de tres fuentes de datos:

| Fuente | Descripción |
|--------|-------------|
| **Notion — Historial de Trades** | Registro principal con 349 trades (excluyendo fila template). Clasificación E1/E2 mediante proxy de confluencias. |
| **Desktop (abr–ago 2026)** | Trades cerrados en plataforma desktop durante el período más reciente. |
| **Visual Context (9 meses)** | Análisis visual de operaciones en los últimos 9 meses. |

**Definiciones:**
- **WIN:** Operación cerrada en ganancia.
- **LOSS:** Operación cerrada en pérdida.
- **BE:** Break-even (sin resultado).
- **WR (Win Rate):** `WIN / (WIN + LOSS) × 100` — excluye BE del denominador.
- **E1 (Continuación):** Estrategia de continuación de tendencia.
- **E2 (Reversión):** Estrategia de reversión / contra-tendencia.
- **Proxy Confluencias:** Clasificación E1/E2 inferida a partir de las confluencias registradas en Notion cuando no hay etiqueta explícita de estrategia.

---

## Resumen Global — Notion

![Win Rate Global y por Activo](images/winrate/winrate-global.png)

![KPI Dashboard Consolidado](images/winrate/winrate-kpi-dashboard.png)

| Métrica | Valor |
|---------|-------|
| WIN | 234 |
| LOSS | 115 |
| BE | 0 |
| **Total** | **349** |
| **Win Rate** | **67.0%** |

### Por Activo

| Activo | WIN | LOSS | Total | WR |
|--------|-----|------|-------|-----|
| BTC | 49 | 22 | 71 | 69.0% |
| US30 | 51 | 28 | 79 | 64.6% |
| BTC+US30 | 100 | 50 | 150 | 66.7% |

### Período Reciente (jul 2025+)

| Métrica | Valor |
|---------|-------|
| WIN | 208 |
| LOSS | 107 |
| Total | 315 |
| **Win Rate** | **66.0%** |

---

## E1 vs E2 — Proxy por Confluencias

![Win Rate E1 vs E2](images/winrate/winrate-estrategia.png)

![E1 vs E2 — PF y P&L (9 meses)](images/winrate/winrate-e1-e2-pf.png)

| Estrategia | WIN | LOSS | Total | WR |
|------------|-----|------|-------|-----|
| Continuación (E1) | 129 | 43 | 172 | **75.0%** |
| Reversión (E2) | 70 | 41 | 111 | 63.1% |
| E2 BTC | 11 | 7 | 18 | 61.1% |
| E2 US30 | 14 | 15 | 29 | 48.3% |

---

## Comparación entre Fuentes

![Comparación de Fuentes](images/winrate/winrate-fuentes.png)

![WR Mensual Desktop 2026](images/winrate/winrate-desktop-mensual.png)

![PF y P&L Mensual — 9 meses](images/winrate/winrate-pf-mensual.png)

| Fuente | Período | WIN | LOSS | Total | WR | Notas |
|--------|---------|-----|------|-------|-----|-------|
| Notion (global) | Histórico | 234 | 115 | 349 | 67.0% | Excl. template |
| Notion (reciente) | Jul 2025+ | 208 | 107 | 315 | 66.0% | — |
| Desktop | Abr–Ago 2026 | 74 | 30 | 104 | **71.2%** | Trades cerrados |
| Visual Context | 9 meses | — | — | 272 | 65.1% | All trades |
| Visual Context | 9 meses | — | — | — | **73.1%** | Solo E1 |

---

## Conclusión Ejecutiva

1. **Win rate global sólido (~67%):** Con 349 trades en Notion, el WR del 67.0% demuestra consistencia estadísticamente significativa. El período reciente (jul 2025+, 66.0%) confirma que el rendimiento se mantiene estable.

2. **E1 supera claramente a E2:** La estrategia de Continuación (E1) alcanza un 75.0% de WR frente al 63.1% de Reversión (E2). La brecha es especialmente marcada en US30 (E2 US30: 48.3%), sugiriendo que las reversiones en índices requieren filtros adicionales.

3. **BTC ligeramente superior a US30:** BTC muestra 69.0% vs 64.6% en US30, aunque ambos activos mantienen WR por encima del 60%.

4. **Consistencia entre fuentes:** Desktop (**71.2%**), Notion (67.0%) y Visual Context (65.1%–73.1%) convergen en un rango de WR entre 65% y 73%, validando la robustez del sistema.

5. **Recomendación operativa:** Priorizar setups E1 (Continuación), especialmente en BTC. Reducir exposición a E2 en US30 o aplicar confluencias más estrictas para reversiones en índices.

---

## Archivos de Contexto Relacionados

| Archivo | Contenido |
|---------|-----------|
| [TRADING_STRATEGY_CONTEXT.md](TRADING_STRATEGY_CONTEXT.md) | Definición de estrategias E1/E2, reglas de entrada y gestión |
| [TRADING_OPERATIONS_DESKTOP_CONTEXT.md](TRADING_OPERATIONS_DESKTOP_CONTEXT.md) | Detalle de operaciones Desktop (abr–ago 2026) |
| [TRADING_VISUAL_CONTEXT.md](TRADING_VISUAL_CONTEXT.md) | Análisis visual de 9 meses de operaciones |
| [TRADING_INDICATORS_RULES.md](TRADING_INDICATORS_RULES.md) | Reglas de uso de indicadores TradingView (CRT MTF, RSI TORYS, stack Legacy Pro) |
| [TRADING_PROFESSIONAL_STATS.md](TRADING_PROFESSIONAL_STATS.md) | **Informe KPI consolidado** — PF, expectativa, benchmarks, WR mensual |

---

*Generado automáticamente — 2026-08-31 · Gráficos: `python generate_winrate_images.py`*
