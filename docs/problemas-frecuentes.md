# Problemas Frecuentes

Consulta esta guía antes de pedir soporte.

## Docker

| Error | Causa | Solución |
|---|---|---|
| `Cannot connect to the Docker daemon` | Docker no está en ejecución | Iniciar Docker Desktop, o `sudo systemctl start docker` en Linux |
| `permission denied ... docker.sock` | Tu usuario no está en el grupo `docker` | `sudo usermod -aG docker $USER && newgrp docker` |
| `docker: command not found` en WSL | Docker Desktop sin integración WSL | Activar la integración en *Settings → Resources → WSL Integration* |
| `port is already allocated` | El puerto ya está ocupado por otro proceso | Cambiar el puerto del host en `compose.yaml`, por ejemplo `5433:5432` |
| `Bind for 0.0.0.0:5432 failed` | Hay un PostgreSQL local corriendo | Detenerlo, o mapear a otro puerto del host |

## uv y Python

| Error | Causa | Solución |
|---|---|---|
| `uv: command not found` | El instalador no está en el `PATH` | Cerrar y abrir la terminal, o recargar el shell |
| `No interpreter found` | Falta instalar la versión de Python | `uv python install 3.12` |
| Las dependencias no se ven | Se ejecutó fuera del entorno del proyecto | Usar `uv run <comando>` en lugar de invocar `python` directamente |

## Claude Code

| Error | Causa | Solución |
|---|---|---|
| `claude: command not found` | Instalación no completada o `PATH` sin recargar | Reabrir la terminal; comprobar con `claude --version` |
| Pide autenticación en cada sesión | El inicio de sesión no se guardó | Volver a ejecutar `claude` y completar el flujo en el navegador |
| Instalado en Windows y no lo ve WSL | Se instaló fuera de Ubuntu | Instalarlo dentro de Ubuntu |
| Comportamiento raro tras muchos turnos | Contexto degradado | `/clear` y reformular la tarea. Se trata en la sesión 3 |
| Un comando de los apuntes no existe | La versión instalada es distinta | `claude --help` y `/help` mandan sobre los apuntes |
| `-p` aborta al intentar una herramienta | En modo no interactivo no puede resolver una aprobación | Configurar `--allowedTools` o `dontAsk` con allowlist; consultar la sesión 10 |
| Auto mode no aparece | El plan, proveedor, modelo, versión o política no cumple sus requisitos | Usar **Ask before edits** (`default`) o `acceptEdits`; revisar `compatibilidad.md` |
| Un Stop hook repite el mismo fallo | La condición sigue roja o el script no tiene salida | Interrumpir, ejecutar el script fuera del hook y revisar timeout/diagnóstico |
| Docker falla dentro del sandbox | Docker necesita acceso que el sandbox no ofrece | Mantenerlo fuera solo con aprobación puntual; no abrir Bash globalmente |

## Git

| Error | Causa | Solución |
|---|---|---|
| `Author identity unknown` | Falta configurar nombre o correo | `git config --global user.name` y `user.email` |
| `Permission denied (publickey)` | Sin credenciales para el remoto | Configurar clave SSH o usar HTTPS con token |
| `error: the branch ... is not fully merged` | `git branch -d` protege trabajo sin integrar | No fuerces con `-D`. Integra primero: `git switch main && git merge --no-ff <rama>` |
| `CONFLICT (content): Merge conflict in ...` | El mismo archivo cambió en las dos ramas | Ver abajo: se resuelve, no se aborta por costumbre |
| `Your branch and 'origin/main' have diverged` | Se confirmó en los dos lados | No usar `reset --hard`. Comparar con `git log --oneline --graph main origin/main` y decidir |
| `fatal: refusing to merge unrelated histories` | Se creó el remoto con README y el local aparte | Crear el repositorio remoto **vacío**, o clonar y mover el trabajo |

### Cuando un merge entra en conflicto

En el camino del curso cada rama sale de un `main` limpio y verificado. Si aparece
un conflicto, suele significar que `main` cambió después de crear la rama o que
repetiste una sesión sobre historia distinta.

```bash
git status                 # qué archivos están en conflicto
git diff --name-only --diff-filter=U
```

Abre cada archivo, resuelve los marcadores `<<<<<<<`, `=======` y `>>>>>>>`, y
confirma:

```bash
git add <archivo>
git commit
uv run pytest -q
```

Ejecuta los tests **después** de resolver: un conflicto mal resuelto compila y
falla en comportamiento. Si prefieres volver atrás y entender el estado antes de
decidir, `git merge --abort` deja el repositorio exactamente como estaba.

No pidas a Claude que resuelva un conflicto sin leerlo tú: es justo el caso donde
una resolución plausible descarta trabajo real y los tests no lo notan.

## WSL

| Error | Causa | Solución |
|---|---|---|
| `WSL 2 requires an update` | Kernel de WSL desactualizado | `wsl --update` desde PowerShell |
| Los archivos van muy lentos | El proyecto está en `/mnt/c` | Trabajar en el sistema de archivos de Linux, dentro de `~` |
| La versión es WSL 1 | La distribución se creó con WSL 1 | `wsl --set-version Ubuntu-24.04 2` |
| Instalaste otra versión de Ubuntu | `wsl --install -d Ubuntu` usa el alias a la última LTS | `wsl --unregister <nombre>` y reinstalar con `Ubuntu-24.04` |

## Si nada de esto resuelve tu caso

Abre un issue en el repositorio con:

- Sistema operativo y versión.
- Comando exacto que ejecutaste.
- Salida completa del error.
- Salida de `claude doctor`, si el problema es de Claude Code.
