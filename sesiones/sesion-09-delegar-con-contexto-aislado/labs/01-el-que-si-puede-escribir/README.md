# Lab 01: El que sí Puede Escribir

## Objetivo

Construir el subagente encargado de modificar código, encargarle un módulo centralizado de manejo de errores para toda la
API sin supervisarlo turno a turno, y comparar su resumen con el diff que dejó.

## Por qué este lab

Llevas ocho sesiones dirigiendo a Claude turno a turno: lees lo que propone,
cortas cuando se desvía, apruebas cada paso. Eso no escala a todo. Hay trabajo
que vas a encargar y no vas a mirar mientras ocurre, y cuando termine tendrás
dos cosas delante: lo que el agente dice que hizo, y lo que realmente cambió en
tus archivos.

Hoy delegas uno de esos trabajos. Lo primero que decides no es qué te haga,
sino **con cuánta autoridad**: un subagente al que no le declaras herramientas
hereda las disponibles para subagentes. La autoridad mínima hay que escribirla, y se escribe en una
línea.

## Requisitos

- Sesión 8 completa: `main` en verde, sin ramas abiertas, `openapi.json`
  confirmado y los dos hooks cargados en `.claude/settings.json`.
- Docker arrancado y la base de datos levantada con las migraciones aplicadas.
  Los contenedores los levanta Claude.

## Ritmo de Trabajo

Este lab tiene 41 minutos:

| Min | Debe existir |
|---:|---|
| 0–4 | La rama abierta y el punto de partida confirmado |
| 4–12 | `.claude/agents/refactorizador.md` revisado, con su límite escrito, y guardado |
| 12–29 | El encargo comprobado y ejecutado, o la conclusión de que no había refactor justificado |
| 29–41 | Captura `.diff` completa con su commit base, comparada con el resumen; resultado de la suite anotado |

**Si necesitas cortar aquí:** guarda y confirma el archivo del agente y anota
el encargo pendiente. Es una pausa: antes del Lab 02 debes terminar la
ejecución y guardar la captura completa con su commit base. Si no había un
refactor justificado, guarda la captura vacía y registra el motivo.

## Paso a Paso

### 1. Abrir la rama y confirmar el punto de partida

```text
Crea la rama feature/errores-en-un-solo-lugar desde main, y confírmame que
main está actualizado, el árbol de trabajo está limpio, la base de datos
está levantada con las migraciones aplicadas y la suite pasa en verde.
```

Si la suite no está verde, para aquí: hoy vas a comparar un antes con un
después, y sin un antes limpio no hay comparación.

Comprueba en el README qué estado deja la suite en la base de datos. Si sus
tests revierten las migraciones al terminar, pide aplicarlas de nuevo antes
de comprobar peticiones contra la API levantada.

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
- Trabaja solo sobre el alcance acordado. Puede crear un módulo común y
  modificar los módulos necesarios para conectarlo; no aprovecha el encargo
  para reorganizar otras partes del proyecto.
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
  hereda las disponibles para subagentes. Aquí necesita leer, buscar, editar y
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
anota la rama y el encargo pendiente, cierra con `/exit` y vuelve a abrir
Claude en la raíz del proyecto. A partir de la próxima vez, los cambios
en ese directorio se recogen solos.

Confirma el archivo del agente en su propio commit `chore:`, antes de
encargarle nada. Anota el identificador completo de ese commit: será la base
de la captura del cambio. Comprueba que el árbol y el área de preparación
quedaron limpios.

### 4. Soltarlo

Primero comprueba si el encargo corresponde a tu implementación:

```text
Sin editar, identifica cómo se manejan los errores en toda la API, incluidos
tareas, proyectos y validación de entradas. Comprueba si existe un módulo
común y si todos esos casos pasan por él. Indica qué archivos habría que
crear o modificar para centralizar ese manejo y qué códigos y cuerpos de
respuesta deben conservarse. No propongas cambios ajenos a ese alcance.
```

Revisa las rutas propuestas: pueden abarcar varios módulos, pero cada cambio
debe servir al manejo centralizado de errores. Si ya existe y cubre toda la
API, encarga al refactorizador comprobarlo y devolver su conclusión sin editar.
Los siguientes labs revisarán el código actual; registra "sin refactor
justificado" y conserva esa condición en el triaje final.

Ahora el encargo. Se invoca por su nombre, con `@agent-refactorizador` al
principio del mensaje:

```text
@agent-refactorizador Centraliza el manejo de errores de toda la API en un
módulo común, incluidos los errores de tareas, proyectos y validación de
entradas. Reutiliza el módulo existente si lo hay y completa su cobertura.
Puedes modificar los módulos necesarios para conectarlo, dentro de las rutas
acordadas; no cambies la lógica de negocio ni reorganices código ajeno al
manejo de errores.

Conserva todos los códigos de estado y cuerpos de respuesta actuales: cada
caso que hoy devuelve 404, 409 o 422 debe devolver exactamente lo mismo, y lo
mismo vale para los demás errores existentes. Conserva también la respuesta
actual de validación del framework. No añadas nuevos comportamientos ni
expongas detalles internos. No cambies el contrato, los tests ni las
dependencias. Ejecuta las comprobaciones existentes y declara qué casos
quedan sin comprobar.
```

Mientras trabaja, **no lo supervises**. Deja que termine el
encargo y atiende los permisos que solicite. Después contrastarás su resumen
con los archivos.

### 5. Guardar el cambio y contrastarlo con el resumen

Lo que tienes delante es el **resumen** del agente: su relato de su propio
trabajo. Léelo entero antes de mirar nada más y anota qué dice que cambió.

Guarda una captura antes de empezar la revisión. Preparar archivos con
`git add` no los confirma: permite incluir en el diff el módulo recién creado,
que un diff de archivos ya versionados podría omitir.

```text
Muéstrame todos los archivos modificados, eliminados y nuevos desde el commit
base que anotamos antes del refactor. Señala cualquier cambio ajeno al encargo.
No incluyas secretos, archivos ignorados ni artefactos temporales. Espera a que
revise la lista antes de preparar las rutas explícitas con git add.
```

Revisa la lista completa. Una modificación fuera de alcance también es
evidencia: no la ocultes del diff. Si contiene información sensible, detente y
resuelve esa exposición antes de generar o enviar la captura.

```text
Prepara en Git las rutas que acabamos de revisar, incluidos los archivos nuevos,
sin hacer commit. Comprueba que HEAD sigue siendo el commit base y que no
quedaron cambios del refactor fuera del área de preparación.
Crea ~/curso-claude/s09-revision/ fuera del repositorio y guarda allí
errores-api.diff con la salida de git diff --cached --binary HEAD.
Si ya existe, usa un nombre nuevo e indícame la ruta; no sobrescribas otra revisión.
Muestra el commit base y el resumen de archivos del diff. Comprueba que la
captura coincide con el diff preparado y que incluye el módulo común y sus
conexiones. Si no hubo cambios, guarda el diff vacío y confirma ese resultado.
```

Lee el archivo completo en el editor y compáralo con el resumen: ¿falta algo
en el relato del agente? ¿Afirma haber cambiado algo que no aparece? Conserva
la ruta de la captura y su commit base en tus notas.

La captura contiene el cambio frente a esa base, no todo el proyecto. No
edites ni confirmes el refactor hasta terminar su revisión: el Lab 02 necesita
ese mismo estado. Si hay que cambiarlo, conserva esta captura y genera otra
identificada antes de revisar de nuevo.

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
6. La ruta de errores-api.diff, su commit base y si coincide con el cambio
   preparado, incluidos los archivos nuevos; qué rutas quedaron fuera.
```

El lab está completo si:

- [ ] `.claude/agents/refactorizador.md` está versionado y confirmado en su propio commit.
- [ ] El archivo declara sus herramientas y su límite, incluido no confirmar en git.
- [ ] El encargo lo ejecutó el agente, no el hilo, y volvió con un resumen.
- [ ] Revisaste el alcance de toda la API y señalaste cualquier archivo cambiado sin justificación; registraste qué comportamientos se comprobaron y cuáles faltan.
- [ ] Guardaste y leíste el `.diff` completo fuera del repositorio, incluidos los archivos nuevos, y anotaste su commit base; si está vacío, explicaste por qué.
- [ ] Comparaste la captura con el resumen y puedes señalar diferencias o afirmar que no las hay.
- [ ] Registraste el resultado de la suite, verde o rojo, y el refactor está **sin confirmar**, o anotaste que no había uno justificado.

## Limpieza

Conserva la captura fuera del repositorio y las rutas preparadas sin confirmar.
El Lab 02 revisa ese mismo estado.
Antes de seguir, `/context`: mira cuánto ocupó en tu ventana un
trabajo que se hizo entero fuera de ella.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El agente no responde a `@agent-refactorizador` | Es el primer archivo de `.claude/agents/`, y ese directorio no existía al arrancar. Guarda tus notas, cierra con `/exit`, vuelve a abrir en la raíz del proyecto y repite el encargo |
| El archivo que te enseña no declara herramientas | Pídeselo explícitamente y que te diga qué hereda si no las declara. Un subagente sin herramientas declaradas hereda las disponibles para subagentes: es justo lo que este lab no quiere |
| Dejó la suite en rojo | Está dentro de lo posible y no invalida el lab: anótalo, porque contrástalo con lo que cubra la revisión del Lab 02. No lo arregles tú todavía |
| El commit del archivo del agente queda bloqueado por el hook | El hook de la sesión 8 compara la especificación con el código, y aquí todavía no has tocado código: comprueba el motivo del bloqueo y el resultado del hook. Regenera `openapi.json`, mira qué cambió y déjalo al día antes de delegar nada |
| Tardó mucho y sigue trabajando | Espera su resultado antes del Lab 02. Si tienes que pausar, registra el trabajo pendiente; el archivo del agente por sí solo no completa el lab |
| Cambió tests para que pasaran | Su límite lo prohíbe. Anota las rutas y conserva el cambio para contrastarlo con la revisión del Lab 02; el revisor podría detectarlo o pasarlo por alto |
