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

## Ritmo de Trabajo

Este lab tiene 45 minutos. Usa estos puntos de control para saber si vas
retrasado antes de que sea tarde:

| Min | Debe existir |
|---:|---|
| 0–8 | Solicitud leída y decisiones que faltan enumeradas |
| 8–18 | Contrato completado con las seis decisiones cerradas |
| 18–30 | Tests escritos y detenidos en el rojo correcto |
| 30–40 | Implementación contra el contrato, sin tocar la comprobación |
| 40–45 | Auditoría con `/diff` y Git, y commit |

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

Puedes editar la plantilla tú o delegarla, indicando qué puede tocar:

```text
Completa @contract_template.md con las decisiones que acabo de darte.
Solo ese archivo. No toques billing.py ni los tests, y no implementes nada.
Si una decisión no está en mi lista, márcala como pendiente en vez de elegirla.
```

Revísala antes de continuar. La última frase importa: sin ella, las decisiones
que faltan vuelven a tomarse solas, que es justo lo que este lab evita.

El contrato está listo si otra persona puede derivar los mismos casos de prueba
sin preguntarte nada más.

### 4. Convertir el contrato en tests y detenerse en rojo

Esta vez el curso no entrega el prompt. Redacta un contrato de tarea breve con la
plantilla de la sesión 1. Debe dejar explícitos estos cinco elementos:

- resultado: convertir cada invariante en una comprobación;
- fuente: `contract_template.md`;
- alcance: solo `test_billing.py`;
- restricción: no modificar `billing.py` durante esta fase;
- terminación: ejecutar `python3 -m unittest -v`, detenerse en el rojo por la
  capacidad ausente y explicar por qué es el rojo esperado.

Antes de enviarlo, intercámbialo con otra persona o pide una crítica del propio
encargo:

```text
Este es el encargo que voy a darte, todavía no lo ejecutes:

<pega aquí tu contrato de tarea>

¿Qué decisión tendrías que adivinar si lo recibieras tal cual? Enuméralas.
No propongas la redacción corregida: quiero escribirla yo.
```

Revisar el encargo cuesta un turno; corregir una implementación que partió de un
encargo ambiguo cuesta varios. Corrige lo que aparezca y entrega tu versión final
a Claude.

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

Continúa en la misma sesión, pero redacta tú el segundo contrato de tarea. Debe
nombrar:

- el comportamiento definido en `contract_template.md`;
- `billing.py` como único archivo de implementación permitido;
- `contract_template.md`, `test_billing.py` y `acceptance_validation.py` como
  comprobaciones protegidas;
- el cambio mínimo y la conservación de la idempotencia anterior;
- `python3 -m unittest -v` y `python3 acceptance_validation.py` como criterio de
  terminación;
- archivos modificados, resultados y riesgo residual como reporte de cierre.

Comprueba que contiene las cinco partes del contrato de tarea y el reporte de
cierre, y entrégalo a Claude.

Interrumpe si cambia la comprobación o amplía el dominio.

### 7. Auditar el resultado

El resumen que acaba de darte Claude no es evidencia. Compruébalo, primero sin
salir de la conversación:

```text
/diff
```

Las flechas izquierda y derecha alternan entre el diff completo y el cambio de
cada turno; arriba y abajo recorren los archivos. Busca una sola cosa: si algún
turno tocó `contract_template.md`, `test_billing.py` o `acceptance_validation.py`.
Un archivo modificado y luego revertido no aparece en el diff final, pero sí en
su turno.

Después sal con `/exit` y comprueba desde Git:

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
- [ ] Redactaste y conservaste los contratos para tests e implementación.
- [ ] Los tests se confirmaron antes de modificar la implementación.
- [ ] Recorriste el cambio con `/diff` antes de salir de la conversación.
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
