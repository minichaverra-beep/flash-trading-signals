# Snapshot COMPLETO XAUUSD M5 (gráfico + checklist)
# Uso: .\scripts\analyze\analyze-xauusd.ps1
#      .\scripts\analyze\analyze-xauusd.ps1 -All -NoChart -ML -Neural

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

if ($All) { $mode = "all" }
elseif ($Both) { $mode = "both" }
else { $mode = "full" }

$argsList = @("-m", "app.controllers.analyze_xauusd_m5", "--mode", $mode)
if ($Ticker) { $argsList += @("--ticker", $Ticker) }
if ($NoChart) { $argsList += "--no-chart" }
if ($ML) { $argsList += "--ml" }
if ($Neural) { $argsList += "--neural" }
if ($Bullish) { $argsList += @("--bias", "bullish") }
elseif ($Bearish) { $argsList += @("--bias", "bearish") }
if ($Break) { $argsList += @("--setup", "break") }
elseif ($Reverse) { $argsList += @("--setup", "reverse") }

Write-Host ">> XAUUSD M5 mode=$mode (yfinance GC=F)..." -ForegroundColor Cyan
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_xauusd_m5 ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Salida FULL:" -ForegroundColor Green
Write-Host "  live\xauusd_m5_snapshot.md" -ForegroundColor Yellow
if ($Both -or $All) {
    Write-Host "Salida LIGHT:" -ForegroundColor Green
    Write-Host "  live\xauusd_m5_signal.md" -ForegroundColor Yellow
}
if ($All) {
    Write-Host "Salida HIGH:" -ForegroundColor Green
    Write-Host "  live\xauusd_m5_high_signal.md" -ForegroundColor Yellow
}
