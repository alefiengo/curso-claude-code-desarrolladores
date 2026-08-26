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
- No debe existir todavía un `CLAUDE.md` de proyecto.

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

Anota en `evidencias/s02.md` qué fuentes ajenas al proyecto existen y cuáles
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

Abre Claude de nuevo y pide una revisión sin edición:

```text
Audita @CLAUDE.md usando @docs/decisiones-ingenieria.md y el repositorio.
No edites todavía.

Para cada bloque indica una de estas decisiones:
- RAÍZ: debe estar presente en cualquier tarea;
- POR RUTA: solo aplica a ciertos archivos;
- BAJO DEMANDA: es un procedimiento, no contexto permanente;
- DOCUMENTACIÓN: pertenece al README o a docs, no a instrucciones;
- ELIMINAR: es genérico, duplicado, obvio o temporal.

Cita la fuente o el riesgo concreto que justifica cada elemento marcado RAÍZ.
Señala también cualquier decisión del equipo que el borrador haya omitido.
```

No evalúes por cantidad de texto. Evalúa si cada instrucción tiene un trabajo
claro y el alcance correcto.

### 5. Escribir el contexto mínimo suficiente

Pide la reescritura con esta barra de calidad:

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

Sal y revisa tú el archivo completo:

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

Si aparece en `/memory` pero no en `/context`, no des por hecha la carga. Revisa
su ubicación y asegúrate de haber iniciado la sesión desde la raíz del proyecto.

### 7. Evaluar el contexto con una propuesta adversa

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

Completa `evidencias/s02.md` con:

- un hecho que Claude descubrió sin memoria;
- una decisión que necesitó comunicación del equipo;
- una línea eliminada del borrador de `/init`;
- los conflictos detectados y omitidos en la propuesta;
- un límite que requeriría enforcement si aumentara el riesgo.

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
| `/init` propone skills o hooks | La versión actual ofrece una inicialización más amplia | Elige solo instrucciones de proyecto; las extensiones llegan cuando exista su necesidad |
| `/init` no crea el archivo | Ya existe o la sesión no está en la raíz | Comprueba `pwd`, mueve el archivo previo a evidencias y repite |
| `/context` no muestra `CLAUDE.md` | La sesión estaba abierta antes de crearlo o arrancó en otro directorio | Cierra y abre `claude` desde la raíz |
| El borrador copia todo el README | Confundió documentación con instrucciones persistentes | Conserva solo comandos frecuentes, fuentes y límites no obvios |
| Claude detecta menos de cuatro conflictos | La instrucción es ambigua o la adherencia varió | Revisa manualmente, precisa una vez y repite el caso omitido |
| Una regla debe cumplirse sin excepción | `CLAUDE.md` solo orienta | Registra el caso para convertirlo en permiso o hook en la sesión 9 |
| Auto memory contiene una regla distinta | Es aprendizaje local, no política compartida | Audítala; no la copies ni la borres sin entender su origen |
