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

#### Sesión 8 — Describir el sistema sin que la descripción envejezca

La especificación OpenAPI la genera el framework, y el diagrama y el
diccionario de datos salen de los modelos y las migraciones: ninguno de los
tres hace falta escribirlo a mano, y una skill nueva los produce a demanda.
Lo que sí hace falta es decidir qué manda cuando la especificación generada y
el contrato escrito dejan de coincidir, y qué impide que vuelvan a separarse.
Una regla escrita en la sesión 7 persuade, pero no obliga: aquí entran dos
hooks, uno que bloquea antes y otro que actúa después, y la diferencia entre
los dos eventos es la lección.

**Decisión central:** qué descripción del sistema se genera desde el código y
se verifica sola, y qué debe ejecutarse siempre sin importar lo que decida
Claude.

**Evidencia:** la especificación OpenAPI versionada y confrontada con el
contrato, el diagrama y el diccionario de datos en `docs/`, y dos hooks
probados en los dos sentidos.

#### Sesión 9 — Delegar con contexto aislado

El cambio de hoy no lo escribe el estudiante ni lo supervisa turno a turno:
lo encarga a un subagente que trabaja solo y devuelve un resumen. La decisión
no es si delegar: es con cuánta autoridad, y se escribe en una línea. Se
construyen cuatro, y cada uno ocupa un punto distinto de esa escala: el que
escribe; un revisor de código y un auditor de seguridad que solo leen, con
autoridad idéntica y distinta lente; y uno que ejecuta comprobaciones sin
recibir ninguna herramienta de edición. Después se tría lo que devuelven:
hallazgo confirmado frente a ruido de quien no sabe qué se decidió a
propósito.

**Decisión central:** qué contexto, qué herramientas y qué autoridad recibe
un trabajo que no estás observando.

**Evidencia:** cuatro subagentes acotados y versionados, cada uno con la
autoridad mínima de su oficio, y sus hallazgos triados en aceptados y
rechazados con motivo, citando cada rechazo dónde está escrita la decisión.

#### Sesión 10 — Conectar sistemas externos, y soltar el volante

Nueve sesiones ejecutando Docker, PostgreSQL y peticiones HTTP a mano o por
shell. El estudiante conecta los tres como MCP y evalúa cada uno antes de
habilitarlo: qué alcance pide, a qué datos llega, qué permisos concede y qué
reemplaza de verdad. Después trabaja sin mirar: `/goal` itera hasta cumplir
una condición, y el mismo contrato de verificación se ejecuta sin interfaz con
salida estructurada. Lo que hace honesto ese bucle no es la promesa del
modelo: es un hook que comprueba la condición al final de cada turno y no le
deja parar hasta que se cumple. Cierra podando lo que diez sesiones
acumularon en `.claude/`.

**Decisión central:** qué alcance y qué permisos justifican una conexión
externa, y qué comprobación tiene que existir antes de dejar de mirar.

**Evidencia:** tres conexiones MCP justificadas, una ejecución no interactiva
reproducible, y un `.claude/` podado con lo que se queda y por qué.

## Proyecto Integrador

El proyecto es una API de gestión de tareas con PostgreSQL. Su dominio es
deliberadamente convencional para que las decisiones difíciles sean de
ingeniería asistida: contrato, migración, contexto, verificación, entrega,
permisos y automatización.

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
