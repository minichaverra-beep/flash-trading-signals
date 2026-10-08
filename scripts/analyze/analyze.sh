#!/usr/bin/env bash
# =============================================================================
# analyze.sh — equivalente bash de analyze-<market>-<tier>.ps1 (Android / Linux)
# =============================================================================
# Uso:
#   bash scripts/analyze/analyze.sh <btc|us30|xauusd> <context|light|high|history> [flags]
#
# Flags (mismos nombres que los .ps1, sin distinguir mayúsculas):
#   -NoChart -ML -Neural -Bullish -Bearish -Break -Reverse -Advanced -NoAdvanced
#   -Ilustrate|-Illustrate -NoOpen -HistoryReview -Entry <precio>
#   -Symbol <sym> (solo btc) -Ticker <tk> (us30 / xauusd)
#
# Ejemplos:
#   bash scripts/analyze/analyze.sh btc high -NoChart -Bullish -Break -ML -Neural -Ilustrate
#   bash scripts/analyze/analyze.sh us30 light -ML -Neural
#   bash scripts/analyze/analyze.sh xauusd history -NoChart -Bearish -Break
#
# Python: $PYTHON (default python3). Corre desde la raíz de Cursor Trading.
# =============================================================================

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
export PYTHONIOENCODING=utf-8
PY="${PYTHON:-python3}"

die() { echo "ERROR: $*" >&2; exit 1; }

[[ $# -ge 2 ]] || die "uso: analyze.sh <btc|us30|xauusd> <context|light|high|history> [flags]"

market="${1,,}"
tier="${2,,}"
shift 2

case "$market" in btc|us30|xauusd) ;; *) die "market debe ser btc|us30|xauusd (recibido: $market)" ;; esac
case "$tier" in context|light|high|history) ;; *) die "tier debe ser context|light|high|history (recibido: $tier)" ;; esac

no_chart=0 ml=0 neural=0 bullish=0 bearish=0 brk=0 reverse=0
advanced=0 no_advanced=0 ilustrate=0 no_open=0 history_review=0
entry="" symbol="" ticker=""

while [[ $# -gt 0 ]]; do
  case "${1,,}" in
    -nochart)               no_chart=1 ;;
    -ml)                    ml=1 ;;
    -neural)                neural=1 ;;
    -bullish)               bullish=1 ;;
    -bearish)               bearish=1 ;;
    -break)                 brk=1 ;;
    -reverse)               reverse=1 ;;
    -advanced)              advanced=1 ;;
    -noadvanced)            no_advanced=1 ;;
    -ilustrate|-illustrate) ilustrate=1 ;;
    -noopen)                no_open=1 ;;
    -historyreview)         history_review=1 ;;
    -entry)                 [[ $# -ge 2 ]] || die "-Entry requiere valor"; entry="$2"; shift ;;
    -symbol)                [[ $# -ge 2 ]] || die "-Symbol requiere valor"; symbol="$2"; shift ;;
    -ticker)                [[ $# -ge 2 ]] || die "-Ticker requiere valor"; ticker="$2"; shift ;;
    *) die "flag desconocido: $1" ;;
  esac
  shift
done

(( bullish && bearish )) && die "-Bullish y -Bearish son mutuamente excluyentes."
(( brk && reverse )) && die "-Break y -Reverse son mutuamente excluyentes."
(( advanced && no_advanced )) && die "-Advanced y -NoAdvanced son mutuamente excluyentes."

if [[ -n "$entry" && ! "$entry" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
  die "-Entry debe ser numérico (recibido: $entry)"
fi

controller="app.controllers.analyze_${market}_m5"
args=(-m "$controller")

if [[ "$market" == "btc" ]]; then
  args+=(--symbol "${symbol:-BTCUSDT}")
elif [[ -n "$ticker" ]]; then
  args+=(--ticker "$ticker")
fi

# history = high + --history-review. Advanced ON por defecto en btc/us30; xauusd solo si se pide.
if [[ "$tier" == "history" ]]; then
  history_review=1
  entry=""
  if [[ "$market" == "xauusd" ]]; then
    (( advanced && !no_advanced )) && advanced=1 || advanced=0
  else
    (( no_advanced )) && advanced=0 || advanced=1
  fi
fi

label="${market^^} M5 ${tier^^}"

case "$tier" in
  context)
    args+=(--mode context --no-chart)
    ;;
  light)
    args+=(--mode light --no-chart)
    (( ml )) && args+=(--ml)
    (( neural )) && args+=(--neural)
    if (( bullish )); then args+=(--bias bullish); elif (( bearish )); then args+=(--bias bearish); fi
    ;;
  high|history)
    args+=(--mode high)
    (( no_chart )) && args+=(--no-chart)
    (( ml )) && args+=(--ml)
    (( neural )) && args+=(--neural)
    (( ilustrate )) && args+=(--ilustrate)
    (( history_review )) && args+=(--history-review)
    (( no_open )) && args+=(--no-open)
    [[ -n "$entry" ]] && args+=(--entry "$entry")
    # btc / us30: Advanced auto con ML + Neural (igual que los .ps1)
    if [[ "$market" != "xauusd" ]] && (( ml && neural )); then advanced=1; fi
    (( advanced )) && args+=(--advanced)
    if (( bullish )); then args+=(--bias bullish); elif (( bearish )); then args+=(--bias bearish); else args+=(--bias auto); fi
    if (( brk )); then args+=(--setup break); elif (( reverse )); then args+=(--setup reverse); else args+=(--setup auto); fi
    ;;
esac

echo ">> $label — $PY ${args[*]}"
set +e
"$PY" "${args[@]}"
code=$?
set -e
if (( code != 0 )); then
  echo "ERROR: fallo $PY -m $controller ($code)" >&2
  exit "$code"
fi
