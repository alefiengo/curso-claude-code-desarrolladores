# Lab 03: Lo que Cualquiera Puede Probar

## Objetivo

Comprobar si tu repositorio le explica el proyecto a alguien que no vivió
esta conversación, y dejar dos artefactos que prueban que el contrato
completo funciona: una colección de peticiones ejecutable, y un README que
lleva de cero a la API corriendo.

## Por qué este lab

`/resume` te devuelve tu conversación entera, con cada herramienta que se
ejecutó. Eso solo sirve si eres tú, en tu máquina, con esa conversación
guardada. Alguien que clona tu repositorio no tiene nada de eso: solo lo que
dejaste escrito en commits, contrato y configuración. Hoy lo compruebas de
verdad: le pides a una conversación sin memoria que describa el proyecto
solo con lo que hay escrito, y comparas su respuesta con lo que tú sabes. Si
algo que tú sabes no aparece ahí, o aparece mal, es un **hueco**:
información real que hasta hoy solo vivía en tu cabeza, no en el
repositorio.

Y cada comprobación que hiciste contra la API corriendo, desde la sesión 2,
vivió igual de encerrada en una conversación: la escribiste, la corriste, la
leíste, y se perdió con el contexto. Un test de `pytest` prueba que el
código hace lo que el propio test decidió probar; no le sirve a quien abre
el repositorio por primera vez y quiere verlo funcionando sin escribirte a
ti antes.

Hoy dejas lo que sí sobrevive: un README que un desconocido puede seguir
solo, una colección de peticiones que cualquiera puede ejecutar, y la
certeza de que la migración completa del proyecto sube y baja sin error.

## Requisitos

- Lab 02 terminado: `main` en verde con la corrección del Lab 01 y las reglas
  del Lab 02, integradas.

## Ritmo de Trabajo

Este lab tiene 50 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | Rama nueva |
| 5–15 | La sesión nombrada, y retomada como tú mismo con `--resume` |
| 15–25 | Retomada sin contexto con `/clear`, y un hueco real encontrado |
| 25–30 | El hueco cerrado en el lugar que le corresponde |
| 30–40 | `api.http` construido y ejecutado contra la API real, con el ciclo completo de la migración |
| 40–45 | `README.md` reescrito y probado con `/clear` |
| 45–50 | Entrega e integración |

## Paso a Paso

### 1. Confirmar el punto de partida

```text
Crea la rama feature/verificacion-completa desde main, y confírmame que main
está actualizado, el árbol de trabajo está limpio, y la base de datos está
levantada y con las migraciones aplicadas.
```

### 2. Nombrar la sesión y retomarla como tú mismo

```text
/rename sesion-7-verificacion
```

Sal de Claude Code con `/exit`. Vuelve a abrirlo, y retómala:

```bash
claude --resume sesion-7-verificacion
```

Fíjate en lo que acabas de recuperar: no un resumen, la conversación entera,
con cada herramienta que se ejecutó. Esto funcionó porque eres tú, en tu
máquina, con el archivo de esta conversación guardado en disco. Ninguna de
esas tres cosas la tiene alguien que solo clona tu repositorio.

### 3. Retomar como si no hubieras estado

Ahora la prueba real. Limpia el contexto de la conversación:

```text
/clear
```

Y pregúntale algo que un compañero nuevo preguntaría, sin darle ninguna
pista de lo que viviste en las sesiones 6 y 7:

```text
Lee el repositorio —README, CLAUDE.md, docs/contrato-api.md, docs/ con los
planes, .claude/rules/ y los últimos quince commits— y dime: en qué estado
está el proyecto, qué decisiones importantes se tomaron y por qué, y qué le
falta al contrato. No me preguntes nada, respóndeme solo con lo que
encuentres escrito.
```

Lee la respuesta completa y compárala con lo que tú sabes que pasó. Busca
una cosa concreta: algo que **tú** sabes y que la respuesta no dice, o dice
mal, porque no está escrito en ningún archivo del repositorio.

Es probable que encuentres al menos una: por qué tareas v2 se implementó en
dos pasadas, por qué la primera migración de Alembic del historial no
cambia nada de esquema, o alguna decisión que solo mencionaste en la
conversación y nunca en un commit.

### 4. Cerrar el hueco

Con lo que encontraste, decide dónde corresponde escribirlo. No todo va al
mismo sitio:

| Si es… | Va en… |
|---|---|
| Una decisión de un cambio que todavía no confirmaste | El mensaje del commit que la toma |
| Una decisión de un cambio que ya integraste | La descripción de esa solicitud de cambios: se puede editar aunque ya esté fusionada, sin reescribir ningún historial |
| Una convención que va a repetirse en el proyecto | `.claude/rules/` o `CLAUDE.md`, según si aplica siempre o solo a un tipo de archivo |
| Contexto que explica por qué algo quedó como quedó | Una línea en el documento del plan correspondiente |

```text
[Describe con tus palabras el hueco que encontraste.] Añádelo en el lugar
que corresponda, en una frase, sin repetir lo que ya está escrito en otro
sitio. Enséñamelo antes de guardarlo.
```

Si el lugar que corresponde es un archivo del repositorio, confírmalo en su
propio commit. Si es la descripción de una solicitud de cambios ya
fusionada, edítala directamente: no hace falta ningún commit para eso.

### 5. Construir la colección de peticiones

```text
Lee docs/contrato-api.md completo. Crea api.http en la raíz del repositorio,
con una petición por cada método y ruta del contrato —salud, estados,
proyectos y tareas, v1 y v2—, en un orden en el que cada petición pueda
apoyarse en el resultado de la anterior: primero crea lo que las siguientes
necesitan. Incluye al menos un caso de error por recurso: un id inexistente,
una validación que falla, el 409 de borrar un proyecto con tareas. Usa el
formato de bloques separados por ###, con el método, la ruta, los headers y
el cuerpo cuando corresponda.
```

Entre los casos de error, incluye el que declaraste sin probar en la
sesión 6: una tarea con `title` igual a un único carácter `U+200B` —espacio
de ancho cero, invisible pero real—. El contrato dice que debe responder
`422`; hasta hoy nunca se comprobó.

Revisa el archivo antes de seguir: cuéntalo contra la lista de endpoints del
contrato, y confirma que el caso de `U+200B` quedó incluido. Si falta algo,
dile qué y que lo agregue.

### 6. Ejecutarla contra la API real, con el ciclo completo de la migración

```text
Levanta la API si no está corriendo. Ejecuta cada petición de api.http en
orden, con curl, y para cada una dime el método, la ruta, el código de
estado que devolvió, y si coincide con lo que dice el contrato. No me
resumas el resultado: quiero cada petición, una por una, en el mismo orden
en que aparece en el archivo.

Después: uv run alembic downgrade base, y luego uv run alembic upgrade head.
Confírmame que las dos direcciones terminan sin error, y que alembic current
vuelve a coincidir con el archivo más reciente del repositorio.
```

Esto no es `pytest`: es la API real, respondiendo a las mismas peticiones
que dejaste escritas, y la migración completa del proyecto bajando y
subiendo de nuevo. Si algo no coincide con el contrato, el problema no es la
comprobación: es la implementación o la migración. Presta especial atención
a la petición con `U+200B`: si responde `201` en vez de `422`, corrige la
validación de `title` para que rechace el valor si, tras recortar los
extremos, no queda ningún carácter fuera de las categorías Unicode `Cc`,
`Cf`, `Zl`, `Zp` o `Zs`. Corrige lo que falle, repite esa petición, y sigue
con las que quedan.

### 7. Reescribir el README

```text
Lee el README.md actual del proyecto. Reescríbelo para que alguien que clona
el repositorio hoy, sin haber hablado contigo, pueda: instalar las
dependencias, levantar la base de datos, aplicar las migraciones, arrancar
la API, y probar un endpoint con api.http. Un paso por línea, en el orden en
que se ejecutan. No copies la lista de endpoints del contrato: enlaza a
docs/contrato-api.md y a api.http para eso.
```

### 8. Probarlo sin ti delante

```text
/clear
```

```text
Acabas de clonar este repositorio y no sabes nada de él. Sigue el README.md
paso a paso, sin saltarte ninguno, y dime en cuál te quedaste atascado o qué
información te faltó. No mires ningún otro archivo del repositorio todavía.
```

Lo que tiene que haber ocurrido: llegó hasta el final, o se detuvo en un
paso concreto que puedes señalar. Si se detuvo, el hueco está ahí: corrígelo
en el README, no en la respuesta que te acaba de dar. Repite este paso desde
`/clear` hasta que llegue al final sin atascarse.

### 9. Entregar e integrar

Revisa el `/diff` completo del lab antes de seguir. Después:

```text
Publica feature/verificacion-completa, abre la solicitud de cambios hacia
main con la descripción de siempre —qué cambia, qué se decidió y por qué,
cómo se comprueba, qué queda sin probar—, y enséñamela antes de crearla.
```

Revísala e intégrala.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Cuántas peticiones tiene api.http y cuántos endpoints tiene el contrato:
   si no coinciden, cuáles faltan.
3. uv run alembic current, y si coincide con el archivo más reciente de
   alembic/versions/.
4. uv run pytest -q y uv run ruff check .
5. Los commits de main que no estaban al empezar el Lab 01, uno por línea.
```

El lab está completo si:

- [ ] Le pediste a una conversación sin tu contexto que describiera el proyecto, y comparaste su respuesta con lo que tú sabes.
- [ ] Encontraste al menos un hueco y lo cerraste en el lugar que le correspondía —o comprobaste que no había ninguno, y sabes por qué.
- [ ] `api.http` tiene una petición por cada endpoint del contrato, incluyendo al menos un caso de error por recurso.
- [ ] `api.http` incluye el título con `U+200B`, y responde `422` contra la API corriendo: el defecto que la sesión 6 dejó declarado y sin probar queda cerrado.
- [ ] Cada petición de `api.http` se ejecutó contra la API real, y el código de estado coincide con el contrato.
- [ ] La migración completa bajó con `downgrade base` y volvió a subir con `upgrade head`, sin error.
- [ ] El `README.md` nuevo lleva de cero a la API corriendo, un paso por línea, probado con `/clear`.
- [ ] `main` integra el hueco cerrado, `api.http` y el README nuevo.

## Limpieza

```text
Detén los contenedores del proyecto sin eliminar volúmenes.
```

Antes de cerrar, `/context`: mira cuánto ocupó reconstruir un README
completo y una colección de peticiones frente a lo que ocupó cada
comprobación suelta de las sesiones anteriores.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| `claude --resume sesion-7-verificacion` no encuentra la sesión | El nombre se puso con `/rename` dentro de la conversación; si saliste antes de ese paso, vuelve a `/resume` sin nombre y elige de la lista |
| La respuesta sin contexto del paso 3 lo describe todo bien, sin huecos | Es un resultado válido: significa que tu historial y tu documentación ya cargan con el trabajo. Dilo en la validación y sigue |
| No sabes dónde va el hueco que encontraste | Vuelve a la tabla del paso 4. Si sigue sin encajar en ninguna fila, probablemente no era un hueco real |
| `api.http` no cubre todos los endpoints | Vuelve al contrato y cuenta: son doce entre salud, estados, proyectos y tareas v1 y v2 |
| No sabes cómo escribir un carácter `U+200B` en `api.http` | Pídeselo a Claude por el nombre del carácter o el código Unicode, no lo copies y pegues de otro sitio: un editor puede normalizarlo sin que lo notes |
| El título con `U+200B` responde `201` en vez de `422` | Es el defecto que la sesión 6 dejó declarado y sin probar. Revisa si la validación de `title` cubre las cinco categorías —`Cc`, `Cf`, `Zl`, `Zp`, `Zs`— o solo espacios ASCII |
| Una petición de `api.http` falla contra la API real, pero `pytest` está en verde | Es información real, no un error del lab: `pytest` solo prueba lo que el test decidió probar. Corrige la implementación contra el contrato |
| `alembic downgrade base` falla a mitad de camino | Revisa cuál migración falla y en qué sentido: una migración que sube limpio pero no baja limpio es un defecto real, no del lab |
| El README probado con `/clear` se atasca en un paso | Anota exactamente cuál, corrígelo, y repite el paso 8 desde cero |
| Necesitas cortar el lab | Lo mínimo es `api.http` ejecutado contra la API real y el ciclo de migración probado. El traspaso y el README se terminan después |
