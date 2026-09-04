# US30 M5 HIGH - analisis profundo CRT + Turtle Soup (max tokens)

# Uso:

#   .\scripts\analyze\analyze-us30-high.ps1

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -ML -Neural          # auto-activa Advanced
#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -Advanced -ML -Neural

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bullish -Reverse

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bearish -Break -ML -Neural -Ilustrate

#   .\scripts\analyze\analyze-us30-high.ps1 -NoChart -Bullish -Reverse -ML -Neural -Ilustrate -Advanced -Entry 53128

#

# Bias (mutuamente excluyente): -Bullish | -Bearish  ->  --bias bullish|bearish|neutral

# Setup (mutuamente excluyente): -Break | -Reverse   ->  --setup break|reverse|auto

#   break   = E1 CRT continuacion / breakout

#   reverse = E2 turtle soup / reversal (operable con 2 velas + winrate)

# -Ilustrate / -Illustrate: PNG anotado 2M5+OPTI (aunque -NoChart)

# -Entry: fill usuario (Entry usuario); Entrada óptima sigue siendo sistema



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

    [string]$Ticker = "",

    [string]$Entry = ""

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

if ($HistoryReview) { $argsList += "--history-review" }

if ($Entry) { $argsList += @("--entry", $Entry) }

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
$histLabel = if ($HistoryReview) { " [HISTORY-REVIEW]" } else { "" }
$entryLabel = if ($Entry) { " [ENTRY $Entry]" } else { "" }
Write-Host ">> US30 M5 HIGH$modeLabel$advLabel$histLabel$entryLabel - CRT + Turtle Soup..." -ForegroundColor Magenta

python @argsList

if ($LASTEXITCODE -ne 0) {

    Write-Host "ERROR: fallo python -m app.controllers.analyze_us30_m5 ($LASTEXITCODE)" -ForegroundColor Red

    exit $LASTEXITCODE

}



Write-Host ""

Write-Host "Cursor HIGH (max contexto):" -ForegroundColor Green

if ($useAdvanced) {
    Write-Host '  @live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md analisis ADVANCED E1 CRT' -ForegroundColor Yellow
} else {
    Write-Host '  @live/us30_m5_high_signal.md @docs/protocols/TRADING_LIVE_US30_HIGH_SIGNAL.md analisis E1 CRT' -ForegroundColor Yellow
}
