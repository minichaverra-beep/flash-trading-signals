# BTC M5 CONTEXT — Protocolo (estructura / vigencia)

> Usar con `@live/btc_m5_context.md` tras `.\scripts\analyze\analyze-btc-context.ps1`
> **No es señal de entrada** (sin Entry/SL/TP). Solo lectura de estructura M5.
> Params distintos de Light/High (EMA9/21, swing lookback 4, ATR vigencia, RSI exh 32/68).

---

## Comando (sin params; sin Cursor IA)

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-btc-context.ps1
```

La **consola** ya muestra Bias + Estado. Opcional en Cursor:

```
@live/btc_m5_context.md @docs/protocols/TRADING_LIVE_BTC_CONTEXT.md
```

| Salida | Contenido |
|--------|-----------|
| `live/btc_m5_context.md` | Bias M5 + VIGENTE / AGOTANDO / TRANSICION + swings + lectura |

Python directo:

```powershell
python -m app.controllers.analyze_btc_m5 --mode context --no-chart
```

---

## Qué mirar (sin Categories / sin ENTRAR)

1. **Bias estructura M5** — BULLISH / BEARISH / NEUTRAL  
2. **Estado del impulso** — VIGENTE / AGOTANDO / TRANSICION  
3. Swings (HL/LL · HH/LH)  
4. Extensión ×ATR, RSI, cuerpos, mecha de rechazo  

| Estado | Lectura |
|--------|---------|
| **VIGENTE** | Bando estructural aún con recorrido; prioriza setups a favor |
| **AGOTANDO** | Impulso débil/estirado; espera pullback o confirmación nueva |
| **TRANSICION** | Mixto / rango; no forzar dirección |

---

## Cuándo usar

| Situación | CONTEXT |
|-----------|---------|
| Antes de Light/High: ¿sigue vivo el tramo? | **SÍ** |
| Solo consola, sin abrir Cursor | **SÍ** |
| Decidir Entry/SL/TP | **NO** — usar High |
| Chequeo Categories / Neural | **NO** — usar Light/High |

---

*CONTEXT ≠ Light/High · no auto-ejecutar*
