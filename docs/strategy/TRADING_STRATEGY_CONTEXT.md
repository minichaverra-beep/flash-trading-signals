# Trading Strategy Context — Danilo

> Archivo de contexto para Cursor AI. Resume el plan operativo, reglas, plantillas y estructura de la bitácora en Notion.
> **Fuente principal:** [Bitácora trading v2](https://app.notion.com/p/1ee58354488080d0af44e687146f2838)
> **Última sincronización desde Notion:** 2026-08-28
> Complementa `TRADING_VISUAL_CONTEXT.md`, `TRADING_INDICATORS_RULES.md` y el resto del stack de contexto.
> **Regla Cursor (auto-carga):** `.cursor/rules/trading.mdc` — requiere abrir esta carpeta como workspace.

---

## 1. Propósito

Este documento permite que Cursor:

- Analice trades contra el plan (no inventar reglas).
- Ayude a registrar operaciones en Notion con los campos correctos.
- Revise cumplimiento de gestión de riesgo y psicología.
- Identifique patrones de fallas recurrentes en la bitácora.

**Notion MCP:** base de datos `Historial de Trades` · data source `collection://1ee58354-4880-8163-b541-000bc30cfc14`

---

## 2. Mercados y sesión

| Regla | Detalle |
|-------|---------|
| **Activos permitidos** | **BTC** y **US30** exclusivamente |
| **Sesión** | Nueva York (Asia solo en demo) |
| **Mercados simultáneos** | Máximo **1** a la vez |
| **Re-entrada tras pérdida** | Esperar lapso significativo antes de volver al mismo mercado |
| **VIX** | Revisar dirección; ~15.94 = zona equilibrio. Si VIX > 16, volatilidad alta: no respeta S/R débiles |

---

## 3. Estrategias

### Estrategia 1 — CRT / Scalping (~70% uso)

- **Tipo:** Continuaciones de tendencia.
- **Zonas:** Soportes o resistencias **débiles**, no macro.
- **SL:** Pequeño, debajo del soporte; **no mover SL**.
- **Temporalidad operativa:** M5 (una sola TF dedicada).
- **Macro:** Tendencia H1; aplicar rectángulos en zonas de quiebre.

### Estrategia 1.1 — Jolu Day-trading

- **Tipo:** Pullbacks de continuidad si se llega tarde al quiebre.
- **SL:** Grande.

### Estrategia 2 — Turtle soup / Yos Day-trading (~30% uso)

- **Tipo:** Reversiones **macro** (turtle soup).
- **Entrada:** Donde iba a ser el SL original.
- **Zona:** Cerca del pool de liquidez.
- **SL:** Grande.

### Reglas transversales de setup

1. Solo entrar **cerca de zonas de reacción**.
2. Líneas horizontales en reversiones macro.
3. Notar movimientos repentinos a favor (acción del precio en vela actual).
4. El trade debe tener buen rango de ganancia y **zona de SL sólida**.
5. **Entrar solo si el setup se parece a la galería de operaciones ganadoras** en Notion.
6. Evitar lateralidad micro.
7. Reconocer contexto macro mensual (crypto alza / economía global alza según noticias de alto impacto).

---

## 4. Análisis y confluencias

### Checklist pre-trade

- [ ] Tendencia macro H1 revisada
- [ ] Operar solo M5
- [ ] VIX revisado (correlación inversa cuando aplique)
- [ ] Rectángulo en zona de quiebre
- [ ] Líneas horizontales en reversiones macro
- [ ] Entrada en zona de reacción
- [ ] Setup similar a galería WIN
- [ ] CTR (H1) aplicado cuando corresponda

### Confluencias válidas (multi-select en Notion)

`Continuación` · `Reversion` · `Macro tendencia` · `Micro tendencia` · `Resistencia débil` · `Soporte débil` · `Pre-Entrada` · `FakeOut` · `Pullback` · `All` · `Tope ganancia enemiga` · `Pool-liquidez` · `Pullback-Continuo`

### Dirección (premium/discount)

`En descuento` · `Pre-equilibrio` · `Premium` · `Macro-Pre-equilibrio` · `Test`

---

## 5. Gestión de riesgo

| Regla | Valor / comportamiento |
|-------|------------------------|
| **R:R objetivo** | 1:2 |
| **Riesgo por operación** | Mismo en probabilidad alta y media; máx. **10%** aunque lleve 3 días buenos |
| **Contra tendencia** | Reducir riesgo |
| **Entradas por operación** | Máx. **3** |
| **Operaciones diarias** | Máx. **3** |
| **SL** | Nunca expandir; no añadir posiciones en negativo |
| **Break-even** | Si el precio respiró suficiente en profit |
| **Meta diaria cumplida** | No arriesgar más; cerrar aunque vaya 1:1 si el mercado “suelta” ganancias que salvan el día |
| **Tope de pérdida diaria** | Definir antes de operar cuánto estás dispuesto a perder |
| **Ganancias del día** | No arriesgarlas si ya cumpliste meta |
| **Cierre semanal** | No comprometer el cierre semanal anterior |

### RISK permitido en bitácora (select)

Preferir: `0.25%` · `0.50%` · `1%` · `1.50%` · `2%`

Evitar valores extremos salvo registro histórico (ej. 10%+, 47%, etc.).

---

## 6. Psicología (~70% del éxito)

- No operar estresado, cansado ni ansioso.
- No recuperar pérdidas; no pedir revancha al mercado.
- No FOMO.
- Si quieres entrar en drawdown → **revisar reglas primero**.
- Evitar el “parásito”; escuchar solo la voz analítica.
- Calma se mantiene si no se salta >30% del capital por día.
- Si cumpliste meta diaria → **no arriesgar más**.

### Motivos de pérdida frecuentes (etiquetar en Notion)

`FOMO` · `No esperé retroceso` · `Venganza` · `Contratendencia` · `Dobleteo` · `OB-Enemigo` · `Zona-enemiga` · `Fakeout` · `SL-Extendido` · `Sobreloteo` · `Mal plan aplicado` · `Frenado CRT` · `No-SL-Macro`

### Fallas primarias (captura)

`No puse Break even` · `Pelee contra tendencia macro` · `Estaba en zona enemiga` · `Contra tendencia` · `Sin confirmación` · `Fomo noticia` · `No espere sopa tortuga` · `Resistencia macro potente` · `Falso rompimiento`

---

## 7. Guía de colores (Notion)

| Color | Significado |
|-------|-------------|
| **Rosado** | Nuevas micro-reglas que debo cumplir |
| **Resaltador rosado** | Incumplimiento de normas más frecuente de lo habitual |
| **Naranja** | Variable según volatilidad |
| **Azul** | Secciones de plan / estrategia |
| **Verde** | Aspectos positivos o estrategias |

---

## 8. Bitácora Notion — estructura

### Recursos

| Recurso | ID / URL |
|---------|----------|
| Página principal | `1ee58354-4880-80d0-af44-e687146f2838` |
| Base de datos | `Historial de Trades y Nueva fuente de datos` |
| Data source trades | `collection://1ee58354-4880-8163-b541-000bc30cfc14` |
| Plantilla por trade | `Diario por operación` |

### Campos obligatorios recomendados al registrar

| Campo | Tipo | Notas |
|-------|------|-------|
| `TRADE` | title | Nombre del trade (ej. "+40 pips") |
| `ACTIVO` | select | BTC, US30, etc. |
| `ENTRY` | select | Buy, Sell, Buy Limit, Sell Limit |
| `RESULTADO` | select | WIN, LOSS, BE |
| `Open` | date | Fecha/hora apertura |
| `Sesión` | multi_select | London, NY, ASIA |
| `Confluencias` | multi_select | Ver lista arriba |
| `Dirección` | select | Premium / descuento / etc. |
| `R:R` | select | 1:1 … 1:6 |
| `RISK` | select | % arriesgado |
| `Lotaje` | select | Tamaño de lote |
| `Tipo Cuenta` | select | Real, Fondeo 6k, Prueba, etc. |
| `Dinero` | number | Resultado en USD |
| `CTR (H1) aplicado` | checkbox | |
| `VIX correl inverso` | select | True / False / No vi |
| `VIX-D5 direction` | select | Descuento / Normal / Premium / No vi |
| `Justificación del trade` | text | |
| `Pysco análisis` | text | |
| `Motivo de perdida` | multi_select | Si LOSS |
| `Falla primaria (Vista en captura)` | multi_select | |
| `Motivo de ejecución emotiva` | multi_select | |
| `Foto` | file | Capturas HTF/LTF |

### Activos en histórico (select)

Prioridad operativa actual: **BTC**, **US30**.  
Histórico también incluye: XAU, USDJPY, SP500, EURUSD, ETH, etc.

### Vistas útiles en Notion

- **Galería:** trades WIN (referencia visual de setups válidos).
- **Rentabilidad:** gráfico donut por RESULTADO.
- **Calendario:** trades por fecha (`Open`).

---

## 9. Plantilla "Diario por operación"

Al crear un trade nuevo, la página debe incluir:

### Análisis (toggle)
- **HTF:** 4H y 1H con observaciones en callouts
- **LTF:** M5 y M1 con capturas y observaciones

### Justificación (toggle)
- Motivos: confluencias, sesión, noticias
- **PROYECCIÓN:** imagen del setup

### Entrada-Salida (toggle)
- Captura de entrada
- Captura de cierre

### Observaciones & Psycho (toggle)
- Reflexión sobre gestión y decisiones durante el trade
- Aspectos psicológicos

---

## 10. Cómo debe ayudar Cursor

### Al analizar un trade propuesto o cerrado

1. Verificar activo ∈ {BTC, US30}.
2. Verificar sesión NY (salvo demo Asia).
3. Clasificar estrategia (CRT continuación vs Turtle soup reversión).
4. Comprobar confluencias mínimas y similitud con galería WIN.
5. Validar R:R, riesgo %, máx. 3 ops/día.
6. Señalar violaciones de psicología o gestión (SL movido, FOMO, contra macro, etc.).

### Al registrar en Notion

- Usar plantilla `Diario por operación`.
- Rellenar propiedades de la BD antes del contenido narrativo.
- Etiquetar pérdidas con `Motivo de perdida` y `Falla primaria`.
- Wins con confluencias que funcionaron para alimentar la galería.

### Al revisar rendimiento

- Filtrar por ACTIVO, RESULTADO, Confluencias, Sesión, Tipo Cuenta.
- Buscar patrones en pérdidas (FOMO, contra tendencia, zona enemiga).
- Comparar win rate CRT vs Turtle soup.

---

## 11. IA TIPS (secciones en Notion)

En la bitácora existen toggles con material de referencia:

- **IA TIPS: Gestión de riesgo**
- **IA TIPS: Rentabilidad de mi plan**
- **IA TIPS: Pendiente categorizar**

Consultar Notion MCP para imágenes y detalle actualizado.

---

## 12. Reglas duras — resumen ejecutivo

```
ACTIVOS     → BTC, US30 only
SESIÓN      → New York
ESTRATEGIAS → CRT (70%) continuaciones | Turtle soup (30%) reversiones macro
TF OP       → M5 entry, H1 macro
R:R         → 1:2
MAX OPS/DÍA → 3
MAX RISK    → 10% por trade (ideal 0.25–2%)
SL          → No mover, no expandir, no promediar en negativo
PSICO       → No FOMO, no revancha, no operar cansado/ansioso
SETUP       → Debe parecerse a galería WIN + zona reacción + SL sólido
```

---

*Generado para uso con Cursor + Notion MCP. Actualizar este archivo si cambian reglas en Bitácora trading v2.*
