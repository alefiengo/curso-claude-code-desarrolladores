# Referencia Rápida: Sesión 2

```text
/init       propuesta inicial de CLAUDE.md
/memory     memorias y auto-memory cargadas
/context    distribución de la ventana de contexto
/config     configuración de la sesión
```

## Contenido de una Buena Memoria

| Sí | No |
|---|---|
| Comandos canónicos | Árbol de carpetas |
| Convenciones no obvias | Dependencias copiadas de `pyproject.toml` |
| Riesgos recurrentes | Historia del proyecto |
| Límites de seguridad | Instrucciones de una sola tarea |
| Razones de decisiones | Datos temporales |

## Verificación de la Base

```bash
uv sync --frozen
uv run pytest -q
uv run ruff check .
docker compose config -q
git diff --check
```
