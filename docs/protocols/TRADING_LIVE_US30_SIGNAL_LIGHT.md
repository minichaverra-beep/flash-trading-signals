# US30 M5 Signal Light — Protocolo mínimo (tokens)

> Usar con `@live/us30_m5_signal.md` tras `.\scripts\analyze\analyze-us30-light.ps1`
> **No** cargar otros MD salvo que el usuario pida análisis completo.

---

## Comando

```powershell
cd "D:\Danilo\Trading\Cursor Trading"
.\scripts\analyze\analyze-us30-light.ps1
.\scripts\analyze\analyze-us30-light.ps1 -Bearish
.\scripts\analyze\analyze-us30-light.ps1 -Bullish -ML -Neural
```

Cursor:

```
@live/us30_m5_signal.md @docs/protocols/TRADING_LIVE_US30_SIGNAL_LIGHT.md
```

---

## Qué incluye el live Light

| Sección | Contenido |
|---------|-----------|
| **Veredicto** | ENTRAR / ESPERAR / NO_OPERAR |
| **Categories** | **Bando usado**, **Recomendación**, acción, tendencia, reglas 8, calidad, prob. hist., ML, Neural |
| **CRT** | PD/H1, fakeout, acción E1 |
| **Red flags** | Top flags |

**Orden de lectura:** **Categories** primero — **Bando usado** y **Recomendación**.

---

## Reglas compartidas (igual que BTC)

- Reloj NY **08–11** y **14–17** UTC-4 — **informativo** (no gate)
- Solo **E1** (90%+)
- SL **~$9** fijo — en US30 ≈ **9 pts** ($1/pt) o **90 pts** (micro)
- R:R mínimo **1:2**
- **2 SL = límite de riesgo diario**
- **2 velas M5** de confirmación obligatorias
- Rules **≥70%** para ENTRAR

---

## Prompt optimizado

```
Señal E1 US30 M5 — análisis light.

Lee PRIMERO Categories del signal file (**Bando usado**, **Recomendación**).

Reglas: E1 only · Bias H1 · Zona ≤0.15% · 2 velas M5 · R:R 1:2 · SL $9 (~9 pts mini)
(Sesión NY = reloj info, no gate)
Rules ≥70% ENTRAR · <70% ESPERAR · <50% NO_OPERAR
ML/Neural si presentes — complementan, no reemplazan TV
Sin 2M5 / 2 SL hoy → ESPERAR o NO_OPERAR según tabla

Responde EXACTAMENTE (máx 5 líneas):

VEREDICTO: ENTRAR | ESPERAR | NO_OPERAR
DIR: LONG | SHORT | —
CLAVE: (1 regla que decide)
INVALID: (precio/nivel)
NOTA: (opcional — confirmar TV si ENTRAR)

Español. No inventar datos.
```

---

*Par completo: `scripts/analyze/analyze-us30.ps1` + `@live/us30_m5_snapshot.md`*
