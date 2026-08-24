# Proyecto Integrador

El proyecto integrador es el hilo conductor del curso. **Cada estudiante construye el suyo** en su propia máquina y en su propio repositorio, `curso-claude-code-api`, a lo largo de las diez sesiones.

No se descarga hecho. Nace en la sesión 2 y crece con los laboratorios de cada sesión.

## La Aplicación

API REST para gestión de tareas, con base de datos relacional y una página estática mínima para probarla desde el navegador.

El dominio es deliberadamente convencional. Lo que se practica es cómo trabajar con el agente, no el diseño de la aplicación.

## Stack

| Componente | Tecnología |
|---|---|
| API | FastAPI, Python 3.12 |
| Base de datos | PostgreSQL 18 |
| Entorno y dependencias | uv |
| Tests | pytest |
| Formato y linter | ruff |
| Contenedores | Docker Compose |
| Página estática | HTML + JavaScript servidos por FastAPI |

## Modelo de Datos

Dos entidades relacionadas y un catálogo clasificador:

```text
proyectos ──< tareas >── estados
```

| Tabla | Contenido |
|---|---|
| `proyectos` | Agrupan tareas |
| `tareas` | Título, descripción, proyecto y estado |
| `estados` | Catálogo: `PENDIENTE`, `EN_CURSO`, `BLOQUEADA`, `HECHA` |

La relación da material para filtros y consultas. El catálogo obliga a validar contra valores permitidos.

## Versiones

El proyecto tiene tres versiones, una por bloque:

| Versión | Cierre | Lo que incluye |
|---|---|---|
| `v1` | Sesión 3 | API FastAPI con PostgreSQL en Compose, CRUD completo de las tres tablas, primeros tests y `CLAUDE.md` del proyecto |
| `v2` | Sesión 6 | Feature planificada y entregada por pull request, con historial limpio y sesiones recuperables |
| `v3` | Sesión 10 | `.claude/` completo: skill de verificación, hooks, `settings.json`, subagente revisor, evaluación MCP y workflow de CI acotado |

## Arquitectura

### Bloques 1 y 2 (v1 y v2)

```text
navegador
    |
página estática (servida por FastAPI)
    |
  API :8000
    |
    +-- PostgreSQL :5432
```

### Bloque 3 (v3)

La aplicación no cambia. Lo que crece es el instrumental alrededor:

```text
repositorio
    |
    +-- .claude/
    |     +-- skills invocables
    |     +-- skill de endpoints
    |     +-- subagente revisor
    |     +-- hooks y settings.json
    |
    +-- integración MCP aprobada, si el entorno lo permite
    +-- GitHub Action de revisión
```

## Cómo se avanza

Cada sesión deja el proyecto en un estado concreto, descrito en su validación.
Los labs son acumulativos, no independientes. Si faltas, el contrato, el lab
correspondiente y el último checkpoint válido forman la ruta de recuperación.

Usa el [contrato de la API](contrato-api.md) como fuente funcional y los
[checkpoints](checkpoints.md) para diagnosticar o recuperar una sesión. El curso
cierra con el [proyecto final](proyecto-final.md).
