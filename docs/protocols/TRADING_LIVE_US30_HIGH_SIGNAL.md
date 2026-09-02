# US30 M5 High Signal — Protocolo análisis profundo (CRT + Turtle Soup)

> Usar con `@live/us30_m5_high_signal.md` tras `.\scripts\analyze\analyze-us30-high.ps1`
> Paralelo a `TRADING_LIVE_BTC_HIGH_SIGNAL.md` — mismas reglas E1/E2.

---

## Comando

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-us30-high.ps1
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -ML -Neural
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bullish -Reverse
.\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate
```

### Flags bias / setup

| Flag PS | Efecto |
|---------|--------|
| `-Bullish` / `-Bearish` | Sesgo forzado LONG/SHORT |
| `-Break` | Continuación E1 CRT |
| `-Reverse` | Contexto turtle soup E2 |
| `-Ilustrate` / `-Illustrate` | PNG anotado 2M5+OPTI → `live/us30_m5_chart_annotated.png` (también con `-NoChart`) |

Cursor:

```
@live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md
```

---

## Qué incluye HIGH

| Sección | High |
|---------|------|
| Categories completo + Neural (ML oculto) | ✅ |
| **Entrada optimizada (E1)** + Plan concreto | ✅ |
| **Ilustración entrada** (`-Ilustrate`) | ✅ opcional |
| **2M5 Válido vs Inválido** | ✅ |
| **Checklist 2M5** (5 ítems) | ✅ |
| **Segunda indicación** (H1 NEUTRAL) | ✅ |
| CRT H1 pending/completed/invalid | ✅ |
| Fakeout PDH/PDL | ✅ |
| Turtle Soup E2 (6 pts) | ✅ |
| RSI TORYS + DMI proxy | ✅ |
| 12 velas M5 | ✅ |
| Galería WIN/LOSS | ✅ |

**Orden de lectura:** Categories → Entrada optimizada → Checklist 2M5 → CRT/E2.

> **Segunda indicación:** cuando H1 es NEUTRAL, el sistema vota sesgo auxiliar desde DMI, CRT premium/discount y swings M5. No reemplaza bias H1.

---

## Prompt optimizado HIGH

```
Análisis E1 CRT US30 M5 — modo HIGH.

Lee Veredicto + Categories (**Bando usado**, **Recomendación**, **Segunda indicación** si H1 NEUTRAL)
+ **Entrada optimizada (E1)** + **Checklist 2M5** + **2M5 Válido/Inválido**
+ CRT + E2 turtle soup del high signal.

Aplica plan Danilo: NY only · E1 90%+ · SL $9 (~9 pts mini Dow) · R:R 1:2 · 2 SL fin sesión
Bias H1 + PDH/PDL + fakeout + 2 velas M5 + zona ≤0.15%
E2 solo watchlist ≤10% — no ejecutar reversión salvo plan explícito
Neural galería complementa Rules % — confirmar siempre en TradingView US30 M5

Responde en español:
1. VEREDICTO + DIR
2. Entrada optimizada (AHORA vs OPTI + trigger/SL/TP)
3. Checklist 2M5 (5 ítems)
4. CRT clave (PD + H1 state + fakeout)
5. Rules X/8 + calidad
6. Invalidación precisa (puntos)
7. ¿Operar o esperar? (1 frase)
```

---

## US30 vs BTC en High

| Aspecto | BTC | US30 |
|---------|-----|------|
| Fuente | Binance 24/7 | yfinance (horario mercado) |
| Decimales precio | 0–1 | 1 (índice ~42k) |
| SL $9 en puntos | % precio | ~9 pts mini / ~90 micro |
| Neural galería | Entrenada BTC desktop | **Misma red** — usar como hint visual, no verdad |

---

*Genera: `live/us30_m5_high_signal.md` + `live/us30_m5_chart.png`*
