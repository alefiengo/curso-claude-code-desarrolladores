# Temario

Diez sesiones de dos horas. El recorrido aumenta la autonomía de Claude Code al
mismo ritmo que aumenta la capacidad del estudiante para darle contexto,
verificarlo y limitarlo.

## Bloque 1 — Controlar la Tarea y el Contexto

### 1. De un ticket a un cambio verificado

**Situación:** un webhook reintentado acredita dos veces el mismo pago.

**Conceptos:** ciclo del agente, contrato de tarea, alcance, verificación por
capas, intervención temprana y revisión del diff.

**Práctica:** corregir el incidente con una regresión protegida; convertir "no
aceptes pagos inválidos" en decisiones, tests y una validación independiente.

**Sales con:** un cambio aceptado por evidencia, no por la afirmación del agente.

### 2. Contexto de proyecto que sí aporta

**Situación:** sin instrucciones, Claude redescubre el proyecto; con demasiadas,
recibe ruido y reglas contradictorias.

**Conceptos:** contexto, instrucciones persistentes, memoria automática, alcance
por directorio y coste de información siempre cargada.

**Práctica:** dirigir a Claude para fundar la API desde un contrato, auditar el
primer diff y probar un `CLAUDE.md` contra una propuesta que contradice sus
reglas.

**Sales con:** una memoria breve donde cada línea cambia una decisión real.

### 3. Mantener señal durante una tarea larga

**Situación:** la conversación acumula archivos, comandos y caminos descartados
mientras se acuerda cómo conectar la API a PostgreSQL.

**Conceptos:** presupuesto de contexto, sesión limpia, compactación, preguntas
laterales y persistencia de decisiones.

**Práctica:** llevar una conversación larga hasta un plan de persistencia
acordado, midiendo qué ocupa contexto antes de decidir qué conservar.

**Sales con:** un plan escrito que sobrevive a la conversación que lo produjo, y
criterio para continuar, compactar o empezar limpio.

## Bloque 2 — Ejecutar, Entregar y Recuperar

### 4. Ejecutar y publicar

**Situación:** el plan está aprobado, deja una decisión sin cerrar y son cuatro
incrementos por delante. Nada de lo que se haga existirá fuera de tu máquina.

**Conceptos:** decisión abierta, un commit por incremento, diferencia entre lo
que pides y lo que permites, configuración de proyecto versionada, remoto y
lectura del historial desde fuera.

**Práctica:** cerrar la decisión abierta antes del primer incremento, dirigir los
cuatro uno a uno, escribir los permisos en `.claude/settings.json` y publicar el
repositorio en un remoto propio.

**Sales con:** la persistencia en verde, los permisos versionados y el trabajo
visible para alguien que no estuvo.

### 5. Revisar e integrar

**Situación:** el trabajo está en verde y sigue siendo tuyo y solo tuyo. Una
suite que pasa no demuestra que el servicio responda, y una rama publicada no
pide nada a nadie.

**Conceptos:** verificación contra el servicio frente a verificación contra las
pruebas, procedimiento reutilizable frente a instrucción suelta, plan aprobado
antes de la ejecución, y autonomía concedida sobre reglas escritas.

**Práctica:** comprobar la API con peticiones reales, entregar e integrar la
rama pendiente en una solicitud de cambios, decidir qué trabajo repetido merece
convertirse en herramienta, escribir dos skills propias, y usarlas para
planificar un recurso completo y repartir su implementación en commits con una
intención cada uno.

**Sales con:** una entrega que otra persona puede entender, ejecutar y
cuestionar, y dos herramientas versionadas en tu repositorio.

### 6. Interrumpir, recuperar y continuar

**Situación:** Claude sigue una hipótesis equivocada y la tarea debe continuar en
otro momento o en otra sesión.

**Conceptos:** interrupción, redirección, checkpoint, rewind, Git como red de
seguridad y traspaso de trabajo.

**Práctica:** comparar corrección y recuperación; retomar desde evidencia mínima
sin reinyectar toda la conversación.

**Sales con:** una estrategia de recuperación y un traspaso probado.

## Bloque 3 — Verificar, Extender y Automatizar

### 7. Reproducir antes de explicar

**Situación:** una entrada Unicode atraviesa una validación y la primera causa
plausible no basta.

**Conceptos:** reproducción, hipótesis, rojo correcto, causa raíz, regresión y
límite de la evidencia visual.

**Práctica:** reproducir, corregir y proteger el fallo; contrastar captura con
comportamiento ejecutable.

**Sales con:** una corrección respaldada por una regresión permanente.

### 8. Convertir repetición en una herramienta evaluada

**Situación:** el mismo procedimiento de verificación se repite y cambia entre
ejecuciones.

**Conceptos:** skills bajo demanda, descubrimiento, instrucciones frente a
código, efectos permitidos y evaluación de una herramienta de IA.

**Práctica:** construir un skill de verificación y someterlo a casos válidos,
inválidos y adversos.

**Sales con:** un skill versionado cuya utilidad y límites fueron probados.

### 9. Convertir reglas en guardarraíles

**Situación:** "no hagas X" es una instrucción; una ejecución automática necesita
una garantía más fuerte.

**Conceptos:** permisos, sandbox, hooks, mínimo privilegio, caso negativo y
diferencia entre persuadir, disparar y bloquear.

**Práctica:** configurar solo la autoridad necesaria y demostrar tanto lo que se
permite como lo que se rechaza.

**Sales con:** permisos y hooks auditables, no una configuración aceptada por fe.

### 10. Delegar y ejecutar sin nadie delante

**Situación:** una segunda opinión contaminada por la conversación no es
independiente, y una ejecución en CI no puede detenerse a pedir permiso.

**Conceptos:** contexto aislado, revisión adversaria, alcance de MCP, ejecución
no interactiva, salida estructurada y límites operativos.

**Práctica:** delegar una revisión, evaluar una conexión externa y ejecutar la
verificación en un flujo automatizado.

**Sales con:** una entrega revisada y un proceso no interactivo con autoridad
explícita.

## La Decisión que Conecta Todo

Las extensiones no son una lista para instalar. Cada una responde a un problema
diferente:

| Necesidad | Mecanismo candidato |
|---|---|
| Información que Claude debe tener en cada sesión | `CLAUDE.md` o regla acotada |
| Procedimiento o conocimiento reutilizable bajo demanda | Skill |
| Acción que debe dispararse en un evento | Hook |
| Acción que nunca debe autorizarse | Regla de permiso o política |
| Investigación o revisión que necesita contexto aislado | Subagente |
| Datos o acciones de un sistema externo | MCP o una CLI existente |

La pregunta profesional no es "¿cómo configuro todo?". Es "¿cuál es el mínimo
mecanismo que resuelve este riesgo y cómo demuestro que funciona?".

## Proyecto y Evaluación

El [proyecto integrador](../proyecto-integrador/README.md) es una API de tareas
que acumula contrato, migraciones, defectos, historia Git y automatización. Cada
sesión deja una evidencia revisable.

El curso usa evaluación formativa. El diagnóstico inicial y la transferencia
final comparan hábitos: investigar, acordar, comprobar, intervenir y revisar.
Consulta [Evaluación y portafolio](evaluacion.md).
