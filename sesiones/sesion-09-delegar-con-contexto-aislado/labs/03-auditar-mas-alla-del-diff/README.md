# Lab 03: Auditar más allá del Diff

## Objetivo

Ampliar la revisión del cambio a la seguridad del repositorio y construir un
auditor de proyecto que solo pueda leer y buscar, con un encargo reutilizable.

## Por qué este lab

La revisión del Lab 02 parte del cambio capturado. Ahora amplías las preguntas
a la configuración, las credenciales y los permisos de todo el repositorio.

Este encargo se repetirá cuando cambien la configuración o los permisos.
Lo guardas en un auditor con un procedimiento estable y herramientas de
lectura y búsqueda. Su justificación es ese alcance recurrente; no hace falta
construir un agente por cada revisión puntual.

## Requisitos

- Lab 02 terminado: la revisión de código y sus dudas anotadas, la captura
  `.diff` conservada fuera del repositorio y el refactor todavía sin confirmar.
  También sirve haber registrado que no hubo hallazgos o que no había un
  refactor justificado; no hace falta que `/subtask` estuviera disponible.

## Ritmo de Trabajo

Este lab tiene 22 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | La revisión de fábrica ejecutada con su alcance, o su omisión por disponibilidad o ruta mínima |
| 5–12 | `.claude/agents/auditor-de-seguridad.md` revisado y guardado |
| 12–19 | Sus hallazgos de vuelta, leídos enteros |
| 19–22 | Anotado qué cubrió la revisión del cambio y qué añadió la auditoría del repositorio |

**Si necesitas cortar aquí:** guarda el auditor y conserva en tus notas los
resultados disponibles. Antes del Lab 04, termina la auditoría y registra sus
hallazgos o su ausencia. Repetirla puede producir resultados distintos.

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
En la ruta mínima también puedes omitirla por tiempo, dejando el motivo.

### 2. Escribir el auditor del repositorio

```text
Crea un subagente de proyecto llamado auditor-de-seguridad. Enséñame el
archivo antes de guardarlo.

Declara solo herramientas de lectura y búsqueda. No le des herramientas
para editar, escribir, ejecutar comandos ni delegar a otros agentes.

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

Antes de guardarlo, comprueba que declara sus herramientas y que solo permiten
leer y buscar. Su instrucción de no corregir acompaña ese recorte.

### 3. Ejecutarlo

```text
Prepara el encargo para auditor-de-seguridad: auditar el repositorio completo
según su procedimiento. Incluye las rutas necesarias, sin el relato del autor
ni los hallazgos de las revisiones anteriores. Enséñame el encargo antes de
invocarlo y espera mi aprobación.
```

Inspecciona el encargo y autoriza su envío. El auditor no hereda el historial,
pero sí recibe el mensaje que redacta Claude. Lee sus hallazgos y consérvalos
en tus notas; el triaje del Lab 04 irá en la solicitud de cambios.

Si aparece un hallazgo sobre una decisión de desarrollo —por ejemplo,
autenticación o credenciales locales—, consérvalo para el triaje. No lo
descartes solo porque sea un entorno de práctica: busca la decisión escrita
y las condiciones en que el riesgo sí importa. Si no hubo hallazgos, registra
el alcance inspeccionado y sus límites.

### 4. Anotar la diferencia

Compara la revisión de código del Lab 02 con la auditoría: qué miró cada una,
qué pudo comprobar y qué sigue pendiente. No atribuyas las diferencias solo
al contexto: también cambian el encargo, las herramientas y el alcance.

Si ejecutaste la revisión del paso 1, compara su alcance observado con el del
auditor. Si no estaba disponible, deja ese contraste como no realizado.

## Validación

```text
Sin cambiar nada, dime:

1. Qué subagentes hay en .claude/agents/ y qué herramientas declara cada uno,
   en una tabla.
2. Si el auditor solo dispone de herramientas de lectura y búsqueda.
3. Si el archivo del auditor declara que no corrige, y con qué palabras.
4. Si apareció algún archivo nuevo que no sea el del subagente.
5. En qué rama estoy y si el refactor sigue sin confirmar y coincide con la
   captura del Lab 01. El único archivo nuevo de este lab debe ser el auditor.
```

El lab está completo si:

- [ ] Ejecutaste la revisión de fábrica y registraste su alcance, o anotaste su omisión por disponibilidad o tiempo.
- [ ] `.claude/agents/auditor-de-seguridad.md` declara solo herramientas de lectura y búsqueda.
- [ ] Sus hallazgos llegaron ordenados por gravedad y con archivo y línea cada uno, o registraste que no encontró ninguno.
- [ ] Si algún hallazgo choca con una decisión ya tomada, lo dejaste sin tocar para el Lab 04; y si no lo hay, lo anotaste.
- [ ] Puedes explicar qué justifica el auditor reutilizable y qué amplía respecto a la revisión puntual del Lab 02.

## Limpieza

Conserva el archivo nuevo del auditor. No hay archivos de prueba que limpiar.
Antes de seguir, `/context`.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| `/security-review` no existe en tu instalación o no puede resolver la rama base | Anótalo y sigue. El lab compara alcances, y el alcance de tu auditor lo defines tú |
| El auditor devuelve treinta hallazgos genéricos | Le falta la exigencia de evidencia. Corrige el archivo para que cada hallazgo cite archivo y línea, y vuelve a invocarlo |
| Dice que el repositorio es seguro y no encuentra nada | Vuelve a invocarlo señalando dos sitios concretos: el manejo de la configuración y los permisos de `.claude/`. Si insiste, anótalo como resultado y compáralo en el Lab 04 con la revisión del Lab 02 |
| Intenta abrir el `.env` y no puede | Mira tus permisos: la regla `deny` que escribiste en la sesión 4 es la primera candidata. Anótalo, porque significa que la autoridad del agente está acotada dos veces, por sus herramientas y por lo que tú autorizaste |
| El informe es larguísimo | Déjalo estar. El Lab 04 construye un agente precisamente para eso |
