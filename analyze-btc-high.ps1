# Thin wrapper — prefer: .\scripts\analyze\analyze-btc-high.ps1
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
    [string]$Symbol = "BTCUSDT",
    [string]$Entry = ""
)

$ErrorActionPreference = "Stop"
& (Join-Path $PSScriptRoot "scripts\analyze\analyze-btc-high.ps1") @PSBoundParameters
exit $LASTEXITCODE
