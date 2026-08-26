# Plan del Curso

## Resumen

Curso práctico de Claude Code para desarrolladores. 20 horas distribuidas en 10 sesiones de 2 horas.

El objetivo es dominar la herramienta, no construir una API. Construyes una API
porque las herramientas necesitan un sitio donde doler: un skill se entiende
cuando te ahorra la quinta repetición, y un hook cuando llevas cuatro sesiones
olvidando el lint.

Cada sesión hace avanzar el proyecto **y** te deja una herramienta nueva en tu
`.claude/`. Al terminar tienes las dos cosas: una API funcionando y un conjunto
de herramientas que te llevas a tu trabajo el lunes siguiente.

## El eje del curso

> Un agente rinde en proporción a **lo limpio que esté su contexto** y a **los medios que tenga para verificarse**.

Todo lo demás son técnicas al servicio de una de esas dos cosas. La ventana de contexto se llena rápido y el rendimiento cae a medida que se llena; sin una comprobación que el agente pueda ejecutar, se detiene cuando le parece que terminó.

### La escalera de verificación

El mismo concepto en cuatro grados de automatización, uno por bloque:

El mismo criterio en cuatro grados. Lo que cambia es **quién decide** si se
cumplió, y cuánto puede reinterpretarlo el agente:

| Grado | Dónde vive el criterio | Quién decide | Sesión |
|---|---|---|---:|
| 1 | En el prompt | El modelo | 1 |
| 2 | En un script que tú ejecutas | Un código de salida | 5 |
| 3 | En un hook que se ejecuta solo | Un código de salida, sin que nadie lo pida | 6 |
| 4 | En otro agente, con contexto limpio | Alguien que no tiene tus supuestos | 9 |

El cuarto es el único que puede descubrir que **el criterio estaba mal**.

Cada sesión trabaja además **un modo de fallo**. Los deterministas se provocan;
los que dependen del modelo se observan como experimentos y se comparan con
evidencia.

## Entorno

El entorno estándar es una terminal Linux. En Windows, el flujo es WSL 2 con Ubuntu 24.04, y los comandos se ejecutan desde Ubuntu, no desde PowerShell ni CMD.

| Sistema | Docker | Python |
|---|---|---|
| Linux | Docker Engine | uv |
| Windows | WSL 2 + Ubuntu 24.04; Docker Engine dentro de WSL, o Docker Desktop según el equipo | uv dentro de WSL |
| macOS | Docker Desktop | uv |

La preparación está documentada en [Instalación del Entorno](docs/instalacion-entorno.md).

## Al finalizar el curso podrás

Trabajar con el agente:

- Formular tareas con un criterio de terminación que el propio agente pueda
  comprobar, y reconocer uno que puede falsear.
- Administrar el contexto: saber qué carga, qué cuesta y cuándo limpiarlo.
- Planificar antes de implementar, y rechazar un plan con evidencia.
- Reproducir un fallo con un test antes de corregirlo.

Construir tus herramientas:

- Escribir un `CLAUDE.md` útil, y podarlo cuando deja de funcionar.
- Crear skills invocables, y sacar a un script lo que no debe variar.
- Poner hooks donde algo tiene que ocurrir siempre, o no poder ocurrir nunca.
- Conectar un servidor MCP, y decidir cuándo **no** conectarlo.
- Delegar en un subagente con contexto limpio.
- Acotar permisos, ejecutar sin persona delante y automatizar en CI.

Y el criterio que ordena todo lo anterior:

- Saber si algo va en `CLAUDE.md`, en un skill, en un hook o en un permiso.
- Podar lo que construiste cuando deja de pagar lo que cuesta.

## Estructura General

| Bloque | Sesiones | Horas | Qué construyes |
|---|---:|---:|---|
| Fundamentos y proyecto | 1–3 | 6h | El modelo mental, la memoria del proyecto y su diseño |
| Construir con herramientas propias | 4–6 | 6h | Los recursos de la API, tus primeros skills y hooks |
| Verificar, delegar y entregar | 7–10 | 8h | MCP, regresión, subagente, permisos y CI |

Así se reparten los 120 minutos de cada sesión:

| Bloque | Minutos |
|---|---:|
| Teoría: la herramienta de hoy y el concepto que la sostiene | 20-25 |
| Laboratorio 1: el trabajo de ingeniería | 45-50 |
| Laboratorio 2: construir la herramienta que ese trabajo pidió | 35-40 |
| Cierre, evidencia e integración en `main` | 10-15 |

Los dos laboratorios se encadenan: el primero produce el problema y el segundo lo
resuelve construyendo algo que reutilizas el resto del curso.

## Proyecto Integrador

Construyes tu propio `curso-claude-code-api` a lo largo del curso. Es el resultado acumulado de las sesiones y el hilo conductor técnico. Está descrito en [proyecto-integrador](proyecto-integrador/README.md).

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

Cada sesión hace avanzar la API **y** sale con una herramienta nueva para tu
`.claude/`. La herramienta no llega antes de tiempo: llega cuando el trabajo de
esa sesión la hace necesaria.

### [Sesión 1: Especificar y Verificar](sesiones/sesion-01-especificar-y-verificar/README.md)

Qué hace distinto a un agente de codificación. El bucle
leer-editar-ejecutar-comprobar. Contexto, alcance y criterio de terminación.
Criterios que el agente puede falsear. Preguntar al código ajeno y exigir la
fuente.

**Comandos nuevos:** `claude`, `claude -p`, `/help`, `/status`, `/diff`, `/model`

### [Sesión 2: Fundar el Proyecto y su Memoria](sesiones/sesion-02-fundar-el-proyecto/README.md)

Arranque de la API con FastAPI y PostgreSQL sobre Compose. Qué carga el agente al
empezar y qué cuesta. Qué entra y qué no en un `CLAUDE.md`, y cómo podarlo.

**Sales con:** el `CLAUDE.md` de tu proyecto.
**Comandos nuevos:** `/init`, `/memory`, `/context`, `/config`

### Sesión 3: Diseñar antes de Implementar _(aún no publicada)_

Esquema, migraciones y el catálogo de estados. Separar la investigación de la
ejecución: leer un plan, rechazarlo con evidencia y corregirlo antes de que se
escriba una línea de código.

**Sales con:** un plan revisable, y la decisión de dónde vive el seed.
**Comandos nuevos:** `/plan`, `Shift+Tab`, `Ctrl+G`, `/goal`

### Sesión 4: El Primer Recurso _(aún no publicada)_

Proyectos, de punta a punta: contrato, tests en rojo, implementación y auditoría.
Al terminar ves el patrón, y lo conviertes en un comando propio.

**Sales con:** tu primer skill.
**Comandos nuevos:** `/skills`, `/reload-skills`

### Sesión 5: El Recurso con Relaciones _(aún no publicada)_

Tareas: claves foráneas, filtros combinados y orden estable. El skill de la
sesión anterior te andamia el recurso, y descubres que su resultado varía entre
ejecuciones.

**Sales con:** el skill con un script dentro, que ya no varía.
**Comandos nuevos:** `/plugin`, `/doctor`

### Sesión 6: Que No Se Te Olvide Nada _(aún no publicada)_

Cerrar la v1. Qué es un hook, qué eventos existen y en qué se diferencia de una
instrucción: lo que persuade frente a lo que impide.

**Sales con:** dos hooks — lint automático y una puerta que impide cerrar en rojo.
**Comandos nuevos:** `/hooks`

### Sesión 7: Probar contra la Base Real _(aún no publicada)_

Los tests están en verde, pero ¿qué hay en la tabla? Conectar el agente a
PostgreSQL y encontrar lo que la suite no ve. Qué amplía un MCP y por qué se
evalúa como una dependencia de producción.

**Sales con:** un servidor MCP conectado, y el criterio para decidir sobre otro.
**Comandos nuevos:** `/mcp`, `claude mcp add`

### Sesión 8: Cuando Algo se Rompe _(aún no publicada)_

TDD asistido sobre un fallo real. Reproducir antes de corregir, distinguir el
rojo correcto del que no vale, y exigir evidencia en lugar de explicaciones.

**Sales con:** un skill que convierte cualquier fallo en un test permanente.
**Comandos nuevos:** `/review`, pegado de imágenes

### Sesión 9: Dejar de Fiarte de Ti Mismo _(aún no publicada)_

Revisar tu propio código no funciona. Qué contexto hereda cada forma de delegar,
por qué una copia de tu conversación no es una segunda opinión, y qué se le
entrega a un revisor.

**Sales con:** un subagente revisor de solo lectura.
**Comandos nuevos:** `/agents`, `/fork`

### Sesión 10: Entregar, Automatizar y Podar _(aún no publicada)_

La entrega: pull request con su evidencia. La automatización: permisos mínimos,
sandbox y la misma verificación corriendo sin nadie delante. Y el cierre que
ninguna formación enseña: **qué quitar** de todo lo que construiste.

**Sales con:** permisos acotados, un workflow de CI y un `.claude/` podado.
**Comandos nuevos:** `/permissions`, `/sandbox`, `/usage`, `claude -p --output-format json`
