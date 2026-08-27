# Glosario

Los términos que el curso usa con un significado preciso. Cada uno se define
también la primera vez que aparece en una sesión; esta página los reúne para
consultarlos en cualquier momento.

## Trabajo con el agente

### Criterio de terminación

La condición que decide si una tarea está hecha. Sirve cuando el propio agente
puede comprobarla: un comando que ejecutar, una salida exacta que comparar. "Que
funcione bien" no es un criterio; "termina cuando `pytest -q` pase con 5 tests"
sí lo es.

Se introduce en la [sesión 1](../sesiones/sesion-01-especificar-y-verificar/README.md).

### Criterio manipulable

Un criterio de terminación que el agente puede cumplir sin hacer el trabajo,
normalmente cambiando aquello con lo que se le mide. Si la condición es "que los
tests pasen" y el agente puede editar los tests, la condición no garantiza nada.

Un criterio también puede fallar por **irrelevante**: si ningún test cubre la
función que cambiaste, que la suite pase no dice nada sobre ella.

### Comprobación

Lo que decide si el trabajo está bien: casi siempre un test, a veces un comando
cuyo código de salida importa. El curso evita llamarla "oráculo".

Una comprobación es **independiente** cuando el agente que hizo el trabajo no
puede modificarla.

### Escalera de verificación

El mismo criterio de terminación, en cuatro grados de automatización. Lo que
cambia no es la idea, es **quién decide** si se cumplió y cuánto dura la
configuración:

| Grado | Dónde vive el criterio | Sesión |
|---|---|---:|
| En el prompt | "ejecuta el test y arregla lo que falle" | 1 |
| En la sesión | `/goal`, con una condición comprobable | 4 |
| En un programa | Stop hook: un código de salida que no se reinterpreta | 9 |
| En otro agente | Un revisor con contexto limpio | 10 |

### Modo de fallo

La forma concreta en que algo sale mal. Cada laboratorio trabaja uno: no como
teoría, sino provocándolo o buscándolo para que lo reconozcas cuando te pase
fuera del curso.

### Preflight

La comprobación del entorno que haces **antes** de empezar: que Claude Code,
Docker, `uv` y Git están instalados y responden, y que tienes el material del
curso descargado. Se hace una vez, antes de la primera sesión, y su salida se
guarda como evidencia.

Está descrito en [instalación del entorno](instalacion-entorno.md).

### Evidencia frente a afirmación

Una afirmación es lo que el agente dice que ocurrió. Una evidencia es la salida
de un comando que puedes volver a ejecutar. El curso pide siempre la segunda.

## Contexto

### Ventana de contexto

Todo lo que el modelo tiene delante en un momento dado: tu conversación, los
archivos leídos, las salidas de comandos, las memorias cargadas y las
definiciones de herramientas. Es finita y todo compite por ella.

### Contexto degradado

El estado en que la ventana está tan llena —o tan cargada de intentos fallidos y
salidas irrelevantes— que las respuestas empeoran. Se diagnostica con `/context`
y se corrige limpiando o compactando, no insistiendo.

Se trabaja en la sesión 3 _(aún no publicada)_.

### Compactar y limpiar

**Compactar** (`/compact`) sustituye la conversación por un resumen: conserva el
hilo, pierde el detalle. **Limpiar** (`/clear`) la descarta entera y empieza de
cero. Compactas cuando sigues en la misma tarea; limpias cuando cambias de tarea.

### Handoff

Una nota breve que deja el trabajo listo para retomarlo otro día, o para que lo
retome otra persona: rama y commit, estado de los tests, en qué ibas, qué queda
fuera de alcance, decisiones ya tomadas y el siguiente comando.

No es la conversación exportada. Una exportación completa obliga a quien la lee
a reconstruirlo todo; el handoff ya trae la conclusión.

Se trabaja en la sesión 6 _(aún no publicada)_.

## Verificación y pruebas

### Determinista

Que ocurre siempre igual, con los mismos pasos y el mismo resultado. Un montaje
de volumen mal escrito impide arrancar a PostgreSQL **siempre**: eso es
determinista y el material puede afirmarlo.

Lo que depende de cómo responda el modelo esta vez **no** lo es. El curso lo
presenta entonces como experimento: se anota lo que salió, y el laboratorio vale
con cualquiera de los resultados posibles.

### Test de caracterización

Un test que fija el comportamiento **actual** de un código antes de tocarlo, sin
juzgar si ese comportamiento es correcto. Sirve para detectar si un refactor lo
cambió sin querer.

### Regresión

Un fallo que ya estaba corregido y vuelve a aparecer. El test que lo reproduce
se conserva para siempre: es lo que impide que vuelva una tercera vez.

### Rojo y verde

**Rojo** es un test que falla; **verde**, uno que pasa. El curso pide el rojo
*antes* del arreglo, y que falle por la razón correcta: si falla al importar un
módulo que no existe (`errors`), no demuestra nada sobre el fallo que investigas.

### Invariante

Algo que debe cumplirse siempre, pase lo que pase por dentro. El contrato de la
API fija invariantes de comportamiento —qué código responde cada ruta, qué campos
devuelve— y deja libre cómo se implementan.

### Idempotente

Que ejecutarlo varias veces deja el mismo resultado que ejecutarlo una. La carga
inicial de datos debe serlo: si arrancar dos veces duplica el catálogo de
estados, no lo es.

## Configuración del agente

### Memoria de proyecto

`CLAUDE.md`: las instrucciones que escribes tú y que se cargan al inicio de cada
conversación. Viaja con el repositorio, así que la lee todo el equipo.

### Auto memory

Las notas que Claude escribe por su cuenta a partir de tus correcciones y
preferencias. Vive en tu máquina, fuera del repositorio, y su índice también
entra en contexto en cada sesión.

Las dos se revisan con `/memory`.

### Permiso, sandbox y hook

Tres capas distintas, que se confunden con facilidad:

| Capa | Qué hace | Qué no garantiza |
|---|---|---|
| Instrucción | Orienta la decisión del modelo | Nada: puede omitirse |
| Permiso | Decide qué herramienta puede intentarse | Que el efecto no se logre por otra vía |
| Sandbox | Acota qué puede alcanzar el proceso | Que lo permitido sea inofensivo |
| Hook | Ejecuta código tuyo en un evento | Que tu script sea correcto |

Una instrucción orienta. Un hook ejecuta una acción en un evento y, solo en los
eventos y condiciones que admiten bloqueo, puede impedir una operación. Los
permisos, el sandbox y los hooks se trabajan en la
sesión 9 _(aún no publicada)_.

### Skill

Un procedimiento que guardas para invocarlo como un comando. Se carga **solo
cuando lo llamas**, a diferencia de `CLAUDE.md`, que se carga siempre.

### Subagente

Otro agente al que delegas una tarea, con su propio contexto. Un **subagente
nombrado** empieza limpio, sin tu conversación; un **fork** hereda la tuya
entera, con tus supuestos incluidos, y por eso su acuerdo vale menos como
segunda opinión.
