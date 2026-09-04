# Lab 01: Inicializar un Proyecto Bajo Contrato

## Objetivo

Dirigir a Claude Code para crear desde cero una base FastAPI reproducible,
mantener el cambio dentro de un alcance explícito y aceptar el resultado solo
después de verificar código, configuración y ejecución real.

## Por qué este lab

Una base preconstruida ocultaría las decisiones que necesitas aprender a
delegar: qué archivos crear, qué dejar fuera, cómo traducir un contrato a tests
y qué evidencia exigir antes de confirmar el primer commit.

Partes de un repositorio que solo contiene dos fuentes humanas: el contrato de
comportamiento y una política mínima de exclusión. Claude construye la
aplicación, las dependencias, los tests, Compose, la documentación y el lock. La
salida puede variar; los criterios de aceptación no.

## Requisitos

- Preflight completado: Git, Python 3.12, uv y Docker funcionan.
- La variable `$CURSO` definida.
- La imagen `postgres:18-alpine` descargada.
- Ningún repositorio previo en `~/curso-claude/curso-claude-code-api` que quieras conservar.

## Ritmo de Trabajo

Este lab tiene 55 minutos. Usa estos puntos de control para no convertir la
generación en una espera pasiva:

| Min | Debe existir |
|---:|---|
| 0–10 | Repositorio mínimo, encargo propio y una diferencia anotada tras el contraste |
| 10–25 | Plan revisado y primera implementación generada |
| 25–40 | Alcance auditado con `/diff` y cuatro comprobaciones independientes en verde |
| 40–45 | PostgreSQL declarado llega a `healthy` |
| 45–55 | Mapa de onboarding, `/context` sin memoria de proyecto y commit |

Una descarga lenta no rebaja el contrato. Mientras termina, revisa el plan, el
árbol y los límites negativos. Si el bloqueo persiste más de dos o tres
minutos, pídele a Claude que ejecute `docker pull postgres:18-alpine` por
separado, con la salida completa a la vista, y no sigas sin ver `healthy`.

## Paso a Paso

### 1. Preparar un repositorio mínimo

```bash
mkdir -p ~/curso-claude/curso-claude-code-api
cd ~/curso-claude/curso-claude-code-api
git init -b main
mkdir -p docs evidencias
export MATERIAL=$CURSO/sesiones/sesion-02-fundar-el-proyecto/labs/01-base-verificable/material
cp $CURSO/proyecto-integrador/contrato-api.md docs/contrato-api.md
cp $MATERIAL/gitignore-proyecto .gitignore
git add docs/contrato-api.md .gitignore
git commit -m "Define el contrato inicial de TaskFlow"
git status --short
```

`.gitignore` es una barrera de seguridad, no una solución del ejercicio. Solo
excluye secretos, entornos y cachés locales. Claude no debe modificarlo.

Comprueba el punto de partida:

```bash
find . -maxdepth 2 -type f -not -path './.git/*' | sort
```

Solo deben aparecer `.gitignore` y `docs/contrato-api.md`. No existe código,
`CLAUDE.md`, lock ni configuración de proyecto.


### 2. Redactar y contrastar la especificación

Redacta tu propio contrato de tarea. Al de la sesión 1 —resultado, fuentes,
alcance, restricciones y verificación— esta entrega le añade una parte más:
el **proceso**, es decir, si Claude debe explorar, planificar y esperar
aprobación antes de editar. La referencia rápida de esta sesión tiene las seis.

Debe partir de `docs/contrato-api.md`, permitir solo la base del proyecto y
dejar todo el contrato futuro fuera de esta entrega.

Después abre Claude Code desde la raíz:

```bash
claude
```

Compara tu borrador con este contrato de referencia. No lo copies sin revisar:
quédate con una restricción que te faltaba o una línea de tu borrador que
eliminaste por innecesaria.

<details>
<summary>Contrato de referencia para contrastar</summary>

```text
Crea desde cero la base de una API FastAPI administrada con uv y Python 3.12.

Antes de editar:
1. lee docs/contrato-api.md y el estado actual del repositorio;
2. identifica las restricciones que afectan a esta primera entrega;
3. presenta un plan breve con archivos y verificaciones;
4. detente y espera mi aprobación.

Alcance permitido:
- pyproject.toml;
- app/;
- tests/;
- compose.yaml;
- .env.example;
- README.md;
- uv.lock, únicamente como resultado del flujo de uv.

No crees CLAUDE.md ni implementes endpoints distintos de GET /health.
No modifiques docs/contrato-api.md ni .gitignore.
No crees, abras, muestres ni edites .env. No escribas secretos reales.

Debe cumplir:
- pyproject.toml limita requires-python a la serie 3.12.
- GET /health responde 200 y {"status":"ok"}.
- La aplicación ASGI se expone como app.main:app.
- tests/test_health.py comprueba código de estado y cuerpo mediante una petición
  ASGI.
- PostgreSQL 18-alpine se declara como servicio db con healthcheck.
- El volumen de PostgreSQL se monta en /var/lib/postgresql, no en
  /var/lib/postgresql/data.
- .env.example documenta POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB y
  POSTGRES_PORT con valores locales ficticios.
- compose.yaml puede renderizarse sin crear .env; usa valores locales seguros
  por defecto cuando sea necesario.
- README.md contiene un solo recorrido canónico basado en uv sync --locked,
  pytest, Ruff, docker compose up, Uvicorn y docker compose down.
- uv run pytest -q, uv run ruff check . y docker compose config -q pasan desde
  la raíz.

No debilites una comprobación para conseguir verde. Todavía no implementes:
primero explora, presenta el plan y espera.
```

</details>

La aplicación **ASGI** es el objeto que recibe peticiones dentro del proceso;
`app.main:app` significa "objeto `app` del módulo `app.main`". Un **healthcheck**
es el comando periódico con el que Docker decide si un servicio está listo. Si
estos términos no aparecían en tu borrador, decide si necesitas nombrarlos o si
el resultado observable ya elimina la ambigüedad.

Entrega a Claude tu versión corregida, no necesariamente la redacción literal de
la referencia.

El contrato contiene información propia de esta tarea: alcance, contrato de
salida y criterio de terminación. No pertenece al futuro `CLAUDE.md` completo.

### 3. Aprobar o corregir el plan

No respondas "sí" por reflejo. El plan debe dejar claro:

| Decisión | Resultado aceptable |
|---|---|
| Comportamiento | Solo `GET /health` |
| Dependencias | FastAPI y Uvicorn; pytest, HTTPX y Ruff para desarrollo |
| Python | `requires-python` acepta 3.12 y excluye 3.13 |
| Aplicación y test | `app.main:app`; petición ASGI en `tests/test_health.py` que afirma `200` y el JSON exacto |
| Compose | PostgreSQL 18, healthcheck y montaje correcto |
| Configuración | `.env.example` ficticio; `compose config` funciona sin `.env` |
| Documentación | Un recorrido canónico, no alternativas incompatibles |
| Exclusiones | Contrato y `.gitignore` permanecen intactos |

Si falta algo, corrige solo el plan:

```text
Antes de implementar, corrige el plan: falta <criterio concreto>.
Mantén el alcance y no edites todavía.
```

Cuando el plan sea aceptable:

```text
Plan aprobado. Implementa exactamente ese alcance. Ejecuta antes de terminar:
uv run pytest -q
uv run ruff check .
docker compose config -q

Si algo falla, corrige la causa sin ampliar el alcance ni debilitar el test.
Al final informa archivos cambiados, resultado de cada comando y riesgos
residuales. No hagas commit.
```

Observa la ejecución. Interrumpe si Claude intenta tocar el contrato, cambiar
`.gitignore`, crear `.env`, añadir endpoints o resolver funcionalidades futuras.

### 4. Auditar el resultado, no el relato

Claude acaba de contarte lo que hizo. Ese resumen no es evidencia: compruébalo
antes de aceptarlo, primero dentro de la sesión y después desde Git.

Sin salir de la conversación, abre el visor de cambios:

```text
/diff
```

Las flechas izquierda y derecha alternan entre el diff completo y **el cambio de
cada turno por separado**; arriba y abajo recorren los archivos. `Enter` abre el
diff de uno, `Esc` vuelve a la lista.

Recorre turno por turno y responde tres preguntas:

| Pregunta | Qué buscas |
|---|---|
| ¿Qué archivo tocó cada turno? | Un turno que edite algo fuera del alcance aprobado |
| ¿Algún turno modificó un archivo protegido? | Contrato, `.gitignore` o un `.env` creado de paso |
| ¿Hay cambios que nadie pidió? | Endpoints extra, dependencias añadidas, configuración futura |

Ver el diff por turno es lo que distingue "el resultado final está bien" de "el
camino fue correcto". Un archivo tocado y luego revertido no aparece en el diff
final, pero sí en su turno.

Después termina la conversación con `/exit` y revisa desde Git:

```bash
git status --short
git add -N .
git diff --check
git diff --name-only
git diff --stat
git diff -- . ':(exclude)uv.lock'
```

`git add -N` no prepara contenido: permite que `git diff` muestre archivos
nuevos. El conjunto esperado es `pyproject.toml`, `uv.lock`, `app/`, `tests/`,
`compose.yaml`, `.env.example` y `README.md`.

Prueba explícitamente los límites negativos:

```bash
git diff --exit-code -- docs/contrato-api.md .gitignore
test ! -e CLAUDE.md
test ! -e .env
git check-ignore -v .env
```

Los cuatro comandos deben terminar correctamente. Una prueba negativa evita
aceptar un resultado que funciona a costa de violar el alcance.

### 5. Ejecutar verificaciones independientes

No uses el resumen de Claude como evidencia. Ejecuta tú:

```bash
uv lock --check
uv run pytest -q
uv run ruff check .
docker compose config -q
```

Cada comando cubre una capa distinta:

| Comprobación | Qué demuestra | Qué no demuestra |
|---|---|---|
| `uv lock --check` | El lock coincide con el proyecto | Que la API se comporte bien |
| `pytest` | `/health` cumple el contrato ejecutable | Que PostgreSQL arranque |
| `ruff` | El código y los tests pasan el análisis configurado | Que el alcance sea correcto |
| `compose config` | Compose renderiza sin depender de un `.env` secreto | Que el servicio llegue a `healthy` |

Si algo falla, vuelve a Claude con el comando, la salida completa y esta
restricción:

```text
Esta verificación independiente falla. Diagnostica la causa antes de editar.
Corrige solo la causa, no cambies el contrato ni debilites el test. Repite las
tres verificaciones obligatorias al terminar.
```

Revisa el nuevo diff antes de continuar.

### 6. Comprobar que la base declarada arranca

Las comprobaciones del paso 5 leen archivos. Esta arranca el servicio: es la
diferencia entre "Compose está bien escrito" y "Compose funciona".

Crea la configuración local fuera de la conversación:

```bash
cp .env.example .env
git check-ignore -v .env
docker compose up -d --wait db
docker compose ps
```

`--wait` no devuelve el control hasta que el healthcheck pasa, así que si el
comando termina, el servicio llegó a `healthy`. Ese es el único hecho que este
paso necesita demostrar: el contrato pedía PostgreSQL 18 con healthcheck, y lo
declarado arranca de verdad.

`.env` debe aparecer ignorado y fuera de `git status`. Claude no lo abre ni lo
necesita.

PostgreSQL queda activo para el Lab 02. La API todavía no lo usa: `GET /health`
no consulta la base, y conectarlos es trabajo de la sesión 3.

### 7. Medir qué puede descubrir sin memoria de proyecto

Abre una conversación nueva y pide una exploración de solo lectura:

```text
Explora este repositorio sin editar nada y prepara un mapa de onboarding breve.

Necesito:
1. fuente de verdad del comportamiento;
2. comandos exactos para instalar, probar, revisar estilo, ejecutar y detener;
3. motor que deben usar los futuros tests de persistencia;
4. límites sobre archivos con secretos;
5. cualquier decisión que no puedas establecer con evidencia.

Cita archivo y línea para cada hecho. Separa hechos, inferencias y desconocidos.
```

El repositorio permite descubrir contrato, comandos y tecnología declarada.
Todavía no contiene dos acuerdos del equipo: si SQLite está permitido para
tests y si Claude puede abrir `.env`. Una respuesta rigurosa los marca como
desconocidos o inferencias, nunca como políticas inventadas.

Antes de salir, comprueba con qué contaba esta conversación:

```text
/context
```

No debe aparecer ningún `CLAUDE.md` de proyecto bajo **Memory files**: todavía
no existe. Lo que Claude acaba de mapear salió de leer el repositorio, no de
instrucciones cargadas. El Lab 02 crea ese archivo y vuelve a mirar aquí.

Antes de salir, ten claro:

- qué decisión del plan corregiste o aprobaste conscientemente;
- qué verificó Claude y qué verificaste tú;
- qué archivo o dependencia quitaste por exceder el alcance;
- las dos lagunas que dejó el mapa de onboarding.

Sal con `/exit`.

### 8. Confirmar la base generada

```bash
git status --short
git add -A
git diff --cached --check
git diff --cached --stat
git diff --cached -- . ':(exclude)uv.lock'
git commit -m "Inicializa TaskFlow bajo contrato"
git status --short
```

El resumen debe incluir `uv.lock`; el diff detallado lo omite porque es generado
y extenso. `.env` y `.venv` no deben entrar al commit.

La base queda confirmada en `main`. El Lab 02 continúa sobre el mismo historial y
añade allí las decisiones y el contexto del proyecto.

## Validación

```bash
cd ~/curso-claude/curso-claude-code-api
git diff HEAD~1 --name-only
git diff HEAD~1 --exit-code -- docs/contrato-api.md .gitignore
git ls-files .env .env.example
uv lock --check
uv run pytest -q
uv run ruff check .
docker compose config -q
git status --short
```

`docker compose ps` no aparece aquí: si ya detuviste el servicio, su salida vacía
no distingue un fallo de una limpieza. El arranque se comprobó en el paso 6.

- [ ] Claude exploró y presentó un plan antes de editar.
- [ ] Redactaste el encargo inicial y registraste qué corregiste al contrastarlo.
- [ ] Recorriste el cambio turno por turno con `/diff` antes de mirar Git.
- [ ] `/context` confirmó que no había memoria de proyecto cargada todavía.
- [ ] El cambio se mantuvo dentro del alcance permitido.
- [ ] Contrato, `.gitignore`, `.env` y `CLAUDE.md` pasaron las pruebas negativas.
- [ ] Lock, test, lint y configuración de Compose pasan de forma independiente.
- [ ] PostgreSQL declarado en Compose llegó a `healthy`.
- [ ] `tests/test_health.py` afirma código y JSON exacto, y pasa.
- [ ] `git ls-files` muestra `.env.example`, nunca `.env`.
- [ ] La evidencia distingue lo que hizo Claude de lo que verificaste tú.
- [ ] `main` termina limpio y en verde.

## Limpieza

Conserva PostgreSQL activo si continúas inmediatamente con el Lab 02; si haces
una pausa, detenlo sin borrar el volumen:

```bash
docker compose down
```

## Problemas Frecuentes

| Problema | Causa probable | Acción |
|---|---|---|
| Claude empieza a editar sin detenerse | Ignoró la puerta del prompt | Interrumpe, revisa el diff actual y exige el plan antes de continuar |
| Propone toda la API del contrato | Confundió fuente de verdad con alcance de la entrega | Repite: solo `GET /health`; el resto es contexto, no trabajo autorizado |
| Modifica contrato o `.gitignore` | Excedió el alcance explícito | Rechaza esos cambios y comprueba con `git diff --exit-code` |
| `docker compose config -q` exige `.env` | Compose no declara valores locales por defecto | Corrige `compose.yaml`; no crees `.env` para ocultar el fallo de configuración |
| `uv lock --check` falla | Dependencias y lock no coinciden | Ejecuta `uv lock`, revisa el cambio y repite las verificaciones |
| El test pasa pero emite advertencias | Eligió una API de test deprecada | Pide eliminar la causa de la advertencia sin silenciarla globalmente |
| PostgreSQL queda `unhealthy` | Variables o healthcheck no coinciden | Revisa `docker compose logs db --tail 30` sin mostrar valores sensibles |
| El puerto de PostgreSQL está ocupado | Otro proceso usa el puerto de host | Cambia solo la variable de puerto en tu `.env` local y repite |
| `.env` aparece en Git | La política de exclusión fue alterada | No confirmes; restaura la política y repite `git check-ignore -v .env` |
