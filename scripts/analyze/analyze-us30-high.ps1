# US30 M5 HIGH - analisis profundo CRT + Turtle Soup

# Uso:

#   .\scripts\analyze\analyze-us30-high.ps1

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -ML -Neural

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate

# -Ilustrate / -Illustrate: PNG anotado 2M5+OPTI (aunque -NoChart)



param(

    [switch]$NoChart,

    [switch]$ML,

    [switch]$Neural,

    [switch]$Bullish,

    [switch]$Bearish,

    [switch]$Break,

    [switch]$Reverse,

    [Alias("Illustrate")]
    [switch]$Ilustrate,

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



$argsList = @("-m", "app.controllers.analyze_us30_m5", "--mode", "high")

if ($Ticker) { $argsList += @("--ticker", $Ticker) }

if ($NoChart) { $argsList += "--no-chart" }

if ($ML) { $argsList += "--ml" }

if ($Neural) { $argsList += "--neural" }

if ($Ilustrate) { $argsList += "--ilustrate" }



if ($Bullish) { $argsList += @("--bias", "bullish") }

elseif ($Bearish) { $argsList += @("--bias", "bearish") }

else { $argsList += @("--bias", "auto") }



if ($Break) { $argsList += @("--setup", "break") }

elseif ($Reverse) { $argsList += @("--setup", "reverse") }

else { $argsList += @("--setup", "auto") }



Write-Host ">> US30 M5 HIGH - CRT + Turtle Soup..." -ForegroundColor Magenta

python @argsList

if ($LASTEXITCODE -ne 0) {

    Write-Host "ERROR: fallo python -m app.controllers.analyze_us30_m5 ($LASTEXITCODE)" -ForegroundColor Red

    exit $LASTEXITCODE

}



Write-Host ""

Write-Host "Cursor HIGH (max contexto):" -ForegroundColor Green

Write-Host '  @live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md analisis E1 CRT' -ForegroundColor Yellow

