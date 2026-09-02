# Trading Indicators Rules — Danilo (Legacy Pro Plan)

> Archivo de contexto para Cursor AI. Define cómo usar los **5 indicadores favoritos** de TradingView dentro del plan E1/E2.
> Complementa `TRADING_STRATEGY_CONTEXT.md` y `TRADING_VISUAL_CONTEXT.md`.
> **Referencia visual:** `images/Indicadores legacy pro plan.png`
> **Última actualización:** 2026-08-28

---

## 1. Propósito

Este documento permite que Cursor:

- **No trate indicadores como señales automáticas** — son capas de contexto sobre el plan existente.
- **Priorice CRT + RSI TORYS** (marcados en verde en la captura) como núcleo del stack.
- **Valide setups E1** cruzando: sesgo HTF (CRT), zona de reacción, confirmación M5 (2 velas), R:R 1:2.
- **Rechace entradas** cuando un indicador contradice macro H1, PDH/PDL o las 8 reglas inmutables.
- **Etiquete confluencias** en Notion con el lenguaje del plan (`Continuación`, `Macro tendencia`, `Resistencia débil`, etc.).

**Regla madre:** Los indicadores **refuerzan** el edge E1 (PF 4.77). Nunca sustituyen zona + 2 velas M5 + SL fijo.

---

## 2. Stack de indicadores — resumen

| # | Indicador | Autor | Boosts | Función principal | Rol E1 / E2 | Prioridad |
|---|-----------|-------|--------|-------------------|-------------|-----------|
| 1 | **CRT MTF + HTF Candles** | Milana Trades (MilanaArsenovna) | 5.3 K | Visualiza velas HTF, CRT pending/completed/invalid, PDH/PDL, FVG, equilibrio 0.5 | **E1:** sesgo macro + timing de continuación en zona débil. **E2:** lectura de fakeout / turtle soup en PDH/PDL | **★★★ NÚCLEO** (verde) |
| 2 | Machine Learning Adaptive DMI Signals | AlgoAlpha | 1.7 K | DMI adaptativo (+DI/-DI), flips ▲/▼, nube direccional, ADX | **E1:** filtro de momentum intradía — alineación con bias CRT. **E2:** no usar como trigger de reversión | ★★ Soporte |
| 3 | **RSI Divergence [TORYS]** | matsu_bitmex | 6.2 K | Divergencias RSI (fondo verde = sesgo alcista, rojo = bajista), BB opcionales | **E1:** confirmación/filtro en zona — **nunca entrada sola**. **E2:** advertencia de agotamiento en macro | **★★★ NÚCLEO** (verde) |
| 4 | Swing High/Low & HigherLow/LowerHigh | matsu_bitmex | 4.4 K | Estructura Dow: swing H/L, HL/LH, fondo verde/rojo por ruptura | **E1:** ubicar SL bajo swing low / sobre swing high, validar continuación. **E2:** identificar barrido de liquidez | ★★ Soporte |
| 5 | Swing Profile [BigBeluga] | BigBeluga (EP) | 11.9 K | Volume profile anclado a cada swing leg, PoC, delta buy/sell | **E1:** confluencia en PoC + zona morada. **E2:** volumen en pool de liquidez macro | ★★ Soporte (invite-only) |

---

## 3. CRT MTF + HTF Candles — Milana Trades (detalle)

### 3.1 Qué hace

Herramienta educativa de **Candle Range Theory (CRT)** que superpone en M5:

- **Velas HTF** (1H, 4H, Daily configurables) con cuerpo, mechas, timers y etiquetas.
- **Tres estados CRT:**
  - *Pending:* precio rompe high/low de vela HTF previa → posible liquidity grab.
  - *Completed:* precio alcanza el lado opuesto del rango roto → CRT cumplido.
  - *Invalid:* cierre fuera del rango HTF antes de completar → ruptura fallida / posible reversión.
- **Niveles clave:** swing sweep, FVG/volume imbalance, línea de **equilibrio (0.5 / midpoint)**.
- **Filtro 50%:** rechazo fuerte si el cierre no supera la mitad del rango (útil para calidad de setup).

### 3.2 Alineación con tu CRT / PDH-PDL (E1)

Cruzar siempre con la lectura visual de `TRADING_VISUAL_CONTEXT.md` §1.1:

| Lectura CRT (PDH/PDL) | Acción E1 |
|----------------------|-----------|
| Precio **dentro** del rango día anterior | **NEUTRAL** — no forzar dirección; esperar pending CRT en HTF |
| **Cierre > PDH** | Sesgo **alcista** — buscar longs en pullback a soporte débil |
| **Cierre < PDL** | Sesgo **bajista** — buscar shorts en rechazo en resistencia débil |
| **Fakeout PDH** (wick arriba, cierre abajo) | **No long E1** — posible trampa; CRT invalid bearish |
| **Fakeout PDL** (wick abajo, cierre arriba) | Contexto **E2** (turtle soup), no scalping E1 |

### 3.3 Configuración recomendada (M5, sesión NY)

| Parámetro | Valor sugerido | Motivo |
|-----------|----------------|--------|
| HTF principal | **1H** (+ Daily opcional) | Alineado con macro H1 del plan |
| HTF secundario | 4H (opcional) | Contexto mensual/semanal sin ruido |
| Mostrar | Pending + Completed + Invalid | Filtrar entradas en CRT inválido |
| Equilibrio 0.5 | **ON** | Entradas E1 en discount/premium dentro del rango HTF |
| FVG / imbalance | ON en zonas de quiebre | Confluencia con rectángulo de path |
| Timer HTF | ON | Saber cuándo cierra vela H1 antes de entrar |

### 3.4 Reglas de uso — CRT

**Usar cuando:**

- Sesión **NY** activa y operas **solo E1**.
- Tendencia H1 clara + CRT **completed** o **pending** alineado con bias.
- Entrada en zona débil (banda morada / pool) **después** de manipulación (sweep) visible en CRT.
- Precio en **discount** (long) o **premium** (short) respecto al 0.5 de la vela HTF activa.
- Setup similar a galería WIN en Notion.

**NO usar / NO entrar cuando:**

- CRT marcado como **invalid** y quieres continuar en la misma dirección del pending fallido.
- Precio en **NEUTRAL** (dentro PDH-PDL) sin pending claro — evitar lateralidad micro.
- VIX > 16 y S/R débiles no se respetan — CRT da contexto pero no override de volatilidad.
- Post **2 SL** del día — indicador irrelevante, sesión terminada.
- Quieres “forzar” un long porque el timer HTF está por cerrar — **esperar cierre + 2 velas M5**.

### 3.5 Confluencias mínimas CRT + E1

Para setup **A+** (alineado con kit final):

1. Bias H1 + CRT HTF **misma dirección**.
2. Zona de reacción (morada / S-R débil) tocada o barrida.
3. CRT pending → completed **o** rechazo en 0.5 con filtro 50%.
4. **2 velas M5** de confirmación a favor.
5. R:R ≥ **1:2**, SL ~$9 fijo bajo/ sobre estructura swing.

---

## 4. RSI Divergence [TORYS] — matsu_bitmex (detalle)

### 4.1 Qué hace

Indicador legacy (2019) que detecta **divergencias RSI** usando pivots en high/low:

- **Fondo verde:** sugerencia de momentum alcista (precio lower low, RSI higher low — divergencia bullish regular; o contexto de recuperación).
- **Fondo rojo:** sugerencia de momentum bajista (precio higher high, RSI lower high — divergencia bearish regular).
- Extras: Bollinger Bands sobre RSI, alertas RSI BB Cross.

### 4.2 Rol en el plan — FILTRO, NO ENTRADA

| Regla | Detalle |
|-------|---------|
| **Nunca** | Entrar solo porque apareció fondo verde/rojo |
| **Sí — E1 long** | Fondo **verde** + pullback a soporte débil + bias CRT alcista + 2 velas M5 alcistas |
| **Sí — E1 short** | Fondo **rojo** + rechazo en resistencia débil + bias CRT bajista + 2 velas M5 bajistas |
| **Contra-señal** | Divergencia bearish (rojo) en resistencia mientras buscas long E1 → **skip** |
| **E2 ocasional** | Divergencia en PDH/PDL o pool macro puede **advertir** agotamiento — requiere checklist E2 completo |

### 4.3 Reglas de uso — RSI TORYS

**Usar cuando:**

- Ya tienes zona de reacción marcada (rectángulo / banda morada).
- Divergencia **coincide** con dirección del trade planeado (hidden divergence = continuación favorable).
- Timeframe operativo **M5**; RSI en panel inferior, no sustituye lectura de velas.
- Quieres confluencia extra para setups A+ o tras 1 SL (solo A+ restantes).

**NO usar cuando:**

- Divergencia **contradice** bias H1/CRT — ignorar o esperar invalidación.
- Mercado lateral micro — RSI diverge constantemente, genera ruido.
- Como único criterio de entrada — viola regla “Sin confirmación” de fallas primarias.
- En **E2** como gatillo único de turtle soup — requiere pool + barrido + estructura macro.

### 4.4 Confluencias RSI + E1

| Confluencia Notion | Cuándo marcar |
|--------------------|---------------|
| `Continuación` | Hidden divergencia a favor + CRT completed |
| `Resistencia débil` / `Soporte débil` | Divergencia regular en zona débil |
| `Macro tendencia` | Solo si H1 y CRT alineados — RSI es micro |
| `Pre-Entrada` | Divergencia visible pero faltan 2 velas M5 — esperar |

---

## 5. Reglas por indicador de soporte

### 5.1 Machine Learning Adaptive DMI — AlgoAlpha

**Función:** DMI con longitud adaptativa (ML selecciona el mejor lookback según performance reciente). Muestra +DI/-DI, flips ▲/▼, nube de control direccional y ADX.

| Usar | No usar |
|------|---------|
| Confirmar que +DI > -DI en longs E1 (y viceversa en shorts) | Entrar en cada flip ▲/▼ sin zona |
| Tras CRT bias definido — DMI a favor refuerza | DMI contra CRT/H1 — **no operar** |
| ADX alto = tendencia; ADX bajo = reducir tamaño o skip | Como reemplazo de 2 velas M5 |

**Rol E1:** 3.er filtro opcional después de CRT + zona.  
**Rol E2:** Solo contexto; reversión macro se lee con pools/PDH-PDL, no con flip DMI.

---

### 5.2 Swing High/Low & HigherLow/LowerHigh — matsu_bitmex

**Función:** Marca swing highs/lows y estructura Dow (HL, LH). Fondo verde si high rompe swing high; rojo si low rompe swing low.

| Usar | No usar |
|------|---------|
| Colocar SL bajo último **swing low** (long) o sobre **swing high** (short) | Cambiar SL si nuevo swing se forma en contra |
| Validar **Higher Low** en pullback long E1 | Entrar solo porque el fondo cambió a verde |
| Identificar **Lower High** en rechazo short E1 | Offset ≠ Swing Length (debe ser igual para precisión) |

**Config:** `Swing High/Low Length` = `Offset` (ej. 3 en M5). El swing confirma tras N velas cerradas.

**Rol E1:** Ancla estructural para SL $9 y lectura de continuación Dow.  
**Rol E2:** LH/LL en macro pueden marcar inicio de turtle soup — solo con checklist E2.

---

### 5.3 Swing Profile [BigBeluga]

**Función:** Volume profile por **leg de swing** (no por sesión fija). PoC, delta buy/sell %, bins adaptativos ATR. **Invite-only** (suscripción BigBeluga).

| Usar | No usar |
|------|---------|
| PoC de swing anterior como zona de reacción (+ banda morada) | PoC como entrada sin confirmación M5 |
| Delta positivo fuerte en swing alcista = continuación E1 más limpia | Delta negativo en rally — sospechar distribución, reducir confianza |
| Confluencia cuando precio retestea PoC + CRT 0.5 | Depender del indicador sin suscripción activa |

**Rol E1:** Confluencia de volumen en zonas ya marcadas.  
**Rol E2:** Volumen en barrido de pool macro — soporte analítico, no trigger.

---

## 6. Integración con el kit operativo existente

### 6.1 Flujo de decisión E1 (orden de lectura)

```
1. Sesión NY + activo único (BTC o US30) + < 3 ops + < 2 SL
2. CRT / PDH-PDL → bias macro (NEUTRAL / BULL / BEAR)
3. Vela HTF 1H → pending / completed / invalid
4. Zona de reacción (morada, pool, S-R débil, PoC opcional)
5. Swing H/L → ancla SL
6. RSI TORYS → filtro a favor (no contra)
7. DMI AlgoAlpha → momentum alineado (opcional A+)
8. 2 velas M5 confirmación
9. R:R ≥ 1:2, SL ~$9, BE en 1:1
```

### 6.2 Las 8 reglas inmutables + indicadores

| Regla kit | Cómo ayudan los indicadores |
|-----------|----------------------------|
| Solo E1 (90%+) | CRT + swings confirman **continuación**, no reversión macro |
| Sesión NY | Usar timer/sesión CRT si está disponible; macro window NY AM prioritario |
| SL ~$9 fijo | Swing H/L define el punto técnico; no expandir si CRT invalida |
| R:R 1:2 | Calcular antes; PoC puede ser target parcial, no excusa para R:R bajo |
| Máx. 3 ops/día | Más indicadores ≠ más trades — mismos límites |
| 2 SL = fin | Apagar pantalla; indicadores no reactivan sesión |
| BE en 1:1 | Independiente de flips DMI o nuevas divergencias RSI |
| Rules >70% | Si operaste sin CRT bias claro → cuenta como rule rota |

### 6.3 Checklist pre-trade — add-ons de indicadores

Añadir a los 30 seg de `TRADING_VISUAL_CONTEXT.md` §5.1:

- [ ] **CRT HTF:** bias 1H/Daily definido (no NEUTRAL forzado)
- [ ] **CRT estado:** no entrar contra CRT **invalid** reciente
- [ ] **0.5 / discount-premium:** long en discount, short en premium (cuando aplique)
- [ ] **RSI TORYS:** divergencia **a favor** o ausente — nunca en contra
- [ ] **Swing H/L:** SL colocado bajo/sobre swing confirmado
- [ ] **DMI (opcional A+):** +DI/-DI alineado con dirección
- [ ] **Swing Profile (si activo):** PoC no contradice zona de entrada
- [ ] Rectángulo path + **2 velas M5** — sin esto, indicadores no cuentan

### 6.4 Registro en Notion

Campos existentes + notas sugeridas en `Justificación del trade`:

- `CTR (H1) aplicado` → marcar cuando CRT HTF 1H estuvo alineado.
- Confluencias: añadir `Continuación` + `Macro tendencia` si CRT completed + H1.
- En capturas: incluir panel RSI TORYS y overlay CRT en HTF/LTF del diario.

---

## 7. Orden del stack en TradingView (M5)

De **arriba hacia abajo** en el gráfico principal (precio):

| Capa | Indicador | Panel |
|------|-----------|-------|
| 1 (fondo) | Swing Profile [BigBeluga] | Gráfico principal — perfiles laterales por swing |
| 2 | **CRT MTF + HTF Candles** | Gráfico principal — velas HTF, líneas CRT, FVG, 0.5 |
| 3 | Swing High/Low & HL/LH | Gráfico principal — etiquetas swing, fondo verde/rojo suave |
| 4 | Machine Learning Adaptive DMI | Panel inferior **o** overlay compacto bajo precio |
| 5 | **RSI Divergence [TORYS]** | **Panel inferior separado** (oscilador) |

**Notas de layout:**

- Máximo **1** gráfico activo (BTC **o** US30).
- Timeframe operativo fijo: **M5**; no cambiar TF para “ver señal” en otro marco.
- Bandas moradas / rectángulos manuales del plan van **encima** del perfil BigBeluga.
- Si el chart satura, ocultar DMI antes que CRT o RSI TORYS.

---

## 8. Matriz rápida E1 — indicador → acción

| Escenario E1 | CRT | RSI TORYS | Swing | DMI | BigBeluga |
|--------------|-----|-----------|-------|-----|-----------|
| Long pullback soporte | Bull bias + discount 0.5 | Verde o neutro | HL confirmado | +DI > -DI | PoC en soporte |
| Short rechazo resistencia | Bear bias + premium 0.5 | Rojo o neutro | LH confirmado | -DI > +DI | PoC en resistencia |
| CRT invalid recién formado | **Esperar** | Ignorar hasta nueva estructura | — | — | — |
| NEUTRAL PDH-PDL | Solo observar pending | No forzar | — | — | — |
| 1 SL en el día | Solo setup A+ | Obligatorio a favor | SL extra tight | Alineado | Opcional |

---

## 9. Errores frecuentes con indicadores (evitar)

| Error | Etiqueta Notion probable | Corrección |
|-------|--------------------------|------------|
| Entrar por flip DMI sin zona | `Sin confirmación` / `FOMO` | Volver a checklist §6.3 |
| Long con RSI rojo en resistencia | `Contratendencia` | Skip o esperar invalidación |
| Ignorar CRT invalid | `Mal plan aplicado` | No continuar en dirección del pending fallido |
| SL bajo swing no confirmado | `SL-Extendido` | Igualar Offset = Length en swings |
| Más indicadores tras 2 SL | `Venganza` | Fin de sesión — regla 6 kit |
| Usar divergencia como entrada única | `Sin confirmación` | Exigir 2 velas M5 + zona |

---

## 10. Cómo debe usar Cursor este archivo

1. **Validar trade propuesto:** recorrer flujo §6.1; si falla paso 2 o 6, rechazar o degradar a “observar”.
2. **Analizar captura:** identificar CRT (pending/completed/invalid), color RSI TORYS, swings para SL.
3. **Registrar en Notion:** CTR (H1), confluencias, mencionar indicadores usados en justificación.
4. **Si proponen indicador como señal única:** citar §4.2 y reglas duras de `TRADING_STRATEGY_CONTEXT.md` §12.
5. **E2:** indicadores de reversión (RSI en macro, CRT fakeout) solo con checklist 6 puntos §7 de visual context.

---

## 11. Referencias

| Recurso | URL / ruta |
|---------|------------|
| Captura favoritos Pro | `images/Indicadores legacy pro plan.png` |
| CRT MTF + HTF Candles | [TradingView — Milana Trades](https://www.tradingview.com/script/OeK1Ts7p-CRT-MTF-HTF-Candles-Milana-Trades/) |
| RSI Divergence [TORYS] | [TradingView — matsu_bitmex](https://www.tradingview.com/script/UGBig8fU/) |
| Swing HL/LH | [TradingView — matsu_bitmex](https://www.tradingview.com/script/eROt0bWE/) |
| Adaptive DMI | [TradingView — AlgoAlpha](https://www.tradingview.com/script/579yGfFJ-Machine-Learning-Adaptive-DMI-Signals-AlgoAlpha/) |
| Swing Profile | [TradingView — BigBeluga](https://www.tradingview.com/script/gFlv7t7R-Swing-Profile-BigBeluga/) |
| Plan estratégico | `TRADING_STRATEGY_CONTEXT.md` |
| Contexto visual E1/E2 | `TRADING_VISUAL_CONTEXT.md` |

---

*Generado para uso con Cursor. Los indicadores marcados en verde (CRT MTF + HTF Candles, RSI Divergence TORYS) son el núcleo del Legacy Pro Plan; el resto es soporte estructural y de volumen.*
