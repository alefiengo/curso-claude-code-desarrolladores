# Lab 02: Convertir Decisiones en Contexto de Proyecto

## Objetivo

Construir un `CLAUDE.md` a partir de fuentes reales, comprobar que se carga y
evaluarlo contra una propuesta que contradice las reglas del equipo.

## Por qué este lab

Un buen archivo de instrucciones no describe el repositorio: reduce errores que
el repositorio no puede prevenir por sí solo.

El equipo de TaskFlow acaba de entregarte decisiones sobre PostgreSQL, tests,
contrato y secretos. Vas a decidir cuáles deben estar presentes en cualquier
sesión, usar `/init` solo como borrador y probar el resultado con una propuesta
que intenta tomar cuatro atajos incompatibles.

No usarás una regla artificial para saber si Claude "obedeció". Revisarás una
decisión de ingeniería que podría aparecer mañana en una pull request.

## Requisitos

- Lab 01 completado.
- `~/curso-claude/curso-claude-code-api` limpio y en `main`.
- Test y lint en verde.
- Sin `CLAUDE.md` de proyecto: el Lab 01 lo dejó fuera del alcance a propósito.
  Si repites este lab y ya existe uno, muévelo a `evidencias/` antes de empezar;
  el paso 3 lo genera de nuevo.

## Ritmo de Trabajo

Este lab tiene 45 minutos. Los puntos de control son:

| Min | Debe existir |
|---:|---|
| 0–8 | Decisiones incorporadas, fuentes de contexto inspeccionadas y borrador de `/init` |
| 8–23 | Auditoría recibida y encargo propio para reescribir `CLAUDE.md` |
| 23–35 | Archivo recargado y propuesta adversa evaluada en una sesión nueva |
| 35–45 | Auto memory revisada, evidencia guardada y contexto confirmado en `main` |

No recortes la prueba adversa para ganar tiempo: es la evidencia de que el
archivo dirige una decisión real y no solo existe.

## Paso a Paso

### 1. Incorporar las decisiones del equipo

```bash
cd ~/curso-claude/curso-claude-code-api
export MATERIAL=$CURSO/sesiones/sesion-02-fundar-el-proyecto/labs/02-memoria-util/material
cp $MATERIAL/decisiones-ingenieria.md docs/decisiones-ingenieria.md
cp $MATERIAL/propuesta-atajo.md evidencias/propuesta-atajo.md
git add docs/decisiones-ingenieria.md evidencias/propuesta-atajo.md
git commit -m "Documenta decisiones de ingeniería del equipo"
```

Lee las decisiones. Para cada sección pregunta:

- ¿Claude puede deducirla con certeza del código actual?
- ¿Debe estar presente en cualquier tarea o solo al tocar una ruta?
- ¿Es orientación o necesita una garantía técnica?

No todas las respuestas tienen que terminar en `CLAUDE.md`.

### 2. Inspeccionar el contexto inicial

Abre una sesión nueva:

```bash
claude
```

Ejecuta:

```text
/context
```

Confirma que el proyecto todavía no aporta un `CLAUDE.md`. Puede haber memoria
de usuario u organización; no la confundas con instrucciones compartidas por el
repositorio.

Revisa también:

```text
/memory
```

Anota en **Contexto de partida** qué fuentes ajenas al proyecto existen y cuáles
mostró `/context` como cargadas. No las borres: basta con conocerlas para
interpretar la prueba final.

### 3. Generar un borrador con `/init`

```text
/init
```

Si la interfaz ofrece configurar varios artefactos, elige solo instrucciones de
proyecto. Skills y hooks todavía no resuelven el problema de esta sesión.

`/init` explora el repositorio y propone un archivo. Sal con `/exit` y conserva
el borrador como evidencia:

```bash
cp CLAUDE.md evidencias/claude-md-borrador.md
wc -l CLAUDE.md
git add -N CLAUDE.md
git diff -- CLAUDE.md
```

`git add -N` registra intención de añadir sin preparar el contenido; así Git
puede mostrar el diff de un archivo nuevo. No confirmes todavía.

### 4. Auditar cada instrucción por función y alcance

El borrador de `/init` mezcla instrucciones que deben cargarse en cualquier
tarea con otras que no. Vas a pedirle a Claude que clasifique cada bloque del
archivo, sin editarlo todavía, en una de estas cinco categorías:

| Categoría | Cuándo aplica |
|---|---|
| SIEMPRE | Debe estar presente en cualquier tarea del repositorio |
| POR RUTA | Solo aplica al trabajar sobre ciertos archivos |
| BAJO DEMANDA | Es un procedimiento que se consulta cuando hace falta, no contexto permanente |
| DOCUMENTACIÓN | Pertenece al README o a `docs/`, no a instrucciones |
| ELIMINAR | Es genérico, duplicado, obvio o temporal |

Escribe tú el encargo. Además de la clasificación debe pedir dos cosas:

- la fuente o el riesgo concreto que justifica cada bloque marcado SIEMPRE;
- qué decisiones de `docs/decisiones-ingenieria.md` faltan en el borrador.

Contrasta tu encargo con esta redacción de referencia y corrige lo que falte.
Anota en **Encargo propio** qué te faltó pedir:

<details>
<summary>Redacción de referencia para contrastar</summary>

```text
Audita @CLAUDE.md usando @docs/decisiones-ingenieria.md y el repositorio.
No edites todavía.

Para cada bloque indica una de estas decisiones:
- SIEMPRE: debe estar presente en cualquier tarea;
- POR RUTA: solo aplica a ciertos archivos;
- BAJO DEMANDA: es un procedimiento, no contexto permanente;
- DOCUMENTACIÓN: pertenece al README o a docs, no a instrucciones;
- ELIMINAR: es genérico, duplicado, obvio o temporal.

Cita la fuente o el riesgo concreto que justifica cada elemento marcado SIEMPRE.
Señala también cualquier decisión del equipo que el borrador haya omitido.
```

</details>

Abre Claude desde el directorio raíz del proyecto y entrega tu versión corregida:

```bash
claude
```

No evalúes por cantidad de texto. Evalúa si cada instrucción tiene un trabajo
claro y el alcance correcto. Conserva esta conversación abierta: el paso 5
reescribe el archivo con la auditoría todavía delante.

### 5. Escribir el contexto mínimo suficiente

Sigue en la misma conversación. Redacta ahora la instrucción de reescritura a
partir de la auditoría que Claude acaba de entregarte.

Tu instrucción debe cumplir esta barra de calidad. Compruébala punto por punto
antes de enviarla:

| Debe exigir | Comprobación |
|---|---|
| Solo lo que aplica a cualquier tarea del repositorio | Ninguna línea sirve para un único archivo o momento |
| Las fuentes de verdad del comportamiento y de las decisiones | Nombra `docs/contrato-api.md` y `docs/decisiones-ingenieria.md` |
| Los comandos canónicos de instalación, test y lint | Aparecen tal como se ejecutan |
| PostgreSQL, no SQLite, para pruebas de persistencia | Queda como regla, no como sugerencia |
| No abrir, mostrar, editar ni confirmar `.env` | Prohibición explícita, sin excepciones |
| No debilitar tests existentes para conseguir verde | Prohibición explícita |
| Formato breve: encabezados y viñetas | Sin párrafos largos |
| Apuntar al documento en vez de duplicarlo | Rutas entre backticks, sin imports con `@` |

Los dos últimos puntos importan por su coste: `CLAUDE.md` se carga entero en cada
sesión, y un import con `@` arrastraría además el documento completo. Copiar el
árbol, las dependencias, un tutorial o el estado actual gasta esa carga en
información que el repositorio ya responde.

<details>
<summary>Prompt de referencia para contrastar</summary>

```text
Reescribe CLAUDE.md solo con elementos que deban estar disponibles en cualquier
tarea del repositorio.

Debe dejar inequívocos:
- fuentes de verdad del comportamiento y de las decisiones de ingeniería;
- comandos canónicos de instalación, test y lint;
- PostgreSQL, no SQLite, para pruebas de persistencia;
- no abrir, mostrar, editar ni confirmar .env;
- no debilitar tests existentes para conseguir verde.

Usa encabezados y viñetas breves. No copies el árbol, dependencias, tutoriales,
estado actual ni consejos genéricos. Para el detalle, apunta al documento que ya
lo contiene en vez de duplicarlo. Nombra sus rutas entre backticks; no uses
imports con @, porque cargarían el documento completo en cada sesión.
```

</details>

Entrega tu versión corregida en la misma conversación de la auditoría, para que
Claude reescriba el archivo con el análisis que acaba de hacer delante.

Cuando termine, sal con `/exit` y revisa tú el archivo completo:

```bash
sed -n '1,220p' CLAUDE.md
git diff --check
git diff -- CLAUDE.md
```

Haz tres preguntas sobre cada línea:

1. ¿En qué tarea futura evitará un error o una búsqueda repetida?
2. ¿Su redacción permite saber si se siguió?
3. ¿Seguirá siendo cierta cuando termine el curso?

Si no puedes responder, corrígela o elimínala.

### 6. Confirmar que la memoria se carga

Cierra cualquier conversación anterior y abre una nueva. `CLAUDE.md` se carga al
inicio:

```bash
claude
```

```text
/context
```

El archivo debe aparecer bajo **Memory files**. Después usa:

```text
/memory
```

`/memory` también debe listar el archivo y permite abrirlo. `/context` añade la
vista de cuánto ocupa dentro de la ventana. Si las dos vistas difieren, anota la
versión, cierra la sesión y vuelve a abrirla desde la raíz antes de continuar.

### 7. Evaluar el contexto con una propuesta adversa

Aquí sí usas `@`. En un prompt carga el archivo una vez, para esta pregunta; lo
que el paso 5 descartó es usarlo dentro de `CLAUDE.md`, donde cargaría el
documento entero en todas las sesiones futuras.

Sin editar archivos, pide:

```text
Revisa @evidencias/propuesta-atajo.md contra las instrucciones y fuentes de este
proyecto. No implementes nada.

Para cada incompatibilidad indica:
1. propuesta concreta que rechazas;
2. regla o fuente que la contradice;
3. riesgo que evita;
4. alternativa compatible.

Termina con la verificación completa que exigirías antes de integrar.
```

Contrasta la respuesta tú mismo:

| Atajo propuesto | Conflicto que debe detectar |
|---|---|
| SQLite en tests | Persistencia se prueba contra PostgreSQL |
| Ajustar tests para facilitar la solución | El contrato cambia primero y no se debilitan tests para conseguir verde |
| Leer `.env` | El archivo local no se abre, muestra, edita ni confirma |
| Cerrar con `pytest` | Debe usar el entorno bloqueado y ejecutar también lint; otras comprobaciones dependen del cambio |

La salida del modelo puede omitir algo. Si ocurre, registra el hueco y revisa si
la instrucción correspondiente era específica, visible y no contradictoria.
Reescríbela una vez y repite solo ese caso.

Si vuelve a omitirlo, conserva el hallazgo: acabas de demostrar que ese límite no
puede depender solo de contexto. No alargues el archivo indefinidamente.

### 8. Revisar auto memory sin mezclar responsabilidades

Abre `/memory` y observa la sección de auto memory. Puede estar vacía o contener
aprendizajes de tus sesiones anteriores.

La decisión es simple:

- `CLAUDE.md`: instrucciones compartidas que el equipo revisa en Git;
- auto memory: aprendizaje local que Claude mantiene para este repositorio.

No copies automáticamente una en la otra. Si la auto memory contiene una
decisión que todo el equipo necesita, llévala primero a revisión y después a una
fuente versionada.

### 9. Guardar la evidencia y confirmar

Termina de completar `evidencias/s02.md`:

| Sección | Qué anotas |
|---|---|
| Descubrible en el repositorio | Un hecho que Claude descubrió sin memoria |
| Decisión que necesitaba el equipo | Una decisión que necesitó comunicación del equipo |
| Encargo propio | Qué te faltó pedir en el encargo de auditoría del paso 4 |
| Línea eliminada de /init | Una línea que quitaste del borrador |
| Prueba del contexto | Los conflictos detectados y omitidos en la propuesta |
| Límite | Un límite que requeriría una garantía técnica si aumentara el riesgo |

Revisa y confirma:

```bash
git status --short
git diff --check
git diff
git add CLAUDE.md evidencias/s02.md evidencias/claude-md-borrador.md
git diff --cached --check
git diff --cached --stat
git commit -m "Define el contexto operativo de TaskFlow"
uv run pytest -q
uv run ruff check .
git status --short
git log --oneline
```

En esta sesión el trabajo se confirma directamente en `main`: no hay revisión de
por medio y el historial queda lineal. A partir de la sesión 3 cada cambio pasa
por una rama y su revisión antes de integrarse.

Si conectaste un remoto propio, publica ahora la base:

```bash
git push -u origin main
```

## Validación

```bash
cd ~/curso-claude/curso-claude-code-api
git ls-files CLAUDE.md docs/decisiones-ingenieria.md evidencias/s02.md
git check-ignore .env
uv run pytest -q
uv run ruff check .
git status --short
```

- [ ] `/context` mostró el `CLAUDE.md` de la raíz.
- [ ] Registraste qué te faltó pedir al contrastar tu encargo con la referencia.
- [ ] Cada bloque tiene fuente, riesgo o uso frecuente que justifica cargarlo siempre.
- [ ] El archivo no repite dependencias, árbol, tutorial ni estado temporal.
- [ ] La propuesta adversa fue revisada contra cuatro conflictos concretos.
- [ ] Registraste cualquier omisión del agente sin convertirla en un falso éxito.
- [ ] Sabes qué instrucción necesitaría permiso o hook para ser garantía.
- [ ] `main` termina limpio y en verde.

## Limpieza

No elimines `CLAUDE.md`, las decisiones ni la evidencia. Forman parte del
proyecto y se reutilizan en las sesiones siguientes.

Puedes detener PostgreSQL sin borrar el volumen:

```bash
docker compose down
```

## Problemas Frecuentes

| Problema | Causa probable | Acción |
|---|---|---|
| `/init` propone skills o hooks | La sesión tiene activado `CLAUDE_CODE_NEW_INIT=1`, que abre el flujo ampliado | Elige solo instrucciones de proyecto; las extensiones llegan cuando exista su necesidad |
| `/init` no crea el archivo | Ya existe o la sesión no está en la raíz | Comprueba `pwd`, mueve el archivo previo a evidencias y repite |
| `/context` no muestra `CLAUDE.md` | La sesión estaba abierta antes de crearlo o arrancó en otro directorio | Cierra y abre `claude` desde la raíz |
| El borrador copia todo el README | Confundió documentación con instrucciones persistentes | Conserva solo comandos frecuentes, fuentes y límites no obvios |
| Claude detecta menos de cuatro conflictos | La instrucción es ambigua o la adherencia varió | Revisa manualmente, precisa una vez y repite el caso omitido |
| Una regla debe cumplirse sin excepción | `CLAUDE.md` solo orienta | Registra el caso para convertirlo en permiso o hook en la sesión 9 |
| Auto memory contiene una regla distinta | Es aprendizaje local, no política compartida | Audítala; no la copies ni la borres sin entender su origen |
