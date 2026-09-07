# Lab 01: Rojo antes que Arreglo

## Objetivo

Diagnosticar el fallo real de tu skill `segmentar-commits` —reescribe código
en vez de repartirlo— contra un cambio real, corregirla antes de invocarla, y
confirmar la corrección con ese mismo cambio.

## Por qué este lab

Tu skill `segmentar-commits`, la que construiste en la sesión 5, lleva dos
sesiones repartiendo commits sin que nadie mirara si el reparto que produce
está realmente limpio. "Reparte en commits separados" sonaba completo. Hoy
no la corriges a ciegas: la revisas contra un cambio real antes de tocar el
archivo, y confirmas la corrección invocándola de verdad.

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
| 10–18 | La skill diagnosticada contra ese cambio y corregida si hacía falta |
| 18–25 | La skill invocada de verdad y el reparto verificado con `git show` |

**Si necesitas cortar aquí:** lo mínimo es la skill diagnosticada y
corregida. La invocación de verificación se hace después.

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
en la validación y sigue igual al paso 4.

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

```text
/skills
```

Comprueba que Claude Code sigue reconociendo la skill después de editarla.
Si la corregiste en el paso 3, confirma esa corrección en su propio commit
`chore:` antes de seguir.

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
- [ ] Los commits que produjo `/segmentar-commits` son subconjuntos limpios del diff original, confirmado con `git show`.
- [ ] Nada de esto quedó publicado: los commits existen solo en `feature/segmentar-commits`.

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
| Necesitas cortar el lab | Lo mínimo es la skill diagnosticada y corregida. La invocación de verificación del paso 4 se hace después |
