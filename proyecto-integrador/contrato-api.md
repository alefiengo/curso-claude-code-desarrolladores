# Contrato de la API del Curso

Este documento fija comportamiento observable. La estructura interna queda
abierta salvo las restricciones de seguridad, migración y verificación.

## Convenciones

- JSON UTF-8 y fechas ISO 8601.
- IDs enteros positivos generados por la base.
- `404` para recurso inexistente, `409` para conflicto y `422` para entrada inválida.
- Los códigos de las tablas siguientes son parte del contrato: son lo que
  afirman los tests, y lo que la sesión 10 compara al revisar. No los cambies
  sin cambiar antes este documento.
- Errores con forma estable: `{"detail": "<mensaje>"}`, donde el mensaje es una
  cadena legible. Para un `422` de validación se admite además la forma que
  genere tu framework, siempre que la clave de primer nivel siga siendo
  `detail`.
- Una referencia a proyecto o estado inexistente no se crea implícitamente.

### Normalización de texto

Se aplica a `title` de tarea y a `code` de estado, **antes** de validar y
guardar:

1. Se recorta el espacio de los extremos.
2. Se rechaza con `422` el valor que no deja **ningún carácter visible**. No
   basta con `strip()`: hay invisibles —como `U+200B`— que lo atraviesan. La
   comprobación es por categoría Unicode, rechazando `Cc`, `Cf`, `Zl`, `Zp`
   y `Zs`.
3. En `code` de estado, además, se pasa a mayúsculas.

La sesión 7 trabaja este defecto a fondo, con un título que parece válido y no
lo es.

### Orden de las listas

Toda colección devuelve un orden **estable entre llamadas idénticas**, para que
un test pueda comparar por posición:

| Endpoint | Orden |
|---|---|
| `GET /states` | Por el campo de orden del catálogo, y `id` como desempate |
| `GET /projects` | Por `id` ascendente |
| `GET /tasks` | Por `id` ascendente, también con filtros aplicados |

## Salud

### `GET /health`

Responde `200`:

```json
{"status": "ok"}
```

No expone credenciales ni detalles internos.

## Estados

Catálogo inicial: `PENDIENTE`, `EN_CURSO`, `BLOQUEADA`, `HECHA`.

| Método y ruta | Comportamiento |
|---|---|
| `GET /states` | `200` con lista ordenada y estable |
| `POST /states` | `201`; crea código normalizado y único, `409` si ya existe, `422` si queda vacío |
| `PATCH /states/{id}` | `200`; cambia **solo** `code`, con la misma normalización y unicidad que el alta. `404` si no existe, `409` si el código ya es de otro estado |
| `DELETE /states/{id}` | `204` si no está usado, `409` si lo está |

El seed debe ser idempotente y versionado mediante migración o mecanismo
equivalente comprobable.

## Proyectos

Campos mínimos: `id`, `name`, `description` opcional.

| Método y ruta | Comportamiento |
|---|---|
| `POST /projects` | `201` con el recurso creado |
| `GET /projects` | `200` con orden determinista |
| `GET /projects/{id}` | `200`, o `404` si no existe |
| `PATCH /projects/{id}` | `200` con actualización parcial |
| `DELETE /projects/{id}` | `204` si no tiene tareas, `409` si las tiene |

El curso adopta `409` al intentar borrar un proyecto con tareas; no hay borrado
en cascada implícito.

## Tareas v1

Campos: `id`, `title`, `description` opcional, `project_id`, `state_id`.

| Método y ruta | Comportamiento |
|---|---|
| `POST /tasks` | `201`; valida proyecto, estado y título |
| `GET /tasks` | `200`; admite `project_id` y `state_id`, solos o combinados |
| `GET /tasks/{id}` | `200`, o `404` si no existe |
| `PATCH /tasks/{id}` | `200` con actualización parcial consistente |
| `DELETE /tasks/{id}` | `204` sin cuerpo |

## Tareas v2: Fechas Límite

Se añade `due_at`, opcional, con zona horaria y normalizado a UTC. Omitirlo
conserva compatibilidad v1. Una fecha **sin** zona se rechaza con `422`: es
ambigua, y el contrato no supone ninguna por su cuenta.

`GET /tasks?overdue=true` devuelve tareas con `due_at` anterior al instante de
evaluación y estado distinto de `HECHA`. Una tarea sin fecha no está vencida.

Fuera de alcance: recordatorios, scheduler, zona preferida del usuario y cambio
automático de estado.

## Esquemas de Respuesta

Estos son los campos que devuelve cada recurso. **Ni más ni menos**: un campo de
sobra rompe a quien consuma la API igual que uno que falta.

```json
// Estado
{"id": 1, "code": "PENDIENTE"}

// Proyecto
{"id": 1, "name": "Casa", "description": null}

// Tarea (v2; en v1, sin due_at)
{
  "id": 1,
  "title": "Regar las plantas",
  "description": null,
  "project_id": 1,
  "state_id": 1,
  "due_at": "2026-03-01T09:00:00Z"
}
```

Tres detalles que deciden si dos implementaciones son intercambiables:

- Un campo opcional ausente se devuelve como `null`, no se omite.
- `due_at` se serializa **siempre en UTC y con `Z`**, no con desplazamiento
  (`+00:00`), y sin microsegundos: `2026-03-01T09:00:00Z`.
- `GET` de colección devuelve una lista JSON en la raíz, no un objeto envolvente
  con metadatos.

## Matriz Mínima de Tests

- Salud.
- CRUD feliz de cada recurso.
- IDs inexistentes.
- Título vacío y espacios ASCII; los invisibles Unicode se trabajan como regresión en la sesión 7.
- Proyecto/estado inexistente.
- Unicidad y conflicto de catálogo.
- Borrado de proyecto/estado referenciado.
- Filtros solos y combinados.
- Orden estable: dos llamadas idénticas devuelven los ids en la misma posición.
- Esquema de respuesta exacto: los campos declarados, ni uno más.
- `PATCH /states` con código duplicado (`409`) y con id inexistente (`404`).
- Migración desde base vacía y rollback de v2.
- `due_at` omitido, válido, sin zona, vencido, futuro y tarea hecha.

Los tests pueden incluir casos adicionales. No pueden debilitar estas invariantes.
