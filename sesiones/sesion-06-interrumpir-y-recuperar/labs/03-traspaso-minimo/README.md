# Lab 03: Traspaso Mínimo

## Objetivo

Cerrar tareas v2, y comprobar si tu repositorio le explica el proyecto a
alguien —o a ti mismo, dentro de tres semanas— sin que esa persona haya
estado en esta conversación.

## Por qué este lab

`/resume` te devuelve todo lo que dijiste e hiciste hoy, con cada comando de
por medio. Es potente, y solo sirve para una cosa: que seas tú, en esta
máquina, con esta conversación guardada. Nadie más tiene acceso a eso. Si
mañana te preguntan por qué el borrado de un proyecto responde `409`, o si
otra persona clona el repositorio para seguir el trabajo, lo único que tienen
es lo que dejaste escrito.

Hoy entregas lo último del contrato, y después le haces una pregunta incómoda
a tu propio repositorio: si nadie te lo cuenta, ¿se explica solo?

## Requisitos

- Lab 02 terminado: tareas v2 en verde, sin publicar.

## Ritmo de Trabajo

Este lab tiene 35 minutos:

| Min | Debe existir |
|---:|---|
| 0–8 | v2 entregada e integrada |
| 8–11 | La sesión de hoy, nombrada |
| 11–18 | Tu conversación retomada con su historial completo |
| 18–30 | El repositorio puesto a prueba sin contexto, y el hueco identificado |
| 30–35 | El hueco cerrado, con la edición mínima que hacía falta |

## Paso a Paso

### 1. Entregar tareas v2

```text
Publica feature/tasks-v2, abre la solicitud de cambios hacia main con la
descripción de siempre —qué cambia, qué se decidió y por qué, cómo se
comprueba, qué queda sin probar—, y enséñamela antes de crearla.
```

En "qué queda sin probar", el contrato tiene una respuesta concreta: el
título de una tarea rechaza espacios vacíos comunes, pero no se comprobó
contra caracteres Unicode invisibles. Dilo así, sin adivinar si eso va a
importar.

Revísala e intégrala. Con esto, el contrato completo de la API —proyectos y
tareas, v1 y v2— está en `main`.

### 2. Nombrar la sesión

```text
/rename tareas-v2
```

Es lo que te permite volver a esta conversación por su nombre, en vez de
buscarla en una lista.

### 3. Retomar como tú mismo

Sal de Claude Code con `/exit`. Vuelve a abrirlo, y retómala:

```bash
claude --resume tareas-v2
```

Fíjate en lo que acabas de recuperar: no un resumen, la conversación entera,
con cada herramienta que se ejecutó. `--continue` habría hecho lo mismo sin
pedirte que eligieras, porque solo tienes una sesión reciente en este
directorio.

Esto funcionó porque eres tú, en tu máquina, con el archivo de esta
conversación guardado en disco. Ninguna de esas tres cosas la tiene alguien
que solo clona tu repositorio.

### 4. Retomar como si no hubieras estado

Ahora la prueba real. Limpia el contexto de la conversación:

```text
/clear
```

Y pregúntale algo que un compañero nuevo preguntaría, sin darle ninguna pista
de lo que viviste hoy:

```text
Lee el repositorio —README, CLAUDE.md, docs/contrato-api.md, docs/ con los
planes, y los últimos quince commits— y dime: en qué estado está el proyecto,
qué decisiones importantes se tomaron y por qué, y qué le falta al contrato.
No me preguntes nada, respóndeme solo con lo que encuentres escrito.
```

Lee la respuesta completa y compárala con lo que tú sabes que pasó hoy y en
las sesiones anteriores. Busca una cosa concreta: algo que **tú** sabes y que
la respuesta no dice, o dice mal, porque no está escrito en ningún archivo del
repositorio.

Es probable que encuentres al menos una: por qué tareas v2 se implementó en
dos pasadas, por qué existe una migración vacía en el historial, o alguna
decisión que solo mencionaste en la conversación y nunca en un commit.

### 5. Cerrar el hueco

Con lo que encontraste, decide dónde corresponde escribirlo. No todo va al
mismo sitio:

| Si es… | Va en… |
|---|---|
| Una decisión de un cambio que todavía no confirmaste | El mensaje del commit que la toma |
| Una decisión de un cambio que ya integraste —como tareas v2, ahora mismo— | La descripción de esa solicitud de cambios: se puede editar aunque ya esté fusionada, sin reescribir ningún historial |
| Una convención que va a repetirse en el proyecto | `docs/decisiones-ingenieria.md` o `CLAUDE.md` |
| Contexto que explica por qué algo quedó como quedó | Una línea en el documento del plan correspondiente |

```text
[Describe con tus palabras el hueco que encontraste.] Añádelo en el lugar que
corresponda, en una frase, sin repetir lo que ya está escrito en otro sitio.
Enséñamelo antes de guardarlo.
```

Si el lugar que corresponde es un archivo del repositorio, confírmalo en su
propio commit. Si es la descripción de la solicitud de cambios ya fusionada,
edítala directamente: no hace falta ningún commit para eso.

## Validación

```text
Sin cambiar nada, dime:

1. Si el contrato completo de la API está implementado: proyectos, tareas v1
   y tareas v2.
2. Los commits de main que no estaban al empezar la sesión.
3. Si queda alguna rama sin integrar.
4. uv run pytest -q y uv run ruff check .
```

El lab está completo si:

- [ ] Tareas v2 está integrada en `main`, y su descripción declara lo que queda sin probar.
- [ ] La sesión tiene nombre, y la retomaste con él.
- [ ] Le pediste a una conversación sin contexto que describiera el proyecto.
- [ ] Encontraste al menos un hueco entre lo que tú sabes y lo que el repositorio dice —o comprobaste que no había ninguno, y sabes por qué.
- [ ] Si encontraste un hueco, lo cerraste en el lugar que le correspondía —un archivo, o la descripción de la solicitud de cambios—, no en cualquiera.

## Limpieza

```text
Detén los contenedores del proyecto sin eliminar volúmenes.
```

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| `claude --resume tareas-v2` no encuentra la sesión | El nombre se puso con `/rename` dentro de la conversación; si saliste antes de ese paso, vuelve a `/resume` sin nombre y elige de la lista |
| Después de `/clear`, Claude sí parece "recordar" algo de hoy | Puede estar leyéndolo del propio repositorio —commits, plan, contrato—, que es exactamente lo que este lab comprueba. No es memoria de la conversación |
| La respuesta sin contexto lo describe todo bien, sin huecos | Es un resultado válido: significa que tu historial y tu documentación ya cargan con el trabajo. Dilo en la validación y sigue |
| No sabes dónde va el hueco que encontraste | Vuelve a la tabla del paso 5. Si sigue sin encajar en ninguna fila, probablemente no era un hueco real: era algo que ya estaba escrito en otro sitio y no lo viste |
| Te da la tentación de escribir un documento nuevo solo para el traspaso | No lo hagas si una frase en un archivo que ya existe alcanza. Un documento nuevo que nadie mantiene es peor que no tenerlo |
