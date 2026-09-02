# Lab 02: Qué Merece Ser una Skill

## Objetivo

Decidir qué parte de tu trabajo repetido merece convertirse en herramienta, y
construir la primera: un procedimiento de planificación versionado en tu
repositorio.

## Por qué este lab

Llevas cuatro sesiones repitiendo cosas. En la 3 acordaste un plan a mano; en la
4 lo ejecutaste incremento a incremento y tuviste que pedir la misma convención
de mensajes de commit en cada encargo. Nada de eso está escrito en ninguna
parte: vive en tu cabeza y en el hilo de una conversación que ya cerraste.

Una skill es ese procedimiento escrito, versionado y disponible por su nombre.
Hoy construyes la primera, y lo que más te va a costar no es escribirla: es
decidir cuál. Vas a pedirle a Claude tres ideas mirando tu propio repositorio, y
al menos una vas a tener que rechazarla. Ese rechazo es el trabajo del lab. Una
carpeta llena de herramientas que nadie invoca no es un sistema; es deuda con
otro nombre.

## Requisitos

- Lab 01 terminado, con `main` en verde y `feature/persistencia` borrada.
- Claude Code abierto en `~/curso-claude/curso-claude-code-api`.

Si te saltaste el Lab 01 porque te faltaba el estado de la sesión 4, este lab
funciona igual: crea la rama del paso 3 desde donde estés y sigue.

Si en el Lab 01 decidiste arrancar una sesión limpia, arráncala ahora. Este lab
no necesita nada de la conversación anterior salvo una cosa que ya sabes: qué
comando tuvo que pedirte permiso.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–8 | Tres recomendaciones a la vista, clasificadas, con al menos una rechazada por escrito |
| 8–11 | La rama `feature/projects` creada desde `main` |
| 11–22 | La skill escrita, y la sesión reconociéndola por su nombre |
| 22–30 | Diff revisado y la skill confirmada en su propio commit |

**Si vas tarde:** la skill escrita es lo único que el Lab 03 necesita. Termina
de clasificar las recomendaciones y de anotar el rechazo después de clase, pero
no llegues al Lab 03 sin la skill.

## Paso a Paso

### 1. Pedir tres recomendaciones sobre tu repositorio

No preguntes en abstracto. Que mire lo que tienes:

```text
Lee este repositorio —el contrato, las decisiones de ingeniería, CLAUDE.md, el
historial de commits y la configuración de .claude— y propónme tres
procedimientos de este proyecto que se hayan repetido y que hoy no estén
escritos en ningún sitio.

Para cada uno dime, en una línea cada cosa:

1. Cuántas veces se ha repetido y dónde lo ves.
2. Qué haría exactamente.
3. Si necesita el contexto de mi conversación o le estorbaría.
4. Si ya está resuelto en otro lugar del repositorio o por Claude Code.

No escribas ninguna todavía. No crees archivos.
```

Tus tres recomendaciones no van a ser las de la persona de al lado, y eso está
bien: el criterio con el que las juzgues sí es el mismo.

### 2. Clasificar y rechazar

Reparte cada recomendación en uno de estos tres grupos. La decisión es tuya, no
suya:

| Grupo | Cuándo | Señal |
|---|---|---|
| Skill | El procedimiento es fijo, ya lo repetiste, y su resultado tiene que quedarse en tu conversación para que sigas dirigiéndolo | "Ya he hecho esto varias veces y siempre igual" |
| Trabajo aparte | El trabajo necesita **no** ver tu conversación, o produciría un muro de texto que no vas a releer. Corre en su propia ventana de contexto y te devuelve solo el resultado. La forma corta es una skill que lo declara en su cabecera, y es el desafío de hoy | "Quiero un juicio que no sepa cómo llegué aquí" |
| Ninguna de las dos | Cabe en una línea que ya está escrita en otro sitio, no lo has repetido nunca, o Claude Code ya lo trae | "Esto es un comando, no un procedimiento" |

Tienes que rechazar **al menos una**, y por escrito. Los tres motivos de rechazo
que aparecen más a menudo:

- **Ya viene incluido.** Claude Code trae skills de fábrica; `/code-review` es
  una de ellas. Escribir tu propio revisor desde cero no es construir una
  herramienta, es duplicar una.
- **Es una línea, no un procedimiento.** Aplicar las migraciones es
  `uv run alembic upgrade head`, y ya está en tu `README.md`. Una skill para eso
  añade un archivo y no quita ningún trabajo.
- **No lo has repetido.** Suena útil y todavía no ha pasado dos veces. Espera a
  que pase.

No lo dejes en la conversación: en este proyecto las decisiones se registran en
archivos versionados, y un rechazo es una decisión. Va en el mensaje del commit
de la skill, en el paso 6. Escríbelo en una frase ahora, mientras lo tienes
claro.

Hoy construyes **la de planificación**, esté o no entre las tres que te
propuso. La necesitas en el Lab 03, y su repetición no está en tus commits sino
en tu recorrido: ya acordaste un plan a mano y lo ejecutaste incremento a
incremento. Si Claude
no la recomendó, apúntalo: acabas de encontrar el límite de pedirle ideas sobre
un repositorio que solo ve una vez.

Las que sobrevivieron y no construyes hoy no se pierden. Una de ellas es el
desafío de esta sesión.

### 3. Abrir la rama del trabajo de hoy

```text
Crea la rama feature/projects desde main y confírmame que main está actualizado
y que el árbol de trabajo está limpio. No hagas nada más.
```

Si en el Lab 01 no llegaste a integrar, sácala de `feature/persistencia` en vez
de `main`: lo que necesitas debajo es la configuración de conexión y las
migraciones, no la rama concreta donde estén.

La skill va en esta rama, junto al código que va a producir. No es un adorno de
tu configuración personal: quien revise la entrega de hoy debería ver **con qué
procedimiento se planificó**, igual que ya puede ver con qué permisos se
trabajó.

### 4. Escribir la skill

Tú decides qué entra. Estos son los elementos que un plan de este proyecto
necesita, y los reconoces porque los echaste de menos al ejecutar el último:

```text
Crea una skill de proyecto llamada planificar-incremento. Escribe el
procedimiento con estos elementos y enséñame el archivo antes de guardarlo:

- Contra qué documentos se planifica en este repositorio, nombrándolos.
- Que el resultado se escriba en docs/, con un nombre que diga de qué es el
  plan.
- Que el plan salga en incrementos numerados, y que cada incremento declare su
  propia comprobación ejecutable.
- Que ninguna decisión quede aplazada: si algo no se puede decidir con lo que
  hay en el repositorio, que se pregunte en vez de proponerse en condicional.
- Que declare explícitamente qué queda fuera de alcance.

Y un límite: la skill planifica y no implementa. No crea ni modifica código,
no instala dependencias y no toca la base de datos.

Dime también dónde queda el archivo y con qué nombre se invoca.
```

Cuando te lo enseñe, comprueba dos cosas antes de guardarlo:

- Que el límite está escrito. Sin él, la primera vez que la invoques va a
  empezar a implementar, porque es lo que suele venir después de un plan.
- Que no repite lo que ya dice `CLAUDE.md`. Tu memoria de proyecto se carga
  siempre; una skill que la copia gasta contexto dos veces.

### 5. Comprobar que la sesión la reconoce

Que el archivo exista no significa que puedas invocarla:

```text
/skills
```

Debe aparecer la tuya entre las demás. Verás bastantes que no escribiste: son
las que Claude Code trae de fábrica.

Si no aparece, es por algo concreto y esta es la única vez que te va a pasar:
`.claude/skills/` no existía cuando arrancaste la sesión, así que Claude Code no
estaba vigilando ese directorio.

```text
/reload-skills
```

Te dirá cuántas skills hay y si cambió algo. Vuelve a `/skills`. Si sigue sin
aparecer, sal con `/exit` y vuelve a abrir Claude Code: al arrancar lee el
directorio entero.

Escribe `/` y busca su nombre en el menú. Ahí es donde vas a invocarla el resto
del curso.

### 6. Revisar y confirmar

```text
/diff
```

Debe aparecer un archivo nuevo y nada más. Si aparece código, la skill se
adelantó al Lab 03: pídele que lo saque.

```text
Confirma la skill en un solo commit. Usa Conventional Commits y empieza por
chore:. En el cuerpo del mensaje incluye, en una frase, qué recomendación
rechacé y por qué: te la doy ahora.

Propón tú el mensaje y enséñamelo antes de confirmar.
```

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué archivos hay bajo .claude/, uno por línea.
3. El contenido de la skill que acabo de crear.
4. Si esa skill menciona algún límite sobre modificar código, y con qué
   palabras.
5. Los commits de esta rama que no están en main.
```

El lab está completo si:

- [ ] Tienes tres recomendaciones clasificadas como skill, trabajo aparte o ninguna de las dos.
- [ ] Al menos una está rechazada, y el motivo quedó escrito en el mensaje del commit.
- [ ] La rama `feature/projects` existe y sale de `main`.
- [ ] La skill está en `.claude/skills/`, versionada, y `/skills` la reconoce.
- [ ] La skill dice contra qué se planifica, cómo se numeran los incrementos y dónde se escribe el resultado.
- [ ] La skill declara que no implementa.
- [ ] El commit es propio y solo contiene la skill.
- [ ] Sabes decir qué recomendación rechazaste y con qué criterio.

## Limpieza

Ninguna. El Lab 03 estrena la skill que acabas de escribir.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| Las tres recomendaciones te parecen las tres buenas | Vuelve a la columna de la señal: ¿cuántas veces has hecho cada una? Si alguna no ha pasado dos veces, no es una skill todavía. Y comprueba si Claude Code ya la trae con `/skills` |
| Ninguna de las tres te sirve | Pídele tres más, diciéndole qué falló en las primeras. También es un resultado válido: significa que este repositorio todavía no ha repetido lo suficiente |
| `/skills` no muestra la tuya | Ejecuta `/reload-skills`. Si sigue sin aparecer, `/exit` y vuelve a abrir: el directorio `.claude/skills/` no existía cuando arrancó la sesión |
| `/skills` la muestra con otro nombre | El nombre viene del directorio, no del título que escribiste dentro. Pídele que renombre el directorio si no te gusta cómo se invoca |
| Claude invoca la skill por su cuenta cuando no la pediste | Es su comportamiento normal: la carga cuando le parece relevante. Si prefieres invocarla siempre a mano, pídele que añada a la cabecera del archivo la opción que lo desactiva |
| La skill quedó tan larga como el plan que tiene que producir | Es un procedimiento, no una plantilla rellena. Pídele que la reduzca a lo que decide, y que quite todo lo que sea ejemplo |
| La skill repite reglas que ya están en `CLAUDE.md` | Pídele que las quite y las deje referenciadas. `CLAUDE.md` se carga en todas las sesiones; la skill solo cuando se invoca |
| Creaste la skill en `~/.claude/skills/` en lugar del proyecto | Entonces no viaja en el repositorio y nadie más la ve. Pídele que la mueva a `.claude/skills/` del proyecto y que la añada a Git |
