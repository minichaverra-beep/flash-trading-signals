# BTC M5 — Revisión P&L última Entry (wrapper High, NO es señal nueva)
#
# Solo lee el último registro de live\btc_signal_history.json y califica
# P&L vs precio vivo. NO append al historial (eso lo hace analyze-btc-high.ps1).
# Categories: Revisión última Entry · P&L · Calificación (no "Entrada óptima" nueva).
#
# Uso:
#   .\scripts\analyze\analyze-btc-history.ps1
#   .\scripts\analyze\analyze-btc-history.ps1 -NoChart -Bearish -Break
#   .\scripts\analyze\analyze-btc-history.ps1 -NoChart -Bullish -Break -ML -Neural -Ilustrate
#   .\scripts\analyze\analyze-btc-history.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate -Advanced
#
# Bias: -Bullish | -Bearish   Setup: -Break | -Reverse
# -Bullish/-Bearish fijan el lado asumido si el historial no tiene `side`.
# -Advanced ON por defecto. Pasa -NoAdvanced para desactivar.
# Delega en analyze-btc-high.ps1 con -HistoryReview.

param(
    [switch]$NoChart,
    [switch]$ML,
    [switch]$Neural,
    [switch]$Bullish,
    [switch]$Bearish,
    [switch]$Break,
    [switch]$Reverse,
    [switch]$Advanced,
    [switch]$NoAdvanced,
    [Alias("Illustrate")]
    [switch]$Ilustrate,
    [string]$Symbol = "BTCUSDT"
)

$ErrorActionPreference = "Stop"
Set-Location (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

if ($Bullish -and $Bearish) {
    Write-Host "ERROR: -Bullish y -Bearish son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}
if ($Break -and $Reverse) {
    Write-Host "ERROR: -Break y -Reverse son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}
if ($Advanced -and $NoAdvanced) {
    Write-Host "ERROR: -Advanced y -NoAdvanced son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Revision P&L BTC: lee ultimo registro de live\btc_signal_history.json" -ForegroundColor Cyan
Write-Host "  Compara Entry previa vs precio actual (pts / % / EN BENEFICIO|PERDIDA)." -ForegroundColor Cyan
Write-Host "  NO es senal de entrada. NO escribe historial nuevo." -ForegroundColor DarkCyan
Write-Host ""

$highArgs = @{
    HistoryReview = $true
}
if ($NoChart) { $highArgs["NoChart"] = $true }
if ($ML) { $highArgs["ML"] = $true }
if ($Neural) { $highArgs["Neural"] = $true }
if ($Bullish) { $highArgs["Bullish"] = $true }
if ($Bearish) { $highArgs["Bearish"] = $true }
if ($Break) { $highArgs["Break"] = $true }
if ($Reverse) { $highArgs["Reverse"] = $true }
if ($Ilustrate) { $highArgs["Ilustrate"] = $true }
if (-not $NoAdvanced) { $highArgs["Advanced"] = $true }
if ($Symbol -ne "BTCUSDT") { $highArgs["Symbol"] = $Symbol }

Write-Host ">> BTC HISTORY-REVIEW (via High) - P&L ultima Entry..." -ForegroundColor Magenta

& (Join-Path $PSScriptRoot "analyze-btc-high.ps1") @highArgs
exit $LASTEXITCODE
