#!/usr/bin/env bash
# =============================================================================
# us30.bash — Señales US30 High SIN Cursor AI
# =============================================================================
# Atajo dedicado US30 (paralelo a btc.bash / trading.bash).
#
# Uso (Git Bash / WSL):
#   cd "/d/Danilo/Trading/Cursor Trading"
#   bash us30.bash                             # High Bullish+Break+ML+Neural+Ilustrate
#   bash us30.bash --bearish --break
#   bash us30.bash --bullish --reverse --entry 53128
#   bash us30.bash history
#   bash us30.bash light
#   bash us30.bash show
#   bash us30.bash open
#   bash us30.bash menu
#   bash us30.bash help
# =============================================================================

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TRADING="$ROOT/trading.bash"

[[ -f "$TRADING" ]] || { echo "ERROR: no existe trading.bash en $ROOT" >&2; exit 1; }

usage() {
  cat <<'EOF'
us30.bash — señales US30 sin Cursor AI

COMANDOS
  (sin comando)   High US30 — default: bullish + break + ml + neural + ilustrate
  high            Igual que sin comando
  history         Revisión P&L última Entry (NO es señal)
  light           Chequeo Light + ML + Neural
  show            Resumen del último live/us30_m5_high_signal.md
  open            Abrir el reporte .md
  menu            Menú interactivo US30
  help            Esta ayuda

FLAGS High / History
  --bullish | --bearish     Bias (default: --bullish)
  --break   | --reverse     Setup (default: --break)
  --entry PRECIO            Fill usuario (solo High)
  --no-ml | --no-neural | --no-ilustrate
  --chart | --no-open | --advanced

EJEMPLOS
  bash us30.bash
  bash us30.bash --bearish --break
  bash us30.bash --bullish --reverse --entry 53128
  bash us30.bash history --bullish --break
  bash us30.bash show

REGLAS DURAS
  • Zona + 2 velas M5 · SL ~$9 · R:R ≥ 1:2 · 2 SL = fin de sesión
  • Confirmar siempre en TradingView US30 M5
EOF
}

menu() {
  local C_BOLD C_RST
  if [[ -t 1 ]]; then C_BOLD=$'\033[1m'; C_RST=$'\033[0m'; else C_BOLD=; C_RST=; fi
  while true; do
    echo ""
    echo "${C_BOLD}=== US30 Trading (sin AI) ===${C_RST}"
    echo "  1) High  Bullish+Break   (día a día)"
    echo "  2) High  Bearish+Break"
    echo "  3) High  Bullish+Reverse"
    echo "  4) High  Bearish+Reverse"
    echo "  5) History P&L (última Entry)"
    echo "  6) Light"
    echo "  7) Ver resumen"
    echo "  o) Abrir reporte"
    echo "  h) Ayuda"
    echo "  q) Salir"
    read -r -p "Opción: " opt
    case "$opt" in
      1) bash "$TRADING" us30 --bullish --break ;;
      2) bash "$TRADING" us30 --bearish --break ;;
      3) bash "$TRADING" us30 --bullish --reverse ;;
      4) bash "$TRADING" us30 --bearish --reverse ;;
      5) bash "$TRADING" us30-history --bullish --break ;;
      6) bash "$TRADING" us30-light ;;
      7) bash "$TRADING" show us30 ;;
      o|O) bash "$TRADING" open us30 ;;
      h|H) usage ;;
      q|Q) echo "Listo."; exit 0 ;;
      *) echo "Opción inválida" ;;
    esac
  done
}

CMD="${1:-high}"
case "$CMD" in
  help|-h|--help)
    usage
    ;;
  menu)
    menu
    ;;
  high)
    shift || true
    bash "$TRADING" us30 "$@"
    ;;
  history)
    shift || true
    bash "$TRADING" us30-history "$@"
    ;;
  light)
    shift || true
    bash "$TRADING" us30-light "$@"
    ;;
  show)
    bash "$TRADING" show us30
    ;;
  open)
    bash "$TRADING" open us30
    ;;
  --*)
    bash "$TRADING" us30 "$@"
    ;;
  *)
    bash "$TRADING" us30 "$@"
    ;;
esac
