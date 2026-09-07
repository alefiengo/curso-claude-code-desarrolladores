# Lab 01: Rojo antes que Arreglo

## Objetivo

Reproducir el fallo real de tu skill `segmentar-commits` antes de tocar el
archivo, y cerrarlo con una prueba que se queda.

## Por qué este lab

Tu skill `segmentar-commits`, la que construiste en la sesión 5, lleva dos
sesiones repartiendo commits sin que nadie mirara si el reparto que produce
está realmente limpio. "Reparte en commits separados" sonaba completo. Hoy
no arreglas nada hasta que el fallo esté delante tuyo, reproducido con un
cambio real, no supuesto.

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
| 5–15 | El reparto de `segmentar-commits` reproducido y diagnosticado con `git show` |
| 15–25 | La skill corregida y probada de nuevo sobre el mismo cambio |

**Si necesitas cortar aquí:** lo mínimo es el fallo reproducido y
diagnosticado, aunque la corrección de la skill se termine después.

## Paso a Paso

### 1. Confirmar el punto de partida

```text
Crea la rama feature/segmentar-commits desde main, y confírmame que main
está actualizado, el árbol de trabajo está limpio, y la base de datos está
levantada y con las migraciones aplicadas.
```

### 2. Reproducir el reparto que reescribe en vez de repartir

No invoques la skill todavía. Genera un cambio real para repartir:

```text
Añade un campo priority opcional a la tarea, con sus tres capas: migración,
esquema y validación en el endpoint. No lo confirmes: quiero ver el diff
completo primero.
```

Revisa `/diff` y quédate con el tamaño real del cambio: cuántos archivos,
cuántas piezas distintas. Ahora invoca tu skill:

```text
/segmentar-commits
```

Deja que reparta y confirme. Cuando termine, reconstruye lo que pasó, commit
por commit:

```text
Para cada commit que acabas de hacer, muéstrame su diff con git show. Dime
si algún commit borra o modifica líneas que otro commit posterior vuelve a
tocar, en vez de limitarse a un subconjunto de archivos o de líneas del
cambio original.
```

Lo que tiene que haber ocurrido, si tu skill tiene el fallo que reportaste:
al menos un commit no es un subconjunto limpio del diff original —tiene
líneas que no estaban ahí, o que un commit siguiente vuelve a tocar—. Eso
significa que la skill no repartió el cambio: lo reescribió commit a commit,
usando su herramienta de edición en vez del índice de Git.

Si los commits sí son subconjuntos limpios del diff original, tu skill no
tiene este fallo. Es un resultado válido: dilo en la validación, deja los
commits tal como quedaron, y sigue con el Lab 02 igual.

### 3. Corregir la skill, no el resultado de hoy

Si reprodujiste el fallo, el problema no está en el campo `priority`: está
en el archivo de la skill.

```text
Deshaz los commits de segmentar-commits con git reset --soft, conservando
todos los cambios sin confirmar. Después abre
.claude/skills/segmentar-commits/SKILL.md y dime cómo arma cada commit hoy:
¿usa git add sobre archivos o fragmentos del cambio que ya existe, o edita
archivos para reconstruir cada estado intermedio?
```

Corrige el procedimiento para que cada commit se arme exclusivamente con
`git add` —de archivos completos o de fragmentos con `git add -p`— sobre el
cambio que ya está en el árbol de trabajo. La skill no debe volver a escribir
ni una línea de código: solo decide qué parte del cambio existente entra en
cada commit.

```text
/skills
```

Comprueba que Claude Code sigue reconociendo la skill después de editarla, y
vuelve a invocarla sobre el mismo cambio de `priority`. Repite la
comprobación del paso 2. Cuando los commits sean subconjuntos limpios,
confirma la corrección de la skill en su propio commit `chore:`.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. uv run pytest -q y uv run ruff check .
3. Si segmentar-commits tenía el fallo del reparto, y si ya quedó corregido.
4. Los commits de esta rama, uno por línea.
```

El lab está completo si:

- [ ] Sabes decir, con el `/diff` y `git show` delante, si `segmentar-commits` tenía el fallo del reparto o no.
- [ ] Si lo tenía, la skill ya arma cada commit con `git add`, no reescribiendo archivos.
- [ ] Nada de esto quedó publicado: los commits existen solo en `feature/segmentar-commits`.

## Limpieza

Ninguna. El Lab 02 trabaja sobre este mismo estado, sin publicar todavía.
Antes de seguir, `/context`: mira cuánto ocupó reproducir y corregir un
fallo real de una skill.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| No encuentras ningún commit "sucio" en el paso 2 | Es un resultado válido para tu skill. No fuerces el paso 3: deja los commits tal como quedaron y sigue con el Lab 02 |
| `git reset --soft` te deja en un estado que no reconoces | Comprueba con `git status` y `git log` antes de seguir: `--soft` mueve la rama, no toca el árbol de trabajo ni el índice |
| La skill sigue reescribiendo código después de corregida | Revisa si la corrección quedó como una preferencia ("intenta usar git add") en vez de una regla ("nunca reescribe código"): la redacción débil es el fallo más común al corregir una skill |
| Necesitas cortar el lab | Lo mínimo es el fallo reproducido y diagnosticado. Deja la skill sin corregir y termínalo después |
