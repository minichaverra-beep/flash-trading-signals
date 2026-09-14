# US30 M5 CONTEXT — estructura / vigente vs agotando (sin params)
# Uso: .\scripts\analyze\analyze-us30-context.ps1
# NO es señal de entrada (sin Entry/SL/TP). Distinto de Light/High.

$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
Set-Location (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

$argsList = @(
    "-m", "app.controllers.analyze_us30_m5",
    "--mode", "context",
    "--no-chart"
)

Write-Host ">> US30 M5 CONTEXT (estructura / vigente vs agotando)..." -ForegroundColor Cyan
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_us30_m5 ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Cursor CONTEXT:" -ForegroundColor Green
Write-Host '  @live/us30_m5_context.md @docs/protocols/TRADING_LIVE_US30_CONTEXT.md' -ForegroundColor Yellow
Write-Host '  (consola basta — no requiere Cursor IA)' -ForegroundColor DarkGray
