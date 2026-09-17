"""
Extract real mobile trade screenshots → dataset v_ops_apr_sep.

OCR (RapidOCR) + color sampling of price labels (gray=entry, green=TP, red=SL/price)
to build a ground-truth ops table for ML / neural signal enrichment.

Usage:
  python -m scripts.extract_mobile_ops_ocr
  python -m scripts.extract_mobile_ops_ocr --limit 10
  python -m scripts.extract_mobile_ops_ocr --force
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from PIL import Image

from app.config import DATA_DIR, IMAGES_DIR, MOBILE_OPS_DIR, OPS_MOBILE_DATA_DIR, PROJECT_ROOT

OUT_DIR = OPS_MOBILE_DATA_DIR / "v_ops_apr_sep"
DATASET_VERSION = "v_ops_apr_sep"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}

# European / mixed numeric: 63.342,92 | 76342.92 | 76.560,760
PRICE_RE = re.compile(
    r"(?<![\d])(\d{1,3}(?:[.\s]\d{3})+(?:,\d{1,3})?|\d{4,6}(?:[.,]\d{1,3})?)(?![\d])"
)
TS_RE = re.compile(r"(20\d{2})(\d{2})(\d{2})[-_]?(\d{2})(\d{2})(\d{2})")
SIDE_LONG_RE = re.compile(r"\b(long|buy|compra|compra[r]?)\b", re.I)
SIDE_SHORT_RE = re.compile(r"\b(short|sell|venta|vender)\b", re.I)


def parse_price(raw: str) -> float | None:
    """Parse OCR price text into float. Returns None if invalid."""
    s = raw.strip().replace(" ", "").replace("U", "0").replace("u", "0").replace("O", "0")
    s = s.replace("o", "0")
    if not s or len(s) < 4:
        return None
    # 63.342,92 or 29.446,130 (EU)
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+,\d{1,3}", s):
        return float(s.replace(".", "").replace(",", "."))
    # 76342.92 or 29425.650 (US)
    if re.fullmatch(r"\d{4,6}\.\d{1,3}", s):
        return float(s)
    # 76.560.760 ambiguous → treat last group as decimals if 3 digits
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+\.\d{1,3}", s):
        parts = s.split(".")
        if len(parts[-1]) <= 3:
            return float("".join(parts[:-1]) + "." + parts[-1])
    # 78400.00 with missing dots already handled; 70-600-00 junk
    if "-" in s:
        return None
    # 64000,00
    if re.fullmatch(r"\d{4,6},\d{1,3}", s):
        return float(s.replace(",", "."))
    # plain int-like 64000
    if re.fullmatch(r"\d{4,6}", s):
        return float(s)
    return None


def is_round_grid(price: float) -> bool:
    """Axis grid lines like 64000.00 / 76300.000."""
    if price <= 0:
        return True
    # near multiple of 50/100/200 with tiny fraction
    frac = abs(price - round(price))
    if frac < 0.02 and (round(price) % 50 == 0):
        return True
    if frac < 0.02 and (round(price) % 100 == 0):
        return True
    return False


def classify_color(rgb: tuple[float, float, float]) -> str:
    r, g, b = rgb
    if r > g + 25 and r > b + 15 and r > 120:
        return "red"
    if g > r + 15 and g > b + 5 and g > 100:
        return "green"
    if abs(r - g) < 22 and abs(g - b) < 22 and 90 < r < 210:
        return "gray"
    # teal TP variants (Exness/TV green-cyan)
    if g > 140 and b > 100 and g > r + 10:
        return "green"
    return "other"


def platform_from_name(name: str) -> str:
    n = name.lower()
    if "exness" in n:
        return "Exness"
    if "tradingview" in n:
        return "TradingView"
    if name.upper().startswith("IMG-") or "-wa" in n:
        return "WhatsApp"
    return "Other"


def capture_ts_from_name(name: str) -> datetime | None:
    m = TS_RE.search(name)
    if not m:
        return None
    y, mo, d, h, mi, s = map(int, m.groups())
    try:
        return datetime(y, mo, d, h, mi, s)
    except ValueError:
        return None


def infer_symbol(prices: list[float], platform: str) -> tuple[str, float]:
    if not prices:
        return "UNKNOWN", 0.3
    med = float(np.median(prices))
    # BTC typically 50k–150k in this gallery; US30 often 25k–50k
    if med >= 50000:
        return "BTCUSDT", 0.9
    if 20000 <= med < 50000:
        # Ambiguous band — prefer US30 for ~25–35k, BTC rare there in mid-2026 gallery
        if med < 40000:
            return "US30", 0.75
        return "BTCUSDT", 0.55
    if 1500 <= med < 5000:
        return "XAUUSD", 0.5
    return "UNKNOWN", 0.25


def sample_box_color(arr: np.ndarray, box: list) -> tuple[float, float, float]:
    xs = [pt[0] for pt in box]
    ys = [pt[1] for pt in box]
    h, w = arr.shape[:2]
    x0, x1 = max(0, int(min(xs)) - 2), min(w, int(max(xs)) + 2)
    y0, y1 = max(0, int(min(ys)) - 2), min(h, int(max(ys)) + 2)
    crop = arr[y0:y1, x0:x1]
    if crop.size == 0:
        return (0.0, 0.0, 0.0)
    return tuple(crop.mean(axis=(0, 1)).tolist())  # type: ignore[return-value]


def pick_trade_levels(
    labeled: list[dict[str, Any]],
) -> dict[str, Any]:
    """Pick entry/SL/TP/side from color-tagged price labels."""
    grays = [x for x in labeled if x["color"] == "gray" and not x["is_grid"]]
    greens = [x for x in labeled if x["color"] == "green" and not x["is_grid"]]
    reds = [x for x in labeled if x["color"] == "red" and not x["is_grid"]]

    entry = None
    tp = None
    sl = None
    side = None
    conf_parts: dict[str, float] = {}

    if grays:
        # Prefer gray between green/red extremes when available
        grays_sorted = sorted(grays, key=lambda x: x["price"])
        if greens and reds:
            lo = min(min(g["price"] for g in greens), min(r["price"] for r in reds))
            hi = max(max(g["price"] for g in greens), max(r["price"] for r in reds))
            between = [g for g in grays_sorted if lo <= g["price"] <= hi]
            pool = between or grays_sorted
        else:
            pool = grays_sorted
        entry = pool[len(pool) // 2]
        conf_parts["entry"] = min(0.95, 0.55 + 0.15 * len(grays) + entry["score"] * 0.2)

    if greens:
        # Best green score / most "trade-like" (not round)
        greens_sorted = sorted(greens, key=lambda x: (-x["score"], abs(x["price"] - round(x["price"]))))
        tp = greens_sorted[0]
        conf_parts["take_profit"] = min(0.95, 0.5 + tp["score"] * 0.4)

    if reds and entry:
        # SL = red farthest from TP side; current price often near last candle
        if tp:
            # reds on opposite side of TP relative to entry
            if tp["price"] < entry["price"]:
                # short: SL above entry
                candidates = [r for r in reds if r["price"] > entry["price"]]
            else:
                candidates = [r for r in reds if r["price"] < entry["price"]]
            if not candidates:
                candidates = [r for r in reds if abs(r["price"] - entry["price"]) > abs(tp["price"] - entry["price"]) * 0.15]
            if candidates:
                sl = max(candidates, key=lambda r: abs(r["price"] - entry["price"]))
                conf_parts["stop_loss"] = min(0.9, 0.45 + sl["score"] * 0.4)
        else:
            # farthest red from entry
            sl = max(reds, key=lambda r: abs(r["price"] - entry["price"]))
            conf_parts["stop_loss"] = 0.4

    # Infer side from geometry
    if entry and tp and sl:
        if sl["price"] > entry["price"] > tp["price"]:
            side = "short"
            conf_parts["side"] = 0.9
        elif tp["price"] > entry["price"] > sl["price"]:
            side = "long"
            conf_parts["side"] = 0.9
    elif entry and tp:
        if tp["price"] < entry["price"]:
            side = "short"
            conf_parts["side"] = 0.65
        else:
            side = "long"
            conf_parts["side"] = 0.65
    elif entry and sl:
        if sl["price"] > entry["price"]:
            side = "short"
            conf_parts["side"] = 0.55
        else:
            side = "long"
            conf_parts["side"] = 0.55

    rr = None
    if entry and tp and sl:
        risk = abs(entry["price"] - sl["price"])
        reward = abs(tp["price"] - entry["price"])
        if risk > 0:
            rr = round(reward / risk, 3)

    return {
        "entry": entry["price"] if entry else None,
        "take_profit": tp["price"] if tp else None,
        "stop_loss": sl["price"] if sl else None,
        "side": side,
        "rr_planned": rr,
        "field_confidence": conf_parts,
        "n_gray": len(grays),
        "n_green": len(greens),
        "n_red": len(reds),
    }


def extract_from_image(path: Path, ocr_engine: Any) -> dict[str, Any]:
    img = Image.open(path).convert("RGB")
    arr = np.array(img)
    result, _elapse = ocr_engine(str(path))
    raw_items = result or []

    all_text = " ".join(t[1] for t in raw_items)
    labeled: list[dict[str, Any]] = []
    skip_tokens = {"maximo", "mínimo", "minimo", "ask", "bid", "buy", "sell"}

    for box, text, score in raw_items:
        t = text.strip()
        if t.lower() in skip_tokens:
            continue
        # Find price-like substrings
        candidates = PRICE_RE.findall(t) or ([t] if re.search(r"\d", t) else [])
        for cand in candidates:
            price = parse_price(cand if isinstance(cand, str) else cand[0] if cand else "")
            if price is None or price < 100:  # ignore RSI-like small numbers
                continue
            if price > 500_000:
                continue
            rgb = sample_box_color(arr, box)
            color = classify_color(rgb)
            labeled.append(
                {
                    "text": t,
                    "price": price,
                    "score": float(score),
                    "color": color,
                    "rgb": rgb,
                    "y": float(min(pt[1] for pt in box)),
                    "is_grid": is_round_grid(price),
                }
            )

    levels = pick_trade_levels(labeled)
    prices = [x["price"] for x in labeled if not x["is_grid"]]
    chart_prices = prices or [x["price"] for x in labeled]
    platform = platform_from_name(path.name)
    symbol, sym_conf = infer_symbol(chart_prices, platform)
    capture_ts = capture_ts_from_name(path.name)

    # Reject entry outliers vs chart scale (e.g. OCR 52k on a 75k BTC axis)
    if levels["entry"] is not None and chart_prices:
        med = float(np.median(chart_prices))
        if med > 0 and abs(levels["entry"] - med) / med > 0.18:
            # Try alternate gray closer to median
            alt_grays = [
                x
                for x in labeled
                if x["color"] == "gray" and not x["is_grid"] and abs(x["price"] - med) / med <= 0.12
            ]
            if alt_grays:
                alt = min(alt_grays, key=lambda x: abs(x["price"] - med))
                levels["entry"] = alt["price"]
                levels["field_confidence"]["entry"] = min(
                    levels["field_confidence"].get("entry", 0.5), 0.7
                )
                # Recompute side/rr with updated entry
                e = levels["entry"]
                tp_v, sl_v = levels["take_profit"], levels["stop_loss"]
                if e and tp_v and sl_v:
                    if sl_v > e > tp_v:
                        levels["side"] = "short"
                    elif tp_v > e > sl_v:
                        levels["side"] = "long"
                    risk = abs(e - sl_v)
                    reward = abs(tp_v - e)
                    levels["rr_planned"] = round(reward / risk, 3) if risk > 0 else None
            else:
                levels["field_confidence"]["entry"] = min(
                    levels["field_confidence"].get("entry", 0.5), 0.35
                )
                levels["field_confidence"]["entry_outlier"] = 0.2

    # Textual side override
    if SIDE_LONG_RE.search(all_text) and not SIDE_SHORT_RE.search(all_text):
        levels["side"] = "long"
        levels["field_confidence"]["side"] = max(levels["field_confidence"].get("side", 0), 0.8)
    elif SIDE_SHORT_RE.search(all_text) and not SIDE_LONG_RE.search(all_text):
        levels["side"] = "short"
        levels["field_confidence"]["side"] = max(levels["field_confidence"].get("side", 0), 0.8)

    field_conf = dict(levels["field_confidence"])
    field_conf["symbol"] = sym_conf
    field_conf["capture_ts"] = 0.95 if capture_ts else 0.0

    # Global confidence
    weights = []
    for k in ("entry", "side", "take_profit", "stop_loss", "symbol"):
        if k in field_conf:
            weights.append(field_conf[k])
    confidence = float(np.mean(weights)) if weights else 0.15
    if levels["entry"] is None:
        confidence = min(confidence, 0.35)

    # Outcome unknown unless we later match market; screenshots usually mid-trade
    outcome = "open" if levels["entry"] else "unknown"

    # Timeframe hint from OCR
    tf = None
    m_tf = re.search(r"\b(M1|M5|M15|M30|H1|H4|D1|1m|5m|15m|1h|4h)\b", all_text, re.I)
    if m_tf:
        tf = m_tf.group(1).upper().replace("1H", "H1").replace("5M", "M5")

    dedupe_payload = f"{symbol}|{levels['side']}|{levels['entry']}|{capture_ts}"
    trade_id = hashlib.sha1(f"{path.name}|{dedupe_payload}".encode()).hexdigest()[:16]
    dedupe_key = hashlib.sha1(
        f"{symbol}|{levels['side']}|{round(levels['entry'] or 0, 1)}|{capture_ts.date() if capture_ts else ''}".encode()
    ).hexdigest()[:12]

    return {
        "trade_id": trade_id,
        "symbol": symbol,
        "side": levels["side"],
        "entry_time": capture_ts.isoformat(sep=" ") if capture_ts else None,
        "exit_time": None,
        "entry_price": levels["entry"],
        "exit_price": None,
        "stop_loss": levels["stop_loss"],
        "take_profit": levels["take_profit"],
        "quantity": None,
        "pnl": None,
        "pnl_pct": None,
        "fees": None,
        "rr_planned": levels["rr_planned"],
        "outcome": outcome,
        "platform": platform,
        "timeframe_hint": tf,
        "source_image": path.name,
        "source_path": str(path),
        "capture_ts_from_name": capture_ts.isoformat(sep=" ") if capture_ts else None,
        "confidence": round(confidence, 3),
        "field_confidence": json.dumps(field_conf, ensure_ascii=False),
        "dedupe_key": dedupe_key,
        "dataset_version": DATASET_VERSION,
        "ocr_n_labels": len(labeled),
        "ocr_n_gray": levels["n_gray"],
        "ocr_n_green": levels["n_green"],
        "ocr_n_red": levels["n_red"],
        "ocr_raw_preview": all_text[:240],
    }


def validate_row(row: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    side = row.get("side")
    entry = row.get("entry_price")
    sl = row.get("stop_loss")
    tp = row.get("take_profit")
    if entry is None:
        issues.append("missing_entry")
    if side is None:
        issues.append("missing_side")
    if entry and sl and tp and side:
        if side == "short" and not (sl > entry > tp):
            issues.append("geometry_inconsistent_short")
        if side == "long" and not (tp > entry > sl):
            issues.append("geometry_inconsistent_long")
    ts = row.get("capture_ts_from_name")
    if ts:
        try:
            dt = datetime.fromisoformat(ts)
            if not (datetime(2026, 3, 1) <= dt <= datetime(2026, 9, 30)):
                issues.append("timestamp_out_of_expected_range")
        except ValueError:
            issues.append("bad_timestamp")
    if (row.get("confidence") or 0) < 0.45:
        issues.append("low_confidence")
    if row.get("ocr_n_labels", 0) < 3:
        issues.append("sparse_ocr")
    return issues


def dedupe_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    best: dict[str, dict[str, Any]] = {}
    for r in rows:
        key = r["dedupe_key"]
        prev = best.get(key)
        if prev is None or (r.get("confidence") or 0) > (prev.get("confidence") or 0):
            best[key] = r
    return list(best.values()), len(rows) - len(best)


def write_quality_report(
    out_dir: Path,
    rows: list[dict[str, Any]],
    n_images: int,
    n_deduped: int,
    problematic: list[dict[str, Any]],
) -> Path:
    high = sum(1 for r in rows if (r.get("confidence") or 0) >= 0.7)
    mid = sum(1 for r in rows if 0.45 <= (r.get("confidence") or 0) < 0.7)
    low = sum(1 for r in rows if (r.get("confidence") or 0) < 0.45)
    with_entry = sum(1 for r in rows if r.get("entry_price") is not None)
    with_side = sum(1 for r in rows if r.get("side") is not None)
    with_sl = sum(1 for r in rows if r.get("stop_loss") is not None)
    with_tp = sum(1 for r in rows if r.get("take_profit") is not None)
    symbols = Counter(r.get("symbol") for r in rows)
    platforms = Counter(r.get("platform") for r in rows)
    sides = Counter(r.get("side") for r in rows)

    missing_fields = {
        "entry_price": n_images - with_entry,
        "side": n_images - with_side,
        "stop_loss": n_images - with_sl,
        "take_profit": n_images - with_tp,
        "quantity": n_images,
        "pnl": n_images,
    }

    lines = [
        f"# Quality report — {DATASET_VERSION}",
        "",
        f"> Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"> Fuente: `{MOBILE_OPS_DIR}`",
        "",
        "## Resumen",
        "",
        "| Métrica | Valor |",
        "|---------|-------|",
        f"| Imágenes escaneadas | {n_images} |",
        f"| Trades tras dedupe | {len(rows)} |",
        f"| Duplicados removidos | {n_deduped} |",
        f"| Alta confianza (≥0.70) | {high} ({100*high/max(len(rows),1):.1f}%) |",
        f"| Media (0.45–0.70) | {mid} |",
        f"| Baja (<0.45) | {low} |",
        f"| Con entry | {with_entry} |",
        f"| Con side | {with_side} |",
        f"| Con SL | {with_sl} |",
        f"| Con TP | {with_tp} |",
        f"| Problemáticas | {len(problematic)} |",
        "",
        "## Símbolos",
        "",
    ]
    for k, v in symbols.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Plataformas", ""]
    for k, v in platforms.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Sides", ""]
    for k, v in sides.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Campos faltantes (aprox. por imagen origen)", ""]
    for k, v in missing_fields.items():
        lines.append(f"- `{k}`: {v}")
    lines += [
        "",
        "## Notas",
        "",
        "- Quantity / PnL / fees casi nunca aparecen en capturas de chart → quedan `null`.",
        "- `entry_time` usa timestamp del nombre de archivo (`Screenshot_YYYYMMDD-HHMMSS`).",
        "- `outcome=open` hasta cruzar con mercado histórico en etapa ML.",
        "- No se borró data histórica; este dataset es versión nueva bajo `data/ops_mobile/`.",
        "",
        "## Archivos",
        "",
        "- `trades.parquet` / `trades.csv`",
        "- `problematic_images.csv`",
        "- `quality_report.md` (este archivo)",
        "",
    ]
    path = out_dir / "quality_report.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract mobile ops OCR → v_ops_apr_sep")
    parser.add_argument("--source", type=Path, default=MOBILE_OPS_DIR)
    parser.add_argument("--out", type=Path, default=OUT_DIR)
    parser.add_argument("--limit", type=int, default=0, help="Process only N images (0=all)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs")
    args = parser.parse_args()

    source: Path = args.source
    out_dir: Path = args.out
    if not source.is_dir():
        print(f"ERROR: source not found: {source}", file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    parquet_path = out_dir / "trades.parquet"
    if parquet_path.exists() and not args.force:
        print(f"Exists: {parquet_path} (use --force to overwrite)")

    images = sorted(
        p for p in source.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTS
    )
    if args.limit and args.limit > 0:
        images = images[: args.limit]
    print(f"Scanning {len(images)} images from {source}")

    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError:
        print("ERROR: pip install rapidocr-onnxruntime", file=sys.stderr)
        return 1

    ocr = RapidOCR()
    rows: list[dict[str, Any]] = []
    for i, path in enumerate(images, 1):
        try:
            row = extract_from_image(path, ocr)
            row["validation_issues"] = json.dumps(validate_row(row))
            rows.append(row)
            flag = "OK" if (row["confidence"] or 0) >= 0.45 and row.get("entry_price") else "LOW"
            msg = (
                f"[{i}/{len(images)}] {flag} conf={row['confidence']:.2f} "
                f"{row.get('symbol')} {row.get('side')} entry={row.get('entry_price')} "
                f"<- {path.name}"
            )
            try:
                print(msg)
            except UnicodeEncodeError:
                print(msg.encode("ascii", "replace").decode("ascii"))
        except Exception as exc:  # noqa: BLE001 — keep batch running
            print(f"[{i}/{len(images)}] FAIL {path.name}: {exc}")
            rows.append(
                {
                    "trade_id": hashlib.sha1(path.name.encode()).hexdigest()[:16],
                    "symbol": "UNKNOWN",
                    "side": None,
                    "entry_time": None,
                    "exit_time": None,
                    "entry_price": None,
                    "exit_price": None,
                    "stop_loss": None,
                    "take_profit": None,
                    "quantity": None,
                    "pnl": None,
                    "pnl_pct": None,
                    "fees": None,
                    "rr_planned": None,
                    "outcome": "unknown",
                    "platform": platform_from_name(path.name),
                    "timeframe_hint": None,
                    "source_image": path.name,
                    "source_path": str(path),
                    "capture_ts_from_name": (
                        capture_ts_from_name(path.name).isoformat(sep=" ")
                        if capture_ts_from_name(path.name)
                        else None
                    ),
                    "confidence": 0.0,
                    "field_confidence": "{}",
                    "dedupe_key": hashlib.sha1(path.name.encode()).hexdigest()[:12],
                    "dataset_version": DATASET_VERSION,
                    "ocr_n_labels": 0,
                    "ocr_n_gray": 0,
                    "ocr_n_green": 0,
                    "ocr_n_red": 0,
                    "ocr_raw_preview": "",
                    "validation_issues": json.dumps(["ocr_exception", str(exc)]),
                }
            )

    deduped, n_removed = dedupe_rows(rows)
    # Prefer keeping all image rows for audit, but also export deduped trades
    df_all = pd.DataFrame(rows)
    df_trades = pd.DataFrame(deduped)

    csv_all = out_dir / "trades_raw_per_image.csv"
    csv_trades = out_dir / "trades.csv"
    parquet_trades = out_dir / "trades.parquet"

    df_all.to_csv(csv_all, index=False)
    df_trades.to_csv(csv_trades, index=False)
    try:
        df_trades.to_parquet(parquet_trades, index=False)
    except Exception as exc:  # noqa: BLE001
        print(f"WARN parquet: {exc} (csv written)")

    problematic = []
    for r in rows:
        issues = json.loads(r.get("validation_issues") or "[]")
        if issues or (r.get("confidence") or 0) < 0.45 or r.get("entry_price") is None:
            problematic.append(
                {
                    "source_image": r.get("source_image"),
                    "confidence": r.get("confidence"),
                    "symbol": r.get("symbol"),
                    "side": r.get("side"),
                    "entry_price": r.get("entry_price"),
                    "issues": ";".join(issues) if isinstance(issues, list) else issues,
                }
            )
    prob_path = out_dir / "problematic_images.csv"
    pd.DataFrame(problematic).to_csv(prob_path, index=False)

    report = write_quality_report(out_dir, deduped, len(images), n_removed, problematic)
    meta = {
        "dataset_version": DATASET_VERSION,
        "source": str(source),
        "n_images": len(images),
        "n_trades_deduped": len(deduped),
        "n_duplicates_removed": n_removed,
        "n_problematic": len(problematic),
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "project_root": str(PROJECT_ROOT),
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print("\nDone.")
    print(f"  trades: {parquet_trades}")
    print(f"  csv:    {csv_trades}")
    print(f"  raw:    {csv_all}")
    print(f"  problems: {prob_path} ({len(problematic)})")
    print(f"  report: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
