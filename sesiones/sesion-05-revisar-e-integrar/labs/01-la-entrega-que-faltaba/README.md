# Lab 01: La Entrega que Faltaba

## Objetivo

Comprobar la API como la ve quien la consume, entregar la rama de la sesión
anterior en una solicitud de cambios que otra persona pueda revisar, e
integrarla dejando `main` en verde.

## Por qué este lab

Tu rama está publicada desde la sesión pasada y ahí sigue: nadie la ha mirado y
nadie puede mirarla, porque una rama publicada no pide nada. La solicitud de
cambios es lo que convierte tu trabajo en algo que otra persona puede aprobar o
rechazar.

Antes de entregarla vas a comprobar una cosa que hasta ahora no comprobaste
nunca. Toda la verificación del curso ha ocurrido dentro de las pruebas, con la
aplicación en memoria y sin servidor. Hoy levantas la API y le haces una
petición de verdad. Puede que responda a la primera; puede que no, y el motivo
te va a decir algo sobre la diferencia entre "las pruebas pasan" y "el servicio
funciona".

Al terminar, la rama estará integrada y borrada. A partir de ahí, una rama
abierta en tu repositorio significa trabajo en curso, y nada más.

## Requisitos

- Sesión 4 completada, con `feature/persistencia` publicada en tu remoto.
- Docker Engine o Docker Desktop arrancado.
- La CLI de tu proveedor instalada y autenticada: `gh` para GitHub, `glab` para
  GitLab. Es el desafío de la sesión 4. Si no la tienes, ve a los **Problemas
  Frecuentes** antes de empezar.
- Claude Code abierto en `~/curso-claude/curso-claude-code-api`.

Si te falta el estado de la sesión 4 —no tienes la rama, o no llegaste a
publicarla—, ve a los **Problemas Frecuentes**: se recupera, pero no dentro de
este lab.

## Ritmo de Trabajo

Este lab tiene 25 minutos:

| Min | Debe existir |
|---:|---|
| 0–4 | Rama correcta, base levantada, y el estado de la base y de la suite a la vista |
| 4–10 | La API respondiendo a una petición real, después de aplicar el esquema |
| 10–14 | El diff de la rama revisado entero |
| 14–20 | La solicitud de cambios abierta, con su descripción escrita |
| 20–25 | Rama integrada y borrada, `main` en verde |

**Si vas tarde:** lo que no puede quedarse a medias es la solicitud de cambios
abierta con su descripción. Integrar y borrar la rama son dos minutos y se
pueden hacer fuera de clase. Si te vas al Lab 02 sin haber integrado, crea allí
la rama desde `feature/persistencia` y no desde `main`: el trabajo de hoy
necesita la configuración de conexión y las migraciones, y `main` todavía no las
tiene.

## Paso a Paso

### 1. Confirmar desde dónde partes

Arranca Claude Code en el repositorio del proyecto:

```bash
cd ~/curso-claude/curso-claude-code-api
claude
```

Pídele el punto de partida, **sin tocar la base de datos**:

```text
Dime, sin cambiar nada del código ni de la base de datos:

1. En qué rama estoy, si el árbol de trabajo está limpio y qué ramas existen en
   el remoto.
2. Los commits de esta rama que no están en main, uno por línea.
3. Si el contenedor de PostgreSQL está levantado. Si no lo está, levántalo y
   espera a que quede sano, pero no apliques ninguna migración.
4. Qué tablas hay ahora mismo en la base de datos y en qué revisión de Alembic
   está.
5. El resultado de uv run pytest -q.
```

Debes estar en `feature/persistencia`. Si no lo estás, pídele que cambie a esa
rama antes de continuar.

Quédate con los dos últimos puntos juntos: **qué hay en tu base y qué dice tu
suite**. Vas a usarlos en el paso siguiente.

### 2. Preguntarle a la API

Hasta ahora comprobabas el comportamiento desde las pruebas, con la aplicación
en memoria. Ahora pregunta al servicio:

```text
Levanta la API en segundo plano, espera hasta que arranque, y hazme estas
peticiones con curl mostrando el código de estado y el cuerpo de cada una:

1. GET /health
2. GET /states

Después detén el servidor. No cambies ningún archivo, no apliques migraciones y
no toques la base de datos.
```

Aquí pueden pasar dos cosas, y las dos son un resultado válido:

| Lo que ves | Qué significa |
|---|---|
| `/states` falla, o responde con una lista vacía | Tu suite estaba en verde y la API no puede responder. Las dos comprobaciones no contestan la misma pregunta |
| `/states` devuelve los cuatro estados | Tu base conservaba el esquema. Lo verás igual en cuanto vuelvas a ejecutar la suite completa |

Si te ha pasado lo primero, no es un error tuyo. Tu suite aplica las migraciones
al empezar y las revierte al terminar, así que dejó la base sin esquema y aun
así terminó en verde: comprueba el comportamiento del código, no que el servicio
esté en pie. El volumen nunca se perdió, y por eso se arregla en un comando.

Arréglalo ahora y vuelve a preguntar:

```text
Aplica las migraciones hasta head y repite las dos peticiones, más una segunda
llamada a GET /states. Dime qué había en la base antes y qué hay después.
```

Lo que tiene que haber ocurrido:

- `/health` responde `200` con `{"status": "ok"}`.
- `/states` devuelve los cuatro estados de tu contrato, con el esquema exacto:
  `id` y `code`, ni un campo más.
- Las dos llamadas a `/states` devuelven los estados **en el mismo orden**.

Fíjate también en algo que pasó de lado: para levantar la API, Claude te pidió
permiso. Tus reglas de la sesión 4 cubren las pruebas, el linter y las
migraciones, pero no esto. Una configuración de permisos envejece con el
trabajo.

### 3. Revisar la rama entera antes de entregarla

Hasta ahora revisabas un cambio recién hecho. Esto es distinto: son los commits
de otro día, y quien los lea no va a tener tu conversación.

```text
/diff
```

Recórrelo con una pregunta concreta: **¿hay algo aquí que no pertenezca a la
persistencia?** Un archivo de configuración de tu editor, una prueba a medias,
un `print` olvidado. Si aparece, dilo y pídele que lo saque en su propio commit
o que lo quite, según lo que sea.

### 4. Abrir la solicitud de cambios

Primero la descripción, y la escribes tú:

```text
Voy a abrir una solicitud de cambios de feature/persistencia hacia main.
Propónme una descripción con estas cuatro secciones y nada más:

- Qué cambia, en dos o tres frases.
- Qué decisión se tomó y por qué, tomándola del plan y de los mensajes de
  commit, sin inventar motivos.
- Cómo se comprueba, con los comandos exactos que otra persona ejecutaría.
- Qué queda sin probar.

Enséñamela antes de crear nada. No la publiques todavía.
```

Lee la última sección con atención, porque es la que nadie escribe. Si dice que
no queda nada sin probar, es falso: el contrato de Proyectos define un `409` al
borrar un proyecto con tareas, y no hay tareas todavía. Díselo y pídele que lo
corrija.

Cuando la descripción te convenza:

```text
Crea la solicitud de cambios de feature/persistencia hacia main con esa
descripción, usando la CLI de mi proveedor. No la integres.
```

### 5. Integrar y cerrar la rama

Ábrela en el navegador y léela como si acabaras de entrar al equipo: la
descripción, la lista de archivos y los mensajes de commit. Quédate con **qué le
falta para que alguien la apruebe sin preguntarte nada**.

Después:

```text
Integra la solicitud de cambios en main. Luego actualiza mi main local, borra la
rama feature/persistencia en local y en el remoto, y comprueba que la suite
sigue verde en main.
```

Una rama integrada que se queda abierta es ruido: en tres semanas nadie sabe si
está pendiente o terminada. Se borra al integrarla, y el historial de `main`
conserva el trabajo.

Antes de pasar al Lab 02, mira dos cosas:

```text
/permissions
```

Te enseña las reglas que están mandando ahora mismo. Fíjate en si publicar sigue
en la lista de lo que se te pregunta, y en qué le faltó cubrir hoy.

```text
/context
```

El Lab 02 empieza una tarea distinta. Decide si sigues en esta conversación o
arrancas limpio, y decídelo mirando el número.

## Validación

Pídele la comprobación completa y léela entera:

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué ramas existen en local y en el remoto.
3. Los últimos ocho commits de main, uno por línea.
4. El estado de la solicitud de cambios que abrí.
5. uv run pytest -q y uv run ruff check .
6. Qué tablas hay en la base de datos y en qué revisión de Alembic está.
```

El lab está completo si:

- [ ] Sabes en qué estado estaba tu base al empezar y qué decía tu suite en ese momento.
- [ ] Comprobaste `GET /health` y `GET /states` contra la API corriendo, no con la suite.
- [ ] Puedes decir en una frase qué pregunta responde la suite y qué pregunta responde una petición real.
- [ ] `GET /states` devolvió los cuatro estados con el esquema exacto, y las dos llamadas en el mismo orden.
- [ ] Revisaste el diff completo de la rama y ningún archivo ajeno a la persistencia llegó a `main`.
- [ ] La descripción de la solicitud de cambios tiene las cuatro secciones, y la de lo que queda sin probar dice algo concreto.
- [ ] La solicitud está integrada y `main` está en verde.
- [ ] `feature/persistencia` ya no existe, ni en local ni en el remoto.
- [ ] Sabes decir qué le falta a tu entrega para que alguien la apruebe sin preguntarte.
- [ ] Sabes qué comando tuvo que pedirte permiso hoy y no estaba en tus reglas.

## Limpieza

Ninguna. La base se queda levantada y el Lab 02 trabaja sobre este mismo
estado.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| No tienes la rama `feature/persistencia`, o no la publicaste | Este lab no se puede recuperar aquí: necesita el trabajo de la sesión 4, que es autosuficiente y trae un plan de referencia en su Lab 01. Hazla entera antes de seguir. Si estás en clase, sáltate este lab y sigue en el 02 desde la rama que tengas: construye herramientas y no depende de la entrega de hoy |
| Faltaste a la sesión 4 y no tienes remoto | Empieza por su Lab 03, que crea el repositorio remoto y publica. Son treinta minutos y sin eso no hay nada que entregar |
| No tienes `gh` ni `glab` instalada | Instálala ahora: es el desafío de la sesión 4 y el resto del lab depende de ella. Pídele a Claude que te guíe con el instalador de tu sistema y que autentique la sesión. Si se alarga, sigue el lab hasta el paso 3 y abre la solicitud desde el navegador |
| `GET /states` responde `200` con una lista vacía | Las migraciones no están aplicadas, o lo están a medias. Vuelve al paso 1 y comprueba en qué revisión está la base. No parchees el endpoint |
| `GET /states` falla con un error de conexión | La API no encuentra la base. Pídele que compruebe que el contenedor está sano y qué URL está usando, sin abrir `.env` |
| El servidor se queda ocupando la terminal | Pídele que lo levante en segundo plano y que te confirme el identificador del proceso, para poder detenerlo al terminar el paso |
| Claude te pide permiso para levantar la API | Es normal: tus reglas de ayer no lo cubrían. Apruébalo por esta vez y anótalo, porque el Lab 02 revisa esa configuración |
| El diff de la rama trae un archivo que no pertenece | Sácalo antes de entregar. Si ya está en un commit anterior, pídele que lo quite en un commit propio con prefijo `chore:` en lugar de reescribir el historial |
| La integración se bloquea por conflictos | No debería haberlos: `main` no cambió desde la sesión 2. Si aparecen, pídele que te enseñe qué archivos y por qué antes de resolver nada |
| No te dejan integrar tu propia solicitud | Algunos proveedores exigen una aprobación. Busca en la configuración del repositorio la regla que lo pide y desactívala: eres el único que trabaja aquí |
| Borraste la rama y te falta algo de ella | El trabajo está en `main`, no se perdió. Si de verdad necesitas la rama, se recrea desde el commit de integración: pídeselo antes de improvisar |
