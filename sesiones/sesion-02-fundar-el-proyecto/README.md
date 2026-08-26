# Sesión 2: Fundar el Proyecto y su Memoria

## Objetivo

Crear una base reproducible para la API y escribir memoria de proyecto que aporte
decisiones, no información que Claude puede descubrir leyendo el repositorio.

**Sales con:** el `CLAUDE.md` de tu proyecto, podado hasta que cada línea se gane
el sitio. Es la primera pieza de tu `.claude/`, y la única que se carga en todas
las conversaciones a partir de hoy.

## Duración

2 horas.

Así se reparten los 120 minutos de la clase:

| Bloque | Minutos |
|---|---:|
| Repaso y contrato del proyecto | 15 |
| [Lab 01 — Base verificable](labs/01-base-verificable/README.md) | 45 |
| [Lab 02 — Memoria útil](labs/02-memoria-util/README.md) | 45 |
| Guardar evidencias y cierre | 15 |

Los dos laboratorios ocupan 90 de los 120 minutos. El Lab 02 trabaja sobre lo
que crea el Lab 01, así que van en orden.

## Materiales

- [Contrato del proyecto](../../proyecto-integrador/contrato-api.md)
- [Compatibilidad](../../docs/compatibilidad.md)
- [Referencia rápida](referencia-rapida.md)
- [Desafío opcional](tareas/desafio-opcional.md)

## Laboratorios

| Lab | Resultado | Qué descubres |
|---|---|---|
| [01 – Base verificable](labs/01-base-verificable/README.md) | FastAPI, uv, tests y Compose | Los tres comandos pueden dar verde sobre algo que no arranca |
| [02 – Memoria útil](labs/02-memoria-util/README.md) | `CLAUDE.md` breve y comprobado | Cuánto de lo que genera `/init` el repositorio ya lo dice |

## Al finalizar esta sesión podrás

- Dar al agente un contrato técnico sin dictar la implementación.
- Validar una base de proyecto desde una máquina limpia.
- Distinguir reglas duraderas de hechos que el código ya expresa.
- Inspeccionar qué memoria y configuración entran en contexto.
- Podar un `CLAUDE.md` generado antes de confirmarlo.

## Conceptos Clave

### Contrato antes que estructura

La estructura de carpetas puede cambiar; los invariantes no. En esta sesión los
invariantes son: una ruta de salud, comandos únicos para instalar y verificar,
secretos fuera de Git y un servicio PostgreSQL con healthcheck.

### Memoria de proyecto

`CLAUDE.md` se carga con frecuencia. Debe contener información cara de inferir:
comandos canónicos, límites, convenciones no obvias y errores conocidos. Una
lista del árbol o de dependencias repite lo que Claude puede leer.

### Jerarquía

Claude puede cargar memoria de usuario, organización, repositorio y directorios
anidados. Una regla cercana al archivo puede especializar una general. Antes de
añadir texto, decide su alcance y propietario.

Se cargan **todas**, concatenadas de la raíz del sistema hacia tu directorio de
trabajo: no se sustituyen entre ellas. Lo más cercano se lee al final.

### Hay dos memorias, y solo escribes una

| | `CLAUDE.md` | Auto memory |
|---|---|---|
| Quién lo escribe | Tú | Claude |
| Qué guarda | Instrucciones y reglas | Aprendizajes y correcciones tuyas |
| Dónde vive | En el repositorio | En tu máquina, fuera del proyecto |
| Viaja con el equipo | Sí, por Git | No |

**Auto memory está activa por omisión.** Cuando ves *"Saved 2 memories"* o
*"Recalled 2 memories"* en la interfaz, Claude está escribiendo o leyendo en
`~/.claude/projects/<proyecto>/memory/`. El índice de ese directorio,
`MEMORY.md`, se carga al principio de cada sesión igual que tu `CLAUDE.md`.

Esto importa para lo que vas a hacer hoy: puedes podar tu `CLAUDE.md` hasta
dejarlo perfecto y seguir teniendo instrucciones entrando por una puerta que no
has mirado. Se audita con `/memory`, y se apaga por proyecto con
`autoMemoryEnabled` si prefieres que la única memoria sea la que versionas.

### Ninguna de las dos obliga

`CLAUDE.md` no forma parte del prompt de sistema: se entrega como un mensaje de
usuario justo después. Claude lo lee y lo intenta seguir, pero no hay garantía de
cumplimiento estricto. Es exactamente la distinción que trabaja la sesión 9: una
instrucción persuade, un hook impide.

De ahí salen dos números útiles. Apunta a **menos de 200 líneas** por archivo:
más largo consume contexto y baja la adherencia. Y si crece, la respuesta no es
recortar a ciegas sino `.claude/rules/`, donde cada archivo cubre un tema y puede
declarar `paths:` para cargarse **solo** cuando Claude toca los archivos que le
corresponden.

## Comandos Nuevos

| Comando | Uso |
|---|---|
| `/init` | Generar una propuesta inicial de memoria |
| `/memory` | Ver y editar memorias cargadas |
| `/context` | Ver qué ocupa la ventana actual |
| `/config` | Consultar o ajustar configuración interactiva |

## Validación General

Desde `curso-claude-code-api`:

```bash
uv run pytest -q
uv run ruff check .
docker compose config -q
git status --short
```

- [ ] Tests y lint pasan.
- [ ] `compose.yaml` es válido.
- [ ] `.env` no está rastreado y `.env.example` sí.
- [ ] `CLAUDE.md` contiene decisiones comprobadas y no un inventario del repo.
- [ ] Sabes qué guarda tu auto memory, y decidiste si la dejas activa.
- [ ] Guardaste `evidencias/s02.md`.

## Cierre en Git

Esta sesión no toca el comportamiento de la API: crea el esqueleto y su memoria.
Eso se trabaja directamente sobre `main`, según el
[flujo de trabajo con Git](../../proyecto-integrador/flujo-git.md).

Comprueba que el trabajo quedó confirmado y que `main` está en verde:

```bash
git switch main
git status --short
uv run pytest -q
git log --oneline
```

`git status --short` debe estar vacío. Ese `main` en verde es el punto de partida
de la sesión 3.

## Limpieza

La API se conserva: es el proyecto integrador. Solo se detiene lo que quedó
levantado.

```bash
cd ~/curso-claude/curso-claude-code-api
docker compose down
docker compose ps
```

`docker compose ps` no debe listar servicios en ejecución. El volumen de datos se
conserva para la sesión 3.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) crea una memoria anidada solo
para `tests/` y comprueba cuándo se carga. No se entrega y no es requisito para
la sesión 3.

## Cierre

Checklist:

- [ ] `GET /health` responde 200 con `{"status":"ok"}`.
- [ ] Los tres comandos del contrato pasan desde una terminal limpia.
- [ ] `.env` está ignorado y `.env.example` versionado.
- [ ] Cada línea de mi `CLAUDE.md` es decisión, comando o riesgo.
- [ ] Sé qué memoria está cargada y cuánto contexto ocupa.

Preguntas de repaso:

- ¿Qué línea de tu `CLAUDE.md` no podría deducirse leyendo código?
- ¿Qué regla moverías a una memoria anidada si el proyecto creciera?
- ¿Cómo reconstruirías el entorno sin recordar comandos manuales?

## Versión

Material probado con **Claude Code 2.1.233**. Si un comando no existe o se
comporta distinto, `claude --help` y `/help` mandan sobre estos apuntes.

## Preparación para la Sesión 3

Comprueba que la base de datos arranca:

```bash
docker compose up -d db
docker compose ps
docker compose logs db --tail 5
```

El servicio `db` debe aparecer como `healthy`. Si no, resuélvelo antes de la
sesión 3: el esquema y las migraciones se construyen encima.

La sesión 3 diseña el esquema de la base y sus migraciones antes de escribir una
línea de código. Llega con `main` en verde y con la conversación de hoy cerrada:
lo que decidiste ya está en tu `CLAUDE.md`, no en un hilo abierto.
