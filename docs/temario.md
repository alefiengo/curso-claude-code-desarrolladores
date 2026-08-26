# Temario

Qué trabaja cada sesión y con qué sales de ella. El desarrollo completo está en
el [plan del curso](../curso.md) y en cada sesión.

Diez sesiones de dos horas. Cada una hace avanzar el proyecto **y** te deja una
herramienta nueva. La herramienta no llega antes de tiempo: llega cuando el
trabajo de esa sesión la hace necesaria.

---

## Bloque 1 — Fundamentos y proyecto

Sesiones 1 a 3. De qué es un agente a un proyecto con memoria propia y un diseño
que se revisó antes de escribirse.

### 1. Especificar y verificar

**El problema:** "arregla los errores" no es una tarea; es un deseo. Y sin forma
de comprobarlo, el agente decide por su cuenta cuándo ha terminado.

**Sales sabiendo:** escribir un prompt con contexto, alcance y criterio de
terminación; detectar un criterio que el agente puede falsear —modificar los
tests con los que se le mide— y cerrarlo; y exigir la fuente de cada afirmación
antes de darla por buena.

### 2. Fundar el proyecto y su memoria

**El problema:** un proyecto que solo arranca en la máquina donde se creó, y un
`CLAUDE.md` tan largo que el agente lo ignora.

**Sales sabiendo** qué carga el agente cuando abres una sesión y qué te cuesta;
qué entra en la memoria del proyecto y qué sobra porque el código ya lo dice.

**Sales con:** el `CLAUDE.md` de tu proyecto, podado hasta que cada línea se
gane el sitio.

### 3. Diseñar antes de implementar

**El problema:** un plan generado suena razonable aunque cite archivos que no
existen. Y una carga inicial de datos que vive en el sitio equivocado funciona en
tu máquina y en ninguna otra.

**Sales sabiendo** separar la investigación de la ejecución, y rechazar un plan
con evidencia del repositorio en lugar de aprobarlo porque suena bien.

**Sales con:** el esquema, las migraciones y un plan revisado antes de que se
escribiera una línea de código.

---

## Bloque 2 — Construir con herramientas propias

Sesiones 4 a 6. El trabajo repetido se convierte en comandos, y lo que no debe
olvidarse deja de depender de tu memoria.

### 4. El primer recurso

**El problema:** acabas de escribir un recurso completo —contrato, tests en rojo,
implementación, auditoría— y ves que el siguiente es exactamente igual.

**Sales sabiendo** qué es un skill, qué lleva dentro, y en qué se diferencia de
`CLAUDE.md`: uno se carga cuando lo llamas, el otro siempre.

**Sales con:** tu primer skill, y el recurso de proyectos funcionando.

### 5. El recurso con relaciones

**El problema:** el skill funciona, pero da un resultado distinto cada vez. Dos
ejecuciones del mismo verificador no se pueden comparar.

**Sales sabiendo** qué parte de una herramienta debe ser código y cuál puede
seguir siendo lenguaje natural.

**Sales con:** el skill con un script dentro, cuyo veredicto ya no varía; y las
tareas con sus relaciones, filtros y orden estable.

### 6. Que no se te olvide nada

**El problema:** llevas cuatro sesiones olvidando pasar el linter, y el agente da
por verificado lo que no ejecutó.

**Sales sabiendo** qué es un hook, cuándo se dispara cada evento y en qué se
diferencia de una instrucción: una persuade, el otro impide.

**Sales con:** dos hooks —uno que reacciona a cada edición y otro que impide
cerrar el turno en rojo— y la v1 cerrada.

---

## Bloque 3 — Verificar, delegar y entregar

Sesiones 7 a 10. Comprobar lo que los tests no ven, pedir una opinión que no sea
la tuya, y dejarlo funcionando sin nadie delante.

### 7. Probar contra la base real

**El problema:** la suite está en verde. ¿Y qué hay en la tabla? Un `DELETE` pudo
dejar filas huérfanas que ningún test mira.

**Sales sabiendo** qué es un servidor MCP, qué amplía —las herramientas del
agente **y** los datos que alcanza— y por qué se evalúa como una dependencia con
acceso a producción.

**Sales con:** un MCP conectado a tu base, y el criterio para decidir sobre otro
que no vas a conectar.

### 8. Cuando algo se rompe

**El problema:** ante un reporte, la primera explicación plausible basta para que
el agente proponga un arreglo. Si lo aceptas, corriges un síntoma.

**Sales sabiendo** reproducir antes de corregir, y distinguir el rojo que
demuestra el fallo del que solo dice que tu test está mal montado.

**Sales con:** un skill que convierte cualquier fallo en un test permanente.

### 9. Dejar de fiarte de ti mismo

**El problema:** revisas tu propio código y no ves nada. Y preguntarle a una copia
de tu conversación es preguntárselo a quien ya escribió la solución.

**Sales sabiendo** qué contexto hereda cada forma de delegar, y qué se le entrega
a un revisor: la especificación y el diff, nunca tu conclusión.

**Sales con:** un subagente revisor de solo lectura.

### 10. Entregar, automatizar y podar

**El problema:** en modo automático no hay nadie a quien preguntar, así que el
permiso se concedió antes o la ejecución falla. Y tu `.claude/` acumula nueve
sesiones de herramientas que nadie ha revisado.

**Sales sabiendo** acotar permisos y probarlos con el caso negativo, ejecutar sin
persona delante, y —lo que casi nadie enseña— **qué quitar**: qué skill no has
vuelto a invocar, qué hook te cuesta en cada edición, qué MCP ocupa contexto sin
usarse.

**Sales con:** permisos mínimos, un workflow de CI y un `.claude/` más pequeño
que al empezar la sesión.

---

## El hilo que une las diez

> Un agente rinde en proporción a **lo limpio que esté su contexto** y a **los
> medios que tenga para verificarse**.

Eso se ve en la **escalera de verificación**, que recorre el curso entero. El
criterio de "esto está terminado" va bajando desde el texto hasta el código:

| Peldaño | Dónde vive el criterio | Quién decide si se cumple | Sesión |
|---|---|---|---:|
| 1 | En el prompt | El modelo, releyendo la tarea | 1 |
| 2 | En un script que tú ejecutas | El código de salida | 5 |
| 3 | En un hook que corre solo | El código de salida, sin que lo pidas | 6 |
| 4 | En un revisor con contexto propio | Otro agente, sin tus supuestos | 9 |

Cada peldaño es más difícil de falsear que el anterior. El cuarto es el único que
puede descubrir que **el criterio estaba mal**. Ninguno es perfecto, y el curso
dice de cada uno **qué sigue sin garantizar**.

## La pregunta que aprendes a responder

Ante cualquier problema nuevo en tu trabajo:

| Si esto... | Entonces va en... |
|---|---|
| Debe pasar **siempre** | Un hook |
| Lo haces **cuando lo pides** | Un skill |
| **No puede** pasar nunca | Un permiso `deny` |
| El agente lo tiene que saber **siempre** | `CLAUDE.md` |
| Necesita **contexto limpio** | Un subagente |
| Necesita **datos de fuera** | Un servidor MCP |

Salir sabiendo responder esa tabla es lo que distingue a alguien que usa un
agente de alguien que lo acumula.

## Lo que construyes

Una API REST de gestión de tareas, con base de datos y una página mínima para
probarla. Crece contigo: al terminar tienes el proyecto funcionando y un
`.claude/` con las herramientas que construiste. Los detalles están en el
[proyecto integrador](../proyecto-integrador/README.md).

El proyecto es el andamio. Lo que te llevas al trabajo es el `.claude/`.

## Cómo se evalúa

**No hay notas.** Cada sesión cierra con una lista de comprobación y una
evidencia de proceso —una decisión y lo que la respalda—. El proyecto final usa
una rúbrica sin calificación, y los desafíos opcionales no se entregan.
