# Sesión 5: Revisar e Integrar

## Objetivo

Convertir trabajo terminado en trabajo entregado, y decidir cuánta autonomía le
concedes a Claude cuando la tarea ya no cabe en un encargo por incremento.
Entregas e integras la rama que dejaste pendiente, construyes tus dos primeras
herramientas propias y las usas para dirigir un cambio que llega de una sola
vez.

El problema profesional de hoy: **un cambio verde que nadie puede revisar**. La
suite pasa, la rama existe y el trabajo sigue siendo tuyo y solo tuyo: nadie
puede leerlo sin que se lo cuentes.

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — La entrega que faltaba](labs/01-la-entrega-que-faltaba/README.md) | 25 |
| [Lab 02 — Qué merece ser una skill](labs/02-que-merece-una-skill/README.md) | 30 |
| [Lab 03 — Planificar y ejecutar con autonomía](labs/03-planificar-y-ejecutar/README.md) | 35 |
| [Lab 04 — El bloque que nadie puede revisar](labs/04-partir-el-bloque/README.md) | 25 |
| Cierre y decisión transferible | 5 |

## Materiales

- Tu repositorio `~/curso-claude/curso-claude-code-api`, en la rama
  `feature/persistencia`, publicada y sin integrar.
- Docker arrancado. Los contenedores los levanta Claude.
- La CLI de tu proveedor —`gh` para GitHub, `glab` para GitLab— instalada y
  autenticada. Es el desafío de la sesión 4 y hoy es **requisito**: sin ella no
  puedes abrir la solicitud de cambios desde la conversación.
- `docs/contrato-api.md`, sección **Proyectos**. Es la fuente de lo que hay que
  implementar, y hoy no se negocia ni se amplía.
- La [referencia rápida](referencia-rapida.md) de la sesión, con la forma de una
  skill y los tres frenos del Lab 03.

**Tu base de datos puede estar sin esquema**, y es normal. Si la estrategia de
pruebas que acordaste aplica la migración al abrir la suite y la revierte al
cerrarla, el último `pytest` de la sesión anterior dejó la base vacía. El
volumen sigue ahí. El Lab 01 lo comprueba antes de tocar nada y lo aplica en su
paso 2; ningún lab de hoy supone que haya datos.

Sigues sin teclear los comandos del proyecto. `uv`, `docker`, `alembic`,
`pytest`, `git`, `curl` y la CLI de tu proveedor los ejecuta Claude, y tú lees
lo que informa. Los únicos comandos que escribes son los de la herramienta.

## Laboratorios

| Lab | Qué haces | Qué descubres |
|---|---|---|
| [01 — La entrega que faltaba](labs/01-la-entrega-que-faltaba/README.md) | Preguntas a la API antes de tocar nada, aplicas el esquema, abres la solicitud de cambios de `feature/persistencia` y la integras | Que una suite verde no responde la misma pregunta que una petición real, y qué se ve de tu trabajo cuando lo abre alguien que no estuvo |
| [02 — Qué merece ser una skill](labs/02-que-merece-una-skill/README.md) | Pides tres recomendaciones sobre tu propio repositorio, decides cuáles merecen existir y construyes la primera | Que rechazar una recomendación cuesta más criterio que aceptarla, y que hay cosas que ya vienen resueltas |
| [03 — Planificar y ejecutar con autonomía](labs/03-planificar-y-ejecutar/README.md) | Planificas `projects` con tu skill, apruebas el plan y dejas que Claude lo implemente entero sin pedirte permiso a cada paso | Que tus reglas de la sesión 4 siguen mandando cuando dejas de aprobar a mano, y cuáles no cubrían lo que hoy hace falta |
| [04 — El bloque que nadie puede revisar](labs/04-partir-el-bloque/README.md) | Conviertes un cambio sin repartir en varios commits con una intención cada uno con tu segunda skill, y repites el minado de candidatas con toda la señal de hoy | Que el reparto de un cambio en commits es una decisión tuya, y que con más señal real el mismo ejercicio del Lab 02 sí produce candidatas defendibles |

## Al finalizar esta sesión podrás

- Comprobar una API como la ve quien la consume, y no solo como la ven sus
  pruebas.
- Publicar una solicitud de cambios con una descripción que otra persona pueda
  revisar sin haber estado en tu conversación.
- Integrar una rama y cerrarla, dejando `main` en verde.
- Decidir si una repetición merece convertirse en herramienta o solo necesita
  una instrucción mejor, y defender la decisión con un criterio en vez de una
  intuición.
- Escribir una skill de proyecto, versionarla y comprobar que la sesión la
  reconoce.
- Separar el plan de un cambio de su ejecución, y aprobar el primero antes de
  permitir el segundo.
- Trabajar con menos interrupciones sabiendo exactamente qué te sigue
  protegiendo.
- Repartir un cambio grande en commits con una intención cada uno, y dejar ese
  criterio escrito para no volver a decidirlo desde cero.

## Conceptos Clave

**Verde no es entregado.** Hasta hoy toda la verificación del curso ocurrió
dentro de las pruebas: la aplicación en memoria, sin servidor. Eso comprueba el
comportamiento, pero no comprueba que la API funcione. Basta una migración sin
aplicar para que la suite pase y el primer `GET` falle, y puede que sea lo
primero que veas hoy. La diferencia entre las dos comprobaciones no es de rigor:
es de pregunta. Una responde "el código hace lo que acordamos"; la otra, "el
servicio está en pie".

**Una skill no es un prompt guardado.** Vive en `.claude/skills/`, se versiona
con el proyecto y la invocas por su nombre. Y hace dos cosas que un texto
copiado no puede: llega con contexto recién obtenido —una skill puede pedir el
diff en el momento de ejecutarse, no el de escribirse— y se comparte, así que
deja de ser tu forma de trabajar y pasa a ser la del repositorio. La pregunta
que decide si algo merece ser una skill no es si es útil, sino si **ya lo has
repetido**. La convención de mensajes de commit que tuviste que pedir en cada
encargo de la sesión pasada es un candidato claro. Aplicar una migración
no lo es: eso es una línea, y ya está en el README.

**Planificar y ejecutar son dos permisos distintos.** Claude Code trae un modo
que bloquea toda edición hasta que apruebes un plan. Eso resuelve el *cuándo*:
nada se toca antes de que digas que sí. No resuelve el *qué*, que es lo que
cambia entre proyectos: contra qué documento se planifica, en cuántos
incrementos, con qué comprobación cada uno y dónde queda escrito. Lo primero lo
da la herramienta; lo segundo lo escribes tú, y por eso las dos cosas se usan
juntas y no compiten.

**La autonomía se concede sobre reglas, no sobre confianza.** Hoy trabajas por
primera vez sin aprobar cada acción: otro modelo revisa lo que Claude va a hacer
en lugar de preguntártelo a ti. Eso sería imprudente si no hubieras escrito nada
antes, y no lo es porque la sesión 4 dejó tres listas en
`.claude/settings.json`. Lo que prohibiste sigue prohibido en todos los modos, y
lo que pediste que se te preguntara se te sigue preguntando. La configuración de
ayer es la condición que hace razonable la comodidad de hoy, y también vas a
descubrir dónde se quedó corta.

**Configuración y procedimiento no son lo mismo.** Ya separaste lo que le pides
a Claude de lo que Claude tiene permitido. Hoy aparece la tercera distinción de
esa familia, y el criterio es si la decisión **cambia según el
caso**. Qué prefijo lleva un mensaje de commit depende de qué cambió: es juicio,
y va dentro de la skill que lo aplica. Que tus commits no lleven la firma de
coautoría de Claude no depende de nada: vale para todos, y va en
`.claude/settings.json`. Meter una regla fija dentro de un procedimiento la deja
activa solo cuando lo invocas, y eso es peor que no tenerla, porque parece que
está.

## Comandos Nuevos

| Comando o control | Uso |
|---|---|
| `/skills` | Ver las skills disponibles y con qué nombre se invoca cada una |
| `/reload-skills` | Recoger una skill que acabas de crear o cambiar, sin cerrar la sesión |
| `/plan` | Entrar en el modo que bloquea ediciones hasta aprobar un plan, y volver a ver el plan de la sesión |
| `Ctrl+G` | Abrir el plan propuesto en tu editor para cambiarlo antes de aprobarlo |
| `/` | El menú de comandos y skills, donde aparece la tuya junto a las incorporadas |

`Shift+Tab` apareció en la sesión 1 como la forma de cambiar el modo de
permisos. Hoy es la primera vez que importa a qué modo cambias, y usas dos que
tienen nombre propio:

- **Plan mode**: bloquea toda edición hasta que apruebes un plan. Es el modo en
  el que entras con `/plan`.
- **Auto mode**: otro modelo revisa las acciones antes de que se ejecuten, en
  lugar de preguntártelas a ti.

Los vas a leer así, en inglés, porque así los nombra la herramienta: la barra de
estado de tu terminal dice cuál está activo, y también cuándo estás en el modo
manual que has usado hasta hoy.

`/permissions` apareció en la sesión 4 para escribir reglas. Hoy le pides algo
distinto: la lista de lo que se te ha denegado durante la sesión. Cuando dejas
de aprobar a mano, esa lista es la única forma de saber qué se intentó y no se
hizo.

`/code-review` viene incorporado en Claude Code y hoy solo lo miras: aparece en
el Lab 02 como una de las cosas que **no** tienes que construir.

## Validación General

Pídele la comprobación completa y léela entera antes de marcar nada:

```text
Comprueba el estado del proyecto y dame el resultado de cada punto por separado,
sin corregir nada:

1. La rama actual, si el árbol de trabajo está limpio y qué ramas existen en el
   remoto.
2. Los commits de main que no estaban antes de hoy, uno por línea.
3. uv run alembic upgrade head, después downgrade base, después upgrade head.
4. uv run pytest -q y uv run ruff check .
5. La respuesta de GET /projects y de GET /states contra la API corriendo, no
   contra la aplicación en memoria.
6. Qué skills de proyecto existen en este repositorio y qué hace cada una,
   leyendo sus archivos.
7. Si queda algo del contrato de Proyectos sin implementar o sin probar.

Si algo falla, dime qué falló y detente. No lo arregles.
```

La sesión está completa si:

- [ ] `main` contiene la persistencia y `GET /states`, integradas desde una solicitud de cambios.
- [ ] La rama `feature/persistencia` ya no existe, ni en local ni en el remoto.
- [ ] Comprobaste la API contra un servidor real, y no solo con la suite.
- [ ] El motivo por el que rechazaste al menos una de las tres recomendaciones quedó escrito en el mensaje de un commit.
- [ ] Existen al menos dos skills de proyecto, versionadas, y `/skills` las reconoce.
- [ ] El plan de `projects` está aprobado y escrito en `docs/` antes del primer archivo de código.
- [ ] Los cinco endpoints de Proyectos responden lo que dice el contrato, con el esquema exacto y el orden estable.
- [ ] Ningún commit de hoy mezcla dos intenciones.
- [ ] Sabes qué te denegó Claude mientras trabajabas con autonomía y si fue acertado, o que no te denegó nada.
- [ ] Declaraste qué parte del contrato de Proyectos sigue sin poder probarse.

## Limpieza

La limpieza es el último paso del
[Lab 04](labs/04-partir-el-bloque/README.md): los contenedores se detienen y el
volumen se queda intacto. No hace falta conservar datos —la migración los
recrea—, pero borrar el volumen tampoco aporta nada, y tu regla de la sesión 4
debería impedirlo.

Vuelve a modo manual antes de cerrar. Terminar la clase con la sesión en
autonomía y retomarla mañana sin recordarlo es la forma más fácil de que un
encargo amplio haga más de lo que esperabas.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) recoge la recomendación del
Lab 02 que decidiste construir y no te dio tiempo, con una condición: que se
ejecute **en su propio contexto** y te devuelva solo el resultado. Una skill lo
declara en su cabecera, y es la manera de que un procedimiento que produce mucha
salida —arrancar la API, llamar a varios endpoints, comparar cada respuesta con
el contrato— no te llene la conversación con texto que no vas a volver a leer.

## Cierre

Preguntas de repaso:

- ¿En qué se diferenció lo que te dijo la suite de lo que te dijo la API cuando la levantaste?
- De las tres recomendaciones del Lab 02, ¿cuál rechazaste y qué criterio usaste?
- ¿Qué decisión tomó Claude durante la implementación que tú habrías tomado distinta, y en qué momento te diste cuenta?
- ¿Qué regla de tu `settings.json` te frenó hoy, y cuál echaste de menos?
- Mira tu solicitud de cambios como si la abriera otra persona. ¿Qué le falta para poder aprobarla sin preguntarte nada?

## Versión

Material revisado el **1 de septiembre de 2026** con Claude Code **2.1.252** y
la documentación oficial de skills, modos de permiso y planificación. Comprueba
tu versión con `claude --version` y la disponibilidad local con `/help`.

- [Skills](https://code.claude.com/docs/en/skills)
- [Modos de permiso](https://code.claude.com/docs/en/permission-modes)
- [Permisos](https://code.claude.com/docs/en/permissions)
- [Comandos](https://code.claude.com/docs/en/commands)

## Estado Final del Repositorio

La sesión 6 parte exactamente de aquí.

En `~/curso-claude/curso-claude-code-api`, con `main` en verde y sin ramas
abiertas:

| Ruta | Origen |
|---|---|
| El plan de proyectos, en `docs/` | Lo escribe tu skill en el Lab 03; el nombre lo decide ella |
| Migración de `projects` y sus cinco endpoints | La implementación del Lab 03, repartida en commits en el Lab 04 |
| `.claude/skills/` con al menos dos skills | `planificar-incremento` y `segmentar-commits`, del Lab 02 y el Lab 04. Pueden ser más: el Lab 04 construye las candidatas que sobrevivan a su segunda ronda de minado |
| `.claude/settings.json` | El de la sesión 4, con la coautoría configurada en el Lab 04 y los permisos que hoy hayan hecho falta |

`feature/persistencia` y `feature/projects` quedan integradas y borradas: a
partir de ahora, una rama abierta es trabajo en curso, no historia.

## Preparación para la Sesión 6

Antes de la clase:

- Deja `main` en verde. Si algo del contrato de Proyectos quedó sin implementar,
  termínalo fuera de clase y confírmalo en su propia rama.
- Comprueba que tus skills se invocan por su nombre y hacen lo que dice su
  archivo. Las vas a seguir usando.
- Actualiza tu copia del material:

```bash
cd $CURSO && git pull
```
