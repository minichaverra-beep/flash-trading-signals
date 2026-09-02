# Thin wrapper — prefer: .\scripts\analyze\analyze-us30-high.ps1
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
    [string]$Ticker = ""
)

$ErrorActionPreference = "Stop"
& (Join-Path $PSScriptRoot "scripts\analyze\analyze-us30-high.ps1") @PSBoundParameters
exit $LASTEXITCODE
