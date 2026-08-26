# Proyecto Integrador

El proyecto integrador es el hilo conductor del curso. **Construyes el tuyo** en tu propia máquina y en tu propio repositorio, `curso-claude-code-api`, a lo largo del curso.

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
| 3 | Esquema, migraciones y el catálogo de estados |
| 4 | Proyectos: CRUD completo con sus tests |
| 5 | Tareas: relaciones, filtros y orden estable |
| 6 | v1 cerrada, con verificación automática |
| 7 | Datos reales, comprobados contra la base |
| 8 | Una regresión corregida y protegida |
| 9 | El cambio revisado por un tercero |
| 10 | Entregado, automatizado y podado |

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
    |     +-- skills invocables, uno con script propio
    |     +-- hooks: lint automático y puerta de cierre
    |     +-- settings.json con permisos mínimos
    |     +-- subagente revisor de solo lectura
    |
    +-- .mcp.json: consulta a la base desde el agente
    +-- GitHub Action que verifica sin nadie delante
```

## Cómo se avanza

Cada sesión deja el proyecto en un estado concreto, descrito en su validación, e
integrado en `main`. Los labs son acumulativos, no independientes.

Si faltas a una sesión, la ruta de recuperación son su laboratorio y el
[contrato de la API](contrato-api.md), que dice qué debe cumplir el resultado.
Trabajas sobre `main`, que siempre está en verde.

El [flujo de trabajo con Git](flujo-git.md) explica cómo se abre y se integra el
trabajo de cada sesión. El curso cierra con el
[proyecto final](proyecto-final.md).
