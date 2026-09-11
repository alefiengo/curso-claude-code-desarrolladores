# Lab 04: Lo que Sobrevive al Triaje

## Objetivo

Construir el tercer revisor —el único que puede ejecutar comprobaciones, y sin
herramientas para editar nada—, usarlo para verificar los hallazgos de los
otros dos, y decidir tú cuáles se aceptan, cuáles se rechazan y qué pasa con el
refactor.

## Por qué este lab

Tienes dos tandas de hallazgos y ninguna forma barata de saber cuáles son
ciertos. Algunos se comprueban en diez segundos ejecutando la suite. Otros son
correctos en general y falsos aquí, porque contradicen algo que el proyecto
decidió a propósito hace cuatro sesiones y quien revisó no tenía forma de
saberlo.

Separar esas tres clases —confirmado, desmentido y ya decidido— es el trabajo
que no se delega. Lo que sí se delega es reunir la evidencia, y para eso hace
falta un agente con un permiso que los otros dos no tienen: ejecutar.

## Requisitos

- Labs 02 y 03 terminados: los hallazgos de los dos revisores en tu
  conversación, y el refactor sin confirmar.

## Ritmo de Trabajo

Este lab tiene 27 minutos:

| Min | Debe existir |
|---:|---|
| 0–7 | `.claude/agents/consolidador-de-hallazgos.md` revisado y guardado |
| 7–13 | Su tabla de hallazgos con la evidencia al lado |
| 13–18 | Tu decisión sobre cada hallazgo, con su motivo |
| 18–27 | El destino del refactor decidido, la solicitud de cambios escrita y todo integrado |

**Si necesitas cortar aquí:** lo mínimo es el triaje decidido. La integración
se puede terminar después, pero no dejes la rama abierta hasta la sesión 10.

## Paso a Paso

### 1. Escribir el que puede ejecutar

```text
Crea un subagente de proyecto llamado consolidador-de-hallazgos. Enséñame el
archivo antes de guardarlo.

Que pueda leer, buscar y ejecutar comandos, y que no reciba ninguna
herramienta de edición.

Que en el cuerpo quede escrito su procedimiento:

- Recibe en el encargo una lista de hallazgos, y empieza juntando los que
  dicen lo mismo con otras palabras.
- Para cada hallazgo, ejecuta la comprobación más barata que lo confirme o
  lo desmienta, y dice cuál ejecutó y qué salió.
- Para cada hallazgo, busca si el proyecto ya decidió eso a propósito, en el
  contrato de la API, en .claude/rules/ o en CLAUDE.md, y cita dónde.
- Devuelve una tabla con una fila por hallazgo: de quién viene, qué dice,
  qué comprobación ejecutó, qué salió y qué dice el proyecto al respecto.

Y un límite: el consolidador reúne evidencia y no decide. No dice qué aceptar
ni qué rechazar, no arregla nada y no escribe archivos.

Dime también por qué le hace falta ejecutar comandos y qué deja de poder hacer
aun teniéndolo.
```

Antes de guardarlo, comprueba que puede ejecutar y que no declara ninguna
herramienta de edición. Son dos cosas distintas y hoy hacen falta las dos.

### 2. Pasarle lo que no puede ver

Un subagente arranca limpio: no ha leído tu conversación, así que no conoce
ni un hallazgo de los labs anteriores. Lo que no ve, se lo das en el encargo:

```text
Invoca al consolidador-de-hallazgos y pásale dentro del encargo, tal como
llegaron, los hallazgos del revisor-de-codigo y los del auditor-de-seguridad.
Enséñame el encargo antes de mandarlo.
```

Míralo antes de que salga: si el encargo llega recortado o resumido, el
consolidador va a verificar un resumen y no los hallazgos.

### 3. Comprobar el límite

Elige un hallazgo de los que confirmó y pídele que lo arregle:

```text
@agent-consolidador-de-hallazgos Arregla el primer hallazgo confirmado de tu
tabla.
```

Hay dos finales posibles, y los dos enseñan lo mismo desde lados opuestos:

- **Dice que no puede**, porque no tiene herramientas de edición. El recorte
  hizo su trabajo.
- **Lo intenta por otro camino**: escribir el archivo con un comando de shell.
  También es un resultado válido, y es el más instructivo. Le diste permiso
  para ejecutar, y ejecutar incluye escribir.

Si lo consiguió, deshaz ese cambio antes de seguir:

```text
Descarta lo que el consolidador acabe de escribir y confírmame que el árbol de
trabajo solo tiene el refactor y los archivos de los subagentes.
```

Anota cuál de los dos te tocó. La conclusión no cambia: recortar herramientas
acota lo que un agente puede hacer **con esas herramientas**, y no cierra los
caminos que pasan por otra. Es el mismo límite que viste en la sesión 4,
cuando una regla escrita sobre la herramienta de lectura no cubría el mismo
archivo leído con un comando. Lo que se quiere prohibir de plano se escribe en
los permisos, que sí miran el comando.

### 4. Triar

Ahora decides tú, hallazgo por hallazgo, con tres reglas:

- **Aceptado** solo si la comprobación lo confirma. Un hallazgo sin evidencia
  no se acepta: queda pendiente, y dices qué faltaría para decidirlo.
- **Rechazado** exige citar dónde está escrita la decisión que lo vuelve ruido.
  "No hace falta" no es un motivo; "el contrato fija esto desde la sesión 6, y
  por eso" sí.
- Lo que no encaje en ninguna de las dos queda declarado como deuda, con su
  nombre. Eso también es un resultado.

El triaje no va a un documento nuevo: va a la descripción de la solicitud de
cambios, que es donde alguien lo va a leer de verdad.

### 5. Decidir el destino del refactor

Con el triaje decidido, el cambio del Lab 01 tiene tres finales posibles, y los
tres son válidos si los puedes defender: integrarlo tal cual, corregir lo
aceptado y después integrarlo, o descartarlo entero.

```text
[Di qué decidiste y por qué.] Aplícalo. Si hay que corregir algo, hazlo en
commits separados de los archivos de los agentes.
```

### 6. Entregar

Revisa el `/diff` completo. Tienen que aparecer los archivos de los
subagentes y el refactor, si decidiste conservarlo, y nada más. Después:

```text
Publica la rama y abre la solicitud de cambios hacia main. En la descripción,
además de qué cambia, qué se decidió y por qué, cómo se comprueba y qué queda
sin probar, incluye el triaje: cada hallazgo con su decisión y su motivo, y
los rechazados citando dónde está escrita la decisión. Enséñamela antes de
crearla.
```

Revísala e intégrala. Lo que quede fuera de esa descripción se pierde, y es
justo lo que se quiere: la sesión deja cuatro agentes versionados y una
decisión escrita donde se toman las decisiones.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué subagentes hay en .claude/agents/, con sus herramientas, en una tabla.
3. Si el repositorio ganó hoy algún archivo que no esté en .claude/agents/.
4. uv run pytest -q y uv run ruff check .
5. Si openapi.json coincide con la especificación que genera el código.
6. Los commits de main que no estaban al empezar hoy, uno por línea.
```

El lab está completo si:

- [ ] Los cuatro subagentes están en `main`, cada uno con su autoridad declarada.
- [ ] El consolidador ejecutó comprobaciones, y sabes qué hizo cuando le pediste arreglar una: negarse, o intentarlo por el camino que le dejaste abierto.
- [ ] Cada hallazgo tiene una decisión con su motivo en la descripción de la solicitud de cambios, y cada rechazo cita dónde está escrita la decisión.
- [ ] El refactor tiene un destino decidido y argumentado, cualquiera de los tres.
- [ ] La suite está en verde, no queda ninguna rama sin integrar y el repositorio no ganó documentos nuevos.

## Limpieza

Detén los contenedores sin eliminar volúmenes.

Antes de cerrar, `/context`: hoy trabajaron cuatro agentes y tu ventana solo
recibió cuatro resúmenes. Compara con lo que ocupaba al terminar la sesión 8.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El consolidador dice que no recibió ningún hallazgo | Llegaron recortados en el encargo. Vuelve al paso 2 y revisa el texto antes de mandarlo |
| El consolidador arregla el hallazgo | No es un fallo del lab: mira **cómo** lo hizo. Si usó herramientas de edición, su archivo declara de más y hay que quitárselas. Si lo hizo con un comando de shell, el archivo está bien y lo que falta es un permiso |
| El consolidador no responde a su nombre | Cierra con `/exit` y vuelve a abrir. Con `.claude/agents/` ya creado no debería pasar, pero si acabas de crear el archivo en otra ventana, esta sesión puede no haberlo recogido |
| Dice que no puede ejecutar la suite | Comprueba que la base de datos está levantada y que le declaraste la herramienta de ejecutar comandos |
| Todos los hallazgos quedan rechazados | Puede ser correcto. Revisa que cada rechazo cite un archivo: si alguno no lo hace, no es un rechazo, es una opinión |
| Todos quedan aceptados | Sospecha, y comprueba: mira si alguno de los hallazgos de seguridad choca con algo que el contrato o `CLAUDE.md` ya deciden. Si de verdad ninguno lo hace, acéptalos y dilo |
| El commit queda bloqueado por el hook de la sesión 8 | La especificación no coincide con el código. Regenera `openapi.json` y mira el diff: si cambió, el refactor tocó el contrato y eso debería estar en el triaje |
| Necesitas cortar antes de integrar | Deja el triaje decidido por escrito en la descripción de la rama. Integra antes de la sesión 10, que empieza con `main` en verde y sin ramas abiertas |
