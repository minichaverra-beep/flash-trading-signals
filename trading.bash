#!/usr/bin/env bash
# =============================================================================
# trading.bash — Usar Cursor Trading SIN Cursor AI
# =============================================================================
# Corre señales BTC/US30, imprime resumen en terminal y abre el reporte .md
#
# Uso rápido (Git Bash / WSL / Linux / macOS):
#   cd "/d/Danilo/Trading/Cursor Trading"   # o tu ruta
#   chmod +x trading.bash
#   ./trading.bash                         # menú interactivo
#   ./trading.bash us30                    # High US30 (Bullish+Break+ML+Neural+Ilustrate)
#   ./trading.bash btc                     # High BTC  (Bullish+Break+ML+Neural+Ilustrate)
#   ./trading.bash us30 --bearish --break
#   ./trading.bash us30 --bullish --reverse --entry 53128
#   ./trading.bash us30-history
#   ./trading.bash show us30
#   ./trading.bash help
#
# Windows (Git Bash):
#   bash trading.bash us30
# =============================================================================

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1

# Preferir python del PATH; fallback a py -3 en Windows
if command -v python >/dev/null 2>&1; then
  PY=(python)
elif command -v python3 >/dev/null 2>&1; then
  PY=(python3)
elif command -v py >/dev/null 2>&1; then
  PY=(py -3)
else
  echo "ERROR: no se encontró python / python3 / py" >&2
  exit 1
fi

# ---------- colores ----------
if [[ -t 1 ]]; then
  C_MAG=$'\033[35m'; C_GRN=$'\033[32m'; C_YEL=$'\033[33m'
  C_RED=$'\033[31m'; C_CYN=$'\033[36m'; C_BOLD=$'\033[1m'; C_RST=$'\033[0m'
else
  C_MAG=; C_GRN=; C_YEL=; C_RED=; C_CYN=; C_BOLD=; C_RST=
fi

die() { echo "${C_RED}ERROR:${C_RST} $*" >&2; exit 1; }

usage() {
  cat <<'EOF'
trading.bash — señales BTC / US30 sin Cursor AI

COMANDOS
  us30 | us30-high          Señal High US30 (default: bullish + break + ml + neural + ilustrate)
  btc  | btc-high           Señal High BTC  (igual default)
  us30-history              Revisión P&L última Entry US30 (NO es señal)
  btc-history               Revisión P&L última Entry BTC
  us30-light | btc-light    Chequeo Light + ML + Neural
  show us30|btc             Resumen del último reporte live/
  open us30|btc             Abrir .md en el editor / visor del SO
  menu                      Menú interactivo
  help                      Esta ayuda

FLAGS (High / History)
  --bullish | --bearish     Bias (default: --bullish)
  --break   | --reverse     Setup (default: --break)
  --entry PRECIO            Fill usuario (solo High; no sobrescribe Entrada óptima)
  --no-ml | --no-neural | --no-ilustrate
  --chart                   Generar chart en markdown (quita --no-chart)
  --no-open                 No abrir preview del SO
  --advanced                Fuerza Advanced (ya auto con ML+Neural)

EJEMPLOS
  ./trading.bash us30
  ./trading.bash us30 --bearish --break
  ./trading.bash us30 --bullish --reverse --entry 53128
  ./trading.bash btc --bearish --break
  ./trading.bash us30-history --bullish --break
  ./trading.bash show us30

REGLAS DURAS (recordatorio)
  • Zona + 2 velas M5 · SL ~$9 · R:R ≥ 1:2 · 2 SL = fin de sesión
  • No operar contra H1 sin cuidado · Confirmar siempre en TradingView
EOF
}

report_path() {
  case "$1" in
    us30) echo "$ROOT/live/us30_m5_high_signal.md" ;;
    btc)  echo "$ROOT/live/btc_m5_high_signal.md" ;;
    us30-light) echo "$ROOT/live/us30_m5_signal.md" ;;
    btc-light)  echo "$ROOT/live/btc_m5_signal.md" ;;
    *) die "activo desconocido: $1" ;;
  esac
}

# Extrae filas clave de la tabla Resumen High / Veredicto
summarize_report() {
  local file="$1"
  [[ -f "$file" ]] || die "no existe reporte: $file"

  echo ""
  echo "${C_BOLD}${C_CYN}======== RESUMEN (sin Cursor) ========${C_RST}"
  echo "Archivo: $file"
  echo ""

  # Header / veredicto
  grep -E '^> |^## Veredicto|^## Resumen' "$file" | head -n 12 || true
  echo ""

  # Filas útiles de la tabla markdown
  awk '
    BEGIN { FS="|" }
    /^\| Precio / || /^\| Veredicto / || /^\| Entrada / || /^\| Plan / || \
    /^\| E2 / || /^\| Métricas / || /^\| Bando usado / || /^\| Bando mercado / || \
    /^\| Dist\. a Entry / || /^\| Dist\. a SL / || /^\| Dist\. a TP / || \
    /^\| Estado 2M5 / || /^\| Bias H1 / || /^\| Calidad / || /^\| Rules E1 / || \
    /^\| Winrate / || /^\| Historial ref / {
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", $2)
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", $3)
      if ($2 != "" && $2 != "Sección" && $2 != "-------")
        printf "  %-18s %s\n", $2, $3
    }
  ' "$file" || true

  echo ""
  # Checklist 2M5 compacto
  echo "${C_BOLD}Checklist 2M5:${C_RST}"
  grep -E '^\- \[[✅❌]\]' "$file" | head -n 8 || true

  echo ""
  echo "${C_BOLD}Red flags:${C_RST}"
  # líneas bajo ### Red flags hasta el próximo ###
  awk '
    /^### Red flags/ {p=1; next}
    /^### / { if(p) exit }
    p && /^- / { print }
  ' "$file" | head -n 8 || true

  echo ""
  echo "${C_YEL}Lee Categories en orden: Precio → Entrada óptima → Confluencia → Checklist 2M5 → CRT${C_RST}"
  echo "${C_GRN}Confirma en TradingView antes de ejecutar. 2 SL = límite diario.${C_RST}"
  echo "${C_CYN}=======================================${C_RST}"
}

open_file() {
  local file="$1"
  [[ -f "$file" ]] || die "no existe: $file"
  if command -v code >/dev/null 2>&1; then
    code "$file"
  elif command -v cursor >/dev/null 2>&1; then
    cursor "$file"
  elif command -v notepad >/dev/null 2>&1; then
    notepad "$file" &
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$file" >/dev/null 2>&1 &
  elif command -v open >/dev/null 2>&1; then
    open "$file"
  else
    echo "Abre manualmente: $file"
  fi
}

# ---------- parse flags comunes ----------
BIAS="bullish"
SETUP="break"
ENTRY=""
DO_ML=1
DO_NEURAL=1
DO_ILUST=1
NO_CHART=1
NO_OPEN=0
ADVANCED=0

parse_flags() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --bullish) BIAS=bullish ;;
      --bearish) BIAS=bearish ;;
      --break)   SETUP=break ;;
      --reverse) SETUP=reverse ;;
      --entry)
        [[ $# -ge 2 ]] || die "--entry requiere precio"
        ENTRY="$2"; shift
        ;;
      --no-ml) DO_ML=0 ;;
      --no-neural) DO_NEURAL=0 ;;
      --no-ilustrate|--no-illustrate) DO_ILUST=0 ;;
      --chart) NO_CHART=0 ;;
      --no-open) NO_OPEN=1 ;;
      --advanced) ADVANCED=1 ;;
      -h|--help) usage; exit 0 ;;
      *) die "flag desconocido: $1 (usa --help)" ;;
    esac
    shift
  done
}

append_common_flags() {
  # Usa array global PY_ARGS
  if [[ $NO_CHART -eq 1 ]]; then PY_ARGS+=(--no-chart); fi
  if [[ $DO_ML -eq 1 ]]; then PY_ARGS+=(--ml); fi
  if [[ $DO_NEURAL -eq 1 ]]; then PY_ARGS+=(--neural); fi
  if [[ $DO_ILUST -eq 1 ]]; then PY_ARGS+=(--ilustrate); fi
  if [[ $NO_OPEN -eq 1 ]]; then PY_ARGS+=(--no-open); fi
  if [[ -n "$ENTRY" ]]; then PY_ARGS+=(--entry "$ENTRY"); fi
  if [[ $ADVANCED -eq 1 || ( $DO_ML -eq 1 && $DO_NEURAL -eq 1 ) ]]; then
    PY_ARGS+=(--advanced)
  fi
  PY_ARGS+=(--bias "$BIAS" --setup "$SETUP")
}

upper() { printf '%s' "$1" | tr '[:lower:]' '[:upper:]'; }

run_python() {
  echo "${C_MAG}>> ${PY[*]} -m ${PY_ARGS[*]}${C_RST}"
  "${PY[@]}" -m "${PY_ARGS[@]}"
}

run_us30_high() {
  local hist="${1:-0}"
  shift || true
  parse_flags "$@"
  PY_ARGS=(app.controllers.analyze_us30_m5 --mode high)
  [[ "$hist" == "1" ]] && PY_ARGS+=(--history-review)
  append_common_flags

  local label="US30 HIGH"
  [[ "$hist" == "1" ]] && label="US30 HISTORY (P&L)"
  echo "${C_MAG}>> $label [$(upper "$BIAS") + $(upper "$SETUP")]${C_RST}"

  run_python
  summarize_report "$(report_path us30)"
  echo ""
  echo "Reporte: $(report_path us30)"
}

run_btc_high() {
  local hist="${1:-0}"
  shift || true
  parse_flags "$@"
  PY_ARGS=(app.controllers.analyze_btc_m5 --symbol BTCUSDT --mode high)
  [[ "$hist" == "1" ]] && PY_ARGS+=(--history-review)
  append_common_flags

  local label="BTC HIGH"
  [[ "$hist" == "1" ]] && label="BTC HISTORY (P&L)"
  echo "${C_MAG}>> $label [$(upper "$BIAS") + $(upper "$SETUP")]${C_RST}"

  run_python
  summarize_report "$(report_path btc)"
  echo ""
  echo "Reporte: $(report_path btc)"
}

run_us30_light() {
  parse_flags "$@"
  echo "${C_MAG}>> US30 LIGHT${C_RST}"
  PY_ARGS=(app.controllers.analyze_us30_m5 --mode light)
  [[ $DO_ML -eq 1 ]] && PY_ARGS+=(--ml)
  [[ $DO_NEURAL -eq 1 ]] && PY_ARGS+=(--neural)
  [[ $NO_OPEN -eq 1 ]] && PY_ARGS+=(--no-open)
  run_python
  summarize_report "$(report_path us30-light)"
}

run_btc_light() {
  parse_flags "$@"
  echo "${C_MAG}>> BTC LIGHT${C_RST}"
  PY_ARGS=(app.controllers.analyze_btc_m5 --symbol BTCUSDT --mode light)
  [[ $DO_ML -eq 1 ]] && PY_ARGS+=(--ml)
  [[ $DO_NEURAL -eq 1 ]] && PY_ARGS+=(--neural)
  [[ $NO_OPEN -eq 1 ]] && PY_ARGS+=(--no-open)
  run_python
  summarize_report "$(report_path btc-light)"
}

menu() {
  while true; do
    echo ""
    echo "${C_BOLD}=== Cursor Trading (sin AI) ===${C_RST}"
    echo "  1) US30 High  Bullish+Break  (día a día)"
    echo "  2) US30 High  Bearish+Break"
    echo "  3) US30 High  Bullish+Reverse"
    echo "  4) BTC  High  Bullish+Break"
    echo "  5) BTC  High  Bearish+Break"
    echo "  6) US30 History (P&L última Entry)"
    echo "  7) BTC  History (P&L última Entry)"
    echo "  8) Ver resumen US30"
    echo "  9) Ver resumen BTC"
    echo "  o) Abrir reporte US30"
    echo "  b) Abrir reporte BTC"
    echo "  h) Ayuda"
    echo "  q) Salir"
    read -r -p "Opción: " opt
    case "$opt" in
      1) run_us30_high 0 --bullish --break ;;
      2) run_us30_high 0 --bearish --break ;;
      3) run_us30_high 0 --bullish --reverse ;;
      4) run_btc_high 0 --bullish --break ;;
      5) run_btc_high 0 --bearish --break ;;
      6) run_us30_high 1 --bullish --break ;;
      7) run_btc_high 1 --bullish --break ;;
      8) summarize_report "$(report_path us30)" ;;
      9) summarize_report "$(report_path btc)" ;;
      o|O) open_file "$(report_path us30)" ;;
      b|B) open_file "$(report_path btc)" ;;
      h|H) usage ;;
      q|Q) echo "Listo."; exit 0 ;;
      *) echo "Opción inválida" ;;
    esac
  done
}

# ---------- main ----------
CMD="${1:-menu}"
shift || true

case "$CMD" in
  menu) menu ;;
  help|-h|--help) usage ;;
  us30|us30-high) run_us30_high 0 "$@" ;;
  btc|btc-high)   run_btc_high 0 "$@" ;;
  us30-history)   run_us30_high 1 "$@" ;;
  btc-history)    run_btc_high 1 "$@" ;;
  us30-light)     run_us30_light "$@" ;;
  btc-light)      run_btc_light "$@" ;;
  show)
    target="${1:-}"; [[ -n "$target" ]] || die "uso: show us30|btc"
    summarize_report "$(report_path "$target")"
    ;;
  open)
    target="${1:-}"; [[ -n "$target" ]] || die "uso: open us30|btc"
    open_file "$(report_path "$target")"
    ;;
  *)
    die "comando desconocido: $CMD (usa: ./trading.bash help)"
    ;;
esac
