# XAUUSD M5 CONTEXT — estructura / vigente vs agotando (sin Entry)
# Uso: .\scripts\analyze\analyze-xauusd-context.ps1
# NO es señal de entrada. Distinto de Light/High.

$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"
Set-Location (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

$argsList = @(
    "-m", "app.controllers.analyze_xauusd_m5",
    "--mode", "context",
    "--no-chart"
)

Write-Host ">> XAUUSD M5 CONTEXT (estructura / vigente vs agotando)..." -ForegroundColor Cyan
python @argsList
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: fallo python -m app.controllers.analyze_xauusd_m5 ($LASTEXITCODE)" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Salida CONTEXT:" -ForegroundColor Green
Write-Host "  live\xauusd_m5_context.md" -ForegroundColor Yellow
Write-Host "  (consola basta — no requiere Cursor IA)" -ForegroundColor DarkGray
