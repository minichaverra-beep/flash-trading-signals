#Requires -Version 5.1
<#
.SYNOPSIS
  Atajo XAUUSD (paralelo a btc.bash / us30.bash) — regenera senal en live/.
.DESCRIPTION
  Cd a Cursor Trading, invoca scripts\analyze\analyze-xauusd-*.ps1.
  Angular (flash-signals-angular) lee los mismos archivos via
  CURSOR_TRADING_ROOT\live\ — no hace falta copiar.

.EXAMPLE
  .\xauusd.ps1
  .\xauusd.ps1 -Bearish -Break
  .\xauusd.ps1 light
  .\xauusd.ps1 context
  .\xauusd.ps1 show
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$Command = "high",

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
    [switch]$NoOpen,
    [string]$Ticker = "",
    [string]$Entry = ""
)

$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot
if (-not $Root) { $Root = Split-Path -Parent $MyInvocation.MyCommand.Path }
Set-Location -LiteralPath $Root

$env:PYTHONIOENCODING = "utf-8"
try {
    chcp 65001 | Out-Null
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
} catch {}

if ([string]::IsNullOrWhiteSpace($Command)) { $Command = "high" }
$Command = $Command.Trim().ToLowerInvariant()

function Show-Help {
    Write-Host "xauusd.ps1 - senales XAUUSD (proxy GC=F) sin Cursor AI"
    Write-Host ""
    Write-Host "COMANDOS"
    Write-Host "  (sin comando) / high   High - default: chart OPTI + -ML -Neural -Bullish -Break"
    Write-Host "  light                  Chequeo Light + ML + Neural"
    Write-Host "  context                Estructura M5 (sin Entry)"
    Write-Host "  history                Fallback High (P&L review aun no en controller)"
    Write-Host "  show                   Resumen del ultimo live\xauusd_m5_high_signal.md"
    Write-Host "  open                   Abrir el reporte .md"
    Write-Host "  help                   Esta ayuda"
    Write-Host ""
    Write-Host "FLAGS High"
    Write-Host "  -Bullish | -Bearish    Bias (default High: -Bullish)"
    Write-Host "  -Break   | -Reverse    Setup (default High: -Break)"
    Write-Host "  -NoChart               Omitir PNG (default: chart con OPTI/SL/TP/zona)"
    Write-Host "  -ML -Neural -Ilustrate -Ticker GC=F"
    Write-Host ""
    Write-Host "EJEMPLOS"
    Write-Host "  .\xauusd.ps1"
    Write-Host "  .\xauusd.ps1 -Bearish -Break"
    Write-Host "  .\xauusd.ps1 light"
    Write-Host "  .\xauusd.ps1 show"
    Write-Host ""
    Write-Host "Angular lee: CURSOR_TRADING_ROOT\live\xauusd_m5_*.md"
}

function Show-Summary {
    $path = Join-Path $Root "live\xauusd_m5_high_signal.md"
    if (-not (Test-Path -LiteralPath $path)) {
        Write-Host "No existe $path - genera primero con .\xauusd.ps1" -ForegroundColor Yellow
        return
    }
    $mtime = (Get-Item -LiteralPath $path).LastWriteTime
    Write-Host "=== live\xauusd_m5_high_signal.md  ($mtime) ===" -ForegroundColor Cyan
    Get-Content -LiteralPath $path -TotalCount 40 -Encoding UTF8
    Write-Host "..." -ForegroundColor DarkGray
}

switch ($Command) {
    "help" {
        Show-Help
        exit 0
    }
    "show" {
        Show-Summary
        exit 0
    }
    "open" {
        $path = Join-Path $Root "live\xauusd_m5_high_signal.md"
        if (-not (Test-Path -LiteralPath $path)) {
            Write-Error "No existe $path"
            exit 1
        }
        Invoke-Item -LiteralPath $path
        exit 0
    }
    { $_ -in @("high", "light", "context", "history") } {
        # continue below
    }
    default {
        Write-Host "Comando desconocido: $Command" -ForegroundColor Red
        Show-Help
        exit 1
    }
}

# Defaults dia a dia — chart ON para líneas OPTI/SL/TP/zona (usar -NoChart si no hace falta PNG)
if ($Command -eq "high") {
    if (-not $PSBoundParameters.ContainsKey("ML")) { $ML = $true }
    if (-not $PSBoundParameters.ContainsKey("Neural")) { $Neural = $true }
    if (-not $Bullish -and -not $Bearish) { $Bullish = $true }
    if (-not $Break -and -not $Reverse) { $Break = $true }
}

$analyzeDir = Join-Path $Root "scripts\analyze"
$scriptMap = @{
    high    = "analyze-xauusd-high.ps1"
    light   = "analyze-xauusd-light.ps1"
    context = "analyze-xauusd-context.ps1"
    history = "analyze-xauusd-history.ps1"
}
$scriptName = $scriptMap[$Command]
$scriptPath = Join-Path $analyzeDir $scriptName
if (-not (Test-Path -LiteralPath $scriptPath)) {
    Write-Error "No existe $scriptPath"
    exit 1
}

$forward = @{}
if ($Command -eq "context") {
    # sin params
}
elseif ($Command -eq "light") {
    if ($ML) { $forward["ML"] = $true }
    if ($Neural) { $forward["Neural"] = $true }
    if ($Bullish) { $forward["Bullish"] = $true }
    if ($Bearish) { $forward["Bearish"] = $true }
    if ($Ticker) { $forward["Ticker"] = $Ticker }
    if (-not $forward.ContainsKey("ML")) { $forward["ML"] = $true }
    if (-not $forward.ContainsKey("Neural")) { $forward["Neural"] = $true }
}
else {
    # high / history
    if ($NoChart) { $forward["NoChart"] = $true }
    if ($ML) { $forward["ML"] = $true }
    if ($Neural) { $forward["Neural"] = $true }
    if ($Bullish) { $forward["Bullish"] = $true }
    if ($Bearish) { $forward["Bearish"] = $true }
    if ($Break) { $forward["Break"] = $true }
    if ($Reverse) { $forward["Reverse"] = $true }
    if ($Advanced) { $forward["Advanced"] = $true }
    if ($Ilustrate) { $forward["Ilustrate"] = $true }
    if ($NoOpen) { $forward["NoOpen"] = $true }
    if ($Ticker) { $forward["Ticker"] = $Ticker }
    if ($Entry -and $Command -eq "high") { $forward["Entry"] = $Entry }
}

Write-Host ""
Write-Host "=== XAUUSD ($Command) ===" -ForegroundColor Cyan
Write-Host "Root: $Root"
& $scriptPath @forward
$code = $LASTEXITCODE

if ($code -eq 0) {
    Write-Host ""
    Write-Host "OK - Angular (flash-signals-angular) puede leer market=xauusd desde live\" -ForegroundColor Green
}
exit $code
