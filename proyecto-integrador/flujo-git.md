# Flujo de Trabajo con Git

El curso usa **GitHub Flow**, que es lo que hace la mayoría de equipos hoy. Una
sola regla:

> `main` siempre funciona. El trabajo va en una rama corta que se integra y se
> borra.

```text
                    sesión 3 en adelante
                   ┌──────────────────────┐
main ────●────●────●────●────●────●────●───►   siempre en verde
                    \  /      \  /
                     ●         ●               una rama por cambio
```

**La sesión 2 confirma directamente en `main`.** Fundas el proyecto, no hay nada
que revisar contra una base anterior y el historial queda lineal.

**Desde la sesión 3** cada cambio arranca en su propia rama desde `main`, se
revisa y se integra al terminar. La sesión siguiente parte de ahí. Ese es el
flujo que usa el resto del curso.

## Por Qué la Rama Corta Importa Más con un Agente

Trabajando solo, una rama es orden. Trabajando con un agente, es **una red de
seguridad**.

Un agente puede tomar una dirección equivocada y hacerlo con convicción: tocar
seis archivos, reescribir un test, cambiar una decisión que no le pediste. Si eso
pasa en una rama, puedes conservar el intento y volver a una base limpia:

```bash
git status --short        # debe quedar vacío tras conservar el intento seguro
git switch main
git branch -m la-rama intento/la-rama-desviada
```

La rama renombrada conserva la evidencia y no contamina `main`. Crea después una
rama nueva desde la base verde.

## Qué Va en Rama y Qué No

Desde la sesión 3:

| Tipo de cambio | Dónde se trabaja |
|---|---|
| Código de la API | Rama propia, integrada al cerrar la sesión |
| Memoria, skills, hooks y configuración compartida | La misma rama revisable de la sesión |
| Experimento que no se conserva | Rama que nunca se integra |

Un `CLAUDE.md`, un skill o un hook también cambia la forma de trabajar del equipo.
Se revisa en rama aunque no cambie una respuesta HTTP.

La fundación de la sesión 2 es la excepción: no hay base previa contra la que
revisarla, así que se confirma en `main`.

## El Ciclo de una Sesión, de la 3 en Adelante

Los comandos de esta sección explican **qué ocurre**, no qué tecleas. Desde la
sesión 4 se los pides a Claude y compruebas lo que informa; lo único que sigues
escribiendo tú son los comandos de la propia herramienta.

**Al empezar**, comprueba que partes de un estado bueno:

```bash
git switch main
git status --short        # debe estar vacío
uv run pytest -q          # debe estar en verde
git log --oneline -3
```

Si `git status` no está vacío, decide qué hacer con eso **antes** de empezar:
confírmalo en su rama o consérvalo en una rama identificable. Arrancar sobre
trabajo a medias sin saber qué contiene es la forma más común de perderlo.

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

Si trabajas con un remoto propio, ese mismo cierre puede hacerse con una pull
request o merge request en lugar del merge local: empujas la rama, abres la
solicitud contra `main` y la integras cuando las comprobaciones estén en verde.
El criterio no cambia; cambia dónde queda registrada la revisión.

## Commits

Un commit útil deja el repositorio en un estado verificable y cuenta **qué
decisión** se tomó, no qué archivos se tocaron —eso ya lo dice el diff.

Trabajando con un agente aparece un problema propio: te deja setenta líneas en un
solo cambio. Eso no se revisa. En la sesión 5 conviertes ese reparto en una
herramienta tuya que propone cómo partirlo; hasta entonces, se hace a mano y con
criterio.

## Recuperar sin Perder Trabajo

Cuando algo se tuerce:

1. **No borres todavía.** Guarda el intento en su rama y deja escrito en el
   mensaje del último commit qué pasó y por qué lo abandonas.
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

Desde la sesión 2 construyes `curso-claude-code-api` en un repositorio local
tuyo. En la **sesión 4 lo publicas**, así que necesitas una cuenta de GitHub o
de GitLab. Cualquiera de las dos sirve, y el repositorio que crees es privado y
tuyo.

El laboratorio de esa sesión lo lleva paso a paso: crear el repositorio remoto
vacío, conectarlo y empujar las ramas, sin pegar tokens en la terminal ni en la
conversación. En esencia son tres órdenes:

```bash
git remote add origin <URL_DEL_REPOSITORIO_VACIO>
git push -u origin main
git remote -v
```

Si el remoto ya contiene commits, no fuerces el push. Compara ambos historiales
y decide cómo integrarlos antes de continuar.

Al terminar el curso contiene dos cosas: la API generada bajo tu dirección y el
directorio `.claude/` con las herramientas que construiste —memoria, skills,
hooks, subagente y configuración de permisos—. La segunda es la que te llevas al
trabajo.

## Contrato de Soporte

Al pedir ayuda incluye: sistema, versión de Claude Code, `git log --oneline -3`,
`git status --short`, el comando que falla y su salida completa sin secretos.
