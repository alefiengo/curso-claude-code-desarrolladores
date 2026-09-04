# Lab 01: Cerrar y Planificar

## Objetivo

Cerrar la comprobación que la sesión anterior dejó pendiente, planificar el
contrato completo de tareas con la skill que ya construiste, e implementar la
primera mitad.

## Por qué este lab

Tu repositorio tiene una skill de planificación que solo has usado una vez.
Hoy la vuelves a invocar, sobre un contrato distinto, sin cambiarle una línea.
Si funciona igual de bien la segunda vez, es una herramienta de verdad; si
tienes que reescribirla para que sirva, era un script de un solo uso con
forma de skill.

Antes de planificar nada, hay una comprobación de la sesión 5 que quedó
declarada y sin probar: el `409` al borrar un proyecto con tareas. No podía
comprobarse porque las tareas no existían. Hoy sí existen, así que la cierras
primero, en cuanto tengas con qué.

## Requisitos

- Sesión 5 completa: `main` en verde con persistencia, proyectos, y
  `.claude/skills/` con `planificar-incremento` y `segmentar-commits`.
- La base de datos levantada.
- `docs/contrato-api.md` a mano, secciones **Tareas v1** y **Tareas v2**.

Si no terminaste los laboratorios 03 y 04 de la sesión 5, complétalos antes de
seguir: son autosuficientes, y este lab da por hecho ese resultado —proyectos
implementado y las dos skills confirmadas.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | Rama nueva y el estado del repositorio confirmado |
| 5–13 | El plan de tareas —v1 y v2— escrito, revisado y confirmado |
| 13–25 | Tareas v1 implementada y en verde |
| 25–30 | El `409` cerrado, y v1 entregada e integrada |

**Si no te alcanza el tiempo:** lo que no puede faltar es el plan confirmado y
`tasks` v1 en verde, aunque el `409` y la entrega se terminen fuera de clase.

## Paso a Paso

### 1. Confirmar el punto de partida

```text
Crea la rama feature/tasks desde main, y confírmame que main está actualizado,
el árbol de trabajo está limpio, y la base de datos está levantada y con las
migraciones aplicadas.
```

### 2. Planificar el contrato completo de tareas

Invoca tu skill sobre las dos secciones a la vez, para no repetir el paso de
planificación cuando llegues a las fechas límite:

```text
/planificar-incremento las tareas del contrato, v1 y v2 completas, según las
secciones Tareas v1 y Tareas v2 de docs/contrato-api.md
```

Revísalo con las mismas cuatro preguntas de la sesión pasada: ¿los incrementos
se pueden ejecutar en orden?, ¿cada uno declara su comprobación?, ¿queda
alguna decisión en condicional?, ¿el alcance es el del contrato y nada más?

Confírmalo en su propio commit, con `docs:` y Conventional Commits.

### 3. Implementar tareas v1

Aprueba solo el primer incremento —v1— y déjalo trabajar:

```text
Implementa el primer incremento del plan, el de tareas v1. Ejecuta las
comprobaciones que declara. No hagas commit de nada: quiero revisar el
conjunto antes.
```

Cuando termine, revisa el `/diff`. Confirma en uno o varios commits, según lo
que veas: si el incremento es una sola intención, un commit basta; si mezcla
más de una, usa tu skill de reparto.

### 4. Cerrar el `409` que quedó pendiente

Ahora que tareas v1 existe, cierra la comprobación declarada sin probar en la
sesión pasada:

```text
Escribe el test que faltaba: crea un proyecto, crea una tarea sobre ese
proyecto, e intenta borrar el proyecto. Tiene que responder 409. Después
ejecútalo y muéstrame el resultado.
```

Si falla, el problema no es el test: es que el incremento anterior no
implementó bien la comprobación. Corrígelo ahí, no aquí.

### 5. Entregar e integrar v1

```text
Publica la rama, abre la solicitud de cambios hacia main con la descripción de
siempre —qué cambia, qué se decidió y por qué, cómo se comprueba, qué queda
sin probar—, y enséñamela antes de crearla.
```

Revísala e intégrala. `main` queda con proyectos y tareas v1 completos; v2
—las fechas límite— es el trabajo del Lab 02.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. El contenido de docs/, y si el plan cubre v1 y v2.
3. uv run pytest -q y uv run ruff check .
4. La respuesta de un DELETE sobre un proyecto con tareas.
5. GET /tasks contra la API corriendo, dos veces seguidas, con al menos tres
   tareas creadas: ¿los ids salen en la misma posición las dos veces?
6. GET /tasks/{id} con un id que no existe. Muestra el código de estado.
7. Los commits de main que no estaban antes de hoy.
```

El lab está completo si:

- [ ] El plan cubre tareas v1 y v2, con incrementos numerados y sin decisiones en condicional.
- [ ] `POST /tasks`, `GET /tasks` con filtros, `GET /tasks/{id}`, `PATCH` y `DELETE` responden lo que dice el contrato.
- [ ] Dos llamadas idénticas a `GET /tasks` devuelven los ids en la misma posición.
- [ ] `GET /tasks/{id}` con un id inexistente responde `404`.
- [ ] El test del `409` existe, crea una tarea real, y pasa.
- [ ] `main` tiene tareas v1 integrada desde una solicitud de cambios.
- [ ] Sabes qué queda para el Lab 02: tareas v2, fechas límite.

## Limpieza

Ninguna. El Lab 02 trabaja sobre este mismo estado.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| No tienes las dos skills de la sesión 5 | No se pueden reconstruir aquí: son el resultado de esa sesión completa. Vuelve a ella antes de seguir |
| La skill deja alguna decisión aplazada | Es su límite funcionando: dile qué opción adoptar, con el contrato delante, y que la escriba como decisión tomada |
| El `409` sigue fallando después de escribir el test | Revisa si el incremento de v1 implementó la comprobación contra tareas reales, o solo devolvía `409` sin consultar nada |
| El plan mezcla v1 y v2 en un solo incremento | Pídele que los separe: son dos incrementos, con su propia comprobación cada uno |
| No te alcanza el tiempo para entregar v1 | Confirma el trabajo revisado y termina la entrega fuera de clase. El Lab 02 puede empezar igual, sobre la rama sin integrar |
