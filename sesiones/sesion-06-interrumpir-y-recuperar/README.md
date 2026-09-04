# Sesión 6: Interrumpir y Recuperar

## Objetivo

Cerrar el dominio completo de la API —proyectos, tareas y sus fechas límite—
mientras aprendes qué hacer cuando un encargo se sale de lo pedido: cuándo
corregirlo hacia adelante, cuándo rebobinarlo, y qué información necesita
quien retome tu trabajo sin haber estado en tu conversación.

El problema profesional de hoy: **un encargo demasiado amplio se lleva por
delante trabajo que ya funcionaba**, y rebobinar no siempre te devuelve al
punto que crees.

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — Cerrar y planificar](labs/01-cerrar-y-planificar/README.md) | 30 |
| [Lab 02 — El encargo ancho](labs/02-el-encargo-ancho/README.md) | 45 |
| [Lab 03 — Traspaso mínimo](labs/03-traspaso-minimo/README.md) | 35 |
| Cierre y decisión transferible | 10 |

## Materiales

- Tu repositorio `~/curso-claude/curso-claude-code-api`, con `main` en verde:
  persistencia, proyectos y tus dos skills de la sesión 5.
- Docker arrancado. Los contenedores los levanta Claude.
- `docs/contrato-api.md`, secciones **Proyectos**, **Tareas v1** y **Tareas v2:
  Fechas Límite**. Hoy cierras el contrato entero.
- La [referencia rápida](referencia-rapida.md) de la sesión, con lo que
  `/rewind` sí revierte y lo que no.

Sigues sin teclear los comandos del proyecto. `uv`, `docker`, `alembic`,
`pytest`, `git` y la CLI de tu proveedor los ejecuta Claude, y tú lees lo que
informa.

## Laboratorios

| Lab | Qué haces | Qué descubres |
|---|---|---|
| [01 — Cerrar y planificar](labs/01-cerrar-y-planificar/README.md) | Planificas tareas v1 y v2 de una vez con tu skill, implementas v1 y cierras el `409` que quedó sin probar en la sesión 5 | Que una skill reutilizada no necesita reescribirse: el procedimiento sigue siendo el mismo, solo cambia el contrato al que apunta |
| [02 — El encargo ancho](labs/02-el-encargo-ancho/README.md) | Le das a Claude un encargo grande para v2, sin pasar por el plan que ya tenías escrito, y revisas qué hizo de más | Que corregir hacia adelante y rebobinar no cuestan lo mismo, y que `/rewind` no toca lo que ya cambiaste con un comando |
| [03 — Traspaso mínimo](labs/03-traspaso-minimo/README.md) | Cierras el contrato de tareas, y compruebas si tu repositorio le explica el proyecto a alguien que no vivió esta conversación | Que retomar tu propio trabajo no es lo mismo que retomarlo otra persona, y qué le falta a tu repositorio para lo segundo |

## Al finalizar esta sesión podrás

- Reutilizar una skill de una sesión anterior sobre un contrato distinto, sin
  reescribirla.
- Reconocer cuándo un encargo se salió de lo pedido, mirando el diff con una
  pregunta concreta.
- Elegir entre corregir hacia adelante y rebobinar, según lo que cada uno
  cuesta en ese momento.
- Explicar qué revierte `/rewind` y qué no, con un caso real delante.
- Recuperar de forma segura un desajuste entre tus archivos y el estado de una
  herramienta externa, sin arriesgar datos que sí importan.
- Comprobar si tu repositorio se explica solo, en vez de suponerlo.

## Conceptos Clave

**Un encargo amplio no es gratis, aunque el resultado esté en verde.** Pedir
"implementa todo lo que falta" cuesta menos escribirlo que "implementa
exactamente esto", y por eso es tentador bajo presión de tiempo. El precio no
se ve en el momento: se ve en el diff, cuando aparece algo que no pediste y
tienes que decidir si te quedas con ello, lo quitas, o dejas que arrastre el
resto del cambio.

**Corregir, rebobinar y empezar limpio resuelven cosas distintas.** Corregir
hacia adelante —decirle a Claude qué quitar y qué conservar— cuesta poco
cuando el desvío es pequeño y localizado: sigues teniendo todo el trabajo
bueno delante. Rebobinar vuelve a un punto anterior de golpe, conversación y
archivos incluidos, y por eso cuesta más cuando ya hiciste algo de valor
después de ese punto. Y cuando el desvío es tan grande y tan enredado que ni
corregir ni rebobinar salen más baratos que repetir, la opción que queda es
empezar limpio: descartar la rama entera y volver a plantear el encargo desde
`main`, con lo que ya aprendiste sobre lo que salió mal. Ninguno de los tres
es el correcto por defecto; la pregunta es qué se pierde con cada uno.

**`/rewind` revierte lo que Claude editó con su herramienta de archivos, no lo
que ejecutó con un comando.** Cuando Claude aplica una migración con `uv run
alembic upgrade head`, eso corre como un comando de shell: cambia tu base de
datos, no un archivo que `/rewind` esté vigilando. Si rebobinas a un punto
anterior a esa migración, el archivo de la migración desaparece de tu
repositorio, pero la base de datos sigue exactamente donde la dejó el comando.
Los dos dejan de coincidir, y ese desajuste es real: lo vas a provocar y a
resolver hoy.

**Tu repositorio es el traspaso, o no lo es.** `/resume` te devuelve tu
conversación entera, con cada herramienta que se ejecutó. Eso solo sirve si
eres tú, en tu máquina, con esa conversación guardada. Alguien que clona tu
repositorio no tiene nada de eso: solo tiene lo que escribiste en los
commits, el contrato y la configuración. Si esa persona no puede reconstruir
las decisiones con lo que hay escrito, el traspaso no existe, aunque tú
recuerdes cada detalle.

## Comandos Nuevos

| Comando o control | Uso |
|---|---|
| `--continue` | Retoma la conversación más reciente de este directorio, sin selector |
| `/rename` | Pone nombre a la sesión, para encontrarla y retomarla por ese nombre |
| `/branch` | Copia la conversación hasta este punto y cambia a la copia, dejando la original intacta |
| `/fork` | Copia la conversación en una sesión nueva, en segundo plano, y tú sigues en esta |

`Esc` apareció en la sesión 1. `/rewind`, `Esc Esc` y `/resume` aparecieron en
la sesión 4. Hoy `/rewind` se usa con una pregunta distinta: no solo qué
revierte, sino qué **no** revierte, con un caso real delante. Y `/resume` se
usa para algo que la sesión 4 no necesitaba: comprobar si lo que recuperas te
sirve solo a ti, o le sirve a cualquiera.

`/diff` y `/context` ya aparecieron. Hoy `/diff` es la herramienta con la que
decides si un encargo se salió de lo pedido, y `/context` cierra la sesión
como en la 5.

## Validación General

Pídele a Claude la comprobación completa y léela entera antes de marcar nada:

```text
Comprueba el estado del proyecto y dame el resultado de cada punto por separado,
sin corregir nada:

1. La rama actual y si el árbol de trabajo está limpio.
2. Los commits de main que no estaban antes de hoy, uno por línea.
3. uv run alembic current, y si coincide con la revisión más reciente que existe
   en alembic/versions/.
4. uv run alembic upgrade head, después downgrade base, después upgrade head.
5. uv run pytest -q y uv run ruff check .
6. La respuesta de POST /tasks, GET /tasks con filtros combinados, y
   GET /tasks?overdue=true, contra la API corriendo.
7. Un intento de DELETE /projects/{id} sobre un proyecto con tareas.
8. Si queda algo del contrato de Proyectos o Tareas sin implementar o sin
   probar.
9. Contra la API corriendo: un CRUD completo de un proyecto y de una tarea que
   no hayas probado todavía en esta sesión —crear, leer, actualizar y borrar
   cada uno—, con el código de estado de cada respuesta.

Si algo falla, dime qué falló y detente. No lo arregles.
```

La sesión está completa si:

- [ ] `main` contiene proyectos, tareas v1 y tareas v2, integradas desde solicitudes de cambios.
- [ ] `DELETE /projects/{id}` sobre un proyecto con tareas responde `409`.
- [ ] `GET /tasks` admite `project_id` y `state_id`, solos y combinados, con orden estable.
- [ ] `GET /tasks?overdue=true` solo devuelve tareas vencidas y sin estado `HECHA`.
- [ ] La migración sube, baja y vuelve a subir sin error, y `alembic current` coincide con el archivo más reciente del repositorio.
- [ ] Sabes decir un caso concreto donde `/rewind` no revirtió algo que esperabas.
- [ ] Le pediste a una conversación sin tu contexto que describiera el proyecto, y comparaste su respuesta con lo que tú sabes.
- [ ] Ninguna rama queda abierta sin integrar.
- [ ] Un CRUD completo de un proyecto y de una tarea responde lo que dice el contrato, endpoint por endpoint.

## Limpieza

Detén los contenedores sin eliminar volúmenes, igual que en la sesión 5. El
Lab 02 no toca el volumen: el desajuste que provoca se recupera con
`alembic stamp`, sin borrar ningún dato. Si hiciste el desafío opcional y ahí
sí recreaste el volumen, confirma que el contenedor vuelve a estar sano antes
de cerrar.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) te pide provocar la misma
desincronización del Lab 02, pero con una migración que sí cambia el esquema
—no una vacía— y encontrar una salida sin recrear el volumen.

## Cierre

Preguntas de repaso:

- ¿Qué encargo diste en el Lab 02, y qué hizo Claude que no le pediste?
- Para ese desvío, ¿corregir hacia adelante te habría costado más o menos que rebobinar?
- Después de rebobinar en el paso de la migración, ¿qué comando te reveló el desajuste, y qué te dijo exactamente?
- ¿Qué le faltaba a tu repositorio para que una conversación sin contexto describiera bien el proyecto, y qué le añadiste?
- De las dos skills que ya tienes, ¿cuál usaste hoy sin cambiarla, y sobre qué contrato distinto?

## Versión

Material revisado el **2 de septiembre de 2026** con Claude Code **2.1.252** y
la documentación oficial de checkpointing y gestión de sesiones. Comprueba tu
versión con `claude --version` y la disponibilidad local con `/help`.

- [Checkpointing](https://code.claude.com/docs/en/checkpointing)
- [Gestión de sesiones](https://code.claude.com/docs/en/sessions)

## Estado Final del Repositorio

La sesión 7 parte exactamente de aquí.

En `~/curso-claude/curso-claude-code-api`, con `main` en verde y sin ramas
abiertas:

| Ruta | Origen |
|---|---|
| El plan de tareas, en `docs/` | Lo escribe tu skill en el Lab 01, cubriendo v1 y v2 |
| Migraciones, modelos y endpoints de `tasks` | Implementación de los Labs 01 y 02 |
| El contrato de Proyectos, cerrado | El `409` que la sesión 5 dejó sin probar, cerrado en el Lab 01 |
| Cualquier ajuste al traspaso escrito | Lo que el Lab 03 encontró que faltaba |

El contrato completo de la API —Proyectos y Tareas, v1 y v2— está implementado
y probado. Ningún endpoint nuevo se añade después de hoy.

## Preparación para la Sesión 7

Antes de la clase:

- Deja `main` en verde, con el contrato completo implementado.
- Actualiza tu copia del material:

```bash
cd $CURSO && git pull
```
