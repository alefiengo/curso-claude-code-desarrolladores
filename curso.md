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

Se conecta la API a PostgreSQL —persistencia, migración inicial y catálogo de
estados— mientras se observa qué llena el contexto. El estudiante separa una
pregunta lateral, una exploración extensa y una decisión persistente; limpia o
compacta solo cuando sabe qué debe conservar.

**Decisión central:** cuándo continuar, compactar, delegar investigación o
empezar una sesión limpia.

**Evidencia:** la persistencia en verde y el registro del contexto antes y
después de una acción.

### Bloque 2 — Diseñar, implementar y recuperar

#### Sesión 4 — Explorar y planificar un cambio multiarchivo

El CRUD de proyectos toca modelo, migración, esquemas, rutas y tests, y el
contrato promete un `409` que todavía no puede implementarse. Antes de editar,
Claude explora el repositorio y propone un plan. El estudiante rechaza
afirmaciones sin fuente, cierra las decisiones que el contrato deja abiertas y
convierte el resultado en contrato ejecutable.

**Decisión central:** cuándo el coste de planificar es menor que el de corregir.

**Evidencia:** especificación autocontenida, plan con archivos reales y tests en
rojo por capacidad ausente.

#### Sesión 5 — Implementar y entregar un cambio revisable

Claude implementa los proyectos contra el contrato ya fijado. El estudiante
dirige por resultados, detecta si los tests se movieron, pide una revisión que no
hereda su conversación, separa commits por intención y prepara una entrega que
otra persona puede revisar sin leer el hilo.

**Decisión central:** cuándo un cambio funciona pero todavía no está listo para
integrarse.

**Evidencia:** migración, suite, diff acotado, historial coherente y descripción
de entrega.

#### Sesión 6 — Interrumpir, recuperar y continuar

Al implementar tareas y filtros, un encargo ancho se lleva por delante trabajo ya
terminado. Se prueban dos caminos: corregir sobre el contexto contaminado o
rebobinar. Rebobinar deja al descubierto qué no cubre un checkpoint —la base de
datos ya migrada, entre otras cosas—. Después se cierra la sesión y otra persona
retoma con un traspaso mínimo.

**Decisión central:** cuándo sale más barato redirigir, rebobinar o empezar
limpio.

**Evidencia:** estado recuperado y continuidad lograda sin recontar toda la
conversación.

### Bloque 3 — Verificar, extender y automatizar

#### Sesión 7 — Reproducir antes de explicar

Una entrada Unicode atraviesa una validación aparentemente correcta. Claude debe
reproducir el fallo antes de proponer la causa, distinguir un fallo útil de un
test mal montado y cerrar con una regresión. Una comprobación visual muestra el
límite de una captura frente a una prueba de comportamiento.

**Decisión central:** qué evidencia demuestra el fallo y qué evidencia demuestra
la corrección.

**Evidencia:** reproducción mínima, regresión permanente y explicación respaldada
por archivo y línea.

#### Sesión 8 — Convertir repetición en una herramienta evaluada

Un procedimiento de verificación ya se repitió varias veces y produce cierres
distintos. El estudiante lo convierte en skill, decide qué queda en lenguaje
natural y qué pasa a código, y lo evalúa con casos válidos, inválidos y adversos.

**Decisión central:** cuándo una repetición merece una skill y cuándo solo
necesita una instrucción más clara.

**Evidencia:** skill versionado, casos de evaluación y prueba de que no edita el
proyecto cuando solo debe verificar.

#### Sesión 9 — Convertir reglas en guardrails

El estudiante diferencia instrucciones, permisos, sandbox y hooks. Configura el
mínimo privilegio necesario, prueba lo permitido y lo prohibido, y añade una
puerta automática donde una recomendación no basta.

**Decisión central:** qué debe persuadirse, qué debe ejecutarse siempre y qué no
puede permitirse.

**Evidencia:** matriz de permisos y hooks probados con casos positivos y
negativos.

#### Sesión 10 — Delegar y ejecutar sin nadie delante

Una revisión se entrega a un subagente con contexto aislado. Una conexión MCP se
evalúa por alcance, datos, permisos y coste antes de habilitarse. Finalmente el
mismo contrato de verificación se ejecuta sin interfaz y produce salida
estructurada para CI.

**Decisión central:** qué contexto, herramientas y autoridad recibe una ejecución
que no estás observando.

**Evidencia:** hallazgos triados, conexión justificada o rechazada y ejecución no
interactiva reproducible.

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
| Laboratorio 1 | 35–45 | Caso principal resuelto con guía |
| Laboratorio 2 | 35–45 | Variación, límite o transferencia |
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
