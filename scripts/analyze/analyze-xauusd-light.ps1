# Snapshot LIGHT XAUUSD M5 (mínimo tokens, señal rápida)
# Uso: .\scripts\analyze\analyze-xauusd-light.ps1

param(
    [switch]$ML,
    [switch]$Neural,
    [switch]$Bullish,
    [switch]$Bearish,
    [string]$Ticker = ""
)

$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
Set-Location (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

if ($Bullish -and $Bearish) {
    Write-Host "ERROR: -Bullish y -Bearish son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}

$argsList = @("-m", "app.controllers.analyze_xauusd_m5", "--mode", "light", "--no-chart")
if ($Ticker) { $argsList += @("--ticker", $Ticker) }
if ($ML) { $argsList += "--ml" }
if ($Neural) { $argsList += "--neural" }
if ($Bullish) { $argsList += @("--bias", "bullish") }
elseif ($Bearish) { $argsList += @("--bias", "bearish") }

Write-Host ">> XAUUSD M5 LIGHT..." -ForegroundColor Cyan
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_xauusd_m5 ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Salida LIGHT:" -ForegroundColor Green
Write-Host "  live\xauusd_m5_signal.md" -ForegroundColor Yellow
