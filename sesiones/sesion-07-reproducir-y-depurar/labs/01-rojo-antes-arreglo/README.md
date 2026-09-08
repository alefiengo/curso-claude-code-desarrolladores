# Lab 01: Rojo antes que Arreglo

## Objetivo

Averiguar si tu skill `segmentar-commits` reparte los commits o reescribe el
código, mirando su archivo contra un cambio real; corregirla antes de
invocarla si hace falta; y comprobarlo con ese mismo cambio, que después
descartas.

## Por qué este lab

Tu skill `segmentar-commits`, la que construiste en la sesión 5, lleva dos
sesiones repartiendo commits sin que nadie mirara si el reparto que produce
está realmente limpio. "Reparte en commits separados" sonaba completo. Hoy
no la corriges a ciegas ni la das por buena: la revisas contra un cambio real
antes de tocar el archivo, y lo que decidas ahí lo compruebas invocándola de
verdad.

Ese cambio real es solo el caso de prueba. Al final lo descartas: el
contrato de la API está cerrado desde la sesión 6, y lo único que se queda de
hoy es la skill arreglada.

## Requisitos

- Sesión 6 completa: `main` en verde con el contrato entero —proyectos y
  tareas, v1 y v2— y sin ramas abiertas.
- `.claude/skills/` con `planificar-incremento` y `segmentar-commits`.
- La base de datos levantada.

## Ritmo de Trabajo

Este lab tiene 25 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | Rama nueva y el punto de partida confirmado |
| 5–10 | Un cambio real generado, sin confirmar, con el diff revisado |
| 10–17 | La skill diagnosticada contra ese cambio, y corregida y confirmada sola si tenía el fallo |
| 17–22 | La skill invocada de verdad y el reparto verificado con `git show` |
| 22–25 | El caso de prueba descartado: en la rama no queda nada más que la corrección, si la hubo |

**Si necesitas cortar aquí:** lo mínimo es la skill diagnosticada, y corregida
y confirmada si tenía el fallo. La invocación de verificación se hace
después.

## Paso a Paso

### 1. Confirmar el punto de partida

```text
Crea la rama feature/segmentar-commits desde main, y confírmame que main
está actualizado, el árbol de trabajo está limpio, y la base de datos está
levantada y con las migraciones aplicadas.
```

### 2. Generar un cambio real para poner a prueba la skill

No invoques la skill todavía. Genera un cambio real para repartir:

```text
Añade un campo priority opcional a la tarea, con sus tres capas: migración,
esquema y validación en el endpoint. No lo confirmes: quiero ver el diff
completo primero.
```

Revisa `/diff` y quédate con el tamaño real del cambio: cuántos archivos,
cuántas piezas distintas.

### 3. Corregir la skill, no el resultado de hoy

Con el cambio real delante, sin confirmarlo todavía, revisa la skill antes
de correrla:

```text
Abre .claude/skills/segmentar-commits/SKILL.md. Con el cambio que acabas de
generar delante, dime cómo va a armar cada commit: ¿usa git add sobre
archivos o fragmentos del cambio que ya existe, o edita archivos para
reconstruir cada estado intermedio?
```

Si la respuesta es que reescribe o reconstruye código, ese es el fallo real
que reportaste: corrígelo antes de invocarla.

```text
Corrige segmentar-commits para que nunca reescriba código: cada commit se
arma exclusivamente con git add, completo o con git add -p, sobre el cambio
que ya existe en el árbol de trabajo. No cambies el criterio de reparto ni
añadas ningún paso nuevo —la skill sigue haciendo lo mismo de antes, solo
que ahora arma cada commit sin tocar una sola línea de código.
```

Si la skill ya usaba `git add` correctamente, no hay nada que corregir: dilo
en la validación, y sáltate el commit de este paso. El resto del lab funciona
igual, solo que la rama va a quedar sin ningún commit al final —que es lo
correcto si no había nada que arreglar—.

Si sí la corregiste, confirma esa corrección sola, sin arrastrar el cambio de
`priority`:

```text
Confirma solo el archivo de la skill en un commit chore:, deja el cambio de
priority sin confirmar, y comprueba con /skills que la sesión sigue
reconociéndola.
```

### 4. Invocar la skill corregida y confirmar

```text
/segmentar-commits
```

Revisa el reparto que propone. Cuando te convenza, apruébalo y deja que
confirme.

```text
Para cada commit que acabas de hacer, muéstrame su diff con git show.
Confirma que cada uno es un subconjunto limpio del diff original: sin
líneas que no estaban ahí, sin que un commit posterior vuelva a tocar lo
mismo.
```

Si algún commit no es un subconjunto limpio, la corrección del paso 3 no
bastó: vuelve al archivo de la skill, no al resultado de hoy.

### 5. Descartar el caso de prueba

`priority` era el cambio con el que pusiste a prueba la skill, no una
capacidad que quieras conservar: el contrato de la API está cerrado desde la
sesión 6, y su esquema de respuesta no admite un campo que no declara.

```text
Dime qué commits vas a descartar y cuáles quedan antes de tocar nada. Después
descarta los commits de priority, conserva el commit chore: de la corrección
de la skill si existe, y confírmame que el árbol de trabajo queda limpio y
que la suite sigue en verde.
```

Lo que tiene que quedar en la rama: el commit de la skill corregida y nada
más. Si la skill no tenía el fallo, la rama queda vacía, y también está
bien. La prueba de que funciona ya la viste con `git show`; el campo no
hace falta para nada más.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. uv run pytest -q y uv run ruff check .
3. Si segmentar-commits tenía el fallo del reparto, y si ya quedó corregido.
4. Los commits de esta rama, uno por línea.
```

El lab está completo si:

- [ ] Revisaste `.claude/skills/segmentar-commits/SKILL.md` contra un cambio real antes de invocarla.
- [ ] Si tenía el fallo, ya arma cada commit con `git add`, no reescribiendo archivos.
- [ ] Los commits que produjo `/segmentar-commits` eran subconjuntos limpios del diff original, confirmado con `git show`.
- [ ] `priority` ya no está en la rama: era el caso de prueba, y el contrato no lo declara.
- [ ] En `feature/segmentar-commits` no queda nada más que la corrección de la skill —o nada en absoluto, si no hacía falta corregirla—, y sin publicar.

## Limpieza

Ninguna. El Lab 02 trabaja sobre este mismo estado, sin publicar todavía.
Antes de seguir, `/context`: mira cuánto ocupó diagnosticar y corregir un
fallo real de una skill.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| No sabes si la skill tiene el fallo sin verla correr | Es parte del método: lee el procedimiento exacto que describe el archivo contra el diff real que generaste en el paso 2, no le preguntes en abstracto |
| La skill dice en el paso 3 que ya usa `git add`, pero el paso 4 muestra un commit sucio | La respuesta del paso 3 fue optimista o incompleta: vuelve a leer el archivo completo, no el resumen que dio Claude |
| La skill sigue reescribiendo código después de corregida | Revisa si la corrección quedó como una preferencia ("intenta usar git add") en vez de una regla ("nunca reescribe código"): la redacción débil es el fallo más común al corregir una skill |
| El commit de la skill arrastró también el cambio de `priority` | Vuelve a rehacerlo confirmando solo el archivo de la skill: es la misma disciplina de "un commit por intención" que practicaste en la sesión 5 |
| Te incomoda descartar el trabajo de `priority` en el paso 5 | Es lo correcto aquí: el contrato está cerrado y no declara ese campo. Si lo dejaras, el `api.http` del Lab 03 fallaría al comprobar el esquema exacto de respuesta |
| Necesitas cortar el lab | Lo mínimo es la skill diagnosticada, corregida y confirmada. La invocación de verificación del paso 4 y el descarte del paso 5 se hacen después |
