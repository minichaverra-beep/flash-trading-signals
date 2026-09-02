# US30 M5 High Signal — Protocolo análisis profundo (CRT + Turtle Soup)

> Usar con `@live/us30_m5_high_signal.md` tras `.\scripts\analyze\analyze-us30-high.ps1`
> Paralelo a `TRADING_LIVE_BTC_HIGH_SIGNAL.md` — mismas reglas E1/E2 y UX High (Categories / Advanced / Salidas).

---

## Comando

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-us30-high.ps1
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -ML -Neural          # auto-activa Advanced
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Advanced -ML -Neural
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bullish -Reverse
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
```

### Flags bias / setup

| Flag PS | Efecto |
|---------|--------|
| `-Bullish` / `-Bearish` | Sesgo forzado LONG/SHORT |
| `-Break` | Breakout de nivel/estructura (no reversión) |
| `-Reverse` | Reversión E2 (turtle soup); operable con 2 velas alineadas + winrate |
| `-Advanced` | Categories ampliada (stats trader) + secciones A–I |
| `-ML` **y** `-Neural` juntos | **Auto-activa** Advanced |
| `-Ilustrate` / `-Illustrate` | PNG anotado 2M5+OPTI → `live/us30_m5_chart_annotated.png` (también con `-NoChart`) |

Cursor:

```
@live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md
```

Advanced:

```
@live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md analisis ADVANCED E1 CRT
```

---

## Qué incluye HIGH

| Sección | High |
|---------|------|
| Categories: **Precio** → **Entrada óptima** → bando/Neural → (**Advanced** si flag) → **Confluencia setup** (última) | ✅ |
| **Entrada optimizada (E1)** + Plan concreto | ✅ |
| **Ilustración entrada** (`-Ilustrate`) + bloque **Salidas** (paths `live/…`, abs, markdown — sin base64) | ✅ |
| **2M5 Válido vs Inválido** | ✅ |
| **Checklist 2M5** (5 ítems) | ✅ |
| **Segunda indicación** (H1 NEUTRAL) | ✅ |
| CRT H1 pending/completed/invalid | ✅ |
| Fakeout PDH/PDL | ✅ |
| Turtle Soup E2 (6 pts) | ✅ |
| RSI TORYS + DMI proxy | ✅ |
| 12 velas M5 | ✅ |
| Galería WIN/LOSS | ✅ |

**Orden de lectura:** Categories (Precio · Entrada óptima · Confluencia) → Entrada optimizada → Checklist 2M5 → CRT/E2 → Salidas.

> **Sesión NY** ya no es fila de la tabla de status signal ni fuerza `NO_OPERAR` en la recomendación. Sigue como info en header.
>
> **Segunda indicación:** cuando H1 es NEUTRAL, el sistema vota sesgo auxiliar desde DMI, CRT premium/discount y swings M5. No reemplaza bias H1.

---

## Modo Advanced (análisis profundo)

| Condición | Efecto |
|-----------|--------|
| `-Advanced` en `scripts/analyze/analyze-us30-high.ps1` | Fuerza modo advanced |
| `-ML` **y** `-Neural` juntos | **Auto-activa** advanced |
| Sin `--advanced` | Output high estándar |

Python: `--advanced` → stats trader en Categories + secciones **A–I** en `live/us30_m5_high_signal.md` (mismo bloque que BTC).

---

## Prompt optimizado HIGH

```
Análisis E1 CRT US30 M5 — modo HIGH.

Lee Veredicto + Categories (**Precio**, **Entrada óptima**, **Bando usado**, **Recomendación**,
**Confluencia setup**, **Segunda indicación** si H1 NEUTRAL)
+ **Entrada optimizada (E1)** + **Checklist 2M5** + **2M5 Válido/Inválido**
+ CRT + E2 turtle soup del high signal.
+ **Salidas** (paths chart anotado si Ilustrate).

Aplica plan Danilo: NY info · E1 90%+ · SL $9 (~9 pts mini Dow) · R:R 1:2 · 2 SL fin sesión
Bias H1 + PDH/PDL + fakeout + 2 velas M5 + zona ≤0.15%
Break = breakout; Reverse = operable con 2 velas + winrate
E2 solo watchlist ≤10% salvo modo Reverse operable
Neural galería complementa Rules % — confirmar siempre en TradingView US30 M5

Responde en español:
1. VEREDICTO + DIR + Confluencia
2. Entrada óptima (AHORA vs OPTI + trigger/SL/TP)
3. Checklist 2M5 (5 ítems)
4. CRT clave (PD + H1 state + fakeout)
5. Rules X/7 + calidad
6. Invalidación precisa (puntos)
7. ¿Operar o esperar? (1 frase)
8. Paths Salidas si hay chart anotado
```

---

## US30 vs BTC en High

| Aspecto | BTC | US30 |
|---------|-----|------|
| Fuente | Binance 24/7 | yfinance (horario mercado) |
| Decimales precio | 0–1 | 1 (índice ~42k) |
| SL $9 en puntos | % precio | ~9 pts mini / ~90 micro |
| Chart anotado | `live/btc_m5_chart_annotated.png` | `live/us30_m5_chart_annotated.png` |
| Neural galería | Entrenada BTC desktop | **Misma red** — hint visual, no verdad |
| Código High | `btc_high_analysis.write_high_signal` | **Mismo pipeline** (`asset_label=US30`) |

---

*Genera: `live/us30_m5_high_signal.md` (+ `live/us30_m5_chart.png` / `us30_m5_chart_annotated.png`)*
