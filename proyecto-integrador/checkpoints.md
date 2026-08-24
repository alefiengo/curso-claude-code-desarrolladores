# Checkpoints y Recuperación

## Ramas

Una sola regla, y el curso entero la sigue:

> El trabajo se hace en una rama. `main` recibe lo que está verificado. El tag se
> crea sobre `main`.

Con un matiz sobre qué merece rama propia:

| Tipo de cambio | Dónde se trabaja | Sesiones |
|---|---|---|
| Código de la API | Rama propia, integrada al cerrar | 3, 4-5, 7, 9 |
| Memoria, skill, subagente y configuración | Directamente sobre `main` | 2, 8, 10 |
| Experimento que no se conserva | Rama `experimento/*`, nunca integrada | 6, 8, 9 |

De ahí salen tres consecuencias que conviene tener presentes:

- **Cada tag existe en `main`.** Por eso `git switch -c rama <tag>` funciona en
  cualquier sesión posterior, y una sesión nunca arranca desde un estado que
  perdió el trabajo de la anterior.
- **Lo que está en rojo no se integra.** `s04-plan-v2` es el único checkpoint que
  se crea fuera de `main`: etiqueta un contrato en rojo a propósito. Queda
  alcanzable desde `main` cuando la sesión 5 pone v2 en verde e integra la rama.
- **Las ramas `experimento/*` no se integran nunca.** Son evidencia de una
  decisión, y se borran cuando ya registraste por qué se abandonaron.

El curso no usa `git reset --hard` ni reescribe historia publicada. Integrar es
`git merge --no-ff`, que deja visible qué rama aportó cada cosa.

## Tags

Los tags no son premios; son puntos de retorno. Créalo solo después de ejecutar
la validación indicada.

| Tag | Estado mínimo | Rama al crearlo | Verificación |
|---|---|---|---|
| `s02-base` | Health, uv, Compose, tests, lint y `CLAUDE.md` | `main` | Sesión 2 |
| `s03-v1` | Contrato v1 y migraciones desde cero | `main` | Sesión 3 |
| `s04-plan-v2` | Especificación, plan y tests rojos de v2 | `feature/fechas-limite` | Sesión 4 |
| `s05-v2` | Fechas límite implementadas y verdes | `main` | Sesión 5 |
| `s06-v2-recuperable` | Handoff y recuperación demostrados | `main` | Sesión 6 |
| `s07-verificado` | Regresión de títulos y página mínima | `main` | Sesión 7 |
| `s08-skill` | Skill evaluado en verde y fallos | `main` | Sesión 8 |
| `s09-control` | Permisos y Stop hook probados | `main` | Sesión 9 |
| `s10-final` | Revisor, ejecución acotada y evidencia final | `main` | Sesión 10 |

Comprueba en cualquier momento que la cadena está donde debe:

```bash
git branch --contains s07-verificado
```

Debe incluir `main`. Si no lo hace, etiquetaste sin integrar. Al terminar el
curso, los nueve tags son alcanzables desde `main`.

## Diagnóstico Antes de una Sesión

```bash
git status --short
git tag --list 's*'
uv sync --frozen
uv run pytest -q
uv run ruff check .
docker compose config -q
```

Si el checkpoint esperado no existe, no etiquetes un estado roto. Sigue el lab
faltante o crea una rama desde el último tag válido:

```bash
git switch -c recuperacion/siguiente-paso ULTIMO_TAG
```

## Recuperación sin Perder Trabajo

1. Conserva el intento actual en una rama y guarda `git diff` en evidencias.
2. Crea una rama nueva desde el último tag verde.
3. Reproduce primero el criterio que falta.
4. Aplica solo commits o cambios comprendidos.
5. Ejecuta la validación completa antes de crear el siguiente tag.

Integra siempre desde `main`, nunca al revés:

```bash
git switch main
git merge --no-ff <rama> -m "Integra <lo que aporta>"
```

Dos cosas pueden salir mal, y las dos tienen respuesta en
[problemas frecuentes](../docs/problemas-frecuentes.md):

| Mensaje | Qué significa |
|---|---|
| `the branch ... is not fully merged` | Intentaste borrar una rama sin integrar. No fuerces con `-D`: integra |
| `CONFLICT (content)` | El mismo archivo cambió en las dos ramas. Se resuelve y se vuelve a probar |

No se usa `git reset --hard` como receta de recuperación. Si falta una sesión
completa, el contrato y los labs permiten reconstruirla; el instructor mantiene
una referencia privada por checkpoint para diagnóstico, no para sustituir el
trabajo del estudiante.

## Contrato de Soporte

Al pedir ayuda incluye: sistema, versión de Claude Code, último tag válido,
`git status --short`, comando que falla y salida completa sin secretos.
