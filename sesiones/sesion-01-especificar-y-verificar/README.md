# Sesión 1: De un Ticket a un Cambio Verificado

En esta sesión no vas a aprender una lista de comandos. En los primeros 40
minutos vas a tomar un incidente de facturación, hacer que Claude Code encuentre
la causa, corregirlo y revisar la evidencia antes de aceptar el cambio.

## Objetivo

Completar un cambio pequeño con Claude Code sin ceder el criterio de ingeniería:
definir el resultado, controlar el alcance, verificar el comportamiento y
revisar el diff.

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| Apertura: del incidente al diff | 10 |
| Conceptos: el ciclo de trabajo y el contrato de tarea | 20 |
| [Lab 01 — Resolver un incidente real](labs/01-bucle-de-verificacion/README.md) | 40 |
| [Lab 02 — Convertir una petición ambigua en contrato](labs/02-criterio-falseable/README.md) | 40 |
| Evidencia, transferencia y cierre | 10 |

## Materiales

- [Instalación del entorno](../../docs/instalacion-entorno.md)
- [Seguridad desde la primera sesión](../../docs/seguridad.md)
- [Referencia rápida](referencia-rapida.md)
- [Desafío opcional](tareas/desafio-opcional.md)

## Laboratorios

| Lab | Situación profesional | Qué descubres |
|---|---|---|
| [01 — Resolver un incidente real](labs/01-bucle-de-verificacion/README.md) | Un webhook reintentado duplica un pago | Claude puede cerrar el ciclo completo si recibe una comprobación ejecutable |
| [02 — Convertir una petición ambigua en contrato](labs/02-criterio-falseable/README.md) | "No aceptes pagos inválidos" no define qué significa inválido | Las decisiones que faltan en el encargo reaparecen como decisiones accidentales en el código |

Los dos labs trabajan sobre el mismo repositorio. El primero corrige un defecto
con una prueba de regresión ya escrita. El segundo te obliga a definir el
comportamiento antes de permitir que cambie el código.

Antes de empezar:

```bash
mkdir -p ~/curso-claude/evidencias
```

## Al finalizar esta sesión podrás

- Distinguir una conversación útil de una tarea delegable.
- Convertir un ticket en un contrato de tarea breve y comprobable.
- Pedir investigación, implementación y evidencia sin dictar la solución.
- Interrumpir y redirigir una ejecución que se sale de alcance.
- Evaluar salida de tests, diff y archivos modificados antes de aceptar.
- Explicar qué sigue sin estar probado aunque todo esté en verde.

## Conceptos Clave

### Claude Code ejecuta un ciclo, no una respuesta

Cuando recibe una tarea sobre un repositorio, Claude Code puede inspeccionar
archivos, ejecutar comandos, editar y volver a comprobar. El ciclo útil es:

```text
entender → acordar → cambiar → comprobar → revisar
```

El valor no está en que escriba código rápido. Está en que pueda recorrer ese
ciclo usando el mismo repositorio, las mismas herramientas y las mismas señales
de calidad que usa el equipo.

Tu responsabilidad cambia. Ya no decides cada línea, pero sigues decidiendo:

- qué problema vale la pena resolver;
- qué resultado cuenta como correcto;
- qué no debe tocarse;
- qué evidencia basta para aceptar el cambio.

### Una tarea profesional es un contrato, no un prompt perfecto

No necesitas una fórmula mágica. Necesitas cinco decisiones explícitas:

| Parte | Pregunta que responde |
|---|---|
| Resultado | ¿Qué comportamiento debe cambiar? |
| Fuentes | ¿Dónde están el ticket, el contrato y los patrones del repositorio? |
| Alcance | ¿Qué puede cambiar y qué queda fuera? |
| Restricciones | ¿Qué compatibilidad, seguridad o diseño debe conservarse? |
| Verificación | ¿Qué comando o evidencia demuestra el resultado? |

Un encargo puede ser corto y contener las cinco. También puede ocupar una página
y no contener ninguna.

Este es el contrato del primer lab:

```text
Resuelve @ticket.md. Reproduce primero el fallo. Corrige la causa con el cambio
mínimo y no modifiques ticket.md ni test_billing.py. Quedan fuera persistencia,
concurrencia y validación de firmas. Termina cuando la suite pase y muestra el
diff y los comandos ejecutados.
```

El contrato define el resultado y los límites. No le dice al agente qué `if`
escribir ni en qué línea. Acotar el problema no significa dictar la solución.

### La verificación tiene capas

"Listo" es una afirmación. Una salida en verde es evidencia, pero solo de lo que
esa comprobación alcanza a mirar.

| Capa | Pregunta |
|---|---|
| Comportamiento | ¿La prueba que reproduce el problema ahora pasa? |
| Regresión | ¿Sigue pasando lo que funcionaba antes? |
| Alcance | ¿Solo cambiaron los archivos autorizados? |
| Calidad del cambio | ¿El diff resuelve la causa sin complejidad accidental? |

Por eso una suite verde no cierra por sí sola el trabajo. Puede no cubrir el
caso importante, puede haber sido debilitada o puede pasar mientras el diff
introduce otra cosa. La revisión combina resultados ejecutables con inspección
del cambio.

En el Lab 01 la prueba ya existe y no puede tocarse. En el Lab 02 primero
acuerdas el contrato, después conviertes ese contrato en tests y recién entonces
implementas. El orden importa: el código no debería inventar el requisito que
se usará para juzgarlo.

### Dirigir es intervenir temprano

No mires una ejecución equivocada hasta el final. Si Claude interpreta mal el
ticket, quiere tocar un archivo fuera de alcance o persigue un enfoque innecesario,
presiona `Esc`, explica la desviación y continúa desde ahí.

Una corrección útil contiene evidencia:

```text
Detente. test_billing.py forma parte de la comprobación y no debe cambiar.
Revierte ese archivo y resuelve el comportamiento en billing.py.
```

Interrumpir no es un fracaso del flujo. Es el mecanismo normal para mantener una
tarea dentro de sus límites.

### La evidencia que debes pedir

Al cerrar una tarea, pide un reporte que puedas auditar en menos de un minuto:

1. causa encontrada, con archivo y línea;
2. archivos modificados y motivo;
3. comandos ejecutados y resultado;
4. riesgos o casos que siguen fuera de alcance.

Después abre el diff. El reporte reduce el tiempo de revisión; no reemplaza la
revisión.

## Comandos Nuevos

| Comando o control | Uso |
|---|---|
| `claude` | Abrir una sesión sobre el directorio actual |
| `@archivo` | Incluir un archivo concreto como fuente de la tarea |
| `/status` | Comprobar el modo de permisos activo |
| `Shift+Tab` | Cambiar el modo de permisos de la sesión |
| `Esc` | Interrumpir la acción actual para redirigirla |
| `/diff` | Revisar los cambios de la sesión |
| `/exit` | Cerrar la sesión interactiva |

Git y la suite del repositorio siguen siendo la fuente de verdad:

```bash
git status --short
git diff --check
python3 -m unittest -v
```

## Validación General

```bash
cd ~/curso-claude/sesion-01/webhook-ledger
python3 -m unittest -v
python3 acceptance_validation.py
git diff --check
git status --short
```

La sesión está completa si:

- [ ] El mismo `event_id` aplicado dos veces cambia el saldo una sola vez.
- [ ] Un evento inválido produce `ValueError` sin modificar el estado.
- [ ] La suite y la validación independiente terminan sin error.
- [ ] Puedes justificar cada archivo modificado.
- [ ] Conservaste el ticket, el contrato y la validación sin cambios durante la implementación.
- [ ] Guardaste una evidencia breve con resultado, comandos y riesgo residual.

## Limpieza

El repositorio de la sesión es descartable. Conserva primero la evidencia:

```bash
ls ~/curso-claude/evidencias/s01.md
```

Si aparece, puedes borrar el laboratorio:

```bash
rm -rf ~/curso-claude/sesion-01
```

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) aplica el mismo ciclo a un
ticket pequeño de un repositorio propio.

## Cierre

Guarda `~/curso-claude/evidencias/s01.md` con este contenido mínimo:

```markdown
# Sesión 1

## Cambio aceptado
Qué comportamiento cambió y por qué.

## Evidencia
Comandos ejecutados y resultado.

## Revisión del diff
Qué archivo cambió y por qué el alcance es correcto.

## Riesgo residual
Qué sigue fuera de alcance o sin probar.
```

Preguntas de repaso:

- ¿Qué diferencia una tarea delegable de una petición vaga?
- ¿Qué demuestra una suite verde y qué no demuestra?
- ¿Por qué se confirma la prueba antes de implementar?
- ¿Cuándo debes interrumpir al agente?
- ¿Qué cuatro datos necesitas para revisar un cierre sin releer toda la sesión?

## Versión

Material revisado el **26 de agosto de 2026** contra la documentación oficial de
Claude Code sobre el ciclo del agente, verificación, contexto y dirección de
sesiones. Comprueba la instalación local con `claude --version` y `/help`.

Si la interfaz difiere, consulta:

- [Cómo funciona Claude Code](https://code.claude.com/docs/en/how-claude-code-works)
- [Prácticas recomendadas](https://code.claude.com/docs/en/best-practices)

## Preparación para la Siguiente Sesión

La sesión 2 crea el proyecto integrador y diseña el contexto que Claude recibirá
en cada sesión. Antes de llegar, comprueba:

```bash
docker run --rm hello-world
uv --version
git config --get user.email
```
