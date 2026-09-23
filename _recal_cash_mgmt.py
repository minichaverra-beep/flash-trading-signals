# -*- coding: utf-8 -*-
"""Recalibrate Cash-Management HTML with mobile OCR ground-truth + SL 30 pips."""
from pathlib import Path
import re

html_path = Path("artifacts/Cash-Management-Danilo-E1.html")
t = html_path.read_text(encoding="utf-8")

# --- Global SL $ → 30 pips ---
replacements = [
    (
        "SL cuenta ~<b>$9</b> fijo — nunca expandir. Máx. 3 ops/día. <b>2 SL = fin de sesión</b>. Tope diario definido antes de operar.",
        "SL mínimo <b>30 pips</b> (estructura) — nunca expandir. Máx. 3 ops/día. <b>2 SL = fin de sesión</b>. Tope diario definido antes de operar.",
    ),
    (
        "SL ~$9 fijo. BE en 1:1 cuando el precio respiró. Cerrar 1:1 si salva el día. Nunca añadir en negativo ni expandir SL.",
        "SL mínimo <b>30 pips</b>. BE en 1:1 cuando el precio respiró. Cerrar 1:1 si salva el día. Nunca añadir en negativo ni expandir SL.",
    ),
    (
        "3 · SL ~$9 fijo<b>Nunca expandir</b>",
        "3 · SL mín. 30 pips<b>Nunca expandir</b>",
    ),
    (
        "Proyecciones con riesgo fijo $9 / win ≈ $18 asumen fills limpios. Slippage, comisiones y BE no están en el núcleo del PF 4,77 — tratar proyecciones como techo optimista.",
        "Proyecciones en <b>R</b> (R:R 1:2) asumen fills limpios y SL ≥30 pips. Slippage, comisiones y BE no están en el núcleo del PF 4,77 — tratar USD como ilustrativo según tamaño de cuenta.",
    ),
    (
        "Modelo conservador E1 only · riesgo $9.",
        "Modelo conservador E1 only · SL ≥30 pips · R:R 1:2.",
    ),
    (
        "*Ganador ≈ $18 · perdedor $9. Fuente: TRADING_PROFESSIONAL_STATS.md §11.",
        "*1R = distancia SL (≥30 pips). Ganador ≈ 2R. Fuente: PROFESSIONAL_STATS §11 + ground-truth móvil v_ops_apr_sep.",
    ),
    (
        "Alineado a SL~$9 en cuentas tipo 50k–100k challenge",
        "Alineado a SL ≥30 pips · riesgo ~1% del capital del mandato",
    ),
    (
        '<p class="kicker">Bitácora trading v2 · corte sep 2026</p>',
        '<p class="kicker">Bitácora v2 · OCR móvil abr–sep 2026 · commit 2041deb</p>',
    ),
    (
        "Perfil del trader, histórico de la bitácora (Notion + desktop), modelos de riesgo derivados del backtesting real y condiciones de mandato propuestas. Sin mezclar aspiración con AUM actual: aquí están los números que sí existen.",
        "Perfil del trader, histórico Notion/desktop y <b>ground-truth OCR</b> de capturas del celular (abr–sep 2026), modelos de riesgo y condiciones de mandato. Sin mezclar aspiración con AUM actual.",
    ),
]

for i, (old, new) in enumerate(replacements, 1):
    if old not in t:
        print(f"MISSING #{i}")
    else:
        t = t.replace(old, new)
        print(f"OK #{i}")

# Projection table USD column → R framing
old_table = """      <table>
        <thead><tr><th>Trades / mes</th><th>R esperado</th><th>USD esperado*</th><th>Notas</th></tr></thead>
        <tbody>
          <tr><td>20</td><td>+25 R</td><td>~$225</td><td>Ritmo bajo</td></tr>
          <tr><td>40</td><td>+50 R</td><td>~$450</td><td>Base sostenible</td></tr>
          <tr><td>60</td><td>+75 R</td><td>~$675</td><td>3 ops × 20 días (techo plan)</td></tr>
        </tbody>
      </table>"""

new_table = """      <table>
        <thead><tr><th>Trades / mes</th><th>R esperado</th><th>1R = SL (≥30 pips)</th><th>Notas</th></tr></thead>
        <tbody>
          <tr><td>20</td><td>+25 R</td><td>25 × 1R en $ cuenta</td><td>Ritmo bajo</td></tr>
          <tr><td>40</td><td>+50 R</td><td>50 × 1R en $ cuenta</td><td>Base sostenible</td></tr>
          <tr><td>60</td><td>+75 R</td><td>75 × 1R en $ cuenta</td><td>3 ops × 20 días (techo plan)</td></tr>
        </tbody>
      </table>"""

if old_table in t:
    t = t.replace(old_table, new_table)
    print("OK projection table")
else:
    print("MISSING projection table")

# Also fix kit line "1 · Solo E1" section if any leftover $9
if "$9" in t:
    print("REMAINING $9 snippets:")
    for m in re.finditer(r".{0,40}\$9.{0,40}", t):
        print(" ", m.group(0).replace("\n", " "))

# Insert new section before #contacto (or after #track)
mobile_section = """
<section class="sec" id="ops-mobile">
  <div class="wrap">
    <div class="head reveal">
      <p class="eyebrow">02b — Ground truth móvil (OCR)</p>
      <h2>Operaciones del celular · abr–sep 2026.</h2>
      <p class="lede">Dataset versionado <span class="mono">data/ops_mobile/v_ops_apr_sep</span> (commit <span class="mono">2041deb</span>). OCR RapidOCR sobre 102 capturas TV/Exness/WA — <b>sin re-escanear</b> en este corte. No se inventan trades.</p>
    </div>

    <div class="g2" style="margin-bottom:28px">
      <div class="card reveal">
        <h3>Calidad OCR</h3>
        <ul class="metrics">
          <li>Imágenes escaneadas<b>102</b></li>
          <li>Trades tras dedupe<b>100</b></li>
          <li>Alta confianza (≥0,70)<b>91%</b></li>
          <li>Con entry / SL / TP<b>93 / 65 / 90</b></li>
          <li>Problemáticas<b>23</b></li>
          <li>BTCUSDT / US30 / XAU<b>91 / 2 / 4</b></li>
          <li>Quantity / PnL en chart<b>casi siempre null</b></li>
          <li>BTCUSDT_REVIEW (&lt;56k)<b>11 · revisión manual</b></li>
        </ul>
      </div>
      <div class="card reveal">
        <h3>Match ML → velas M5 (BTC)</h3>
        <ul class="metrics">
          <li>Ops candidatas / matched<b>63 / 53</b></li>
          <li>WR ground-truth matched<b class="up">62,3%</b></li>
          <li>Wins / Losses<b>33 / 20</b></li>
          <li>Labels real_sl_tp / fixed_rr<b>36 / 17</b></li>
          <li>Error precio medio al bar<b>0,026%</b></li>
          <li>US30 matches<b>0</b> <span class="note">(cache M5 corto)</span></li>
          <li>Visión mobile_simple acc<b>~0,80</b></li>
          <li>Modelo BTC F1 after ops<b>0,54 (+0,12)</b></li>
        </ul>
      </div>
    </div>

    <h3 style="font-family:var(--disp);font-size:24px;margin-bottom:14px" class="reveal">WR matched BTC por mes (ground truth)</h3>
    <div class="scroll reveal" style="background:var(--card);border:1px solid var(--rule);padding:16px 18px;margin-bottom:22px">
      <table>
        <thead><tr><th>Mes</th><th>n matched</th><th>WR</th></tr></thead>
        <tbody>
          <tr><td>Mar 2026</td><td>2</td><td>0%</td></tr>
          <tr><td>May 2026</td><td>3</td><td>66,7%</td></tr>
          <tr><td>Jun 2026</td><td>9</td><td>88,9%</td></tr>
          <tr><td>Jul 2026</td><td>5</td><td>40,0%</td></tr>
          <tr><td>Ago 2026</td><td>25</td><td>64,0%</td></tr>
          <tr><td>Sep 2026</td><td>9</td><td>55,6%</td></tr>
          <tr><td><b>TOTAL matched</b></td><td><b>53</b></td><td><b>62,3%</b></td></tr>
        </tbody>
      </table>
    </div>

    <div class="g2">
      <div class="card reveal">
        <h3>SL observado (BTCUSDT OCR)</h3>
        <p>Entre filas con entry+SL (n=57): mediana distancia <b>~234</b> (puntos precio) · p25 ~130 · mín. documentado ~38. <b>Ningún SL OCR &lt; 30 pips</b> en el subset con SL legible — alineado a la regla operativa actual.</p>
        <p class="note">RR planificado mediano (OCR) ≈ 1,80 · long/short en BTC: 36 / 27.</p>
      </div>
      <div class="card reveal">
        <h3>Lift ML tabular (BTC, --quick)</h3>
        <div class="scroll">
          <table>
            <thead><tr><th>Métrica</th><th>Before</th><th>After</th><th>Δ</th></tr></thead>
            <tbody>
              <tr><td>Accuracy</td><td>0,508</td><td>0,564</td><td class="up">+0,056</td></tr>
              <tr><td>Precision</td><td>0,467</td><td>0,548</td><td class="up">+0,082</td></tr>
              <tr><td>Recall</td><td>0,375</td><td>0,531</td><td class="up">+0,156</td></tr>
              <tr><td>F1</td><td>0,416</td><td>0,540</td><td class="up">+0,124</td></tr>
            </tbody>
          </table>
        </div>
        <p class="note" style="margin-top:10px">Fuente: ml_ops_integration_report.md · repo flash-trading-signals.</p>
      </div>
    </div>

    <div class="callout reveal" style="margin-top:22px">
      <span class="pill">v_ops_apr_sep</span><span class="pill">OCR versionado</span>
      Recalibración del dossier: el WR móvil matched (62,3%) es <b>complementario</b> al WR Notion E1 (75%) — distinta ventana, fills reales y labels por SL/TP o R:R fijo. US30 aún sin matches OCR suficientes.
    </div>
  </div>
</section>
"""

anchor = '<section class="sec" id="metodo">'
if anchor in t and 'id="ops-mobile"' not in t:
    t = t.replace(anchor, mobile_section + "\n" + anchor)
    print("OK inserted ops-mobile section")
elif 'id="ops-mobile"' in t:
    # replace existing section
    t = re.sub(
        r'<section class="sec" id="ops-mobile">.*?</section>\s*',
        mobile_section + "\n",
        t,
        count=1,
        flags=re.S,
    )
    print("OK replaced ops-mobile section")
else:
    print("FAIL insert ops-mobile")

# Nav link
old_nav = """      <a href="#track">Track record</a>
      <a href="#metodo">Método</a>"""
new_nav = """      <a href="#track">Track record</a>
      <a href="#ops-mobile">OCR móvil</a>
      <a href="#metodo">Método</a>"""
if old_nav in t:
    t = t.replace(old_nav, new_nav)
    print("OK nav")

# KPI strip — add mobile WR hint in 4th or update subtitle
t = t.replace(
    '<div><span class="k">Day win E1</span><span class="v">~84%</span><span class="s">días positivos sesión</span></div>',
    '<div><span class="k">WR OCR matched BTC</span><span class="v">62%</span><span class="s">53 fills · celular</span></div>',
)

# Mandatos límites line
t = t.replace(
    "<b>Límites comprometidos en cualquier mandato:</b> BTC/US30 · NY · nunca expandir SL · un mercado a la vez · titularidad y riesgo explícitos antes de la primera operación.",
    "<b>Límites comprometidos en cualquier mandato:</b> BTC/US30 · NY · SL ≥ <b>30 pips</b> (nunca expandir) · un mercado a la vez · titularidad y riesgo explícitos antes de la primera operación.",
)

# Documentation card — add mobile dataset
old_doc = """        <p class="note">Local: Cursor Trading/docs/strategy/TRADING_PROFESSIONAL_STATS.md</p>"""
new_doc = """        <p class="note">Local: docs/strategy/TRADING_PROFESSIONAL_STATS.md · data/ops_mobile/v_ops_apr_sep/</p>
        <p class="note">GitHub: flash-trading-signals @ 2041deb · OCR + ML ground-truth</p>"""
if old_doc in t:
    t = t.replace(old_doc, new_doc)
    print("OK docs")

# Disclaimer footer refresh
t = t.replace(
    "Resultados pasados (PF 4,77, WR 67–75%, +$2.843 en 9 meses) no garantizan resultados futuros.",
    "Resultados pasados (PF 4,77, WR Notion 67–75%, WR OCR matched BTC 62%, +$2.843 en 9 meses) no garantizan resultados futuros.",
)

# Risk model card about 1 SL ≈ $15 — keep psychology dollars as illustrative OR reframe
# Leave psychology $15 as historical note from bitácora tips; optional soften
t = t.replace(
    "<li>1 SL E1 ≈<b>~$15</b></li>",
    "<li>1 SL E1 (legado tip)<b>≥30 pips</b></li>",
)
t = t.replace(
    "<li>Día malo E1 ≈<b>−$15</b></li>",
    "<li>Día malo E1 (legado)<b>~−1–2R</b></li>",
)

html_path.write_text(t, encoding="utf-8")
print("wrote", html_path.name, "bytes", html_path.stat().st_size)
left = len(re.findall(r"\$9", t))
print("remaining $9 count:", left)
