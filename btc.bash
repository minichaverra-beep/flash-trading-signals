#!/usr/bin/env bash
# =============================================================================
# btc.bash — Señales BTC High SIN Cursor AI
# =============================================================================
# Atajo dedicado BTC (paralelo a us30.bash / trading.bash).
#
# Uso (Git Bash / WSL):
#   cd "/d/Danilo/Trading/Cursor Trading"
#   bash btc.bash                              # High Bullish+Break+ML+Neural+Ilustrate
#   bash btc.bash --bearish --break
#   bash btc.bash --bullish --reverse --entry 97450.5
#   bash btc.bash history                      # P&L última Entry (NO es señal)
#   bash btc.bash light
#   bash btc.bash show
#   bash btc.bash open
#   bash btc.bash menu
#   bash btc.bash help
# =============================================================================

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TRADING="$ROOT/trading.bash"

[[ -f "$TRADING" ]] || { echo "ERROR: no existe trading.bash en $ROOT" >&2; exit 1; }

usage() {
  cat <<'EOF'
btc.bash — señales BTC sin Cursor AI

COMANDOS
  (sin comando)   High BTC — default: bullish + break + ml + neural + ilustrate
  high            Igual que sin comando
  history         Revisión P&L última Entry (NO es señal)
  light           Chequeo Light + ML + Neural
  show            Resumen del último live/btc_m5_high_signal.md
  open            Abrir el reporte .md
  menu            Menú interactivo BTC
  help            Esta ayuda

FLAGS High / History
  --bullish | --bearish     Bias (default: --bullish)
  --break   | --reverse     Setup (default: --break)
  --entry PRECIO            Fill usuario (solo High)
  --no-ml | --no-neural | --no-ilustrate
  --chart | --no-open | --advanced

EJEMPLOS
  bash btc.bash
  bash btc.bash --bearish --break
  bash btc.bash --bullish --break --entry 97450.5
  bash btc.bash history --bullish --break
  bash btc.bash show

REGLAS DURAS
  • Zona + 2 velas M5 · R:R ≥ 1:2 · 2 SL = fin de sesión
  • Confirmar siempre en TradingView BTCUSDT M5
EOF
}

menu() {
  local C_BOLD C_RST
  if [[ -t 1 ]]; then C_BOLD=$'\033[1m'; C_RST=$'\033[0m'; else C_BOLD=; C_RST=; fi
  while true; do
    echo ""
    echo "${C_BOLD}=== BTC Trading (sin AI) ===${C_RST}"
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
      1) bash "$TRADING" btc --bullish --break ;;
      2) bash "$TRADING" btc --bearish --break ;;
      3) bash "$TRADING" btc --bullish --reverse ;;
      4) bash "$TRADING" btc --bearish --reverse ;;
      5) bash "$TRADING" btc-history --bullish --break ;;
      6) bash "$TRADING" btc-light ;;
      7) bash "$TRADING" show btc ;;
      o|O) bash "$TRADING" open btc ;;
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
    bash "$TRADING" btc "$@"
    ;;
  history)
    shift || true
    bash "$TRADING" btc-history "$@"
    ;;
  light)
    shift || true
    bash "$TRADING" btc-light "$@"
    ;;
  show)
    bash "$TRADING" show btc
    ;;
  open)
    bash "$TRADING" open btc
    ;;
  --*)
    # Flags directos: bash btc.bash --bearish --break
    bash "$TRADING" btc "$@"
    ;;
  *)
    # Si el primer arg no es subcomando, tratar todo como flags de High
    bash "$TRADING" btc "$@"
    ;;
esac
