# -*- coding: utf-8 -*-
from pathlib import Path

p = Path("artifacts/Cash-Management-Danilo-E1.html")
t = p.read_text(encoding="utf-8")
reps = [
    ("51 matched · abr–sep", "51 emparejados · abr–sep"),
    ("stack live BTC / US30 en Cursor.", "sistema en vivo BTC / US30 en Cursor."),
    (
        "El edge documentado es <b>E1 Flopy-Scalping</b>",
        "La ventaja documentada es <b>E1 Flopy-Scalping</b>",
    ),
    ("queda ocasional u OFF en fondeo.", "queda ocasional o desactivado en fondeo."),
    ("Scalping / day en M5.", "Scalping intradía en M5."),
    ("reportes live + OCR", "reportes en vivo + OCR"),
    ("E2 ≤10% / OFF eval", "E2 ≤10% / desact. en eval"),
    ("Capa A · Visual Context", "Capa A · Contexto visual"),
    ("matched BTC <b>51</b>", "emparejados BTC <b>51</b>"),
    (
        "<th>WIN</th><th>LOSS</th><th>OPEN</th>",
        "<th>Ganadas</th><th>Perdidas</th><th>Abiertas</th>",
    ),
    (
        "Composición del edge (calibración High)",
        "Composición de la ventaja (calibración High)",
    ),
    ("WR ground-truth ventana", "WR referencia de campo (ventana)"),
    ("WR matched BTC por mes", "WR emparejado BTC por mes"),
    ("<th>n matched</th>", "<th>n emparejados</th>"),
    ("Mar 2026 (2 matched, 0% WR)", "Mar 2026 (2 emparejados, 0% WR)"),
    ("matched BTC n=51", "emparejados BTC n=51"),
    (
        'aria-label="Donut cobertura matched"',
        'aria-label="Donut cobertura emparejada"',
    ),
    ("<tr><td>Accuracy</td>", "<tr><td>Exactitud</td>"),
    ("<tr><td>Precision</td>", "<tr><td>Precisión</td>"),
    ("<tr><td>Recall</td>", "<tr><td>Sensibilidad</td>"),
    ("<th>Before</th><th>After</th>", "<th>Antes</th><th>Después</th>"),
    ("fills reales", "ejecuciones reales"),
    (
        "El stack live genera Context/High/History",
        "El sistema en vivo genera Contexto / High / Historial",
    ),
    ("hard gate H1 / CTR", "filtro obligatorio H1 / CTR"),
    ("Hard gate", "Filtro obligatorio"),
    ("galería WIN como referencia", "galería de aciertos como referencia"),
    ("Opcional / OFF eval", "Opcional / desact. en eval"),
    ("Fallas primarias en LOSS", "Fallas primarias en pérdida"),
    ("fills limpios", "ejecuciones limpias"),
    ("ground-truth móvil", "referencia móvil"),
    ("E2 <b>OFF</b>", "E2 <b>Desactivado</b>"),
    ("E2 <b>OFF en eval</b>", "E2 <b>Desactivado en eval</b>"),
    ("OCR + ML ground-truth", "OCR + ML referencia de campo"),
    ("<h3>Stack live</h3>", "<h3>Sistema en vivo</h3>"),
    (
        "Analyze Context / High / History · ML tabular · Neural galería WIN · Ilustrate 2M5.",
        "Análisis Contexto / High / Historial · ML tabular · Neural galería de aciertos · Ilustrar 2M5.",
    ),
    ("WR OCR matched BTC ventana", "WR OCR emparejado BTC ventana"),
    ("con edge medido", "con ventaja medida"),
    ("el edge se diluye", "la ventaja se diluye"),
    ("el edge no depende", "la ventaja no depende"),
    ("Rules &lt;60%", "Reglas &lt;60%"),
    ("bias de la sesión", "sesgo de la sesión"),
]
n = 0
miss = []
for a, b in reps:
    if a in t:
        t = t.replace(a, b)
        n += 1
    else:
        miss.append(a[:70])
p.write_text(t, encoding="utf-8")
print("replaced", n, "of", len(reps))
for m in miss:
    print("MISS", m)
