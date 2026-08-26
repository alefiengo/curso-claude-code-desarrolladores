# Lab 01: Bucle de Verificación

## Objetivo

Observar la diferencia entre una tarea que el agente puede comprobar y una que no, sobre el mismo problema.

## Por qué este lab

Vas a lanzar la misma tarea tres veces, cambiando una cosa cada vez:

1. **Con una condición de terminación**, diciéndole exactamente qué debe cumplirse
   para dar el trabajo por hecho.
2. **Sin esa condición.** Claude puede comprobar su trabajo por su cuenta o no.
   Aquí verás si la prueba venía de lo que pediste o de su criterio del momento.
3. **Sin interfaz**, con `-p`, y sin autorizar herramientas de antemano. Como no
   hay nadie a quien pedir permiso, lo normal es que se detenga.

Al terminar sabrás pedir una tarea de forma que el propio agente compruebe si la
cumplió.

## Requisitos

- Claude Code instalado y autenticado.
- Python 3 disponible en la terminal.

## Paso a Paso

### 1. Preparar el archivo

El archivo de partida está en este repositorio, junto al lab. `$CURSO` es la
copia del material que clonaste en el
[preflight](../../../../docs/instalacion-entorno.md). Guarda la carpeta del lab
en una variable, porque la vas a usar tres veces:

```bash
mkdir -p ~/curso-claude/sesion-01/lab-01 && cd ~/curso-claude/sesion-01/lab-01
export MATERIAL=$CURSO/sesiones/sesion-01-especificar-y-verificar/labs/01-bucle-de-verificacion/material
cp $MATERIAL/calc.py .
```

Si `cp` dice que no existe el archivo, `$CURSO` no está definida: vuelve a
[El material del curso](../../../../docs/instalacion-entorno.md) en el preflight.

Ábrelo en VS Code para verlo mientras trabajas:

```bash
code calc.py
```

La función tiene un error evidente: `suma` resta. Compruébalo:

```bash
python3 -c "import calc; print(calc.suma(2, 3))"
```

Imprime `-1`.

### 2. Abrir una sesión y lanzar la tarea con criterio de terminación

Arranca en **modo Manual**, para que el agente se detenga antes de cada edición
y cada comando:

```bash
claude --permission-mode manual
```

No es un detalle: en los planes Pro, Max y Team una sesión arranca en auto mode,
donde un clasificador aprueba las acciones en tu lugar. Con `claude` a secas
verías muchas menos preguntas, y este paso te pide justamente observarlas.

Si tu versión no acepta `manual`, usa su valor de configuración, que es el mismo
modo con otro nombre:

```bash
claude --permission-mode default
```

Dentro de la sesión, pega este prompt:

```text
El archivo calc.py tiene un bug en la función suma. Corrígelo y verifica
ejecutando: python3 -c "import calc; assert calc.suma(2,3)==5; print('OK')"
```

Revisa cada solicitud de permiso antes de aceptarla. Una sesión interactiva es
intencional en este primer lab: permite ver qué archivo quiere editar Claude y
qué comando quiere ejecutar. Acepta solo si coincide con el alcance del lab. El
modo no interactivo `-p` necesita permisos preconfigurados; la sesión 10 desarrolla
este mecanismo con más profundidad.

### 3. Leer la respuesta

El texto varía en cada ejecución. Lo que debe haber ocurrido:

- Menciona **qué cambió** en el código: de resta a suma.
- **Ejecutó el comando de verificación**, no solo lo citó.
- Recoge el resultado de esa ejecución: el `OK`.

Si la respuesta no menciona haber ejecutado nada, revisa que tu prompt llevara la parte `verifica ejecutando ...`.

Revisa el cambio antes de darlo por bueno:

```text
/diff
```

Confirma el estado del archivo **sin cerrar Claude Code**. Divide la terminal
integrada de VS Code con `Ctrl+Shift+5`: te quedan dos paneles lado a lado, uno
con Claude Code y otro libre.

El panel nuevo abre una terminal desde cero: no está en la carpeta del lab y no
conoce el `$MATERIAL` que definiste antes, porque `export` solo vive en la
terminal donde se escribe. Prepáralo una vez, y lo usarás el resto del lab:

```bash
cd ~/curso-claude/sesion-01/lab-01
export MATERIAL=$CURSO/sesiones/sesion-01-especificar-y-verificar/labs/01-bucle-de-verificacion/material
```

Ahora sí, comprueba el archivo:

```bash
cat calc.py
python3 -c "import calc; print(calc.suma(2, 3))"
```

`calc.py` debe decir `return a + b`, y el comando imprimir `5`.

### 4. Repetir sin criterio de terminación

Desde el segundo panel, vuelve a romper el archivo:

```bash
cp $MATERIAL/calc.py .
```

Verás el cambio en el editor al instante, porque VS Code recarga el archivo. Esa
es la ventaja de tenerlo abierto: el estado del que partes no es una suposición.

Abre sesión y pide lo mismo sin decirle cómo comprobarlo:

```text
Corrige el bug de calc.py
```

El resultado vuelve a ser correcto: el error es de una línea.

La diferencia está en **cómo terminó**:

| Ejecución | Qué contiene la respuesta |
|---|---|
| Con criterio | Un comando ejecutado y su salida |
| Sin criterio | Puede haber evidencia, pero el prompt no la exige |

Si Claude también ejecutó una comprobación en la segunda, anótalo. No invalida
el ejercicio: demuestra que su comportamiento puede ser útil sin que forme parte
del contrato de la tarea. Con un bug de una línea da igual. Con una tarea de tres
archivos, no conviene depender de una decisión que puede cambiar entre ejecuciones.

> La diferencia no es si Claude acertó esta vez, sino si la comprobación formaba
> parte del resultado exigido y, por tanto, era reproducible y auditable.

### 5. La misma tarea sin interfaz

Hay un modo no interactivo que ejecuta la tarea, imprime y sale. Sirve para scripts y CI, y se trabaja a fondo en la última sesión.

Antes de continuar, revisa los cambios en la sesión abierta con `/diff` y sal
con `/exit`. Después rompe el archivo una vez más y prueba así:

```bash
cp $MATERIAL/calc.py .

claude -p "El archivo calc.py tiene un bug en la función suma. Corrígelo y \
verifica ejecutando python3 -c 'import calc; assert calc.suma(2,3)==5; print(\"OK\")'"
```

Con una configuración de permisos limpia o predeterminada, el agente debería
detenerse al no poder pedir autorización para editar. Comprueba si el archivo
quedó intacto:

```bash
cat calc.py
```

Sigue diciendo `return a - b`.

Si el archivo sí cambió, no des por fallido el lab: abre una sesión interactiva,
ejecuta `/permissions` y localiza qué regla previa autorizó la operación. Registra
esa evidencia antes de seguir.

### 6. Por qué se bloqueó, y cómo se resuelve

Sin interfaz no hay a quién preguntar. Las herramientas que necesita hay que **preautorizarlas**:

```bash
claude -p "El archivo calc.py tiene un bug en la función suma. Corrígelo y \
verifica ejecutando python3 -c 'import calc; assert calc.suma(2,3)==5; print(\"OK\")'" \
  --allowedTools "Read Edit Bash(python3 *)"
```

Ahora sí edita, ejecuta y responde.

```bash
cat calc.py
python3 -c "import calc; assert calc.suma(2,3)==5; print('OK')"
```

`--allowedTools` declara qué puede usar sin preguntar. Aquí: leer, editar, y ejecutar `python3`. Nada más — ni instalar paquetes, ni tocar git.

Es la primera aparición de una idea central del curso: **automatizar exige decidir de antemano qué se autoriza**. La sesión 10 la desarrolla.

## Validación

```bash
cd ~/curso-claude/sesion-01/lab-01
python3 -c "import calc; assert calc.suma(2,3)==5; print('OK')"
```

La práctica está completa si:

- [ ] El comando anterior imprime `OK`.
- [ ] En el paso 2 concediste permisos y sabes decir qué te pidió.
- [ ] En el paso 3 la respuesta incluía el comando ejecutado y su salida; en el paso 4 no, o no estaba garantizado.
- [ ] Registraste si la segunda ejecución produjo evidencia espontánea y puedes explicar por qué no formaba parte del criterio.
- [ ] En el paso 5 viste el bloqueo esperado o identificaste la regla que lo evitó, y en el paso 6 lo resolviste con `--allowedTools`.
- [ ] Puedes nombrar los cinco pasos del bucle: leer, editar, ejecutar, comprobar, responder.

## Limpieza

No limpies todavía. La carpeta `~/curso-claude/sesion-01` se usa en el resto de la sesión y se elimina al final, desde el README de la sesión.

## Problemas Frecuentes

| Error | Causa | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'calc'` | El comando se ejecuta fuera de la carpeta del lab | `cd ~/curso-claude/sesion-01/lab-01` |
| `cp: cannot stat '/calc.py'` | `$MATERIAL` está vacía en ese panel: `export` no viaja entre terminales | Repetir el `export MATERIAL=...` del paso 3 en el panel donde estés |
| El paso 5 no se bloquea y edita igual | Hay reglas de permiso previas en tu configuración | Comprobar con `/permissions`. El bloqueo depende de tu configuración, no del comando |
| `--allowedTools` sigue pidiendo permiso | El patrón no cubre la herramienta que necesita | Leer qué herramienta menciona el mensaje y añadirla al listado |
| Las comillas dan error en la terminal | Mezcla de comillas simples y dobles | Copiar el comando tal cual, con la barra invertida al final de la línea |
| El agente pide permiso y la tarea se queda esperando | La sesión espera tu decisión | Leer la operación y aceptar solo si coincide con el lab |
| No aparece ninguna petición de permiso | La sesión arrancó en auto mode, no en Manual | Salir con `/exit` y volver a abrir con `claude --permission-mode manual` |
| El agente corrige el archivo pero no ejecuta nada | El prompt no incluía el comando de verificación | Revisar que lleve la parte `verifica ejecutando ...` |
| En el paso 4 el agente sí ejecuta algo por su cuenta | Puede decidir comprobarse aunque no se lo pidas | Registrarlo como evidencia espontánea y comparar igualmente: **no estaba exigida** |
