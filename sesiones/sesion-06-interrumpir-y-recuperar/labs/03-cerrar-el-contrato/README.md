# Lab 03: Cerrar el Contrato

## Objetivo

Comprobar el contrato completo —proyectos y tareas, v1 y v2— contra la API
corriendo, y publicar e integrar tareas v2.

## Por qué este lab

Tienes v2 implementada y corregida desde el Lab 02, pero sin publicar.
Cada endpoint por separado ya pasó su prueba en algún momento de estas dos
sesiones; hoy es la última vez que el contrato entero cabe en una sola
revisión antes de entregarlo. Compruébalo junto, no solo lo que acabas de
tocar, y ciérralo.

## Requisitos

- Lab 02 terminado: tareas v2 en verde, sin publicar.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–10 | El contrato completo —v1 y v2— comprobado contra la API corriendo |
| 10–15 | La rama publicada, con la descripción revisada |
| 15–25 | Integrada, `main` en verde, ninguna rama abierta |
| 25–30 | Estado final confirmado |

## Paso a Paso

### 1. Comprobar el contrato completo antes de publicar

```text
Contra la API corriendo, sin cambiar nada: haz un CRUD completo de un
proyecto y de una tarea con due_at que no hayas probado todavía hoy —crear,
leer, actualizar y borrar cada uno—, y GET /tasks?overdue=true con al menos
una tarea vencida entre las que crees. Muéstrame el código de estado de
cada respuesta.
```

Si algo no coincide con el contrato, corrígelo aquí, antes de publicar nada.

### 2. Entregar tareas v2

```text
Publica feature/tasks-v2, abre la solicitud de cambios hacia main con la
descripción de siempre —qué cambia, qué se decidió y por qué, cómo se
comprueba, qué queda sin probar—, y enséñamela antes de crearla.
```

En "qué queda sin probar", el contrato tiene una respuesta concreta: el
título de una tarea rechaza espacios vacíos comunes, pero no se comprobó
contra caracteres Unicode invisibles. Dilo así, sin adivinar si eso va a
importar.

Revisa el `/diff` completo antes de aprobarla.

### 3. Integrar

```text
Integra la solicitud de cambios, actualiza main en local, borra la rama
feature/tasks-v2 en local y en el remoto, y comprueba que la suite sigue
verde en main.
```

Con esto, el contrato completo de la API —proyectos y tareas, v1 y v2—
está en `main`.

### 4. Confirmar el estado final

```text
Sin cambiar nada, dime: los commits de main que no estaban al empezar la
sesión, si queda alguna rama sin integrar, y si el contrato completo —diez
endpoints entre proyectos y tareas v1 y v2— está implementado.
```

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Los commits de main que no estaban al empezar la sesión.
3. Si queda alguna rama sin integrar.
4. uv run pytest -q y uv run ruff check .
5. Si el contrato completo —diez endpoints entre proyectos y tareas v1 y
   v2— está implementado y probado.
```

El lab está completo si:

- [ ] Tareas v2 está integrada en `main`, y su descripción declara lo que queda sin probar.
- [ ] Comprobaste contra la API corriendo un CRUD de proyecto y uno de tarea que no habías probado todavía hoy.
- [ ] `GET /tasks?overdue=true` respondió lo esperado contra datos reales, no solo contra `pytest`.
- [ ] Ninguna rama queda abierta sin integrar.
- [ ] Sabes decir, sin adivinar, qué queda del contrato sin probar y por qué.

## Limpieza

```text
Detén los contenedores del proyecto sin eliminar volúmenes.
```

Antes de cerrar, `/context`: mira cuánto ocupó la sesión completa.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| Alguna respuesta del paso 1 no coincide con el contrato | El problema no es la comprobación: es la implementación. Corrígela antes de publicar, con el contrato delante |
| No tienes ninguna tarea vencida para probar `overdue=true` | Créala tú mismo con un `due_at` en el pasado, antes de la comprobación: es parte del paso, no un dato que deba existir de antes |
| La solicitud de cambios no menciona el defecto de Unicode | Pídeselo explícito: "qué queda sin probar" tiene una respuesta concreta hoy, no la dejes en blanco |
| No te alcanza el tiempo para todo el lab | Lo que no puede faltar es tareas v2 integrada en `main`. La comprobación completa del contrato se hace fuera de clase, antes de la sesión 7 |
