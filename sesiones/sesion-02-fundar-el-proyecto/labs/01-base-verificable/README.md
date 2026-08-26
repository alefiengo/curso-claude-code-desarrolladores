# Lab 01: Base Verificable

## Objetivo

Crear `curso-claude-code-api` con una ruta de salud y un entorno repetible.

## Por qué este lab

"Crea una API" suele producir algo que arranca en la máquina donde se creó y en
ninguna otra. En vez de eso vas a entregar una lista de condiciones concretas
—qué debe responder, cómo se declara la base de datos, qué comandos tienen que
pasar— y luego a comprobar el resultado tú mismo.

Verás algo que se repite en todo el curso: los tres comandos de verificación
pueden dar verde sobre un archivo que **no arranca**. Comprobar la sintaxis no es
comprobar que funciona.

## Requisitos

- Preflight completado.
- [Contrato de la API](../../../../proyecto-integrador/contrato-api.md) abierto.
- Reglas de [seguridad](../../../../docs/seguridad.md) leídas.

## Paso a Paso

### 1. Crear el repositorio

```bash
mkdir -p ~/curso-claude/curso-claude-code-api
cd ~/curso-claude/curso-claude-code-api
git init -b main
code .gitignore
```

Crea el archivo en el editor con estas cinco líneas y guárdalo:

```text
.env
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
```

```bash
git add .gitignore && git commit -m "Inicia el repositorio"
```

`main` es la rama de integración durante todo el curso: recibe lo que está
verificado, y cada sesión arranca desde ahí. La regla completa está en el
[flujo de trabajo con Git](../../../../proyecto-integrador/flujo-git.md).

A partir de la sesión 3, los cambios de código van en su propia rama y se
integran al cerrar. Hoy no: este es el commit fundacional y va directo a `main`,
porque todavía no existe un estado verificado del que salir ni contra el que
comparar. Una rama aquí no protegería nada.

Crea `docs/` y `evidencias/`. Copia el
[contrato del curso](../../../../proyecto-integrador/contrato-api.md) como
`docs/contrato-api.md`; ese archivo será la fuente funcional dentro de tu
repositorio.

### 2. Formular el contrato

Abre `claude` y entrega esta tarea:

```text
Crea la base de una API FastAPI administrada con uv y Python 3.12.
Alcance: pyproject.toml, app/, tests/, compose.yaml, .env.example y README.md.
Respeta docs/contrato-api.md; en esta sesión implementa solo GET /health.
No escribas secretos ni modifiques .gitignore.

Invariantes:
- GET /health responde 200 y {"status":"ok"}.
- PostgreSQL 18-alpine se declara como servicio db con healthcheck, y su volumen
  se monta en /var/lib/postgresql, no en /var/lib/postgresql/data.
- .env.example documenta variables sin valores reales.
- README contiene un único camino para instalar, probar, ejecutar y detener.
- `uv run pytest -q`, `uv run ruff check .` y `docker compose config -q` pasan.

Explora primero. Implementa y ejecuta las tres verificaciones antes de terminar.
```

Revisa las solicitudes de instalación y los archivos antes de aprobar.

### 3. Comprobar que `pytest` encuentra tu código

Ejecuta la suite antes de seguir:

```bash
uv run pytest -q
```

Pueden pasar dos cosas, y las dos son normales. Anota cuál te tocó:

| Lo que ves | Qué significa |
|---|---|
| `1 passed` | `pyproject.toml` declara un `[build-system]`, así que `uv sync` instaló tu proyecto y `app` ya es importable |
| `ModuleNotFoundError: No module named 'app'` | No hay `[build-system]`: `app` no está instalado ni en la ruta de búsqueda |

Los tests viven en `tests/` e importan `app`. Para que eso funcione, `app` tiene
que estar instalado —lo hace `uv sync` cuando el proyecto declara cómo
construirse— o estar en la ruta donde Python busca módulos. Que el agente haya
declarado un `[build-system]` o no depende de cómo resolvió la tarea.

**Si te salió el error**, añade a `pyproject.toml`:

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
```

Y vuelve a ejecutar `uv run pytest -q`. Es la solución más directa: le dice a
`pytest` que busque módulos también en la raíz del proyecto.

**Si te salió en verde**, no añadas nada. Comprueba por qué funciona:

```bash
grep -A3 "build-system" pyproject.toml
```

En los dos casos acabas con la suite pasando, que es lo que exige el contrato.
Lo que cambia es qué mecanismo lo consigue, y ahora sabes cuál usa tu proyecto.

> La configuración se añade cuando el código la pide, no por adelantado. Más
> adelante, al aparecer la primera ruta que inyecta dependencias, hará falta otro
> ajuste para `ruff`. Añadirlo hoy sería configuración muerta en el repositorio.

### 4. Auditar, no solo ejecutar

```bash
git status --short
git diff -- . ':(exclude)uv.lock'
uv run pytest -q
uv run ruff check .
docker compose config -q
git check-ignore -v .env
```

**Los tres comandos en verde no bastan, y conviene ver por qué.**
`docker compose config -q` valida la **sintaxis** del archivo. Devuelve `0`
aunque la contraseña quede vacía, aunque el puerto no se publique y aunque el
healthcheck sea `true`, que no comprueba nada. Es una comprobación que no mira
lo que a ti te importa: el mismo problema que viste en el Lab 02 de la sesión 1,
ahora en tu propia validación.

Míralo tú, que es lo que el comando no hace:

```bash
docker compose config | grep -A3 "healthcheck:"
docker compose config | grep -E "POSTGRES_|published"
```

Comprueba dos cosas concretas:

- El healthcheck ejecuta `pg_isready` contra la base y el usuario reales, no un
  comando que siempre sale bien ni una comprobación de que el proceso existe.
  Verás `$${POSTGRES_USER}` con doble `$`: es la forma correcta de escaparlo para
  que la variable la resuelva el contenedor y no Compose al leer el archivo.
- Las variables se interpolan con un valor. Si ves `POSTGRES_PASSWORD: ""`, tu
  `.env` no está o no tiene esa clave: `config -q` no te lo va a decir.

No hace falta levantar todavía la API dentro de Compose, pero **sí la base**.
Es la única forma de saber si arranca:

```bash
docker compose up -d --wait db
docker compose ps
```

`--wait` no devuelve el control hasta que el servicio esté `healthy`, así que no
te lo encuentras a medio arrancar. Si en su lugar el comando **falla o se
queda esperando**, la base no llega a estar sana: lee la causa antes de seguir.

```bash
docker compose logs db | tail -20
```

**El fallo más probable está en el volumen.** Las imágenes `postgres:18` y
posteriores guardan los datos en un subdirectorio por versión mayor y rechazan
arrancar si el volumen se monta directamente sobre `/var/lib/postgresql/data`,
que es lo que hacía la convención anterior y lo que un modelo entrenado con
ejemplos de PostgreSQL 16 tiende a escribir. El montaje correcto para esta
imagen es el directorio padre:

```yaml
volumes:
  - pgdata:/var/lib/postgresql
```

Es el ejemplo más claro de este lab: `docker compose config -q` da verde sobre
un archivo que **no puede arrancar**. La sintaxis era correcta; el valor no.

Cuando esté `healthy`, compruébalo contra la base real y déjala corriendo:

```bash
docker compose exec db psql -U curso -d curso -c "select version();"
```

### 5. Probar la ruta

Uvicorn se queda ocupando la terminal, así que hacen falta dos paneles. Divide
la terminal integrada con `Ctrl+Shift+5` y arranca el servidor en el primero:

```bash
uv run uvicorn app.main:app --port 8000
```

En el segundo panel:

```bash
curl -fsS http://127.0.0.1:8000/health
```

VS Code detecta el puerto 8000 y ofrece abrirlo en el navegador; para esta
comprobación basta con `curl`, que además deja la salida por escrito.

### 6. Confirmar

```bash
git add -A
git commit -m "Crea la base verificable de la API"
```

## Validación

- [ ] La instalación parte de `uv.lock`.
- [ ] La ruta de salud tiene un test, y `uv run pytest -q` lo ejecuta.
- [ ] Sabes por qué `pytest` encuentra `app` en tu proyecto: porque se instaló
      con `[build-system]`, o porque añadiste `pythonpath`.
- [ ] No hay credenciales en el diff.
- [ ] Los tres comandos del contrato pasan.
- [ ] Leíste el `docker compose config` renderizado: el healthcheck usa
      `pg_isready` y las variables tienen valor.
- [ ] Sabes decir qué **no** comprueba `docker compose config -q`.
- [ ] Levantaste la base y llegó a `healthy`. No basta con que el archivo
      valide: que arranque es una comprobación distinta.

## Limpieza

Detén Uvicorn con `Ctrl+C`. Detén la base cuando termines:

```bash
docker compose down
```

Sin `-v`, para conservar el volumen y los datos. Conserva el repositorio.

## Problemas Frecuentes

| Error | Causa | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'app'` al ejecutar `pytest` | Los tests están en `tests/` y `app` no se instaló ni está en la ruta de búsqueda | Añadir a `pyproject.toml`: `[tool.pytest.ini_options]` con `pythonpath = ["."]`, como en el paso 3 |
| `uv` elige otro Python | No se fijó `requires-python` | Pedir 3.12 y ejecutar `uv python pin 3.12` |
| Compose interpola una variable vacía | Falta valor por defecto o `.env` local | Copiar `.env.example` a `.env` y no confirmarlo. `config -q` **no** avisa: mira las advertencias y el `config` renderizado |
| `docker compose config -q` pasa pero el servicio no sirve | Solo valida sintaxis, no valores ni healthcheck | Inspeccionar `docker compose config` y comprobar `pg_isready` y las variables |
| El contenedor sale solo y el log habla de `pg_ctlcluster` y de datos en `/var/lib/postgresql/data` | El volumen se monta sobre el directorio de datos; `postgres:18` lo rechaza | Montar el volumen en `/var/lib/postgresql`, sin `/data`. Después `docker compose down -v` para descartar el volumen a medio crear |
| El estado se queda en `unhealthy` | El healthcheck no encuentra la base o el usuario | Comparar `POSTGRES_USER` y `POSTGRES_DB` del `.env` con los del `pg_isready` renderizado |
| El puerto 5432 está ocupado | PostgreSQL local | Usar otro puerto de host; no cambiar el puerto interno |
| El agente añade secretos de ejemplo reales | Criterio insuficiente | Sustituir por valores inequívocamente ficticios y revisar el diff |
