"""Tarjeta de señal (póster) compuesta en el servidor con Pillow.

Misma disposición que el póster del navegador (signal-share-poster.ts):
cabecera, píldoras, ESPERAR/TOMAR, gráfico de entrada, barras COMPRA/VENTA,
riesgo, niveles clave, escenarios y pie. Solo pinta los bloques que trae el
spec: no inventa precios ni textos. El gráfico se lee del PNG de live/, así la
tarjeta sale igual en el escritorio y en el APK (el WebView no interviene).

Uso:
    python -m app.views.signal_card --spec spec.json --out tarjeta.png

Imprime una línea JSON: {"ok": true, "path": ..., "chart": true|false, "chart_error": ...}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

W = 1080
PAD = 44
GAP = 18
INNER = W - PAD * 2

C = {
    "bg": "#101110",
    "surface": "#181a19",
    "border": "#343a36",
    "text": "#f4fbf6",
    "muted": "#8e9992",
    "purple": "#4a33af",
    "pink": "#f075c0",
    "gain": "#3ecf8e",
    "loss": "#f07171",
    "amber": "#e7c56a",
    "track": "#1e2220",
}

MAX_TEXT = 400
MAX_ITEMS = 12


# --------------------------------------------------------------------------- fuentes
def _font_dir() -> Path | None:
    try:
        import matplotlib

        p = Path(matplotlib.get_data_path()) / "fonts" / "ttf"
        return p if p.is_dir() else None
    except Exception:
        return None


_FONT_CACHE: dict[tuple[bool, int], Any] = {}


def font(size: int, bold: bool = False):
    """DejaVu (viene con matplotlib) o la fuente por defecto de Pillow."""
    key = (bold, size)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    from PIL import ImageFont

    f = None
    d = _font_dir()
    if d is not None:
        candidate = d / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
        if candidate.is_file():
            try:
                f = ImageFont.truetype(str(candidate), size)
            except Exception:
                f = None
    if f is None:
        try:
            f = ImageFont.load_default(size=size)
        except TypeError:
            f = ImageFont.load_default()
    _FONT_CACHE[key] = f
    return f


def text_w(draw, text: str, fnt) -> float:
    try:
        return float(draw.textlength(text, font=fnt))
    except Exception:
        box = draw.textbbox((0, 0), text, font=fnt)
        return float(box[2] - box[0])


def wrap(draw, text: str, max_w: float, fnt) -> list[str]:
    words = [w for w in str(text or "").split() if w]
    if not words:
        return []
    lines: list[str] = []
    cur = ""
    for word in words:
        for part in _split_long(draw, word, max_w, fnt):
            nxt = f"{cur} {part}" if cur else part
            if cur and text_w(draw, nxt, fnt) > max_w:
                lines.append(cur)
                cur = part
            else:
                cur = nxt
    if cur:
        lines.append(cur)
    return lines


def _split_long(draw, word: str, max_w: float, fnt) -> list[str]:
    if text_w(draw, word, fnt) <= max_w:
        return [word]
    out: list[str] = []
    buf = ""
    for ch in word:
        if buf and text_w(draw, buf + ch, fnt) > max_w:
            out.append(buf)
            buf = ch
        else:
            buf += ch
    if buf:
        out.append(buf)
    return out


def fit(draw, text: str, max_w: float, fnt) -> str:
    if max_w <= 0:
        return ""
    if text_w(draw, text, fnt) <= max_w:
        return text
    t = text
    while len(t) > 1 and text_w(draw, t + "…", fnt) > max_w:
        t = t[:-1]
    return t + "…"


# --------------------------------------------------------------------------- spec
def _s(v: Any) -> str:
    t = str(v if v is not None else "").strip()
    return t[:MAX_TEXT]


def _num(v: Any) -> float | None:
    try:
        n = float(v)
    except (TypeError, ValueError):
        return None
    if n != n or n in (float("inf"), float("-inf")):
        return None
    return n


def normalize_spec(raw: dict | None) -> dict:
    """Spec saneado: strings acotados, listas acotadas, números reales. Sin valores inventados."""
    raw = raw if isinstance(raw, dict) else {}
    direction = _s(raw.get("direction"))
    if direction not in ("Alcista", "Bajista"):
        direction = ""
    odds = raw.get("odds") if isinstance(raw.get("odds"), dict) else None
    odds_n = None
    if odds:
        compra, venta = _num(odds.get("compra")), _num(odds.get("venta"))
        if compra is not None and venta is not None:
            odds_n = {"compra": max(0, min(100, compra)), "venta": max(0, min(100, venta))}
    action = raw.get("action") if isinstance(raw.get("action"), dict) else None
    action_n = None
    if action and _s(action.get("state")) in ("TOMAR", "ESPERAR"):
        action_n = {"state": _s(action.get("state")), "reason": _s(action.get("reason")) or None}

    pills = []
    for p in (raw.get("pills") or [])[:MAX_ITEMS]:
        if isinstance(p, dict) and _s(p.get("title")):
            pills.append({"kicker": _s(p.get("kicker")), "title": _s(p.get("title")), "detail": _s(p.get("detail"))})
    levels = []
    for lv in (raw.get("levels") or [])[:MAX_ITEMS]:
        if isinstance(lv, dict) and _s(lv.get("value")):
            tone = _s(lv.get("tone"))
            levels.append({"label": _s(lv.get("label")), "value": _s(lv.get("value")),
                           "tone": tone if tone in ("gain", "loss") else "text"})

    def scenario(v):
        if not isinstance(v, dict):
            return None
        bullets = [_s(b) for b in (v.get("bullets") or [])[:MAX_ITEMS] if _s(b)]
        if not bullets:
            return None
        return {"title": _s(v.get("title")) or "Escenario", "tone": "loss" if _s(v.get("tone")) == "loss" else "gain",
                "bullets": bullets}

    risk = _num(raw.get("risk"))
    risk_fill = _num(raw.get("riskFill"))
    return {
        "symbol": _s(raw.get("symbol")).upper(),
        "timeframe": _s(raw.get("timeframe")) or None,
        "tier": _s(raw.get("tier")) or None,
        "price": _s(raw.get("price")) or None,
        "asOf": _s(raw.get("asOf")) or None,
        "direction": direction or None,
        "odds": odds_n,
        "pills": pills,
        "action": action_n,
        "levels": levels,
        "primary": scenario(raw.get("primary")),
        "pullback": scenario(raw.get("pullback")),
        "footer": _s(raw.get("footer")) or None,
        "risk": risk if risk is not None and risk >= 0 else None,
        "riskFill": max(0.0, min(100.0, risk_fill)) if risk_fill is not None else None,
        "riskNote": _s(raw.get("riskNote")) or None,
        "chart": _s(raw.get("chart")) or None,
    }


def format_risk(points: float) -> str:
    r = round(points * 10) / 10
    return str(int(r)) if float(r).is_integer() else f"{r:.1f}"


# --------------------------------------------------------------------------- dibujo
def _panel(draw, box: tuple[int, int, int, int], stroke: str, radius: int = 14) -> None:
    x, y, w, h = box
    draw.rounded_rectangle((x, y, x + w, y + h), radius=radius, fill=C["surface"], outline=stroke, width=2)


def _mark(draw, x: int, y: int) -> None:
    for i, (w, col) in enumerate(((52, C["purple"]), (38, C["pink"]), (24, C["purple"]))):
        draw.rounded_rectangle((x, y + i * 18, x + w, y + i * 18 + 12), radius=4, fill=col)


def _chevron(draw, x: int, y: int, up: bool, color: str) -> None:
    pts = [(x, y + 16), (x + 11, y), (x + 22, y + 16)] if up else [(x, y), (x + 11, y + 16), (x + 22, y)]
    draw.polygon(pts, fill=color)


def _load_chart(path: str | None):
    """PNG del gráfico de entrada. Devuelve (imagen RGBA | None, error | None)."""
    if not path:
        return None, None
    p = Path(path)
    if not p.is_file():
        return None, f"PNG no encontrado: {p.name}"
    try:
        from PIL import Image

        im = Image.open(p)
        im.load()
        if im.width < 2 or im.height < 2:
            return None, "PNG vacío"
        return im.convert("RGBA"), None
    except Exception as exc:  # pragma: no cover - depende del archivo
        return None, f"PNG ilegible: {exc}"


def render_signal_card(spec: dict, out_path: Path | str) -> dict:
    """Compone el PNG. Devuelve {"ok", "path", "chart", "chart_error", "height"}."""
    from PIL import Image, ImageDraw

    card = normalize_spec(spec)
    chart, chart_error = _load_chart(card.get("chart"))

    # Medición sobre un lienzo de prueba; después se dibuja en el definitivo.
    probe = ImageDraw.Draw(Image.new("RGB", (W, 10)))
    plan = _plan(probe, card, chart)
    height = plan["height"]

    img = Image.new("RGB", (W, height), C["bg"])
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 8, height), fill=C["purple"])
    _draw_all(img, draw, card, chart, plan)
    draw.rectangle((1, 1, W - 2, height - 2), outline=C["border"], width=2)

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(out.name + ".tmp")
    img.save(tmp, format="PNG", optimize=False)
    tmp.replace(out)
    return {"ok": True, "path": str(out), "chart": chart is not None, "chart_error": chart_error, "height": height}


def _plan(draw, card: dict, chart) -> dict:
    y = PAD
    header_h = _header_h(card)
    if header_h:
        y += header_h + GAP

    pills = []
    if card["pills"]:
        n = len(card["pills"])
        gap = 14
        w = min(560, INNER) if n == 1 else (INNER - gap * (n - 1)) / n
        measured = [_measure_pill(draw, p, w) for p in card["pills"]]
        h = max(m["h"] for m in measured)
        for i, m in enumerate(measured):
            pills.append({"x": int(PAD + i * (w + gap)), "y": int(y), "w": int(w), "h": int(h), **m})
        y += h + GAP

    action = None
    if card["action"]:
        action = {"x": PAD, "y": int(y), "w": INNER, "h": 96 if card["action"]["reason"] else 72}
        y += action["h"] + GAP

    chart_box = None
    if chart is not None:
        raw = INNER * (chart.height / chart.width)
        h = int(round(max(280, min(820, raw))))
        chart_box = {"y": int(y), "h": h}
        y += h + GAP

    odds_y = int(y) if card["odds"] else 0
    if card["odds"]:
        y += 156 + GAP

    risk_y = int(y) if card["risk"] is not None else 0
    if card["risk"] is not None:
        y += (168 if card["riskNote"] else 118) + GAP

    levels = []
    levels_label_y = 0
    if card["levels"]:
        levels_label_y = int(y)
        y += 32
        cols = _level_cols(card["levels"])
        gap = 12
        natural = (INNER - gap * (cols - 1)) / cols
        w = min(320, natural) if len(card["levels"]) == 1 else natural
        rows = [card["levels"][i:i + cols] for i in range(0, len(card["levels"]), cols)]
        for row in rows:
            measured = [_measure_level(draw, lv, w) for lv in row]
            h = max(m["h"] for m in measured)
            for col, m in enumerate(measured):
                levels.append({"x": int(PAD + col * (w + gap)), "y": int(y), "w": int(w), "h": int(h), **m})
            y += h + gap
        y = y - gap + GAP

    primary = pullback = None
    if card["primary"] or card["pullback"]:
        both = bool(card["primary"] and card["pullback"])
        gap = 14
        w = (INNER - gap) / 2 if both else INNER
        pm = _measure_scenario(draw, card["primary"], w) if card["primary"] else None
        bm = _measure_scenario(draw, card["pullback"], w) if card["pullback"] else None
        h = max(pm["h"] if pm else 0, bm["h"] if bm else 0)
        if pm:
            primary = {"x": PAD, "y": int(y), "w": int(w), "h": int(h), **pm}
        if bm:
            pullback = {"x": int(PAD + w + gap) if both else PAD, "y": int(y), "w": int(w), "h": int(h), **bm}
        y += h + GAP

    footer_lines = wrap(draw, card["footer"], INNER - 8, font(18)) if card["footer"] else []
    footer_y = int(y)
    if footer_lines:
        y += len(footer_lines) * 26
    if y == PAD:
        y += 80
    return {
        "height": int(y + PAD), "header_h": header_h, "pills": pills, "action": action, "chart": chart_box,
        "odds_y": odds_y, "risk_y": risk_y, "levels_label_y": levels_label_y, "levels": levels,
        "primary": primary, "pullback": pullback, "footer_y": footer_y, "footer_lines": footer_lines,
    }


def _header_h(card: dict) -> int:
    if not (card["symbol"] or card["price"] or card["tier"] or card["timeframe"]):
        return 0
    symbol_h = 62 if (card["symbol"] or card["timeframe"]) else 0
    tier_h = 28 if card["tier"] else 0
    price_h = (18 + 8 + 56 + (26 if card["asOf"] else 0)) if card["price"] else 0
    return max(64, symbol_h + tier_h, price_h)


def _measure_pill(draw, pill: dict, w: float) -> dict:
    text_w_ = w - 108
    title = wrap(draw, pill["title"], text_w_, font(28, True))
    detail = wrap(draw, pill["detail"], text_w_, font(18)) if pill["detail"] else []
    text_h = len(title) * 34 + ((8 + len(detail) * 24) if detail else 0)
    return {"h": max(108, 28 + text_h + 16), "title_lines": title, "detail_lines": detail}


def _measure_level(draw, level: dict, w: float) -> dict:
    lines = wrap(draw, level["value"], w - 28, font(26, True))
    return {"h": 22 + 20 + len(lines) * 32 + 16, "value_lines": lines}


def _measure_scenario(draw, sc: dict, w: float) -> dict:
    title = wrap(draw, sc["title"].upper(), w - 36, font(20, True))
    bullets = [wrap(draw, b, w - 58, font(18)) for b in sc["bullets"]]
    h = 20 + len(title) * 28 + 8
    for lines in bullets:
        h += len(lines) * 26 + 8
    return {"h": h + 14, "title_lines": title, "bullets": bullets}


def _level_cols(levels: list[dict]) -> int:
    long = any(len(lv["value"]) > 18 for lv in levels)
    mx = 3 if long else min(5, len(levels))
    return max(1, min(mx, len(levels)))


def _draw_all(img, draw, card: dict, chart, plan: dict) -> None:
    if plan["header_h"]:
        _draw_header(draw, card, PAD, plan["header_h"])
    for pill, box in zip(card["pills"], plan["pills"]):
        _draw_pill(draw, pill, box, card["direction"])
    if plan["action"]:
        _draw_action(draw, card["action"], plan["action"])
    if plan["chart"] and chart is not None:
        _draw_chart(img, draw, chart, PAD, plan["chart"]["y"], INNER, plan["chart"]["h"])
    if card["odds"]:
        _draw_odds(draw, card, plan["odds_y"])
    if card["risk"] is not None:
        _draw_risk(draw, card, plan["risk_y"])
    if plan["levels"]:
        draw.text((PAD, plan["levels_label_y"]), "NIVELES CLAVE", fill=C["pink"], font=font(15, True))
        for lv, box in zip(card["levels"], plan["levels"]):
            _draw_level(draw, lv, box)
    if plan["primary"]:
        _draw_scenario(draw, card["primary"], plan["primary"])
    if plan["pullback"]:
        _draw_scenario(draw, card["pullback"], plan["pullback"])
    for i, line in enumerate(plan["footer_lines"]):
        draw.text((PAD, plan["footer_y"] + i * 26), line, fill=C["muted"], font=font(18))


def _draw_header(draw, card: dict, y: int, h: int) -> None:
    mark_x = PAD
    if card["symbol"] or card["price"]:
        _mark(draw, mark_x, y + 4)
    text_x = mark_x + 78 if (card["symbol"] or card["price"]) else PAD
    price_f = font(52, True)
    price_w = min(420, text_w(draw, card["price"], price_f) + (40 if card["direction"] else 0)) if card["price"] else 0
    text_max = W - PAD - text_x - (price_w + 24 if price_w else 0)

    if card["symbol"] or card["timeframe"]:
        title_f = font(54, True)
        avail = max(80, text_max)
        sep = "  |  " if (card["symbol"] and card["timeframe"]) else ""
        tf = card["timeframe"] or ""
        if tf and text_w(draw, f"{card['symbol']}{sep}{tf}", title_f) > avail:
            tf = fit(draw, tf, min(140, avail * 0.4), title_f)
        sep_w = text_w(draw, sep, title_f) if sep else 0
        tf_w = text_w(draw, tf, title_f) if tf else 0
        symbol = fit(draw, card["symbol"], max(40, avail - sep_w - tf_w), title_f) if card["symbol"] else ""
        x = text_x
        if symbol:
            draw.text((x, y), symbol, fill=C["text"], font=title_f)
            x += text_w(draw, symbol, title_f)
        if sep:
            draw.text((x, y), sep, fill=C["muted"], font=title_f)
            x += sep_w
        if tf:
            draw.text((x, y), tf, fill=C["pink"], font=title_f)
    if card["tier"]:
        tier_f = font(20)
        draw.text((text_x, y + (62 if (card["symbol"] or card["timeframe"]) else 0)),
                  fit(draw, card["tier"], text_max, tier_f), fill=C["muted"], font=tier_f)

    if card["price"]:
        right = W - PAD
        kick_f = font(15, True)
        draw.text((right, y), "PRECIO ACTUAL", fill=C["pink"], font=kick_f, anchor="ra")
        price = fit(draw, card["price"], 420, price_f)
        pw = text_w(draw, price, price_f)
        draw.text((right, y + 26), price, fill=C["text"], font=price_f, anchor="ra")
        if card["direction"]:
            up = card["direction"] == "Alcista"
            _chevron(draw, int(right - pw - 34), y + 42, up, C["gain"] if up else C["loss"])
        if card["asOf"]:
            asof_f = font(18)
            draw.text((right, y + 86), fit(draw, card["asOf"], 460, asof_f), fill=C["muted"], font=asof_f, anchor="ra")

    if h > 0:
        draw.line((PAD, y + h + 2, W - PAD, y + h + 2), fill=C["border"], width=1)


def _pill_icon(draw, x: int, y: int, kicker: str, direction: str | None) -> None:
    draw.ellipse((x, y, x + 44, y + 44), outline=C["purple"], width=2)
    k = kicker.lower()
    if "tendencia" in k:
        if not direction:
            draw.rectangle((x + 12, y + 20, x + 32, y + 24), fill=C["muted"])
            return
        up = direction == "Alcista"
        _chevron(draw, x + 11, y + 14, up, C["gain"] if up else C["loss"])
        return
    if "probabilidad" in k:
        draw.text((x + 22, y + 23), "%", fill=C["pink"], font=font(16, True), anchor="mm")
        return
    draw.ellipse((x + 14, y + 14, x + 30, y + 30), outline=C["pink"], width=2)
    draw.ellipse((x + 19, y + 19, x + 25, y + 25), fill=C["pink"])


def _draw_pill(draw, pill: dict, box: dict, direction: str | None) -> None:
    _panel(draw, (box["x"], box["y"], box["w"], box["h"]), C["border"])
    _pill_icon(draw, box["x"] + 18, box["y"] + 22, pill["kicker"], direction)
    x = box["x"] + 84
    y = box["y"] + 18
    if pill["kicker"].strip():
        kf = font(15, True)
        draw.text((x, y), fit(draw, pill["kicker"].upper(), box["w"] - 100, kf), fill=C["pink"], font=kf)
        y += 24
    for line in box["title_lines"]:
        draw.text((x, y), line, fill=C["text"], font=font(28, True))
        y += 34
    for line in box["detail_lines"]:
        draw.text((x, y), line, fill=C["muted"], font=font(18))
        y += 24


def _draw_action(draw, action: dict, box: dict) -> None:
    accent = C["gain"] if action["state"] == "TOMAR" else C["amber"]
    _panel(draw, (box["x"], box["y"], box["w"], box["h"]), accent)
    draw.rectangle((box["x"] + 10, box["y"] + 14, box["x"] + 18, box["y"] + box["h"] - 14), fill=accent)
    draw.text((box["x"] + 32, box["y"] + 16), action["state"], fill=accent, font=font(34, True))
    if action["reason"]:
        rf = font(18)
        draw.text((box["x"] + 32, box["y"] + 58), fit(draw, action["reason"], box["w"] - 56, rf), fill=C["text"], font=rf)


def _draw_chart(img, draw, chart, x: int, y: int, w: int, h: int) -> None:
    from PIL import Image, ImageDraw

    scale = min(w / chart.width, h / chart.height)
    dw, dh = max(1, int(chart.width * scale)), max(1, int(chart.height * scale))
    resized = chart.resize((dw, dh), Image.Resampling.LANCZOS)
    panel = Image.new("RGBA", (w, h), C["surface"])
    panel.alpha_composite(resized, ((w - dw) // 2, (h - dh) // 2))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=16, fill=255)
    img.paste(panel, (x, y), mask)
    draw.rounded_rectangle((x, y, x + w, y + h), radius=16, outline=C["border"], width=2)


def _draw_bar_row(draw, label: str, pct: float, color: str, x: int, y: int, width: int) -> None:
    draw.text((x, y + 12), label, fill=C["text"], font=font(18, True), anchor="lm")
    label_w = 108
    pct_text = f"{int(round(pct))}%"
    pf = font(20, True)
    pct_w = text_w(draw, pct_text, pf)
    bar_x = x + label_w
    bar_w = max(40, width - label_w - pct_w - 16)
    bar_y = y + 5
    draw.rounded_rectangle((bar_x, bar_y, bar_x + bar_w, bar_y + 14), radius=7, fill=C["track"])
    fill_w = max(0, min(bar_w, bar_w * pct / 100))
    if fill_w > 0:
        draw.rounded_rectangle((bar_x, bar_y, bar_x + fill_w, bar_y + 14), radius=7, fill=color)
    draw.text((x + width, y + 13), pct_text, fill=color, font=pf, anchor="rm")


def _draw_odds(draw, card: dict, y: int) -> None:
    odds = card["odds"]
    _panel(draw, (PAD, y, INNER, 156), C["border"])
    pair = " · ".join(p for p in (card["symbol"], card["timeframe"]) if p)
    head = f"{pair} | Probabilidad estimada" if pair else "Probabilidad estimada"
    hf = font(22, True)
    draw.text((PAD + 18, y + 16), fit(draw, head, INNER - 36, hf), fill=C["text"], font=hf)
    _draw_bar_row(draw, "COMPRA", odds["compra"], C["gain"], PAD + 18, y + 58, INNER - 36)
    _draw_bar_row(draw, "VENTA", odds["venta"], C["loss"], PAD + 18, y + 104, INNER - 36)


def _risk_tone(fill: float) -> str:
    if fill < 40:
        return C["gain"]
    if fill < 70:
        return C["amber"]
    return C["loss"]


def _draw_risk(draw, card: dict, y: int) -> None:
    note = card["riskNote"]
    _panel(draw, (PAD, y, INNER, 168 if note else 118), C["border"])
    fill = card["riskFill"] if card["riskFill"] is not None else 0.0
    value = f"{format_risk(card['risk'])} pts"
    x = PAD + 18
    width = INNER - 36
    row_y = y + 28
    draw.text((x, row_y + 22), "Riesgo", fill=C["text"], font=font(22, True), anchor="lm")
    vf = font(26, True)
    value_w = text_w(draw, value, vf)
    label_w = 128
    bar_x = x + label_w
    bar_w = max(40, width - label_w - value_w - 20)
    bar_h = 36
    bar_y = row_y + 4
    draw.rounded_rectangle((bar_x, bar_y, bar_x + bar_w, bar_y + bar_h), radius=18, fill=C["track"])
    fill_w = max(0, min(bar_w, bar_w * fill / 100))
    if fill_w > 0:
        _gradient_bar(draw, bar_x, bar_y, bar_w, bar_h, fill_w)
    if card["riskFill"] is not None:
        mx = bar_x + max(14, min(bar_w - 14, fill_w))
        cy = bar_y + bar_h / 2
        draw.ellipse((mx - 12, cy - 12, mx + 12, cy + 12), fill="#f4fbf6", outline=_risk_tone(fill), width=2)
    draw.text((x + width, row_y + 22), value, fill=_risk_tone(fill), font=vf, anchor="rm")
    if note:
        draw.text((x, y + 132), note, fill=C["muted"], font=font(20), anchor="lm")


def _gradient_bar(draw, x: int, y: int, w: float, h: int, fill_w: float) -> None:
    """Verde → ámbar → rojo (misma rampa que el póster del navegador), recortado a fill_w."""
    stops = [(0.0, (0x3E, 0xCF, 0x8E)), (0.45, (0xE7, 0xC5, 0x6A)), (0.78, (0xF0, 0x71, 0x71)), (1.0, (0xCD, 0x18, 0x18))]
    steps = max(1, int(fill_w))
    for i in range(steps):
        t = i / max(1, w - 1)
        col = _lerp_stops(stops, t)
        draw.line((x + i, y + 2, x + i, y + h - 2), fill=col)
    # Redondeo en los extremos: tapar esquinas con el color de la pista.
    draw.rounded_rectangle((x, y, x + w, y + h), radius=18, outline=C["surface"], width=1)


def _lerp_stops(stops, t: float) -> tuple[int, int, int]:
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t <= t1:
            k = 0 if t1 == t0 else (t - t0) / (t1 - t0)
            return tuple(int(round(a + (b - a) * k)) for a, b in zip(c0, c1))
    return stops[-1][1]


def _draw_level(draw, level: dict, box: dict) -> None:
    _panel(draw, (box["x"], box["y"], box["w"], box["h"]), C["border"])
    kf = font(15, True)
    draw.text((box["x"] + 14, box["y"] + 16), fit(draw, level["label"].upper(), box["w"] - 28, kf), fill=C["pink"], font=kf)
    col = C["gain"] if level["tone"] == "gain" else C["loss"] if level["tone"] == "loss" else C["text"]
    for i, line in enumerate(box["value_lines"]):
        draw.text((box["x"] + 14, box["y"] + 42 + i * 32), line, fill=col, font=font(26, True))


def _draw_scenario(draw, sc: dict, box: dict) -> None:
    tone = C["loss"] if sc["tone"] == "loss" else C["gain"]
    _panel(draw, (box["x"], box["y"], box["w"], box["h"]), tone)
    y = box["y"] + 16
    for line in box["title_lines"]:
        draw.text((box["x"] + 16, y), line, fill=tone, font=font(20, True))
        y += 28
    y += 4
    bf = font(18)
    for lines in box["bullets"]:
        draw.text((box["x"] + 16, y), "✓", fill=tone, font=bf)
        for li, line in enumerate(lines):
            draw.text((box["x"] + 38, y + li * 26), line, fill=C["text"], font=bf)
        y += len(lines) * 26 + 8


# --------------------------------------------------------------------------- CLI
def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", required=True, help="JSON con la tarjeta (ShareCardModel + chart)")
    ap.add_argument("--out", required=True, help="PNG de salida")
    args = ap.parse_args(argv)
    try:
        spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
        result = render_signal_card(spec, args.out)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
