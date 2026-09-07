# Plan del Curso

## Propósito

Este curso enseña a usar Claude Code como parte de un sistema de ingeniería, no
como sustituto del criterio técnico.

La competencia final es concreta:

> Tomar un cambio real desde un ticket incompleto hasta una entrega verificable,
> manteniendo control sobre contexto, alcance, evidencia y permisos.

La API del proyecto es el entorno de práctica. No se evalúa cuánto FastAPI
recuerdas; se evalúa cómo entiendes, diriges, verificas y entregas el cambio.

## El Modelo de Trabajo

Todas las sesiones repiten un mismo ciclo:

```text
entender → acordar → cambiar → comprobar → revisar
```

| Momento | Decisión humana | Trabajo que puede hacer Claude |
|---|---|---|
| Entender | Qué problema importa y qué fuente es confiable | Explorar código, historial, logs y documentación |
| Acordar | Qué resultado, límites y riesgos se aceptan | Detectar ambigüedades y proponer alternativas |
| Cambiar | Cuánta autonomía corresponde al riesgo | Implementar y corregir con feedback |
| Comprobar | Qué evidencia basta y qué sigue sin probarse | Ejecutar tests, lint, build y validaciones |
| Revisar | Si el diff merece integrarse | Resumir, comparar contrato y señalar riesgos |

El estudiante no memoriza una ceremonia. Aprende a reducir o ampliar cada
momento según el trabajo. Un cambio de una línea puede ir directo a
implementación. Una migración o una modificación multiarchivo necesita
investigación y plan antes de editar.

## Principios Didácticos

### El escenario aparece antes que el concepto

Cada sesión empieza con una situación reconocible: un incidente, un cambio de
contrato, una sesión degradada, un falso positivo o una automatización con más
permisos de los necesarios. La teoría nombra lo que el estudiante acaba de
necesitar.

### Una sesión produce una decisión y una evidencia

El resultado no es "vi hooks". Es "elegí un hook porque la acción debía ocurrir
siempre, lo probé con el caso permitido y con el bloqueado, y conservé la
salida".

### Las respuestas variables no se convierten en guiones falsos

Cuando interviene el modelo, el material describe invariantes: qué archivo debe
haber cambiado, qué comando debe haber terminado, qué límite debe haberse
respetado. No promete una redacción ni una secuencia exacta de herramientas.

### La complejidad técnica paga una lección

Ninguna dependencia, comando o paso entra solo para hacer que el ejercicio
parezca avanzado. PostgreSQL existe para practicar migraciones y datos reales.
Git existe para revisar, recuperar y entregar. Si una pieza no cambia una
decisión profesional, se elimina.

### La autonomía crece junto con los controles

Primero se dirige una tarea supervisada. Después se incorpora memoria de
proyecto, recuperación, procedimientos reutilizables, guardrails, delegación y
modo no interactivo. Más autonomía exige mejor verificación y límites más
claros.

## Arquitectura de 20 Horas

### Bloque 1 — Controlar una tarea y su contexto

#### Sesión 1 — De un ticket a un cambio verificado

Un webhook reintentado acredita dos veces el mismo pago. El estudiante recibe
un incidente, reproduce el defecto, dirige una corrección mínima y audita suite,
alcance y diff. Después toma una petición ambigua, cierra decisiones, confirma
tests en rojo e implementa contra un contrato ya fijado.

**Decisión central:** qué necesita una tarea para poder delegarse.

**Evidencia:** contrato, rojo correcto, verde final, diff y riesgo residual.

#### Sesión 2 — Dar contexto que sí cambia el resultado

El estudiante dirige a Claude para crear desde cero la base del proyecto bajo
un contrato explícito, audita alcance y gates, y observa qué puede descubrir el
agente sin memoria. Después genera y depura un `CLAUDE.md`: elimina inventario,
estado temporal y consejos genéricos; conserva comandos, decisiones no evidentes
y límites reales. Finalmente lo prueba contra una propuesta que contradice
cuatro reglas del equipo.

**Decisión central:** qué merece cargarse en cada sesión.

**Evidencia:** borrador auditado, `CLAUDE.md` cargado y revisión de una propuesta
adversa con cuatro conflictos conocidos.

#### Sesión 3 — Mantener señal durante un cambio largo

Se acuerda cómo conectar la API a PostgreSQL —persistencia, migración inicial y
catálogo de estados— mientras se observa qué llena el contexto. El estudiante
separa una pregunta lateral, una exploración extensa y una decisión persistente;
limpia o compacta solo cuando sabe qué debe conservar.

**Decisión central:** cuándo continuar, compactar, delegar investigación o
empezar una sesión limpia.

**Evidencia:** un plan de persistencia escrito y aprobado, y el registro del
contexto antes y después de una acción.

### Bloque 2 — Ejecutar, entregar y recuperar

#### Sesión 4 — Ejecutar un plan acordado y publicarlo

El plan de persistencia está aprobado, tiene cuatro incrementos y deja una
decisión sin cerrar. El estudiante la cierra por escrito antes de que la cierre
el agente, dirige los incrementos uno a uno con un commit por incremento, y
convierte en configuración versionada los permisos que hasta ahora aprobaba de
uno en uno. La sesión termina con el trabajo publicado en un remoto propio.

**Decisión central:** qué se le pide al agente y qué se le permite, que no son
la misma lista.

**Evidencia:** cuatro commits con la migración reversible y `GET /states` en
verde, `.claude/settings.json` en el repositorio y dos ramas en el remoto.

#### Sesión 5 — Integrar lo hecho y construir tus primeras herramientas

La rama de la sesión anterior sigue publicada y sin integrar. El estudiante
comprueba la API contra un servidor real —no solo contra su suite—, la entrega
en una solicitud de cambios que otra persona puede revisar sin leer el hilo, y
la integra. Después decide qué de su trabajo repetido merece convertirse en
herramienta y construye sus dos primeras skills: con una planifica los
proyectos contra el contrato ya fijado, y con la otra reparte en commits el
bloque de código que llega cuando deja de aprobar cada acción.

**Decisión central:** cuánta autonomía se le concede a un cambio, y qué tiene
que estar escrito antes de concederla.

**Evidencia:** una rama integrada desde una solicitud de cambios, al menos dos
skills versionadas, un plan aprobado antes del primer archivo de código y un
historial con una intención por commit.

#### Sesión 6 — Interrumpir y recuperar

Al implementar tareas y filtros, un encargo ancho se lleva por delante trabajo ya
terminado. Se prueban dos caminos: corregir sobre el contexto contaminado o
rebobinar. Rebobinar deja al descubierto qué no cubre un checkpoint —la base de
datos ya migrada, entre otras cosas—. La sesión cierra comprobando el contrato
completo contra el servidor real, no solo contra la suite.

**Decisión central:** cuándo sale más barato corregir hacia adelante, rebobinar o empezar
limpio.

**Evidencia:** el desvío corregido o rebobinado, el desajuste de `/rewind`
resuelto, y el contrato completo demostrado contra la API corriendo.

### Bloque 3 — Verificar, extender y automatizar

#### Sesión 7 — Reproducir antes de explicar

Una skill propia reparte commits reescribiendo código en vez de usar el índice
de Git, y una entrada Unicode atraviesa una validación aparentemente correcta.
Claude reproduce los dos fallos antes de proponer una causa, y las reglas que
los hubieran evitado se escriben en `.claude/rules/`. La sesión cierra
comprobando si el repositorio se explica solo a alguien que no vivió la
conversación, con una colección de peticiones y un README que cualquiera puede
repetir.

**Decisión central:** qué evidencia demuestra un fallo, y qué convierte una
corrección en algo que no vuelve a pasar.

**Evidencia:** dos fallos reproducidos y cerrados, tres reglas de proyecto
comprobadas, y el contrato completo demostrado sin depender de esta
conversación.

#### Sesión 8 — Convertir reglas en guardarraíles, y delegar con contexto aislado

Una regla escrita en la sesión 7 persuade, pero no obliga: es contexto que
Claude lee, no una condición que se cumpla sin importar lo que decida. El
estudiante configura un hook donde una regla no basta, con casos permitidos y
bloqueados. Después entrega una revisión a un subagente con contexto aislado,
y decide qué autoridad y qué herramientas le concede a un trabajo que no va a
supervisar turno a turno.

**Decisión central:** qué debe ejecutarse siempre sin importar la decisión de
Claude, y qué autoridad delegas a un contexto que no supervisas paso a paso.

**Evidencia:** un hook probado con casos positivos y negativos, y una revisión
delegada con hallazgos triados.

#### Sesión 9 — Evaluar y conectar sistemas externos

El estudiante quiere que Claude consulte PostgreSQL directamente y administre
colecciones de Postman, sin `psql` suelto ni copiar y pegar. Evalúa las dos
conexiones MCP por alcance, datos, permisos y coste antes de habilitarla o
rechazarla. Con esa disciplina fresca, planifica el incremento del BFF con la
misma skill de planificación que ya construyó, sin implementarlo todavía.

**Decisión central:** qué alcance, qué datos y qué permisos justifican
habilitar una conexión externa.

**Evidencia:** dos conexiones MCP evaluadas —aceptada o rechazada, con
motivo— y el plan del BFF aprobado antes del primer archivo de código.

#### Sesión 10 — Delegar y ejecutar sin nadie delante

Con el plan del BFF ya aprobado, el estudiante dirige su implementación con
`/goal`, sin supervisar cada turno. El mismo contrato de verificación se
ejecuta después sin interfaz y produce salida estructurada para CI.

**Decisión central:** qué autoridad recibe una ejecución que no estás
observando, y qué evidencia demuestra que terminó bien.

**Evidencia:** el BFF implementado con `/goal`, y una ejecución no interactiva
reproducible.

## Proyecto Integrador

El proyecto es una API de gestión de tareas con PostgreSQL, a la que más
adelante se antepone un BFF. Su dominio es deliberadamente convencional para que
las decisiones difíciles sean de ingeniería asistida: contrato, migración,
contexto, verificación, entrega, permisos y automatización.

No se construye una aplicación distinta en cada sesión. El mismo repositorio
acumula historia, decisiones y herramientas, de modo que también aparecen los
problemas reales de continuidad y mantenimiento.

Consulta [Proyecto integrador](proyecto-integrador/README.md).

## Anatomía de una Sesión

| Tramo | Minutos orientativos | Resultado |
|---|---:|---|
| Apertura y demostración | 10 | Problema visible y pregunta de ingeniería |
| Conceptos precisos | 15–20 | Modelo mental necesario para decidir |
| Laboratorio 1 | 35–50 | Caso principal resuelto con guía |
| Laboratorios siguientes | 20–45 | Variación, límite o transferencia |
| Revisión y cierre | 10–15 | Evidencia, riesgo residual y conexión con la siguiente sesión |

Los tiempos exactos están en cada sesión y suman 120 minutos. Si una práctica no
cabe tras pilotarla, se reduce el alcance; no se convierte en lectura acelerada.

## Evaluación

No hay nota numérica. Se evalúan hábitos observables:

- investiga antes de afirmar;
- explicita decisiones que el ticket no tomó;
- usa una comprobación pertinente;
- interviene ante una desviación;
- revisa todos los archivos modificados;
- distingue evidencia de conclusión;
- declara lo que sigue sin estar probado.

El diagnóstico y la tarea final usan problemas equivalentes para comparar el
proceso, no la cantidad de código. La rúbrica está en
[Evaluación y portafolio](docs/evaluacion.md).

## Fuentes y Versionado

Claude Code cambia con frecuencia. Las afirmaciones sobre capacidades se
contrastan con dos fuentes:

- la ayuda de la versión instalada (`claude --help` y `/help`);
- la [documentación oficial](https://code.claude.com/docs).

La primera confirma disponibilidad local. La segunda explica semántica,
restricciones y cambios. Ninguna reemplaza a la otra.
