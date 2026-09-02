# BTC M5 HIGH - analisis profundo CRT + Turtle Soup (max tokens)

# Uso:

#   .\scripts\analyze\analyze-btc-high.ps1

#   .\scripts\analyze\analyze-btc-high.ps1 -NoChart

#   .\scripts\analyze\analyze-btc-high.ps1 -NoChart -ML -Neural          # auto-activa Advanced
#   .\scripts\analyze\analyze-btc-high.ps1 -NoChart -Advanced -ML -Neural

#   .\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break

#   .\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bullish -Reverse

#   .\scripts\analyze\analyze-btc-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate

#

# Bias (mutuamente excluyente): -Bullish | -Bearish  ->  --bias bullish|bearish|neutral

# Setup (mutuamente excluyente): -Break | -Reverse   ->  --setup break|reverse|auto

#   break   = E1 CRT continuacion

#   reverse = E2 turtle soup / reversal watchlist

# -Ilustrate / -Illustrate: PNG anotado 2M5+OPTI (aunque -NoChart)



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



$argsList = @("-m", "app.controllers.analyze_btc_m5", "--symbol", $Symbol, "--mode", "high")

if ($NoChart) { $argsList += "--no-chart" }

if ($ML) { $argsList += "--ml" }

if ($Neural) { $argsList += "--neural" }

if ($Ilustrate) { $argsList += "--ilustrate" }

# Advanced: explicit flag, or auto when ML + Neural both set
$useAdvanced = $Advanced -or ($ML -and $Neural)
if ($useAdvanced) { $argsList += "--advanced" }

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



$advLabel = if ($useAdvanced) { " [ADVANCED]" } else { "" }
Write-Host ">> BTC M5 HIGH ($Symbol)$modeLabel$advLabel - CRT + Turtle Soup..." -ForegroundColor Magenta

python @argsList

if ($LASTEXITCODE -ne 0) {

    Write-Host "ERROR: fallo python -m app.controllers.analyze_btc_m5 ($LASTEXITCODE)" -ForegroundColor Red

    exit $LASTEXITCODE

}



Write-Host ""

Write-Host "Cursor HIGH (max contexto):" -ForegroundColor Green

if ($useAdvanced) {
    Write-Host '  @live/btc_m5_high_signal.md @docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md analisis ADVANCED E1 CRT' -ForegroundColor Yellow
} else {
    Write-Host '  @live/btc_m5_high_signal.md @docs/protocols/TRADING_LIVE_BTC_HIGH_SIGNAL.md analisis E1 CRT' -ForegroundColor Yellow
}

