# Sesión 1: Especificar y Verificar

## Objetivo

Formular tareas que Claude Code pueda comprobar por sí mismo, y reconocer cuándo un criterio no sirve.

## Duración

2 horas.

Así se reparten los 120 minutos de la clase:

| Bloque | Minutos |
|---|---:|
| Comprobar el entorno y repasar seguridad | 10 |
| Cómo trabaja el agente: conceptos de la sesión | 15 |
| [Lab 01 — Bucle de verificación](labs/01-bucle-de-verificacion/README.md) | 25 |
| [Lab 02 — Criterio falseable](labs/02-criterio-falseable/README.md) | 35 |
| [Lab 03 — Preguntar al código ajeno](labs/03-preguntar-al-codigo/README.md) | 25 |
| Guardar evidencias y cierre | 10 |

**Los tres laboratorios son el centro de la sesión**: ocupan 85 de los 120
minutos. Hazlos en orden; el Lab 02 da por hecho lo que trabajaste en el 01.

Si haces la sesión por tu cuenta, cuenta con algo más de tiempo: en clase
avanzas acompañado.

## Materiales

- [Instalación del entorno](../../docs/instalacion-entorno.md)
- [Seguridad desde la primera sesión](../../docs/seguridad.md)
- [Referencia rápida](referencia-rapida.md)
- [Desafío opcional](tareas/desafio-opcional.md)

## Laboratorios

| Lab | Tema | Riesgo o contraste |
|---|---|---|
| [01 – Bucle de verificación](labs/01-bucle-de-verificacion/README.md) | Leer, editar, ejecutar, comprobar | La misma tarea sin criterio: termina cuando le parece |
| [02 – Criterio falseable](labs/02-criterio-falseable/README.md) | Contexto, alcance y criterio | El agente modifica los tests para cumplir la condición |
| [03 – Preguntar al código ajeno](labs/03-preguntar-al-codigo/README.md) | Entender un repositorio desconocido | Una afirmación sin fuente que no se sostiene |

Los resultados que dependen del modelo se registran como experimento. La sesión
evalúa la calidad de la evidencia, no que Claude responda igual para todos.

Antes del primer lab:

```bash
mkdir -p ~/curso-claude/evidencias
```

Esta es la única sesión que trabaja fuera del proyecto: los tres laboratorios
usan carpetas desechables, porque todavía no existe la API. Por eso tu evidencia
de hoy vive en `~/curso-claude/evidencias/`. La sesión 2 crea
`curso-claude-code-api` con su propia carpeta `evidencias/`, y ahí se guarda todo
a partir de entonces; si quieres un portafolio único, la sesión 2 te indica dónde
copiar el archivo de hoy.

## Al finalizar esta sesión podrás

- Explicar qué hace un agente de codificación que un asistente de chat no hace.
- Escribir un prompt con contexto, alcance y criterio de terminación.
- Detectar un criterio que el agente puede falsear, y cerrarlo.
- Obtener información sobre un repositorio y verificarla contra el archivo.
- Revisar lo que cambió antes de aceptarlo.
- Saber qué modelo estás usando y por qué no conviene subirlo sin motivo.

## Conceptos Clave

### El eje del curso

> Un agente rinde en proporción a lo limpio que esté su contexto y a los medios que tenga para verificarse.

Esta sesión trabaja la segunda mitad. El contexto llega en la sesión 3.

### Bucle de verificación

```text
leer → editar → ejecutar → comprobar → responder
```

El paso que distingue a un agente es **ejecutar y leer la salida**. Un chat te devuelve texto y la comprobación la haces tú.

### Determinista y no determinista

Un proceso **reproducible** da la misma salida cada vez que le das la misma
entrada, **con el mismo código, las mismas dependencias y el mismo entorno**.
`pytest` lo es bajo esas condiciones: los mismos tests sobre el mismo código dan
el mismo resultado y el mismo código de salida. `ruff` lo es. Git lo es.

Esa letra pequeña importa. Un test que lee el reloj, la red, un número aleatorio
o el estado que dejó otro test **puede fallar sin que nadie haya tocado el
código**. Eso tiene nombre —un test *inestable*, o *flaky*— y es un defecto del
test, no del código que prueba. Cuando lo encuentres, la respuesta no es
repetirlo hasta que pase: es fijar lo que variaba.

El modelo **no**. La misma petición dos veces puede darte dos redacciones, dos
órdenes de pasos, o dos decisiones distintas sobre cómo estructurar un archivo.
No es un defecto que se vaya a arreglar: es cómo funciona.

De ahí salen las dos reglas que vas a usar durante todo el curso:

| Porque el modelo no es determinista | Porque las herramientas sí son reproducibles |
|---|---|
| No esperes un texto literal concreto | Sí puedes exigir un código de salida concreto |
| No verifiques comparando la respuesta | Verifica ejecutando el comando |
| Un resultado bueno una vez no está probado | Un comando en verde sigue verde mientras no cambien código, dependencias ni entorno |

Por eso el criterio de terminación es un **comando**, no una descripción. Y por
eso los laboratorios de este curso te dicen *qué debe haber ocurrido* en lugar
de qué texto vas a leer: cuando algo depende del modelo, el lab lo trata como
experimento y cualquiera de los resultados posibles es válido, siempre que
registres cuál te tocó.

La escalera de verificación de más abajo es, leída así, un recorrido desde lo
menos determinista —una instrucción en el prompt— hasta lo más determinista: un
script con código de salida que decide por ti.

### Las tres partes de un prompt

| Parte | Qué aporta |
|---|---|
| Contexto | Qué problema real existe y dónde |
| Alcance | Qué archivos entran y cuáles no |
| Criterio | Cómo sabrá que terminó |

### Criterio de terminación

Una condición que el agente puede comprobar por sí mismo.

| Sirve | No sirve |
|---|---|
| `python3 -m unittest discover -q` pasa | "que quede bien" |
| El comando imprime una salida exacta | "que sea profesional" |
| `timeit` baja de un umbral | "que siga buenas prácticas" |

La pregunta que resuelve casi todo: **¿cómo sabrá el agente que terminó?**

### Criterio falseable

Si le pides refactorizar y el criterio es "que los tests pasen", puede modificar los tests. Un criterio que el agente puede reescribir no es un criterio.

Se cierra acotando lo intocable:

```text
...manteniendo el comportamiento. No modifiques test_medidas.py.
Termina cuando los tests pasen sin haberlos tocado.
```

### Evidencia frente a afirmación

Pide la prueba, no la conclusión: la salida del comando, el archivo y la línea. Una afirmación sin fuente no es un hecho.

### Escalera de verificación

Lo de hoy es el primer peldaño. Los otros tres llegan más adelante:

| Nivel | Mecanismo | Qué garantiza | Sesión |
|---|---|---|---|
| **En el prompt** | **"ejecuta el test y arregla lo que falle"** | **Evidencia producida por el agente** | **1** |
| En la sesión | `/goal` | Evaluación probabilística: otro modelo revisa la condición | 4 |
| Puerta determinista | Stop hook | Un script decide. Con límite: tras varios bloqueos seguidos, Claude Code lo anula | 9 |
| Segunda opinión | Subagente revisor | Otro contexto juzga el resultado | 10 |

Ninguno es infalible, y no garantizan lo mismo. Cada sesión explica el límite del suyo.

### Permisos

En los planes Pro, Max y Team, una sesión **arranca en auto mode**: en lugar de
preguntarte, un segundo modelo —el clasificador— revisa cada acción y la aprueba
o la para. Vas a ver muchas menos preguntas de las que esperas, y eso no
significa que no esté pasando nada.

Hoy quieres verlo todo, así que trabaja en **modo Manual**, donde el agente se
detiene antes de cada edición y cada comando:

```bash
claude --permission-mode manual
```

`Shift+Tab` cicla entre modos dentro de la sesión, y la barra de estado dice en
cuál estás. El modo se llama **Manual** en la interfaz; su valor de
configuración es `default`, que es el que verás en los archivos y en los hooks.

Los seis modos, el clasificador y el sandbox se ven en la sesión 9.

### Qué modelo estás usando

Comprueba con `/status` cuál está activo. Se cambia con `/model`.

| Alias | Para qué |
|---|---|
| `haiku` | Tareas mecánicas y repetitivas |
| `sonnet` | Trabajo habitual |
| `opus` | Tareas difíciles y razonamiento largo |
| `fable` | Tareas más largas que una sesión. No es el modelo por defecto |
| `best` | El más capaz al que llegue tu cuenta |
| `opusplan` | Planifica con el modelo fuerte, ejecuta con el rápido |
| `default` | **No es un modelo**: quita el override y vuelve al de tu cuenta |

**El curso se hace con `default`.** No es una recomendación de prudencia: es lo
que hace comparables las evidencias entre compañeros y lo que evita gastar la
cuota en la sesión 3. Si cambias de modelo, anota cuál en tu evidencia, porque
la salida deja de ser comparable con la de los demás.

Los alias apuntan a la versión recomendada y **cambian con el tiempo**. Sobre la
API de Anthropic, hoy `opus` es Opus 5 y `sonnet` es Sonnet 5; sobre Bedrock,
Vertex o Foundry resuelven a versiones distintas. Los sufijos `[1m]` piden la
ventana de un millón de tokens: con `sonnet` ya resolviendo a Sonnet 5, que la
trae de serie, `sonnet[1m]` no cambia nada. Comprueba el tuyo con `/model`.

El **nivel de esfuerzo** (`low`, `medium`, `high`, `xhigh`, `max`) regula cuánto
razona antes de actuar. **El valor por defecto es `high`**, y la escala está
calibrada por modelo: el mismo nombre no significa lo mismo en dos modelos
distintos. Se ve con `/effort`.

El menú de `/effort` ofrece además `ultracode`, que **no es un nivel de
esfuerzo**: es un ajuste de Claude Code que manda `xhigh` al modelo y encima le
hace orquestar un flujo de trabajo por cada tarea de cierta entidad. Sabes que
existe; el curso no lo usa.

> **`ultrathink` sí; `piensa más` no.** Escribir `ultrathink` en cualquier parte
> del prompt pide más razonamiento **solo en ese turno**, sin tocar el nivel de
> la sesión. Es una palabra que Claude Code reconoce y convierte en una
> instrucción. Otras frases que circulan —"think", "think hard", "think more"—
> **no** son palabras clave: viajan como texto normal del prompt. Es un ejemplo
> temprano de la regla de la sesión 7: lo que se repite en internet no es lo que
> hace tu instalación.

> **Consumo.** Modelo caro y esfuerzo alto gastan más cuota y tardan más. El propio Claude Code advierte que el esfuerzo máximo puede derivar en sobre-razonamiento. Trabaja con el valor por defecto salvo que tengas un motivo, o llegarás a mitad del curso sin cuota.

Medir la diferencia y elegir con criterio es el trabajo de la **sesión 4**. Hoy solo necesitas saber qué estás usando y no dispararlo sin motivo.

## Comandos Nuevos

| Comando | Uso |
|---|---|
| `claude` | Sesión interactiva sobre el directorio actual |
| `claude -p "..."` | No interactivo: ejecuta, imprime y sale |
| `/help` | Comandos disponibles en tu versión |
| `/status` | Versión, modelo, cuenta y conectividad |
| `/diff` | Cambios sin confirmar y diffs por turno |
| `/model` | Ver y cambiar el modelo de la sesión |

## Validación General

```bash
cd ~/curso-claude/sesion-01
python3 -c "import sys; sys.path.insert(0,'lab-01'); import calc; print(calc.suma(2,3))"
cd lab-02 && python3 -m unittest discover -q && git diff --stat HEAD~1 HEAD
```

La sesión está completa si:

- [ ] `lab-01/calc.py` devuelve `5` para `suma(2, 3)`.
- [ ] `lab-02` tiene tests y todos pasan.
- [ ] El último commit de `lab-02` no modifica el archivo de tests.
- [ ] Tienes anotadas las respuestas del lab 03 con su archivo citado y su marca de verificación.
- [ ] Guardaste `~/curso-claude/evidencias/s01.md` con una decisión y su evidencia.

## Guardar la Evidencia

Antes de borrar nada, escribe tu evidencia de la sesión:

```bash
code ~/curso-claude/evidencias/s01.md
```

No es un resumen de lo que hiciste. Es **una decisión y lo que la respalda**:

```markdown
# Sesión 1

## Decisión
Reformulé "arregla los errores" como un criterio con salida exacta.

## Evidencia
El comando `python3 -c "...contar_por_sensor(ms)"` imprime
`{'cocina': 1, 'patio': 2}`, que es lo que el prompt exigía.

## Qué observé
En el paso 4 del Lab 01, sin criterio, el agente [sí / no] ejecutó una
comprobación por su cuenta.

## Lo que sigo sin poder garantizar
...
```

Ese archivo es tuyo y lo relees antes de la sesión 2. Es lo único de hoy que se
conserva.

## Limpieza

**Esto borra los tres laboratorios de hoy**, con sus repositorios Git y el clon
de `click`. Comprueba primero que tu evidencia está guardada fuera de esa
carpeta:

```bash
ls ~/curso-claude/evidencias/s01.md
```

Si el archivo aparece, ya puedes borrar el resto:

```bash
rm -rf ~/curso-claude/sesion-01
ls ~/curso-claude
```

Debe quedar `evidencias` y, si ya la clonaste, `material`. No hay nada más que
conservar: el trabajo de hoy era el aprendizaje, no el código.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) aplica el criterio de terminación a un problema de rendimiento y a código propio.

## Cierre

Checklist:

- [ ] Puedo explicar qué hace el agente que un chat no hace.
- [ ] Puedo escribir un prompt con contexto, alcance y criterio.
- [ ] Puedo detectar un criterio que el agente podría falsear.
- [ ] Pido la fuente antes de dar por buena una afirmación.
- [ ] Reviso el diff antes de aceptar.

Preguntas de repaso:

- ¿Qué paso del bucle distingue a un agente de un chat?
- ¿Por qué "que quede más limpio" no es un criterio?
- Si el criterio es "que los tests pasen", ¿qué puede salir mal?
- ¿Cuándo conviene **no** detallar cómo debe implementarse algo?
- ¿Qué harías si el agente cita un archivo que no dice lo que afirma?
- ¿Qué modelo está activo en tu sesión, y qué pasa si trabajas siempre con el más caro?

## Versión

Material probado con **Claude Code 2.1.233**. Comprueba la tuya con
`claude --version`.

Si un comando no existe o se comporta distinto, hacen falta **dos** fuentes, y
responden cosas distintas:

| Fuente | Qué responde |
|---|---|
| `claude --help`, `/help` | Si algo existe en **tu** instalación y con qué nombre |
| [La documentación oficial](https://code.claude.com/docs) | Qué significa, qué cambió y qué depende de tu plan |

Ninguna basta sola: la ayuda de la CLI no lista todos los flags ni explica
comportamientos que dependen del plan, y la documentación describe la última
versión, que puede no ser la tuya. Es la misma regla que la sesión 7 convierte
en método.

## Preparación para la Siguiente Sesión

La sesión 2 crea la API del curso y escribe su `CLAUDE.md`. Necesitas:

```bash
docker pull postgres:18-alpine
docker run --rm hello-world
uv --version
```
