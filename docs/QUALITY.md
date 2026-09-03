# Calidad, Git y SonarQube



Buenas prácticas del repo **flash-trading-signals** (Cursor Trading).



## Flujo Git



- Rama principal: `main`. Features en ramas cortas (`feature/...`, `fix/...`).

- Antes de push: correr al menos `pytest tests/test_high_signal_rules.py`.

- No subir secretos (`.env`, tokens, claves). Usar `.env.example` si hace falta plantilla.

- No versionar salidas regenerables: `live/*.png`, `live/*_signal_history.json`, CSV/parquet en `data/`, venv, coverage, `.scannerwork/`.



## Señales vs history-review



| Runner | Escribe historial | Propone entrada nueva |

|--------|-------------------|------------------------|

| `analyze-*-high.ps1` | Sí (append) | Sí (señal High) |

| `analyze-*-history.ps1` | No | No — solo P&L de la última Entry |



History-review **no** es señal de entrada.



## Tests y coverage



```powershell

cd "D:\Danilo\Trading\Cursor Trading"

pip install -r requirements-dev.txt

pytest tests/test_high_signal_rules.py

# Con coverage (genera coverage.xml para Sonar):

pytest tests/ --cov=app --cov-report=xml --cov-report=term-missing

```



Config en `pyproject.toml`. `coverage.xml` y `.scannerwork/` están en `.gitignore`.



## Sonar — análisis local (Windows PowerShell)



Objetivo: correr SonarScanner contra un **SonarQube local** (`http://localhost:9000`), no solo CI/SonarCloud.



### Requisitos



1. **Java 17+** en PATH (el scanner lo necesita). Verificar: `java -version`

2. **SonarScanner CLI** en PATH (`sonar-scanner.bat` en Windows):

   - Descarga: [SonarScanner CLI](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/)

   - O con Chocolatey: `choco install sonarqube-scanner.portable -y` (luego reinicia PowerShell)

   - Verificar: `Get-Command sonar-scanner.bat`

3. **SonarQube** escuchando en `http://localhost:9000` (servicio Windows o Docker)

4. **Token** en la sesión (nunca en el repo):

   ```powershell

   $env:SONAR_TOKEN = "<token-generado-en-SonarQube>"

   # Opcional:

   $env:SONAR_HOST_URL = "http://localhost:9000"

   ```



### Camino rápido (script)



```powershell

cd "D:\Danilo\Trading\Cursor Trading"

$env:SONAR_TOKEN = "<tu-token>"

.\scripts\analyze\run-sonar-local.ps1

```



El script:



1. Genera coverage con pytest (`coverage.xml`)

2. Comprueba que el host responda

3. Ejecuta `sonar-scanner` con `-Dsonar.host.url=...` y el token

4. En hosts locales **omite** `sonar.organization` (propiedad solo de SonarCloud)



Flags útiles:



```powershell

.\scripts\analyze\run-sonar-local.ps1 -SkipTests          # usa coverage.xml ya generado

.\scripts\analyze\run-sonar-local.ps1 -HostUrl http://localhost:9000

.\scripts\analyze\run-sonar-local.ps1 -Cloud              # no limpia organization (SonarCloud)

```



### Manual (sin script)



```powershell

cd "D:\Danilo\Trading\Cursor Trading"

pip install -r requirements-dev.txt

pytest tests/ --cov=app --cov-report=xml

sonar-scanner.bat `

  -Dsonar.host.url=http://localhost:9000 `

  -Dsonar.token=$env:SONAR_TOKEN `

  -Dsonar.organization=

```



Proyecto: clave `flash-trading-signals` (ver `sonar-project.properties`). Créalo en la UI de SonarQube si aún no existe.



### SonarQube con Docker (opcional)



Solo si tienes **Docker Desktop**. En esta máquina a veces no está instalado; no es obligatorio.



```powershell

docker compose -f docker-compose.sonar.yml up -d

# Esperar 1–2 min → http://localhost:9000 (admin/admin la primera vez)

# Crear proyecto + token → $env:SONAR_TOKEN = "..."

.\scripts\analyze\run-sonar-local.ps1

```



Parar: `docker compose -f docker-compose.sonar.yml down`



## SonarCloud (remoto / CI)



El job de GitHub Actions **falla de forma explícita** si falta `SONAR_TOKEN`. Pytest puede pasar y aun así el workflow falla en el paso Sonar hasta que configures el secreto.



### Pasos obligatorios (una sola vez)



1. En [SonarCloud](https://sonarcloud.io): inicia sesión con GitHub y **crea / importa** el proyecto del repo `minichaverra-beep/flash-trading-signals`.

2. Comprueba en la UI de SonarCloud (Project Information) que coincidan con `sonar-project.properties`:

   - Organization key: `minichaverra-beep`

   - Project key: `flash-trading-signals`

   Si SonarCloud te asignó otra key (p. ej. `minichaverra-beep_flash-trading-signals`), actualiza `sonar.projectKey` en el repo para que coincida.

3. Genera un token: SonarCloud → **My Account → Security → Generate Tokens** (tipo Analysis o Global Analysis).

4. Añade el secreto en GitHub (esto no se puede hacer desde el código):

   - Repo → **Settings → Secrets and variables → Actions → New repository secret**

   - Name: `SONAR_TOKEN`

   - Value: el token de SonarCloud

5. Vuelve a lanzar el workflow **SonarCloud** (push a `main`/`master` o **Actions → SonarCloud → Run workflow**).



**Sin `SONAR_TOKEN` el scan no puede autenticarse** (antes: action deprecada + exit code 3 / aviso de token ausente).



### Análisis local hacia la nube



```powershell

pytest tests/ --cov=app --cov-report=xml

$env:SONAR_TOKEN = "<token-sonarcloud>"

sonar-scanner.bat -Dsonar.host.url=https://sonarcloud.io -Dsonar.token=$env:SONAR_TOKEN

# o: .\scripts\analyze\run-sonar-local.ps1 -Cloud -HostUrl https://sonarcloud.io

```



### CI



Workflow: `.github/workflows/sonarcloud.yml` usa `SonarSource/sonarqube-scan-action` con `SONAR_HOST_URL=https://sonarcloud.io` y el secreto `SONAR_TOKEN`.



### IDE (SonarLint Connected Mode)



Tras crear el proyecto, `.sonarlint/connectedMode.json`:



```json

{

  "sonarCloudOrganization": "minichaverra-beep",

  "projectKey": "flash-trading-signals"

}

```



Hasta que el proyecto exista en SonarCloud / SonarQube y el token esté en Actions, MCP / SonarLint no tendrán issues ni quality gate que consultar.


