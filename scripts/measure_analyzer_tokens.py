#!/usr/bin/env python3
"""Mide tamaño y tokens estimados de los 3 tiers BTC M5 (live + protocolo)."""
from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from app.config import PROJECT_ROOT

ROOT = PROJECT_ROOT

_PROTOCOLS = ROOT / "docs" / "protocols"
TIERS = {
    "light": {
        "label": "Light",
        "live": ROOT / "live" / "btc_m5_signal.md",
        "protocol": _PROTOCOLS / "TRADING_LIVE_BTC_SIGNAL_LIGHT.md",
    },
    "full": {
        "label": "Full",
        "live": ROOT / "live" / "btc_m5_snapshot.md",
        "protocol": _PROTOCOLS / "TRADING_LIVE_BTC_M5_ANALYSIS.md",
    },
    "high": {
        "label": "High",
        "live": ROOT / "live" / "btc_m5_high_signal.md",
        "protocol": _PROTOCOLS / "TRADING_LIVE_BTC_HIGH_SIGNAL.md",
    },
    "high_advanced": {
        "label": "High Advanced",
        "live": ROOT / "live" / "btc_m5_high_signal.md",
        "protocol": _PROTOCOLS / "TRADING_LIVE_BTC_HIGH_SIGNAL.md",
        "note": "Same files as high; live grows ~+450 lines when generated with --advanced",
    },
    "superhigh": {
        "label": "Super High",
        "live": ROOT / "live" / "btc_super_high_signal.md",
        "protocol": _PROTOCOLS / "TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md",
    },
}


@dataclass
class FileStats:
    path: str
    bytes: int
    lines: int
    words: int
    chars: int
    tokens_chars_div4: int
    tokens_words_x13: int
    tokens_tiktoken: int | None = None


def _line_count(text: str) -> int:
    if not text:
        return 0
    return text.count("\n") + (0 if text.endswith("\n") else 1)


def _tiktoken_count(text: str) -> int | None:
    try:
        import tiktoken

        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        return None


def measure_file(path: Path) -> FileStats:
    text = path.read_text(encoding="utf-8")
    words = len(text.split())
    chars = len(text)
    return FileStats(
        path=str(path.relative_to(ROOT)),
        bytes=path.stat().st_size,
        lines=_line_count(text),
        words=words,
        chars=chars,
        tokens_chars_div4=round(chars / 4),
        tokens_words_x13=round(words * 1.3),
        tokens_tiktoken=_tiktoken_count(text),
    )


def sum_stats(*items: FileStats) -> dict:
    total = {
        "bytes": sum(i.bytes for i in items),
        "lines": sum(i.lines for i in items),
        "words": sum(i.words for i in items),
        "chars": sum(i.chars for i in items),
        "tokens_chars_div4": sum(i.tokens_chars_div4 for i in items),
        "tokens_words_x13": sum(i.tokens_words_x13 for i in items),
    }
    tik = [i.tokens_tiktoken for i in items if i.tokens_tiktoken is not None]
    total["tokens_tiktoken"] = sum(tik) if tik and len(tik) == len(items) else None
    return total


def main() -> int:
    out: dict = {"root": str(ROOT), "tiers": {}, "generated_at_utc": None}

    from datetime import datetime, timezone

    out["generated_at_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    for key, cfg in TIERS.items():
        if not cfg["live"].is_file() or not cfg["protocol"].is_file():
            out["tiers"][key] = {
                "label": cfg["label"],
                "skipped": True,
                "reason": "live or protocol file missing",
            }
            continue
        live = measure_file(cfg["live"])
        proto = measure_file(cfg["protocol"])
        out["tiers"][key] = {
            "label": cfg["label"],
            "live": asdict(live),
            "protocol": asdict(proto),
            "prompt_total": sum_stats(live, proto),
        }

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
