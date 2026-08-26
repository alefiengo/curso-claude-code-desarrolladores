# Lab 02: Convertir una Petición Ambigua en Contrato

## Objetivo

Transformar una petición incompleta en comportamiento verificable, fijar los
tests antes de implementar y comprobar el resultado con una validación
independiente.

## Por qué este lab

"No aceptes pagos inválidos" parece claro hasta que alguien tiene que escribir
el código. ¿Cero es válido? ¿Un booleano cuenta como entero? ¿Se registra el
evento rechazado? ¿Qué error recibe quien llama?

Si esas decisiones no están en el encargo, no desaparecen: el agente las toma
por ti. Aquí vas a descubrir las ambigüedades antes de editar, convertir las
respuestas en un contrato y separar dos momentos: escribir la comprobación y
escribir la solución.

## Requisitos

- Haber completado el Lab 01.
- El repositorio `~/curso-claude/sesion-01/webhook-ledger` limpio.
- El último commit debe ser la corrección de idempotencia.

## Paso a Paso

### 1. Incorporar la solicitud y la plantilla

```bash
cd ~/curso-claude/sesion-01/webhook-ledger
git status --short
export MATERIAL=$CURSO/sesiones/sesion-01-especificar-y-verificar/labs/02-criterio-falseable/material
cp $MATERIAL/change_request.md .
cp $MATERIAL/contract_template.md .
cp $MATERIAL/acceptance_validation.py .
git add change_request.md contract_template.md acceptance_validation.py
git commit -m "Añade solicitud de validación de pagos"
```

Lee la solicitud:

```bash
cat change_request.md
```

Contiene una intención, pero todavía no define un comportamiento implementable.

### 2. Pedir investigación, no código

Abre Claude:

```bash
claude
```

```text
Lee @change_request.md y @billing.py. No edites nada todavía.
Enumera las decisiones de comportamiento que faltan para poder implementar sin
adivinar. Hazme como máximo cinco preguntas, ordenadas por impacto.
```

La respuesta puede variar. Lo importante es que detecte decisiones sobre tipos,
límites, error observable y efectos laterales.

Si empieza a editar, presiona `Esc`: todavía no existe un contrato.

### 3. Cerrar las decisiones

Usa estas decisiones de producto para completar `contract_template.md`:

| Tema | Decisión |
|---|---|
| Identificador | Cadena con al menos un carácter que no sea espacio |
| Importe | Entero mayor que cero; `True` y `False` no son importes |
| Error | `ValueError` para cualquier entrada inválida |
| Estado | Un rechazo no cambia saldo ni eventos procesados |
| Compatibilidad | Los casos válidos y la idempotencia anterior se conservan |
| Fuera de alcance | Persistencia, concurrencia, firma y formato HTTP |

Puedes editar la plantilla tú o pedirle a Claude que la complete con esas
decisiones. Revísala antes de continuar.

El contrato está listo si otra persona puede derivar los mismos casos de prueba
sin preguntarte nada más.

### 4. Convertir el contrato en tests y detenerse en rojo

```text
Convierte @contract_template.md en tests dentro de test_billing.py.
En esta fase no modifiques billing.py.

Cubre cada invariante del contrato, ejecuta `python3 -m unittest -v` y detente
cuando los tests nuevos fallen por el comportamiento que aún falta. Explica por
qué ese rojo es el esperado.
```

Un rojo útil falla porque falta la capacidad descrita. Un error de importación,
una sintaxis rota o un nombre inventado no demuestra el requisito.

Revisa los tests añadidos:

```bash
git diff -- test_billing.py
python3 -m unittest -v
```

Comprueba que hay casos para identificador, importe, ausencia de efectos y
compatibilidad. Si falta uno, corrige los tests antes de implementar.

### 5. Fijar la comprobación

Cuando los tests representan el contrato:

```bash
git add test_billing.py contract_template.md
git commit -m "Define contrato y regresiones de pagos inválidos"
git status --short
```

A partir de este commit, la implementación no puede cambiar ni el contrato ni
los tests para conseguir verde.

### 6. Implementar contra el contrato

Continúa en la misma sesión:

```text
Implementa @contract_template.md en billing.py.
No modifiques contract_template.md, test_billing.py ni acceptance_validation.py.
Haz el cambio mínimo y conserva la idempotencia del ticket anterior.

Termina cuando pasen:
- `python3 -m unittest -v`
- `python3 acceptance_validation.py`

Después muestra los archivos modificados, los resultados y cualquier riesgo que
siga fuera de alcance.
```

Interrumpe si cambia la comprobación o amplía el dominio.

### 7. Auditar el resultado

Sal de Claude y ejecuta:

```bash
git status --short
git diff --exit-code HEAD -- contract_template.md test_billing.py acceptance_validation.py
git diff --check
python3 -m unittest -v
python3 acceptance_validation.py
git diff -- billing.py
```

La validación independiente no sustituye tus tests. Confirma desde otro archivo
las decisiones principales del contrato y detecta si los tests generados
olvidaron una de ellas.

### 8. Aceptar el cambio

Antes de confirmar, responde:

- ¿Cada decisión del contrato tiene una comprobación?
- ¿Una entrada inválida deja el objeto exactamente como estaba?
- ¿El cambio preserva la idempotencia?
- ¿El diff contiene algo que el ticket no pidió?

Si las respuestas están respaldadas por código o salida ejecutable:

```bash
git add billing.py
git commit -m "Rechaza eventos de pago inválidos"
git status --short
```

## Validación

```bash
cd ~/curso-claude/sesion-01/webhook-ledger
python3 -m unittest -v
python3 acceptance_validation.py
git log --oneline -3
git status --short
```

- [ ] La solicitud vaga terminó convertida en un contrato explícito.
- [ ] Los tests se confirmaron antes de modificar la implementación.
- [ ] El rojo inicial correspondía al comportamiento ausente.
- [ ] Suite y validación independiente pasan.
- [ ] Contrato, tests y validación no cambiaron durante la implementación.
- [ ] El repositorio termina limpio.

## Limpieza

No borres todavía. El README de la sesión pide guardar evidencia antes de
eliminar `~/curso-claude/sesion-01`.

## Problemas Frecuentes

| Problema | Causa probable | Acción |
|---|---|---|
| Claude propone código en el paso 2 | Confundió investigación con implementación | Interrumpe y repite que todavía faltan decisiones |
| Los tests nuevos pasan antes de implementar | No representan una capacidad ausente | Compáralos con cada fila del contrato y añade el caso que falta |
| La suite da error en vez de fallo | El test no puede ejecutar el comportamiento | Corrige montaje, importación o sintaxis antes de seguir |
| La validación independiente falla y la suite pasa | Los tests generados omitieron una invariante | Conserva la validación; añade el caso faltante a la suite y corrige el código |
| Cambiaron tests durante la implementación | La comprobación dejó de ser independiente | Restaura los archivos desde `HEAD` y repite la implementación |
