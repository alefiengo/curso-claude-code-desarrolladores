# Flujo de Trabajo con Git

El curso usa **GitHub Flow**, que es lo que hace la mayoría de equipos hoy. Una
sola regla:

> `main` siempre funciona. El trabajo va en una rama corta que se integra y se
> borra.

```text
main ────●────●────●────●────●───►   siempre en verde
          \  /      \  /
           ●         ●               una rama por sesión
```

Cada sesión arranca desde `main`, trabaja en su rama y la integra al terminar. La
sesión siguiente parte de ahí.

## Por Qué la Rama Corta Importa Más con un Agente

Trabajando solo, una rama es orden. Trabajando con un agente, es **una red de
seguridad**.

Un agente puede tomar una dirección equivocada y hacerlo con convicción: tocar
seis archivos, reescribir un test, cambiar una decisión que no le pediste. Si eso
pasa en una rama, la respuesta es una línea:

```bash
git switch main && git branch -D la-rama
```

Si pasa en `main`, la respuesta es una tarde.

## Qué Va en Rama y Qué No

| Tipo de cambio | Dónde se trabaja |
|---|---|
| Código de la API | Rama propia, integrada al cerrar la sesión |
| Memoria, skills, hooks, configuración | Directamente sobre `main` |
| Experimento que no se conserva | Rama que nunca se integra |

Crear un `CLAUDE.md` o un skill no necesita rama: no cambia el comportamiento de
la API y no hay nada que revisar contra una base.

## El Ciclo de una Sesión

**Al empezar**, comprueba que partes de un estado bueno:

```bash
git switch main
git status --short        # debe estar vacío
uv run pytest -q          # debe estar en verde
git log --oneline -3
```

Si `git status` no está vacío, decide qué hacer con eso **antes** de empezar: o
lo confirmas, o lo descartas. Arrancar sobre trabajo a medias es la forma más
común de perderlo.

**Durante**, en tu rama:

```bash
git switch -c feature/lo-que-toque
```

**Al cerrar**, integra:

```bash
uv run pytest -q
git switch main
git merge --no-ff feature/lo-que-toque -m "Integra <lo que aporta>"
git branch -d feature/lo-que-toque
```

`--no-ff` deja visible qué rama aportó cada cosa. `-d` en minúscula solo borra
ramas ya integradas: si se niega, es que el merge no llegó a hacerse.

## Commits

Un commit útil deja el repositorio en un estado verificable y cuenta **qué
decisión** se tomó, no qué archivos se tocaron —eso ya lo dice el diff.

Trabajando con un agente aparece un problema propio: te deja setenta líneas en un
solo cambio. Eso no se revisa. La sesión 10 construye un comando que propone cómo
partirlo; hasta entonces, se hace a mano y con criterio.

## Sin Tags

Un tag apunta a un commit fijo. En cuanto haces una corrección posterior, el tag
señala un estado que ya no es el bueno, y hay que borrarlo y recrearlo.

`main` no tiene ese problema: es una referencia móvil que absorbe correcciones
sin ceremonia. Por eso el curso no usa tags, y el punto de retorno es siempre el
mismo: **el último `main` en verde**.

## Recuperar sin Perder Trabajo

Cuando algo se tuerce:

1. **No borres todavía.** Guarda el intento en su rama y anota en tus evidencias
   qué pasó y por qué lo abandonas.
2. Vuelve a `main`, que está en verde.
3. Crea una rama nueva desde ahí.
4. Reproduce primero la comprobación que falta.
5. Aplica solo cambios que entiendas.

El curso **no usa `git reset --hard`** como receta de recuperación: descarta
trabajo sin dejar rastro. Se conserva lo que se intentó, aunque se abandone.

Dos cosas pueden salir mal, y las dos tienen respuesta en
[problemas frecuentes](../docs/problemas-frecuentes.md):

| Mensaje | Qué significa |
|---|---|
| `the branch ... is not fully merged` | Intentaste borrar una rama sin integrar. No fuerces con `-D`: integra |
| `CONFLICT (content)` | El mismo archivo cambió en las dos ramas. Se resuelve y se vuelve a probar |

## Si Faltas a una Sesión

El material de cada sesión es autocontenido: los laboratorios llevan el paso a
paso completo y el contrato dice qué debe cumplir el resultado. Puedes recuperar
una sesión entera trabajando sobre `main`, sin depender de nadie.

## Tu Repositorio es Tuyo

Desde la sesión 2 construyes `curso-claude-code-api` en tu propia cuenta de
GitHub o GitLab. Nadie más escribe en él.

Al terminar el curso contiene dos cosas: la API, y el directorio `.claude/` con
las herramientas que construiste —memoria, skills, hooks, subagente y
configuración de permisos—. La segunda es la que te llevas al trabajo.

## Contrato de Soporte

Al pedir ayuda incluye: sistema, versión de Claude Code, `git log --oneline -3`,
`git status --short`, el comando que falla y su salida completa sin secretos.
