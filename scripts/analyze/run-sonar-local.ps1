#Requires -Version 5.1
<#
.SYNOPSIS
  Local Sonar analysis: pytest coverage + sonar-scanner against a local SonarQube.

.DESCRIPTION
  Defaults to http://localhost:9000 (SonarQube Community / Developer).
  For SonarCloud, pass -HostUrl https://sonarcloud.io and keep sonar.organization
  in sonar-project.properties.

  Prerequisites:
  - Java 17+ on PATH (required by SonarScanner CLI)
  - sonar-scanner or sonar-scanner.bat on PATH
    https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/
  - Local SonarQube running (or use Docker Compose: docker-compose.sonar.yml)
  - Token in $env:SONAR_TOKEN (SonarQube: My Account > Security > Generate Tokens)

.EXAMPLE
  $env:SONAR_TOKEN = "<token>"
  .\scripts\analyze\run-sonar-local.ps1

.EXAMPLE
  .\scripts\analyze\run-sonar-local.ps1 -SkipTests -HostUrl http://localhost:9000
#>
[CmdletBinding()]
param(
    [string]$HostUrl = $(if ($env:SONAR_HOST_URL) { $env:SONAR_HOST_URL } else { "http://localhost:9000" }),
    [switch]$SkipTests,
    [switch]$Cloud
)

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $RepoRoot

function Find-SonarScanner {
    $cmd = Get-Command sonar-scanner.bat -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    $cmd = Get-Command sonar-scanner -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    return $null
}

Write-Host "== Cursor Trading -- Sonar local ==" -ForegroundColor Cyan
Write-Host "Repo: $RepoRoot"
Write-Host "Host: $HostUrl"

# --- Token ---
$token = $env:SONAR_TOKEN
if ([string]::IsNullOrWhiteSpace($token)) {
    Write-Host ""
    Write-Host "SONAR_TOKEN no esta definido." -ForegroundColor Yellow
    Write-Host "  1) Abre SonarQube ($HostUrl) > My Account > Security > Generate Tokens"
    Write-Host "  2) En esta sesion de PowerShell:"
    Write-Host '       $env:SONAR_TOKEN = "<tu-token>"'
    Write-Host "  3) Vuelve a ejecutar este script."
    Write-Host ""
    Write-Host "Nunca commits el token al repo." -ForegroundColor Yellow
    exit 1
}

# --- Scanner ---
$scanner = Find-SonarScanner
if (-not $scanner) {
    Write-Host ""
    Write-Host "sonar-scanner no esta en PATH." -ForegroundColor Red
    Write-Host "Instala SonarScanner CLI y agrega su carpeta bin al PATH:"
    Write-Host "  https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/"
    Write-Host "  O con Chocolatey: choco install sonarqube-scanner.portable -y"
    Write-Host "Luego reinicia PowerShell y verifica:"
    Write-Host "  Get-Command sonar-scanner.bat"
    exit 1
}
Write-Host "Scanner: $scanner"

# --- Server reachability ---
try {
    $status = Invoke-RestMethod -Uri "$HostUrl/api/system/status" -TimeoutSec 8
    Write-Host "Server status: $($status.status)"
    if ($status.status -ne "UP") {
        Write-Host "SonarQube responde pero no esta UP (status=$($status.status))." -ForegroundColor Yellow
    }
}
catch {
    Write-Host ""
    Write-Host "No se pudo conectar a $HostUrl" -ForegroundColor Red
    Write-Host "Arranca SonarQube local (servicio Windows o Docker) y reintenta."
    Write-Host "Opcional Docker Compose (si Docker Desktop esta instalado):"
    Write-Host "  docker compose -f docker-compose.sonar.yml up -d"
    Write-Host "Ver docs\QUALITY.md seccion Local."
    exit 1
}

# --- Coverage ---
if (-not $SkipTests) {
    Write-Host ""
    Write-Host "-> pytest coverage..." -ForegroundColor Cyan
    if (Test-Path "requirements-dev.txt") {
        pip install -r requirements-dev.txt -q
    }
    else {
        pip install pytest pytest-cov -q
    }
    pytest tests/ --cov=app --cov-report=xml --cov-report=term-missing
    if ($LASTEXITCODE -ne 0) {
        Write-Host "pytest fallo (exit $LASTEXITCODE). Corrige tests antes de Sonar." -ForegroundColor Red
        exit $LASTEXITCODE
    }
    if (-not (Test-Path "coverage.xml")) {
        Write-Host "No se genero coverage.xml." -ForegroundColor Yellow
    }
}
else {
    Write-Host "SkipTests: se usa coverage.xml existente (si hay)." -ForegroundColor Yellow
}

# --- Scan ---
Write-Host ""
Write-Host "-> sonar-scanner..." -ForegroundColor Cyan

$scannerArgs = @(
    "-Dsonar.host.url=$HostUrl",
    "-Dsonar.token=$token"
)

# Local SonarQube ignores / rejects sonar.organization (SonarCloud-only).
# Override empty so local server analysis works without editing the properties file.
if (-not $Cloud -and $HostUrl -notmatch "sonarcloud\.io") {
    $scannerArgs += "-Dsonar.organization="
    Write-Host "Modo local: se omite sonar.organization (propiedad de SonarCloud)."
}

& $scanner @scannerArgs
$scanExit = $LASTEXITCODE
if ($scanExit -ne 0) {
    Write-Host "sonar-scanner fallo (exit $scanExit)." -ForegroundColor Red
    exit $scanExit
}

Write-Host ""
Write-Host "Analisis enviado. Revisa el proyecto en: $HostUrl" -ForegroundColor Green
Write-Host "Project key: flash-trading-signals (ver sonar-project.properties)"
