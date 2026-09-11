# Referencia Rápida — Sesión 9

## Comandos de la Sesión

| Comando o control | Qué hace | Dónde lo usas |
|---|---|---|
| `@agent-<nombre>` | Invoca a un subagente concreto, en vez de dejar que Claude elija | Labs 01, 03 y 04 |
| `/code-review` | Revisa el diff actual | Lab 02 |
| `/subtask` | Delega aparte, con tu conversación completa, y devuelve el resultado aquí | Lab 02 |
| `/security-review` | Revisión de seguridad de fábrica, sobre lo pendiente de la rama | Lab 03 |
| `/skills` | Lista las skills que la sesión reconoce, incluidas las incorporadas | Lab 02, para ver si tienes `/code-review` |
| `/context` | Muestra qué ocupa la ventana de contexto | Al cerrar cada lab |
| `/list-agents` | Lista los subagentes que la sesión reconoce, si tu instalación lo trae | Lab 01, al comprobar el primero |
| `/exit` | Cierra la sesión, para recoger el primer archivo de `.claude/agents/` | Lab 01, solo si hace falta |

`/list-agents` lista los subagentes, pero no es el equivalente de `/skills` o
`/hooks`: lista también otras sesiones y solo está donde la mensajería entre
sesiones está habilitada. Lo que siempre funciona es invocar al agente.

## Contexto de Cada Forma de Trabajo

| Forma | Qué contexto lleva | Qué devuelve | Cuándo sirve |
|---|---|---|---|
| Pedirlo en tu hilo | Todo: la conversación entera | La respuesta, en el hilo | Cuando quieres seguir dirigiendo turno a turno |
| `/subtask` | Hereda tu conversación | El resultado vuelve al hilo | Delegar una tarea con el historial disponible |
| `/fork` | Copia tu conversación | Crea otra sesión en segundo plano; con agent view desactivado conserva la modalidad de subagente | Continuar aparte; comprueba la modalidad en `/help` |
| Subagente de `.claude/agents/` | Instrucciones y encargo redactado por Claude; no hereda el historial | Su resultado | Revisar con un encargo inspeccionado que excluya el relato del autor |

El que hereda tu conversación recibe también sus supuestos. Para comprobar
una duda del hilo puede ser útil; no lo cuentes como una revisión independiente.

## Qué Carga un Subagente al Arrancar

| Sí carga | No carga |
|---|---|
| El cuerpo de su propio archivo, que es su oficio | Tu conversación |
| La jerarquía de `CLAUDE.md` del proyecto | Los archivos que Claude ya leyó en tu hilo |
| Una instantánea de git status del inicio de la sesión principal | El contenido actualizado de todos los archivos: debe leerlos |
| El encargo que redacta Claude | Los hallazgos anteriores, salvo que se incluyan en el encargo |

Por eso, si quieres que sepa algo que solo está en tu conversación —lo que
encontró otro agente, por ejemplo—, se lo pasas **dentro del encargo**. No
hace falta inventar un archivo para eso.

Lo que sí lo acompaña son tus hooks: los dos que configuraste en la sesión 8
se disparan igual cuando el que llama a la herramienta es un subagente.

## La Captura del Cambio

`~/curso-claude/s09-revision/errores-api.diff` guarda el cambio del Lab 01
fuera del repositorio, con su commit base anotado en tus notas. Las rutas
revisadas se preparan con `git add` antes de capturarlas con
`git diff --cached --binary HEAD`, para incluir los archivos nuevos.
Preparar no es confirmar: el refactor sigue pendiente de revisión.

Si cambia el código, conserva la captura anterior y genera otra identificada.
El diff no contiene todo el proyecto ni sustituye al contrato. La revisión
del Lab 02 usa esa captura como referencia del alcance; el Lab 04 registra
qué estado se revisó antes de integrar.

## La Escalera de Autoridad

| Agente | Qué puede | Qué no puede |
|---|---|---|
| `refactorizador` | Leer, buscar, editar, escribir, ejecutar | Sus herramientas permiten confirmar y tocar tests o contrato; su instrucción le ordena no hacerlo |
| `auditor-de-seguridad` | Leer y buscar | Editar, escribir, ejecutar y delegar |
| `consolidador-de-hallazgos` | Leer, buscar y ejecutar | Editar y escribir **con herramientas de edición**; ejecutar deja abierto el camino del shell |

Dos cosas que conviene no confundir. La primera: **si no declaras
herramientas, el agente hereda las disponibles para subagentes**. La segunda: recortar
herramientas no es lo mismo que negar un permiso. Son dos capas distintas, y
la de permisos tiene además una regla propia para esto —`Agent(<nombre>)` en
tu lista `deny` impide usar un subagente concreto sin tocar su archivo—.

## Skill, Hook o Subagente

| Lo que necesitas | Qué usar | Por qué |
|---|---|---|
| Un procedimiento repetido, con tu contexto delante | Skill | Puede definir un procedimiento reutilizable; revisa dónde se ejecuta cada skill |
| Que algo ocurra siempre, decida lo que decida Claude | Hook | Se dispara al ocurrir el evento configurado y coincidir su filtro |
| Un juicio que no conozca tu conversación | Subagente | Su valor está justo en no saber cómo llegaste ahí |
| Terminar algo que ya empezaste, sin gastar tu ventana | `/subtask` | Delega con tu contexto completo y devuelve el resultado |

La prueba opcional del Lab 04 usa un archivo temporal fuera de la API.
Registra si el consolidador se niega, escribe por comandos o queda bloqueado
por permisos; limpia la prueba y comprueba que el refactor no cambió.

## Cómo se Tría un Hallazgo

| Clase | Qué exige | Qué se escribe |
|---|---|---|
| Aceptado | Una comprobación que lo confirme y pertinencia al alcance | Qué se ejecutó y qué salió |
| Rechazado por evidencia | Una comprobación que desmienta el problema | Qué se comprobó y qué resultado lo desmiente |
| Rechazado por alcance o decisión | La decisión documentada que lo deja fuera de alcance | Archivo y decisión; condiciones en que un riesgo real sí importaría |
| Pendiente | Nada lo confirma ni lo desmiente todavía | Qué faltaría para decidirlo |

## Si Algo Falla

| Señal | Causa habitual |
|---|---|
| El agente no responde a su nombre | Es el primer archivo de `.claude/agents/` y el directorio no existía al arrancar: cierra con `/exit` y vuelve a abrir |
| Devuelve buenas prácticas genéricas | Le falta oficio en el archivo, no contexto: escribe contra qué revisa y en qué orden |
| Hace más de lo que le pediste | Le declaraste de más, o no le declaraste nada y heredó todo |
| No puede leer un archivo que necesita | Mira `/permissions`: una regla `deny` de la sesión 4 es la primera candidata |
| Su informe se perdió al seguir trabajando | Solo vuelve el resumen, y vive en la conversación: si lo vas a necesitar más tarde, cópialo a tus notas o vuelve a invocarlo |
| Los veredictos coinciden en todo | Resultado válido. Registra contexto, herramientas y alcance; la coincidencia no prueba ausencia de defectos |
