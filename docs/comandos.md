# Mapa Acumulativo de Comandos

Este mapa orienta. `claude --help` y `/help` mandan en la versión instalada.

| Momento | Comandos o controles | Sesión |
|---|---|---:|
| Abrir y diagnosticar | `claude`, `claude -p`, `claude doctor`, `/help`, `/status` | 1 |
| Revisar cambios y modelo | `/diff`, `/model` | 1 |
| Memoria y configuración | `/init`, `/memory`, `/context`, `/config` | 2 |
| Gestionar conversación | `/clear`, `/compact`, `/autocompact`, `/btw`, `@ruta` | 3 |
| Plan y objetivo | `/plan`, `Shift+Tab`, `Ctrl+G`, `/goal`, `/effort`, `/advisor`, `/cost` | 4 |
| Directorios e integración | `/add-dir`, `/cd`, `/install-github-app` | 5 |
| Recuperación | `Esc`, `Esc Esc`, `/rewind`, `/branch`, `/resume`, `--continue`, `/recap`, `/export`, `/copy` | 6 |
| Revisión | `/code-review`, imágenes | 7 |
| Extensiones | `/skills`, `/reload-skills`, `/plugin`, `/doctor` | 8 |
| Control | `/permissions`, `/hooks`, `/sandbox` | 9 |
| Delegación e integración | `/subtask`, `/fork`, `/mcp`, `/insights`, `/team-onboarding` | 10 |
| Automatización | `claude -p --output-format json --permission-mode dontAsk --allowedTools ...` | 10 |

## Etiquetas del Curso

- **Obligatorio:** se practica y aparece en una validación.
- **Opcional:** depende de plan, plataforma o versión.
- **Referencia:** se muestra para descubrimiento, no se memoriza.
- **Creado en el lab:** skill o comando propio, no incorporado a Claude Code.

No evalúes memorización de la tabla. Evalúa si la persona elige la herramienta
correcta para el riesgo y puede verificar su efecto.
