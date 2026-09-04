# Lab 02: El Encargo Ancho

## Objetivo

Dar un encargo demasiado amplio para tareas v2, reconocer qué hizo de más,
corregirlo hacia adelante, y comprobar con un caso controlado qué es
exactamente lo que `/rewind` no revierte.

## Por qué este lab

Tienes un plan escrito para v2 desde el Lab 01. Hoy lo vas a ignorar a
propósito, con un encargo grande y sin pasar por él, porque es lo que ocurre
de verdad cuando hay prisa: el plan existe, y aun así se pide todo de una vez
"para no perder tiempo". Vas a ver qué cuesta eso, y vas a comprobar algo que
no se nota hasta que lo necesitas: `/rewind` deshace turnos y archivos, no lo
que un comando le hizo a tu base de datos.

## Requisitos

- Lab 01 terminado: `main` con proyectos y tareas v1, el plan de v2 escrito en
  `docs/`.
- La base de datos levantada, con las migraciones de v1 aplicadas.

## Ritmo de Trabajo

Este lab tiene 45 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | Rama nueva y la revisión actual de Alembic anotada |
| 5–15 | v2 implementada de un encargo ancho, sin plan |
| 15–20 | El diff revisado, con lo que sobra identificado |
| 20–30 | Lo que sobra corregido hacia adelante, v2 en verde |
| 30–40 | El límite de `/rewind` comprobado con una migración desechable |
| 40–45 | Comparación de los dos caminos |

**Si no te alcanza el tiempo:** lo que no puede faltar es v2 corregida y en
verde. La comprobación del límite de `/rewind` con la migración desechable se
puede hacer fuera de clase; no arriesga nada tuyo si la dejas pendiente.

## Paso a Paso

### 1. Confirmar el punto de partida

```text
Crea la rama feature/tasks-v2 desde main, y dime la revisión actual de Alembic
con alembic current.
```

Anota esa revisión. La vas a comparar más adelante.

### 2. Dar el encargo ancho

No le pidas el plan. Dale algo que suena razonable bajo presión:

```text
Implementa las fechas límite de las tareas: due_at y el filtro overdue. Hazlo
completo, con migración y todo. No hace falta que sigas el plan paso a paso,
ve directo y arréglalo todo lo que necesites para que quede bien.
```

Deja que trabaje sin interrumpir, salvo que veas algo que claramente no tiene
que ver con fechas límite.

### 3. Revisar qué hizo

```text
/diff
```

No hay un desvío único que debas encontrar: depende de la ejecución, y
cualquiera de estos es un resultado válido para seguir. Recórrelo con estas
preguntas:

| Pregunta | Qué buscas |
|---|---|
| ¿Tocó algo de proyectos? | Un archivo, un esquema o una ruta que no tiene que ver con tareas |
| ¿Modificó un test de v1 que ya estaba en verde? | Cambiar un test existente para que un cambio nuevo pase es debilitarlo, no corregirlo |
| ¿Cambió el esquema de salida de otro recurso? | Un campo añadido o quitado en `states` o `projects` que el contrato no pidió |
| ¿El commit que propondría mezclaría dos intenciones? | Fechas límite y "una mejora" que nadie pidió, en el mismo cambio |

Si no encuentras nada fuera de sitio, dilo: también es un resultado válido, y
el lab sigue igual desde el paso 5.

### 4. Corregir hacia adelante

Con lo que encontraste delante, pide exactamente lo que sobra:

```text
[Nombra el archivo o el cambio concreto que sobra, con lo que viste en el
diff.] Quítalo, y deja el resto de fechas límite tal como está. No toques
nada más.
```

Corrígelo, no repitas el encargo entero. Cuando el diff quede limpio, ejecuta
la suite y comprueba `GET /tasks?overdue=true` contra la API corriendo.
Confírmalo, pero **no lo publiques todavía**: el Lab 03 cierra la entrega.

### 5. Probar el límite de `/rewind`

Esto es un experimento aparte, y no toca el trabajo de v2 que acabas de dejar
en verde. Pide una migración que no cambia nada:

```text
Crea una revisión de Alembic vacía, sin ningún cambio de esquema —igual que la
revisión inicial que ya tienes en el historial del proyecto—, y aplícala. Dime
la revisión anterior y la nueva revisión, con sus identificadores completos.
```

Anota los dos identificadores. Ahora rebobina: `Esc Esc` con el campo de texto
vacío, y elige el punto justo antes de ese encargo. Cuando te ofrezca las
opciones de restaurar, elige la que restaura código **y** conversación.

Sin pedirle que arregle nada:

```text
Ejecuta uv run alembic current y dime exactamente qué responde.
```

Lo que tiene que haber ocurrido: el archivo de la migración vacía ya no está
—lo borró el rebobinado—, pero la base de datos sigue marcada con esa
revisión. Alembic no puede resolverla contra los archivos que tiene delante:
te lo dice con un error, o con un identificador que no reconoces en tu
historial. Cualquiera de los dos confirma lo mismo: la conversación volvió
atrás, la base de datos no.

### 6. Recuperar sin arriesgar nada

La migración era vacía, así que la base de datos no tiene ningún cambio de
esquema pendiente de deshacer. Marca la tabla de control con la revisión
correcta, sin ejecutar nada:

```text
Ejecuta uv run alembic stamp [pega aquí el identificador que anotaste antes de
la migración vacía]. Después confirma con alembic current que coincide con el
archivo más reciente del repositorio.
```

Esto funciona porque la migración no cambiaba nada de verdad. Si hubiera sido
una migración real —como la que añadió `due_at`—, marcar la tabla no habría
bastado: la columna seguiría ahí, sin ningún archivo que la explique. Por eso
el paso 5 se hizo con una migración vacía, y por eso corregiste v2 hacia
adelante en el paso 4, en vez de rebobinarla.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. uv run alembic current, y si coincide con el archivo de migración más
   reciente del repositorio.
3. uv run pytest -q y uv run ruff check .
4. Crea, contra la API corriendo, una tarea sin due_at, una con due_at en el
   pasado y estado distinto de HECHA, y una con due_at en el pasado pero
   estado HECHA. Enséñame el cuerpo completo de cada respuesta.
5. GET /tasks?overdue=true con esas tres tareas creadas: dime cuáles devuelve.
6. En cualquiera de esas respuestas, el valor exacto de due_at tal como lo
   serializa la API.
7. Si el diff de esta rama toca algo fuera de tareas.
```

Del punto 5, lo que tiene que haber ocurrido: solo aparece la tarea vencida y
sin `HECHA`. La que no tiene fecha, y la que está vencida pero ya terminada,
quedan fuera las dos. Del punto 6: `due_at` sale en UTC, con `Z` al final, sin
desplazamiento y sin microsegundos —es el único formato que el contrato acepta
como válido.

El lab está completo si:

- [ ] Diste el encargo ancho sin pasar por el plan del Lab 01.
- [ ] Revisaste el diff con las cuatro preguntas, y anotaste el resultado, cualquiera que fuera.
- [ ] v2 está en verde, sin nada fuera del alcance de fechas límite.
- [ ] `GET /tasks?overdue=true` excluye la tarea sin fecha y la tarea vencida pero `HECHA`.
- [ ] `due_at` se serializa en UTC con `Z`, sin desplazamiento y sin microsegundos.
- [ ] Provocaste el desajuste entre el archivo de una migración y el estado de la base de datos, y lo viste con tus propios ojos.
- [ ] `alembic current` coincide otra vez con el archivo más reciente del repositorio.
- [ ] Sabes decir, sin mirar la referencia rápida, qué revierte `/rewind` y qué no.

## Limpieza

Ninguna. El Lab 03 entrega e integra lo que dejaste aquí.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El desvío del paso 3 es tan grande que corregirlo se siente como reescribir todo | No lo corrijas ni lo rebobines: descarta la rama y vuelve a `feature/tasks-v2` desde `main`, con el encargo del paso 2 pero más acotado. Empezar limpio es la tercera opción, y a veces es la más barata |
| El encargo ancho no produjo ningún desvío | Es un resultado válido. Sigue al paso 5 con lo que tienes: v2 ya está en verde |
| No encuentras el punto exacto en el selector de `/rewind` | El selector lista tus mensajes, no los de Claude. Busca el que diste en el paso 5, el de la migración vacía |
| `alembic current` no muestra ningún error tras el rebobinado | Puede que el rebobinado no haya llegado a borrar el archivo de la migración. Comprueba con `git status` si el archivo sigue en `alembic/versions/` |
| `alembic stamp` no encuentra la revisión que le diste | Revisa que copiaste el identificador **anterior** a la migración vacía, no el nuevo |
| Te preocupa haber roto algo de verdad | No: la migración era vacía, sin cambios de esquema. El único desajuste posible es de bookkeeping, y `stamp` lo corrige sin tocar ningún dato |
| Quieres probar esto con una migración que sí cambia el esquema | Es el desafío opcional de esta sesión. No lo hagas aquí: sin una migración vacía de por medio, la recuperación no es tan simple |
