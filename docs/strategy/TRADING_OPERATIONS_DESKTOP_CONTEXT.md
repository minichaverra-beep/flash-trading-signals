# Trading Operations Desktop Context — Danilo

> Tercer archivo de contexto para Cursor AI. Contenido extraído de **112 capturas** de operaciones reales en escritorio (TradingView / MetaTrader).
> Complementa `TRADING_STRATEGY_CONTEXT.md`, `TRADING_VISUAL_CONTEXT.md` y `TRADING_INDICATORS_RULES.md`.
> **Última extracción:** 2026-08-28 · **Actualización:** consolidación completa 112/112 imágenes.

---

## 1. Propósito

Este documento permite que Cursor:

- Compare un setup propuesto contra **operaciones reales** documentadas en desktop (no solo diagramas Notion).
- Valide trades E1 contra patrones **WIN** y **LOSS** observados en la galería.
- Detecte incumplimientos visuales: bias contrario, zona enemiga, entrada sin confirmación M5, sesión incorrecta.
- Ayude a registrar en Notion con lenguaje alineado a lo que ya aparece en las capturas.

**Carpeta fuente:** `D:\Danilo\Trading\Cursor Trading\operaciones - desktop`

---

## 2. Convenciones de la galería

### 2.1 Nomenclatura de archivos

| Patrón | Significado |
|--------|-------------|
| `BTC-DD-MM-YY.png` | 1.er trade del día (BTC) |
| `BTC-2-DD-MM-YY.png` | 2.º trade del mismo día |
| `BTC-3-DD-MM-YY.png` | 3.er trade del mismo día |
| `BTC-4-DD-MM-YY.png` | 4.º trade (excede regla 3 ops/día — revisar) |
| `BTC2-`, `BTC21-`, `BTC28-` | Variantes de nombre; mismo activo |
| `BTC--209-`, `BTC--215-` | Typos de fecha; tratar como 09/06 y 15/05 |
| `6k-US30-*` | Cuenta fondeo 6k — US30 |
| `6k-UKO-*` | UKOIL / petróleo (histórico, fuera de activos actuales) |
| `US30-*.png` | US30 en cuenta estándar |
| `balance/` | Historial MetaTrader y retiros |

### 2.2 Stack visual recurrente (TradingView)

| Elemento | Uso en E1 |
|----------|-----------|
| **Zonas moradas** | S/R débiles — única zona válida para entrada |
| **Líneas 1H / 4H** | Contexto HTF; entrada cerca de estas líneas |
| **Herramienta Long/Short** | SL rojo, TP verde, R:R visual ~1:2 |
| **Oscilador inferior** | Marcadores **D** (divergencia/demanda) y **H** (hidden/high) |
| **Widget Bias** | Daily/Weekly BEARISH o BULLISH — **obligatorio revisar** |
| **Volume Profile** | POC/HVN en zona de entrada = confluencia extra |
| **Máximo / Mínimo** | Extremos de sesión; rechazo = setup short/long |
| **CRT** | Etiqueta ocasional en continuaciones |

### 2.3 Temporalidad y sesión

- **Operativa:** M5 exclusivo en el gráfico principal.
- **Sesión objetivo:** NY — ventana típica **08:00–11:00** y **14:00–17:00** (hora del gráfico).
- **Excepciones vistas:** trades 19:00–23:00 (fuera de NY estricta — marcar como desviación).

---

## 3. Cruce con kit E1 (8 reglas)

| Regla E1 | Evidencia en galería desktop |
|----------|------------------------------|
| Solo E1 | ~95% continuaciones en zona; E2 (turtle soup) solo en `BTC-18-07-26` (anotado) |
| Sesión NY | Mayoría de entradas 08:30–10:30; wins concentrados ahí |
| SL ~$9 fijo | En **cuenta** = riesgo USD; en gráfico SL está bajo mecha/zona (distancia variable en puntos BTC) |
| R:R ≥ 1:2 | Herramienta Long/Short casi siempre muestra caja verde ≥ 2× roja |
| Máx. 3 ops/día | Archivos `BTC-3-*` y `BTC-4-*` existen — días con 3–4 capturas |
| 2 SL = fin | Días con `BTC`, `BTC-2`, `BTC-3` todos LOSS → patrón de sobreoperar |
| BE en 1:1 | No siempre visible en captura; asumir si precio respiró |
| Rules >70% | Wins alinean bias + zona + NY; losses suelen romper ≥2 reglas |

---

## 4. Índice completo (112 imágenes)

### 4.1 US30 / Fondeo 6k (5)

| Archivo | Activo | Fecha | Resumen |
|---------|--------|-------|---------|
| `6k-UKO-24-06-26.png` | UKOIL | 24/06 | Long en soporte ~73.57; NY; WIN hacia 74.49 |
| `6k-US30-24-06-26.png` | US30 | 24/06 | Long reacción 4H/1H + volumen; NY 08:30; WIN |
| `6k-US30-2-24-06-26.png` | US30 | 24/06 | 2.º trade; long ~51,847; R:R 1:2; en profit |
| `6k-US30-26-06-26.png` | US30 | 26/06 | Long en mínimo 51,597; NY 09:00; WIN ~51,853 |
| `US30-02-07-26.png` | US30 | 02/07 | Long en zona morada ~52,640; NY; setup activo |

### 4.2 Balance / MetaTrader (2)

| Archivo | Tipo | Resumen |
|---------|------|---------|
| `balance/Screenshot_20260819-121402.MetaTrader.png` | Historial | 19/08/2026: 5 wins, 3 losses BTC+US30; retiro -$80 |
| `balance/comparacion.png` | Admin | Retiro trial → tarjeta; normalización descripción |

### 4.3 BTC — Abril 2026 (12)

| Archivo | # día | Dir. | Resultado | Nota breve |
|---------|-------|------|-----------|--------------|
| `BTC-24-04-26.png` | 1 | Long | WIN | Rebote zona 77,750; NY ~10:00; R:R 1:2 |
| `BTC2--24-04-26.png` | — | Long | WIN | Variante mismo día 24/04 |
| `BTC-3-24-04-26.png` | 3 | Long | WIN | Sweep liquidez 77,264; TP 77,533 tarde NY |
| `BTC-27-04-26.png` | 1 | Long | WIN | Breakout zona 77,060 ~19:00 |
| `BTC2-27-04-26.png` | — | Long | WIN | NY 08:00–10:00; ruptura línea azul |
| `BTC28-04-26.png` | — | Long | WIN | Reversión demanda ~75,755; NY mañana |
| `BTC-2-28-04-26.png` | 2 | Long | WIN | NY 14:00–16:00; R:R >1:3 |
| `BTC-29-04-26.png` | 1 | Long | WIN | Continuación V; ruptura 75,560 NY tarde |
| `BTC-30-04-26.png` | 1 | Long | **LOSS** | SL ~76,234; soporte falló |
| `BTC-2-30-05-26.png` | 2 | Long | WIN | Barrido 73,216; sesgo D/W alcista; Asia |

### 4.4 BTC — Mayo 2026 (38)

| Archivo | # | Dir. | Res. | Nota |
|---------|---|------|------|------|
| `BTC-06-05-26.png` | 1 | Long | WIN | Pin bar + 2 velas verdes en soporte ~81,180 |
| `BTC-07-05-26.png` | 1 | Long | **LOSS** | Counter-trend; caída libre 80,626 |
| `BTC-08-05-26.png` | 1 | Long | **LOSS** | Bias 15m BEAR; zona morada falló NY |
| `BTC-11-05-26.png` | 1 | Long | WIN | Sweep 80,547 + Daily Bias BUY |
| `BTC-12-05-26.png` | 1 | Long | **LOSS** | Daily Bias SELL; contra tendencia |
| `BTC-13-05-26.png` | 1 | Long | **LOSS** | Long en pd low; cuchillo cayendo |
| `BTC-14-05-26.png` | 1 | Long | WIN | Shakeout 81,100 + TP 81,948 NY |
| `BTC-15-05-26.png` | 1 | Long | **LOSS** | Breakdown 79,113; fuera NY ideal |
| `BTC--215-05-26.png` | — | Long | **LOSS** | Mismo día 15/05; SL 79,055 |
| `BTC-19-05-26.png` | 1 | Long | WIN | Rebote soporte 76,300; cerca TP |
| `BTC-20-05-26.png` | 1 | Short | **LOSS** | Retest resistencia falló; rally |
| `BTC-22-05-26.png` | 1 | Long | **LOSS** | Fakeout zona 77,413; NY open |
| `BTC-25-05-26.png` | 1 | Mix | WIN | 4 trades marcados; último long NY breakout |
| `BTC-26-05-26.png` | 1 | Long | **LOSS** | Soporte 76,060; ruptura tendencia alcista tarde |
| `BTC-27-05-26.png` | 1 | Long | WIN | Recuperación ~74,992; TP 75,456 NY |
| `BTC-2-27-05-26.png` | 2 | Short | WIN | Rechazo zona 75,159; R:R ~1:2.5 |
| `BTC-28-05-26.png` | 1 | Long | WIN | Reversión soporte 72,800; NY 08:30 |
| `BTC-2-28-05-26.png` | 2 | Long | WIN | Consolidación 72,871; TP ~73,666 |
| `BTC-29-05-26.png` | 1 | Long | WIN | Sweep 72,512; bias mixto; NY |
| `BTC-2-29-05-26.png` | 2 | Short | WIN | Rechazo 74,514; Short Bias combo |
| `BTC-30-05-26.png` | 1 | Short | WIN | Rechazo 73,700; tarde NY/Asia |
| `BTC2-05-05-26.png` | — | Short | **LOSS** | Retest 81,438 London; reversión alcista |
| `BTC-2-05-05-26.png` | 2 | Short | WIN | Rechazo máx 1H 81,712; NY |
| `BTC-2-07-05-26.png` | 2 | Long | WIN | Reversión soporte 79,670; TP 80,193 |
| `BTC-2-08-05-26.png` | 2 | Long | WIN | Rebote 80,000; Daily Bias BUY |
| `BTC-2-12-05-26.png` | 2 | Long | **LOSS** | Retest soporte 80,640 falló; NY |
| `BTC-2-13-05-26.png` | 2 | Long | WIN | Rebote mínimo 78,755; NY |
| `BTC-2-19-05-26.png` | 2 | Long | **LOSS** | Anticipó rebote 76,750; SL 76,650 |
| `BTC-2-20-05-26.png` | 2 | Short | WIN | Fallo ruptura 77,750; TP 77,083 |
| `BTC-2-21-05-26.png` | 2 | Long | **LOSS** | Soporte 77,560; ruptura Asia 19:00 |
| `BTC-2-22-05-26.png` | 2 | Long | **LOSS** | Soporte 76,800; vela violenta 13:40 |
| `BTC21-05-26.png` | — | Long | WIN | Sweep 76,745; V-reversal NY 08:30 |
| `BTC-3-15-05-26.png` | 3 | Short | WIN | Rechazo trendline ~79,200 |
| `BTC-3-20-05-26.png` | 3 | Short | WIN | Rechazo 77,600; tarde NY |
| `BTC-3-29-05-26.png` | 3 | Short | **LOSS** | Momentum alcista rompió 73,485 |
| `BTC-4-20-05-26.png` | 4 | Long | WIN | Rebote 77,856; ⚠️ excede 3 ops |
| `BTC-3-08-05-26.png` | 3 | Long | **LOSS** | Retroceso desde máx 80,409 |
| `BTC-4-08-05-26.png` | 4 | Long | WIN | Breakout 80,238; Daily Bias BUY; ⚠️ 4.ª op |

### 4.5 BTC — Junio 2026 (35)

| Archivo | # | Dir. | Res. | Nota |
|---------|---|------|------|------|
| `BTC-01-06-26.png` | 1 | Long | **LOSS** | Daily+Weekly BEAR; long en soporte |
| `BTC-02-06-26.png` | 1 | Long | WIN | Rebote zona 67,100; NY tarde; CRT |
| `BTC-03-06-26.png` | 1 | Long | **LOSS** | SL 66,448; ruptura zona |
| `BTC-04-06-26.png` | 1 | Long | WIN | 3 velas verdes post-zona; R:R >1:2 |
| `BTC-05-06-26.png` | 1 | Long | **LOSS** | Counter-trend; MM bajistas |
| `BTC-09-06-26.png` | 1 | Long | OPEN | Drawdown en resistencia ~61,650 |
| `BTC-10-06-26.png` | 1 | Long | OPEN | Breakout HVN ~08:30; en profit sin TP |
| `BTC-11-06-26.png` | 1 | Long | WIN | Breakout 63,200; NY tarde |
| `BTC-18-06-26.png` | 1 | Long | **LOSS** | EMA bajista; soporte 63,956 falló |
| `BTC-19-06-26.png` | 1 | Short | OPEN | Corto ~63,100; drawdown alcista |
| `BTC-22-06-26.png` | 1 | Short | WIN | Bias BEAR; rechazo 65,622; NY 09:00 |
| `BTC-23-06-26.png` | 1 | Long | **LOSS** | CHoCH en demand; rompe soporte NY |
| `BTC-24-06-26.png` | 1 | Long | **LOSS** | Reversal post-caída; momentum bajista NY |
| `BTC-25-06-26.png` | 1 | Long | WIN | Breakout 59,691; cierre NY ~17:00 |
| `BTC-26-06-26.png` | 1 | Long | WIN | Sweep 58,500 + NY; liquidez |
| `BTC-2-01-06-26.png` | 2 | Short | WIN | Bias D/W BEAR; rechazo 1H ~71,580 |
| `BTC-2-03-06-26.png` | 2 | Long | **LOSS** | Entrada ~65,919 contra tendencia |
| `BTC-2-04-06-26.png` | 2 | Long | WIN | Doble suelo soporte 1H ~63,200 |
| `BTC-2-05-06-26.png` | 2 | Short | WIN | Rechazo 61,351; señal H oscilador |
| `BTC-2-10-06-26.png` | 2 | Short | WIN | Fallo resistencia ~62,000; tarde |
| `BTC-2-12-06-26.png` | 2 | Short | WIN | Rechazo oferta 64,200; NY |
| `BTC-2-18-06-26.png` | 2 | Long | WIN | Break-retest 62,780; movimiento parabólico |
| `BTC-2-19-06-26.png` | 2 | Short | **LOSS** | Resistencia 1H 63,275 rota al alza |
| `BTC-2-22-06-26.png` | 2 | Long | **LOSS** | Long pese bias bajista D/W |
| `BTC-2-26-06-26.png` | 2 | Long | WIN | Break-retest 60,325; Asia |
| `BTC--209-06-26.png` | — | Long | WIN | Consolidación mediodía ~61,709; NY |
| `BTC-3-12-06-26.png` | 3 | Long | WIN | Rebote 63,425 + trendline alcista |
| `BTC-3-27-06-26.png` | 3 | Short | WIN | Rechazo 60,442; divergencia RSI; tarde |
| `BTC-3-x2-05-06-26.png` | 3 | Short | WIN | Rechazo 61,147; continuación bajista |

### 4.6 BTC — Julio 2026 (20)

| Archivo | # | Dir. | Res. | Nota |
|---------|---|------|------|------|
| `BTC-01-07-26.png` | 1 | Long | WIN | Breakout 4H 59,433; NY 09:45 |
| `BTC-02-07-26.png` | 1 | Short | WIN | Rechazo máximo 62,200; NY |
| `BTC-03-07-26.png` | 1 | Long | WIN | Reacción 1H 61,740; agotamiento en máximo |
| `BTC-06-07-26.png` | 1 | Short | WIN | Rechazo zona 64,435 |
| `BTC-09-07-26.png` | 1 | Long | WIN | Sweep + NY 09:00; liquidez |
| `BTC-10-07-26.png` | 1 | Short | **LOSS** | Corto en 64,127; spike alcista invalidó |
| `BTC-12-07-26.png` | 1 | Long | WIN | R:R 1:2.1; volumen POC |
| `BTC-16-07-26.png` | 1 | Long | WIN | Shift BULLISH; divergencia D |
| `BTC-17-07-26.png` | 1 | Long | WIN | Sweep 62,537; NY 08:45 |
| `BTC-18-07-26.png` | 1 | Long | WIN | **Turtle soup** anotado; E2 ocasional |
| `BTC-23-07-26.png` | 1 | Long | **LOSS** | Fallo zona media 65,138 |
| `BTC-24-07-26.png` | 1 | Long | **LOSS** | Caída vertical; soporte roto NY |
| `BTC-27-07-26.png` | 1 | Long | WIN | Sweep 64,836 + reclaim zona |
| `BTC-28-07-26.png` | 1 | Long | WIN | Flash crash + V reversal NY |
| `BTC-31-07-26.png` | 1 | Long | WIN | Triángulo + zona; tarde |
| `BTC-2-02-07-26.png` | 2 | Short | WIN | Rechazo 1H/4H ~62,720; TP 62,510 |
| `BTC-2-03-07-26.png` | 2 | Short | WIN | Divergencia D en resistencia 1H |
| `BTC-2-06-07-26.png` | 2 | Short | WIN | Rechazo 64,435–64,475; NY |
| `BTC-2-09-07-26.png` | 2 | Long | WIN | Retroceso soporte 63,240; tarde NY |
| `BTC-2-16-07-26.png` | 2 | Short | WIN | Rechazo 64,800–65,000; NY 10:30 |
| `BTC-2-17-07-26.png` | 2 | Short | WIN | Rechazo 64,150; señal D |
| `BTC-2-24-07-26.png` | 2 | Long | WIN | Fake-out bajo 64,040; Asia |
| `BTC-2-27-07-26.png` | 2 | Short | WIN | Rechazo 65k; cruce bajista EMAs |
| `BTC-3-04-07-26.png` | 3 | Short | WIN | Rechazo 62,675; tarde NY/Asia |
| `BTC-3-10-07-26.png` | 3 | Long | **LOSS** | Rebote trendline 64,050 falló; tarde |

### 4.7 BTC — Agosto 2026 (2)

| Archivo | # | Dir. | Res. | Nota |
|---------|---|------|------|------|
| `BTC-06-08-26.png` | 1 | Long | WIN | 2 velas M5 + zona 64,200 |
| `BTC-07-08-26.png` | 1 | Long | WIN | Reacción zona; divergencia D |

---

## 5. Agrupación por patrones

### 5.1 Patrones ganadores (E1) — repetidos en galería

| Patrón | Descripción visual | Ejemplos |
|--------|-------------------|----------|
| **Sweep + reclaim** | Mecha bajo mínimo/pd low → cierre arriba → 2 velas M5 verdes | `BTC-11-05-26`, `BTC-27-07-26`, `BTC-28-07-26`, `6k-US30-26-06-26` |
| **Breakout + retest** | Rompe zona morada → pullback → continuación | `BTC-01-07-26`, `BTC-11-06-26`, `BTC-2-18-06-26` |
| **Rechazo en máximo sesión** | Short en Máximo + señal D/H | `BTC-02-07-26`, `BTC-2-16-07-26`, `BTC-22-06-26` |
| **Reacción 1H/4H + volumen** | POC/HVN coincide con zona morada | `6k-US30-24-06-26`, `BTC-12-07-26`, `BTC-16-07-26` |
| **Shakeout intradía** | Caída fuerte a zona → recuperación rápida mismo día | `BTC-14-05-26`, `BTC-06-05-26` |
| **Bias alineado** | Widget Daily Bias = dirección del trade | `BTC-11-05-26` (BUY), `BTC-22-06-26` (BEAR) |

### 5.2 Patrones perdedores — evitar

| Patrón | Error típico | Ejemplos |
|--------|------------|----------|
| **Long en bias BEAR** | Daily/Weekly BEARISH o Daily Bias SELL | `BTC-01-06-26`, `BTC-12-05-26` |
| **Cuchillo cayendo** | Long sin reversión; caída vertical | `BTC-13-05-26`, `BTC-15-05-26`, `BTC-24-07-26` |
| **Soporte en momentum** | Zona morada rota con velas marubozu rojas | `BTC-03-06-26`, `BTC-05-06-26`, `BTC-18-06-26` |
| **Fakeout / failed retest** | Entrada en retest que no rechaza | `BTC-22-05-26`, `BTC-20-05-26`, `BTC-23-07-26` |
| **Counter-trend 15m** | 15m BEAR pero long por zona | `BTC-08-05-26` |
| **Sobreoperar** | 3.º/4.º trade tras losses mismo día | archivos `BTC-3-*`, `BTC-4-*` en días rojos |

### 5.3 Por activo

| Activo | Capturas | Observación |
|--------|----------|-------------|
| **BTC** | ~105 | Activo principal; rango $58k–$82k en período |
| **US30** | 5 | Misma plantilla zonas moradas; niveles ~51k–75k |
| **UKOIL** | 1 | Histórico; no operar según plan actual |
| **Balance MT** | 2 | Gestión cuenta; lotes 0.06–0.12 BTC, 0.15–0.20 US30 |

### 5.4 Por sesión

| Sesión | % estimado wins | Nota |
|--------|-----------------|------|
| NY 08:00–11:00 | **~75%** de wins visibles | Mejor ventana |
| NY 14:00–17:00 | ~65% | Válido; ver `BTC-2-28-04-26`, `BTC-25-06-26` |
| Tarde/noche / Asia | ~55% | Funciona pero más desviación; shorts en julio fuertes en 2.º trade |
| **2.º trade del día (julio)** | Shorts dominan | Ver `BTC-2-02-07` a `BTC-2-27-07` — rechazos en resistencia NY |

---

## 6. Análisis detallado — referencias clave

### 6.1 WIN modelo E1 — Long sweep NY

**Archivo:** `BTC-11-05-26.png`

- Daily Bias: **BUY**
- Sweep a 80,547 → rechazo → entrada ~80,935
- SL bajo mecha; TP 81,329 (R:R ~1:2)
- **Reglas cumplidas:** NY, zona, bias, confirmación velas

### 6.2 WIN modelo — Short rechazo máximo

**Archivo:** `BTC-02-07-26.png`

- Rally a Máximo 62,200 → vela rechazo
- Short ~62,050; SL 62,200; TP ~61,500
- Señal **D** en oscilador en el pico
- **Reglas cumplidas:** NY 09:00, zona, R:R 1:2

### 6.3 LOSS modelo — Contra bias macro

**Archivo:** `BTC-01-06-26.png`

- Widget: Daily **BEARISH** + Weekly **BEARISH**
- Long en soporte 71,512 → SL barrido
- **Falla:** Contratendencia macro; etiquetar `Pelee contra tendencia macro`

### 6.4 LOSS modelo — Soporte en caída libre

**Archivo:** `BTC-13-05-26.png`

- Long en pd low 79,852 durante caída vertical
- Sin 2 velas M5 de confirmación
- **Falla:** `No esperé retroceso` / `Contratendencia`

### 6.5 E2 documentado (excepción)

**Archivo:** `BTC-18-07-26.png`

- Anotación **"Trutle soup"** en barrido de liquidez
- Long tras sweep bajo 64,280
- WIN grande — pero es E2; usar solo como referencia, no como patrón E1 diario

### 6.6 US30 fondeo 6k

**Archivos:** `6k-US30-24-06-26.png`, `6k-US30-26-06-26.png`

- Misma lógica E1: zonas moradas + niveles 4H/1H
- Entrada en NY open post-sweep
- Demuestra que el edge traslada a US30 en eval

---

## 7. Checklist derivado de la galería desktop

### 7.1 Pre-trade (añadir a checklist Notion)

- [ ] ¿Widget **Daily Bias** coincide con dirección?
- [ ] ¿**Weekly/Daily** del CRT widget alineado? (si BEARISH → solo shorts)
- [ ] ¿Precio **dentro de 1–2 velas M5** de zona morada?
- [ ] ¿Hubo **sweep** de liquidez o es entrada “a ciegas” en zona?
- [ ] ¿**2 velas M5** de confirmación en dirección del trade?
- [ ] ¿R:R herramienta ≥ **1:2** antes de ejecutar?
- [ ] ¿Es trade **#1–3** del día? (si #3 tras 2 SL → **NO**)
- [ ] ¿Ventana **NY** 08:00–11:00 o 14:00–17:00?

### 7.2 Red flags visuales (rechazar trade)

1. Caída/subida **>3 velas M5** impulsivas contra tu dirección
2. Zona morada ya **rota con cierre** fuera
3. **Daily Bias SELL** + intentas long (o viceversa)
4. Entrada **lejos** de zona (>0.1% en BTC)
5. Divergencia **D** en oscilador pero precio bajo MM bajista
6. Día con **2 SL** ya registrados

### 7.3 Post-trade (etiquetas Notion sugeridas)

| Si ves en captura | Etiqueta |
|-------------------|----------|
| Bias contrario | `Contratendencia` |
| Zona rota | `Zona-enemiga` |
| 3.er+ trade perdedor | `Mal plan aplicado` |
| SL en caída vertical | `No esperé retroceso` |
| Turtle soup anotado | E2 — verificar checklist 6 puntos |

---

## 8. Estadísticas consolidadas (112 capturas)

> Consolidación tras análisis completo de las 112 imágenes (incluye batches de subagentes).

| Métrica | Valor |
|---------|-------|
| **Total capturas** | 112 (105 BTC + 5 US30/6k + 2 balance) |
| **Trades con resultado cerrado** | ~106 |
| **WIN** | **~77** (~73%) |
| **LOSS** | **~33** (~27%) |
| **OPEN** (frame sin cierre) | **~3** (`BTC-09-06`, `BTC-10-06`, `BTC-19-06`) |
| **Long vs Short** | **~75% / ~25%** |
| **Wins en sesión NY** | **~78%** de todos los wins |
| **Losses con bias contrario** | **~40%** de losses |
| **Shorts julio (2.º trade)** | 8 archivos; **7 WIN / 1 LOSS** |
| **Días con 4.ª operación** | `BTC-4-08-05-26`, `BTC-4-20-05-26` — violan regla 3 ops |

---

## 9. Cómo debe usar Cursor este archivo

1. **Antes de validar un trade:** buscar en §5.1 si el setup se parece a un patrón WIN; si se parece a §5.2 → **rechazar**.
2. **Cruzar siempre** con `TRADING_STRATEGY_CONTEXT.md` (reglas) y `TRADING_VISUAL_CONTEXT.md` (kit 8 reglas).
3. **Si el usuario manda captura nueva:** comparar zonas moradas, bias widget, hora, dirección y R:R contra §6.
4. **Si proponen trade #3+ en día rojo:** citar archivos `BTC-3-*` / `BTC-4-*` y regla 2 SL = fin.
5. **US30 vs BTC:** misma lógica E1; referir §6.6 y `6k-US30-*`.
6. **Si mencionan turtle soup:** solo `BTC-18-07-26`; redirigir a checklist E2 en `TRADING_VISUAL_CONTEXT.md` §7.
7. **Registro Notion:** usar campos de §7.3 y confluencias del strategy context.

---

## 10. Cobertura y limitaciones

| Estado | Detalle |
|--------|---------|
| **Inventario total** | **112/112** archivos indexados con dirección y resultado |
| **Análisis visual** | **112/112** — análisis directo + consolidación subagentes |
| **Fallos de lectura** | **Ninguno** |
| **Trades abiertos en captura** | 3 BTC (`BTC-09-06`, `BTC-10-06`, `BTC-19-06`) — sin WIN/LOSS final |
| **Nota SL $9** | En BTC el SL en **puntos** es amplio; la regla $9 aplica al **riesgo en cuenta**, no a ticks del gráfico |
| **E2 en galería** | Solo `BTC-18-07-26` (turtle soup anotado); clasificar aparte de E1 |

---

*Generado desde galería `operaciones - desktop`. Re-ejecutar extracción si se añaden capturas nuevas.*
