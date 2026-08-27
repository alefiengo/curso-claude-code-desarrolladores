# Sesión 2: Contexto de Proyecto que Sí Aporta

Un repositorio puede explicar qué archivos tiene. No puede explicar por sí solo
qué decisiones tomó el equipo, qué fuente manda cuando dos documentos difieren
o qué atajo está prohibido aunque funcione.

En esta sesión fundas el proyecto integrador y construyes el contexto persistente
que Claude recibirá cada vez que trabaje en él.

## Objetivo

Dirigir a Claude para crear una línea base reproducible desde un contrato y
escribir un `CLAUDE.md` breve que reduzca errores reales de onboarding, sin
convertirlo en una copia del repositorio.

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — Fundar el proyecto desde un repositorio vacío](labs/01-base-verificable/README.md) | 55 |
| Conceptos retrospectivos: contexto persistente, alcance y garantía | 10 |
| [Lab 02 — Convertir decisiones en contexto de proyecto](labs/02-memoria-util/README.md) | 45 |
| Evidencia y cierre | 10 |

## Materiales

- [Contrato del proyecto](../../proyecto-integrador/contrato-api.md)
- [Seguridad](../../docs/seguridad.md)
- [Referencia rápida](referencia-rapida.md)
- [Desafío opcional](tareas/desafio-opcional.md)

## Laboratorios

| Lab | Situación profesional | Qué descubres |
|---|---|---|
| [01 — Inicializar un proyecto bajo contrato](labs/01-base-verificable/README.md) | Debes delegar la creación de un servicio nuevo sin aceptar alcance ni éxito por declaración | Un prompt de tarea dirige la generación; Git y las comprobaciones automáticas deciden si se acepta |
| [02 — Convertir decisiones en contexto de proyecto](labs/02-memoria-util/README.md) | Una propuesta rápida contradice cuatro reglas del proyecto | Un `CLAUDE.md` útil dirige la revisión; no garantiza que el agente obedezca |

## Arranque: Un Repositorio sin Código

No leas todavía los conceptos. Abre el Lab 01 y llega hasta la primera ejecución
de las tres verificaciones obligatorias:

```bash
code $CURSO/sesiones/sesion-02-fundar-el-proyecto/labs/01-base-verificable/README.md
```

En los primeros diez minutos debes haber comprobado que el repositorio solo
contiene el contrato y `.gitignore`, y debes tener un primer borrador propio del
encargo. Completa el lab y vuelve después a esta página: la explicación sobre
contexto parte de lo que Claude pudo y no pudo descubrir durante la generación.

## Al finalizar esta sesión podrás

- Separar hechos descubribles de decisiones que el equipo debe declarar.
- Dirigir la inicialización de un proyecto vacío con alcance y criterios
  comprobables.
- Auditar archivos nuevos y límites negativos antes del primer commit.
- Elegir qué pertenece al `CLAUDE.md` raíz y qué necesita otro alcance.
- Usar `/init` como borrador y auditarlo antes de conservarlo.
- Comprobar con `/context` qué instrucciones se cargaron y usar `/memory` para
  inspeccionar sus fuentes y la memoria automática.
- Probar el contexto con un caso diseñado para contradecirlo.
- Distinguir contexto, documentación y garantías técnicas: límites que se
  cumplen aunque el modelo decida otra cosa, porque los aplica un permiso o un
  hook configurado para bloquear.
- Dejar `main` en un estado reproducible para las sesiones siguientes.

## Conceptos Clave

### El contexto ya existe antes de tu primer mensaje

Una sesión no empieza vacía. Claude Code carga instrucciones del sistema,
información del entorno, memoria de proyecto, memoria automática y definiciones
de herramientas. Después se suman la conversación, los archivos que lee y las
salidas de comandos.

`/context` muestra qué ocupa la ventana actual. `/memory` enumera los archivos
de instrucciones cargados y permite abrirlos, además de inspeccionar la memoria
automática. Responden preguntas distintas:

| Pregunta | Herramienta |
|---|---|
| ¿Qué ocupa contexto ahora? | `/context` |
| ¿Qué instrucciones se cargaron y qué auto memory puedo inspeccionar? | `/memory` |

Usa `/memory` para identificar y abrir las fuentes cargadas. Usa **Memory files**
dentro de `/context` para ver además cuánto contexto ocupan. Si difieren, registra
la versión y reinicia desde la raíz antes de diagnosticar la configuración.

La consecuencia profesional no es "usar pocos tokens". Es mantener alta la
proporción entre señal y ruido: cada instrucción cargada siempre debe justificar
la atención que compite con la tarea actual.

### Repositorio, documentación e instrucciones no son lo mismo

| Lugar | Para qué sirve | Ejemplo |
|---|---|---|
| Código y configuración | Estado ejecutable del proyecto | Dependencias, rutas, versión de Python |
| Documentación | Explicación detallada y fuentes de verdad | Contrato de la API, decisiones de arquitectura |
| `CLAUDE.md` | Orientación breve que debe estar disponible en cada sesión | Comando canónico, fuente que manda, límite no obvio |

Una lista de dependencias no pertenece a `CLAUDE.md`: `pyproject.toml` ya la
responde. Un tutorial de instalación tampoco: vive mejor en el README.

El prompt que crea la base tampoco debe copiarse entero a `CLAUDE.md`. "En esta
entrega implementa solo `/health`" es alcance temporal; "el contrato de
comportamiento vive en `docs/contrato-api.md`" sí puede seguir siendo útil en
cualquier tarea. La diferencia no es el formato, sino cuánto dura la decisión.

Los comandos canónicos sí pueden merecer una línea aunque también aparezcan en
el README. Se usan en casi todas las tareas, una variante incorrecta puede dar
un resultado distinto y el coste de redescubrirlos se repite. La regla correcta
no es "si está en el repositorio, bórralo"; es esta:

> Conserva lo que Claude debe tener presente con frecuencia y cuyo
> redescubrimiento cuesta tiempo o introduce riesgo.

### Qué merece contexto persistente

Un `CLAUDE.md` de proyecto suele ganar su lugar con cuatro tipos de información:

| Tipo | Ejemplo del curso |
|---|---|
| Fuente de verdad | El comportamiento vive en `docs/contrato-api.md` |
| Comando canónico | `uv run pytest -q` ejecuta la suite del entorno bloqueado |
| Restricción no obvia | Las pruebas de persistencia usan PostgreSQL, no SQLite |
| Límite de trabajo | No abrir, mostrar, editar ni confirmar `.env` |

No lo llenes con frases genéricas como "escribe código limpio", estados
temporales como "hoy solo existe `/health`" ni recorridos multi-paso que solo se
usan en una tarea concreta.

### Elegir el alcance correcto

Antes de escribir una regla, decide cuándo debe cargar y quién la comparte:

| Necesidad | Lugar adecuado |
|---|---|
| Aplica a cualquier tarea del repositorio | `CLAUDE.md` raíz |
| Solo aplica cuando se trabaja en ciertas rutas | `.claude/rules/` con `paths:` |
| Es personal y no debe viajar con el equipo | `CLAUDE.local.md` ignorado |
| Es un procedimiento bajo demanda | Skill, que se trabaja en la sesión 8 |
| Debe cumplirse aunque el modelo decida otra cosa | Permiso o hook, sesión 9 |

Dividir un archivo mediante imports mejora organización, pero no reduce contexto:
lo importado también se carga. Para reducir carga necesitas alcance condicional
o contenido bajo demanda.

### `/init` propone; el equipo decide

`/init` explora el repositorio y genera una base. Puede encontrar comandos,
estructura y patrones. No conoce acuerdos que nunca se escribieron, y puede
convertir hechos temporales o detalles obvios en instrucciones permanentes.

Trata su salida como cualquier otro cambio generado:

1. revisa cada línea;
2. exige una fuente o un riesgo concreto;
3. mueve lo que tenga otro alcance;
4. elimina lo genérico, duplicado o temporal;
5. prueba el resultado con una tarea adversa.

### Una instrucción no es una garantía

`CLAUDE.md` entra como contexto que el modelo intenta seguir. No es una política
de seguridad. Una instrucción vaga, contradictoria o perdida entre ruido puede
ignorarse.

En el Lab 02 usarás una propuesta que pide SQLite, editar tests, leer `.env` y
cerrar con una comprobación incompleta. El resultado sirve para evaluar si el
contexto orienta bien la revisión. Si Claude omite un conflicto, no "falló el
curso": encontraste el límite de una instrucción. Los límites que no admiten
excepciones se convierten en permisos o hooks más adelante.

## Comandos Nuevos

| Comando | Uso |
|---|---|
| `/init` | Generar o mejorar una propuesta de instrucciones de proyecto |
| `/context` | Ver la distribución del contexto y los archivos cargados |
| `/memory` | Inspeccionar instrucciones y memoria automática |

## Validación General

Desde `~/curso-claude/curso-claude-code-api`:

```bash
uv sync --locked
uv run pytest -q
uv run ruff check .
docker compose config -q
git check-ignore .env
git status --short
```

La sesión está completa si:

- [ ] Claude creó la base desde el contrato, sin recibir una solución preconstruida.
- [ ] El plan se aprobó antes de editar y el diff respetó el alcance permitido.
- [ ] El `uv.lock` generado coincide con el proyecto y pasan tests y lint.
- [ ] PostgreSQL llegó a estado `healthy` al menos una vez.
- [ ] `CLAUDE.md` declara fuentes, comandos y límites relevantes para cualquier tarea.
- [ ] No contiene inventario, tutorial, estado temporal ni consejo genérico.
- [ ] `/context` confirma que el archivo está cargado.
- [ ] La revisión de la propuesta detectó sus cuatro incompatibilidades, o registraste cuál omitió Claude.
- [ ] `.env` está ignorado y no aparece en el historial.
- [ ] Guardaste `evidencias/s02.md` y `main` está limpio.

## Limpieza

Conserva la API y su historial. Detén los procesos locales:

```bash
docker compose down
docker compose ps
```

No uses `-v`: el volumen se reutiliza en la sesión 3.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) mueve convenciones de tests a
una regla con alcance por ruta y comprueba cuándo entra en contexto.

## Cierre

Guarda `evidencias/s02.md`:

```markdown
# Sesión 2

## Descubrible en el repositorio
Un hecho que Claude encontró sin memoria y su fuente.

## Primera delegación
Una decisión del plan que aprobaste o corregiste y qué prueba usaste.

## Decisión que necesitaba el equipo
Una regla que no podía inferirse con seguridad.

## Línea eliminada de /init
Qué quitaste y por qué no merecía carga permanente.

## Prueba del contexto
Qué conflictos encontró Claude en la propuesta y cuál omitió, si hubo uno.

## Límite
Qué parte requiere una garantía técnica y no solo una instrucción.
```

Preguntas de repaso:

- ¿Qué dato útil dejaste fuera de `CLAUDE.md` porque ya tenía un lugar mejor?
- ¿Qué decisión no podía deducirse del código?
- ¿Qué información aporta `/memory` y qué información adicional aporta `/context`?
- ¿Qué regla de tu archivo debería convertirse en garantía técnica si el riesgo aumenta?

## Versión

Material revisado el **27 de agosto de 2026** con Claude Code **2.1.247** y la
documentación oficial de memoria y contexto. Comprueba tu versión con
`claude --version` y la disponibilidad local con `/help`.

- [Memoria de proyecto](https://code.claude.com/docs/en/memory)
- [Depurar configuración](https://code.claude.com/docs/en/debug-your-config)
- [Ventana de contexto](https://code.claude.com/docs/en/context-window)

## Preparación para la Sesión 3

Llega con el proyecto limpio y la base disponible:

```bash
git switch main
git status --short
uv run pytest -q
docker compose up -d --wait db
docker compose ps
```

La sesión 3 implementa la v1 y observa cómo cambia el contexto durante una tarea
larga. Cierra la conversación de hoy: las decisiones duraderas ya están en el
repositorio.
