# Plan del Curso

## Resumen

Curso práctico de Claude Code para desarrolladores. 20 horas distribuidas en 10 sesiones de 2 horas.

El objetivo es dominar la herramienta, no construir una API. A lo largo del curso construyes una API como medio para practicar: lo que se aprende es cómo trabajar con el agente, no el código que resulta.

## El eje del curso

> Un agente rinde en proporción a **lo limpio que esté su contexto** y a **los medios que tenga para verificarse**.

Todo lo demás son técnicas al servicio de una de esas dos cosas. La ventana de contexto se llena rápido y el rendimiento cae a medida que se llena; sin una comprobación que el agente pueda ejecutar, se detiene cuando le parece que terminó.

### La escalera de verificación

El mismo concepto en cuatro grados de automatización, uno por bloque:

| Nivel | Mecanismo | Sesión |
|---|---|---|
| En el prompt | "ejecuta el test y arregla lo que falle" | 1 |
| En la sesión | `/goal` con condición comprobable | 4 |
| Puerta determinista | Stop hook que bloquea el fin de turno | 9 |
| Segunda opinión | Subagente nombrado en contexto aislado | 10 |

Cada sesión trabaja además **un modo de fallo**. Los fallos deterministas se
provocan; los que dependen del modelo se observan como experimentos y se
comparan con evidencia.

## Entorno

El entorno estándar es una terminal Linux. En Windows, el flujo es WSL 2 con Ubuntu 24.04, y los comandos se ejecutan desde Ubuntu, no desde PowerShell ni CMD.

| Sistema | Docker | Python |
|---|---|---|
| Linux | Docker Engine | uv |
| Windows | WSL 2 + Ubuntu 24.04; Docker Engine dentro de WSL, o Docker Desktop según el equipo | uv dentro de WSL |
| macOS | Docker Desktop | uv |

La preparación está documentada en [Instalación del Entorno](docs/instalacion-entorno.md).

## Al finalizar el curso podrás

- Formular tareas con criterio de terminación verificable por el propio agente.
- Reconocer un criterio que el agente puede falsear.
- Escribir un `CLAUDE.md` útil, y podarlo cuando deja de funcionar.
- Diagnosticar y limpiar un contexto degradado.
- Explorar y planificar antes de implementar, y corregir el plan.
- Llevar una feature de rama a pull request con revisión asistida.
- Recuperar una sesión que se torció, sin empezar de cero.
- Reproducir un fallo con un test y depurarlo con evidencia.
- Crear skills invocables como comandos y distinguirlos de memoria, hooks y subagentes.
- Configurar hooks, permisos y sandbox.
- Delegar en subagentes, conectar servidores MCP y ejecutar en CI.

## Estructura General

| Bloque | Sesiones | Horas | Enfoque |
|---|---:|---:|---|
| Modelo mental y proyecto | 1–3 | 6h | Especificar, dar contexto, gestionar el contexto |
| El ciclo de trabajo | 4–6 | 6h | Explorar, planificar, implementar, entregar y recuperarse |
| Automatizar y escalar | 7–10 | 8h | Reproducir y depurar, extender, automatizar, delegar |

Cada bloque cierra con una versión comprobable del proyecto integrador.

## Proyecto Integrador

Cada estudiante construye su propio `curso-claude-code-api` a lo largo del curso. Es el resultado acumulado de las sesiones y el hilo conductor técnico. Está descrito en [proyecto-integrador](proyecto-integrador/README.md).

## Desafíos Opcionales

Cada sesión incluye un desafío opcional para profundizar fuera del horario de clase. No se entregan y no son requisito para avanzar.

## Evaluación Formativa

No hay calificación numérica. Cada sesión produce evidencia de proceso y el
curso termina con un proyecto de transferencia evaluado mediante rúbrica. La
evaluación se describe en [Evaluación y Portafolio](docs/evaluacion.md).

## Compatibilidad y Seguridad

Claude Code cambia con frecuencia. La versión, los planes y las alternativas por
capacidad se mantienen en [Compatibilidad](docs/compatibilidad.md). Las reglas
que se aplican desde la primera sesión están en [Seguridad](docs/seguridad.md).

## Sesiones

### [Sesión 1: Especificar y Verificar](sesiones/sesion-01-especificar-y-verificar/README.md)

Qué hace distinto a un agente de codificación. El bucle leer-editar-ejecutar-comprobar. Contexto, alcance y criterio de terminación. Criterios que el agente puede falsear. Preguntar al código ajeno y exigir la fuente. Qué modelo estás usando y por qué el consumo importa desde el primer día.

**Comandos nuevos:** `claude`, `claude -p`, `/help`, `/status`, `/diff`, `/model`

### Sesión 2: Fundar el Proyecto y su Memoria _(aún no publicada)_

Arranque de la API con FastAPI y PostgreSQL sobre Compose. `/init` y la jerarquía de memoria. Qué entra y qué no en un `CLAUDE.md`, y cómo podarlo cuando se vuelve tan largo que el agente lo ignora.

**Comandos nuevos:** `/init`, `/memory`, `/context`, `/config`

### Sesión 3: Administrar el Contexto _(aún no publicada)_

CRUD completo del proyecto. Ver qué ocupa el contexto y por qué el rendimiento cae. Limpiar, resumir y meter información sin ensuciar el hilo.

**Comandos nuevos:** `/clear`, `/compact`, `/autocompact`, `/btw`, `@`, piping con `cat archivo | claude`

### Sesión 4: Explorar y Planificar _(aún no publicada)_

Plan mode: separar la investigación de la ejecución. Leer y corregir un plan antes de aprobarlo. Dejar que Claude te entreviste para escribir una especificación. `/goal` como criterio a nivel de sesión. Medir modelo y esfuerzo sobre una tarea real: `opusplan`, coste comparado y el sobre-razonamiento del esfuerzo máximo.

**Comandos nuevos:** `/plan`, `Shift+Tab`, `Ctrl+G`, `/goal`, `/effort`, `/advisor`, `/cost`

### Sesión 5: Implementar y Entregar _(aún no publicada)_

Cierre del ciclo explorar → planificar → implementar → entregar. Commits acotados, ramas, pull request y revisión asistida de un diff.

**Comandos nuevos:** `/add-dir`, `/cd`, `/install-github-app`

### Sesión 6: Interrumpir y Recuperar _(aún no publicada)_

Qué hacer cuando la sesión va mal: interrumpir, deshacer, ramificar la conversación y saber cuándo conviene empezar de cero en lugar de seguir corrigiendo. Retomar trabajo entre días.

**Comandos nuevos:** `Esc`, `/rewind`, `/branch`, `/resume`, `--continue`, `/recap`, `/export`, `/copy`

### Sesión 7: Reproducir y Depurar _(aún no publicada)_

TDD asistido. Reproducir un fallo con un test antes de corregirlo. Exigir evidencia en lugar de afirmaciones. Iteración visual con capturas sobre la página estática.

**Comandos nuevos:** `/code-review`, pegado de imágenes

### Sesión 8: Extender con Skills _(aún no publicada)_

`claude --help` como fuente de verdad. Convertir un prompt repetido en un skill
invocable como comando. Skills bajo demanda frente al `CLAUDE.md` que se carga
siempre, y evaluación de workflows reutilizables.

**Comandos nuevos:** `/skills`, `/reload-skills`, `/plugin`, `/doctor`, subcomandos de `claude`

### Sesión 9: Acotar Permisos y Automatizar _(aún no publicada)_

Permisos, auto mode y sandbox. Hooks como garantía determinista frente a instrucciones que son solo consejo. Stop hook: la puerta que bloquea el cierre sin verificar, y su límite. Qué no delegar nunca.

**Comandos nuevos:** `/permissions`, `/hooks`, `/sandbox`; Auto mode como ruta opcional

### Sesión 10: Delegar y Ejecutar sin Interfaz _(aún no publicada)_

Subagentes nombrados en contexto aislado frente a forks que heredan la
conversación. Evaluación segura de servidores MCP. Modo no interactivo acotado,
CI y cierre con análisis de las evidencias del curso.

**Comandos nuevos:** `/subtask`, `/fork`, `/mcp`, `/insights`, `/team-onboarding`, `claude -p --output-format json`
