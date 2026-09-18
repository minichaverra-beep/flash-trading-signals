# Zentinel TV Presets — calibraciones en el stack local

> Presets de indicadores **FVG Multi TF + Volumen 2.0** e **ICT Zentinel Watchtower**.
> El stack **no lee TradingView en vivo**: valores versionados en config + checklist manual en TV.
> **Última actualización:** 2026-09-18

---

## Dónde viven

| Artefacto | Ruta |
|-----------|------|
| YAML (fuente) | `config/zentinel_presets.yaml` |
| API Python | `app/models/zentinel_presets.py` |
| Doc | este archivo |

Presets TV:

| Mercado | FVG+Vol | Watchtower |
|---------|---------|------------|
| BTC | `Zentinel_BTC_E1` | `Watchtower_BTC_E1` |
| US30 | `Zentinel_US30_E1` | `Watchtower_US30_E1` |

---

## A) FVG Multi TF + Volumen — filtro (nunca trigger)

| | BTC | US30 |
|--|-----|------|
| Alto | 1.7 | 1.6 |
| Extremo | 2.6 | 2.8 |
| Bajo | 0.75 | 0.70 |
| Muy bajo | 0.45 | 0.40 |
| Período | 84 | 48 |
| Labels | small | small |

**Rol:** confluencia. **Entrada** = H1/CTR + zona + 2M5.

En señales High/Advanced, el vol relativo (última vela / media del período) suma puntos soft en `compute_confluencia_setup` — no dispara ENTRAR.

---

## B) Watchtower — Killzones NY only

Chart TZ: **America/New_York**.

| | Ventanas |
|--|----------|
| **ON** | 08:00–10:00 · 10:00–11:00 · 14:00–16:00 |
| **OFF** | Asia 19–20 · London 02–05 · Lunch 11–14 |

| | BTC | US30 |
|--|-----|------|
| SMT HTF | OFF | OFF |
| SMT max | 3 | 3 |
| SMT lookback | 5 · Sym1 ETH · Sym2 ES | 3 · Sym1 ES · Sym2 NQ |
| Bias avg | 3 | 3 |
| Bias neutral | 0.5% | 0.3% |
| MNO | ON | OFF |
| ORG | OFF | ON RTH 09:30–16:15 |
| CE50% | — | ON |
| Labels | — | OFF |
| PW MID | OFF | ON |

`session_flags` (BTC + US30) usa estas ventanas ON para `in_ny_window` / etiqueta `window`.

---

## Qué cablea el pipeline local

1. **Señales / Confluencia** — umbrales de volumen + soft bonus killzone NY.
2. **ICT scan** — `killzone_ok` desde flags Watchtower.
3. **Advanced** — bloque markdown corto con presets + banda de volumen.
4. **Gráfico / -Ilustrate** — subtítulo con nombres de preset + badge KZ si ON.

## Checklist TradingView (manual)

- [ ] Cargar preset `Zentinel_*_E1` y `Watchtower_*_E1` del mercado.
- [ ] Chart timezone = America/New_York.
- [ ] Confirmar killzones ON/OFF como arriba.
- [ ] Volumen: labels small; umbrales del mercado.
- [ ] No usar FVG/Vol como trigger; solo filtro junto a H1/CTR + zona + 2M5.
