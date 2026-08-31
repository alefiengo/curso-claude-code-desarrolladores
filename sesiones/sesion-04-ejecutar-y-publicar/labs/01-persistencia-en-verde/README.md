# Lab 01: La Persistencia en Verde

## Objetivo

Cerrar las decisiones que tu plan dejó abiertas y ejecutar sus incrementos, uno
por commit, comprobando cada uno antes de confirmarlo.

## Por qué este lab

El plan que acordaste en la sesión 3 está aprobado, pero no está cerrado. Lo
escribió Claude en tu conversación, así que el tuyo no es idéntico al de tus
compañeros: puede tener tres incrementos o cinco, y puede dejar decisiones
pendientes con una frase del tipo "se confirma en el incremento 1". Si llegas
ahí sin cerrarlas, las cierra Claude. Elegirá algo razonable y no te avisará.

Hoy las cierras tú primero, por escrito, y después diriges los incrementos que
tenga tu plan. De paso vas a ver algo que hasta ahora pasaba desapercibido:
cuántas veces te pide permiso una tarea de este tamaño, y cuáles de esas veces
respondiste sin leer. Al terminar le pides la lista de todo lo que ejecutó, y
con esa lista empieza el laboratorio siguiente.

A partir de aquí no vuelves a teclear los comandos del proyecto. Se los pides a
Claude y lees lo que informa.

## Requisitos

- Sesión 3 completada, con tu plan confirmado en la rama `feature/persistencia`.
- Docker Engine o Docker Desktop arrancado en tu máquina.
- Claude Code abierto en `~/curso-claude/curso-claude-code-api`.

Si faltaste a la sesión 3, o tu plan quedó inservible, el paso 2 te da uno de
referencia. Si ya ejecutaste por tu cuenta la sección **Terminar la
Persistencia** de la sesión 3, ve a los **Problemas Frecuentes**: te dice cómo
comprobar dónde te quedaste.

## Ritmo de Trabajo

Este lab tiene 50 minutos:

| Min | Debe existir |
|---:|---|
| 0–4 | Rama correcta, base de datos levantada y punto de partida confirmado |
| 4–12 | Tu plan leído y normalizado: sabes cuántos incrementos tiene y qué comprueba cada uno |
| 12–17 | Las decisiones abiertas del plan cerradas por escrito, en su commit |
| 17–45 | Un commit por incremento, con su diff revisado antes de confirmar |
| 45–50 | `GET /states` respondiendo y la lista de comandos ejecutados a la vista |

**Si tu plan tiene más incrementos de los que caben:** para en cuanto
`GET /states` responda, declara lo que falta y termínalo fuera de clase. Es
preferible llegar al Lab 02 con tres incrementos revisados que con cinco sin
mirar.

## Paso a Paso

### 1. Confirmar desde dónde partes

Arranca Claude Code en el repositorio del proyecto:

```bash
cd ~/curso-claude/curso-claude-code-api
claude
```

Pídele el punto de partida:

```text
Dime, sin cambiar nada:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Los últimos cinco commits, uno por línea.
3. Qué archivos hay bajo docs/, app/ y tests/.
4. Si el contenedor de PostgreSQL está levantado.

Si no está levantado, levántalo y espera a que quede sano. No hagas nada más.
```

Debes estar en `feature/persistencia`. Si no lo estás, pídele que cambie a esa
rama antes de continuar.

Fíjate en lo que acaba de pasar: para levantar la base de datos, Claude te pidió
permiso. Va a pedírtelo cada vez que ejecute algo, y hoy ejecuta mucho. No
apuntes nada mientras trabajas; al terminar el lab le pedirás la lista completa
de lo que ejecutó.

### 2. Leer tu plan y darle una forma trabajable

Tu plan y el de la persona de al lado no dicen lo mismo. Antes de ejecutar nada,
averigua qué dice el tuyo:

```text
Lee mi plan de persistencia en docs/ completo y respóndeme sin editar nada:

1. Cuántos incrementos tiene y qué comprobación exige cada uno.
2. Qué decisiones deja abiertas o aplazadas, con la frase exacta donde lo dice.
3. Si algo del plan ya no coincide con el estado real del repositorio.

No propongas mejoras. Dime qué dice y qué no dice.
```

Esa respuesta te dice cuántas vueltas vas a dar en el paso 4.

Si tu plan viene desordenado —incrementos sin numerar, comprobaciones mezcladas
con la descripción— pídele que lo deje utilizable sin cambiar lo acordado:

```text
Reescribe el plan conservando exactamente el mismo alcance y las mismas
decisiones. Solo cambia la forma: incrementos numerados, y bajo cada uno su
comprobación en una lista. No añadas ni quites trabajo.
```

Renómbralo, porque en las próximas sesiones habrá otros planes:

```text
Renombra el plan a docs/plan-persistencia.md con git mv. Nada más.
```

**Si no tienes un plan usable**, cierra Claude un momento y copia el de
referencia:

```bash
export MATERIAL=$CURSO/sesiones/sesion-04-ejecutar-y-publicar/labs/01-persistencia-en-verde/material
cp $MATERIAL/plan-persistencia.md docs/
```

Tiene cuatro incrementos y una decisión abierta. Es un plan válido, pero no es
el tuyo: no lo uses si tienes el que acordaste en clase.

### 3. Cerrar las decisiones que el plan deja abiertas

El paso anterior te dijo cuáles son y con qué palabras las aplazó tu plan. Una
decisión aplazada es una decisión que tomará Claude solo cuando llegue el
incremento, así que ciérrala ahora y déjala escrita:

```text
Cierra en @docs/plan-persistencia.md las decisiones que el propio plan dejó
aplazadas. Para cada una, adopta la opción que el plan propone y escríbela en su
sección como decisión tomada, no como propuesta. Añade una línea diciendo por
qué esa opción encaja con lo que ya existe en el repositorio.

Si alguna decisión aplazada no trae ninguna propuesta, no la inventes: dímelo y
detente ahí.

No toques nada más del repositorio. No hagas commit.
```

Adoptar lo que propone el plan no es delegar la decisión: el plan es tuyo y lo
aprobaste en la sesión 3. Lo que cambia hoy es que deja de estar en condicional.

Si Claude se detiene porque alguna decisión no traía propuesta, el criterio es
corto: gana lo que ya existe. La app y sus tests son async, la base es
PostgreSQL y `docs/decisiones-ingenieria.md` prohíbe SQLite. Elige la opción que
no obligue a cambiar nada de eso, díselo en una frase y sigue.

Si tu plan no dejaba ninguna decisión abierta, salta este encargo y confirma
solo el renombrado.

Revisa el resultado con `/diff` y confírmalo:

```text
Confirma este cambio en un solo commit. Usa Conventional Commits y empieza por
docs:. Propón tú el mensaje y enséñamelo antes de confirmar.
```

**Conventional Commits** es la convención que usa el curso de aquí en adelante:
un prefijo que dice de qué tipo es el cambio (`docs:`, `chore:`, `feat:`,
`test:`, `fix:`), dos puntos y una frase en imperativo. Sirve para leer un
historial largo de un vistazo, que es justo lo que harás en el Lab 03.

### 4. Ejecutar los incrementos, uno a uno

Este paso se repite **una vez por cada incremento de tu plan**. Cambia el número
y nada más:

```text
Implementa el incremento 1 de @docs/plan-persistencia.md. Solo ese incremento.

No modifiques docs/, CLAUDE.md, .gitignore ni .env. No abras .env.

Al terminar ejecuta las comprobaciones que ese incremento declara en el plan,
pégame la salida completa de cada una y detente. No hagas commit.
```

Fíjate en que el encargo no repite las comprobaciones: las tiene el plan. Ese es
el criterio de aceptación, en vez de fiarte de que Claude diga "listo".

Antes de confirmar, revisa el diff con `/diff` y busca lo que corresponda a lo
que ese incremento toca:

| Si el incremento toca… | Mira en el diff |
|---|---|
| Dependencias y conexión | Que no aparezca SQLite por ningún lado, y que la URL de conexión no esté escrita dentro del código |
| Migraciones | Que la migración se haya probado subiendo **y** bajando. Una migración que solo sube no está probada, está estrenada |
| La tabla del catálogo y su seed | Que el seed sea **idempotente** —ejecutarlo dos veces deja el mismo resultado que ejecutarlo una— y que los códigos sean los del contrato, sin traducir ni inventar |
| Un endpoint nuevo | Que exista su test y que hayas visto el rojo antes de la implementación. Un test que nunca falló no demuestra nada |
| Cualquier incremento | Que no haya archivos fuera de lo que ese incremento declara |

Si algo no cuadra, díselo con el hecho concreto delante —"el incremento 1 de mi
plan no incluye `app/models.py`"— en vez de pedirle que lo revise otra vez. Y si
lo ves desviarse mientras trabaja, interrumpe con `Esc` en ese turno: no esperes
al final.

Cuando el diff te convenza:

```text
Confirma este incremento en un solo commit, con Conventional Commits. Propón tú
el mensaje según lo que hace el incremento y enséñamelo antes de confirmar.

No incluyas nada que no pertenezca a este incremento.
```

Vuelve al principio de este paso con el siguiente número. Terminas cuando
`GET /states` responde, o cuando se acaba el tiempo del lab.

### 5. Cerrar el lab

Pídele la lista de lo que ejecutó durante todo el trabajo:

```text
Enumera todos los comandos de shell que ejecutaste en esta conversación, uno por
línea y sin repetir. Agrúpalos por herramienta: uv, docker, alembic, git y las
que haya. No ejecutes nada más.
```

Esa lista es el punto de partida del Lab 02: cada línea es algo que tuviste que
aprobar a mano y que podrías no volver a aprobar nunca.

Ahora mira `/context`. Acabas de gastar varios incrementos de conversación en
una sola sesión, y el Lab 02 empieza otra tarea distinta. Con lo que aprendiste
en la sesión 3, decide si sigues aquí o arrancas limpio: las dos opciones son
defendibles, pero toma la decisión mirando el número.

## Validación

Pídele la comprobación completa y léela entera:

```text
Comprueba el estado del trabajo y dame el resultado de cada punto por separado,
sin corregir nada:

1. Los commits de esta rama que no están en main, uno por línea.
2. La migración: subir, bajar y volver a subir.
3. La suite completa y el linter.
4. La respuesta de GET /states, obtenida contra la aplicación en memoria como
   hacen los tests, dos veces seguidas. No levantes ningún servidor.
5. Si aparece la palabra sqlite en app, tests o pyproject.toml.
6. Si el árbol de trabajo está limpio.

Si algo falla, dime qué falló y detente. No lo arregles.
```

El lab está completo si:

- [ ] Las decisiones que tu plan dejaba abiertas están escritas dentro de él como decisiones tomadas.
- [ ] El plan se llama `docs/plan-persistencia.md` y el renombrado aparece en el historial.
- [ ] Hay un commit por incremento ejecutado, más el del plan, y ninguno mezcla dos incrementos.
- [ ] Los commits que confirmaste hoy siguen Conventional Commits.
- [ ] La migración sube, baja y vuelve a subir sin error.
- [ ] `GET /states` devuelve los cuatro estados del contrato, y las dos llamadas los devuelven en el mismo orden.
- [ ] No aparece SQLite en ninguna parte.
- [ ] Tienes a la vista la lista de comandos que Claude ejecutó durante el lab.
- [ ] Si quedaron incrementos sin ejecutar, sabes cuáles y lo has anotado en el plan.

## Limpieza

Ninguna. La base de datos se queda levantada y la rama sin integrar: los dos
laboratorios siguientes trabajan sobre este mismo estado.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| Tu plan tiene más incrementos de los que caben en el lab | Para en cuanto `GET /states` responda. Pídele que anote al final del plan qué incrementos quedan pendientes, y termínalos fuera de clase |
| Tu plan tiene menos incrementos y ya llegaste al final | Está bien: el criterio es el resultado, no el número. Ve al paso 5 |
| Ya ejecutaste la tarea puente de la sesión 3 | Haz el paso 1 igual. Los commits que tengas te dicen por dónde vas; retoma en el incremento que corresponda. Haz también el paso 2, porque el renombrado del plan no estaba en esa tarea |
| Tus commits de la tarea puente no siguen Conventional Commits | Es normal: aquella tarea dictaba otros mensajes. No reescribas el historial para uniformarlo. La convención se aplica a partir de hoy, y un repositorio real tiene esa costura en algún punto |
| No tienes plan, o el que tienes no se puede seguir | Copia el de referencia en el paso 2. Tiene cuatro incrementos y funciona sobre el mismo repositorio |
| Claude cerró una decisión por su cuenta antes de que llegaras al paso 3 | Compruébalo en el diff. Si eligió lo mismo, escríbelo igual en el plan: la decisión debe estar registrada, no solo ocurrida. Si eligió otra cosa, pídele que la revierta y la sustituya |
| Un incremento no pasa sus comprobaciones | No pases al siguiente. Dile qué comprobación falló y con qué salida, y pídele que lo corrija dentro del mismo incremento. Confirmar en rojo arrastra el problema a todos los commits siguientes |
| La migración falla por conexión | La base no está levantada o no está sana todavía. Pídele que la levante y espere, y vuelve a intentarlo |
| Un commit incluyó archivos de otro incremento | Pídele que deshaga ese commit conservando los cambios y confirme solo lo que pertenece al incremento. No borres el trabajo |
| Te pide permiso constantemente y te está frenando | Es exactamente el problema que resuelve el Lab 02. Por hoy aprueba y sigue: la lista del paso 5 es el punto de partida del laboratorio siguiente |
| La lista de comandos del paso 5 sale incompleta | Ocurre si compactaste o limpiaste la conversación durante el lab: lo que se resumió ya no está entero. Completa lo que falte pidiéndole que lea el plan y diga qué comandos exige cada incremento |
