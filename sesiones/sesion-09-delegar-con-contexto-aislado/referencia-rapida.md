# Referencia Rápida — Sesión 9

## Comandos de la Sesión

| Comando o control | Qué hace | Dónde lo usas |
|---|---|---|
| `@agent-<nombre>` | Invoca a un subagente concreto, en vez de dejar que Claude elija | Los cuatro labs |
| `/subtask` | Delega aparte, con tu conversación completa, y devuelve el resultado aquí | Lab 02 |
| `/security-review` | Revisión de seguridad de fábrica, sobre lo pendiente de la rama | Lab 03 |
| `/skills` | Lista las skills que la sesión reconoce, incluidas las incorporadas | Lab 02, para ver si tienes `/code-review` |
| `/diff` | Revisa los cambios antes de confirmar | Labs 01 y 04 |
| `/context` | Muestra qué ocupa la ventana de contexto | Al cerrar cada lab |
| `/list-agents` | Lista los subagentes que la sesión reconoce, si tu instalación lo trae | Lab 01, al comprobar el primero |
| `/exit` | Cierra la sesión, para recoger el primer archivo de `.claude/agents/` | Lab 01, solo si hace falta |

`/list-agents` lista los subagentes, pero no es el equivalente de `/skills` o
`/hooks`: lista también otras sesiones y solo está donde la mensajería entre
sesiones está habilitada. Lo que siempre funciona es invocar al agente.

## Tres Formas de Delegar, y qué Contexto Lleva Cada Una

| Forma | Qué contexto lleva | Qué devuelve | Cuándo sirve |
|---|---|---|---|
| Pedirlo en tu hilo | Todo: la conversación entera | La respuesta, en el hilo | Cuando quieres seguir dirigiendo turno a turno |
| `/subtask` o `/fork` | Todo: hereda tu conversación | El resultado vuelve al hilo | Continuar algo que ya empezaste, sin gastar tu ventana |
| Subagente de `.claude/agents/` | Tu `CLAUDE.md` y el repositorio; **no** tu conversación | Solo su resumen final | Un juicio que no sepa cómo llegaste ahí |

La consecuencia práctica: el que hereda tu conversación también hereda tus
supuestos, así que su acuerdo vale menos como segunda opinión.

## Qué Carga un Subagente al Arrancar

| Sí carga | No carga |
|---|---|
| El cuerpo de su propio archivo, que es su oficio | Tu conversación |
| La jerarquía de `CLAUDE.md` del proyecto | Los archivos que Claude ya leyó en tu hilo |
| Una foto del estado del repositorio | Lo que otro subagente encontró antes |

Por eso, si quieres que vea un informe anterior, alguien tiene que dejarlo en
disco: de un subagente solo vuelve el resumen, y lo que no se guarda se
pierde.

Lo que sí lo acompaña son tus hooks: los dos que configuraste en la sesión 8
se disparan igual cuando el que llama a la herramienta es un subagente.

## La Escalera de Autoridad

| Agente | Qué puede | Qué no puede |
|---|---|---|
| `refactorizador` | Leer, buscar, editar, escribir, ejecutar | Confirmar en git, cambiar el contrato, tocar tests |
| `revisor-de-codigo` | Leer y buscar | Editar, escribir, ejecutar |
| `auditor-de-seguridad` | Leer y buscar, igual que el revisor | Lo mismo que el revisor |
| `consolidador-de-hallazgos` | Leer, buscar y ejecutar | Editar y escribir **con herramientas de edición**; ejecutar deja abierto el camino del shell |

Dos cosas que conviene no confundir. La primera: **si no declaras
herramientas, el agente hereda todas las tuyas**. La segunda: recortar
herramientas no es lo mismo que negar un permiso. Son dos capas distintas, y
la de permisos tiene además una regla propia para esto —`Agent(<nombre>)` en
tu lista `deny` impide usar un subagente concreto sin tocar su archivo—.

## Skill, Hook o Subagente

| Lo que necesitas | Qué usar | Por qué |
|---|---|---|
| Un procedimiento repetido, con tu contexto delante | Skill | Se invoca en tu hilo y el resultado se queda aquí para dirigirlo |
| Que algo ocurra siempre, decida lo que decida Claude | Hook | Es la única capa que se ejecuta pase lo que pase |
| Un juicio que no conozca tu conversación | Subagente | Su valor está justo en no saber cómo llegaste ahí |
| Terminar algo que ya empezaste, sin gastar tu ventana | `/subtask` | Delega con tu contexto completo y devuelve el resultado |

## Cómo se Tría un Hallazgo

| Clase | Qué exige | Qué se escribe |
|---|---|---|
| Aceptado | Una comprobación que lo confirme | Qué se ejecutó y qué salió |
| Rechazado | La decisión que lo vuelve ruido, con su archivo | Dónde está escrita, no "no hace falta" |
| Pendiente | Nada lo confirma ni lo desmiente todavía | Qué faltaría para decidirlo |

## Si Algo Falla

| Señal | Causa habitual |
|---|---|
| El agente no responde a su nombre | Es el primer archivo de `.claude/agents/` y el directorio no existía al arrancar: cierra con `/exit` y vuelve a abrir |
| Devuelve buenas prácticas genéricas | Le falta oficio en el archivo, no contexto: escribe contra qué revisa y en qué orden |
| Hace más de lo que le pediste | Le declaraste de más, o no le declaraste nada y heredó todo |
| No puede leer un archivo que necesita | Mira `/permissions`: una regla `deny` de la sesión 4 es la primera candidata |
| Su informe se perdió al seguir trabajando | Solo vuelve el resumen: guárdalo en `evidencias/` antes de continuar |
| Los tres veredictos coinciden en todo | Resultado válido. Anota cuál llegó habiendo leído el relato del autor, que es lo que este lab mide |
