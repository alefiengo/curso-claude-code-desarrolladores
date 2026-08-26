# Mapa Acumulativo de Comandos

Este mapa orienta. `claude --help` y `/help` mandan en la versión instalada.

| Momento | Comandos o controles | Sesión |
|---|---|---:|
| Abrir y diagnosticar | `claude`, `claude -p`, `claude doctor`, `/help`, `/status` | 1 |
| Revisar cambios y modelo | `/diff`, `/model` | 1 |
| Memoria y contexto | `/init`, `/memory`, `/context`, `/config`, `/clear`, `/compact`, `@ruta` | 2 |
| Plan y objetivo | `/plan`, `Shift+Tab`, `Ctrl+G`, `/goal` | 3 |
| Skills propios | `/skills`, `/reload-skills` | 4 |
| Extensiones y diagnóstico | `/plugin`, `/doctor` | 5 |
| Hooks | `/hooks` | 6 |
| Integraciones externas | `/mcp`, `claude mcp add`, `claude mcp list` | 7 |
| Depuración y revisión | `/review`, imágenes, `/rewind` | 8 |
| Delegación | `/agents`, `/fork`, `/subtask` | 9 |
| Control y automatización | `/permissions`, `/sandbox`, `/usage`, `claude -p --output-format json` | 10 |
| Recuperación (transversal) | `Esc`, `Esc Esc`, `/rewind`, `/resume`, `--continue`, `/export` | 2-10 |

## Etiquetas del Curso

- **Obligatorio:** se practica y aparece en una validación.
- **Opcional:** depende de plan, plataforma o versión.
- **Referencia:** se muestra para descubrimiento, no se memoriza.
- **Creado en el lab:** skill o comando propio, no incorporado a Claude Code.

No evalúes memorización de la tabla. Evalúa si la persona elige la herramienta
correcta para el riesgo y puede verificar su efecto.
