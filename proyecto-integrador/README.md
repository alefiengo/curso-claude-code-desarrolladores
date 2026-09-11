# Proyecto Integrador

El proyecto integrador es el hilo conductor del curso. **Construyes el tuyo** en tu propia máquina y en tu propio repositorio, `curso-claude-code-api`, a lo largo del curso.

Nace en la sesión 2 desde un repositorio mínimo que solo contiene el contrato y
la política de exclusión. Cada estudiante dirige a Claude para generar la base,
audita el plan y el diff, demuestra los criterios de aceptación y confirma su
propio resultado. Los laboratorios siguientes lo hacen crecer desde esa primera
base verificada.

## La Aplicación

API REST para gestión de tareas, con base de datos relacional. Un solo
servicio: el curso no añade capas nuevas después de cerrar su contrato.

El dominio es deliberadamente convencional. Lo que se practica es cómo trabajar
con el agente, no el diseño de la aplicación.

## Stack

| Componente | Tecnología |
|---|---|
| API | FastAPI, Python 3.12 |
| Base de datos | PostgreSQL 18 |
| Entorno y dependencias | uv |
| Tests | pytest |
| Formato y linter | ruff |
| Contenedores | Docker Compose |

## Modelo de Datos

Dos entidades relacionadas y un catálogo clasificador:

```text
proyectos ──< tareas >── estados
```

| Tabla | Contenido |
|---|---|
| `proyectos` | Agrupan tareas. CRUD completo |
| `tareas` | Título, descripción, proyecto y estado. CRUD con relaciones y filtros |
| `estados` | Catálogo fijo: `PENDIENTE`, `EN_CURSO`, `BLOQUEADA`, `HECHA`. Sin CRUD: llega por migración |

La relación da material para filtros y consultas. El catálogo obliga a validar
contra valores permitidos, y su carga plantea una decisión de ingeniería real:
dónde vive el seed para que exista en todos los entornos, no solo en el tuyo.

## Versiones

El proyecto crece en incrementos que se planifican, se prueban y se verifican por
separado:

| Sesión | Lo que se añade |
|---:|---|
| 2 | Esqueleto: FastAPI, Compose, `GET /health` y el `CLAUDE.md` del proyecto |
| 3 | El plan de persistencia, acordado y escrito antes de generar código |
| 4 | Persistencia, migración, catálogo de estados y `GET /states`; los permisos del proyecto versionados; el repositorio publicado |

De la sesión 5 a la 6 el proyecto completa el resto del contrato. Cada sesión
declara en su propia página qué añade y en qué estado deja el repositorio.

La API crece en rebanadas finas, una por sesión. Es deliberado: cada sesión
introduce **el mínimo de dominio que hace necesaria su herramienta**, y el resto
de los minutos son para Claude Code.

Al terminar la sesión 6, el contrato completo —salud, estados, proyectos y
tareas, con sus fechas límite— está implementado. Ninguna capacidad nueva se
añade después: las sesiones 7 a 10 trabajan sobre el sistema que rodea a la
API, no sobre su contrato.

## Arquitectura

Un solo servicio, de principio a fin del curso:

```text
  API :8000
    |
    +-- PostgreSQL :5432
```

### Alrededor del código

La aplicación no cambia, pero el instrumental del repositorio sí crece:

```text
repositorio
    |
    +-- .claude/
    |     +-- settings.json con los permisos del proyecto
    |     +-- lo que cada sesión añada: skills, hooks, subagentes
    |
    +-- verificación que se ejecuta sin nadie delante
```

## Cómo se avanza

Cada sesión deja el proyecto en un estado concreto, descrito en su validación.
Los labs son acumulativos, no independientes. Casi siempre ese estado está ya
integrado en `main`; cuando una sesión cierra con trabajo en una rama todavía sin
integrar, lo dice en su página.

Si faltas a una sesión, la ruta de recuperación son su laboratorio y el
[contrato de la API](contrato-api.md), que dice qué debe cumplir el resultado.

El [flujo de trabajo con Git](flujo-git.md) explica cómo se abre y se integra el
trabajo de cada sesión. El curso cierra con un
[cuestionario sobre Claude Code](../docs/evaluacion.md), no con una entrega de
este repositorio.
