# Versionado (Git)

Este repo usa un archivo `VERSION` en la raíz y tags anotados de Git.

## Formato

- `VERSION` línea 1: `MAJOR.MINOR.PATCH` (semver)
- Tags: `vMAJOR.MINOR.PATCH` (ejemplo: `v1.1.0`)

## Cómo subir versión

1. Edita `VERSION` (línea 1) al nuevo número; actualiza fecha/nota en las líneas siguientes.
2. Commit de los cambios de código + `VERSION`.
3. Crea tag anotado:

```powershell
git tag -a v1.1.0 -m "Release v1.1.0"
```

4. (Opcional) Empuja commits y tags solo si hay remote y lo pedís:

```powershell
git push
git push --tags
```

## Qué no versionar

Ver `.gitignore`: parquet/CSV en `data/`, pesos `.pt` neural, charts `live/*.png`, historial `live/*_signal_history.json`, `__pycache__`, `.env`, `coverage.xml`, `.scannerwork/`.
Los `models/*.joblib` pequeños y `live/*.md` sí pueden ir al repo.

Prácticas de calidad / Sonar: [QUALITY.md](QUALITY.md).
