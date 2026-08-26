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

| Lab | Tema | Qué descubres |
|---|---|---|
| [01 – Bucle de verificación](labs/01-bucle-de-verificacion/README.md) | Leer, editar, ejecutar, comprobar | Sin una condición de terminación, el agente para cuando le parece |
| [02 – Criterio falseable](labs/02-criterio-falseable/README.md) | Contexto, alcance y criterio | "Los tests pasan" puede ser cierto y no significar nada |
| [03 – Preguntar al código ajeno](labs/03-preguntar-al-codigo/README.md) | Entender un repositorio desconocido | Cuánto cambia una respuesta cuando exiges la fuente |

Los resultados que dependen del modelo se registran como experimento. La sesión
evalúa la calidad de la evidencia, no que Claude responda igual para todos.

Antes del primer lab:

```bash
mkdir -p ~/curso-claude/evidencias
```

Esta es la única sesión que trabaja fuera del proyecto, porque todavía no existe
la API. Vas a usar dos sitios distintos dentro de `~/curso-claude/`:

```text
~/curso-claude/
├── evidencias/     tu archivo s01.md. Se conserva.
└── sesion-01/      una carpeta por lab. Se borra al terminar la sesión.
    ├── lab-01/
    ├── lab-02/
    └── lab-03/
```

Cada lab crea su propia carpeta en su primer paso; no tienes que prepararlas
ahora. Lo único que se guarda de hoy es `evidencias/s01.md`.

Desde la sesión 2 esto cambia: el proyecto `curso-claude-code-api` trae su propia
carpeta `evidencias/` y ahí se guarda lo de cada sesión. Lo de hoy se queda
donde está: esta sesión trabaja fuera del proyecto y su evidencia también.

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

Esta sesión trabaja la segunda mitad. El contexto llega en la sesión 2.

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
eso los laboratorios te dicen *qué debe haber ocurrido* en lugar de qué texto
vas a leer: cuando algo depende del modelo, cualquiera de los resultados
posibles es válido, siempre que registres cuál te tocó.

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
|---|---|---|---:|
| **En el prompt** | **"ejecuta el test y arregla lo que falle"** | **Evidencia producida por el agente** | **1** |
| En un script | Un archivo que ejecutas tú | Un código de salida, que no se reinterpreta | 5 |
| En un hook | El mismo script, disparado solo | Lo anterior, sin que nadie se acuerde de pedirlo | 6 |
| En otro agente | Un revisor con contexto limpio | Puede encontrar que el criterio estaba mal | 9 |

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

Los seis modos, el clasificador y el sandbox se ven en la sesión 10.

### Qué modelo estás usando

Comprueba con `/status` cuál tienes activo. Se cambia con `/model`.

**El curso se hace con `default`**, que no es un modelo: quita cualquier override
y te deja el de tu cuenta. No es prudencia, es lo que hace comparables las
evidencias entre compañeros y lo que evita quedarte sin cuota a mitad del curso. Si
cambias de modelo, anótalo en tu evidencia.

Hoy basta con eso: saber qué estás usando y no dispararlo sin motivo. La tabla de
alias, los niveles de esfuerzo y la palabra `ultrathink` están en
[compatibilidad](../../docs/compatibilidad.md#modelos-y-nivel-de-esfuerzo), para
consultarlos cuando los necesites.

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
versión, que puede no ser la tuya. Es una regla que vas a aplicar en las diez
sesiones: nada sobre la herramienta se da por sabido sin comprobarlo.

## Preparación para la Siguiente Sesión

La sesión 2 crea la API del curso y escribe su `CLAUDE.md`. Necesitas:

```bash
docker pull postgres:18-alpine
docker run --rm hello-world
uv --version
```
