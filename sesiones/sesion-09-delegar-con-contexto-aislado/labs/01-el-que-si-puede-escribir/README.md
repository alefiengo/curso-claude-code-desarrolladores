# Lab 01: El que sí Puede Escribir

## Objetivo

Construir el primer subagente del proyecto —el único de hoy con autoridad para
escribir—, soltarlo sobre un cambio acotado sin supervisarlo turno a turno, y
comparar el resumen que devuelve con el diff que dejó.

## Por qué este lab

Llevas ocho sesiones dirigiendo a Claude turno a turno: lees lo que propone,
cortas cuando se desvía, apruebas cada paso. Eso no escala a todo. Hay trabajo
que vas a encargar y no vas a mirar mientras ocurre, y cuando termine tendrás
dos cosas delante: lo que el agente dice que hizo, y lo que realmente cambió en
tus archivos.

Hoy delegas uno de esos trabajos. Lo primero que decides no es qué te haga,
sino **con cuánta autoridad**: un subagente al que no le declaras herramientas
las hereda todas. La autoridad mínima hay que escribirla, y se escribe en una
línea.

## Requisitos

- Sesión 8 completa: `main` en verde, sin ramas abiertas, `openapi.json`
  confirmado y los dos hooks cargados en `.claude/settings.json`.
- Docker arrancado y la base de datos levantada con las migraciones aplicadas.
  Los contenedores los levanta Claude.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–4 | La rama abierta y el punto de partida confirmado |
| 4–13 | `.claude/agents/refactorizador.md` revisado, con su límite escrito, y guardado |
| 13–22 | El encargo entregado al agente y su resumen de vuelta |
| 22–30 | El diff leído entero y comparado con lo que el resumen dice |

**Si necesitas cortar aquí:** lo mínimo es el archivo del agente guardado y
confirmado. El encargo puede esperar, pero el Lab 02 necesita un cambio que
revisar.

## Paso a Paso

### 1. Abrir la rama y confirmar el punto de partida

```text
Crea la rama feature/errores-en-un-solo-lugar desde main, y confírmame que
main está actualizado, el árbol de trabajo está limpio, la base de datos
está levantada con las migraciones aplicadas y la suite pasa en verde.
```

Si la suite no está verde, para aquí: hoy vas a comparar un antes con un
después, y sin un antes limpio no hay comparación.

### 2. Escribir el primer subagente

Un subagente vive en `.claude/agents/`, se versiona como las skills, y arranca
**sin tu conversación**. Todo lo que sabe de su oficio está en el archivo.

```text
Crea un subagente de proyecto llamado refactorizador. Enséñame el archivo
antes de guardarlo.

Que su descripción diga cuándo delegarle trabajo: reorganizar código
existente sin cambiar comportamiento.

Que en el cuerpo quede escrito que:

- Antes de tocar nada, lee el contrato de la API y las reglas del proyecto.
- Trabaja sobre un solo modulo por encargo, el que se le indique.
- Deja la suite en verde: si algo se pone en rojo, lo arregla o revierte su
  cambio y lo dice.
- Termina informando qué archivos tocó y qué decidió, no solo que terminó.

Y un límite: el refactorizador reorganiza, no decide. No cambia el contrato
de la API, no modifica tests para que pasen, no añade dependencias y no
confirma nada en git.

Dime también qué herramientas le declaras y por qué esas.
```

Cuando te lo enseñe, comprueba tres cosas antes de guardarlo:

- **Que declara sus herramientas.** Si el archivo no las declara, el agente
  hereda todas las que tú tienes. Aquí necesita leer, buscar, editar y
  ejecutar; nada más.
- **Que el límite está escrito**, y que incluye no confirmar en git: el commit
  se decide aquí, con el diff delante.
- **Que no repite lo que ya dice tu `CLAUDE.md`.** Un subagente carga tu
  memoria de proyecto igual que tú; copiarla dentro gasta contexto dos veces.

### 3. Comprobar que existe

Hay un comando que los lista, `/list-agents`, pero no es el equivalente exacto
de `/skills` o `/hooks`: lista también otras sesiones y solo está disponible
donde la mensajería entre sesiones lo está. Pruébalo, y si no te responde, la
comprobación que siempre funciona es mirar el disco:

```text
Lista los archivos que hay ahora mismo en .claude/agents/ y enséñame el
encabezado del que acabas de crear, tal como quedó en disco.
```

Hay un tropiezo que solo ocurre hoy: `.claude/agents/` no existía cuando
arrancaste la sesión. Si más adelante el agente no responde a su nombre,
cierra con `/exit` y vuelve a abrir. A partir de la próxima vez, los cambios
en ese directorio se recogen solos.

Confirma el archivo del agente en su propio commit `chore:`, antes de
encargarle nada.

### 4. Soltarlo

Ahora el encargo. Se invoca por su nombre, con `@agent-refactorizador` al
principio del mensaje:

```text
@agent-refactorizador Los endpoints de tareas levantan sus errores cada uno
por su cuenta. Centraliza el manejo de errores de ese modulo en un solo
lugar, sin cambiar ni un código de estado ni la forma de la respuesta:
lo que hoy devuelve 404, 409 o 422 tiene que seguir devolviendo exactamente
lo mismo, con el mismo cuerpo.
```

Mientras trabaja, **no lo supervises**. No es una recomendación de estilo: es
la situación que estás practicando. Trabaja en su propia ventana de contexto,
y de todo lo que haga ahí dentro solo va a volver una cosa.

### 5. Leer lo que volvió, y después lo que hizo

Lo que tienes delante es el **resumen** del agente: su relato de su propio
trabajo. Léelo entero antes de mirar nada más y anota qué dice que cambió.

Ahora mira el cambio de verdad:

```text
/diff
```

Recórrelo entero, archivo por archivo. Después contesta tú, sin preguntárselo
a Claude: ¿hay algo en el diff que el resumen no menciona? ¿Hay algo del
resumen que no aparece en el diff?

No confirmes el refactor todavía. Sin revisar, no se integra.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y qué archivos tiene modificados el árbol de trabajo.
2. Qué hay en .claude/agents/, y qué herramientas declara cada archivo.
3. Si el archivo del refactorizador dice explícitamente que no confirma en
   git, y con qué palabras.
4. uv run pytest -q y uv run ruff check .
5. Si openapi.json sigue coincidiendo con la especificación que genera el
   código ahora mismo.
```

El lab está completo si:

- [ ] `.claude/agents/refactorizador.md` está versionado y confirmado en su propio commit.
- [ ] El archivo declara sus herramientas y su límite, incluido no confirmar en git.
- [ ] El encargo lo ejecutó el agente, no el hilo, y volvió con un resumen.
- [ ] Leíste el `/diff` entero y puedes nombrar una diferencia entre lo que el resumen cuenta y lo que el diff muestra, o afirmar que no la hay.
- [ ] La suite sigue en verde y el refactor está **sin confirmar**.

## Limpieza

Ninguna. El Lab 02 revisa exactamente este cambio, sin confirmar y sin
publicar. Antes de seguir, `/context`: mira cuánto ocupó en tu ventana un
trabajo que se hizo entero fuera de ella.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El agente no responde a `@agent-refactorizador` | Es el primer archivo de `.claude/agents/`, y ese directorio no existía al arrancar. Cierra con `/exit`, vuelve a abrir y repite el encargo |
| El archivo que te enseña no declara herramientas | Pídeselo explícitamente y que te diga qué hereda si no las declara. Un subagente sin herramientas declaradas las hereda todas: es justo lo que este lab no quiere |
| Dejó la suite en rojo | Está dentro de lo posible y no invalida el lab: anótalo, porque es exactamente lo que el Lab 02 tiene que detectar. No lo arregles tú todavía |
| El commit del archivo del agente queda bloqueado por el hook | El hook de la sesión 8 compara la especificación con el código, y aquí todavía no has tocado código: si salta, arrastras algo desde la sesión 8. Regenera `openapi.json`, mira qué cambió y déjalo al día antes de delegar nada |
| Tardó mucho y sigue trabajando | Déjalo terminar. Si te pasas del tiempo del lab, el mínimo para continuar es tener el agente guardado y confirmado |
| Cambió tests para que pasaran | Su límite lo prohíbe. No lo corrijas en el hilo: déjalo tal cual, porque el Lab 02 lo va a encontrar y esa es la prueba de que el revisor sirve |
