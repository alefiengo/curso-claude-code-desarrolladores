# Instalación del Entorno

Prepara esto **antes de la primera sesión**. Resolverlo en clase consume el tiempo de práctica.

Al terminar debes poder ejecutar los cinco comandos de la [verificación final](#verificación-final).

## Resumen por sistema

| Sistema | Editor | Dónde corre la terminal | Docker | Python |
|---|---|---|---|---|
| Linux | VS Code | La del sistema | Docker Engine | uv |
| Windows | VS Code + Remote-WSL | Ubuntu, dentro de WSL 2 | Docker Engine en WSL, o Docker Desktop | uv dentro de WSL |
| macOS | VS Code | La del sistema | Docker Desktop | uv |

**El curso usa VS Code como entorno único.** No es una preferencia estética: con
veinticinco personas en una clase en vivo, que todos vean la misma pantalla
convierte "no me funciona" en algo diagnosticable. Todo lo que hagas cabe en una
ventana: el editor, la terminal integrada donde corre Claude Code, y el panel de
Git para revisar diffs.

Los comandos del curso se ejecutan siempre desde una terminal Linux, macOS o WSL.
Nunca desde PowerShell ni CMD. En Windows, la terminal integrada de VS Code
**ya está** dentro de Ubuntu cuando abres la carpeta con Remote-WSL: es la forma
más fiable de cumplir esa regla, porque no tienes que acordarte de nada.

---

## 1. VS Code

Instálalo desde [code.visualstudio.com](https://code.visualstudio.com/), que
detecta tu sistema y ofrece el paquete correcto.

En **macOS**, además, hay que habilitar el comando `code` a mano: abre VS Code,
pulsa `Cmd+Shift+P`, escribe `Shell Command: Install 'code' command in PATH` y
acéptalo. Los laboratorios usan `code archivo.py` para abrir archivos, así que
sin ese paso el comando no existe.

Extensiones necesarias, y solo estas dos:

| Extensión | Identificador | Para qué |
|---|---|---|
| Python | `ms-python.python` | Resaltado, ejecución de tests y entorno virtual |
| WSL | `ms-vscode-remote.remote-wsl` | **Solo Windows.** Abre el proyecto dentro de Ubuntu |

Se instalan desde el panel de extensiones (`Ctrl+Shift+X`) buscando por
identificador. Cuantas menos extensiones, menos cosas pueden fallar el primer día.

Docker tiene extensión oficial y es cómoda, pero el curso no la necesita: todo lo
que se hace con contenedores se hace con `docker compose` desde la terminal.

### Comprobar que abre en el sitio correcto

En Linux y macOS no hay nada que comprobar. En Windows, después de instalar WSL
en el paso siguiente, la barra inferior izquierda de VS Code debe decir
**`WSL: Ubuntu-24.04`**. Si no lo dice, estás editando desde Windows y los
comandos del curso fallarán.

---

## 2. Terminal

### Linux y macOS

No hay nada que preparar.

### Windows: WSL 2 con Ubuntu 24.04

Desde PowerShell como administrador:

```powershell
wsl --install -d Ubuntu-24.04
```

Usa el nombre con versión. `Ubuntu` a secas es un alias a la última LTS, y el curso necesita que todos trabajen sobre la misma.

Para ver los nombres disponibles:

```powershell
wsl --list --online
```

Reinicia cuando lo pida. Al arrancar Ubuntu por primera vez, crea tu usuario y contraseña.

Comprueba la versión:

```powershell
wsl -l -v
```

La columna `VERSION` debe decir `2`. Si dice `1`:

```powershell
wsl --set-version Ubuntu-24.04 2
```

A partir de aquí, **todo el curso ocurre dentro de Ubuntu**.

### Abrir el proyecto desde VS Code

Desde la terminal de Ubuntu, en la carpeta que quieras abrir:

```bash
code .
```

La primera vez que lo ejecutes, VS Code instala su servidor dentro de Ubuntu y
tarda unos segundos. Cuando abra, comprueba la barra inferior izquierda: debe
decir `WSL: Ubuntu-24.04`.

Alternativa sin terminal: en VS Code, `Ctrl+Shift+P` → *WSL: Connect to WSL*.

A partir de ese momento la terminal integrada (`Ctrl+ñ`, o *Terminal → Nuevo
terminal*) es una terminal de Ubuntu. Ahí es donde corre todo el curso.

---

## 3. Docker

### Linux: Docker Engine

Instala Docker Engine siguiendo la [documentación oficial](https://docs.docker.com/engine/install/) para tu distribución.

Después, añade tu usuario al grupo `docker` para no depender de `sudo`:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### Windows: Engine dentro de WSL, o Docker Desktop

Dos opciones según el equipo:

| Opción | Cuándo | Cómo |
|---|---|---|
| Docker Engine dentro de WSL | Equipos con poca RAM, o si prefieres no instalar software en Windows | Igual que en Linux, desde la terminal de Ubuntu |
| Docker Desktop | Equipos holgados, o si ya lo usas | Instalar en Windows y activar la integración con WSL en *Settings → Resources → WSL Integration* |

Con Docker Desktop, los comandos `docker` funcionan desde Ubuntu si la integración está activada.

### macOS

Instala [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/). Es la vía soportada en macOS.

### Comprobar Docker

```bash
docker run --rm hello-world
```

Descarga previa de la imagen de PostgreSQL que se usa desde la sesión 2:

```bash
docker pull postgres:18-alpine
```

Hazlo con tiempo: descargarla en clase consume varios minutos.

### Descarga previa del repositorio del Lab 03

El Lab 03 de la sesión 1 trabaja sobre `click`, un proyecto que no has leído
antes. Clónalo ahora y guárdalo aparte, para no depender de la red ese día:

```bash
mkdir -p ~/curso-claude/material-lab-03
git clone --branch 8.1.7 --depth 1 \
  https://github.com/pallets/click ~/curso-claude/material-lab-03/click
```

Comprueba que quedó en el commit correcto:

```bash
git -C ~/curso-claude/material-lab-03/click log --oneline -1
```

Debe imprimir `874ca2b`. Esa carpeta se copia en el lab; no trabajes dentro de
ella. Si el clon falla, el lab explica cómo seguir con otro proyecto que ya
tengas en disco.

---

## 4. Python con uv

`uv` gestiona la versión de Python, el entorno virtual y las dependencias. Es un binario único y no compila nada.

### Linux, macOS y WSL

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Cierra y vuelve a abrir la terminal, o recarga tu shell.

Instala la versión de Python del curso:

```bash
uv python install 3.12
```

Comprueba:

```bash
uv --version
uv python list
```

No necesitas `pyenv`, `virtualenv` ni `pip` por separado.

---

## 5. Git

Comprueba primero si ya lo tienes:

```bash
git --version
```

Si el comando no existe, instálalo: en **Linux y WSL** con
`sudo apt update && sudo apt install -y git`; en **macOS** basta `git --version`,
que ofrece instalar las herramientas de línea de comandos de Xcode; en
**Windows** no hace falta, porque el curso trabaja dentro de WSL.

Después configura tu identidad, que es lo que firma cada commit:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
```

Comprueba que ambos devuelven valor:

```bash
git config --get user.name
git config --get user.email
```

---

## 6. Claude Code

Necesitas una cuenta compatible: suscripción de Claude, Anthropic API o acceso
empresarial configurado. Algunas capacidades opcionales dependen del plan. Revisa
la [matriz de compatibilidad](compatibilidad.md) antes del curso.

Instalación nativa:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

La instalación con npm es heredada y puede mostrar aviso de migración. Úsala
solo si tu organización la exige:

```bash
npm install -g @anthropic-ai/claude-code
```

Si ya la tienes, ejecuta `claude doctor` y sigue la migración que indique tu
versión en lugar de mantener dos instalaciones en paralelo.

En Windows, instálalo **dentro de Ubuntu**, no en Windows.

Autenticación:

```bash
claude
```

La primera ejecución abre el flujo de inicio de sesión en el navegador.

### Sandbox: dos paquetes en Linux y WSL

El sandbox de Bash que se usa en la sesión 9 funciona en Linux, macOS y WSL 2, y
**no** en Windows nativo. En macOS no hay nada que instalar. En Linux y WSL 2
necesita dos paquetes:

```bash
sudo apt-get install bubblewrap socat
```

Sin ellos, `/sandbox` abre una pestaña de dependencias en lugar de funcionar.
Instálalos ahora: es un `apt-get` de treinta segundos que evita perder el paso 6
del laboratorio.

Diagnóstico:

```bash
claude doctor
```

Debe terminar sin errores.

Guarda también tu versión, para poder compararla con la línea base del curso si
algo se comporta distinto:

```bash
claude --version
```

### Precalentamiento (opcional, recomendado)

Claude Code trae lecciones interactivas. En una sesión:

```text
/powerup
```

Diez lecciones cortas: hablar con tu código, enseñarle tus reglas, modos, deshacer, subagentes, comandos propios, automatizar, ejecución en segundo plano, elección de modelo y uso multi-dispositivo.

Son de **descubrimiento**: muestran que la funcionalidad existe y la dejan probar una vez. El curso trabaja el criterio para usarlas. Hacerlas antes de la sesión 1 te ahorra tiempo de nivelación.

---

## 7. El material del curso

Varios laboratorios parten de un archivo que ya está escrito —con su error
dentro— y que vive junto al lab en este repositorio. Clónalo una vez:

```bash
mkdir -p ~/curso-claude
git clone https://github.com/alefiengo/curso-claude-code-desarrolladores.git ~/curso-claude/material
```

Los labs se refieren a esa ruta como `$CURSO`. Defínela de forma permanente para
no tener que escribirla cada vez:

```bash
echo 'export CURSO=~/curso-claude/material' >> ~/.bashrc
source ~/.bashrc
```

Si usas `zsh` —el predeterminado en macOS—, sustituye `~/.bashrc` por `~/.zshrc`
en las dos líneas.

### Qué acabas de crear

`~/curso-claude/` es la carpeta del curso, y va a contener cosas con vidas
distintas. Conviene tener el mapa antes de empezar:

```text
~/curso-claude/
├── material/            este repositorio. Es $CURSO. No trabajes aquí dentro.
├── material-lab-03/     el clon de click para el Lab 03 de la sesión 1.
├── evidencias/          lo que escribes tú. Se conserva.
└── sesion-01/           carpetas desechables de los labs. Se borran al terminar.
```

Desde la sesión 2 aparece además `curso-claude-code-api`, el proyecto que
construyes durante el curso, con su propia carpeta `evidencias/`.

Comprueba que apunta a donde debe:

```bash
ls $CURSO/sesiones
```

Debe listar la carpeta de la sesión 1. **Las demás aparecen conforme se
imparten**: el material se publica sesión a sesión, así que no te falta nada si
solo ves una. Antes de cada clase, actualiza tu copia:

```bash
cd $CURSO && git pull
```

Para leer el material con el mismo editor que usarás en clase:

```bash
code $CURSO
```

---

## Verificación final

**Todo esto se hace desde la terminal integrada de VS Code.** Si estás en
Windows y la barra inferior izquierda no dice `WSL: Ubuntu-24.04`, para y vuelve
al paso 2: lo que sigue fallará.

Ejecuta los cinco comandos. Los cinco deben responder sin error:

```bash
code --version
claude --version
docker run --rm hello-world
uv --version
git config --get user.email
```

Y comprueba dos cosas más: que la imagen de PostgreSQL está descargada y que el
material del curso está donde los labs lo esperan.

```bash
docker image ls postgres
ls $CURSO/sesiones
```

Guarda la salida como evidencia del preflight:

```bash
mkdir -p ~/curso-claude/evidencias
{ code --version; claude --version; uv --version; git --version
  docker --version; docker run --rm hello-world > /dev/null && echo "docker daemon: ok"
  echo "CURSO=$CURSO"; ls $CURSO/sesiones; } \
  | tee ~/curso-claude/evidencias/preflight.txt
```

`docker --version` responde aunque el daemon esté parado: por eso el bloque
ejecuta también un contenedor real. Y `echo $CURSO` en vacío significa que la
variable no quedó definida, que es la causa más común de que fallen los `cp` de
los laboratorios.

Si algo falla, revisa [problemas frecuentes](problemas-frecuentes.md).

Antes de abrir un repositorio real, lee [Seguridad desde la Primera Sesión](seguridad.md).
