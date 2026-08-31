# Lab 02: Cerrar la Tarea con Contexto Deliberado

## Objetivo

Elegir entre continuar, hacer una pregunta lateral, compactar o empezar con
contexto limpio, y comprobar el efecto de la elección antes de integrar la rama.

## Por qué este lab

La conversación del Lab 01 contiene decisiones útiles, archivos leídos,
resultados repetidos y caminos descartados. El porcentaje ocupado no decide por
ti: una conversación grande puede seguir siendo precisa y una pequeña puede
estar contaminada por una hipótesis equivocada.

Vas a cerrar la misma entrega en dos fases. Primero conservarás la continuidad
necesaria para auditar la implementación. Después cambiarás de función y
revisarás la rama desde una conversación vacía, sin los argumentos usados para
construirla.

## Requisitos

- Lab 01 completado en `feature/persistencia`, con un commit por incremento.
- Suite, Ruff, lock y Compose en verde contra una base recién creada.
- El catálogo de estados implementado y la migración reproducible.
- Conversación de implementación todavía abierta.
- La línea base de contexto, las intervenciones y la decisión del paso 5 del
  Lab 01, presentes en la conversación o en tus notas.
- `git status --short` vacío.

## Ritmo de Trabajo

Este lab tiene 40 minutos:

| Min | Debe existir |
|---:|---|
| 0–6 | Diagnóstico del contexto tras el Lab 01 |
| 6–12 | Pregunta lateral comprobada contra una fuente |
| 12–20 | Compactación enfocada y hechos recuperados desde Git |
| 20–32 | Revisión de la rama desde contexto limpio |
| 32–40 | Evidencia confirmada, rama integrada y `main` en verde |

## Paso a Paso

### 1. Diagnosticar antes de actuar

En la conversación larga ejecuta:

```text
/context all
```

Antes de actuar, responde:

- categoría que más espacio ocupa;
- información que todavía necesitas para cerrar la entrega;
- información que ya no cambia ninguna decisión;
- una señal observada, si existe: restricción olvidada, exploración repetida,
  corrección circular o respuesta cada vez menos concreta.

No inventes una degradación para completar la evidencia. Si la conversación
sigue siendo útil, anótalo. `/context` muestra composición y capacidad; la
calidad se juzga por el trabajo.

### 2. Separar una pregunta lateral

Formula con `/btw` una pregunta que pueda responderse únicamente con lo que la
conversación ya conoce. Por ejemplo, una decisión tomada durante el incremento
de persistencia o el nombre de una comprobación ya ejecutada.

```text
/btw <tu pregunta sobre algo ya visto>
```

La respuesta no entra al historial principal y no puede usar herramientas.
Compruébala contra el commit, el archivo o la salida guardada y registra el
resultado. Si necesitas que lea o ejecute algo, `/btw` era la herramienta
equivocada: haz una petición normal.

### 3. Compactar para terminar la misma tarea

Todavía estás cerrando la misma entrega. Antes de resumir la conversación,
comprueba que el estado importante ya vive fuera de ella:

```bash
git status --short
git log --oneline main..HEAD
uv run pytest -q
uv run ruff check .
```

Redacta una instrucción propia para `/compact`. Debe pedir que se conserven:

- objetivo y fuentes del contrato de tarea;
- rama, incrementos y estado actual;
- archivos protegidos;
- comprobaciones ejecutadas y sus resultados;
- decisión pendiente de integración y riesgo residual.

Debe permitir descartar salidas repetidas, intentos corregidos y explicaciones
que ya están en el repositorio. Ejecuta tu instrucción:

```text
/compact <tu foco de compactación>
```

Después usa `/context all`. Pide a Claude tres hechos concretos sobre el estado
actual y verifica cada uno contra Git o los archivos. Que el resumen los recuerde
no los vuelve verdad; la comprobación externa sigue mandando.

### 4. Cambiar de función con contexto limpio

La implementación terminó. Ahora necesitas revisar, no continuar defendiendo
las decisiones de la conversación anterior. Etiqueta esa sesión y comienza una
vacía:

```text
/clear implementacion-persistencia
```

La conversación anterior queda disponible para una recuperación futura, pero
no entra en el nuevo contexto. Ejecuta `/context all` y confirma que las
instrucciones del proyecto sí se cargaron.

Redacta un contrato de revisión. Debe pedir
una auditoría de solo lectura con estas fuentes y límites:

- `@docs/contrato-api.md`, limitado a las secciones Salud y Estados;
- `docs/decisiones-ingenieria.md` y `CLAUDE.md` como políticas del proyecto;
- diff completo `main...HEAD` y commits de la rama;
- tests y migraciones como evidencia que debe inspeccionar, no asumir;
- sin editar, confirmar, fusionar ni cambiar la rama;
- hallazgos clasificados como bloqueante, advertencia o riesgo residual, con
  archivo y línea.

El uso de `@docs/contrato-api.md` añade el contenido completo del archivo al
contexto. Aquí el coste está justificado porque el contrato es la fuente contra
la que se revisa toda la entrega; `@` no es una forma gratuita de cargar datos.

Entrega tu contrato de revisión. Comprueba cada hallazgo antes de aceptarlo. Si
aparece un bloqueante real, regístralo, autoriza una corrección mínima en esta
sesión y repite las verificaciones. No llames "revisión independiente" a una
segunda revisión hecha después de que la misma conversación corrigió el cambio.

### 5. Confirmar la evidencia e integrar

Sal de Claude y revisa la rama tú:

```bash
git status --short
git diff --check main...HEAD
git diff --stat main...HEAD
git diff --exit-code main...HEAD -- docs/contrato-api.md docs/decisiones-ingenieria.md CLAUDE.md .gitignore
uv lock --check
uv run alembic upgrade head
uv run pytest -q
uv run ruff check .
docker compose config -q
```

Antes de integrar, ten claros los hallazgos que descartaste y lo que sigue sin
estar probado: son lo que declaras al abrir la revisión.

Integra sin crear tags:

```bash
git switch main
git merge --no-ff feature/persistencia -m "Integra la capa de persistencia"
uv run pytest -q
uv run ruff check .
git branch -d feature/persistencia
git status --short
git log --oneline -6
```

Si trabajas con un remoto propio, puedes sustituir el merge local por una pull
request o merge request. Los criterios de revisión y las verificaciones no
cambian.

## Validación

- [ ] Diagnosticaste el contexto por composición y señales, no por un umbral inventado.
- [ ] `/btw` respondió una pregunta que no necesitaba herramientas y comprobaste la respuesta.
- [ ] Tu instrucción de compactación conservó estado, verificaciones y riesgo.
- [ ] Comprobaste hechos del resumen contra Git o archivos.
- [ ] `/clear` abrió contexto vacío y conservó la conversación anterior fuera del hilo nuevo.
- [ ] La revisión limpia inspeccionó contrato, diff, tests y migraciones sin editar.
- [ ] Triaste cada hallazgo y declaraste lo que sigue sin estar probado.
- [ ] La rama se integró sin tags y `main` terminó limpio y en verde.

## Limpieza

Conserva código, migraciones, tests y decisiones. Detén PostgreSQL
sin borrar el volumen que acabas de reconstruir:

```bash
docker compose down
docker compose ps
git status --short
```

La conversación de implementación quedó guardada por `/clear`; no necesitas
reanudarla para la sesión 4. Las decisiones duraderas ya viven en Git.

## Problemas Frecuentes

| Problema | Causa probable | Acción |
|---|---|---|
| `/context` no muestra un porcentaje | La interfaz presenta capacidad como grid o advertencia | Registra categorías y estado visible; no inventes una cifra |
| Compactar reduce poco | El contexto útil seguía siendo grande o la instrucción conservó demasiado | Revisa qué información realmente cambia el cierre; no repitas por reflejo |
| El resumen olvida una decisión | `/compact` conserva una síntesis, no una transcripción | Recupera el hecho desde Git o el archivo y corrige el curso de la tarea |
| `/btw` no puede leer un archivo | Las preguntas laterales no tienen herramientas | Usa una petición normal si necesitas nueva evidencia |
| `/btw` no existe | La versión instalada no lo incluye | Abre una sesión aparte para la consulta y no la uses como evidencia persistente |
| `@ruta` aumenta mucho el contexto | Una referencia de archivo incluye su contenido completo | Carga solo la fuente necesaria y evita directorios o archivos grandes sin motivo |
| `/clear` parece haber perdido el trabajo | El trabajo solo estaba en la conversación | Usa Git y los tests; la conversación anterior sigue disponible en el historial |
| La revisión propone proyectos o tareas | Leyó el contrato completo sin respetar el alcance de hoy | Rechaza el hallazgo: esas secciones son contexto, no trabajo autorizado |
| Aparece un bloqueante al final | Una comprobación previa no cubría ese riesgo | No integres hasta corregir y repetir los gates; conserva el hallazgo en la evidencia |
