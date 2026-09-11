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
convertirse en herramienta, escribir tus primeras skills propias, y usarlas
para planificar un recurso completo y repartir su implementación en commits
con una intención cada uno.

**Sales con:** una entrega que otra persona puede entender, ejecutar y
cuestionar, y al menos dos herramientas versionadas en tu repositorio.

### 6. Interrumpir y recuperar

**Situación:** un encargo demasiado amplio se lleva por delante trabajo que ya
funcionaba, y rebobinar no siempre te devuelve al punto que crees.

**Conceptos:** costo de corregir hacia adelante frente a rebobinar, y qué
revierte un checkpoint y qué no —un comando ejecutado no es un archivo
editado—.

**Práctica:** cerrar el contrato completo de la API —proyectos y tareas—,
reutilizar una skill de la sesión anterior sobre un contrato distinto, y
provocar y resolver el desajuste entre una migración rebobinada y la base de
datos.

**Sales con:** el contrato completo implementado, y un criterio para decidir
entre corregir hacia adelante, rebobinar o empezar limpio.

## Bloque 3 — Verificar, Extender y Automatizar

### 7. Reproducir antes de explicar

**Situación:** una skill propia reparte commits reescribiendo código en vez de
usar el índice de Git, y una entrada Unicode atraviesa una validación que
parece correcta.

**Conceptos:** reproducción antes que explicación, causa raíz, regla de
proyecto frente a `CLAUDE.md`, y la diferencia entre retomar tu propia
conversación y que el repositorio se explique solo.

**Práctica:** reproducir y corregir los dos fallos, escribir las reglas que
los hubieran evitado, comprobar el propio repositorio con una conversación
sin contexto, y dejar una colección de peticiones ejecutable que demuestra
el contrato completo.

**Sales con:** dos fallos corregidos con su regla escrita, y el contrato
completo demostrado sin depender de esta conversación.

### 8. Describir el sistema sin que la descripción envejezca

**Situación:** la especificación que describe tu API y el contrato que
prometiste dejan de coincidir, y nadie se entera.

**Conceptos:** descripción generada frente a escrita a mano, deriva entre
código y contrato, y la diferencia entre persuadir, decidir la autoridad y
garantizar —instrucción, regla, permiso, hook—.

**Práctica:** exportar la especificación OpenAPI y confrontarla con el
contrato; construir una skill que genere el diagrama y el diccionario de datos
desde los modelos y las migraciones; y configurar dos hooks —uno que bloquea
el commit cuando la descripción quedó desincronizada, otro que la regenera al
editar los modelos—, probados con un caso permitido y uno bloqueado.

**Sales con:** una descripción del sistema que se regenera y se verifica sola,
y dos guardarraíles probados en los dos sentidos.

### 9. Delegar con contexto aislado

**Situación:** una segunda opinión contaminada por la conversación que produjo
el cambio no es independiente.

**Conceptos:** contexto aislado, autoridad acotada de un trabajo delegado,
revisión adversaria y triaje de hallazgos.

**Práctica:** crear cuatro subagentes con la autoridad mínima de su oficio
—uno que escribe y produce el cambio; un revisor de código y un auditor de
seguridad que solo leen; y uno que ejecuta comprobaciones sin herramientas de
edición—, comparar tres revisiones del mismo cambio según el contexto que
lleva cada una, y triar los hallazgos en aceptados y rechazados con motivo.

**Sales con:** cuatro subagentes acotados y versionados, y hallazgos triados
con criterio propio en la solicitud de cambios.

### 10. Conectar sistemas externos, y soltar el volante

**Situación:** llevas nueve sesiones ejecutando Docker, PostgreSQL y peticiones
HTTP a mano; y tu verificación solo corre cuando alguien se acuerda de mirarla.

**Conceptos:** alcance de un MCP, datos a los que llega, permisos que concede,
coste; condición comprobable frente a promesa del modelo; ejecución no
interactiva y salida estructurada; y poda de lo acumulado en `.claude/`.

**Práctica:** conectar y evaluar tres servidores MCP —Docker, Postman y
PostgreSQL—; dejar a Claude trabajando contra una condición con `/goal` y
ejecutar la misma verificación sin interfaz; y podar `.claude/`, `CLAUDE.md` y
el `README.md` final.

**Sales con:** tres conexiones justificadas, una ejecución no interactiva
reproducible, y un repositorio del que sabes decir qué se queda y por qué.

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

El diagnóstico inicial y la transferencia final comparan hábitos: investigar,
acordar, comprobar, intervenir y revisar, y no llevan nota. La calificación son
dos cifras: el cuestionario final sobre Claude Code, con 24 horas de plazo desde
que se publica, vale el 80 %, y la asistencia el 20 %. Consulta
[Evaluación](evaluacion.md).
