# Lab 02: Configurar el Directorio `.claude`

## Objetivo

Convertir los permisos que acabas de aprobar de uno en uno en reglas escritas,
versionadas y comprobables.

## Por qué este lab

Acabas de terminar el Lab 01 con una lista de todo lo que Claude ejecutó. Cada
línea de esa lista es una interrupción que tuviste: una pregunta a la que
respondiste que sí, casi siempre sin leerla, porque leerla veinte veces cuesta
más que el riesgo de no leer una.

Ese es el problema de fondo. No es la molestia: es que aprobar por inercia
convierte tu autorización en un trámite, y el día que aparezca algo que sí
importaba, lo vas a aprobar igual.

La respuesta no es aprobar más rápido. Es decidir **una sola vez**, por escrito,
qué puede hacer Claude en este proyecto sin preguntar, qué te tiene que
preguntar siempre y qué no puede hacer aunque tú se lo pidas.

## Requisitos

- Lab 01 terminado, con sus commits en `feature/persistencia`.
- La lista de comandos que Claude ejecutó, a la vista.

Si limpiaste la conversación y perdiste la lista, recupérala con `/resume`:
abre el selector de conversaciones de este directorio y vuelve a la del Lab 01.

## Ritmo de Trabajo

Este lab tiene 22 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | La lista repartida en tres grupos: lo que se permite, lo que se pregunta y lo que se prohíbe |
| 5–12 | `.claude/settings.json` escrito, con las tres listas |
| 12–17 | `/permissions` reconoce el archivo, y el bloqueo comprobado con un caso real |
| 17–22 | El cambio revisado y confirmado en la rama |

## Paso a Paso

### 1. Repartir la lista en tres grupos

Antes de escribir nada, decide. Mira tu lista del Lab 01 y reparte cada comando
en uno de estos tres grupos:

| Grupo | Criterio | Ejemplos de tu lista |
|---|---|---|
| Permitir | Lo repetiste muchas veces, es reversible y no sale de tu máquina | La suite, el linter, las migraciones, `git status`, `git diff` |
| Preguntar | Es normal hacerlo, pero tiene consecuencias fuera de tu equipo | Publicar en un remoto |
| Prohibir | No quieres que ocurra nunca en este proyecto, ni por error ni porque tú lo pidas en un mal momento | Leer el archivo de secretos, borrar el volumen de datos |

Fíjate en el tercer grupo: no es "lo que Claude no debe hacer", es **lo que no
debe poder hacer aunque se lo pidas tú**. Ahí está la diferencia entre una
instrucción y una regla.

Si quieres ayuda para clasificar, pídesela, pero la decisión es tuya:

```text
Tengo la lista de comandos que ejecutaste. Para cada uno dime, en una línea, si
es reversible, si afecta solo a mi máquina y si podría destruir datos. No
propongas configuración todavía.
```

### 2. Escribir las reglas

Ahora sí:

```text
Crea .claude/settings.json con un bloque de permisos con tres listas.

En allow: los comandos del proyecto que repetí durante el lab anterior —el
gestor de dependencias, los tests, el linter, las migraciones, y los comandos de
git que solo leen o confirman en local—. Escríbelos con el patrón de prefijo,
por ejemplo Bash(uv run pytest *), poniendo el asterisco después del subcomando.

En ask: publicar en un remoto.

En deny: leer .env, y borrar el volumen de datos con docker compose down cuando
lleva -v o --volumes.

Enséñame el archivo antes de guardarlo y explícame en una línea por qué cada
regla está en la lista en la que está.
```

Cuando te lo enseñe, comprueba una cosa concreta antes de guardarlo: que el
borrado del volumen esté cubierto en **sus dos formas**, la corta y la larga. Una
regla que solo contempla una de las dos deja la otra abierta, y esta es de las
que no vas a poder probar.

Dos cosas más que conviene que sepas antes de leer lo que te enseñe:

- **El orden de evaluación es `deny`, después `ask`, después `allow`.** Gana la
  primera que coincida. Una regla `deny` amplia bloquea aunque exista un `allow`
  más específico, así que una lista de prohibiciones no admite excepciones.
- **El asterisco va después del subcomando.** `Bash(git commit *)` permite solo
  `git commit`; `Bash(git *)` permite cualquier comando de git, borrados
  incluidos. Escrito al revés —`Bash(git * main)`— la regla se vuelve mucho más
  ancha de lo que parece.

Si al leerlo ves que el archivo quedó demasiado permisivo, no lo parchees encima:
`/rewind` —o `Esc Esc`, que abre el mismo selector— deshace el turno y su edición,
y vuelves a pedirlo con el límite claro. Los commits del Lab 01 no se tocan.

### 3. Comprobar que las reglas mandan

Que el archivo exista no significa que esté activo. Compruébalo:

```text
/permissions
```

Deben aparecer tus reglas, y el archivo del proyecto como su origen. Si no
aparecen, mira los **Problemas Frecuentes**.

Ahora una prueba de verdad. Pídele algo que tu propia regla prohíbe:

```text
Lee el archivo .env con tu herramienta de lectura de archivos y enséñame su
contenido. No uses comandos de shell para esto.
```

Debe negarse, y debe negarse **por la regla**, no por buena voluntad. Es la
diferencia que decidiste en el paso 1: en la sesión 2 escribiste "no toques
`.env`" en tus instrucciones y eso era una petición; esto es otra cosa.

El encargo nombra la herramienta a propósito. Tu regla protege las herramientas
de archivo, y un comando de shell que imprima el archivo llega por otro camino
que ninguna lista de comandos prohibidos cubre entera: siempre queda otro
programa capaz de leerlo. Anótalo, porque es el mismo límite que vas a
encontrarte con el volumen.

**La regla del volumen no la vamos a probar.** Comprobar que bloquea significa
pedir el borrado, y si la regla estuviera mal escrita, perderías el trabajo del
Lab 01. Anótalo como lo que es: una regla que solo puedes verificar leyéndola,
y que cubre las formas habituales del comando, no todas las que existen. Cuando
necesites una garantía que no dependa de haber previsto la variante correcta,
hace falta otro mecanismo; el curso llega a él más adelante.

### 4. Revisar y confirmar

Revisa con `/diff` y confirma:

```text
Confirma .claude/settings.json en un solo commit. Usa Conventional Commits,
empieza por chore: y propón tú el mensaje. Enséñamelo antes de confirmar.
```

Esto no es persistencia, y sin embargo va en la rama `feature/persistencia`
junto al resto. Es deliberado: quien revise este cambio debería ver **con qué
permisos se hizo**, no encontrárselos sueltos tres semanas más tarde. Por eso
lleva su propio commit y su propio prefijo, para que en el diff se distinga sin
esfuerzo qué es código y qué es configuración.

## Validación

```text
Sin cambiar nada, dime:

1. El contenido de .claude/settings.json.
2. Si está versionado o sigue sin añadirse.
3. Los commits de esta rama que no están en main, uno por línea.
4. Si el árbol de trabajo está limpio.
```

El lab está completo si:

- [ ] `.claude/settings.json` existe, está versionado y tiene las tres listas.
- [ ] Cada regla de `allow` corresponde a algo que de verdad repetiste en el Lab 01.
- [ ] Publicar en un remoto está en `ask`, no en `allow`.
- [ ] `/permissions` muestra tus reglas y reconoce el archivo del proyecto como origen.
- [ ] Pedirle que lea `.env` con su herramienta de archivos se rechaza.
- [ ] La regla del volumen cubre las dos formas del borrado, la corta y la larga, y lo comprobaste leyéndola.
- [ ] El commit es propio, no mezclado con ningún incremento de persistencia.
- [ ] Sabes decir qué regla de las tuyas no puedes comprobar sin arriesgarte a romper algo.

## Limpieza

Ninguna. El Lab 03 trabaja sobre este mismo estado, y va a poner a prueba lo que
acabas de escribir.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| `/permissions` no muestra tus reglas | La sesión puede haber cargado la configuración al arrancar, antes de que el archivo existiera. Sal con `/exit`, vuelve a abrir Claude Code y comprueba otra vez |
| Claude te lee `.env` igualmente | Mira **cómo** lo leyó. Si usó un comando de shell, la regla no aplica y es el límite que describe el paso 3. Si usó su herramienta de lectura, entonces la regla no está activa o apunta a otra ruta: compruébala en `/permissions` |
| El archivo quedó con `Bash(git *)` o similar | Es una regla mucho más ancha de lo que parece: incluye borrar ramas y publicar. `/rewind` y vuelve a pedirlo nombrando los subcomandos uno a uno |
| Te sigue preguntando por comandos que pusiste en `allow` | Compara el patrón con el comando exacto que ejecuta. `Bash(pytest *)` no cubre `uv run pytest`, porque el programa es `uv` |
| No encuentras la lista del Lab 01 | `/resume` y vuelve a esa conversación. Si tampoco está, pídele que lea el plan y enumere qué comandos exige cada incremento |
| Dudas de si una regla debería ser `ask` o `deny` | Si algún día vas a querer hacerlo, es `ask`. `deny` es para lo que no quieres poder hacer ni pidiéndolo |
