# Lab 03: Misma Autoridad, otra Lente

## Objetivo

Ejecutar la revisión de seguridad que Claude Code trae de fábrica, ver hasta
dónde llega su alcance, y construir un auditor propio con **las mismas
herramientas exactas** que el revisor del Lab 02 y un oficio distinto.

## Por qué este lab

El revisor del Lab 02 mira un cambio. Una vulnerabilidad casi nunca está en el
cambio que acabas de hacer: está en un archivo que nadie ha vuelto a abrir
desde la sesión 2, en una variable de entorno, en un permiso que concediste
una vez.

Hoy construyes el segundo revisor y le declaras las mismas herramientas que al
primero, sin tocar una letra. Si los dos devuelven cosas distintas teniendo la
misma autoridad, vas a poder decir de dónde sale la diferencia.

## Requisitos

- Lab 02 terminado: el informe del revisor en `evidencias/s09-revisor.md` y el
  refactor todavía sin confirmar.

## Ritmo de Trabajo

Este lab tiene 20 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | La revisión de fábrica ejecutada y anotado hasta dónde llegó, o anotado que tu instalación no la trae |
| 5–12 | `.claude/agents/auditor-de-seguridad.md` revisado y guardado |
| 12–18 | Su informe en `evidencias/s09-auditor.md` |
| 18–20 | Anotada la diferencia entre los dos agentes de autoridad idéntica |

**Si necesitas cortar aquí:** lo mínimo es el auditor escrito y su informe
guardado. El Lab 04 lo necesita en disco.

## Paso a Paso

### 1. La revisión que viene incluida

```text
/security-review
```

Léela entera y anota dos cosas: qué encontró, y **sobre qué miró**. Esa
segunda es la que importa hoy. La skill de fábrica revisa los cambios
pendientes de la rama en la que estás; no es un repaso del repositorio.

Si tu instalación no la trae, no la sustituyas: sigue igual y anótalo. El lab
funciona con la comparación que viene después.

### 2. Escribir el auditor con la autoridad copiada

```text
Crea un subagente de proyecto llamado auditor-de-seguridad. Enséñame el
archivo antes de guardarlo.

Copia sus herramientas del revisor-de-codigo, exactamente las mismas, sin
añadir ni quitar ninguna.

Que en el cuerpo quede escrito que audita el repositorio entero, no un
cambio, y que mire al menos:

- Cómo se manejan las credenciales y la configuración: qué hay en el
  repositorio, qué está ignorado y qué se ve en el compose.
- Qué devuelven los errores de la API y si alguno deja ver detalles
  internos.
- Dónde se valida la entrada y qué pasa con lo que no encaja.
- Qué autoridad concede el propio repositorio: los permisos, los hooks y
  los subagentes de .claude/.

Que ordene los hallazgos por gravedad y que cada uno diga qué vio, en qué
archivo y en qué línea. Nada de riesgos genéricos sin evidencia en el
código.

Y un límite: el auditor audita, no corrige. No propone parches, no toca
configuración y no ejecuta nada.
```

Antes de guardarlo, comprueba que la línea de herramientas es **idéntica** a
la del revisor. Ábrelos uno al lado del otro si hace falta.

### 3. Ejecutarlo y guardar lo que devuelve

```text
@agent-auditor-de-seguridad Audita este repositorio y dame tus hallazgos.
```

```text
Guarda el informe completo del auditor-de-seguridad en
evidencias/s09-auditor.md, tal como lo devolvió.
```

Lo más probable es que aparezca algún hallazgo sobre algo que el curso decidió
a propósito: que la API no tiene autenticación, que la contraseña de la base
de datos está a la vista en el entorno de desarrollo, o similar. Si aparece,
no lo corrijas ni lo descartes ahora: es correcto en abstracto y equivocado
aquí, y separar las dos cosas es el trabajo del Lab 04. Si no aparece ninguno
así, anótalo también: significa que tu auditor se quedó corto de alcance, o
que el repositorio tiene menos superficie de la que parecía.

### 4. Anotar la diferencia

Dos agentes, la misma línea de herramientas, resultados distintos. Escribe en
una frase de dónde sale la diferencia, y guárdala: es la respuesta a una de
las preguntas del cierre de hoy.

Y anota también el contraste con el paso 1: la skill de fábrica miró lo
pendiente de la rama; tu auditor miró el repositorio. Ninguna de las dos
sobra, y eligen alcances distintos.

## Validación

```text
Sin cambiar nada, dime:

1. Qué subagentes hay en .claude/agents/ y qué herramientas declara cada uno,
   en una tabla.
2. Si el revisor-de-codigo y el auditor-de-seguridad declaran exactamente las
   mismas herramientas.
3. Cuántos hallazgos tiene evidencias/s09-auditor.md y cómo están ordenados.
4. Si el archivo del auditor declara que no corrige, y con qué palabras.
5. En qué rama estoy y si el refactor sigue sin confirmar.
```

El lab está completo si:

- [ ] Ejecutaste la revisión de fábrica y sabes decir sobre qué miró.
- [ ] `.claude/agents/auditor-de-seguridad.md` declara las mismas herramientas que el revisor.
- [ ] Su informe está en `evidencias/s09-auditor.md`, ordenado por gravedad.
- [ ] Si algún hallazgo choca con una decisión ya tomada, lo dejaste sin tocar para el Lab 04; y si no lo hay, lo anotaste.
- [ ] Puedes explicar en una frase por qué dos agentes con la misma autoridad devuelven cosas distintas.

## Limpieza

Ninguna. El Lab 04 lee los dos informes. Antes de seguir, `/context`.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| `/security-review` no existe en tu instalación | Anótalo y sigue. El lab compara alcances, y el alcance de tu auditor lo defines tú |
| El auditor devuelve treinta hallazgos genéricos | Le falta la exigencia de evidencia. Corrige el archivo para que cada hallazgo cite archivo y línea, y vuelve a invocarlo |
| Dice que el repositorio es seguro y no encuentra nada | Vuelve a invocarlo señalando dos sitios concretos: el manejo de la configuración y los permisos de `.claude/`. Si insiste, anótalo como resultado y compáralo en el Lab 04 con lo que dijo el revisor |
| Intenta abrir el `.env` y no puede | Mira tus permisos: la regla `deny` que escribiste en la sesión 4 es la primera candidata. Anótalo, porque significa que la autoridad del agente está acotada dos veces, por sus herramientas y por lo que tú autorizaste |
| El informe es larguísimo | Guárdalo igual. El Lab 04 construye un agente precisamente para eso |
