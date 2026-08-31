# Referencia Rápida — Sesión 4

## Comandos de la Sesión

| Comando o control | Qué hace | Dónde lo usas |
|---|---|---|
| `/permissions` | Muestra qué tiene permitido la sesión y de qué archivo salen las reglas | Lab 02 y Lab 03 |
| `/rewind` | Vuelve a un punto anterior de la conversación, de los archivos, o de ambos | Lab 02, si la configuración queda mal |
| `Esc Esc` | Abre el mismo selector que `/rewind` | Igual |
| `/resume` | Retoma una conversación anterior de este directorio | Lab 02, si perdiste la lista del Lab 01 |
| `/diff` | Revisa los cambios de la sesión antes de confirmar | Entre cada incremento y su commit |
| `/context` | Muestra qué ocupa la ventana de contexto | Al cerrar cada lab |
| `Esc` | Interrumpe el turno en curso para redirigirlo | En cuanto veas una desviación |

`/rewind` **no es Git**. Deshace turnos y los cambios de archivo hechos en ellos;
no toca commits ya confirmados. Por eso confirmar cada incremento antes de
empezar el siguiente deja `/rewind` acotado al incremento en curso.

## Las Tres Listas de Permisos

Se escriben en `.claude/settings.json`, dentro de un bloque `permissions`:

| Lista | Para qué | Criterio |
|---|---|---|
| `allow` | Se ejecuta sin preguntar | Lo repites mucho, es reversible y no sale de tu máquina |
| `ask` | Pregunta siempre, una vez | Es normal hacerlo, pero tiene consecuencias fuera de tu equipo |
| `deny` | No se ejecuta nunca | No quieres poder hacerlo ni pidiéndolo tú |

**Se evalúan en ese orden: `deny`, `ask`, `allow`.** Gana la primera que coincida.
Un `deny` amplio bloquea aunque exista un `allow` más específico, así que una
lista de prohibiciones no admite excepciones.

## Patrones de Regla

| Forma | Cubre | No cubre |
|---|---|---|
| `Bash(uv run pytest *)` | `uv run pytest -q`, y también `uv run pytest` a secas | `pytest -q` sin `uv run` delante |
| `Bash(git commit *)` | Solo `git commit` | `git push`, `git branch -D` |
| `Bash(git *)` | **Todo** git: publicar y borrar ramas incluidos | — |
| `Read(./.env)` | Que las herramientas de archivo lean ese archivo | Que un comando de shell lo imprima |

Dos reglas de escritura que evitan casi todos los errores:

- **El asterisco va después del subcomando.** `Bash(git log *)` acota;
  `Bash(git * main)` no, y Claude Code avisa al arrancar cuando lo detecta.
- **El espacio antes del asterisco final es parte de la regla.** `Bash(ls *)`
  no cubre `lsof`; `Bash(ls*)` sí.

`Bash(ls:*)` es una forma equivalente de escribir `Bash(ls *)`. Los dos puntos
solo valen al final del patrón.

## Conventional Commits

Prefijo, dos puntos y una frase en imperativo:

| Prefijo | Para |
|---|---|
| `feat:` | Una capacidad nueva del producto |
| `fix:` | Una corrección de comportamiento |
| `test:` | Tests que no cambian el comportamiento |
| `chore:` | Dependencias, configuración, herramientas |
| `docs:` | Documentación y decisiones escritas |

## Git de Hoy

Todo lo ejecuta Claude. Esta tabla es para que reconozcas qué está pasando.

| Qué ocurre | Cuándo |
|---|---|
| Un commit por incremento, sin mezclar | Lab 01 |
| Un commit propio para la configuración | Lab 02 |
| `origin` apuntando a una dirección SSH | Lab 03 |
| `main` publicada **primero** | Lab 03: el primer push fija la rama por defecto |
| `feature/persistencia` publicada y sin integrar | Lab 03: la integración es trabajo de la sesión 5 |

## Si Algo Falla

| Señal | Causa habitual |
|---|---|
| El push se rechaza por historiales que no coinciden | El repositorio remoto no nació vacío |
| `Permission denied (publickey)` | Registraste la clave privada, o ninguna. La pública termina en `.pub` |
| `/permissions` no muestra tus reglas | La sesión arrancó antes de que el archivo existiera. Sal y vuelve a entrar |
| Te sigue preguntando por algo que pusiste en `allow` | El patrón no coincide con el comando exacto. `Bash(pytest *)` no cubre `uv run pytest` |
| Una migración falla por conexión | La base no está levantada o todavía no está sana |
