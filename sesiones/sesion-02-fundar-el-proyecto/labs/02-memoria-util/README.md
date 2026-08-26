# Lab 02: Memoria Útil

## Objetivo

Generar, auditar y podar `CLAUDE.md` hasta que solo queden instrucciones con
valor duradero.

## Por qué este lab

`CLAUDE.md` se carga entero en cada conversación, hable de lo que hable. Cada
línea ocupa espacio que le quita a la tarea, y cuanto más largo es el archivo,
menos caso le hace Claude a las reglas que sí importan.

`/init` te va a generar un borrador con bastante material que el propio
repositorio ya dice. Tu trabajo es recortarlo hasta que cada línea se gane el
sitio: lo que queda son decisiones, comandos y avisos que Claude no puede
deducir leyendo el código.

## Requisitos

- Lab 01 completado: la base de la API existe y sus tres comandos pasan.
- Estar dentro de `~/curso-claude/curso-claude-code-api`.
- Repositorio sin cambios pendientes (`git status --short` vacío).

## Paso a Paso

### 1. Medir el contexto inicial

Dentro de Claude Code:

```text
/context
/init
```

No confirmes el resultado sin leerlo. Guarda una copia del primer borrador:

```bash
cp CLAUDE.md evidencias/claude-md-inicial.md
```

### 2. Clasificar cada sección

Marca cada bloque con una categoría temporal:

- `D`: decisión o convención no deducible.
- `C`: comando canónico que debe ejecutarse exactamente así.
- `R`: riesgo o error recurrente.
- `O`: obvio al leer el repositorio.
- `T`: dato temporal que se volverá falso.

Pide ayuda, pero exige justificación:

```text
Audita CLAUDE.md. Para cada sección indica D, C, R, O o T y cita el archivo que
permitiría deducir cualquier elemento marcado O. No edites todavía.
```

### 3. Podar

Conserva solo D, C y R. El archivo debe incluir:

- Comandos de instalación, test, lint y ejecución.
- Regla de no modificar tests existentes para hacer pasar una feature.
- Regla de no leer ni confirmar `.env`.
- Convención de migraciones que se aplicará desde la sesión 3.
- La razón de cualquier decisión no estándar.

El techo recomendado es 200 líneas, y está explicado en los conceptos de la
sesión. Aquí trabaja un umbral más exigente: este proyecto acaba de nacer y
todavía no tiene convenciones que defender, así que si tu archivo supera **80
líneas** exige que cada sección justifique su coste permanente. No es otro
límite: es la señal de que estás documentando el repositorio en vez de decidir
sobre él.

### 4. Comprobar la memoria efectiva

```text
/memory
/context
```

Pregunta a Claude cuáles son los comandos canónicos y contrástalos con README y
`pyproject.toml`. Corrige cualquier discrepancia en su fuente propietaria.

Los dos comandos no dicen lo mismo, y la diferencia importa. `/memory` lista
**ubicaciones**: te enseña dónde pueden vivir los archivos de memoria, incluidas
rutas que todavía no existen, y te deja abrirlas. `/context` lista bajo **Memory
files** lo que de verdad **se cargó** en esta sesión.

Si tu archivo aparece en `/memory` pero no en `/context`, Claude no lo está
viendo, y ninguna poda lo va a arreglar.

Ahora mira la otra puerta. En `/memory`, abre la carpeta de auto memory:

```text
/memory
```

Ahí está lo que Claude ha decidido recordar por su cuenta —tus preferencias, las
correcciones que le has dado— en archivos de texto que puedes leer y borrar. No
lo has escrito tú y no está en el repositorio, pero su índice entra en contexto
en cada sesión igual que tu `CLAUDE.md`.

Anota en `evidencias/s02.md` qué encontraste y decide una cosa: dejarlo activo
sabiendo que existe, o apagarlo para este proyecto y que la única memoria sea la
que versionas. Las dos respuestas valen; lo que no vale es no saber que estaba.

### 5. Guardar evidencia

```bash
git diff --stat
git diff -- CLAUDE.md
git add CLAUDE.md
git commit -m "Define la memoria operativa del proyecto"
```

En `evidencias/s02.md`, incluye una línea eliminada y explica por qué sobraba.

## Validación

- [ ] Cada regla del archivo es decisión, comando o riesgo.
- [ ] Los comandos coinciden con el repositorio.
- [ ] No contiene secretos, árbol de carpetas ni lista de dependencias.
- [ ] Puedes explicar qué alcance tendrá una memoria anidada.

## Limpieza

No elimines nada. `CLAUDE.md` y `evidencias/` forman parte del proyecto
integrador y se usan en todas las sesiones siguientes.

Comprueba que el trabajo quedó confirmado:

```bash
git status --short
git log --oneline -2
```

## Problemas Frecuentes

| Problema | Causa | Solución |
|---|---|---|
| `/init` no cambia nada | Ya existe un `CLAUDE.md` y no lo sobrescribe | Pedir una auditoría explícita del archivo actual |
| La propuesta borra una decisión real | Parecía deducible del repositorio, y no lo era | Restaurarla y documentar por qué no se deduce |
| `/memory` muestra otra regla | Viene de un alcance distinto (usuario u organización) | Identificar su alcance antes de duplicarla o contradecirla |
| `/context` no muestra el `CLAUDE.md` | El archivo se creó después de abrir la sesión | Salir y volver a abrir `claude`; la memoria se carga al inicio |
| Claude ignora una regla del archivo | El archivo es demasiado largo y la regla se pierde | Es el fallo que trabaja el lab: podar y volver a comprobar |
| La poda deja el archivo casi vacío | Casi todo era deducible del repositorio | No es un error. Un `CLAUDE.md` corto y cierto vale más que uno largo |
