# Compatibilidad de Claude Code

Claude Code cambia con frecuencia. Esta página separa lo obligatorio de lo
opcional para que una diferencia de plan o versión no bloquee el curso.

## Línea Base

- Material revisado contra **Claude Code 2.1.233** y la documentación disponible
  el **17 de agosto de 2026**.
- Ejecuta `claude --version`, `claude doctor` y `claude --help` antes de la sesión 1.
- Dentro de Claude Code, `/help` es la fuente de verdad de tu instalación.
- Actualiza antes del curso. No actualices entre dos pasos de un mismo lab.

El instructor registra al comienzo de cada cohorte la versión usada. Si un
comando no está disponible, aplica la alternativa indicada en la sesión y abre
un issue con versión y sistema operativo.

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

## Editor

El curso usa **VS Code con su terminal integrada**: Claude Code se ejecuta como
un comando más de la terminal. Todos los labs funcionan igual en cualquier otro
editor, o sin editor: lo único que se da por supuesto es que puedes abrir un
archivo y dividir la terminal en dos paneles.

Aparte de eso existe la integración con el editor, que conecta la sesión con el
IDE abierto. `claude --help` la documenta como `--ide`: *"Automatically connect
to IDE on startup if exactly one valid IDE is available"*. Busca `/ide` en
`/help` para la forma equivalente dentro de una sesión.

**Es opcional y ningún laboratorio depende de ella.** Si la usas, sigue
registrando la evidencia con los comandos del lab: la integración cambia dónde
ves el diff, no lo que hay que verificar.

## Preflight de la Cohorte

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
