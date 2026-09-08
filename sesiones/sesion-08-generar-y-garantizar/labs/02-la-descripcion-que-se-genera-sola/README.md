# Lab 02: La Descripción que se Genera Sola

## Objetivo

Construir una skill que produzca el diagrama y el diccionario de datos desde
los modelos y las migraciones, estrenarla, y corregir el archivo de la skill
—no su resultado— si lo que devuelve no sirve.

## Por qué este lab

La especificación del Lab 01 describe la API por fuera: rutas, códigos y
formas de respuesta. No dice nada de la base de datos: qué tablas hay, qué
columna admite nulos, qué clave apunta a dónde, ni qué significa el catálogo
de estados. Eso hoy solo se sabe leyendo las migraciones en orden.

Y es información que envejece cada vez que alguien añade una columna, así que
no la vas a escribir a mano: la escribe un procedimiento que puedes volver a
invocar. La skill que ya tienes para repartir commits te enseñó cómo se
construye una; esta reutiliza ese mismo molde para un trabajo distinto.

## Requisitos

- Lab 01 terminado: `openapi.json` exportado y confirmado en
  `feature/descripcion`, sin publicar.
- `.claude/skills/` con las skills que ya construiste.

## Ritmo de Trabajo

Este lab tiene 25 minutos:

| Min | Debe existir |
|---:|---|
| 0–4 | Decidido qué tiene que contener la descripción, con el contrato delante |
| 4–13 | La skill escrita, revisada antes de guardarse y confirmada |
| 13–19 | `docs/esquema.md` generado por la skill |
| 19–25 | La skill corregida si hizo falta, y el resultado confirmado |

**Si necesitas cortar aquí:** lo mínimo es la skill escrita y confirmada.
Estrenarla y generar `docs/esquema.md` se puede terminar después.

## Paso a Paso

### 1. Decidir qué tiene que contener

Antes de pedir nada, mira contra qué se va a comparar:

```text
Lee docs/contrato-api.md y las migraciones de alembic/versions/. Dime qué
información sobre la base de datos no está escrita en ninguno de los dos y
solo se deduce leyendo las migraciones en orden.
```

Quédate con esa lista: es lo que la descripción tiene que cubrir. Lo que ya
está en el contrato **no** se repite.

### 2. Escribir la skill

```text
Crea una skill de proyecto llamada describir-esquema. Enséñame el archivo
antes de guardarlo.

Que el procedimiento haga esto:

- Empiece por el estado real de los modelos y de alembic/versions/ en el
  momento de invocarla, no por lo que se supone que hay.
- Produzca un solo archivo, docs/esquema.md, con dos partes: un diagrama de
  las tablas y sus relaciones, y un diccionario de datos con una fila por
  columna —nombre, tipo, si admite nulos, y qué significa cuando no es
  evidente—.
- Escriba el diagrama en un formato de texto que se pueda versionar y
  diferenciar en un commit, y que se renderice en el repositorio.
- No repita lo que ya dice docs/contrato-api.md: si algo está ahí, lo enlaza
  en vez de copiarlo.

Y un límite: la skill describe, no modifica. No toca modelos, migraciones,
el contrato ni la base de datos.

Dime también qué inyectas del estado del repositorio para que arranque, y por
qué eso y no el contenido completo de cada archivo.
```

Antes de guardarla, comprueba dos cosas en el archivo que te enseñó: que el
límite esté escrito, y que no repita lo que ya dice tu `CLAUDE.md`. Una skill
que copia el `CLAUDE.md` gasta contexto dos veces.

Confírmala en su propio commit `chore:`.

### 3. Estrenarla

```text
/skills
```

Compruébalo en la lista, y después invócala:

```text
/describir-esquema
```

Revisa el `/diff` de `docs/esquema.md` con dos preguntas concretas: ¿el
diagrama se entiende sin leer el diccionario?, ¿el diccionario tiene una fila
por cada columna que existe de verdad, incluidas las que añadió la última
migración?

### 4. Corregir la skill, no el resultado

Si lo que devolvió no sirve —le falta una tabla, el diagrama es ilegible, el
diccionario repite el contrato—, el problema no es este `docs/esquema.md`:

```text
[Di qué le falta o qué sobra.] Corrige el archivo de la skill para que la
próxima invocación ya salga así, y vuelve a invocarla sobre el estado actual.
```

Una skill se estrena mal casi siempre. Corregirla ahora, con un resultado
real delante, cuesta menos que adivinarlo antes de usarla.

Cuando `docs/esquema.md` te convenza, confírmalo. Si la skill cambió,
confírmala aparte: son dos intenciones distintas.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué skills de proyecto hay en .claude/skills/ y en qué commit entró cada
   una.
3. Si el archivo de describir-esquema declara su límite, y cuál es.
4. Cuántas tablas y cuántas columnas describe docs/esquema.md, y si coinciden
   con las que crean las migraciones de alembic/versions/.
5. Si docs/esquema.md repite algo que ya está en docs/contrato-api.md.
```

El lab está completo si:

- [ ] `describir-esquema` está versionada y declara por escrito que describe y no modifica.
- [ ] La invocaste y produjo `docs/esquema.md` con diagrama y diccionario.
- [ ] El diccionario cubre todas las columnas que crean las migraciones, sin inventar ninguna.
- [ ] El diagrama está en texto versionable, no en una imagen.
- [ ] Si la corregiste, cambiaste el archivo de la skill y no solo su resultado, y quedó en su propio commit.

## Limpieza

Ninguna. El Lab 03 necesita `openapi.json` y `docs/esquema.md` tal como
quedaron aquí.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| La skill devuelve el diagrama como una imagen o un enlace a un servicio | Recházalo: una imagen no se puede diferenciar en un commit ni revisar en una solicitud de cambios. Pídele texto que el repositorio renderice |
| El diccionario copia entero el contrato | Es el fallo que el límite tenía que evitar. Corrige el archivo de la skill para que enlace `docs/contrato-api.md` en vez de repetirlo |
| Faltan las columnas de la última migración | La skill está leyendo los modelos y no las migraciones, o al revés. Pídele que lea las dos fuentes y que diga cuál usó para cada fila |
| `/skills` no la ve | `.claude/skills/` ya existía al arrancar la sesión, así que debería aparecer sin recargar nada. Si no, `/reload-skills`, y si sigue sin salir, sal con `/exit` y vuelve a abrir |
| Necesitas cortar el lab | Lo mínimo es la skill escrita y confirmada. Estrenarla se termina después, pero el Lab 04 la va a necesitar funcionando |
