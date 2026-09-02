# Snapshot COMPLETO US30 M5 (grafico + checklist + analisis detallado)
# Uso: .\scripts\analyze\analyze-us30.ps1
#      .\scripts\analyze\analyze-us30.ps1 -All -NoChart -ML -Neural

param(
    [switch]$NoChart,
    [switch]$Both,
    [switch]$All,
    [switch]$ML,
    [switch]$Neural,
    [switch]$Bullish,
    [switch]$Bearish,
    [switch]$Break,
    [switch]$Reverse,
    [string]$Ticker = ""
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

if ($All) { $mode = "all" }
elseif ($Both) { $mode = "both" }
else { $mode = "full" }

$argsList = @("-m", "app.controllers.analyze_us30_m5", "--mode", $mode)
if ($Ticker) { $argsList += @("--ticker", $Ticker) }
if ($NoChart) { $argsList += "--no-chart" }
if ($ML) { $argsList += "--ml" }
if ($Neural) { $argsList += "--neural" }
if ($Bullish) { $argsList += @("--bias", "bullish") }
elseif ($Bearish) { $argsList += @("--bias", "bearish") }
if ($Break) { $argsList += @("--setup", "break") }
elseif ($Reverse) { $argsList += @("--setup", "reverse") }

Write-Host ">> US30 M5 mode=$mode (yfinance)..." -ForegroundColor Cyan
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_us30_m5 ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Cursor FULL:" -ForegroundColor Green
Write-Host '  analiza @live/us30_m5_snapshot.md con mi plan E1 M5' -ForegroundColor Yellow
if ($Both -or $All) {
    Write-Host "Cursor LIGHT:" -ForegroundColor Green
    Write-Host '  @live/us30_m5_signal.md @docs/protocols/TRADING_LIVE_US30_SIGNAL_LIGHT.md' -ForegroundColor Yellow
}
if ($All) {
    Write-Host "Cursor HIGH:" -ForegroundColor Green
    Write-Host '  @live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md' -ForegroundColor Yellow
}
