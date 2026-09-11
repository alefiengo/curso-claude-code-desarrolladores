# Sesión 9: Delegar con Contexto Aislado

## Objetivo

Entregar un cambio a un agente que trabaja solo, y después entregar su
revisión a otros que no saben nada de él. Cada uno recibe la autoridad mínima
de su oficio, escrita en una línea, y tú te quedas con la única decisión que
no se delega: cuál de sus hallazgos es real.

El problema profesional de hoy: **una segunda opinión contaminada por la
conversación que produjo el cambio no es independiente.**

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — El que sí puede escribir](labs/01-el-que-si-puede-escribir/README.md) | 28 |
| [Lab 02 — El revisor que no estuvo ahí](labs/02-el-revisor-que-no-estuvo-ahi/README.md) | 28 |
| [Lab 03 — Misma autoridad, otra lente](labs/03-misma-autoridad-otra-lente/README.md) | 22 |
| [Lab 04 — Lo que sobrevive al triaje](labs/04-lo-que-sobrevive-al-triaje/README.md) | 27 |
| Cierre y decisión transferible | 15 |

## Materiales

- Tu repositorio `~/curso-claude/curso-claude-code-api`, con `main` en verde y
  sin ramas abiertas: el contrato completo, las tres reglas de
  `.claude/rules/`, las skills, los dos hooks de la sesión 8 y `openapi.json`
  al día.
- Docker arrancado. Los contenedores los levanta Claude.
- `docs/contrato-api.md`, que hoy es el documento contra el que revisan tus
  agentes y el que te da los motivos para rechazar un hallazgo.
- La [referencia rápida](referencia-rapida.md) de la sesión, con la tabla de
  qué contexto recibe cada forma de delegar.

Sigues sin teclear los comandos del proyecto. Hoy, además, hay trabajo que no
ejecuta ni Claude en tu hilo: lo ejecutan agentes que corren aparte y te
devuelven un resumen.

## Laboratorios

| Lab | Qué haces | Qué descubres |
|---|---|---|
| [01 — El que sí puede escribir](labs/01-el-que-si-puede-escribir/README.md) | Construyes el único subagente con autoridad para escribir y le sueltas un refactor acotado sin supervisarlo | Que lo que vuelve de un trabajo delegado es el relato del agente, y que el diff cuenta otra cosa |
| [02 — El revisor que no estuvo ahí](labs/02-el-revisor-que-no-estuvo-ahi/README.md) | Haces la misma pregunta tres veces: en tu sesión, con `/subtask` y con un subagente limpio | Que el veredicto cambia según cuánto de tu conversación haya leído quien revisa |
| [03 — Misma autoridad, otra lente](labs/03-misma-autoridad-otra-lente/README.md) | Ejecutas `/security-review` y después construyes un auditor con las mismas herramientas exactas que el revisor | Que el recorte de herramientas define lo que un agente no puede hacer, no lo que sabe mirar |
| [04 — Lo que sobrevive al triaje](labs/04-lo-que-sobrevive-al-triaje/README.md) | Construyes uno que ejecuta comprobaciones sin herramientas de edición, y trías sus hallazgos | Que un hallazgo correcto en general puede ser ruido aquí, y que distinguirlo es tuyo |

## Al finalizar esta sesión podrás

- Escribir un subagente de proyecto con la autoridad mínima de su oficio, y
  explicar qué hereda si no se la declaras.
- Distinguir las tres formas de delegar por el contexto que llevan: tu hilo,
  un delegado que hereda tu conversación, y un agente que arranca limpio.
- Decir qué carga un subagente al arrancar y qué no verá nunca.
- Pasarle a un agente limpio, dentro del encargo, lo que solo existe en tu
  conversación.
- Comparar una skill de revisión de fábrica con un revisor propio, y decir en
  qué se diferencian sus alcances.
- Triar hallazgos con evidencia: aceptar solo lo comprobado y rechazar citando
  dónde está escrita la decisión.
- Explicar por qué recortar herramientas no sustituye a una regla de permisos.

## Conceptos Clave

**Un subagente es una autoridad declarada, no un ayudante más.** Vive en
`.claude/agents/`, se versiona con el proyecto y su cuerpo es todo lo que sabe
de su oficio. La línea que decide de verdad es la de sus herramientas: si no
se la escribes, hereda todas las que tú tienes. La autoridad mínima no es el
valor por defecto; es una decisión que se toma cada vez.

**Y ese recorte tiene un límite conocido.** Quitarle las herramientas de
edición a un agente que sí puede ejecutar comandos no le impide escribir: le
impide escribir *con esas herramientas*. Es lo mismo que viste en la sesión 4,
cuando una regla sobre la herramienta de lectura no cubría el mismo archivo
leído con un comando. Las herramientas acotan por dónde puede pasar; los
permisos son los que miran el comando.

**Lo que vuelve de un trabajo delegado es un resumen, y un resumen es un
relato.** El agente trabaja en su propia ventana de contexto: sus pasos, sus
dudas y lo que descartó se quedan ahí. Lo que llega a tu conversación es su
versión de lo que hizo. Por eso la revisión se hace contra el código y el
diff, no contra el informe, y por eso quien lea el informe antes de revisar ya
no es independiente.

**Delegar tiene tres formas, y se distinguen por el contexto que llevan.** Tu
propio hilo lo sabe todo. `/subtask` y `/fork` mandan el trabajo aparte pero
con tu conversación completa, supuestos incluidos. Un subagente de
`.claude/agents/` arranca limpio: carga tu `CLAUDE.md` y una foto del
repositorio, y nada más. Cuál sirve depende de lo que pidas: para terminar
algo que ya empezaste, el que hereda; para una segunda opinión, el que no
puede estar de acuerdo contigo por inercia.

**Dos agentes con la misma autoridad pueden encontrar cosas distintas.** El
revisor y el auditor de hoy declaran exactamente las mismas herramientas. Lo
que los separa es el cuerpo del archivo: contra qué revisa cada uno y en qué
orden mira. Recortar herramientas decide lo que un agente **no puede hacer**;
el oficio lo decide lo que le escribiste.

**El triaje no se delega.** Un revisor que no conoce tu historia encuentra
cosas ciertas y cosas que solo parecen problemas porque contradicen una
decisión que se tomó hace sesiones. Aceptar exige evidencia; rechazar exige
citar dónde está escrita esa decisión. Sin esas dos reglas, una revisión
automática se convierte en una lista que nadie lee.

## Comandos Nuevos

| Comando o control | Uso |
|---|---|
| `.claude/agents/` | Donde viven los subagentes del proyecto, un archivo por agente |
| `@agent-<nombre>` | Invoca a un subagente concreto en vez de dejar que Claude elija |
| `/subtask` | Delega una tarea aparte **con** tu conversación completa, y devuelve el resultado a este hilo |
| `/security-review` | Revisión de seguridad de fábrica, sobre los cambios pendientes de la rama |

`/code-review` es otra skill incorporada y aparece en el Lab 02; compruébala
con `/skills` antes de usarla, porque no todas las instalaciones traen las
mismas. `/fork`, que ya usaste en la sesión 6, pertenece a la misma familia
que `/subtask`: los dos se llevan tu conversación.

`/list-agents` lista los subagentes que la sesión reconoce, pero no es el
equivalente exacto de `/skills` o `/hooks`: lista además otras sesiones y solo
está disponible donde la mensajería entre sesiones lo está. La comprobación que
siempre funciona es invocar al agente.

## Validación General

Pídele a Claude la comprobación completa y léela entera antes de marcar nada:

```text
Comprueba el estado del proyecto y dame el resultado de cada punto por separado,
sin corregir nada:

1. La rama actual y si el árbol de trabajo está limpio.
2. Los commits de main que no estaban antes de hoy, uno por línea.
3. Qué archivos hay en .claude/agents/ y qué herramientas declara cada uno,
   en una tabla.
4. Cuál de ellos puede escribir, cuál puede ejecutar y cuáles solo leen.
5. Si el repositorio ganó hoy algún archivo que no esté en .claude/agents/.
6. Qué dice la descripción de la solicitud de cambios de hoy sobre los
   hallazgos: cuántos aceptados, cuántos rechazados y con qué motivo.
7. uv run pytest -q y uv run ruff check .
8. Si openapi.json coincide con la especificación que genera el código.
9. Si queda alguna rama sin integrar.

Si algo falla, dime qué falló y detente. No lo arregles.
```

La sesión está completa si:

- [ ] Los cuatro subagentes están en `main`, cada uno con sus herramientas declaradas en el archivo.
- [ ] Ninguno de los tres revisores declara herramientas de edición, y solo uno de ellos puede ejecutar.
- [ ] El triaje está en la descripción de la solicitud de cambios, no en un documento inventado para la ocasión.
- [ ] Cada hallazgo rechazado cita dónde está escrita la decisión que lo vuelve ruido.
- [ ] El refactor del Lab 01 tiene un destino decidido y argumentado.
- [ ] La suite está en verde y no queda ninguna rama sin integrar.

## Limpieza

Detén los contenedores sin eliminar volúmenes. Los cuatro subagentes se
quedan: son parte del repositorio a partir de hoy, y la sesión 10 decide
cuáles sobreviven a la poda.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) te pide lo contrario de lo
que hiciste hoy: proponer un quinto subagente y **rechazarlo con argumentos**,
y comprobar de primera mano qué hereda un agente al que no le declaras
herramientas.

## Cierre

Preguntas de repaso:

- ¿Qué decía el resumen del refactorizador que el diff no mostraba, o al revés?
- De los tres veredictos del Lab 02, ¿cuál llegó habiendo leído el relato del autor?
- El revisor y el auditor declaran las mismas herramientas. ¿De dónde sale la diferencia entre lo que devolvieron?
- ¿Qué pasó exactamente cuando le pediste al consolidador que arreglara un hallazgo?
- Si rechazaste algún hallazgo, ¿cuál era el más razonable de todos, y dónde está escrita la decisión que lo vuelve ruido?

## Versión

Material revisado el **10 de septiembre de 2026** con Claude Code **2.1.268**
y la documentación oficial de subagentes. Comprueba tu versión con
`claude --version` y la disponibilidad local con `/help`.

- [Referencia de subagentes](https://code.claude.com/docs/en/sub-agents)
- [Referencia de comandos](https://code.claude.com/docs/en/commands)

## Estado Final del Repositorio

La sesión 10 parte exactamente de aquí.

En `~/curso-claude/curso-claude-code-api`, con `main` en verde y sin ramas
abiertas:

| Ruta | Origen |
|---|---|
| `.claude/agents/refactorizador.md` | Lab 01 |
| `.claude/agents/revisor-de-codigo.md` | Lab 02 |
| `.claude/agents/auditor-de-seguridad.md` | Lab 03 |
| `.claude/agents/consolidador-de-hallazgos.md` | Lab 04 |
| El refactor integrado, corregido o descartado | Decisión del Lab 04 |
| El triaje, en la descripción de la solicitud de cambios | Lab 04 |

El contrato de la API sigue siendo el de la sesión 6, y el repositorio no gana
ningún documento nuevo. Lo que cambia es quién puede tocarlo y con qué
autoridad: cuatro agentes versionados, y una decisión escrita donde se toman
las decisiones.

## Preparación para la Sesión 10

Antes de la clase:

- Deja `main` en verde, con la rama de hoy integrada y el triaje confirmado.
- Comprueba que Docker arranca sin errores: la sesión 10 conecta servicios
  externos y empieza por ahí.
- Actualiza tu copia del material:

```bash
cd $CURSO && git pull
```
