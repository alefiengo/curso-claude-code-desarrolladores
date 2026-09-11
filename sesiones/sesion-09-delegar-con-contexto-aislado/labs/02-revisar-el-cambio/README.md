# Lab 02: Revisar el Cambio

## Objetivo

Revisar el cambio capturado en el Lab 01, comprobar qué cubre la revisión y
dejar hallazgos y dudas concretas para el triaje.

## Por qué este lab

Ya tienes código modificado y un archivo `.diff` que muestra el antes y el
después. Ahora necesitas revisar ese cambio contra el contrato. Empieza con
la revisión disponible; solo delega otra tarea si queda una pregunta concreta
sin responder. No necesitas crear otro agente para repetir la misma revisión.

## Requisitos

- Lab 01 terminado: refactor sin confirmar y su captura
  `~/curso-claude/s09-revision/errores-api.diff`, con el commit base anotado.
- El código sigue igual que al generar la captura. Conserva el resultado de
  las comprobaciones del Lab 01, aunque alguna haya fallado.
- Si la captura está vacía porque la centralización ya estaba resuelta,
  registra esa condición y revisa el manejo de errores actual con la
  alternativa del paso 1.

## Ritmo de Trabajo

Este lab tiene 15 minutos:

| Min | Debe existir |
|---:|---|
| 0–3 | La captura contrastada con el código y la revisión elegida |
| 3–11 | La revisión terminada, con hallazgos o ausencia de ellos |
| 11–15 | Preguntas pendientes anotadas; una comprobación adicional solo si hace falta y cabe |

**Si necesitas cortar aquí:** conserva la captura y la revisión obtenida.
Si aún no terminó, completa la revisión antes del Lab 03. No dejes una
comprobación ejecutándose al cambiar de lab: espera su resultado o cancélala
y registra la duda como pendiente para el Lab 04.

## Paso a Paso

### 1. Revisar el cambio capturado

Pídele a Claude que compruebe que el código todavía coincide con la captura
del Lab 01, incluidos los archivos nuevos. Si cambió, detente y genera una
nueva captura identificada antes de revisar; conserva la anterior.

Consulta `/skills`. Si aparece `/code-review`, ejecuta:

```text
/code-review
```

Esta skill revisa el diff actual. El archivo guardado fija qué cambio esperas
que revise: comprueba que incluyó el módulo nuevo y sus conexiones. No le
pidas aplicar correcciones todavía.

Si la skill no está disponible, o la captura está vacía, usa este encargo en
el hilo:

```text
Revisa ~/curso-claude/s09-revision/errores-api.diff y los archivos necesarios
del repositorio contra docs/contrato-api.md y las reglas del proyecto.
Comprueba el manejo centralizado de errores de toda la API, incluidos tareas,
proyectos y validación: códigos de estado, cuerpos de respuesta y conexiones
con el módulo común. Si el diff está vacío, revisa el estado actual y acláralo.
No edites ni confirmes nada. Devuelve hallazgos con archivo, línea y evidencia,
y separa lo observado de lo que todavía falta comprobar.
```

Si usaste otra ruta para la captura, sustitúyela. El diff facilita comparar,
pero no sustituye al contrato ni al código que rodea las líneas modificadas.

### 2. Decidir si falta una comprobación

Lee el resultado: ¿cubrió códigos y cuerpos de respuesta en tareas,
proyectos y validación? ¿Revisó el módulo nuevo? ¿Señala pruebas o solo
afirma que funciona?

Si queda una duda concreta que puedas comprobar ahora, delega esa pregunta.
Sustituye el texto entre corchetes antes de enviarlo:

```text
/subtask Comprueba esta duda de la revisión: [pregunta concreta]. Usa ~/curso-claude/s09-revision/errores-api.diff, el contrato y el código actual. No edites ni confirmes nada. Devuelve la evidencia y lo que no pudiste comprobar.
```

`/subtask` hereda tu conversación: sirve para continuar la revisión, no para
obtener una opinión independiente del hilo. Si no está disponible, pide esa
misma comprobación en el hilo. Si no queda una duda o no alcanza el tiempo,
omite esta ejecución y registra el motivo; lo no comprobado queda pendiente.

### 3. Dejar el resultado para el triaje

Conserva en tus notas el origen de la revisión, los hallazgos con sus rutas,
la evidencia disponible y las preguntas pendientes. Si no hubo hallazgos,
anótalo sin convertirlo en garantía de ausencia de defectos.

No corrijas ni confirmes todavía. El Lab 03 amplía la mirada a seguridad y
el Lab 04 decide qué hacer con los resultados.

## Validación

```text
Sin editar nada, comprueba que el refactor sigue sin confirmar y que su
contenido coincide con la captura revisada. Distingue los hallazgos de la
revisión principal, la comprobación adicional si la hubo y las dudas pendientes.
```

- [ ] La revisión cubrió la captura completa, o declaraste que revisaste el estado actual sin cambios.
- [ ] Los hallazgos tienen evidencia y lo no comprobado quedó pendiente.
- [ ] La comprobación adicional respondió una duda concreta, o anotaste por qué la omitiste.
- [ ] El código no cambió durante la revisión y no añadiste otro archivo de agente en `.claude/agents/`.

## Limpieza

Conserva el `.diff` fuera del repositorio hasta cerrar el triaje del Lab 04.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| La revisión no incluyó el archivo nuevo | Vuelve a la captura del Lab 01: comprueba las rutas preparadas en Git y pide revisar lo omitido |
| El código cambió desde la captura | Conserva la captura anterior, genera otra identificada y vuelve a revisar el cambio actualizado |
| La revisión dice que todo está bien | Comprueba qué examinó y qué evidencia aporta; deja sin comprobar lo que no cubrió |
| La revisión propone arreglar algo | Conserva la propuesta como hallazgo; las correcciones se deciden en el Lab 04 |
