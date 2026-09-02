# Rutina diaria — 4 análisis BTC M5 (NY AM + NY PM)

> Workflow operativo para **4 lecturas al día** en Cursor: **2 en la mañana NY** + **2 en la tarde NY**, cada bloque en **chat separado** para ahorrar tokens.
> Complementa `TRADING_ANALYZER_TOKEN_USAGE.md` · Estrategia auto-cargada vía `.cursor/rules/trading.mdc`
> **Última revisión:** 2026-09-01

---

## Resumen ejecutivo

| Concepto | Detalle |
|----------|---------|
| **Frecuencia** | 4 análisis / día |
| **Bloques** | NY AM (2) · NY PM (2) |
| **Chats Cursor** | **1 chat nuevo por bloque** — no reutilizar el chat del otro bloque |
| **Estrategia** | E1 CRT/scalping **90%+** · E2 Turtle Soup **≤10%** |
| **Activos** | BTC / US30 (máx. 1 a la vez) |
| **Sesión** | Nueva York — ventanas **08:00–11:00** y **14:00–17:00** (UTC-4) |
| **Riesgo** | SL ~**$9** fijo · R:R mín. **1:2** · **2 SL = fin de sesión** |
| **Tier Full** | **No** forma parte de la rutina diaria (solo excepcional / post-noticia) |

### Mix recomendado de tiers (día típico)

| Análisis | Ventana sugerida | Tier por defecto | Tokens prompt (~) |
|----------|------------------|------------------|-------------------|
| AM #1 | ~**08:30** NY | **Light** | ~357 |
| AM #2 | ~**10:00** NY | **High** *(o Light si AM #1 fue claro)* | ~1 757 / ~357 |
| PM #1 | ~**14:30** NY | **Light** | ~357 |
| PM #2 | ~**16:00** NY | **Light** | ~357 |
| **Total día (1H + 3L)** | | | **~2 830** |

Comparativa: 4× Full ≈ **~8 700** tokens — **~3× más caro** que el mix híbrido.

---

## Antes de abrir Cursor (una sola vez al día)

Ejecutar desde PowerShell **al inicio de la sesión NY** (antes del primer chat AM):

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-btc.ps1 -All -NoChart -ML -Neural
```

Esto regenera los **3 live files** (`btc_m5_signal.md`, `btc_m5_snapshot.md`, `btc_m5_high_signal.md`) sin PNG embebido en el markdown, con **ML prob** y **Neural galería** en la sección Categories de cada uno. El neural usa el mismo PNG `live/btc_m5_chart.png` (generado internamente aunque uses `-NoChart`). Luego, en cada análisis, solo corres el script del tier que necesites con `-ML -Neural` si quieres refrescar probabilidades (o vuelves a ejecutar `-All -NoChart -ML -Neural` si pasó mucho tiempo / hubo noticia).

> **Categories con ML + Neural:** al usar `-ML -Neural` / `--ml --neural`, aparecen **ML prob** y **Neural galería** junto a **Bando usado**, **Recomendación**, acción, tendencia, reglas X/8 y prob. histórica. Ambos **complementan** Rules % — no reemplazan E1 ni TradingView.

> **Bias forzado (cualquier tier):** `-Bullish` / `-Bearish` en cualquier launcher PS1 (`scripts/analyze/analyze-btc-light.ps1`, `scripts/analyze/analyze-btc-high.ps1`, `scripts/analyze/analyze-btc.ps1`, `analyze-us30-*.ps1`, `scripts/analyze/analyze-btc-superhigh.ps1`) → **Bando usado** = BULLISH/BEARISH y **Recomendación** con dirección explícita (ej. `ENTRAR SHORT`). Sin flag → **AUTO** (derivado del mercado/setup).

> **No hace falta @ `TRADING_STRATEGY_CONTEXT.md` ni otros MD de estrategia** en cada chat: la regla `.cursor/rules/trading.mdc` ya carga el plan cuando esta carpeta es el workspace.

---

## Bloque mañana — Chat **「NY AM」**

**Ventana NY:** 08:00–11:00 (UTC-4) · Mejor ventana histórica (~75% wins).

Abrir **chat nuevo** con título o contexto mental `NY AM`. No arrastrar historial del día anterior ni del bloque PM.

### AM #1 — Chequeo apertura (~08:30 NY)

| Paso | Acción |
|------|--------|
| **Tier** | **Light** |
| **Comando** | `.\scripts\analyze\analyze-btc-light.ps1 -ML -Neural` |
| **@ en Cursor** | `@live/btc_m5_signal.md` `@docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` |
| **Prompt ejemplo** | Copiar bloque **Prompt optimizado** de `../protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` — o disparador: `Señal E1 — análisis light según protocolo (Categories primero, máx 5 líneas).` |

**Objetivo:** veredicto rápido en la ventana óptima (trade #1 del día). Si `ENTRAR` + confirmación TV → operar. Si `ESPERAR` / `OBSERVAR` → pasar a AM #2 con posible escalado.

### AM #2 — Cierre ventana mañana (~10:00 NY)

| Paso | Acción |
|------|--------|
| **Tier** | **High** si AM #1 fue ambiguo · **Light** si AM #1 ya definió el plan |
| **Comando High** | `.\scripts\analyze\analyze-btc-high.ps1 -ML -Neural` |
| **Comando Light** | `.\scripts\analyze\analyze-btc-light.ps1 -ML -Neural` |
| **@ High** | `@live/btc_m5_high_signal.md` `@docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` |
| **@ Light** | `@live/btc_m5_signal.md` `@docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` |
| **Prompt High** | Copiar bloque **Prompt optimizado** de `../protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` — o disparador: `Análisis E1 CRT HIGH — bias, fakeout PDH/PDL, score reglas, galería WIN.` |
| **Prompt Light** | Copiar bloque **Prompt optimizado** de `../protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` — o disparador: `Update señal E1 — ¿sigue válido el plan de AM #1? (máx 5 líneas).` |

**Regla práctica:** si AM #1 dijo `ESPERAR`, `H1:NEUTRAL` o `OBSERVAR` → **usa High en AM #2**. Si AM #1 fue `ENTRAR` ejecutado o `NO_OPERAR` claro → **Light basta**.

---

## Bloque tarde — Chat **「NY PM」**

**Ventana NY:** 14:00–17:00 (UTC-4).

Abrir **chat nuevo** (`NY PM`). El chat AM ya cumplió su ciclo — no continuar ahí aunque Cursor “recuerde” el contexto.

### PM #1 — Apertura tarde (~14:30 NY)

| Paso | Acción |
|------|--------|
| **Tier** | **Light** |
| **Comando** | `.\scripts\analyze\analyze-btc-light.ps1 -ML -Neural` *(o `-All -NoChart -ML -Neural` si pasaron >2 h desde la última corrida)* |
| **@ en Cursor** | `@live/btc_m5_signal.md` `@docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` |
| **Prompt ejemplo** | Copiar bloque **Prompt optimizado** de `../protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` — o disparador: `Señal E1 tarde NY — veredicto e invalidación (máx 5 líneas).` |

**Nota:** si ya llevas **2 SL** en el día → **no abras este chat**. Fin de sesión.

### PM #2 — Cierre ventana tarde (~16:00 NY)

| Paso | Acción |
|------|--------|
| **Tier** | **Light** por defecto · **High** solo si PM #1 fue ambiguo o evalúas E2 |
| **Comando Light** | `.\scripts\analyze\analyze-btc-light.ps1 -ML -Neural` |
| **Comando High** | `.\scripts\analyze\analyze-btc-high.ps1 -ML -Neural` |
| **@ Light** | `@live/btc_m5_signal.md` `@docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` |
| **@ High** | `@live/btc_m5_high_signal.md` `@docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` |
| **Prompt Light** | Copiar bloque **Prompt optimizado** de `../protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` — o disparador: `Última lectura PM — ¿hay trade o cerrar pantalla? (máx 5 líneas).` |
| **Prompt High** | Copiar bloque **Prompt optimizado** de `../protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` — o disparador: `Análisis E1 CRT tarde — Turtle Soup watchlist si aplica (≤10%).` |

**Segundo High en el día:** reservar para PM #2 **solo si** PM #1 devolvió `ESPERAR`/`NEUTRAL` y aún estás dentro de ventana NY con **< 2 SL**. Caso contrario, mantener **1 High AM + 3 Light**.

---

## Presupuesto de tokens — schedule 2 + 2

Estimación por **prompt @** (live + protocolo). No incluye historial del chat ni reglas del proyecto.

| Escenario | Composición | Tokens/día (~) | vs 4× Full |
|-----------|-------------|---------------:|-----------:|
| **Recomendado** | 1 High + 3 Light | **~2 830** | **−67%** |
| Conservador | 4× Light | ~1 428 | −84% |
| Día ambiguo | 2 High + 2 Light | ~4 242 | −51% |
| Evitar rutina | 4× Full | ~8 700 | — |
| Evitar rutina | 4× High | ~7 028 | −19% vs Full |

### Desglose recomendado (1H + 3L)

| # | Bloque | Hora NY | Tier | Tokens (~) |
|---|--------|---------|------|----------:|
| 1 | AM #1 | 08:30 | Light | 357 |
| 2 | AM #2 | 10:00 | **High** | 1 757 |
| 3 | PM #1 | 14:30 | Light | 357 |
| 4 | PM #2 | 16:00 | Light | 357 |
| | | | **Total** | **2 828** |

Regenerar cifras: `python measure_analyzer_tokens.py` tras `-All`.

---

## Reglas operativas

### Cuándo escalar Light → High

| Señal en Light | Acción |
|----------------|--------|
| `ESPERAR` / `OBSERVAR` | Escalar al **siguiente** análisis del bloque con **High** |
| `H1:NEUTRAL` o bias mixto | **High** |
| Dudas en zona / fakeout PDH-PDL | **High** |
| Evaluar E2 Turtle Soup (≤10%) | **High** — opcional `-Reverse` para elevar watchlist E2 |
| Ya tienes sesgo claro (ej. solo shorts AM) | **High** con `-Bearish -Break` o `-Bullish -Break` |
| `ENTRAR` claro + 2M5:Y + NY:OK | **Quedarse en Light** — confirmar en TV |
| `NO_OPERAR` / fuera NY | No escalar — respetar veredicto |

### Cuándo detener el día

| Condición | Acción |
|-----------|--------|
| **2 SL** alcanzados | **Fin de sesión** — sin excepciones, sin indicadores, sin “un trade más” |
| Fuera ventana NY | **NO OPERAR** (salvo demo explícito) |
| Trade #3 tras día rojo | Recordar protocolo anti-sobreoperación (visual context) |
| AM #1 + AM #2 sin setup A+ | Cerrar bloque AM sin forzar PM |

### Tier Full — fuera de rutina

Usar `@live/btc_m5_snapshot.md` + `@docs/protocols/TRADING_LIVE_BTC_M5_ANALYSIS.md` solo si:

- Primera lectura post-noticia de alto impacto
- Cambio estructural H1 no capturado por Light/High
- Revisión pedagógica fuera de horario operativo

**No** usar Full en los 4 slots diarios.

---

## Checklist rápido

### Inicio del día

- [ ] Workspace = `D:\Danilo\Trading\Cursor Trading`
- [ ] `.\scripts\analyze\analyze-btc.ps1 -All -NoChart -ML -Neural` ejecutado
- [ ] Categories incluye **ML prob** y **Neural galería** (si usaste `-ML -Neural`)
- [ ] Contador SL del día = **0**
- [ ] Chat **NY AM** nuevo (no reutilizar ayer)

### Cada análisis (AM o PM)

- [ ] ¿Dentro de ventana NY (08–11 o 14–17)?
- [ ] ¿Menos de 2 SL hoy?
- [ ] Script del tier correcto ejecutado
- [ ] Solo **un par** @ (Light **o** High — nunca los 3 protocolos)
- [ ] Respuesta ≤5 líneas si es Light
- [ ] Confirmación final en TradingView antes de ejecutar

### Entre bloques

- [ ] Cerrar mentalmente el chat AM al terminar ~11:00
- [ ] Chat **NY PM** nuevo ~14:00
- [ ] Re-ejecutar light/high (o `-All`) si pasó >2 h o hubo volatilidad extrema

### Fin del día

- [ ] Registrar trades en Notion (campos de `TRADING_STRATEGY_CONTEXT.md`)
- [ ] Anotar si escalaste Light→High y por qué (mejora continua)

---

## Referencia rápida de comandos

```powershell
cd "D:\Danilo\Trading\Cursor Trading"

# Una vez al inicio
.\scripts\analyze\analyze-btc.ps1 -All -NoChart -ML -Neural

# Por análisis (añadir -ML -Neural para ML + Neural en Categories)
.\scripts\analyze\analyze-btc-light.ps1 -ML -Neural -Bearish   # bias forzado bajista
.\scripts\analyze\analyze-btc-high.ps1 -ML -Neural -Bullish     # bias forzado alcista
.\scripts\analyze\analyze-btc.ps1 -All -NoChart -ML -Neural -Bearish
.\scripts\analyze\analyze-us30.ps1 -All -NoChart -ML -Bearish
.\scripts\analyze\analyze-btc-superhigh.ps1 -ML -Neural -Bearish  # ~2 508 tokens — solo con captura entry/SL/TP
.\scripts\analyze\analyze-btc.ps1 -NoChart -ML -Neural       # Full ~2 175 — excepcional
```

| Tier | @ mentions | Cuándo en rutina 4× |
|------|------------|---------------------|
| **Light** | `@live/btc_m5_signal.md` `@docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md` | AM #1, PM #1, PM #2 (+ AM #2 si plan claro) |
| **High** | `@live/btc_m5_high_signal.md` `@docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md` | AM #2 por defecto; PM #2 solo si ambiguo |
| **Super High** | `@live/btc_super_high_signal.md` `@docs/protocols/TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md` | **On-demand** — cuando tengas captura entry/SL/TP lista (**no** en rutina 4×) |
| Full | `@live/btc_m5_snapshot.md` `@docs/protocols/TRADING_LIVE_BTC_M5_ANALYSIS.md` | **No** en rutina diaria |

---

## Flujo visual del día

```
08:00 NY ─────────────────────────────────────────────── 17:00 NY
    │                    │                    │                │
    │◄── NY AM chat ────►│                    │◄── NY PM chat ►│
    │  #1 Light 08:30    │  #2 High/L 10:00   │  #3 L 14:30    │  #4 L 16:00
    │                    │                    │                │
    └─ -All -NoChart -ML -Neural al inicio (opcional refresh entre bloques)
```

---

## US30 on-demand (cuando operas índice, no BTC)

> **No** sustituye la rutina 4× BTC. Usar solo el día que operas **US30** (máx. 1 mercado a la vez).

```powershell
cd "D:\Danilo\Trading\Cursor Trading"

# Inicio sesión US30 (equivalente a -All BTC)
.\scripts\analyze\analyze-us30.ps1 -All -NoChart -ML -Neural

# Por análisis
.\scripts\analyze\analyze-us30-light.ps1 -ML -Neural
.\scripts\analyze\analyze-us30-high.ps1 -ML -Neural
```

| Tier | @ mentions |
|------|------------|
| **Light** | `@live/us30_m5_signal.md` `@docs/protocols/TRADING_LIVE_US30_SIGNAL_LIGHT.md` |
| **High** | `@live/us30_m5_high_signal.md` `@docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md` |
| Full | `@live/us30_m5_snapshot.md` `@docs/protocols/TRADING_LIVE_US30_M5_ANALYSIS.md` |

Entrenar ML US30 (semanal): `python -m app.controllers.train_us30_signals`  
Protocolo completo: `../protocols/TRADING_LIVE_US30_M5_ANALYSIS.md`

---

*Danilo · Rutina 4× optimizada para tokens · Ver también `TRADING_ANALYZER_TOKEN_USAGE.md`*
