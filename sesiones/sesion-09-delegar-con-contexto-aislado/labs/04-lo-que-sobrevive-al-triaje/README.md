# Lab 04: Lo que Sobrevive al Triaje

## Objetivo

Construir un consolidador que ejecuta comprobaciones sin herramientas de
edición, usarlo para verificar los hallazgos de la revisión de código y de
la auditoría, y decidir tú cuáles se aceptan, cuáles se rechazan y qué pasa con el
refactor.

## Por qué este lab

Tienes resultados de revisión, evidencia y preguntas pendientes. Ahora
compruebas qué hallazgos se sostienen. Una suite verde no desmiente un problema
que sus tests no cubren; una decisión de alcance tampoco elimina un riesgo.
Necesitas distinguir ambas cosas antes de integrar.

Separar esas tres clases —confirmado, desmentido y ya decidido— es el trabajo
que no se delega. Lo que sí se delega es reunir la evidencia, y para eso hace
el consolidador necesita ejecutar, una capacidad que no diste al auditor.

## Requisitos

- Labs 02 y 03 terminados: resultados de la revisión de código y de la
  auditoría, captura `.diff` con su base y refactor sin confirmar.
  Si no hubo hallazgos o refactor justificado, trae ese resultado explícito.
  No se exige haber ejecutado las revisiones incorporadas no disponibles.

## Ritmo de Trabajo

Este lab tiene 27 minutos:

| Min | Debe existir |
|---:|---|
| 0–7 | `.claude/agents/consolidador-de-hallazgos.md` revisado y guardado |
| 7–13 | Evidencia para hasta dos hallazgos prioritarios, o comprobaciones generales si no hubo ninguno |
| 13–18 | Triaje decidido; prueba en archivo temporal realizada y limpiada, o registrada como omitida |
| 18–27 | El destino del refactor decidido, la solicitud de cambios escrita y todo integrado |

**Si necesitas cortar aquí:** lo mínimo es el triaje decidido. La integración
se puede terminar después, pero no dejes la rama abierta hasta la sesión 10.
Si falta tiempo, deja sin verificar los hallazgos restantes como pendientes,
omite el experimento del paso 3 y descarta el refactor si requiere correcciones
que no puedes completar. Antes de pausar, termina la limpieza del archivo
temporal si hiciste la prueba.

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
- Lee en el README cómo ejecutar las comprobaciones y qué estado dejan en la
  base de datos. No ejecutes peticiones sobre un esquema que los tests acaban
  de revertir; informa si necesita preparación antes de continuar.
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
llegaron, los hallazgos de la revisión de código del Lab 02, las comprobaciones
adicionales si las hubo y los del auditor-de-seguridad. Incluye la ruta de
la captura y su commit base; conserva el origen de cada hallazgo.
Enséñame el encargo antes de mandarlo.
```

Míralo antes de que salga: si el encargo llega recortado o resumido, el
consolidador va a verificar un resumen y no los hallazgos.

Para la ruta mínima, indícale que verifique hasta dos hallazgos prioritarios y
marque el resto como pendientes con la comprobación que falta. Si no hubo
ninguno, pásale ese resultado y encárgale ejecutar la suite, el linter y la
comparación de OpenAPI, sin inventar hallazgos para llenar la tabla.

### 3. Comprobar el límite sin tocar el refactor

Este experimento es opcional si falta tiempo. Puedes hacerlo aunque no haya
hallazgos: compruebas una capacidad, no corriges un defecto.

Pídele a Claude crear un directorio temporal nuevo fuera del repositorio y
mostrar su ruta absoluta. El archivo `prueba-escritura.txt` todavía no debe
existir allí. Sustituye la ruta antes de enviar el encargo:

```text
Retoma al consolidador y pídele escribir solo la palabra prueba en
[ruta absoluta del directorio temporal]/prueba-escritura.txt.
No modifiques la API, la captura, Git, permisos ni configuración.
```

Observa la llamada real, no solo la respuesta del agente:

- Si se niega por su instrucción de no escribir, registra ese motivo.
- Si intenta escribir mediante un comando, observa si lo consigue o si los
  permisos lo bloquean. No cambies los permisos para forzar el resultado.

Pide a Claude comprobar si el archivo existe y qué contiene. Después elimina
solo ese archivo de prueba y el directorio si está vacío. Comprueba que el
código sigue coincidiendo con la captura y que el área de preparación no
cambió.

Quitar herramientas de edición no cierra la escritura por comandos. Una
negativa basada en instrucciones tampoco prueba que la capacidad no exista.
Si omitiste el experimento, deja su resultado como no observado.

### 4. Triar

Ahora decides tú, hallazgo por hallazgo:

- **Aceptado** solo si la comprobación lo confirma y corresponde al alcance.
  Un hallazgo sin evidencia no se acepta: queda pendiente, y dices qué faltaría para decidirlo.
- **Rechazado por evidencia**: cita la comprobación que desmiente el problema y
  su resultado. No reproducirlo una vez no basta si la prueba no cubre el caso.
- **Rechazado por alcance o decisión**: cita el archivo y la decisión que
  explica por qué no corresponde corregirlo aquí. Esto no desmiente un riesgo
  real: registra las condiciones en que sí importaría.
- **Pendiente** si falta evidencia para decidir. Indica qué comprobación falta
  y si esa incertidumbre impide integrar el refactor.

El triaje no va a un documento nuevo: va a la descripción de la solicitud de
cambios, que es donde alguien lo va a leer de verdad.
Si no hubo hallazgos, registra esa ausencia, las comprobaciones generales y
sus límites. No equivale a demostrar que no hay defectos.

### 5. Decidir el destino del refactor

Con el triaje decidido, el cambio del Lab 01 tiene tres finales posibles, y los
tres son válidos si los puedes defender: integrarlo tal cual, corregir lo
aceptado y después integrarlo, o descartarlo entero.
Si no había refactor justificado, conserva esa conclusión e integra solo los
agentes. Si la suite quedó roja, corrige o descarta el cambio hasta recuperar
el estado verde antes de integrar.

```text
[Di qué decidiste y por qué.] Aplica esa decisión sin confirmar todavía.
Si descartamos el refactor, recupera sus archivos desde el commit base y retira
solo los archivos nuevos de ese cambio, preservando los agentes. Si corregimos,
conserva los tests existentes y añade una prueba de regresión cuando haga falta.
Ejecuta la suite, el linter y la comparación de OpenAPI. No integres si fallan.
```

### 6. Entregar

La captura del Lab 01 sigue documentando lo que se revisó entonces. Si
corregiste el código, prepara sus rutas revisadas y genera otra captura
identificada contra el mismo commit base, incluyendo los archivos nuevos de
la corrección. Limita esa captura a las rutas del refactor; los agentes se
revisan aparte. Revisa la corrección antes de integrar y conserva la original.

Revisa el cambio completo de la rama contra `main`, incluidos los archivos
nuevos: deben estar los tres agentes y el refactor, si lo conservaste. El
módulo común nuevo es parte válida del refactor. Separa lo que preparaste en
el Lab 01 de los archivos de agentes antes de repartir los commits; preparar
las rutas entonces no autorizaba confirmarlas juntas.

Pide a Claude el reparto por intención con `segmentar-commits`, revisa las
rutas de cada grupo y autoriza los commits por separado. El commit del
refactor debe incluir el módulo nuevo; los archivos de agentes van en su
propio grupo. Comprueba la suite y el diff de la rama antes de publicar:


```text
Publica la rama y abre la solicitud de cambios hacia main. En la descripción,
además de qué cambia, qué se decidió y por qué, cómo se comprueba y qué queda
sin probar, incluye la identificación de la captura revisada y su commit base.
Añade el triaje: cada hallazgo con decisión y motivo; los rechazos deben citar
la prueba que los desmiente o la decisión documentada de alcance. Si no hubo hallazgos, dilo. Enséñamela antes de
crearla.
```

Revísala e intégrala cuando las comprobaciones estén en verde. Pide volver a
`main`, actualizarla y retirar la rama ya integrada. La sesión deja tres
agentes versionados y el triaje en la solicitud de cambios.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué subagentes hay en .claude/agents/, con sus herramientas, en una tabla.
3. Qué archivos nuevos hay fuera de .claude/agents/ y si todos pertenecen al
   refactor aprobado; la captura .diff debe seguir fuera del repositorio.
4. uv run pytest -q y uv run ruff check .
5. Si openapi.json coincide con la especificación que genera el código.
6. Los commits de main que no estaban al empezar hoy, uno por línea.
```

El lab está completo si:

- [ ] Los tres subagentes están en `main`, cada uno con su autoridad declarada.
- [ ] El consolidador ejecutó comprobaciones de hallazgos o las generales si no hubo ninguno; lo no comprobado queda pendiente.
- [ ] Registraste la prueba de escritura, limpiaste su archivo temporal y comprobaste que la API no cambió, o anotaste que la omitiste por tiempo.
- [ ] Cada hallazgo tiene una decisión motivada en la solicitud de cambios; cada rechazo cita evidencia o una decisión documentada. Si no hubo hallazgos, consta ese resultado.
- [ ] El refactor tiene un destino decidido y argumentado, o consta que no había uno justificado.
- [ ] La suite está en verde, no queda ninguna rama sin integrar y el repositorio no ganó documentos nuevos.

## Limpieza

Detén los contenedores sin eliminar volúmenes.

Antes de cerrar, `/context`: observa el espacio ocupado por encargos,
resúmenes y revisiones. No equivale al contexto total consumido por todos
los agentes. Conserva la captura hasta registrar el triaje y verificar la
integración; no la añadas al repositorio.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El consolidador dice que no recibió ningún hallazgo | Comprueba el encargo: si los revisores no encontraron ninguno, usa las comprobaciones generales del paso 2; si se omitieron por error, vuelve a pasarlos |
| El consolidador escribe el archivo de prueba | Registra la herramienta que usó y limpia el archivo. Si usó una herramienta de edición, revisa su configuración; si fue un comando, observaste el límite del recorte |
| El consolidador no responde a su nombre | Cierra con `/exit` y vuelve a abrir. Con `.claude/agents/` ya creado no debería pasar, pero si acabas de crear el archivo en otra ventana, esta sesión puede no haberlo recogido |
| Dice que no puede ejecutar la suite | Comprueba que la base de datos está levantada y que le declaraste la herramienta de ejecutar comandos |
| Todos los hallazgos quedan rechazados | Puede ser correcto. Comprueba que cada rechazo cite la evidencia que lo desmiente o la decisión documentada que lo deja fuera de alcance |
| Todos quedan aceptados | Sospecha, y comprueba: mira si alguno de los hallazgos de seguridad choca con algo que el contrato o `CLAUDE.md` ya deciden. Si de verdad ninguno lo hace, acéptalos y dilo |
| El commit queda bloqueado por el hook de la sesión 8 | La especificación no coincide con el código. Regenera `openapi.json` y mira el diff: si cambió, el refactor tocó el contrato y eso debería estar en el triaje |
| Necesitas cortar antes de integrar | Conserva el triaje en tus notas; pásalo a la descripción de la solicitud de cambios al abrirla. Integra antes de la sesión 10, que empieza con `main` en verde y sin ramas abiertas |
