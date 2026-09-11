# Lab 02: El Revisor que no Estuvo Ahí

## Objetivo

Hacer la misma pregunta tres veces sobre el mismo código —en tu sesión, con un
delegado que hereda tu conversación, y con un subagente que no sabe nada de
ella— y comparar qué encuentra cada uno.

## Por qué este lab

El cambio que tienes sin confirmar lo escribió un agente, y lo único que volvió
de él fue su propio relato: qué tocó, qué decidió, por qué está bien. Ese
relato ya está en tu conversación. Todo lo que preguntes a partir de ahora lo
lee primero.

Una segunda opinión que empieza leyendo la versión del autor no es una segunda
opinión. Hoy ves cuánto cambia el veredicto según con cuánto contexto llega
quien revisa, y construyes el primer revisor que no tiene ninguno.

## Requisitos

- Lab 01 terminado: el refactor en `feature/errores-en-un-solo-lugar`, sin
  confirmar, y `.claude/agents/refactorizador.md` ya confirmado.

## Ritmo de Trabajo

Este lab tiene 28 minutos:

| Min | Debe existir |
|---:|---|
| 0–8 | Los dos veredictos que heredan tu conversación, anotados |
| 8–16 | `.claude/agents/revisor-de-codigo.md` revisado y guardado |
| 16–23 | Su veredicto, y qué contexto dice que tenía |
| 23–28 | La tabla con los tres, y qué encontró cada uno que los otros no |

**Si necesitas cortar aquí:** lo mínimo es el revisor escrito y guardado. Sus
hallazgos viven en esta conversación y se van con ella, pero el agente y la
rama se quedan en disco: mañana lo vuelves a invocar sobre el mismo estado y
tienes los hallazgos otra vez.

## Paso a Paso

La pregunta de hoy es una sola, y se la vas a hacer a los tres igual:

```text
Revisa el manejo de errores de los endpoints de tareas tal como está ahora en
el repositorio, contra el contrato de la API y las reglas del proyecto, y dime
si lo integrarías: qué está bien, qué está mal y qué te falta para decidir.
```

### 1. El veredicto de dentro de tu sesión

Claude Code trae una skill de revisión incorporada. Comprueba primero si tu
instalación la tiene:

```text
/skills
```

Si aparece `/code-review`, úsala. Si no aparece, pega la pregunta de arriba en
el hilo.

Cualquiera de las dos formas sirve para lo que mide este lab, y por el mismo
motivo: en una sesión de terminal, `/code-review` corre como un **fork**, así
que se lleva tu conversación entera igual que si preguntaras aquí. Además
revisa lo que revisa de fábrica —errores de corrección y limpiezas—, no tu
contrato ni tus reglas.

Anota el veredicto en una línea.

### 2. El veredicto del que hereda tu conversación

```text
/subtask
```

Y a continuación, la misma pregunta.

`/subtask` manda el trabajo aparte, pero **con tu contexto completo**: lleva la
conversación entera, incluido el relato del refactorizador. Anota su veredicto
al lado del anterior.

### 3. Escribir el revisor que no estuvo ahí

```text
Crea un subagente de proyecto llamado revisor-de-codigo. Enséñame el archivo
antes de guardarlo.

Que solo pueda leer y buscar: nada de editar, escribir ni ejecutar comandos.

Que en el cuerpo quede escrito contra qué revisa, en este orden:

- El contrato de la API: que ningún comportamiento observable se haya movido.
- Las reglas del proyecto en .claude/rules/.
- Los tests: si alguno está escrito para pasar en vez de para comprobar,
  decir cuál y por qué.
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

### 4. El veredicto del que no sabe nada

```text
@agent-revisor-de-codigo
```

Y la misma pregunta, otra vez. No le cuentes que hubo un refactor: que lo note
o que no lo note es parte de lo que estás midiendo.

Fíjate en lo que eso implica. Sin herramientas para ejecutar comandos no puede
correr `git diff`, así que no va a comparar dos versiones: va a juzgar el
código como está, contra el contrato. Es justo lo que le pides a un revisor
que no estuvo ahí —que no sepa qué había antes ni por qué se cambió—, y es la
diferencia con los otros dos, que revisan un cambio del que ya conocen la
historia.

Cuando vuelva, pregúntale qué sabía al empezar:

```text
@agent-revisor-de-codigo ¿Qué contexto tenías al arrancar? Dime qué archivos
de instrucciones del proyecto habías cargado y si sabías algo de la
conversación en la que se produjo ese código.
```

Lo que tiene que haber ocurrido: no conoce la conversación, y sí conoce el
`CLAUDE.md` del proyecto. Si además menciona las reglas de `.claude/rules/`,
anótalo. Lo que se comprueba mirando vale más que lo que se supone.

### 5. Comparar

Esta tabla la escribes tú, y no va a ningún archivo: la necesitas hoy, en el
Lab 04.

| Quién revisó | Qué contexto tenía | Veredicto | Qué encontró que los otros no |
|---|---|---|---|
| Tu sesión | Tu conversación entera | | |
| `/subtask` | Tu conversación entera, aparte | | |
| `revisor-de-codigo` | Ninguno: el repositorio y nada más | | |

No hay un resultado obligatorio. Puede que los tres coincidan, y eso también
dice algo: que el cambio era limpio, o que el relato del refactorizador era
fiel.

Al leer la tabla, ten presente que los separan **dos** cosas, no una. La
primera es cuánto contexto llevaban. La segunda es que al tercero le
escribiste un oficio —contra qué revisa y en qué orden— que los otros dos no
tenían. Cuando encuentre algo que los demás no vieron, pregúntate cuál de las
dos lo explica: a veces es que no conocía el relato del autor, y a veces es
que llevaba una lista y ellos no.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y qué archivos tiene modificados el árbol de trabajo.
2. Qué hay en .claude/agents/, con las herramientas que declara cada uno.
3. Si el archivo del revisor-de-codigo declara que no arregla, y con qué
   palabras.
4. Si apareció algún archivo nuevo que no sea el del subagente.
5. uv run pytest -q
```

El lab está completo si:

- [ ] Los tres veredictos están anotados, con quién tenía qué contexto.
- [ ] `.claude/agents/revisor-de-codigo.md` declara solo herramientas de lectura y búsqueda.
- [ ] Sabes decir qué cargó el revisor al arrancar y qué no.
- [ ] No apareció ningún documento nuevo: los hallazgos siguen en la conversación.
- [ ] El refactor sigue sin confirmar.

## Limpieza

Ninguna. El Lab 03 trabaja sobre el mismo estado. Antes de seguir, `/context`:
compara lo que ocupó la revisión del `/subtask` con lo que ocupó la del
subagente, que solo te devolvió su informe.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| `/code-review` no aparece en `/skills` | Pega la pregunta en el hilo. Lo que compara este lab es el contexto de quien revisa, no la skill concreta |
| El revisor intenta editar y falla | Es la prueba de que el recorte funciona. Anótalo: la herramienta no está, así que no hay nada que negociar |
| Devuelve una lista genérica de buenas prácticas | Le falta oficio en el archivo, no contexto. Añade contra qué revisa —contrato, reglas, tests— y vuelve a invocarlo |
| No encuentra el módulo de tareas | Dile la ruta. Ve el repositorio en disco, pero no sabe cómo llamas tú a cada parte |
| Los tres veredictos son idénticos | Resultado válido. Anota si coinciden en aprobar o en rechazar: el Lab 04 va a verificar los hallazgos uno por uno |
| El revisor propone el parche igualmente | Su límite lo prohíbe. Corrige el archivo del agente, no la respuesta de hoy, y vuelve a invocarlo |
