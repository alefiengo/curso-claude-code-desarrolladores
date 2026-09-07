# Referencia Rápida — Sesión 7

## Comandos de la Sesión

| Comando o control | Qué hace | Dónde lo usas |
|---|---|---|
| `/rename` | Pone nombre a la sesión actual, para encontrarla y retomarla por ese nombre | Lab 03 |
| `--resume <nombre>` | Retoma una conversación anterior de este directorio, por el nombre que le pusiste | Lab 03 |
| `--continue` | Retoma la conversación más reciente de este directorio, sin selector | Referencia |
| `/clear` | Vacía el contexto de la conversación, sin perder el archivo de la sesión | Lab 03, para simular retomar sin contexto |
| `/diff` | Revisa los cambios antes de confirmar | Lab 01, Lab 02 y Lab 03 |
| `/skills` | Lista las skills que la sesión reconoce | Lab 01 |
| `/context` | Muestra qué ocupa la ventana de contexto | Al cerrar cada lab |

`--continue` no se usa hoy con hands-on: hace lo mismo que `--resume <nombre>`
cuando solo tienes una sesión reciente en el directorio, sin que tengas que
recordar el nombre.

## `.claude/rules/` frente a `CLAUDE.md`

| | `CLAUDE.md` | `.claude/rules/*.md` |
|---|---|---|
| Cuándo carga | Siempre, al iniciar la sesión | Siempre, si no tiene `paths`; solo cuando Claude toca un archivo que coincide, si lo tiene |
| Para qué sirve | Contexto general del proyecto: arquitectura, comandos, decisiones | Convenciones acotadas a un procedimiento o a un tipo de archivo |
| Cómo se acota | No se acota: todo el archivo carga siempre | Con `paths` en el encabezado, con patrones como `src/api/**/*.py` |

Una regla sin `paths` se comporta igual que una sección de `CLAUDE.md`: carga
siempre. La diferencia es organizativa, no de comportamiento —por eso el
Lab 02 te hace decidir cuál de las dos formas le corresponde a cada cosa que
escribes.

## El Carácter que no se Ve

`U+200B` —espacio de ancho cero— es un carácter real que no imprime nada
visible. Un `title` compuesto solo por ese carácter parece vacío para quien
lo mira, pero no lo es para un `strip()` que solo recorta espacios ASCII: el
valor sigue teniendo longitud, así que pasa la validación.

El contrato lo resuelve por categoría Unicode, no por lista de caracteres:
rechaza el valor si, tras recortar los extremos, no queda ningún carácter
fuera de `Cc` (control), `Cf` (formato), `Zl` (separador de línea), `Zp`
(separador de párrafo) o `Zs` (espacio). Cualquier carácter invisible que
exista cae en alguna de esas cinco categorías.

## Qué es un Hueco

Es información real sobre el proyecto que solo existe en tu memoria, no en
ningún archivo del repositorio. Se detecta pidiéndole a una conversación sin
contexto —`/clear`, o cualquiera que no haya vivido lo que tú viviste— que
describa el proyecto solo con lo que encuentra escrito, y comparando su
respuesta con lo que tú sabes. Se cierra escribiendo esa pieza en el lugar
que le corresponde: un commit, una descripción de entrega, una regla, o el
documento del plan.

## Si Algo Falla

| Señal | Causa habitual |
|---|---|
| `claude --resume <nombre>` no encuentra la sesión | El nombre se puso con `/rename` dentro de la conversación; sin ese paso, retómala con `/resume` sin nombre y elige de la lista |
| Después de `/clear`, la respuesta parece "recordar" la conversación | Está leyéndolo del repositorio —commits, plan, contrato—, que es exactamente lo que el Lab 03 comprueba. No es memoria de la conversación |
| Una regla de `.claude/rules/` no aparece en `/context` | Si tiene `paths`, solo carga cuando Claude lee un archivo que coincide con el patrón. Pídele que lea uno y vuelve a mirar |
| El título con `U+200B` sigue respondiendo `201` | La validación cubre espacios ASCII pero no categorías Unicode. Revisa que rechace `Cc`, `Cf`, `Zl`, `Zp` y `Zs`, no solo el carácter de espacio común |
