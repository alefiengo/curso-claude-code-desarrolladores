# Lab 01: Lo que la Especificación no Promete

## Objetivo

Exportar al repositorio la especificación OpenAPI que tu API ya genera,
confrontarla con el contrato escrito, y clasificar cada discrepancia según
cuál de los dos manda.

## Por qué este lab

Tu API genera su propia especificación desde el primer día, y nunca la has
mirado. Mientras tanto, `docs/contrato-api.md` lleva seis sesiones siendo la
fuente de verdad: es lo que afirman los tests y lo que comparas cuando algo
responde raro.

Hoy los pones uno al lado del otro. Vas a encontrar tres clases de
diferencia, y solo una es un defecto: hay cosas que el contrato promete y la
especificación **no puede** expresar, hay cosas donde el contrato ya cedió a
propósito, y puede haber alguna donde uno de los dos simplemente está mal.
Confundirlas es lo que hace que la gente tire un documento creyendo que el
otro lo reemplaza.

## Requisitos

- Sesión 7 completa: `main` en verde, con el contrato completo demostrado por
  `api.http`, las tres reglas en `.claude/rules/` y `segmentar-commits` ya
  diagnosticada.
- La base de datos levantada.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | Rama nueva y el punto de partida confirmado |
| 5–13 | `openapi.json` exportado, confirmado, y el comando que lo genera escrito en el `README.md` |
| 13–25 | La confrontación contra el contrato, con cada diferencia clasificada |
| 25–30 | La decisión registrada donde corresponde, y confirmada |

**Si necesitas cortar aquí:** lo mínimo es `openapi.json` exportado y su
comando escrito. La confrontación se termina después, pero el Lab 03 la
necesita hecha.

## Paso a Paso

### 1. Confirmar el punto de partida

```text
Crea la rama feature/descripcion desde main, y confírmame que main está
actualizado, el árbol de trabajo está limpio, y la base de datos está
levantada y con las migraciones aplicadas.
```

### 2. Exportar la especificación

No asumas por qué ruta se sirve ni cómo se genera: pídelo.

```text
Esta API genera su especificación OpenAPI sola. Dime dónde la expone y de
qué forma se puede obtener sin levantar el servidor ni tocar la base de
datos. Después expórtala a openapi.json en la raíz del repositorio, al lado
de api.http, y escribe en el README.md la línea que la regenera.
```

Que quede escrito en el `README.md` no es un adorno: el Lab 03 va a
comparar contra ese mismo comando, y una comprobación que solo tú sabes
ejecutar no sirve de guardarraíl.

Revisa el `/diff` y confirma el archivo y la línea del `README.md` en un solo
commit.

### 3. Confrontar contra el contrato

```text
Compara openapi.json con docs/contrato-api.md, entero. Lista cada diferencia
que encuentres y clasifícala en uno de estos tres grupos, diciendo en qué
línea de cada documento la ves:

1. El contrato promete algo que la especificación no puede expresar.
2. El contrato cede a propósito ante lo que genera el framework.
3. Uno de los dos está mal y hay que corregirlo.

No corrijas nada todavía. Solo la lista.
```

Si empieza a corregir en vez de comparar, `Esc`: hoy la lista es el trabajo.

Lo que tiene que haber ocurrido: el grupo 1 no sale vacío. El caso limpio es
el **orden estable entre llamadas idénticas**: una especificación describe la
forma de una respuesta, y no tiene dónde decir que dos llamadas seguidas
devuelven los elementos en el mismo sitio.

El formato de `due_at` es más interesante, y conviene mirarlo despacio: una
especificación **sí** puede restringir la forma de la cadena, así que el
"UTC con `Z`, sin microsegundos" es expresable. Lo que no puede es
garantizar que la implementación lo cumpla —una especificación describe, no
ejecuta—. Si Claude te lo señala, tiene razón: anótalo en el grupo 1 con ese
matiz, o en el grupo 3 si resulta que la especificación de tu proyecto no lo
restringe y podría.

El grupo 2 tampoco: el contrato ya admite, para un `422` de validación, la
forma que genere tu framework, siempre que la clave de primer nivel siga
siendo `detail`.

El grupo 3 es el único que puede salir vacío, y es el único que obliga a
hacer algo.

### 4. Decidir y registrar

Para cada diferencia del grupo 3, decide **cuál de los dos documentos está
mal** antes de tocar ninguno: si el código hace lo correcto y el contrato
está desactualizado, se corrige el contrato; si el contrato tiene razón, se
corrige el código y la especificación se regenera sola.

```text
[Di qué decidiste para cada diferencia del grupo 3, y por qué.] Aplícalo:
corrige lo que decidí y regenera openapi.json si el cambio lo afecta. Si no
hubo ninguna diferencia del grupo 3, dilo y no toques nada.
```

Confirma en su propio commit. Si no hubo nada del grupo 3, no hay commit que
hacer aquí: es un resultado válido.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Si openapi.json está confirmado, y si el README.md incluye la línea que
   lo regenera.
3. Regenera la especificación en un archivo temporal y compárala con
   openapi.json: ¿son idénticos?
4. uv run pytest -q y uv run ruff check .
5. Cuántas diferencias quedaron en cada uno de los tres grupos.
```

El lab está completo si:

- [ ] `openapi.json` está en la raíz, confirmado, y regenerarlo no produce diferencias.
- [ ] El `README.md` dice con qué comando se regenera.
- [ ] Sabes nombrar al menos una cosa que el contrato promete y la especificación no puede expresar.
- [ ] Sabes nombrar la diferencia que el contrato acepta a propósito.
- [ ] Si hubo alguna diferencia del grupo 3, decidiste cuál documento estaba mal antes de corregir, y quedó registrado.

## Limpieza

Ninguna. El Lab 02 trabaja sobre este mismo estado, sin publicar todavía.
Antes de seguir, `/context`: la especificación completa de una API ocupa más
de lo que parece, y conviene que veas cuánto.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| Propone obtener la especificación levantando el servidor y llamando a una ruta | Funciona, pero pídele la forma que no necesita el servidor: el Lab 03 va a ejecutar esta comprobación antes de cada commit, y arrancar la API para eso es caro |
| La comparación devuelve treinta diferencias de formato | Casi todas serán ruido de orden de claves o de indentación. Pídele que compare por contenido y que agrupe: lo que importa son las tres categorías, no la cantidad |
| Dice que el contrato y la especificación coinciden en todo | Vuelve a pedirlo señalando dos sitios concretos: el orden estable de las colecciones y el formato exacto de `due_at`. Si sigue diciendo que coinciden, está comparando forma contra forma y le falta leer las garantías del contrato |
| Regenerar la especificación produce diferencias cada vez, sin que cambies nada | Hay algo no determinista en la generación —un orden que depende del arranque—. Anótalo: es exactamente lo que va a hacer inútil el hook del Lab 03 si no se resuelve antes |
| Necesitas cortar el lab | Lo mínimo es `openapi.json` exportado y su comando escrito en el `README.md`. La confrontación se termina después |
