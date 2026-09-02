# Trading Visual Context — Danilo (desde imágenes Notion)

> Segundo archivo de contexto para Cursor AI. Contenido transcrito y analizado de **46 imágenes** embebidas en [Bitácora trading v2](https://app.notion.com/p/1ee58354488080d0af44e687146f2838).
> Complementa `TRADING_STRATEGY_CONTEXT.md` y `TRADING_INDICATORS_RULES.md` (stack TradingView Legacy Pro). **Última extracción:** 2026-08-28.
>
> Imágenes locales: `images/bitacora-v2/` (01–46)

---

## 0. Convenciones E1 / E2

| Código | Estrategia | Uso recomendado |
|--------|------------|-----------------|
| **E1** | Flopy-Scalping / CRT — **continuaciones** en zonas débiles | **90%+** — identidad principal del trader |
| **E2** | Turtle Soup — **reversiones macro** | **≤10%** — ocasional, demo, mes favorable |

**Frase final (imagen 27):** *"Llevo 4 años construyendo. 9 meses lo prueban. E1 es mi edge. Solo ejecuto."*

---

## 1. Diagramas de estrategia (imágenes 01–02)

### 1.1 CRT — Candle Range Theory (imagen 01)

Reglas visuales con **PDH** (Previous Day High) y **PDL** (Previous Day Low):

| Escenario | Lectura |
|-----------|---------|
| Precio **dentro del rango** del día anterior | **NEUTRAL** — no forzar dirección |
| **Cierre por encima de PDH** | **BULLISH** — sesgo alcista |
| **Cierre por debajo de PDL** | **BEARISH** — sesgo bajista |
| **Ruptura fallida de PDH** (wick arriba, cierre abajo) | **BEARISH** — fakeout / liquidity grab |
| **Ruptura fallida de PDL** (wick abajo, cierre arriba) | **BULLISH** — turtle soup en mínimos |

### 1.2 Turtle Soup — E2 (imagen 02)

Setup de **reversión long** tras barrido de liquidez:

1. Precio en tendencia, forma mínimos ascendentes.
2. Rompe mínimo previo (**Turtle soup** — zona roja).
3. Revierte agresivamente hacia **Buyside liquidity** (máximo previo / BSL).
4. Entrada: donde iba a ser el SL original (cerca del pool de liquidez).

**Uso:** solo reversiones **macro**, SL grande, no mezclar con scalping E1.

---

## 2. Estadísticas y rentabilidad (imágenes 06, 13–17, 18)

### 2.1 Resumen 4 meses (imagen 06)

| Métrica | Valor |
|---------|-------|
| Profit factor total | **2.57** |
| Trades analizados | 87 |
| Win rate global | 63.2% |
| P&L neto | +$673.7 |
| Mejor mes | Diciembre (PF 4.55) |
| Peor mes | Marzo (PF 1.96) |
| PF potencial (gestión al 85%) | ~3.2–3.5 |

**Conclusión:** enero/marzo bajan por **gestión**, no por análisis. Subir gestión 60%→80% acerca PF a ~3.0+ sin cambiar entradas.

### 2.2 PF por mes — 9 meses (imagen 13)

| Mes | Trades | WR | PF | P&L |
|-----|--------|-----|-----|------|
| Jul 2025 | 37 | 59.5% | 1.85 | +$172 |
| Ago 2025 | 44 | 63.6% | 3.40 | +$410 |
| Sep 2025 | 23 | 82.6% | 5.89 | +$384 |
| Oct 2025 | 41 | 63.4% | 2.55 | +$299 |
| Nov 2025 | 41 | 68.3% | 4.84 | +$933 |
| Dic–Mar 2026 | 86 | 62.8% | 2.51 | +$645 |
| **TOTAL 9m** | **272** | **65.1%** | **3.16** | **+$2,843** |

- **Peor mes (aprendizaje):** Julio PF 1.85 — empezó mezcla E2, pérdidas -220 y -400 pips (11 jul).
- **Mejor mes ($):** Noviembre +$933 — subió lotaje.
- **Mes más limpio:** Septiembre PF 5.89 / E1 PF 9.83 — 11/11 wins.

### 2.3 E1 vs E2 — impacto en PF (imágenes 11–12, 15–16)

Excluyendo 30 trades E2 (pérdidas ≥90 pips = SL expandible):

| Métrica | Todo (E1+E2) | Solo E1 |
|---------|--------------|---------|
| Trades | 272 | 242 |
| Win rate | 65.1% | **73.1%** |
| Profit factor | 3.16 | **4.77** |
| P&L neto | +$2,843 | **+$3,287** |
| E2 (30 trades) | — | **-$444** (~13% profit) |

| Acción | PF estimado |
|--------|-------------|
| Operar solo E1 en eval fondeo | **~4.0** |
| Mezclar E1 + E2 (actual) | ~2.57 |
| E1 base + E2 ocasional (reglas estrictas) | ~3.2–3.5 |

**Decisión confirmada:** dedicarse a **E1**. E2 solo ocasiones especiales o **eliminarla en eval de fondeo**.

### 2.4 Conclusión operativa (imagen 18)

- **E1 solo** → PF ~4.77, day win ~**84%**
- **Rules >70%** → sostenible
- **Rules <60%** → PF cae a ~2.5 (mezclar E2, expandir SL, London)
- **Meta** → escalar lento, no "recuperar rápido"
- **Regla de oro:** en drawdown **bajas exposición**, no la subes

### 2.5 Veredicto honesto (imagen 17)

| Pregunta | Respuesta |
|----------|-----------|
| ¿Estadísticamente listo? | **Sí** |
| ¿Con 4 años de prep? | **Sí** |
| ¿Solo con "no sentir nada"? | **No** — necesitas reglas automáticas |
| ¿Listo hoy si operas E1 + rules al 90%? | **Sí, razonablemente** |
| ¿Listo si mezclas E2, London o 10% riesgo? | **No** |

---

## 3. Gestión de riesgo y drawdown (imágenes 03–05, 19–22)

### 3.1 Señales de venganza — cortar aquí (imagen 03)

| Señal | Lo que piensas | Realidad |
|-------|----------------|----------|
| 1 SL | "Un trade más y lo recupero" | 1 SL E1 ≈ ~$15. Dos seguidos ≈ ~$30 |
| 2 SL | "El mercado me debe" | Tu regla: **fin de sesión** |
| Día rojo | "Necesito cerrar en verde" | Día malo E1 ≈ -$15 promedio |
| Barrido | "Entro de nuevo más grande" | Eso es E2 / revancha disfrazada |
| London/NY mal | "En el próximo lo corrijo" | Cambiar sesión sin plan = FOMO |
| Ves otro moverse | "Me lo perdí, entro ya" | FOMO → lotaje alto |

**Si reconoces 2 o más → cierra plataforma 24 h.**

### 3.2 Qué evitar en drawdown (imagen 04)

**Sobreapalancamiento — NO:**
- Subir lotaje "para recuperar"
- Pasar de 0.02 a 0.04 tras un SL
- Arriesgar >1–1.5% porque "conozco el setup"

**SÍ:**
- Bajar lotaje **50%** tras 1 SL del día
- Tras 2 SL en la semana → lotaje mínimo **3 días**
- En eval fondeo: **0.75–1% max**, nunca 10%

**Venganza — NO:**
- Reentrar al mismo par en <30 min
- Tercer trade del día "porque voy 0-2"
- Cambiar de E1 a E2 "porque E1 falló"
- Operar estresado / impotente

**SÍ:**
- **2 SL = fin de sesión** (sin excepciones)
- Anotar en Notion: "¿Era A+ o revancha?"
- BackTesting al día siguiente si perdiste control

**Expandir SL — NO:**
- Mover SL porque "casi revierte"
- Convertir scalping en swing en pérdida

**SÍ:**
- Salir antes si no hay confirmación (2 velas M5)
- SL fijo E1 — si toca, aceptar y cerrar

### 3.3 Sesión y frecuencia (imagen 19, secciones 4–5)

**NO:** London porque "NY ya pasó" · 4–5 trades en drawdown · otro activo "para compensar"

**SÍ:** Solo **NY** · Máx. **3 ops/día** (en drawdown: máx. **2**) · Solo **BTC** (o US30, un mercado)

**Perseguir meta en rojo — NO:** "Solo necesito $20 más" con 2 SL encima

**SÍ:** Tope diario de pérdida **ANTES** de operar · Ejemplo cuenta 50k: **-$500/día = STOP** · Meta cumplida → no arriesgar ganancias

### 3.4 Protocolo anti-drawdown — 4 niveles (imagen 20)

| Nivel | Trigger | Acción |
|-------|---------|--------|
| **1** | 1 SL en el día | Lotaje -50% · solo setups **A+** (zona + 2 velas + R:R 1:2) · máx. 2 trades restantes |
| **2** | 2 SL en el día | **Fin de sesión** · no mirar gráficos hasta mañana · bitácora: qué rule rompiste |
| **3** | 2 días rojos en la semana | Siguiente semana: lotaje mínimo · solo E1, sin E2 · objetivo: no perder, no recuperar |
| **4** | DD >3% (eval) o >5% (cuenta propia) | Pausa **48–72 h** · revisar últimos 10 trades · volver con **1 trade/día** hasta 3 días verdes |

### 3.5 Frases de emergencia (imagen 21)

1. *"Recuperar no es mi trabajo. Ejecutar E1 es mi trabajo."*
2. *"Un día -$15 no me quiebra. Un trade de venganza a -$150 sí."*
3. *"Si subo lotaje en drawdown, le regalo el mes a E2."*
4. *"2 SL = cierro. El mercado estará mañana."*

### 3.6 Frase pre-sesión (imagen 05)

> *"No necesito sentirme bien. Necesito cumplir 5 rules: NY, E1, 1% riesgo, 3 ops máx, 2 SL = fin."*

---

## 4. Kit final — 8 reglas inmutables (imagen 26)

| # | Regla |
|---|-------|
| 1 | **Solo E1 (90%+)** |
| 2 | **Sesión NY** |
| 3 | **SL ~$9 fijo — nunca expandir** |
| 4 | **R:R mínimo 1:2** |
| 5 | **Máx. 3 ops/día** |
| 6 | **2 SL = fin de sesión** |
| 7 | **BE en 1:1** |
| 8 | **Rules >70% siempre** |

**Evidencia:** 9 meses, 272 trades, PF 4.77 E1, day win 84%, +$2,843.

---

## 5. Checklists operativos (imagen 46)

### 5.1 Pre-trade (30 seg)

- [ ] Sesión **NY**
- [ ] Solo **E1**
- [ ] **Zona de reacción** (bandas moradas / pools / S/R débil)
- [ ] **R:R ≥ 1:2**
- [ ] **SL $9 fijo**
- [ ] **< 3 ops hoy**
- [ ] **< 2 SL hoy**
- [ ] Sin ansiedad / **FOMO**

### 5.2 Post-trade (1 min)

Registrar: Fecha · E1/E2 · Rules % · Resultado $ · ¿Revancha? S/N · Lección (1 frase)

### 5.3 Revisión semanal (15 min)

Trades · WR · PF semana · Rules % · Peor error · **1 micro-regla nueva (rosado en Notion)**

---

## 6. Estrategia E1 — detalle operativo (imagen 35)

| Tema | Regla |
|------|-------|
| Definición | Continuaciones en **zonas débiles** |
| Zonas | Bandas moradas, pools, S/R débiles |
| Entrada | Solo cerca de zona + **confirmación** |
| Confirmación | **2 velas M5** + (opcional) web rusa |
| Path | Rectángulo — marcar quiebre antes de entrar |
| Long E1 | Pullback en soporte + bias alcista |
| Short E1 | Rechazo en resistencia + bias bajista |
| Caso ganador ref. | Long ~73,400 → ~73,549 |
| **Cuándo NO entrar** | Lateralidad · lejos de zona · post-2 SL |

### Patrón ganador validado (imagen 25)

| Elemento | Histórico E1 |
|----------|--------------|
| Bias alcista + pullback a soporte | Continuación E1 ✅ |
| Entrada en zona morada | "Solo en reacción" ✅ |
| SL bajo el mínimo | SL fijo, pequeño ✅ |
| Sesión / plan | Mismo framework ✅ |
| Resultado profit | WR E1 73% — esperable |

---

## 7. Estrategia E2 — reglas restrictivas (imagen 41)

| Regla | Detalle |
|-------|---------|
| Frecuencia | Máx. **1/semana**, checklist 6 puntos |
| Setup | Turtle Soup macro — pool liquidez + barrido |
| Impacto PF | Baja de 4.77 → 3.16 |
| Lección $444 | Salir antes vs expandir SL |
| **En eval fondeo** | **PROHIBIDO** hasta pasar |

---

## 8. Gestión de riesgo numérica (imagen 36)

| Tema | Valor |
|------|-------|
| SL fijo | **$9** — no expandir |
| R:R mínimo | **1:2** — calcular antes de entrar |
| Break even | Automático en **1:1** |
| Lotaje | Según capital $450–900 real/fondeo |
| Tope diario | Meta + límite de pérdida definidos antes |
| Máx ops | **3/día** |
| Calculadora | Capital + SL pts → $ riesgo (BTC / MYM) |

---

## 9. Psicología — métricas de control (imagen 29)

| Área | % dominio | Notas |
|------|-----------|-------|
| **Análisis** | 85% | Difícil de sabotear — ya dominado |
| **Psicología** | 70% | ~30% sesiones en riesgo |
| **Gestión** | 60% | Donde psicología + dinero se juntan |

**Si subes Psicología 70%→85%:**
- Rachas: 4 SL → **2 SL max**
- PF: 3.16 → **~3.8–4.0** (sin tocar entradas)
- Eval: probabilidad de pasar ↑ notablemente

**Mayor enemigo:** Psicología (70%), no análisis (85%).

---

## 10. Prop firms recomendadas (imágenes 07–10, 23)

### Kraken Prop (#1 para perfil E1, BTC, sin prisa)

| Característica | Detalle |
|----------------|---------|
| BTC | 60+ pares, BTC/ETH 5x |
| Riesgo/trade | Sin regla fija — tú eliges |
| DD diario | 3% |
| DD máximo | 3% Turbo / 5% Pro / 6% Classic |
| Tiempo límite | Ninguno |
| Split | 80–90% |
| Plan recomendado | **Classic 1-Step $10k** (~$85 fee, meta ~$1k, DD 6%) |

**Pre-eval checklist (3–7 días demo):**
1. Solo E1 — E2 apagado
2. Sesión NY
3. SL ~$9 fijo
4. Máx. 3 ops/día
5. 2 SL = fin de día
6. 2–3 días demo Kraken Pro mismas rules
7. Si cumples **>70% rules** → paga eval

**Evitar Turbo (3% DD)** al principio — barridos aprietan más.

### Comparativa rápida (imagen 10)

| Firma | BTC | Sin límite/trade | Leverage | DD máx | Confianza |
|-------|-----|------------------|----------|--------|-----------|
| Kraken Prop | ✅ | ✅ | 5x | 3–6% | ⭐⭐⭐⭐⭐ |
| HyroTrader | ✅ | ⚠️ | 100x | ~6% | ⭐⭐⭐⭐ |
| GFT | ✅ | ⚠️ | 100x | 6% | ⭐⭐⭐⭐ |
| Apex | ❌ | ❌ | Futuros | ~6% | N/A BTC |

---

## 11. Curso / Academia — estructura (imágenes 33–45)

### Módulos clave

| Módulo | Tema | Entregable |
|--------|------|------------|
| 0 | Bienvenida — PF 4.77, 272 trades, +$2,843 | Plantilla Notion vacía |
| 1 | Fundamentos — BTC/US30, NY, M5, E1 vs E2 | Checklist "¿Es E1 o E2?" |
| 2 | E1 Flopy-Scalping | Flowchart decisión entrada |
| 3 | Gestión riesgo — SL $9, R:R 1:2 | Calculadora Notion |
| 4 | Psicología drawdown | Tarjeta Protocolo drawdown |
| 5 | Bitácora y métricas | Dashboard Rentabilidad |
| 6 | Sesión NY, VIX, un mercado | Tabla horarios NY |
| 7 | Fondeo Kraken/Apex | Checklist pre-trade 30 seg |
| 8 | E2 ocasional (opcional) | Checklist E2 (6 condiciones) |
| 9 | Proyecto final | 20 trades demo E1, >70% rules |

### Estructura Notion del curso (imagen 43)

```
📁 Academia Flopy Method
├── 📄 Módulo 0-9 (páginas por lección)
├── 📊 Plantilla Bitácora (duplicable)
├── ✅ Checklists (E1, E2, pre-trade, drawdown)
├── 📈 Dashboard métricas (PF, day win, E1 vs E2)
├── 🎥 Links videos (Loom / YouTube)
└── 👥 Alumnos (BD: nombre, % rules, trades, notas)
```

### Lo que guardar para siempre (imagen 24)

1. **E1 (Flopy-Scalping)** = identidad como trader
2. **Rules >70%** = contrato contigo
3. **Bitácora** = ventaja sobre el 90% que no mide
4. **Salir antes / SL fijo** = separa PF 4.77 de 2.57
5. **Psicología** = lo único que puede romper un sistema que ya funciona

---

## 12. Índice de imágenes por sección

| # | Archivo | Sección Notion |
|---|---------|----------------|
| 01 | CRT_strategy.png | Estrategia 1 CRT |
| 02 | Turtle soup diagram | Estrategia 2 |
| 03–05 | Venganza, drawdown, frase sesión | IA TIPS — Gestión riesgo |
| 06 | PF 4 meses | IA TIPS — Rentabilidad |
| 07–12 | Prop firms, E1 vs E2 | IA TIPS — Pendiente categorizar |
| 13–17 | PF mensual, veredicto | IA TIPS — Rentabilidad |
| 18–22 | Conclusión, protocolo, frases | IA TIPS — Gestión riesgo |
| 23–26 | Kraken eval, kit final | Final Boss |
| 27–32 | Frase final, control, roadmap | Final Boss / Academia |
| 33–45 | Módulos curso 0–9 | Academia Flopy Method |
| 46 | 3 checklists | Academia — operativa diaria |

---

## 13. Cómo debe usar Cursor este archivo

1. **Antes de validar un trade:** cruzar con secciones 4, 5, 6 y kit final (§4).
2. **Tras 1 SL:** aplicar protocolo nivel 1 (§3.4).
3. **Tras 2 SL:** fin de sesión — no negociar (§3.4, §4 regla 6).
4. **Si proponen E2:** verificar checklist 6 puntos y que NO sea eval (§7).
5. **Si PF baja:** revisar rules %, mezcla E2, London, SL expandido (§2.4).
6. **Setup visual:** comparar con CRT (§1.1) o Turtle Soup (§1.2) según E1/E2.

---

*Generado automáticamente desde 46 imágenes de Bitácora trading v2. Re-sincronizar si cambias capturas en Notion.*
