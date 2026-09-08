# Referencia Rápida — Sesión 8

## Comandos de la Sesión

| Comando o control | Qué hace | Dónde lo usas |
|---|---|---|
| `/hooks` | Muestra los hooks configurados: evento, filtro, tipo y archivo de origen | Labs 03 y 04 |
| `/permissions` | Muestra tus listas de permisos | Lab 03, para descartar que el caso sea un permiso |
| `/skills` | Lista las skills que la sesión reconoce | Lab 02 |
| `/diff` | Revisa los cambios antes de confirmar | Los cuatro labs |
| `Esc` | Interrumpe el turno en curso | Lab 01, si empieza a corregir en vez de comparar |
| `/context` | Muestra qué ocupa la ventana de contexto | Al cerrar cada lab |

`/hooks` **no configura nada**: es un visor. Los hooks se escriben en
`.claude/settings.json`, el mismo archivo de los permisos de la sesión 4.

## Cuatro Capas, y Cuándo Decide Cada Una

| Capa | Dónde vive | Cuándo decide | Qué no puede |
|---|---|---|---|
| Instrucción | `CLAUDE.md` | Al leerla, cada sesión | Obligar: es contexto |
| Convención | `.claude/rules/` | Al cargar, siempre o por ruta | Obligar: sigue siendo contexto |
| Permiso | `.claude/settings.json` | Antes de la herramienta, por nombre y argumento | Depender del resultado de una comprobación |
| Hook | `.claude/settings.json` | En un evento del ciclo de vida | Salir del ciclo de vida de Claude Code |

La frontera que decide el Lab 03: un permiso sabe bloquear `git commit`
siempre; no sabe bloquearlo **solo cuando** una comprobación falla. Esa
condición es lo que hace falta un hook.

## Antes y Después no son lo Mismo

| | Evento de antes | Evento de después |
|---|---|---|
| Cuándo se dispara | Antes de que la herramienta se ejecute | Cuando ya terminó |
| Puede impedirlo | Sí | **No**: lo escrito ya está escrito |
| Para qué sirve | Guardarraíl: la operación no ocurre si la comprobación falla | Reacción: regenerar algo, avisar, dejar constancia |
| Fallo típico de diseño | Ponerlo demasiado ancho y pagar la comprobación en cada comando | Creer que bloquea, y quedarse con un aviso donde querías una barrera |

Un hook **de tipo comando** ejecuta shell, así que solo puede regenerar lo
que un comando produce. Lo que produce una skill —porque la skill se invoca en
la sesión— no lo puede regenerar: como mucho, avisar de que quedó viejo. La
documentación lista otros tipos de hook, entre ellos uno que lanza un
subagente; el curso no los usa.

## Dónde Termina un Hook

Un hook se dispara en el ciclo de vida de **Claude Code**. Un comando que
tecleas tú en otra terminal no es una llamada a herramienta, así que no lo
atraviesa. Y la documentación oficial es explícita en que el filtro por
contenido del comando es de mejor esfuerzo: para prohibir algo de plano, la
capa correcta son los permisos, no un hook.

## Lo que una Especificación no Puede Prometer

| El contrato dice | OpenAPI puede expresarlo |
|---|---|
| Qué campos devuelve cada ruta, y de qué tipo | Sí |
| Qué código de estado corresponde a cada error | Sí |
| Que una colección devuelve una lista en la raíz | Sí |
| Que dos llamadas idénticas devuelven el mismo orden | **No**: es una garantía entre llamadas |
| Que `due_at` sale siempre en UTC con `Z` y sin microsegundos | **A medias**: puede restringir la forma de la cadena, pero no obliga a la implementación a cumplirla |

Y una donde el contrato cede a propósito: para un `422` de validación acepta
la forma que genere el framework, con la condición de que la clave de primer
nivel siga siendo `detail`.

## Si Algo Falla

| Señal | Causa habitual |
|---|---|
| El hook no aparece en `/hooks` | El JSON no cargó. Revisa el archivo y vuelve a mirar: si no está en el visor, no existe para la sesión |
| El commit pasa con la especificación desincronizada | El filtro no captura el comando, o el evento elegido no es de los que pueden bloquear |
| Todos los comandos se volvieron lentos | El filtro cubre cualquier uso de Bash y la comprobación corre en cada uno |
| El hook bloquea siempre, incluso con todo al día | La comprobación falla por otra razón. Ejecútala a mano y mira su salida y su código de salida |
| Regenerar la especificación da un resultado distinto cada vez | Hay algo no determinista en la generación. Sin resolver eso, el hook del Lab 03 bloquea al azar |
