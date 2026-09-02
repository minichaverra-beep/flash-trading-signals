# Snapshot LIGHT BTC M5 (minimo tokens, senal rapida)
# Uso: .\scripts\analyze\analyze-btc-light.ps1

param(
    [switch]$ML,
    [switch]$Neural,
    [switch]$Bullish,
    [switch]$Bearish,
    [string]$Symbol = "BTCUSDT"
)

$ErrorActionPreference = "Stop"
Set-Location (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

if ($Bullish -and $Bearish) {
    Write-Host "ERROR: -Bullish y -Bearish son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}

$argsList = @("-m", "app.controllers.analyze_btc_m5", "--symbol", $Symbol, "--mode", "light", "--no-chart")
if ($ML) { $argsList += "--ml" }
if ($Neural) { $argsList += "--neural" }
if ($Bullish) { $argsList += @("--bias", "bullish") }
elseif ($Bearish) { $argsList += @("--bias", "bearish") }

Write-Host ">> BTC M5 LIGHT ($Symbol)..." -ForegroundColor Cyan
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_btc_m5 ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Cursor LIGHT:" -ForegroundColor Green
Write-Host '  @live/btc_m5_signal.md @docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md' -ForegroundColor Yellow
