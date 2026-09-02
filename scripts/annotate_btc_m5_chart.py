"""Annotate live/btc_m5_chart.png → live/btc_m5_chart_annotated.png for 2M5 SHORT guide."""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

from app.config import PROJECT_ROOT, LIVE_DIR, DATA_DIR, MODELS_DIR, TRAINING_NEURAL_DIR

BASE = PROJECT_ROOT
sys.path.insert(0, str(BASE))

from app.controllers.analyze_btc_m5 import fetch_klines, nearest_zone, save_chart  # noqa: E402

OUT = BASE / "live" / "btc_m5_chart_annotated.png"
RESISTANCE = 77444.0
ENTRY_OPT = 77400.0
SL_STRUCT = RESISTANCE * 1.002
TP_2R = ENTRY_OPT - 2 * (SL_STRUCT - ENTRY_OPT)
ZONE_EDGE = 77328.0  # ~0.15% below resistance at retest


def save_annotated_chart(m5: list[dict], path: Path, title: str) -> None:
    fig, ax = plt.subplots(figsize=(12, 5.5), facecolor="#1e1e1e")
    ax.set_facecolor("#1e1e1e")
    show = m5[-60:]
    n = len(show)

    for i, c in enumerate(show):
        color = "#4ec9b0" if c["close"] >= c["open"] else "#f48771"
        ax.plot([i, i], [c["low"], c["high"]], color=color, linewidth=0.8)
        bottom = min(c["open"], c["close"])
        height = abs(c["close"] - c["open"]) or (c["high"] - c["low"]) * 0.01
        ax.add_patch(Rectangle((i - 0.3, bottom), 0.6, height, facecolor=color, edgecolor=color))

    # Highlight last 2 candles (2M5 actuales — lejos de zona)
    for idx in (n - 2, n - 1):
        c = show[idx]
        ax.add_patch(
            Rectangle(
                (idx - 0.42, c["low"]),
                0.84,
                c["high"] - c["low"],
                linewidth=2.5,
                edgecolor="#ffd700",
                facecolor="none",
                linestyle="--",
            )
        )

    # Horizontal levels
    ax.axhline(RESISTANCE, color="#c586c0", linewidth=1.5, linestyle="-", alpha=0.9)
    ax.axhline(ZONE_EDGE, color="#c586c0", linewidth=1, linestyle=":", alpha=0.7)
    ax.axhline(ENTRY_OPT, color="#4fc1ff", linewidth=1, linestyle="--", alpha=0.85)
    ax.axhline(SL_STRUCT, color="#f44747", linewidth=1, linestyle="--", alpha=0.85)
    ax.axhline(TP_2R, color="#6a9955", linewidth=1, linestyle="--", alpha=0.85)

    ax.text(
        n - 0.5, RESISTANCE + 30,
        f"Resistencia 77444",
        color="#c586c0", fontsize=9, va="bottom", fontweight="bold",
    )
    ax.text(
        2, ENTRY_OPT + 25,
        f"Entrada OPTI retest ~77400",
        color="#4fc1ff", fontsize=9, va="bottom",
    )
    ax.text(
        2, SL_STRUCT + 25,
        f"SL estructural ~77615",
        color="#f44747", fontsize=9, va="bottom",
    )
    ax.text(
        2, TP_2R - 40,
        f"TP 1:2 ~{TP_2R:.0f}",
        color="#6a9955", fontsize=9, va="top",
    )

    # Arrow: need 2nd red AT resistance (not here)
    last = show[-1]
    ax.add_patch(
        FancyArrowPatch(
            (n - 3, RESISTANCE - 80),
            (n - 1.5, last["close"]),
            arrowstyle="->",
            color="#ffd700",
            linewidth=2,
            mutation_scale=14,
        )
    )
    ax.text(
        n - 8, RESISTANCE - 120,
        "2R aqui = lejos zona\n→ ESPERAR retest 77444",
        color="#ffd700", fontsize=9, ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#2d2d30", edgecolor="#ffd700", alpha=0.9),
    )

    t_last = show[-1]["open_time"].strftime("%H:%M")
    t_prev = show[-2]["open_time"].strftime("%H:%M")
    ax.text(
        n - 2, show[-2]["low"] - 90,
        f"2M5 [{t_prev}]+[{t_last}] R",
        color="#ffd700", fontsize=8, ha="center",
    )

    ax.set_title(title, color="#569cd6", fontsize=12, fontweight="bold")
    ax.tick_params(colors="#e0e0e0")
    for spine in ax.spines.values():
        spine.set_color("#3e3e42")
    ax.set_ylabel("BTCUSDT", color="#e0e0e0")
    fig.tight_layout()
    fig.savefig(path, dpi=140, facecolor="#1e1e1e")
    plt.close(fig)


def main() -> None:
    m5 = fetch_klines("BTCUSDT", "5m", 200)
    now = m5[-1]["open_time"]
    title = (
        f"BTCUSDT M5 · {now.strftime('%Y-%m-%d %H:%M')} UTC · "
        "BEARISH+BREAK · 2M5 SHORT guía"
    )
    save_annotated_chart(m5, OUT, title)
    print(f"Annotated chart: {OUT}")


if __name__ == "__main__":
    main()
