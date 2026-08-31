# Sesión 4: Ejecutar y Publicar

## Objetivo

Convertir un plan acordado en código verificado sin que el alcance crezca por el
camino. Auditas lo que el plan deja abierto, diriges sus incrementos uno a uno,
conviertes en configuración los permisos que hoy apruebas a mano, y cierras con
el trabajo publicado en un remoto tuyo.

El problema profesional de hoy: **un plan aprobado, ejecutado sin límites y sin
publicar**. Que el plan esté escrito no impide que el alcance crezca mientras se
ejecuta, ni que el resultado se quede en tu disco.

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — La persistencia en verde](labs/01-persistencia-en-verde/README.md) | 50 |
| Conceptos: el directorio `.claude` y el coste de aprobar a mano | 8 |
| [Lab 02 — Configurar el directorio `.claude`](labs/02-configurar-claude/README.md) | 22 |
| [Lab 03 — Publicar el trabajo](labs/03-publicar-el-trabajo/README.md) | 30 |
| Cierre y decisión transferible | 10 |

## Materiales

- Tu repositorio `~/curso-claude/curso-claude-code-api`, en la rama
  `feature/persistencia`.
- `docs/plan.md`, el plan que acordaste en la sesión 3. Lo escribió Claude en tu
  conversación, así que el tuyo no es idéntico al de tus compañeros: tendrá tres
  incrementos o cinco, y puede dejar decisiones sin cerrar.
- Docker arrancado en tu máquina. Los contenedores del proyecto los levanta
  Claude.
- Una cuenta de **GitHub o GitLab** ya creada, con acceso al correo con el que
  la registraste.

Si ya ejecutaste por tu cuenta la sección **Terminar la Persistencia** de la
sesión 3, no rehagas el trabajo: el Lab 01 te dice cómo comprobar lo que tienes
y dónde retomar.

A partir de hoy no vuelves a teclear los comandos del proyecto. `uv`, `docker`,
`alembic`, `pytest` y `git` los ejecuta Claude, y tú lees lo que informa. Los
únicos comandos que escribes son los de la propia herramienta.

## Laboratorios

| Lab | Qué haces | Qué descubres |
|---|---|---|
| [01 — La persistencia en verde](labs/01-persistencia-en-verde/README.md) | Auditas el plan, cierras las decisiones que dejó abiertas y diriges sus incrementos, uno por commit | Cuántas veces te pide permiso una tarea de este tamaño, y qué acabas aprobando sin leer |
| [02 — Configurar el directorio `.claude`](labs/02-configurar-claude/README.md) | Conviertes esos permisos en `.claude/settings.json`, y proteges el volumen que acabas de poblar | Que una regla escrita decide antes de que te pregunten, y que `deny` gana sobre lo que tú mismo autorizarías por inercia |
| [03 — Publicar el trabajo](labs/03-publicar-el-trabajo/README.md) | Creas el repositorio remoto, conectas el tuyo y publicas las dos ramas | Que el historial que escribió Claude se lee distinto cuando lo abre otra persona |

## Al finalizar esta sesión podrás

- Auditar un plan antes de ejecutarlo y cerrar sus decisiones abiertas por
  escrito, en vez de dejar que las cierre el agente.
- Dirigir una tarea larga por incrementos, con un commit por incremento y una
  comprobación entre uno y el siguiente.
- Distinguir lo que le pides a Claude de lo que Claude tiene permitido hacer, y
  escribir la segunda parte en `.claude/settings.json`.
- Bloquear una operación destructiva concreta con una regla, sin depender de
  acordarte de ella.
- Recuperar un turno que se desvió con `/rewind` y retomar una conversación
  anterior con `/resume`.
- Publicar un repositorio local en un remoto propio y leer su historial como lo
  leería alguien que no estuvo.

## Conceptos Clave

**Un plan aprobado no es un plan cerrado.** El que escribiste en la sesión 3
suele traer una sección de decisiones aplazadas: propone un driver o una capa
de acceso, y deja la confirmación para "el incremento 1". Si llegas ahí sin
haberla cerrado, la cierra Claude, y lo hará razonablemente y sin avisarte. La
diferencia entre dirigir y acompañar está casi siempre en decisiones así:
pequeñas, técnicas y fáciles de delegar por inercia.

**Instrucción y permiso no son lo mismo.** Cuando escribes "no toques `.env`" en
un encargo, estás pidiendo algo. Cuando lo escribes en `.claude/settings.json`,
estás decidiendo algo. Lo primero depende de que el modelo lo tenga presente
veinte turnos después; lo segundo se aplica antes de que la herramienta llegue a
ejecutarse. Hoy solo usas la forma más simple de esa idea —una lista de lo
permitido y una lista corta de lo prohibido—, y el curso vuelve sobre ella
cuando el riesgo lo justifique.

**El directorio `.claude` es configuración del proyecto, y se versiona.** No es
una preferencia tuya: viaja en el repositorio, se revisa en el diff y cambia
cómo trabaja cualquiera que clone el proyecto. Por eso entra en la misma rama
que el código y se explica en su commit, igual que un cambio en `pyproject.toml`.

**Publicar cambia quién es el lector.** Mientras el historial vive en tu disco,
los mensajes de commit son notas para ti. En cuanto hay un remoto, son la única
explicación disponible para quien llegue después. Un mensaje escrito por un
agente que acaba de hacer el cambio suele describir el *qué* con precisión y
omitir el *por qué*, que es justo lo que no se deduce del diff. Hoy lo compruebas
leyendo tu propio historial desde fuera.

## Comandos Nuevos

| Comando o control | Uso |
|---|---|
| `/permissions` | Ver y editar qué tiene permitido la sesión, y en qué archivo queda escrito |
| `/rewind` | Volver a un punto anterior de la conversación, del código, o de ambos |
| `Esc Esc` | Atajo que abre el mismo selector de `/rewind` |
| `/resume` | Retomar una conversación anterior de este directorio |

`/diff` y `/context` ya aparecieron en sesiones anteriores. Aquí `/diff` revisa
un cambio que llegó en varias tandas separadas, no en una.

`/rewind` no es `git`. Deshace turnos de la conversación y los cambios de
archivo que Claude hizo en ellos; no toca commits ya confirmados. Por eso importa
el orden que practicas hoy: confirmar cada incremento antes de empezar el
siguiente deja `/rewind` como red de seguridad del incremento en curso y solo de
ese.

## Validación General

Pídele a Claude la comprobación completa y léela entera antes de marcar nada:

```text
Comprueba el estado del proyecto y dame el resultado de cada punto por separado,
sin corregir nada:

1. La rama actual y si el árbol de trabajo está limpio.
2. uv run alembic upgrade head, después downgrade base, después upgrade head.
3. uv run pytest -q y uv run ruff check .
4. La respuesta de GET /states, obtenida contra la aplicación en memoria como
   hacen los tests. No levantes ningún servidor.
5. Los remotos configurados y qué ramas existen en cada uno.
6. Los últimos ocho commits en una línea cada uno.

Si algo falla, dime qué falló y detente. No lo arregles.
```

La sesión está completa si:

- [ ] Las decisiones que el plan dejaba abiertas quedaron cerradas por escrito antes del primer incremento.
- [ ] Cada incremento ejecutado tiene su commit, y ningún commit mezcla dos.
- [ ] La migración sube y baja en los dos sentidos sin error.
- [ ] `GET /states` devuelve los cuatro estados del contrato, y dos llamadas seguidas los devuelven en el mismo orden.
- [ ] Ningún archivo fuera del alcance del plan aparece en el diff de la rama.
- [ ] `.claude/settings.json` existe, está versionado y `/permissions` lo reconoce como origen de las reglas.
- [ ] Comprobaste que una regla bloquea de verdad, y sabes cuáles de las tuyas no puedes comprobar sin arriesgarte a romper algo.
- [ ] El repositorio remoto existe y tiene `main` y `feature/persistencia`.
- [ ] Leíste tu historial desde el remoto y anotaste qué commit no se entiende sin ti.

## Limpieza

La limpieza es el último paso del
[Lab 03](labs/03-publicar-el-trabajo/README.md): los contenedores se detienen y
el volumen se queda intacto, porque la sesión 5 continúa sobre estos datos.

Tu regla del Lab 02 debería impedir ese borrado aunque se lo pidieras. No lo
pruebes para verlo: si la regla no cubre la variante exacta del comando, la
prueba te cuesta el trabajo del día.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) instala la CLI de tu proveedor
—`gh` para GitHub, `glab` para GitLab—, la autentica y comprueba que Claude puede
usarla. La sesión 5 abre el primer pull o merge request desde la conversación, y
sin esa CLI no es posible: hazlo antes de la próxima clase.

## Cierre

Preguntas de repaso:

- ¿Qué decisión del plan cerró Claude por ti, y en qué incremento te diste cuenta?
- De todos los permisos que aprobaste en el Lab 01, ¿cuál no habrías aprobado si te lo hubieran preguntado una sola vez, por escrito?
- ¿Qué regla de tu `settings.json` protege algo que tú mismo habrías roto por inercia?
- Lee tus mensajes de commit. ¿Cuál no se entiende sin haber estado aquí?

## Versión

Material revisado el **31 de agosto de 2026** con Claude Code **2.1.251** y la
documentación oficial de permisos, configuración y sesiones. Comprueba tu versión
con `claude --version` y la disponibilidad local con `/help`.

- [Modos de permiso](https://code.claude.com/docs/en/permission-modes)
- [Configuración](https://code.claude.com/docs/en/settings)
- [El directorio .claude](https://code.claude.com/docs/en/claude-directory)
- [Sesiones](https://code.claude.com/docs/en/sessions)

## Estado Final del Repositorio

La sesión 5 parte exactamente de aquí.

En `~/curso-claude/curso-claude-code-api`, rama `feature/persistencia`, con
`main` sin tocar desde la sesión 2:

| Ruta | Origen |
|---|---|
| `docs/plan-persistencia.md` | El plan de la sesión 3, renombrado en el Lab 01 |
| Configuración de conexión y migraciones | Generadas por Claude, incremento a incremento |
| Migración de `states` con su seed | Un incremento propio |
| `GET /states` y su test | El incremento que cierra el trabajo de hoy |
| `.claude/settings.json` | Escrito por ti en el Lab 02 |

`feature/persistencia` **no se integra hoy**. Se queda publicada y esperando: la
sesión 5 la integra desde un pull o merge request, que es donde ese trabajo se
revisa de verdad.

## Preparación para la Sesión 5

La sesión 5 cierra la persistencia con una revisión hecha desde fuera y empieza
a entregar cambios que otra persona puede leer sin ayuda.

Antes de la clase, dos cosas:

- Completa el desafío opcional. La CLI de tu proveedor es requisito, no adorno.
- Actualiza tu copia del material:

```bash
cd $CURSO && git pull
```
