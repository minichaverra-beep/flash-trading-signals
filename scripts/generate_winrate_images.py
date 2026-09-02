"""Generate win rate and KPI chart images for trading stats."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from app.config import IMAGES_DIR

OUTPUT_DIR = IMAGES_DIR / "winrate"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DATE_LABEL = "2026-08-31"
BG = "#1e1e1e"
HEADER_BG = "#2d2d30"
ROW_ALT = "#252526"
TEXT = "#e0e0e0"
GREEN = "#4ec9b0"
RED = "#f48771"
ACCENT = "#569cd6"
GOLD = "#dcdcaa"
BORDER = "#3e3e42"


def style_table(table, col_widths=None):
    cells = table.get_celld()
    nrows = max(r for r, _ in cells) + 1

    for (row, col), cell in cells.items():
        cell.set_edgecolor(BORDER)
        cell.set_linewidth(0.8)
        cell.set_text_props(color=TEXT, fontsize=11)

        if row == 0:
            cell.set_facecolor(HEADER_BG)
            cell.set_text_props(weight="bold", color=ACCENT, fontsize=11)
        elif row % 2 == 0:
            cell.set_facecolor(ROW_ALT)
        else:
            cell.set_facecolor(BG)

        text = cell.get_text().get_text()
        if "%" in text and row > 0:
            try:
                val = float(text.replace("%", "").strip())
                color = GREEN if val >= 65 else (TEXT if val >= 55 else RED)
                cell.get_text().set_color(color)
                cell.get_text().set_weight("bold")
            except ValueError:
                pass

    if col_widths:
        for col, w in enumerate(col_widths):
            for row in range(nrows):
                cells[(row, col)].set_width(w)


def save_figure(fig, filename):
    path = OUTPUT_DIR / filename
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close(fig)
    return path


def add_title(fig, title, subtitle=None, y=0.95):
    fig.text(0.5, y, title, ha="center", va="top", fontsize=16,
             fontweight="bold", color=ACCENT, fontfamily="sans-serif")
    if subtitle:
        fig.text(0.5, y - 0.05, subtitle, ha="center", va="top", fontsize=10,
                 color="#888888", fontfamily="sans-serif")


def footer(fig, text):
    fig.text(0.5, 0.01, text, ha="center", va="center", fontsize=9, color="#666666")


def create_global_image():
    fig = plt.figure(figsize=(10, 7), facecolor=BG)
    add_title(fig, "Win Rate — Resumen Global", "Notion Historial de Trades (349 trades, excl. template)")

    global_data = [
        ["Métrica", "Valor"],
        ["WIN", "234"],
        ["LOSS", "115"],
        ["BE", "0"],
        ["Total", "349"],
        ["Win Rate", "67.0%"],
    ]

    ax1 = fig.add_axes([0.08, 0.55, 0.35, 0.30])
    ax1.axis("off")
    t1 = ax1.table(cellText=global_data[1:], colLabels=global_data[0],
                   loc="center", cellLoc="center")
    t1.auto_set_font_size(False)
    t1.set_fontsize(11)
    t1.scale(1.2, 1.8)
    style_table(t1, [0.45, 0.35])
    ax1.set_title("Global", color=TEXT, fontsize=12, pad=8, fontweight="bold")

    asset_data = [
        ["Activo", "WIN", "LOSS", "Total", "WR"],
        ["BTC", "49", "22", "71", "69.0%"],
        ["US30", "51", "28", "79", "64.6%"],
        ["BTC+US30", "100", "50", "150", "66.7%"],
    ]

    ax2 = fig.add_axes([0.52, 0.40, 0.44, 0.45])
    ax2.axis("off")
    t2 = ax2.table(cellText=asset_data[1:], colLabels=asset_data[0],
                   loc="center", cellLoc="center")
    t2.auto_set_font_size(False)
    t2.set_fontsize(11)
    t2.scale(1.0, 1.8)
    style_table(t2)
    ax2.set_title("Por Activo", color=TEXT, fontsize=12, pad=8, fontweight="bold")

    fig.text(0.5, 0.12,
             "Período reciente (jul 2025+): 208 WIN · 107 LOSS · 315 total → WR 66.0%",
             ha="center", va="center", fontsize=11, color=GREEN, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.5", facecolor=HEADER_BG, edgecolor=BORDER))

    footer(fig, f"Fuente: Notion — Historial de Trades  |  Fecha: {DATE_LABEL}")
    return save_figure(fig, "winrate-global.png")


def create_estrategia_image():
    fig = plt.figure(figsize=(10, 5.5), facecolor=BG)
    add_title(fig, "Win Rate — E1 vs E2 (Proxy Confluencias)",
              "Clasificación por tipo de estrategia · Expectativa @ R:R 1:2")

    data = [
        ["Estrategia", "WIN", "LOSS", "Total", "WR", "Exp. R"],
        ["Continuación (E1)", "129", "43", "172", "75.0%", "+1.25R"],
        ["Reversión (E2)", "70", "41", "111", "63.1%", "+0.89R"],
        ["E2 BTC", "11", "7", "18", "61.1%", "+0.83R"],
        ["E2 US30", "14", "15", "29", "48.3%", "+0.45R"],
    ]

    ax = fig.add_axes([0.06, 0.20, 0.88, 0.55])
    ax.axis("off")
    table = ax.table(cellText=data[1:], colLabels=data[0],
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.0, 2.0)
    style_table(table, [0.28, 0.10, 0.10, 0.10, 0.12, 0.12])

    fig.text(0.5, 0.08,
             "E1 supera E2 · PF E1 = 4.77 vs PF global 3.16 · E2 US30 bajo breakeven operativo",
             ha="center", va="center", fontsize=10, color=GREEN, fontweight="bold")

    footer(fig, f"Fuente: Notion — Proxy por Confluencias  |  Fecha: {DATE_LABEL}")
    return save_figure(fig, "winrate-estrategia.png")


def create_fuentes_image():
    fig = plt.figure(figsize=(10, 5.8), facecolor=BG)
    add_title(fig, "Win Rate — Comparación entre Fuentes",
              "Consolidado TRADING_PROFESSIONAL_STATS.md")

    data = [
        ["Fuente", "Período", "WIN", "LOSS", "Total", "WR", "Notas"],
        ["Notion (global)", "Histórico", "234", "115", "349", "67.0%", "Excl. template"],
        ["Notion (reciente)", "Jul 2025+", "208", "107", "315", "66.0%", "Estable"],
        ["Desktop", "Abr–Ago 2026", "74", "30", "104", "71.2%", "112 capturas"],
        ["Visual Context", "9 meses", "—", "—", "272", "65.1%", "E1+E2"],
        ["Visual Context", "9 meses", "—", "—", "242", "73.1%", "Solo E1"],
    ]

    ax = fig.add_axes([0.03, 0.18, 0.94, 0.58])
    ax.axis("off")
    table = ax.table(cellText=data[1:], colLabels=data[0],
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.0, 1.9)
    style_table(table, [0.18, 0.12, 0.08, 0.08, 0.08, 0.10, 0.22])

    fig.text(0.5, 0.06,
             "Rango WR consolidado: 65% – 75%  |  Desktop reciente: 71.2% (mejor disciplina jul–ago)",
             ha="center", va="center", fontsize=10, color=GREEN, fontweight="bold")

    footer(fig, f"Fuentes: Notion · Desktop · Visual Context  |  Fecha: {DATE_LABEL}")
    return save_figure(fig, "winrate-fuentes.png")


def create_kpi_dashboard():
    fig = plt.figure(figsize=(12, 8), facecolor=BG)
    add_title(fig, "KPI Dashboard — Plan Trading Danilo",
              "Consolidado 5 archivos MD · BTC · US30 · E1 CRT · Sesión NY", y=0.97)

    kpi_data = [
        ["KPI", "Valor", "Estado"],
        ["Win Rate Global (Notion)", "67.0%", "349 trades"],
        ["Win Rate E1", "75.0%", "Edge principal"],
        ["Win Rate E2", "63.1%", "E2 US30 48.3%"],
        ["Profit Factor (9m)", "3.16", "Excelente"],
        ["PF Solo E1", "4.77", "Profesional"],
        ["P&L 9 meses", "+$2,843", "272 trades"],
        ["P&L Solo E1", "+$3,287", "E2 −$444"],
        ["Day Win E1", "~84%", "Días positivos"],
        ["Desktop WR 2026", "71.2%", "74W / 30L"],
        ["Expectativa E1 @ 1:2", "+1.25 R", "Breakeven 33%"],
        ["Cumplimiento plan", "~74%", "Disciplina = gap"],
    ]

    ax = fig.add_axes([0.05, 0.42, 0.90, 0.48])
    ax.axis("off")
    table = ax.table(cellText=kpi_data[1:], colLabels=kpi_data[0],
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.0, 1.7)
    style_table(table, [0.40, 0.25, 0.35])

    scenarios = ["Notion\nGlobal", "Notion\nReciente", "Visual\nE1+E2", "Visual\nSolo E1", "Desktop\n2026"]
    wr_values = [67.0, 66.0, 65.1, 73.1, 71.2]
    colors = [ACCENT if v >= 67 else GOLD if v >= 65 else RED for v in wr_values]

    ax_bar = fig.add_axes([0.10, 0.08, 0.80, 0.28])
    ax_bar.set_facecolor(BG)
    bars = ax_bar.bar(scenarios, wr_values, color=colors, edgecolor=BORDER, linewidth=0.8)
    ax_bar.axhline(67, color=GREEN, linestyle="--", linewidth=1, alpha=0.6)
    ax_bar.set_ylabel("Win Rate %", color=TEXT)
    ax_bar.set_ylim(0, 85)
    ax_bar.tick_params(colors=TEXT)
    ax_bar.spines["bottom"].set_color(BORDER)
    ax_bar.spines["left"].set_color(BORDER)
    ax_bar.spines["top"].set_visible(False)
    ax_bar.spines["right"].set_visible(False)

    for bar, val in zip(bars, wr_values):
        ax_bar.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                    f"{val}%", ha="center", va="bottom", color=TEXT, fontsize=10, fontweight="bold")

    footer(fig, f"TRADING_PROFESSIONAL_STATS.md  |  Fecha: {DATE_LABEL}")
    return save_figure(fig, "winrate-kpi-dashboard.png")


def create_desktop_mensual():
    months = ["Abr\n2026", "May\n2026", "Jun\n2026", "Jul\n2026", "Ago\n2026"]
    wins = [8, 23, 20, 21, 2]
    losses = [1, 16, 9, 4, 0]
    wr = [w / (w + l) * 100 if (w + l) else 0 for w, l in zip(wins, losses)]

    fig = plt.figure(figsize=(11, 6), facecolor=BG)
    add_title(fig, "Win Rate Mensual — Desktop 2026",
              "Galería operaciones · 74 WIN · 30 LOSS · 71.2% global")

    ax1 = fig.add_axes([0.08, 0.38, 0.84, 0.48])
    ax1.set_facecolor(BG)
    x = list(range(len(months)))
    w1 = 0.35
    ax1.bar([i - w1 / 2 for i in x], wins, w1, label="WIN", color=GREEN, edgecolor=BORDER)
    ax1.bar([i + w1 / 2 for i in x], losses, w1, label="LOSS", color=RED, edgecolor=BORDER)
    ax1.set_xticks(x)
    ax1.set_xticklabels(months, color=TEXT)
    ax1.set_ylabel("Trades", color=TEXT)
    ax1.tick_params(colors=TEXT)
    ax1.legend(facecolor=HEADER_BG, edgecolor=BORDER, labelcolor=TEXT, loc="upper right")
    ax1.spines["bottom"].set_color(BORDER)
    ax1.spines["left"].set_color(BORDER)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    ax2 = fig.add_axes([0.08, 0.12, 0.84, 0.22])
    ax2.set_facecolor(BG)
    wr_colors = [GREEN if v >= 70 else (GOLD if v >= 60 else RED) for v in wr]
    ax2.plot(x, wr, color=ACCENT, marker="o", linewidth=2, markersize=8, zorder=3)
    ax2.bar(x, wr, color=wr_colors, alpha=0.35, edgecolor=BORDER, linewidth=0.5)
    ax2.axhline(71.2, color=GREEN, linestyle="--", linewidth=1, alpha=0.7)
    ax2.set_xticks(x)
    ax2.set_xticklabels(months, color=TEXT)
    ax2.set_ylabel("WR %", color=TEXT)
    ax2.set_ylim(0, 100)
    ax2.tick_params(colors=TEXT)
    ax2.spines["bottom"].set_color(BORDER)
    ax2.spines["left"].set_color(BORDER)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    for i, v in enumerate(wr):
        ax2.text(i, v + 3, f"{v:.1f}%", ha="center", color=TEXT, fontsize=10, fontweight="bold")

    fig.text(0.5, 0.04,
             "Mejor: Jul 84% · Peor: May 59% (bias contrario + sobreoperar)",
             ha="center", color=GOLD, fontsize=10, fontweight="bold")

    footer(fig, f"Fuente: TRADING_OPERATIONS_DESKTOP_CONTEXT.md  |  Fecha: {DATE_LABEL}")
    return save_figure(fig, "winrate-desktop-mensual.png")


def create_pf_mensual():
    months = ["Jul\n25", "Ago\n25", "Sep\n25", "Oct\n25", "Nov\n25", "Dic–Mar\n26"]
    pf = [1.85, 3.40, 5.89, 2.55, 4.84, 2.51]
    pnl = [172, 410, 384, 299, 933, 645]

    fig = plt.figure(figsize=(11, 6.5), facecolor=BG)
    add_title(fig, "Profit Factor & P&L Mensual — 9 Meses",
              "272 trades · WR 65.1% · PF 3.16 · P&L +$2,843")

    ax1 = fig.add_axes([0.08, 0.40, 0.84, 0.45])
    ax1.set_facecolor(BG)
    x = list(range(len(months)))
    pf_colors = [GREEN if p >= 3 else (GOLD if p >= 2 else RED) for p in pf]
    bars = ax1.bar(x, pf, color=pf_colors, edgecolor=BORDER, linewidth=0.8)
    ax1.axhline(2.0, color=ACCENT, linestyle="--", linewidth=1, alpha=0.7, label="PF 2.0 (excelente)")
    ax1.axhline(4.77, color=GREEN, linestyle=":", linewidth=1, alpha=0.5, label="PF E1 = 4.77")
    ax1.set_xticks(x)
    ax1.set_xticklabels(months, color=TEXT)
    ax1.set_ylabel("Profit Factor", color=TEXT)
    ax1.tick_params(colors=TEXT)
    ax1.legend(facecolor=HEADER_BG, edgecolor=BORDER, labelcolor=TEXT, loc="upper left", fontsize=9)
    ax1.spines["bottom"].set_color(BORDER)
    ax1.spines["left"].set_color(BORDER)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    for bar, val in zip(bars, pf):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.08,
                 f"{val:.2f}", ha="center", color=TEXT, fontsize=10, fontweight="bold")

    ax2 = fig.add_axes([0.08, 0.12, 0.84, 0.22])
    ax2.set_facecolor(BG)
    ax2.bar(x, pnl, color=[GREEN if p >= 400 else ACCENT for p in pnl], edgecolor=BORDER)
    ax2.set_xticks(x)
    ax2.set_xticklabels(months, color=TEXT)
    ax2.set_ylabel("P&L $", color=TEXT)
    ax2.tick_params(colors=TEXT)
    ax2.spines["bottom"].set_color(BORDER)
    ax2.spines["left"].set_color(BORDER)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    for i, v in enumerate(pnl):
        ax2.text(i, v + 15, f"+${v}", ha="center", color=GREEN, fontsize=9, fontweight="bold")

    fig.text(0.5, 0.04,
             "Mejor mes: Nov +$933 (PF 4.84) · Más limpio: Sep PF 5.89 · Peor: Jul PF 1.85",
             ha="center", color=GOLD, fontsize=10, fontweight="bold")

    footer(fig, f"Fuente: TRADING_VISUAL_CONTEXT.md  |  Fecha: {DATE_LABEL}")
    return save_figure(fig, "winrate-pf-mensual.png")


def create_e1_vs_e2_pf():
    fig = plt.figure(figsize=(10, 5.5), facecolor=BG)
    add_title(fig, "E1 vs E2 — Impacto en Rentabilidad (9 meses)",
              "242 trades E1 · 30 trades E2")

    data = [
        ["Escenario", "Trades", "WR", "PF", "P&L neto"],
        ["E1 + E2 (todo)", "272", "65.1%", "3.16", "+$2,843"],
        ["Solo E1", "242", "73.1%", "4.77", "+$3,287"],
        ["Solo E2", "30", "—", "—", "−$444"],
    ]

    ax = fig.add_axes([0.08, 0.22, 0.84, 0.58])
    ax.axis("off")
    table = ax.table(cellText=data[1:], colLabels=data[0], loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.0, 2.2)
    style_table(table, [0.22, 0.12, 0.12, 0.12, 0.18])

    fig.text(0.5, 0.08,
             "Operar solo E1 en eval → PF ~4.0  |  E2 restó ~13% del profit total",
             ha="center", color=GREEN, fontsize=11, fontweight="bold")

    footer(fig, f"Fuente: TRADING_VISUAL_CONTEXT.md  |  Fecha: {DATE_LABEL}")
    return save_figure(fig, "winrate-e1-e2-pf.png")


if __name__ == "__main__":
    creators = [
        create_global_image,
        create_estrategia_image,
        create_fuentes_image,
        create_kpi_dashboard,
        create_desktop_mensual,
        create_pf_mensual,
        create_e1_vs_e2_pf,
    ]
    for fn in creators:
        path = fn()
        print(f"Created: {path} ({path.stat().st_size:,} bytes)")
