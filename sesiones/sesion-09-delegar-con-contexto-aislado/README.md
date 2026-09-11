# Sesión 9: Delegar con Contexto Aislado

## Objetivo

Delegar la centralización de errores de la API, capturar el cambio en un
`.diff` y revisarlo antes de integrar. Usas la revisión disponible, amplías
el alcance con un auditor propio y delegas la verificación de hallazgos.
Tú decides cuáles se sostienen con evidencia y qué hacer con el cambio.

El problema profesional de hoy: **el resumen de un trabajo delegado no basta
para decidir si puedes integrarlo.**

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — El que sí puede escribir](labs/01-el-que-si-puede-escribir/README.md) | 41 |
| [Lab 02 — Revisar el cambio](labs/02-revisar-el-cambio/README.md) | 15 |
| [Lab 03 — Auditar más allá del diff](labs/03-auditar-mas-alla-del-diff/README.md) | 22 |
| [Lab 04 — Lo que sobrevive al triaje](labs/04-lo-que-sobrevive-al-triaje/README.md) | 27 |
| Cierre y decisión transferible | 15 |

Ruta mínima: conserva los tres agentes, la captura y la revisión del Lab 02.
Si falta tiempo, omite `/security-review` y la comprobación adicional con
`/subtask`, registrando qué no ejecutaste. En el Lab 04 verifica hasta dos
hallazgos prioritarios, deja el resto pendiente y omite la prueba de escritura.
Si corregir el refactor no cabe, descártalo con motivo y recupera la suite
verde. Una pausa entre labs exige completar sus requisitos antes de retomar;
no equivale a terminar la sesión.

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
| [01 — El que sí puede escribir](labs/01-el-que-si-puede-escribir/README.md) | Construyes el subagente que centraliza los errores de toda la API en un módulo común, conservando sus respuestas | Que lo que vuelve de un trabajo delegado es el relato del agente, y que el diff cuenta otra cosa |
| [02 — Revisar el cambio](labs/02-revisar-el-cambio/README.md) | Revisas la captura del Lab 01 y solo delegas una comprobación adicional si queda una duda | Que una revisión necesita un cambio identificado y evidencia, no tres veredictos |
| [03 — Auditar más allá del diff](labs/03-auditar-mas-alla-del-diff/README.md) | Amplías la revisión a la seguridad del repositorio con un auditor que solo lee y busca | Que un agente propio se justifica por un encargo recurrente y un alcance definido |
| [04 — Lo que sobrevive al triaje](labs/04-lo-que-sobrevive-al-triaje/README.md) | Construyes uno que ejecuta comprobaciones sin herramientas de edición, y trías sus hallazgos | Que un hallazgo correcto en general puede ser ruido aquí, y que distinguirlo es tuyo |

## Al finalizar esta sesión podrás

- Escribir un subagente de proyecto con la autoridad mínima de su oficio, y
  explicar qué hereda si no se la declaras.
- Distinguir las tres formas de delegar por el contexto que llevan: tu hilo,
  un delegado que hereda tu conversación, y un agente que arranca limpio.
- Guardar un diff que incluya archivos nuevos e identificar el estado revisado.
- Decir qué carga un subagente y qué información recibe dentro del encargo.
- Pasarle a un agente limpio, dentro del encargo, lo que solo existe en tu
  conversación.
- Distinguir una revisión puntual de un encargo que conviene guardar como
  subagente reutilizable.
- Triar hallazgos con evidencia: aceptar lo confirmado y pertinente; rechazar
  con una comprobación que lo desmiente o una decisión documentada de alcance.
- Explicar por qué recortar herramientas no sustituye a una regla de permisos.

## Conceptos Clave

**Un subagente de proyecto tiene un encargo y herramientas declaradas.** Vive en
`.claude/agents/`, se versiona con el proyecto y su cuerpo es todo lo que sabe
de su oficio. La línea que decide de verdad es la de sus herramientas: si no
se la escribes, hereda las herramientas disponibles para subagentes,
sujetas a los permisos y filtros de ejecución de Claude Code. La autoridad
mínima no es el valor por defecto; es una decisión que se toma cada vez.

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
diff, no solo contra el informe. Si buscas una mirada sin el relato del
autor, inspecciona el encargo que recibe el auditor.

**Delegar tiene tres formas, y se distinguen por el contexto que llevan.** Tu
propio hilo conserva el contexto de la conversación. `/subtask` y `/fork`
mandan el trabajo aparte con tu conversación, supuestos incluidos. Un subagente de
`.claude/agents/` no hereda el historial, pero recibe sus instrucciones, la
jerarquía de `CLAUDE.md`, el encargo que redacta Claude y una instantánea de
git status del inicio de la sesión principal. Lee el código con sus
herramientas. Inspecciona el encargo para excluir el relato del autor: el
aislamiento por sí solo no garantiza una revisión independiente.

**Una revisión puntual no exige un agente nuevo.** El Lab 02 usa una revisión
incorporada o un encargo en el hilo. El auditor del Lab 03 sí conserva un
procedimiento para revisar configuración, credenciales y permisos del
repositorio: ese trabajo recurrente justifica su archivo y su recorte de
herramientas.

**El triaje no se delega.** Un revisor que no conoce tu historia encuentra
cosas ciertas y cosas que solo parecen problemas porque contradicen una
decisión que se tomó hace sesiones. Aceptar exige evidencia y pertinencia;
rechazar exige una prueba que lo desmienta o citar la decisión de alcance.
Lo que falta comprobar queda pendiente. Sin esas reglas, una revisión
automática se convierte en una lista que nadie lee.

## Comandos Nuevos

| Comando o control | Uso |
|---|---|
| `.claude/agents/` | Donde viven los subagentes del proyecto, un archivo por agente |
| `@agent-<nombre>` | Invoca a un subagente concreto en vez de dejar que Claude elija |
| `/code-review` | Revisa el diff actual; se contrasta con la captura del Lab 01 |
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
5. Qué archivos nuevos hay fuera de .claude/agents/ y si pertenecen al
   refactor aprobado; la captura .diff no debe estar en el repositorio.
6. Qué dice la descripción de la solicitud de cambios de hoy sobre los
   hallazgos: cuántos aceptados, cuántos rechazados y con qué motivo.
7. uv run pytest -q y uv run ruff check .
8. Si openapi.json coincide con la especificación que genera el código.
9. Si queda alguna rama sin integrar.

Si algo falla, dime qué falló y detente. No lo arregles.
```

La sesión está completa si:

- [ ] Los tres subagentes están en `main`, cada uno con sus herramientas declaradas en el archivo.
- [ ] El auditor solo lee y busca; el consolidador puede ejecutar pero no declara herramientas de edición.
- [ ] La revisión del Lab 02 identifica su captura y commit base, o declara que revisó el estado actual sin cambios.
- [ ] El triaje está en la descripción de la solicitud de cambios, no en un documento inventado para la ocasión.
- [ ] Cada rechazo cita la evidencia que lo desmiente o la decisión documentada de alcance; si no hubo hallazgos, consta ese resultado y qué se comprobó.
- [ ] El refactor del Lab 01 tiene un destino decidido y argumentado, o consta que no había uno justificado.
- [ ] La prueba de escritura usó un archivo temporal fuera de la API, quedó limpia y no cambió el refactor, o consta que se omitió por tiempo.
- [ ] La suite está en verde y no queda ninguna rama sin integrar.

## Limpieza

Detén los contenedores sin eliminar volúmenes. Los tres subagentes se
quedan: son parte del repositorio a partir de hoy, y la sesión 10 decide
cuáles sobreviven a la poda.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) te pide evaluar otros
candidatos a subagente, rechazar los que no se justifiquen y comprobar qué
hereda un agente al que no le declaras herramientas.

## Cierre

Preguntas de repaso:

- ¿Qué decía el resumen del refactorizador que el diff no mostraba, o al revés?
- De las revisiones disponibles del Lab 02, ¿qué información recibió cada una y cómo lo comprobaste?
- ¿Qué justifica guardar al auditor como agente propio y usar una revisión puntual en el Lab 02?
- ¿Qué incluye tu `.diff` y qué lo volvería obsoleto?
- Si hiciste el experimento del consolidador, ¿qué herramienta usó y cómo comprobaste que la API no cambió? Si lo omitiste, ¿por qué?
- Si rechazaste algún hallazgo, ¿qué prueba lo desmintió o qué decisión documentada lo dejó fuera de alcance?

## Versión

Material revisado el **11 de septiembre de 2026** con Claude Code **2.1.268**
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
| `.claude/agents/auditor-de-seguridad.md` | Lab 03 |
| `.claude/agents/consolidador-de-hallazgos.md` | Lab 04 |
| La centralización de errores de toda la API integrada, corregida o descartada, o la conclusión de que ya estaba resuelta | Decisión del Lab 04 |
| El triaje o la ausencia de hallazgos, comprobaciones, pendientes y resultado u omisión del experimento, en la solicitud de cambios | Lab 04 |

El contrato de la API sigue siendo el de la sesión 6, y el repositorio no gana
ningún documento nuevo. Lo que cambia es quién puede tocarlo y con qué
autoridad: tres agentes versionados, y una decisión escrita donde se toman
las decisiones.

La captura `.diff` se guarda fuera del repositorio durante la revisión. La
solicitud de cambios registra su identificación y commit base; no se versiona
un parche junto al código que describe.

## Preparación para la Sesión 10

Antes de la clase:

- Deja `main` en verde, con la rama de hoy integrada y el triaje confirmado.
- Comprueba que Docker arranca sin errores: la sesión 10 conecta servicios
  externos y empieza por ahí.
- Actualiza tu copia del material:

```bash
cd $CURSO && git pull
```
