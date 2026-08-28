# Lab 01: Dirigir un Cambio Largo sin Perder el Control

## Objetivo

Dirigir la conexión de la API a PostgreSQL interviniendo durante el trabajo:
detectar una desviación en el turno en que ocurre, redirigir con un hecho
concreto y decidir cuándo la conversación deja de ayudar.

## Por qué este lab

En la sesión 2 revisaste el resultado al final, con `/diff` y Git. Eso funciona
cuando el cambio cabe en un turno.

Conectar la API a una base de datos no cabe. Hay que declarar modelos, montar
migraciones, sembrar un catálogo, preparar fixtures contra PostgreSQL y escribir
tests que dependen de todo lo anterior. La conversación se alarga: aparecen
salidas repetidas, intentos corregidos y supuestos que nadie declaró. Revisar
solo al final significa descubrir una desviación cuando ya está enterrada bajo
seis turnos de trabajo encima.

Aquí revisas mientras ocurre. El objetivo no es que Claude acierte a la primera:
es que tú notes el primer turno en que se sale del acuerdo.

## Requisitos

- Sesión 2 completada, con `main` limpio y en verde.
- `CLAUDE.md`, `docs/contrato-api.md` y `docs/decisiones-ingenieria.md`
  versionados.
- PostgreSQL declarado en Compose y la imagen `postgres:18-alpine` disponible.
- `git status --short` vacío.

## Ritmo de Trabajo

Este lab tiene 55 minutos:

| Min | Debe existir |
|---:|---|
| 0–8 | Rama creada, línea base verificada y contexto inicial registrado |
| 8–18 | Contrato de tarea propio y secuencia de incrementos acordada |
| 18–33 | Persistencia y migración, con al menos una intervención registrada |
| 33–40 | Tests del catálogo de estados en rojo |
| 40–48 | Decisión de contexto tomada y registrada |
| 48–55 | Catálogo en verde, reproducción desde base vacía y commits |

Si un incremento se alarga, no lo compenses saltando la revisión: conserva la
rama y termina desde este mismo contrato antes de la sesión 4.

## Paso a Paso

### 1. Abrir la rama y medir el punto de partida

Desde el `main` verificado que dejó la sesión 2:

```bash
cd ~/curso-claude/curso-claude-code-api
git switch main
git status --short
uv run pytest -q
uv run ruff check .
docker compose up -d --wait db
git switch -c feature/persistencia
export MATERIAL=$CURSO/sesiones/sesion-03-administrar-el-contexto/labs/01-persistencia-vigilada/material
cp $MATERIAL/evidencia-s03.md evidencias/s03.md
```

Si falta `.env`, créalo tú, fuera de la conversación:

```bash
cp .env.example .env
git check-ignore -v .env
```

Abre una conversación y mide con qué empiezas:

```bash
claude
```

```text
/context all
```

Registra en `evidencias/s03.md` qué ocupa más espacio ahora. Esta es tu línea
base: al final del lab vuelves a mirar y la comparas. Todavía no es una razón
para compactar.

### 2. Acordar el contrato de tarea

Completa **Contrato de Tarea** en `evidencias/s03.md` antes de pedir código.

Es el mismo contrato de las sesiones 1 y 2. Cambia una cosa: las restricciones
se abren en dos filas —lo que queda fuera del alcance y los archivos que no se
tocan— porque el cambio llega en varios turnos y necesitas poder decir cuál de
los dos límites se cruzó.

Tu encargo debe resolver estas decisiones:

| Parte | Barra de aceptación |
|---|---|
| Fuentes | `docs/contrato-api.md` (secciones Salud y Estados), `docs/decisiones-ingenieria.md`, `CLAUDE.md` |
| Resultado | La API persiste sobre PostgreSQL 18 y expone el catálogo de estados |
| Alcance | Configuración de base de datos, modelos, migración, seed del catálogo, fixtures de test y la ruta de estados |
| Fuera de alcance | Proyectos, tareas, filtros, `due_at`, skills, hooks y CI |
| Protegidos | Contrato, decisiones, `CLAUDE.md`, `.gitignore`, `.env` y los tests ya confirmados |
| Proceso | Explorar, proponer incrementos, esperar aprobación y **detenerse después de cada uno** |
| Terminación | Migración desde base vacía, suite, Ruff, lock y Compose, sin debilitar ninguna comprobación para conseguir verde |

Proyectos y tareas llegan en las sesiones 4 y 5. Hoy construyes la capa sobre la
que se apoyan, que es la parte que de verdad llena una conversación.

Contrasta tu borrador con la referencia y entrega después tu versión:

<details>
<summary>Contrato de referencia para contrastar</summary>

```text
Vamos a conectar esta API a PostgreSQL en varios incrementos. Hoy solo acordamos
el plan.

Fuentes: docs/contrato-api.md, secciones Salud y Estados;
docs/decisiones-ingenieria.md; CLAUDE.md.

Antes de editar nada:
1. explora el repositorio y di qué existe ya;
2. propón una secuencia de incrementos, cada uno con su comprobación;
3. detente y espera mi aprobación.

Cada incremento debe poder confirmarse solo. Después de terminar uno, para y
espera; no encadenes el siguiente.

Fuera de alcance: proyectos, tareas, filtros, due_at, skills, hooks y CI.

No modifiques docs/contrato-api.md, docs/decisiones-ingenieria.md, CLAUDE.md,
.gitignore ni .env. No abras .env.

No debilites una comprobación para conseguir verde.
```

</details>

La secuencia que propongas debe conservar estas tres puertas, aunque los nombres
de archivo varíen:

1. persistencia y migración inicial;
2. tests del catálogo de estados, en rojo;
3. catálogo de estados en verde.

Si la propuesta mezcla todo en un paso, corrígela antes de aprobar. Un incremento
que no se puede confirmar solo tampoco se puede revisar solo.

### 3. Vigilar el primer incremento

Autoriza solo persistencia y migración. Mientras Claude trabaja, **no esperes al
final**: observa qué archivo abre y qué decide.

Interrumpe con `Esc` en cuanto veas cualquiera de estas señales:

| Señal | Por qué importa |
|---|---|
| Abre o intenta leer `.env` | Es un límite declarado, no una preferencia |
| Introduce SQLite | Contradice las decisiones de ingeniería |
| Edita el contrato o `CLAUDE.md` | Está cambiando la fuente en vez de cumplirla |
| Escribe una URL de conexión en el código | Convierte configuración ausente en error de conexión |
| Empieza el catálogo sin haber terminado la migración | Encadenó incrementos; el acuerdo era detenerse |

Al interrumpir, redirige con el hecho, no con una queja:

```text
Para. Acabas de <acción concreta>, y el acuerdo dice <límite concreto>.
Vuelve al incremento actual y termina solo eso.
```

Registra en `evidencias/s03.md` **en qué turno ocurrió y qué dijiste**. Si no
hubo ninguna desviación, anótalo también: es un resultado válido, y saber que lo
vigilaste es la evidencia.

Cuando el incremento termine, revísalo dentro de la sesión antes de mirar Git:

```text
/diff
```

Recorre turno por turno. Buscas lo mismo que en la sesión 2 —archivos fuera de
alcance, protegidos tocados, cambios que nadie pidió— pero ahora sobre un cambio
que llegó en varios turnos.

Después comprueba fuera:

```bash
uv run alembic upgrade head
uv run alembic downgrade base
uv run alembic upgrade head
uv run pytest -q
grep -Rni 'sqlite' app tests pyproject.toml
git add -A && git commit -m "Añade persistencia y la migración inicial"
```

Los dos `upgrade` con un `downgrade` en medio comprueban que la migración se
puede repetir. El `grep` no debe encontrar nada.

### 4. Fijar los tests en rojo

Autoriza solo la suite del catálogo. Debe cubrir que los estados definidos en el
contrato existen tras migrar, que se devuelven en un orden estable y que el
catálogo no se duplica al aplicar la migración dos veces.

Cuando termine, comprueba que el rojo es el correcto:

```bash
uv run pytest -q > evidencias/estados-rojo.txt 2>&1
sed -n '1,60p' evidencias/estados-rojo.txt
```

Un rojo útil dice `failed`, no `errors`. Si ves `errors`, los tests se rompieron
al importar algo que aún no existe y no están probando el contrato: pide que
usen solo lo que ya está montado.

```bash
git add tests evidencias/estados-rojo.txt && git commit -m "Define el contrato ejecutable del catálogo de estados"
```

### 5. Decidir qué hacer con la conversación

Llevas dos incrementos y una exploración inicial. Antes de seguir, mide:

```text
/context all
```

Compara con tu línea base del paso 1 y responde en `evidencias/s03.md`:

- ¿qué ocupa más espacio ahora?
- ¿qué parte todavía cambia una decisión?
- ¿qué parte ya es ruido —salidas repetidas, intentos corregidos, exploración
  que terminó?

Ahora elige, y anota **por qué**:

| Si… | Entonces |
|---|---|
| La tarea sigue clara y lo cargado es pertinente | Continúa |
| Necesitas un dato de algo ya visto, sin interrumpir | `/btw <pregunta>` |
| Sigue la misma tarea pero la historia útil ocupa demasiado | `/compact <foco>` |

Si compactas, tu foco debe nombrar qué conservar: rama, incrementos hechos,
archivos protegidos, comprobaciones ejecutadas y lo que falta. Después vuelve a
mirar `/context all` y pide tres hechos concretos sobre el estado actual;
comprueba cada uno contra Git antes de creerlo.

No hay respuesta correcta única. Continuar es una decisión tan válida como
compactar, siempre que puedas decir qué observaste para tomarla. Lo que se
evalúa es la razón, no el porcentaje.

### 6. Cerrar el catálogo en verde

Autoriza el último incremento. Al aceptarlo exige dos cosas a la vez:

- los tests del catálogo pasan;
- la migración sigue siendo reproducible desde una base vacía.

```bash
git diff --exit-code HEAD -- docs CLAUDE.md .gitignore
uv run pytest -q
uv run ruff check .
git add -A && git commit -m "Implementa el catálogo de estados"
```

`git diff --exit-code` sobre los protegidos falla si alguno cambió. Es la
comprobación que no depende de que tú te acuerdes de mirar.

### 7. Reproducir desde cero y auditar la rama

La siguiente operación borra **el volumen local de PostgreSQL de este proyecto**.
Contiene datos de ejercicio que deben poder reconstruirse; si guardaste algo más
ahí, respáldalo antes.

```bash
docker compose down -v
docker compose up -d --wait db
uv run alembic upgrade head
uv run pytest -q
uv run ruff check .
uv lock --check
docker compose config -q
git log --oneline main..HEAD
git status --short
```

Tres commits, uno por incremento. No integres todavía: el Lab 02 revisa esta
rama desde una conversación vacía antes de fusionarla.

## Validación

- [ ] La rama nació de un `main` limpio y en verde, sin tags.
- [ ] Redactaste el contrato de tarea y acordaste la secuencia antes de generar.
- [ ] Vigilaste durante la generación y registraste las intervenciones, o su ausencia.
- [ ] Recorriste al menos un incremento con `/diff` turno por turno.
- [ ] Los tests del catálogo fallaron con `failed`, no con `errors`, antes de implementar.
- [ ] Los archivos protegidos pasan `git diff --exit-code`.
- [ ] Decidiste entre continuar, `/btw` y `/compact` con una razón registrada.
- [ ] La migración reconstruye el esquema y el catálogo desde una base vacía.
- [ ] El historial tiene un commit por incremento.

## Limpieza

No borres la rama ni el volumen: el Lab 02 los necesita.

```bash
git branch --show-current
git log --oneline main..HEAD
```

## Problemas Frecuentes

| Problema | Causa probable | Acción |
|---|---|---|
| Claude encadena incrementos sin parar | El contrato no exigió detenerse después de cada uno | Interrumpe con `Esc`, recuerda el acuerdo y pide terminar solo el actual |
| Alembic falla por conexión | PostgreSQL no está listo o `.env` no coincide con `.env.example` | Revisa `docker compose ps`; recrea `.env` tú, sin mostrarlo a Claude |
| `pytest` devuelve `errors` en vez de `failed` | Los tests importan algo que todavía no existe | Pide que usen solo lo ya montado; la estructura futura llega con su incremento |
| Todo verde antes del último incremento | Los tests no cubren el catálogo, o el alcance creció | Audita el diff de `tests` antes de confirmar |
| El catálogo de estados se duplica | El seed no es [idempotente](../../../../docs/glosario.md#idempotente) o vive fuera de la migración | Corrige la migración y prueba dos `upgrade` sobre una base vacía |
| Aparece una URL de PostgreSQL en el código | Se añadió un valor por defecto para tapar configuración ausente | Elimínalo; sin variables el proyecto debe fallar diciendo eso |
| Claude empieza a crear proyectos o tareas | Confundió la fuente de verdad con el alcance de hoy | Recuerda que el contrato completo es contexto; el trabajo autorizado son estados |
| No hubo ninguna desviación que interrumpir | El modelo acertó esta vez | Regístralo como resultado; la vigilancia es la práctica, no el fallo |
| El contexto apenas creció | El incremento salió limpio y sin correcciones | Registra "continuar" con esa razón; no compactes por cumplir el paso |
