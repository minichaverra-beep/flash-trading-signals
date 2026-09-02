# BTC M5 SUPER HIGH - analisis captura usuario entry/SL/TP (tier mas profundo)
# Uso: .\scripts\analyze\analyze-btc-superhigh.ps1
# Requiere: live/super_high_entry.png (captura TradingView con entry, SL, TP)

param(
    [switch]$ML,
    [switch]$Neural,
    [switch]$Bullish,
    [switch]$Bearish,
    [switch]$SmokeTest
)

$ErrorActionPreference = "Stop"
Set-Location (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

if ($Bullish -and $Bearish) {
    Write-Host "ERROR: -Bullish y -Bearish son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}

$extensions = @(".png", ".jpg", ".jpeg", ".webp")
$captureFound = $false
foreach ($ext in $extensions) {
    $p = Join-Path "live" ("super_high_entry" + $ext)
    if (Test-Path $p) {
        $captureFound = $true
        break
    }
}
if (-not $captureFound) {
    $capDir = Join-Path "live" "super_high_captures"
    if (Test-Path $capDir) {
        $imgs = Get-ChildItem $capDir -File | Where-Object { $extensions -contains $_.Extension.ToLower() }
        if ($imgs.Count -gt 0) { $captureFound = $true }
    }
}

if (-not $captureFound -and -not $SmokeTest) {
    Write-Host "ERROR: no se encontro captura en live/super_high_entry.*" -ForegroundColor Red
    Write-Host "  1. En TradingView M5: dibuja entry, SL y TP" -ForegroundColor Yellow
    Write-Host "  2. Guarda captura como live/super_high_entry.png" -ForegroundColor Yellow
    Write-Host "  3. (Opcional) live/super_high_entry.md con entry/SL/TP/direction" -ForegroundColor Yellow
    Write-Host "  4. Vuelve a ejecutar .\scripts\analyze\analyze-btc-superhigh.ps1" -ForegroundColor Yellow
    exit 1
}

$argsList = @("-m", "app.controllers.analyze_super_high_entry")
if ($ML) { $argsList += "--ml" }
if ($Neural) { $argsList += "--neural" }
if (-not $ML -and -not $Neural) {
    $argsList += "--ml"
    $argsList += "--neural"
}
if ($SmokeTest) { $argsList += "--smoke-test" }
if ($Bullish) { $argsList += @("--bias", "bullish") }
elseif ($Bearish) { $argsList += @("--bias", "bearish") }

Write-Host ">> BTC M5 SUPER HIGH - captura entry/SL/TP..." -ForegroundColor Magenta
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_super_high_entry ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Cursor SUPER HIGH (max profundidad + captura usuario):" -ForegroundColor Green
Write-Host '  @live/btc_super_high_signal.md @docs/protocols/TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md' -ForegroundColor Yellow
