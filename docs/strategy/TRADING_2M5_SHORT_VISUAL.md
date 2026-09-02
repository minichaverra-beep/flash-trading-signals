# Guía visual — 2 velas M5 SHORT confirmadas (BTC M5 live)

> **Datos live:** 2026-09-02 **14:20 UTC** · NY **10:20** · Precio **77282.01**  
> Modo: **BEARISH + BREAK (E1)** · Veredicto sistema: **ESPERAR SHORT**  
> Fuente: `live/btc_m5_high_signal.md` + chart generado en vivo

---

## 1. Chart M5 actual (live)

![BTC M5 chart live](live/btc_m5_chart.png)

**Chart anotado** (resistencia, 2M5, entrada óptima, SL/TP):

![BTC M5 chart anotado](live/btc_m5_chart_annotated.png)

---

## 2. Qué VER en el chart AHORA (lectura anotada)

### Las 2 últimas velas M5 (índice derecho del gráfico)

| # | UTC   | O      | H      | L      | C      | Color | Rol en setup |
|---|-------|--------|--------|--------|--------|-------|----------------|
| **Vela X** | **14:15** | 77346.8 | 77382.4 | 77239.5 | **77310.3** | **[R]** | 1ª roja reciente |
| **Vela Y** | **14:20** | 77310.3 | 77310.3 | 77282.0 | **77282.0** | **[R]** | 2ª roja reciente |

En el PNG anotado están **resaltadas en amarillo** (velas 58–59 del panel de 60).

### Zona de resistencia

| Nivel | Precio | En chart |
|-------|--------|----------|
| **resistencia_debil** (swing HH) | **77444** | Línea **morada** horizontal — pico del impulso ~13:40–14:10 |
| H1 high del rango | 77444 | Mismo techo INSIDE_RANGE H1 |
| H1 0.5 midpoint | 77029 | Referencia CRT (no es la entrada SHORT) |
| Borde zona E1 (≤0.15%) | **~77328** | Línea morada punteada — mínimo para “cerca de zona” |

**Nota:** El usuario mencionaba ~77049; eso es el **high de la vela H1 12:00**, no la resistencia operativa actual. La resistencia SHORT operativa del sistema es **77444**.

### Tabla últimas 12 velas M5 (contexto)

```
13:25  O=76778.0  H=76960.0  L=76748.0  C=76881.1  [G]
13:30  O=76881.1  H=76881.1  L=76694.0  C=76774.3  [R]
13:35  O=76774.3  H=76778.0  L=76625.0  C=76720.0  [R]
13:40  O=76720.0  H=77400.6  L=76709.3  C=77381.6  [G]  ← breakout
13:45  O=77381.7  H=77443.6  L=77102.0  C=77102.0  [R]  ← tocó 77444
13:50  O=77102.0  H=77288.1  L=77100.0  C=77122.7  [G]
13:55  O=77122.7  H=77194.0  L=76996.0  C=77146.0  [G]
14:00  O=77146.0  H=77204.0  L=77010.2  C=77088.0  [R]
14:05  O=77088.0  H=77310.8  L=77068.0  C=77195.2  [G]
14:10  O=77195.2  H=77346.8  L=77182.4  C=77346.8  [G]
14:15  O=77346.8  H=77382.4  L=77239.5  C=77310.3  [R]  ← vela X
14:20  O=77310.3  H=77310.3  L=77282.0  C=77282.0  [R]  ← vela Y (AHORA)
```

### Escalera de precios (ASCII sobre niveles live)

```
77615 ─ ─ ─ ─ ─ ─ ─ ─ ─  SL estructural (+0.2% sobre 77444)
77444 ═══════════════════  RESISTENCIA débil (swing HH) — zona SHORT
77400 │    ← ENTRADA ÓPTIMA (limit en retest)
77328 │    ← borde 0.15% “cerca de zona”
77310 ●    vela 14:15 [R] — 2M5 OK pero YA LEJOS al cerrar
77282 ●    vela 14:20 [R] — precio AHORA (0.21% lejos → ESPERAR)
77029 ─ ─ ─ ─ ─ ─ ─ ─ ─  H1 0.5 midpoint (CRT)
76970 ─ ─ ─ ─ ─ ─ ─ ─ ─  TP 1:2 (desde entry 77400)
```

### Qué significa “2 velas M5 SHORT confirmadas”

1. **Dos cierres M5 consecutivos rojos** (`close < open`) → **[R][R]**.
2. **En zona**: precio dentro de **≤0.15%** de `resistencia_debil` **77444**.
3. **Bias BEARISH + BREAK**: rechazo en resistencia tras impulso (no short en discount lejos del techo).

**AHORA:** tienes **[R][R]** en 14:15 + 14:20, pero el precio **ya cayó** ~162 pts lejos de 77444 (**0.21%** > 0.15%). Son 2 rojas **en el lugar equivocado** (confirmación tardía, sin retest).

---

## 3. AHORA vs ENTRADA OPTIMIZADA

| | **AHORA (14:20 UTC)** | **ENTRADA OPTIMIZADA** |
|---|------------------------|-------------------------|
| Precio | **77282** | Retest **77328–77444** |
| 2M5 SHORT | Sí (14:15 + 14:20) | **Nuevas** 2 rojas **en zona** tras retest |
| Cerca zona | ❌ 0.21% lejos | ✅ ≤0.15% de 77444 |
| Señal sistema | **ESPERAR SHORT** | **ENTRAR SHORT** (si resto checklist OK) |
| Por qué | Regla dura: *“Lejos de swing S/R débil (>0.15%)”* | CRT NEUTRAL + discount → solo short **en premium cerca del techo** |
| En TradingView | Ves 2 rojas bajando **lejos del morado 77444** | Ves precio **volver a 77400**, wick a 77444, **2 cierres rojos** sin romper SL |

### AHORA — por qué ESPERAR (no “otro ESPERAR vacío”)

- El sistema marca **2M5 SHORT: SÍ** pero **Cerca de zona: NO**.
- Entrar aquí en 77282 = short **chasing** el movimiento ya hecho; SL estructural en 77615 implica **~333 pts de riesgo** vs entry actual → R:R real peor que 1:2 con SL $9 cuenta.
- ML **30.4%** (grade C) + Neural **49%** — no compensan violar zona.

### ENTRADA OPTIMIZADA — trigger exacto en TV

> **ENTRAR SHORT cuando:** precio **retestea 77328–77444** (ideal wick 77380–77444) y **cierran 2 velas M5 rojas consecutivas** con ambos cierres **≥ 77328** y **< 77444** (rechazo, no breakout).

**Ejemplo concreto de trigger (hipotético próximo):**

| Paso | Vela UTC | Qué ver | Acción |
|------|----------|---------|--------|
| 1 | ~14:25–14:35 | Precio sube a **77350–77420**, toca zona morada | Observar |
| 2 | Vela A | Cierra **roja** cerca de 77400 | 1ª confirmación en zona |
| 3 | Vela B | Cierra **roja** debajo de A | **ENTRAR SHORT** al cierre de B (market) o limit **77400** si B confirma |

**Invalidación inmediata:** cierre M5 **> 77615** o cierre fuerte **> 77444** con volumen (breakout, no rechazo).

---

## 4. Tabla de entrada optimizada (números live)

| Campo | Valor exacto |
|-------|----------------|
| **Bias** | **BEARISH + BREAK (E1)** |
| **Zona entrada** | `resistencia_debil` **77444** · banda operativa **77328–77444** (≤0.15%) |
| **Trigger 2M5** | Entrar cuando cierren **2 rojas en zona**: vela nueva **A** + vela nueva **B** tras retest (las 14:15/14:20 **no cuentan** — ocurrieron lejos) |
| **Entry** | **Limit 77400** (retest) o **market** al cierre de la 2ª roja en zona |
| **SL estructural** | **77615** (`77444 × 1.002`) — swing high + buffer |
| **SL cuenta** | **~$9 fijo** → ajustar lotaje: riesgo $9 / distancia SL (~215 pts desde 77400) |
| **TP 1:2** | **76970** (entry 77400 − 2 × 215) |
| **R:R** | **1:2** · riesgo **215 pts** · reward **430 pts** |
| **BE** | Mover a break-even en **1:1** (~77185) |
| **Invalidación** | Cierre M5 **> 77615** o reclaim **> 77444** sin rechazo |

### Si setup actual es ESPERAR — próximo escenario válido

| Escenario | Condición | Entry | SL | TP 1:2 |
|-----------|-----------|-------|-----|--------|
| **A — Retest techo (preferido)** | Precio vuelve a 77328–77444 + 2×[R] | 77400 | 77615 | 76970 |
| **B — Falla retest 30 min** | No toca zona antes ~**14:50 UTC** | — | — | — |

**Plan B (sin 2M5 en 30 min):**

1. **Light re-scan** ~14:50 UTC: `.\scripts\analyze\analyze-btc-light.ps1` o snapshot rápido.
2. Si precio sigue **< 77328** sin retest → **skip trade #1 AM** (no perseguir).
3. Reservar energía para PM #2 solo si AM = ESPERAR y **< 2 SL**.

---

## 5. Resumen una línea

**ESPERAR → ENTRAR SHORT:** cuando el precio **reteste 77444** (cierres ≥ **77328**) y **cierren 2 velas M5 rojas nuevas en esa zona** — no las 14:15/14:20 actuales, que ya confirmaron **lejos** del techo.

---

*Generado: 2026-09-02 14:20 UTC · `TRADING_2M5_SHORT_VISUAL.md`*
