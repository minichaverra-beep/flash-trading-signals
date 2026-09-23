# XAUUSD M5 — History (compat Angular)
#
# El controller analyze_xauusd_m5 aún no implementa --history-review ni
# live\xauusd_signal_history.json. Este wrapper regenera HIGH (lectura fresca)
# para que POST /api/signals/run?market=xauusd&tier=history no falle.
#
# Uso:
#   .\scripts\analyze\analyze-xauusd-history.ps1
#   .\scripts\analyze\analyze-xauusd-history.ps1 -NoChart -Bearish -Break -ML -Neural

param(
    [switch]$NoChart,
    [switch]$ML,
    [switch]$Neural,
    [switch]$Bullish,
    [switch]$Bearish,
    [switch]$Break,
    [switch]$Reverse,
    [switch]$Advanced,
    [switch]$NoAdvanced,
    [Alias("Illustrate")]
    [switch]$Ilustrate,
    [switch]$NoOpen,
    [string]$Ticker = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $ProjectRoot.Path
$env:PYTHONIOENCODING = "utf-8"

if ($Bullish -and $Bearish) {
    Write-Host "ERROR: -Bullish y -Bearish son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}
if ($Break -and $Reverse) {
    Write-Host "ERROR: -Break y -Reverse son mutuamente excluyentes." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "WARN: History-Review XAUUSD no está implementado aún." -ForegroundColor DarkYellow
Write-Host "  Se regenera HIGH (live\xauusd_m5_high_signal.md) como fallback." -ForegroundColor DarkYellow
Write-Host ""

$highArgs = @{}
if ($NoChart) { $highArgs["NoChart"] = $true }
if ($ML) { $highArgs["ML"] = $true }
if ($Neural) { $highArgs["Neural"] = $true }
if ($Bullish) { $highArgs["Bullish"] = $true }
if ($Bearish) { $highArgs["Bearish"] = $true }
if ($Break) { $highArgs["Break"] = $true }
if ($Reverse) { $highArgs["Reverse"] = $true }
if ($Ilustrate) { $highArgs["Ilustrate"] = $true }
if ($Advanced -and -not $NoAdvanced) { $highArgs["Advanced"] = $true }
if ($NoOpen) { $highArgs["NoOpen"] = $true }
if ($Ticker) { $highArgs["Ticker"] = $Ticker }

Write-Host ">> XAUUSD HISTORY (fallback via High)..." -ForegroundColor Magenta
& (Join-Path $PSScriptRoot "analyze-xauusd-high.ps1") @highArgs
exit $LASTEXITCODE
