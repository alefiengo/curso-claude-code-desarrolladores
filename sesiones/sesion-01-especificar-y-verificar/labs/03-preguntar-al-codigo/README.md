# Lab 03: Preguntar al Código Ajeno

## Objetivo

Entender un repositorio desconocido apoyándote en el agente, y verificar cada afirmación contra el archivo que la respalda.

## Por qué este lab

Preguntar a un agente sobre código que no conoces es rápido, y por eso es fácil
creerle sin más. Aquí vas a pedirle siempre el archivo y la línea de donde saca
cada respuesta, y a comprobarlo tú.

Al final harás una pregunta distinta: en vez de "qué hace este código", "por qué
se diseñó así". La respuesta ya no se puede comprobar abriendo un archivo, y
notar esa diferencia es lo que te llevas del lab.

## Requisitos

- Claude Code instalado y autenticado.
- Git configurado.
- Conexión a internet para clonar, o la copia que descargaste en el preflight
  (ver paso 1).

## Paso a Paso

### 1. Clonar un proyecto que no conozcas

```bash
mkdir -p ~/curso-claude/sesion-01/lab-03 && cd ~/curso-claude/sesion-01/lab-03
git clone --branch 8.1.7 --depth 1 https://github.com/pallets/click
cd click
```

Sirve cualquier proyecto Python de tamaño medio que no hayas leído antes. `click`
es una librería de línea de comandos: en el tag `8.1.7` son unas **10 000 líneas
de código en 16 archivos**, más 6 000 de tests.

Ese número importa más de lo que parece. Es demasiado para leerlo entero antes de
preguntar, y demasiado para volcarlo en una conversación. Es exactamente la
situación que hace útil a un agente, y el problema que trabaja la sesión 2.

El tag `8.1.7` fija el contenido usado por el curso. `--depth 1` evita descargar
el historial completo. Clonar un tag deja el repositorio en `detached HEAD`, y
Git lo avisa: aquí da igual, porque no vas a confirmar nada.

**Si el clon falla o la red va lenta**, tienes dos salidas.

La primera es la copia que descargaste en el preflight. Si seguiste la
[instalación del entorno](../../../../docs/instalacion-entorno.md), ya tienes
`click` en `~/curso-claude/material-lab-03/click`: cópiala y sigue igual.

```bash
cp -r ~/curso-claude/material-lab-03/click .
cd click
git log --oneline -1
```

Debe decir `874ca2b`. Es el mismo commit y el mismo contenido: el lab funciona
idéntico, solo cambia de dónde salen los archivos.

La segunda es usar **otro proyecto Python que ya tengas en disco**, tuyo o
clonado antes. Sirve cualquiera entre 5 000 y 20 000 líneas que no hayas leído a
fondo. Lo único que pierdes es la comprobación concreta del paso 5, donde el lab
sabe de antemano dónde vive la configuración de `pytest`; el método —preguntar,
exigir la fuente, verificarla— es el mismo.

### 2. Abrir la sesión sobre el repositorio

```bash
claude
```

### 3. Primera pregunta

```text
¿Cómo se ejecutan los tests de este proyecto?
```

El agente busca en el repositorio y responde.

### 4. Exigir la fuente

No des la respuesta por buena. Pregunta:

```text
¿En qué archivo y línea lo viste?
```

El agente cita un archivo concreto.

### 5. Verificar tú mismo

Abre el archivo citado **en el editor**: `Ctrl+P`, escribe el nombre y salta a la
línea con `Ctrl+G`. Comprueba que dice lo que el agente afirmó. Tener el archivo
delante mientras lees la respuesta es justo lo que hace verificable la afirmación.

Compruébalo también desde la terminal, sobre el archivo que **el agente** citó:

```bash
grep -n "pytest" ARCHIVO_QUE_CITO
```

Sustituye `ARCHIVO_QUE_CITO` por el que te haya dado. Si no sabes cuál es, esa
ya es la primera señal: la respuesta no traía fuente comprobable.

En `click` 8.1.7 la configuración de pytest **no** está en `pyproject.toml`
—ese archivo no existe en este proyecto—, sino en `setup.cfg` y `tox.ini`. Si el
agente citó `pyproject.toml`, acabas de encontrar una afirmación que no se
sostiene: márcala como incorrecta. Es el resultado más útil del lab.

Anota el resultado con una de estas marcas:

| Marca | Significado |
|---|---|
| ✅ Verificada | El archivo decía lo que el agente dijo |
| ⚠️ Imprecisa | Parcialmente cierto, o el archivo no era ese |
| ❌ Incorrecta | No se sostiene |

### 6. Repetir con dos preguntas más

Aplica el mismo ciclo —preguntar, exigir la fuente, verificar— a estas dos:

```text
¿Qué dependencias de terceros necesita para funcionar, sin contar las de desarrollo?
```

```text
¿Qué convención siguen la ubicación y el nombre de los archivos de test?
```

### 7. Buscar el límite

Haz una cuarta pregunta más difícil, de las que no tienen una respuesta literal en un archivo. Por ejemplo:

```text
Si tuviera que añadir un tipo de parámetro nuevo, ¿en qué archivo empezaría y por qué?
```

Exige la fuente igual que antes.

Aquí la respuesta ya no es un hecho literal del repositorio, sino una inferencia
de diseño. Fíjate en si el agente la presenta como hipótesis razonada, separa
evidencia de conclusión y reconoce alternativas.

### 8. Anotar el resultado

Escribe una tabla con las cuatro preguntas:

| Pregunta | Respuesta | Archivo citado | Tipo | Marca |
|---|---|---|---|---|
| Cómo se ejecutan los tests | … | `setup.cfg:36` | Hecho | ✅ |

Usa `Hecho`, `Inferencia` o `Sin evidencia` en la columna `Tipo`.

La columna que importa es la última.

## Validación

```bash
cd ~/curso-claude/sesion-01/lab-03/click
ls
git log --oneline -1
```

La práctica está completa si:

- [ ] Tienes las cuatro preguntas anotadas con su archivo citado y su marca.
- [ ] Verificaste al menos una respuesta abriendo el archivo por tu cuenta.
- [ ] Sabes distinguir cuáles tenían respuesta literal y cuál requería una inferencia.
- [ ] En la cuarta separaste la evidencia del razonamiento.

## Limpieza

No hace falta limpiar todavía.

## Problemas Frecuentes

| Error | Causa | Solución |
|---|---|---|
| `fatal: could not read Username` | El remoto pide credenciales | Clonar por HTTPS público, sin usuario, tal como está en el paso 1 |
| La clonación tarda mucho | Se omitió `--depth 1`, o hay mucha gente clonando a la vez | Cancelar y repetir con `--depth 1`; si sigue lento, usar la copia del preflight |
| No hay red, o GitHub no responde | El clon viene de un servicio externo | Usar la copia del preflight, o cualquier proyecto Python que ya tengas en disco (paso 1) |
| El agente responde sin citar archivo | La pregunta no exigía fuente | Preguntar explícitamente en qué archivo y línea lo vio |
| El archivo citado no existe | La afirmación no se sostiene | Marcar ❌ y pedirle que lo compruebe de nuevo |
| El repositorio es demasiado grande | Se eligió un proyecto extenso | Usar `click`, o uno de tamaño parecido: entre 5 000 y 20 000 líneas |
| No existe `~/curso-claude/material-lab-03` | No hiciste esa descarga en el preflight | Clonar ahora con el comando del paso 1, o usar otro proyecto Python que ya tengas en disco |
| Git avisa de `detached HEAD` | Se clonó un tag, no una rama | Es lo esperado en este lab. No confirmes nada aquí |
