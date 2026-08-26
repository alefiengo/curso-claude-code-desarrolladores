# Compatibilidad de Claude Code

Claude Code cambia con frecuencia. Esta página separa lo obligatorio de lo
opcional para que una diferencia de plan o versión no bloquee el curso.

## Línea Base

- Base general revisada contra **Claude Code 2.1.233** y la documentación
  disponible el **17 de agosto de 2026**.
- Las sesiones 1 y 2, ya reconstruidas, se volvieron a verificar con **Claude
  Code 2.1.246** y la documentación disponible el **26 de agosto de 2026**. La
  versión declarada en cada sesión manda sobre esta referencia general.
- Ejecuta `claude --version`, `claude doctor` y `claude --help` antes de la sesión 1.
- Dentro de Claude Code, `/help` es la fuente de verdad de tu instalación.
- Actualiza antes del curso. No actualices entre dos pasos de un mismo lab.

Anota tu versión antes de empezar. Si un comando no existe en tu instalación,
aplica la alternativa que indica la sesión y abre un issue con tu versión y tu
sistema operativo.

## Cuenta y Proveedor

Claude Code admite autenticación mediante suscripción de Claude, Anthropic API
y proveedores empresariales compatibles. El curso no presupone que todas las
cuentas tengan las mismas capacidades.

| Capacidad | Ruta común | Alternativa del curso |
|---|---|---|
| Sesiones interactivas, archivos y Bash | Pro, Max, Team, Enterprise o API | Obligatoria |
| Modelos concretos | Depende del plan y proveedor | Usar `default` y registrar el activo |
| Contexto de 1M | Depende del plan y créditos | No es requisito |
| Auto mode | Pro, Max y Team: es el modo de arranque | Cambiar a Manual con `Shift+Tab`, o `acceptEdits` / `dontAsk` |
| GitHub App y funciones cloud | Dependen de cuenta y GitHub | Flujo local con `git diff` y `git format-patch` |
| Revisión cloud avanzada | Depende de disponibilidad y créditos | Revisión local con subagente nombrado |

## Funciones Sensibles a la Versión

| Función | Comprobación | Alternativa |
|---|---|---|
| `/autocompact` | Presente en 2.1.233, con `--autocompact` como equivalente al arrancar | Usar `/context` y `/compact` manualmente |
| `/subtask` | Buscarla en `/help` | Delegar en un subagente nombrado |
| `/goal` | Buscarla en `/help` | Trabajar en turnos con el mismo criterio de terminación |
| `/reload-skills` | Buscarla en `/help` | Reiniciar la sesión |
| `/code-review` | Buscarla en `/help` | Pedir revisión del diff con rúbrica explícita |
| `/cost` | Buscarla en `/help` | En 2.1.233 es alias de `/usage`, igual que `/stats` |

Los subagentes nombrados se crean escribiendo el archivo en `.claude/agents/`.
En 2.1.233, `/agents` existe pero está marcado como retirado y solo remite a esa
carpeta: el material no depende de él en ninguna sesión.

No se usan como requisito comandos que solo existan en una instalación local o
en un plugin no documentado. Si el curso crea un comando propio, el material lo
etiqueta como **creado en el lab**.

## Modelos y Nivel de Esfuerzo

El curso se hace con `default`. Esta sección es de consulta: no hace falta para
seguir ninguna sesión, y la sesión 4 _(aún no publicada)_
mide la diferencia sobre una tarea real.

Comprueba cuál tienes activo con `/status`; se cambia con `/model`.

| Alias | Para qué |
|---|---|
| `haiku` | Tareas mecánicas y repetitivas |
| `sonnet` | Trabajo habitual |
| `opus` | Tareas difíciles y razonamiento largo |
| `fable` | Tareas más largas que una sesión. No es el modelo por defecto |
| `best` | El más capaz al que llegue tu cuenta |
| `opusplan` | Planifica con el modelo fuerte, ejecuta con el rápido |
| `default` | **No es un modelo**: quita el override y vuelve al de tu cuenta |

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

**`ultrathink` sí; `piensa más` no.** Escribir `ultrathink` en cualquier parte
del prompt pide más razonamiento **solo en ese turno**, sin tocar el nivel de la
sesión. Es una palabra que Claude Code reconoce y convierte en una instrucción.
Otras frases que circulan —"think", "think hard", "think more"— **no** son
palabras clave: viajan como texto normal del prompt.

**Consumo.** Modelo caro y esfuerzo alto gastan más cuota y tardan más. El propio
Claude Code advierte que el esfuerzo máximo puede derivar en sobre-razonamiento.
Trabaja con el valor por defecto salvo que tengas un motivo, o llegarás a mitad
del curso sin cuota.

## Editor

**La sesión 1 se hace entera en la terminal**, sin editor: solo necesitas poder
abrir una segunda ventana o pestaña de tu terminal. Desde la sesión 2 el curso
usa **VS Code con su terminal integrada**, y Claude Code se ejecuta como un
comando más dentro de ella.

Todos los labs funcionan igual en cualquier otro editor. Lo único que se da por
supuesto a partir de la sesión 2 es que puedes abrir un archivo y dividir la
terminal en dos paneles.

Aparte de eso existe la integración con el editor, que conecta la sesión con el
IDE abierto. `claude --help` la documenta como `--ide`: *"Automatically connect
to IDE on startup if exactly one valid IDE is available"*. Busca `/ide` en
`/help` para la forma equivalente dentro de una sesión.

**Es opcional y ningún laboratorio depende de ella.** Si la usas, sigue
registrando la evidencia con los comandos del lab: la integración cambia dónde
ves el diff, no lo que hay que verificar.

## Comprobación Previa

Guarda la salida en `evidencias/preflight.txt`:

```bash
mkdir -p evidencias
{
  claude --version
  claude doctor
  docker --version
  uv --version
  git --version
} | tee evidencias/preflight.txt
```

Dentro de Claude Code comprueba, sin cambiar nada:

```text
/help
/status
```

Si una capacidad opcional no existe, anótala. No impide empezar.
