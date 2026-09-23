# XAUUSD M5 HIGH — análisis profundo (proxy GC=F / yfinance)
#
# Uso:
#   .\scripts\analyze\analyze-xauusd-high.ps1
#   .\scripts\analyze\analyze-xauusd-high.ps1 -NoChart -ML -Neural
#   .\scripts\analyze\analyze-xauusd-high.ps1 -NoChart -Bearish -Break
#   .\scripts\analyze\analyze-xauusd-high.ps1 -Bullish -Break -ML -Neural -Ilustrate
#
# Bias: -Bullish | -Bearish  ->  --bias bullish|bearish|auto
# Setup: -Break | -Reverse   ->  --setup break|reverse|auto
#
# -Ilustrate / -Illustrate: PNG anotado 2M5+OPTI (aunque -NoChart)
# Sin -NoChart: live\xauusd_m5_chart.png incluye líneas Entry/SL/TP/zona

param(
    [switch]$NoChart,
    [switch]$ML,
    [switch]$Neural,
    [switch]$Bullish,
    [switch]$Bearish,
    [switch]$Break,
    [switch]$Reverse,
    [switch]$Advanced,
    [Alias("Illustrate")]
    [switch]$Ilustrate,
    [switch]$HistoryReview,
    [switch]$NoOpen,
    [string]$Ticker = "",
    [string]$Entry = ""
)

$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
Set-Location (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

if ($Bullish -and $Bearish) {
    Write-Host "ERROR: -Bullish y -Bearish son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}
if ($Break -and $Reverse) {
    Write-Host "ERROR: -Break y -Reverse son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}

$argsList = @("-m", "app.controllers.analyze_xauusd_m5", "--mode", "high")
if ($Ticker) { $argsList += @("--ticker", $Ticker) }
if ($NoChart) { $argsList += "--no-chart" }
if ($ML) { $argsList += "--ml" }
if ($Neural) { $argsList += "--neural" }
if ($Advanced) { $argsList += "--advanced" }
if ($Ilustrate) { $argsList += "--ilustrate" }
if ($HistoryReview) { $argsList += "--history-review" }
if ($NoOpen) { $argsList += "--no-open" }
if ($Entry) { $argsList += @("--entry", $Entry) }

if ($Bullish) { $argsList += @("--bias", "bullish") }
elseif ($Bearish) { $argsList += @("--bias", "bearish") }
else { $argsList += @("--bias", "auto") }

if ($Break) { $argsList += @("--setup", "break") }
elseif ($Reverse) { $argsList += @("--setup", "reverse") }
else { $argsList += @("--setup", "auto") }

$modeHint = @()
if ($Bullish) { $modeHint += "BULLISH" }
elseif ($Bearish) { $modeHint += "BEARISH" }
if ($Break) { $modeHint += "BREAK" }
elseif ($Reverse) { $modeHint += "REVERSE" }
$modeLabel = if ($modeHint.Count -gt 0) { " [" + ($modeHint -join " + ") + "]" } else { "" }

Write-Host ">> XAUUSD M5 HIGH$modeLabel (GC=F proxy)..." -ForegroundColor Magenta
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_xauusd_m5 ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Salida HIGH (Angular lee CURSOR_TRADING_ROOT\live\):" -ForegroundColor Green
Write-Host "  live\xauusd_m5_high_signal.md" -ForegroundColor Yellow
if (-not $NoChart) {
    Write-Host "  live\xauusd_m5_chart.png (OPTI/SL/TP/zona)" -ForegroundColor Yellow
}
if ($Ilustrate) {
    Write-Host "  live\xauusd_m5_chart_annotated.png" -ForegroundColor Yellow
}
