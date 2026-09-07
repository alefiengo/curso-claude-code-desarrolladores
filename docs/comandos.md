# Mapa Acumulativo de Comandos

Este mapa orienta. `claude --help` y `/help` mandan en la versión instalada.

Todo lo que aparece aquí se contrastó con dos fuentes: la instalación
(Claude Code 2.1.252) y la [documentación oficial](https://code.claude.com/docs).
Una sola no basta.

## Por Sesión

| Sesión | Se introduce | Para qué |
|---:|---|---|
| 1 | `claude`, `@ruta`, `Esc`, `Shift+Tab`, `/diff`, `/status`, `/context` | Dirigir una tarea y auditar su resultado |
| 2 | `/init`, `/memory`, `/context all` | Dar contexto de proyecto que cambia el resultado |
| 3 | `/clear`, `/compact`, `/btw`, `/autocompact` | Mantener señal en una conversación larga |
| 4 | `/permissions`, `/rewind`, `Esc Esc`, `/resume` | Ejecutar un plan con límites y poder deshacer |
| 5 | `/skills`, `/reload-skills`, `/plan`, `Ctrl+G` | Entregar un cambio e integrarlo con herramientas propias |
| 6 | `/branch`, `/fork` | Interrumpir y recuperar |
| 7 | `/rename`, `--continue` | Reproducir un fallo y demostrar su corrección |
| 8 | `/hooks`, `/agents`, `/list-agents`, `/subtask` | Convertir reglas en guardarraíles, y delegar con contexto aislado |
| 9 | `/mcp` | Evaluar y conectar sistemas externos |
| 10 | `/goal`, `/background`, `/tasks`, `claude -p`, `--output-format json`, `--json-schema` | Ejecutar sin nadie delante: construir el BFF |

## Etiquetas del Curso

- **Obligatorio:** se practica y aparece en una validación.
- **Opcional:** depende de plan, plataforma o versión.
- **Referencia:** se muestra para descubrimiento, no se memoriza.
- **Creado en el lab:** skill o comando propio, no incorporado a Claude Code.

Ninguna fila de las sesiones 8 a 10 está marcada como opcional todavía: el
diseño se decidió el 07/09/2026 y aún no se escribió ningún lab.

Las filas de la sesión 8 en adelante son **provisionales**: la sesión 7 ya
está escrita y verificada, con su propia sección **Comandos Nuevos**. Manda
siempre esa sección de cada sesión, que es la que se verifica contra la
instalación antes de publicarse.

No evalúes memorización de la tabla. Evalúa si la persona elige la herramienta
correcta para el riesgo y puede verificar su efecto.

## Cosas Que No Necesitan Comando

Parte de aprender la herramienta es saber qué no hay que hacer.

| Creencia frecuente | Qué ocurre de verdad |
|---|---|
| "Hay que recargar los skills tras editarlos" | Casi nunca. Claude Code vigila `~/.claude/skills/`, el `.claude/skills/` del proyecto y el de cada directorio añadido con `/add-dir`, y recoge los cambios dentro de la sesión. `/reload-skills` existe para el caso que el vigilante no cubre: un directorio de skills que **no existía** cuando arrancó la sesión |
| "Hay que reiniciar para probar un cambio en un `SKILL.md`" | Solo si creas un directorio de skills de primer nivel que no existía al arrancar la sesión |
| "Un plugin se recarga igual que un skill" | No. La detección en vivo cubre el texto de `SKILL.md`; los cambios en `hooks/`, `.mcp.json`, `agents/` y `output-styles/` de un plugin necesitan `/reload-plugins` |

## Fuera del Temario

Existen y son útiles, pero ningún lab depende de ellas. Se mencionan para que
sepas que están:

`/batch`, `/loop`, `/insights`, `/deep-research`, `/export`, `/teleport`,
`/doctor`, `/usage`, `/model`, `/fast`, worktrees, equipos de agentes,
integración con Chrome y Remote Control.

Consulta [Compatibilidad](compatibilidad.md) antes de dar por supuesta cualquiera
de ellas en tu plataforma o plan.
