# Lab 01: Resolver un Incidente Real

## Objetivo

Corregir un defecto de idempotencia con Claude Code y aceptar el cambio solo
después de revisar comportamiento, alcance y diff.

## Por qué este lab

Los sistemas de pago reintentan webhooks. Si el mismo evento se procesa dos
veces, el servicio no puede aplicar dos veces el mismo movimiento. Es un caso
pequeño, pero tiene todo lo que importa en un cambio profesional: un incidente,
un contrato, una regresión, límites y una decisión de aceptación.

Vas a recorrer el ciclo completo sobre código que no escribiste. No necesitas
entender cada línea antes de empezar; sí necesitas entender la evidencia antes
de aceptar.

## Requisitos

- Claude Code instalado y autenticado.
- Python 3 y Git disponibles.
- La variable `$CURSO` definida por el preflight.

## Paso a Paso

### 1. Preparar el repositorio

```bash
mkdir -p ~/curso-claude/sesion-01/webhook-ledger
cd ~/curso-claude/sesion-01/webhook-ledger
export MATERIAL=$CURSO/sesiones/sesion-01-especificar-y-verificar/labs/01-bucle-de-verificacion/material
cp $MATERIAL/billing.py .
cp $MATERIAL/test_billing.py .
cp $MATERIAL/ticket.md .
git init -q
git add .
git commit -qm "Añade caso inicial del webhook"
```

Comprueba que partes del estado preparado:

```bash
python3 -m unittest -v
```

La prueba `test_same_event_is_applied_once` debe fallar: el saldo termina en
`5000` cuando debería quedar en `2500`. Las otras dos deben pasar.

Si todas pasan, no continúes: el defecto ya no está presente y el lab perdió su
punto de partida.

### 2. Leer el ticket antes de delegar

```bash
sed -n '1,220p' ticket.md
sed -n '1,220p' billing.py
```

Responde antes de abrir Claude:

- ¿Qué comportamiento está roto?
- ¿Qué archivo no debe modificarse?
- ¿Qué temas quedan explícitamente fuera?
- ¿Qué comando decide si el cambio funciona?

Si no puedes responder las cuatro, el agente tampoco recibió todavía un
encargo controlable.

### 3. Abrir Claude Code en el repositorio correcto

```bash
claude
```

El directorio importa: aquí Claude puede ver el ticket, el código, la suite y el
estado de Git.

Comprueba el modo de permisos con `/status`. En los planes Pro, Max y Team la
sesión arranca en Auto mode: un clasificador aprueba acciones por ti. Cambia a
Manual con `Shift+Tab` antes de continuar, para ver cada permiso que Claude
pide.

### 4. Entregar el contrato de tarea

```text
Resuelve @ticket.md.

Antes de editar, reproduce el fallo y explica la causa con archivo y línea.
Haz el cambio mínimo que corrige la causa. No modifiques ticket.md ni
test_billing.py. Persistencia, concurrencia y validación de firmas quedan fuera.

Termina cuando `python3 -m unittest -v` pase. Al cerrar, informa:
1. causa encontrada;
2. archivos modificados;
3. comandos ejecutados y resultado;
4. riesgo que sigue fuera de alcance.
```

No copies una solución. Deja que Claude inspeccione, formule una hipótesis y la
pruebe.

### 5. Observar y dirigir

Mientras trabaja, busca este ciclo:

```text
lee ticket y código → reproduce → edita → ejecuta la suite → lee el resultado
```

Interrumpe con `Esc` si intenta:

- modificar `test_billing.py`;
- ampliar el trabajo a persistencia o concurrencia;
- declarar éxito sin ejecutar la suite;
- reescribir más código del necesario.

Redirige con el hecho concreto. Ejemplo:

```text
test_billing.py es parte de la comprobación y está fuera de alcance. Revierte
ese archivo y corrige el comportamiento en billing.py.
```

### 6. Revisar la evidencia del agente

La respuesta final debe permitirte localizar la causa, reconocer el cambio y
saber qué se ejecutó. Si falta un dato, pídelo antes de salir.

Abre el diff dentro de Claude:

```text
/diff
```

Después cierra la sesión:

```text
/exit
```

### 7. Verificar fuera de la conversación

```bash
git status --short
git diff --check
git diff --exit-code -- ticket.md test_billing.py
python3 -m unittest -v
git diff -- billing.py
```

Comprueba el significado de cada resultado:

- `git diff --exit-code -- ticket.md test_billing.py` termina en `0`: las
  fuentes del encargo y la comprobación no cambiaron.
- La suite termina en `OK`: el incidente y los casos anteriores pasan.
- El diff de `billing.py` es pequeño y explica el resultado sin trabajo ajeno.

### 8. Guardar el checkpoint

```bash
git add billing.py
git commit -m "Evita aplicar dos veces el mismo evento"
git status --short
```

El estado debe quedar limpio. Este commit es la base del Lab 02.

## Validación

```bash
cd ~/curso-claude/sesion-01/webhook-ledger
python3 -m unittest -v
git show --stat --oneline HEAD
git status --short
```

- [ ] Las tres pruebas pasan.
- [ ] El último commit solo cambia `billing.py`.
- [ ] Puedes señalar la causa del defecto en el código anterior.
- [ ] Puedes nombrar al menos un riesgo que el ticket dejó fuera.
- [ ] Revisaste el diff, no solo el resumen del agente.

## Limpieza

No borres el repositorio. El Lab 02 continúa desde este commit.

## Problemas Frecuentes

| Problema | Causa probable | Acción |
|---|---|---|
| `cp` no encuentra los archivos | `$CURSO` no está definida en esta terminal | Repite el `export` indicado en la instalación |
| Python no encuentra `billing` | Ejecutaste la suite fuera de `webhook-ledger` | Vuelve a la carpeta del lab |
| Todas las pruebas pasan al inicio | Copiaste una versión ya corregida | Repite el paso 1 desde el material del curso |
| Claude quiere cambiar el test | Busca el camino más corto al verde | Interrumpe y recuerda que el test está fuera de alcance |
| El diff incluye archivos inesperados | La tarea se amplió o había cambios previos | Detente, revisa `git status --short` y recupera el checkpoint |
