# Sesión 7: Reproducir y Depurar

## Objetivo

Cerrar dos fallos reales que una explicación plausible dejó sin ver —uno en
una skill propia, otro declarado y nunca probado—, escribir las reglas que
evitan que se repitan, y dejar el contrato completo demostrado de una forma
que cualquiera pueda repetir sin preguntarte.

El problema profesional de hoy: **una explicación plausible reemplaza a la
reproducción**, y por eso un fallo real —en tu código o en tus propias
herramientas— puede pasar sesiones enteras sin que nadie lo vea.

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — Rojo antes que Arreglo](labs/01-rojo-antes-arreglo/README.md) | 25 |
| [Lab 02 — Lo que no Vuelve a Pasar](labs/02-lo-que-no-vuelve-a-pasar/README.md) | 30 |
| [Lab 03 — Lo que Cualquiera Puede Probar](labs/03-lo-que-cualquiera-puede-probar/README.md) | 50 |
| Cierre y decisión transferible | 15 |

## Materiales

- Tu repositorio `~/curso-claude/curso-claude-code-api`, con `main` en verde:
  el contrato completo —proyectos y tareas, v1 y v2— desde la sesión 6.
- Docker arrancado. Los contenedores los levanta Claude.
- `.claude/skills/` con `planificar-incremento` y `segmentar-commits`.
- `docs/contrato-api.md` completo.
- La [referencia rápida](referencia-rapida.md) de la sesión.

Sigues sin teclear los comandos del proyecto. `uv`, `docker`, `alembic`,
`pytest`, `git` y la CLI de tu proveedor los ejecuta Claude, y tú lees lo que
informa.

## Laboratorios

| Lab | Qué haces | Qué descubres |
|---|---|---|
| [01 — Rojo antes que Arreglo](labs/01-rojo-antes-arreglo/README.md) | Reproduces el reparto que tu skill `segmentar-commits` hace mal, antes de corregirla | Que un fallo se reproduce con un caso real, no se explica desde la memoria |
| [02 — Lo que no Vuelve a Pasar](labs/02-lo-que-no-vuelve-a-pasar/README.md) | Escribes reglas en `.claude/rules/` que capturan lo que aprendiste, y podas tu `CLAUDE.md` | Que una regla escrita cambia lo que Claude hace, no solo lo que promete |
| [03 — Lo que Cualquiera Puede Probar](labs/03-lo-que-cualquiera-puede-probar/README.md) | Compruebas si tu repositorio se explica solo, cierras un hueco real, y dejas `api.http` y un README que prueban el contrato completo | Que retomar tu propio trabajo no es lo mismo que retomarlo otra persona, y que una suite verde no basta para demostrar que algo funciona |

## Al finalizar esta sesión podrás

- Reproducir un fallo con un caso real antes de proponer una corrección, sea
  en tu código o en una herramienta propia.
- Corregir una skill que falla sin tocar el resultado del día en que la
  descubriste.
- Escribir reglas de proyecto acotadas por archivo o siempre activas, y
  comprobar que cambian el comportamiento de Claude, no solo que existen.
- Decidir qué merece vivir en `CLAUDE.md` y qué merece su propia regla.
- Comprobar si tu repositorio se explica solo a alguien sin tu contexto, y
  cerrar el hueco que encuentres.
- Demostrar con una colección de peticiones y un README que el contrato
  completo funciona, sin depender de una conversación.

## Conceptos Clave

**Una explicación plausible reemplaza a la reproducción.** "Rechaza los
títulos vacíos" suena completo. "Reparte en commits separados" también.
Ninguna de las dos frases es falsa, y ninguna te dice si el código o la
skill hacen de verdad lo que la frase promete. La única manera de saberlo es
forzar el caso real —un carácter que nadie prueba, un cambio que nadie
audita commit a commit— y mirar qué pasa antes de decidir que ya funciona.

**Un fallo en una herramienta propia es tan real como un fallo en la API.**
Una skill que reparte commits reescribiendo código en vez de usar el índice
de Git no se nota en ningún test de la aplicación: la suite sigue en verde,
porque el fallo está en el procedimiento que usas para entregar el cambio,
no en el cambio mismo. Diagnosticarlo pide el mismo método que cualquier
otro bug: reproducirlo con un caso concreto antes de tocar nada.

**Una regla en `.claude/rules/` no es lo mismo que un `CLAUDE.md` que sigue
creciendo.** Lo que aplica siempre —una convención de commits, un criterio
de pruebas— compite por espacio con lo que solo importa en un tipo de
archivo. Separar los dos no es organización: es la diferencia entre una
instrucción que Claude lee siempre y una que solo le llega cuando de verdad
hace falta, acotada por ruta.

**Una suite en verde demuestra que el código hace lo que el test decidió
probar, no que el contrato entero funciona.** Una colección de peticiones
ejecutable contra el servidor real, y un README que alguien sin tu contexto
puede seguir de punta a punta, prueban algo distinto: que el sistema
completo responde lo que promete, a cualquiera que lo intente, no solo a ti
en esta conversación.

## Comandos Nuevos

| Comando o control | Uso |
|---|---|
| `/rename` | Pone nombre a la sesión actual, para encontrarla y retomarla por ese nombre |

`--continue` retoma la conversación más reciente de este directorio, sin
selector: hace lo mismo que `--resume` con el nombre, cuando solo tienes una
sesión reciente ahí. `/resume` ya apareció en la sesión 4; hoy lo usas para
algo que esa sesión no necesitaba: comprobar si lo que recuperas te sirve
solo a ti, o le sirve a cualquiera que clone tu repositorio.

`/clear`, `/diff`, `/context` y `/skills` ya aparecieron. Hoy `/clear` simula
retomar el proyecto sin ningún contexto, `/diff` decide si una skill reparte
limpio, y `/context` cierra cada lab como en sesiones anteriores.

## Validación General

Pídele a Claude la comprobación completa y léela entera antes de marcar nada:

```text
Comprueba el estado del proyecto y dame el resultado de cada punto por separado,
sin corregir nada:

1. La rama actual y si el árbol de trabajo está limpio.
2. Los commits de main que no estaban antes de hoy, uno por línea.
3. uv run pytest -q y uv run ruff check .
4. uv run alembic downgrade base, después upgrade head, y si alembic current
   coincide con el archivo más reciente del repositorio.
5. Contra la API corriendo: una tarea con title igual a un único carácter
   U+200B, y el código de estado de la respuesta.
6. Qué archivos hay en .claude/rules/, y cuáles tienen paths en su
   encabezado.
7. Cuántas peticiones tiene api.http y cuántos endpoints tiene el contrato.
8. Si segmentar-commits arma cada commit con git add, o reescribiendo
   archivos.
9. Si README.md explica, paso a paso, cómo levantar el proyecto desde cero.

Si algo falla, dime qué falló y detente. No lo arregles.
```

La sesión está completa si:

- [ ] `segmentar-commits` arma cada commit con `git add`, no reescribiendo código.
- [ ] `.claude/rules/` tiene `testing.md`, `code-style.md` y `api-conventions.md`, y las tres cambian el comportamiento de Claude, no solo existen.
- [ ] Un título de un único `U+200B` responde `422` contra la API corriendo.
- [ ] `api.http` tiene una petición por cada endpoint del contrato, ejecutada y verificada.
- [ ] La migración completa sube, baja y vuelve a subir sin error.
- [ ] `README.md` lleva de cero a la API corriendo, probado con `/clear`.
- [ ] Le pediste a una conversación sin tu contexto que describiera el proyecto, y cerraste el hueco que encontraste.
- [ ] Todo el trabajo de los tres labs está integrado en `main`.

## Limpieza

Detén los contenedores sin eliminar volúmenes. Ninguno de los tres labs
toca el volumen de datos.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) te pide comparar una
captura de pantalla contra `api.http` como evidencia de que algo funciona, y
decidir cuál de las dos sobrevive a la siguiente pregunta que te hagan.

## Cierre

Preguntas de repaso:

- ¿Qué reprodujiste primero en el Lab 01: el fallo, o la corrección? ¿Por qué en ese orden?
- De las tres reglas que escribiste, ¿cuál comprobaste que cambiaba el comportamiento de Claude, y cómo lo comprobaste sin mencionarla?
- ¿Qué hueco encontró la conversación sin contexto del Lab 03, y dónde lo cerraste?
- ¿Qué demuestra `api.http` que `pytest` no demuestra?
- ¿Qué revisarías primero si alguien te dijera que tu skill de reparto volvió a fallar?

## Versión

Material revisado el **7 de septiembre de 2026** con Claude Code **2.1.252**
y la documentación oficial de reglas de proyecto y skills integradas.
Comprueba tu versión con `claude --version` y la disponibilidad local con
`/help`.

- [Memoria y reglas de proyecto](https://code.claude.com/docs/en/memory)
- [Skills](https://code.claude.com/docs/en/skills)

## Estado Final del Repositorio

La sesión 8 parte exactamente de aquí.

En `~/curso-claude/curso-claude-code-api`, con `main` en verde y sin ramas
abiertas:

| Ruta | Origen |
|---|---|
| `.claude/skills/segmentar-commits/SKILL.md`, corregida | El fallo reproducido y cerrado en el Lab 01 |
| `.claude/rules/testing.md`, `code-style.md`, `api-conventions.md` | Escritas y comprobadas en el Lab 02 |
| `CLAUDE.md`, podado de lo que ya cubren las reglas nuevas | Decisión del Lab 02 |
| El título de una tarea, validado contra las categorías Unicode del contrato | El hueco que la sesión 6 dejó declarado, cerrado en el Lab 03 |
| `api.http` y `README.md`, reescritos | El Lab 03 |

El contrato completo de la API sigue siendo el de la sesión 6: ningún
endpoint nuevo se añade hoy. Lo que cambia es la evidencia de que funciona,
y las reglas que evitan que un fallo como los de hoy vuelva a pasar
desapercibido.

## Preparación para la Sesión 8

Antes de la clase:

- Deja `main` en verde, con las reglas y los artefactos de hoy integrados.
- Actualiza tu copia del material:

```bash
cd $CURSO && git pull
```
