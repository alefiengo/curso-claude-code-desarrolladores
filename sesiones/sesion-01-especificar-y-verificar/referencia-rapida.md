# Referencia Rápida: Sesión 1

Es la más larga de las diez, y es la única que conviene tener a mano durante todo
el curso: además de los comandos de arranque contiene el método para escribir un
prompt, y eso se aplica en las diez sesiones. Las referencias siguientes son
cortas porque solo recogen lo que su sesión añade.

El mapa acumulativo de comandos vive en [comandos](../../docs/comandos.md).

## Verificar la Instalación

```bash
claude --version
claude doctor
claude --help
```

## Abrir una Sesión

```bash
claude                      # sesión interactiva sobre el directorio actual
claude "tu prompt"          # sesión interactiva con prompt inicial
claude -p "tu prompt"       # no interactivo: ejecuta, imprime y sale
claude -p "..." --allowedTools "Read Edit Bash(python3 *)"   # preautoriza herramientas
```

## Dentro de la Sesión

| Comando | Uso |
|---|---|
| `/help` | Comandos disponibles en tu versión |
| `/exit` | Salir de la sesión |

`Ctrl+D` también sale.

## Anatomía de un Prompt

```text
[CONTEXTO]  Qué problema real existe y dónde.
[ALCANCE]   Qué archivos entran. Qué NO tocar.
[CRITERIO]  Cómo sabrá que terminó.
```

Ejemplo:

```text
contar_por_sensor en medidas.py devuelve 1 para todos los sensores en lugar
de contar las mediciones de cada uno. Corrígelo sin cambiar la firma.
Termina cuando este comando imprima {'cocina': 1, 'patio': 2}:
python3 -c "import medidas as m; ms=[...]; print(m.contar_por_sensor(ms))"
```

## Modo No Interactivo

Sin interfaz no hay a quién pedir permiso: las herramientas se preautorizan o la tarea se bloquea.

```bash
--allowedTools "Read Edit Bash(python3 *)"
```

Declara solo lo que la tarea necesita.

## Criterios de Terminación

| Sirve | No sirve |
|---|---|
| `python3 -m unittest discover -q` pasa | "que quede bien" |
| El comando imprime una salida exacta | "que sea profesional" |
| `timeit` baja de un umbral en ms | "que siga buenas prácticas" |
| El endpoint responde 201 | "que esté optimizado" |

Prueba rápida: si el agente no puede comprobarlo solo, no es un criterio.

## Formas de Medir

| Quieres | Comando |
|---|---|
| Que pasen los tests | `python3 -m unittest discover -q` |
| Una salida concreta | `python3 -c "..."` |
| Un umbral de tiempo | `python3 -m timeit -s "setup" "codigo"` |
| Que no cambie el comportamiento | Tests previos, y prohibir tocarlos |

## Blindar un Criterio

Si el agente puede reescribir la condición, no es un criterio:

```text
...manteniendo el comportamiento. No modifiques test_medidas.py.
Termina cuando los tests pasen sin haberlos tocado.
```

Comprobar qué tocó:

```bash
git diff --stat
```

## Verificar una Afirmación

```text
¿En qué archivo y línea lo viste?
```

Sin fuente, no es un hecho.

## Checklist Antes de Enviar un Prompt

- [ ] ¿Está claro qué problema se resuelve, no solo qué hacer?
- [ ] ¿Dije qué archivos entran y cuáles no?
- [ ] ¿Hay un criterio que el agente pueda comprobar por sí mismo?
- [ ] ¿Puede el agente modificar aquello con lo que se mide?
- [ ] ¿Dejé el cómo abierto, salvo restricciones reales?

## Errores Comunes

| Error | Síntoma |
|---|---|
| Pedir texto, no resultados | Copias y pegas mucho |
| Sin criterio de terminación | Se declara satisfecho antes que tú |
| Criterio falseable | Los tests pasan pero el comportamiento cambió |
| Aceptar sin leer | Descubres el fallo tres sesiones después |
| Dictar la implementación | Le quitas la parte donde aporta |

## Limpieza de la Sesión

```bash
rm -rf ~/curso-claude/sesion-01
```
