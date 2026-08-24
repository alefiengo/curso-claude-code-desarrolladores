# Lab 02: Criterio Falseable

## Objetivo

Convertir peticiones vagas en objetivos verificables, y reconocer cuándo un criterio puede ser falseado por el propio agente.

## Riesgo que trabaja

Dos fallos distintos, que se confunden con facilidad:

1. **El oráculo no observa lo que se interviene.** Si los tests no cubren la función que vas a refactorizar, "los tests pasan" no dice nada sobre ella.
2. **El oráculo es modificable.** Aunque sí la cubran, el agente puede reescribir el test para cumplir la condición.

El lab demuestra el primero de forma determinista y audita el segundo como un
riesgo: Claude puede modificar el oráculo o no. El objetivo no es forzar un fallo
concreto, sino reconocer qué garantías ofrece realmente el criterio.

## Requisitos

- Lab 01 completado.
- Python 3 y Git disponibles.

## Paso a Paso

### 1. Preparar el archivo de trabajo

```bash
mkdir -p ~/curso-claude/sesion-01/lab-02 && cd ~/curso-claude/sesion-01/lab-02
export MATERIAL=$CURSO/sesiones/sesion-01-especificar-y-verificar/labs/02-criterio-falseable/material
cp $MATERIAL/medidas.py .
code medidas.py
git init -q
printf '__pycache__/\n' > .gitignore
git add medidas.py .gitignore && git commit -qm "Estado inicial"
```

El `.gitignore` no es un detalle: Python deja archivos `.pyc` en `__pycache__/`
cada vez que se importa un módulo. Sin ignorarlos, los `git add -A` de este lab
los confirman y **cada `git diff --stat` sale con ruido binario**, justo en el
laboratorio donde vas a auditar diffs.

`$CURSO` es la copia del material que clonaste en el
[preflight](../../../../docs/instalacion-entorno.md). `medidas.py`
tiene cuatro funciones y varios defectos deliberados; con el archivo abierto en
el editor puedes seguir lo que hace el agente en cada paso.

El repositorio te va a servir para comprobar qué archivos tocó el agente.

### 2. Ver el problema con tus propios ojos

```bash
python3 -c "
import medidas as m
ms = [m.registrar('cocina', 22), m.registrar('patio', 35), m.registrar('patio', 31)]
print(m.contar_por_sensor(ms))
"
```

Salida:

```text
{'cocina': 1, 'patio': 1}
```

Debería decir `{'cocina': 1, 'patio': 2}`. Hay dos mediciones de `patio`.

### 3. Reformular "arregla los errores"

La petición original no sirve: no dice qué error, ni cómo se sabrá que quedó resuelto.

Reformulada con las tres partes:

```text
contar_por_sensor en medidas.py devuelve 1 para todos los sensores en lugar
de contar las mediciones de cada uno. Corrígelo sin cambiar la firma.
Termina cuando este comando imprima {'cocina': 1, 'patio': 2}:
python3 -c "import medidas as m; ms=[m.registrar('cocina',22),m.registrar('patio',35),m.registrar('patio',31)]; print(m.contar_por_sensor(ms))"
```

| Parte | Dónde está |
|---|---|
| Contexto | "devuelve 1 para todos los sensores en lugar de contar" |
| Alcance | "en medidas.py", "sin cambiar la firma" |
| Criterio | "termina cuando este comando imprima …" |

Lo que lo hace verificable es **una salida exacta**, no "que cuente bien".

Lánzala:

```bash
claude
```

Pega la reformulación en la sesión.

Comprueba:

```bash
python3 -c "
import medidas as m
ms = [m.registrar('cocina', 22), m.registrar('patio', 35), m.registrar('patio', 31)]
print(m.contar_por_sensor(ms))
"
git add -A && git commit -qm "Corrige contar_por_sensor"
```

### 4. Reformular "añade tests"

"Añade tests" deja que el agente elija qué cubrir. Nombra cuatro casos, pero deja
fuera deliberadamente la función que vas a refactorizar después:

```text
medidas.py no tiene ningún test. Crea test_medidas.py con unittest cubriendo:
registrar devuelve las claves esperadas, buscar sin coincidencias, buscar con
dos coincidencias y contar_por_sensor con un sensor repetido.
No modifiques medidas.py.
Termina cuando `python3 -m unittest discover -q` pase y muestre 4 tests.
```

Comprueba:

```bash
python3 -m unittest discover -v 2>&1 | tail -5
git add -A && git commit -qm "Añade tests"
```

### 5. Comprobar qué cubre realmente la suite

Los cuatro tests cubren `registrar`, `buscar` y `contar_por_sensor`. **Ninguno toca `resumen`**, que es justo la función que vas a refactorizar en el paso siguiente.

Compruébalo:

```bash
grep -c "resumen" test_medidas.py
```

Devuelve `0`.

Esto importa: si refactorizas `resumen` y tu único criterio es "que los tests pasen", **la suite pasará aunque rompas `resumen` por completo**. El criterio no es falseable: es irrelevante.

Antes de tocar nada, fija el comportamiento actual con un test de caracterización:

```bash
python3 -c "
import medidas as m
ms = [m.registrar('cocina', 22), m.registrar('patio', 35)]
print(repr(m.resumen(ms)))
"
```

Copia esa salida exacta y pídele el test:

```text
Añade a test_medidas.py un test de caracterización para resumen que compare
su salida exacta con este valor, para la entrada
[registrar('cocina',22), registrar('patio',35)]:
<pega aquí la salida del comando anterior>
No modifiques medidas.py.
Termina cuando `python3 -m unittest discover -q` pase y muestre 5 tests.
```

```bash
python3 -m unittest discover -v 2>&1 | tail -3
git add -A && git commit -qm "Fija el comportamiento de resumen"
```

Ahora la suite sí observa lo que vas a intervenir.

### 6. Auditar un criterio falseable

`resumen` mezcla el conteo y el formateo en un solo bucle. Pide refactorizarlo **con el criterio insuficiente a propósito**:

```text
Refactoriza resumen en medidas.py separando el conteo del formateo.
Termina cuando los tests pasen.
```

Cuando termine, revisa qué archivos cambió. Hacen falta **los dos** comandos:

```bash
git diff --stat
git status --short
```

`git diff --stat` solo ve archivos que Git ya sigue. Si al "separar el conteo del
formateo" el agente creó un módulo nuevo, ese archivo no aparece en el diff y sí
en `git status --short`, marcado con `??`. Auditar lo que cambió con un solo
comando deja fuera justo lo que no esperabas.

### 7. Comprobar si falseó el criterio

Si en la salida aparece `test_medidas.py`, el agente **modificó aquello con lo
que se le mide**. Cumplió la condición al pie de la letra sin conservar un
oráculo independiente. Si no aparece, el resultado salió bien esta vez, pero el
criterio seguía concediendo ese permiso.

> Un criterio que el agente puede reescribir no es un criterio.

Vuelve al estado anterior y repite con el criterio cerrado. Otra vez hacen falta
dos comandos, por la misma razón:

```bash
git restore -- .           # deshace cambios en archivos seguidos
git clean -nd              # LISTA lo que borraría, sin borrar nada
```

**Lee esa lista antes de seguir.** `git clean` borra sin pasar por la papelera:
lo que desaparezca ahí no se recupera. Deben aparecer solo archivos que creó el
agente en este paso. Si ves algo tuyo, no continúes: sácalo de la carpeta
primero.

Cuando la lista sea la esperada, ejecuta el borrado:

```bash
git clean -fd              # elimina los archivos nuevos que creó el agente
git status --short         # debe quedar vacío
```

`-n` es "dry run" y `-f` es "force". Previsualizar antes de una operación
irreversible es el mismo hábito que este lab entrena con los diffs.

```text
Refactoriza resumen en medidas.py separando el conteo del formateo,
manteniendo la salida idéntica. No modifiques test_medidas.py.
Termina cuando `python3 -m unittest discover -q` pase con 5 tests sin haber
tocado los tests. Muestra también `git diff --stat` como evidencia.
```

Comprueba de nuevo:

```bash
git diff --stat
git status --short
```

Ahora `test_medidas.py` no debe aparecer en el diff. Si `git status --short`
muestra archivos `??`, decide si forman parte del refactor —un módulo nuevo puede
ser legítimo— o si son residuo. En cualquier caso, tienes que verlos antes de
confirmar.

### 8. Guardar el resultado

```bash
git add -A && git commit -qm "Refactoriza resumen"
```

## Validación

```bash
cd ~/curso-claude/sesion-01/lab-02
python3 -m unittest discover -q
git log --oneline
git diff --stat HEAD~1 HEAD
```

La práctica está completa si:

- [ ] `python3 -m unittest discover -q` pasa y muestra 5 tests.
- [ ] `contar_por_sensor` devuelve `{'cocina': 1, 'patio': 2}` para el caso del paso 2.
- [ ] El último commit no modifica `test_medidas.py`.
- [ ] Revisaste los archivos nuevos con `git status --short`, no solo el diff.
- [ ] Puedes explicar por qué "termina cuando los tests pasen" era un criterio insuficiente.

## Limpieza

No limpies todavía. La validación general de la sesión necesita `lab-01` y
`lab-02`. La limpieza conjunta está al final del README de la sesión.

## Problemas Frecuentes

| Error | Causa | Solución |
|---|---|---|
| `No tests ran` | Los tests no siguen el patrón `test*.py` | Comprobar el nombre del archivo generado y renombrarlo |
| El agente no falsea el criterio en el paso 6 | Resolvió el refactor sin tocar los tests | No es un fallo. Lee `git diff` y anótalo: la lección es que **no estaba garantizado** |
| El test de caracterización falla nada más crearlo | La salida pegada no coincide con la real | Volver a ejecutar el comando del paso 5 y copiar la salida exacta, incluidos los saltos de línea |
| `git restore -- .` no revierte | Los cambios ya estaban confirmados | No borres commits. Crea una rama desde el commit `Fija el comportamiento de resumen` y repite allí |
| Tras revertir sigue habiendo un archivo del intento anterior | `git restore` solo toca archivos seguidos por Git | `git status --short`, luego `git clean -nd` para ver la lista y `git clean -fd` para borrar |
| El diff parece limpio pero el refactor creó un módulo | `git diff` no muestra archivos sin seguir | Comprobar siempre también `git status --short` |
| El agente modifica `medidas.py` al añadir tests | El prompt no lo prohibía | Revisar que la reformulación incluya "No modifiques medidas.py" |
| `ModuleNotFoundError: No module named 'medidas'` | El comando se ejecuta fuera de la carpeta | `cd ~/curso-claude/sesion-01/lab-02` |
