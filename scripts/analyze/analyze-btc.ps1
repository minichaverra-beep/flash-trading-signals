# Snapshot COMPLETO BTC M5 (grafico + checklist + analisis detallado)
# Uso: .\scripts\analyze\analyze-btc.ps1
#      .\scripts\analyze\analyze-btc.ps1 -NoChart
#      .\scripts\analyze\analyze-btc.ps1 -Both    # full + light
#      .\scripts\analyze\analyze-btc.ps1 -All    # full + light + high
#      .\scripts\analyze\analyze-btc.ps1 -ML     # incluye ML prob en Categories
#      .\scripts\analyze\analyze-btc.ps1 -Neural # incluye Neural galería en Categories
#      .\scripts\analyze\analyze-btc.ps1 -All -NoChart -ML -Neural
#      .\scripts\analyze\analyze-btc.ps1 -All -NoChart -Bearish -Break   # bias/setup pasan al tier High

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

if ($All) { $mode = "all" }
elseif ($Both) { $mode = "both" }
else { $mode = "full" }

$argsList = @("-m", "app.controllers.analyze_btc_m5", "--symbol", $Symbol, "--mode", $mode)
if ($NoChart) { $argsList += "--no-chart" }
if ($ML) { $argsList += "--ml" }
if ($Neural) { $argsList += "--neural" }
if ($Bullish) { $argsList += @("--bias", "bullish") }
elseif ($Bearish) { $argsList += @("--bias", "bearish") }
if ($Break) { $argsList += @("--setup", "break") }
elseif ($Reverse) { $argsList += @("--setup", "reverse") }

Write-Host ">> BTC M5 mode=$mode ($Symbol)..." -ForegroundColor Cyan
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_btc_m5 ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Cursor FULL:" -ForegroundColor Green
Write-Host '  analiza @live/btc_m5_snapshot.md con mi plan E1 M5' -ForegroundColor Yellow
if ($Both -or $All) {
    Write-Host "Cursor LIGHT:" -ForegroundColor Green
    Write-Host '  @live/btc_m5_signal.md @docs/protocols/TRADING_LIVE_BTC_SIGNAL_LIGHT.md' -ForegroundColor Yellow
}
if ($All) {
    Write-Host "Cursor HIGH:" -ForegroundColor Green
    Write-Host '  @live/btc_m5_high_signal.md @docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md' -ForegroundColor Yellow

    $superHighCapture = $false
    foreach ($ext in @(".png", ".jpg", ".jpeg", ".webp")) {
        if (Test-Path (Join-Path "live" ("super_high_entry" + $ext))) {
            $superHighCapture = $true
            break
        }
    }
    if (-not $superHighCapture -and (Test-Path "live/super_high_captures")) {
        $imgs = Get-ChildItem "live/super_high_captures" -File -ErrorAction SilentlyContinue |
            Where-Object { @(".png", ".jpg", ".jpeg", ".webp") -contains $_.Extension.ToLower() }
        if ($imgs.Count -gt 0) { $superHighCapture = $true }
    }
    if ($superHighCapture) {
        Write-Host ">> Super High (captura detectada)..." -ForegroundColor Magenta
        $shArgs = @("-m", "app.controllers.analyze_super_high_entry", "--ml", "--neural")
        python @shArgs
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Cursor SUPER HIGH:" -ForegroundColor Green
            Write-Host '  @live/btc_super_high_signal.md @docs/protocols/TRADING_LIVE_BTC_SUPER_HIGH_SIGNAL.md' -ForegroundColor Yellow
        } else {
            Write-Host "WARN: Super High omitido (fallo python -m app.controllers.analyze_super_high_entry)" -ForegroundColor Yellow
        }
    }
}
