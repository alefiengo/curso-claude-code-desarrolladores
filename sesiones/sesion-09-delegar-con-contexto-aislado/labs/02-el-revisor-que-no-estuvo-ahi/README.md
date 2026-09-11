# Lab 02: El Revisor que no Estuvo Ahí

## Objetivo

Pedir la misma revisión tres veces sobre el mismo cambio —con la skill de
fábrica, con un delegado que hereda tu conversación, y con un subagente que no
sabe nada de ella— y comparar qué encuentra cada uno.

## Por qué este lab

El cambio que tienes sin confirmar lo escribió un agente, y lo único que
volvió de él fue su propio relato: qué tocó, qué decidió, por qué está bien.
Ese relato ya está en tu conversación. Todo lo que le preguntes a partir de
ahora lo lee primero.

Una segunda opinión que empieza leyendo la versión del autor no es una segunda
opinión. Hoy ves cuánto cambia el veredicto según con cuánto contexto llegue
quien revisa, y construyes el primer revisor que no tiene ninguno.

## Requisitos

- Lab 01 terminado: el refactor en `feature/errores-en-un-solo-lugar`, sin
  confirmar, y `.claude/agents/refactorizador.md` ya confirmado.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–4 | El cambio guardado en un archivo que cualquiera pueda leer |
| 4–12 | Los dos veredictos que heredan tu conversación |
| 12–20 | `.claude/agents/revisor-de-codigo.md` revisado y guardado |
| 20–27 | Su veredicto, y su informe guardado en `evidencias/` |
| 27–30 | La tabla con los tres, y qué encontró cada uno que los otros no |

**Si necesitas cortar aquí:** lo mínimo es el revisor escrito y su veredicto
guardado. La comparación se puede terminar después, pero el Lab 04 necesita el
informe en disco.

## Paso a Paso

### 1. Dejar el cambio en un archivo

Un subagente que solo lee no puede ejecutar `git diff`: no tiene con qué. Si
quieres que revise un cambio, el cambio tiene que estar en algo que se pueda
leer.

```text
Guarda el diff completo de esta rama contra main en
evidencias/s09-cambio.diff, sin confirmar nada.
```

Esa dependencia es real y conviene verla ahora: recortar herramientas tiene un
precio, y el precio es que hay trabajo de preparación que se queda de tu lado.

### 2. El veredicto de la skill de fábrica

Claude Code trae una skill de revisión incorporada. Comprueba primero si tu
instalación la tiene:

```text
/skills
```

Si aparece `/code-review`, úsala sobre el cambio actual. Si no aparece, pide
la revisión en el hilo con este encargo:

```text
Revisa el cambio sin confirmar de esta rama y dime si lo integrarías: qué
está bien, qué está mal y qué te falta para decidir.
```

Anota su veredicto en una línea. Da igual cuál de las dos formas usaste: las
dos corren dentro de tu sesión, con tu conversación delante.

### 3. El veredicto del que hereda tu conversación

```text
/subtask Revisa el cambio sin confirmar de esta rama contra el contrato de la
API y dime si lo integrarías, con los motivos.
```

`/subtask` manda el trabajo aparte, pero **con tu contexto completo**: lleva la
conversación entera, incluido el relato del refactorizador. Anota su veredicto
al lado del anterior.

### 4. Escribir el revisor que no estuvo ahí

```text
Crea un subagente de proyecto llamado revisor-de-codigo. Enséñame el archivo
antes de guardarlo.

Que solo pueda leer y buscar: nada de editar, escribir ni ejecutar comandos.

Que en el cuerpo quede escrito contra qué revisa, en este orden:

- El contrato de la API: que ningún comportamiento observable cambie.
- Las reglas del proyecto en .claude/rules/.
- Los tests: si alguno cambió, decir cuál y por qué eso es sospechoso.
- La legibilidad del resultado, al final y solo si lo anterior está limpio.

Que devuelva una lista de hallazgos, cada uno con el archivo, qué encontró,
qué lo hace un problema y qué tan grave es. Que separe lo que rompe algo de
lo que es cuestión de gusto.

Y un límite: el revisor revisa, no arregla. No propone parches y no reescribe
código en su respuesta.

Dime también qué herramientas le declaraste y qué pasaría si no le declararas
ninguna.
```

Comprueba lo mismo que en el Lab 01 antes de guardarlo: que las herramientas
están declaradas, que el límite está escrito y que no repite tu `CLAUDE.md`.

### 5. El veredicto del que no sabe nada

```text
@agent-revisor-de-codigo Revisa el cambio que está en evidencias/s09-cambio.diff
contra el código del repositorio y dime si lo integrarías.
```

Cuando vuelva, pregúntale qué sabía al empezar:

```text
@agent-revisor-de-codigo ¿Qué contexto tenías al arrancar? Dime qué archivos
de instrucciones del proyecto habías cargado y si sabías algo de la
conversación en la que se produjo ese cambio.
```

Lo que tiene que haber ocurrido: no conoce la conversación, y sí conoce el
`CLAUDE.md` del proyecto. Si además menciona las reglas de `.claude/rules/`,
anótalo. Lo que se comprueba mirando vale más que lo que se supone.

### 6. Guardar su informe y comparar

El revisor no puede escribir. Su informe lo guardas tú:

```text
Guarda el informe completo del revisor-de-codigo en evidencias/s09-revisor.md,
tal como lo devolvió, sin resumirlo ni añadirle nada.
```

Ahora la comparación, y esta la escribes tú:

| Quién revisó | Qué contexto tenía | Veredicto | Qué encontró que los otros no |
|---|---|---|---|
| La skill de fábrica o el hilo | Tu conversación entera | | |
| `/subtask` | Tu conversación entera, aparte | | |
| `revisor-de-codigo` | Ninguno: el repositorio y nada más | | |

No hay un resultado obligatorio. Puede que los tres coincidan, y eso también
dice algo: que el cambio era limpio, o que el relato del refactorizador era
fiel. Lo que no puede pasar es que no sepas cuál de los tres leyó primero la
versión del autor.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y qué archivos tiene modificados el árbol de trabajo.
2. Qué hay en .claude/agents/, con las herramientas que declara cada uno.
3. Si evidencias/s09-cambio.diff y evidencias/s09-revisor.md existen y
   cuántas líneas tiene cada uno.
4. Si el archivo del revisor-de-codigo declara que no arregla, y con qué
   palabras.
5. uv run pytest -q
```

El lab está completo si:

- [ ] Los tres veredictos están anotados, con quién tenía qué contexto.
- [ ] `.claude/agents/revisor-de-codigo.md` declara solo herramientas de lectura y búsqueda.
- [ ] El informe del revisor está en `evidencias/s09-revisor.md`, completo.
- [ ] Sabes decir qué cargó el revisor al arrancar y qué no.
- [ ] El refactor sigue sin confirmar.

## Limpieza

Ninguna. El Lab 03 trabaja sobre el mismo estado. Antes de seguir, `/context`:
compara lo que ocupó la revisión del `/subtask` con lo que ocupó la del
subagente, que solo te devolvió su informe.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| `/code-review` no aparece en `/skills` | Usa el encargo del paso 2 en el hilo. Lo que compara este lab es el contexto de quien revisa, no la skill concreta |
| El revisor intenta editar y falla | Es la prueba de que el recorte funciona. Anótalo: la herramienta no está, así que no hay nada que negociar |
| Devuelve una lista genérica de buenas prácticas | Le falta oficio en el archivo, no contexto. Añade contra qué revisa —contrato, reglas, tests— y vuelve a invocarlo |
| Dice que no encuentra el diff | Comprueba que `evidencias/s09-cambio.diff` existe y que le diste la ruta. El agente no ve tu árbol de trabajo: ve el repositorio en disco |
| Los tres veredictos son idénticos | Resultado válido. Anota si coinciden en aprobar o en rechazar, y guárdalo: el Lab 04 va a verificar los hallazgos uno por uno |
| El revisor propone el parche igualmente | Su límite lo prohíbe. Corrige el archivo del agente, no la respuesta de hoy, y vuelve a invocarlo |
