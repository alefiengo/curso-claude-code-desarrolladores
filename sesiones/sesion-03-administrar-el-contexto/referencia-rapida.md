# Referencia Rápida: Sesión 3

## Decidir Qué Hacer con el Contexto

| Situación | Acción |
|---|---|
| La misma tarea sigue clara y lo cargado es pertinente | Continuar |
| Pregunta sobre algo que la conversación ya conoce | `/btw <pregunta>` |
| Misma tarea, historia útil mezclada con salidas repetidas | `/compact <foco>` |
| Tarea o función nueva; necesitas dejar atrás los supuestos anteriores | `/clear [nombre]` |
| Una fuente concreta es necesaria para el turno | `@ruta` |

`/context all` muestra composición y capacidad. No mide corrección ni define un
porcentaje universal para compactar.

## Antes de Compactar

Conserva fuera de la conversación:

```bash
git status --short
git log --oneline main..HEAD
uv run pytest -q
uv run ruff check .
```

El foco de `/compact` debería nombrar:

- objetivo y fuentes;
- rama y estado;
- límites protegidos;
- verificaciones y resultados;
- decisión pendiente y riesgo residual.

Después comprueba el resumen contra Git o los archivos.

## Qué Sobrevive a `/compact`

| Contenido | Después |
|---|---|
| `CLAUDE.md` de la raíz y reglas sin `paths:` | Se reinyecta desde disco |
| Memoria automática | Se reinyecta desde disco |
| Archivos leídos o editados | Se releen hasta cinco, los modificados más recientemente |
| Reglas con `paths:` y `CLAUDE.md` anidados | Se recargan al volver a leer un archivo que los activa |
| Todo lo demás | Se resume |

Un archivo grande vuelve como referencia de ruta, sin contenido. Y una decisión
que solo dijiste en la conversación es justo lo que el resumen puede perder: si
está en un archivo o en un commit, sobrevive.

## Límites Importantes

| Mecanismo | Límite |
|---|---|
| `/btw` | Ve la conversación, pero no puede leer archivos ni ejecutar herramientas; no añade su intercambio al historial principal |
| `/compact` | Sustituye el historial por un resumen y puede perder detalle |
| `/clear [nombre]` | Abre contexto vacío y deja la conversación anterior fuera, disponible para retomarla después |
| `@archivo` | Incluye el contenido completo del archivo en la conversación |
| `@directorio/` | Incluye un listado, no todo el contenido de sus archivos |

## Verificar la Persistencia

```bash
uv lock --check
docker compose up -d --wait db
uv run alembic upgrade head
uv run pytest -q
uv run ruff check .
docker compose config -q
git diff --check main...HEAD
git diff --stat main...HEAD
```

## Integrar sin Tags

```bash
git switch main
git merge --no-ff feature/persistencia -m "Integra la capa de persistencia"
uv run pytest -q
git branch -d feature/persistencia
git status --short
```
