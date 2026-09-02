# Referencia Rápida — Sesión 5

## Comandos de la Sesión

| Comando o control | Qué hace | Dónde lo usas |
|---|---|---|
| `/skills` | Lista las skills disponibles y el nombre con el que se invoca cada una | Lab 02 y Lab 04, al comprobar que la tuya existe |
| `/reload-skills` | Recoge las skills añadidas o cambiadas en disco durante la sesión | Lab 02, si la primera no aparece |
| `/plan` | Entra en el modo que bloquea ediciones hasta que apruebes un plan, y vuelve a mostrar el plan de la sesión | Lab 03, antes de ejecutar |
| `Ctrl+G` | Abre el plan propuesto en tu editor para cambiarlo antes de aprobarlo | Lab 03 |
| `Shift+Tab` | Cicla los modos de permiso de la sesión | Lab 03, para volver a manual |
| `/permissions` | Muestra las reglas activas y **lo que se te ha denegado** en la sesión | Lab 01 y Lab 03 |
| `/diff` | Revisa los cambios antes de confirmar | Lab 01, Lab 02 y Lab 04 |
| `/context` | Muestra qué ocupa la ventana de contexto | Al cerrar el Lab 01 y el Lab 04 |
| `Esc` | Interrumpe el turno en curso | En cuanto veas una desviación |
| `/` | El menú de comandos y skills | Cuando no recuerdes cómo se llama la tuya |

`/reload-skills` casi nunca hace falta: Claude Code vigila los directorios de
skills y recoge los cambios por su cuenta. La excepción es la del Lab 02: un
directorio `.claude/skills/` que **no existía** cuando arrancó la sesión. Si
tras recargar sigue sin aparecer, sal con `/exit` y vuelve a entrar.

## Anatomía de una Skill

```text
.claude/skills/<nombre>/SKILL.md
```

El **nombre del directorio** es el nombre con el que se invoca: `/<nombre>`. El
archivo tiene dos partes.

| Parte | Qué es |
|---|---|
| Cabecera entre `---` | Metadatos. `description` es el que importa: con él Claude decide cuándo cargarla por su cuenta |
| Cuerpo en Markdown | El procedimiento que sigue cuando se ejecuta |

Va en el repositorio y se versiona: deja de ser tu forma de trabajar y pasa a
ser la del proyecto. Si la pones en `~/.claude/skills/` es tuya y nadie más la
ve.

| Quieres | Ponlo en la cabecera |
|---|---|
| Que solo se ejecute cuando la invoques tú | La opción que desactiva la invocación por parte del modelo |
| Que se ejecute en su propio contexto y te devuelva solo el resultado | La opción de contexto aislado. Es el desafío de esta sesión |

Una skill que se ejecuta aparte hace su trabajo en una ventana propia y te
devuelve la conclusión: lo que leyó para llegar a ella no vuelve contigo.

Pídele a Claude el nombre exacto de cada opción y que te enseñe el archivo: los
metadatos cambian entre versiones y la cabecera se lee solo si los tres guiones
son la primera línea.

## Contexto Inyectado

Una skill puede traer la salida de un comando **en el momento de invocarla**. Es
lo que la separa de un texto guardado: el procedimiento es fijo, los datos son
frescos.

| Inyecta | Cuesta | Sirve para |
|---|---|---|
| El resumen por archivo del diff | Poco | Saber qué se tocó y cuánto: el mapa del cambio |
| El diff completo | Mucho, y crece con el cambio | Casi nada que no resuelva el resumen |

La regla es la misma que con el contexto de una conversación: inyecta lo que
necesitas para decidir, no todo lo que existe.

## Los Tres Frenos del Lab 03

Sobre el mismo trabajo actúan tres cosas distintas, y conviene no confundirlas.

| Freno | Qué controla | Se salta si… |
|---|---|---|
| La skill | **Cómo** se hace el trabajo aquí | El modelo decide otra cosa: es una instrucción, no una garantía |
| Plan mode | Que **nada** se edite hasta que apruebes | No se salta: bloquea las ediciones |
| Tus reglas de `settings.json` | Qué está permitido, decida lo que decida | No se salta: `deny` bloquea en todos los modos |

Al aprobar un plan eliges cómo seguir, y una de las opciones deja la sesión
trabajando sin pedirte permiso en cada paso. Ahí sigue mandando lo que escribiste
en la sesión 4:

- Lo que está en `deny` **no se ejecuta**, en ningún modo.
- Lo que está en `ask` **te pregunta**, aunque todo lo demás pase sin consultarte.
- El resto lo revisa un modelo distinto, que bloquea lo que se sale de lo pedido.

Esa opción depende de tu modelo y de la política de tu organización. Si no
aparece, aprueba revisando cada edición: el laboratorio funciona igual y
aprobarás más veces.

## Configuración o Procedimiento

Ya separaste una instrucción de un permiso. Ahora separas la configuración del
procedimiento, y el criterio es si la decisión **cambia según el caso**.

| Decisión | Dónde va | Por qué |
|---|---|---|
| El prefijo del mensaje de commit | La skill | Depende de qué cambió: `feat:`, `test:`, `chore:` |
| Cómo se agrupan los archivos | La skill | Depende del cambio que tengas delante |
| No firmar los commits con la coautoría de Claude | `settings.json` | Es fija: vale para todos los commits, los haga una skill o no |

La coautoría se controla con el bloque `attribution`, y sus dos claves son
**cadenas de texto**, no `true` ni `false`. La cadena vacía oculta la línea:

```json
{
  "attribution": {
    "commit": "",
    "pr": ""
  }
}
```

Existe un campo antiguo que todavía funciona y hace algo parecido. Si Claude te
lo propone, pídele el vigente.

## Conventional Commits

La convención entró en la sesión 4, y hoy cambia quién la aplica: la pides una
vez dentro de la skill del Lab 04 y deja de aparecer en cada encargo. Los
prefijos y el criterio para elegirlos están en la
[referencia rápida de la sesión 4](../sesion-04-ejecutar-y-publicar/referencia-rapida.md).

Lo único que añade esta sesión: el prefijo describe **lo que hace el commit**, no
el tipo de archivo que toca. Una migración y su prueba pueden ir en el mismo
`feat:` si son la misma decisión.

## Un Plan Utilizable

Lo que tu skill del Lab 02 tiene que producir, y lo que revisas antes de
aprobarlo:

| Debe tener | Señal de que falta |
|---|---|
| Incrementos numerados | Una lista de tareas sin orden ni dependencia |
| Una comprobación ejecutable por incremento | "Verificar que funciona" |
| Todas las decisiones tomadas | "Se propone", "se podría", "se confirmará más adelante" |
| El alcance del contrato y nada más | Aparece algo que no está en la sección que planificas |
| Lo que queda fuera, escrito | No hay sección de fuera de alcance |

Una decisión aplazada es una decisión que va a tomar Claude cuando llegue el
incremento. La tomará razonablemente y no te avisará.

## Entregar

| Sección de la descripción | Qué responde |
|---|---|
| Qué cambia | Dos o tres frases, sin listar archivos: eso ya lo dice el diff |
| Qué decisión se tomó y por qué | Lo que no se deduce leyendo el código |
| Cómo se comprueba | Los comandos exactos que ejecutaría otra persona |
| Qué queda sin probar | Lo que nadie escribe y todos necesitan |

En esta sesión hay una respuesta concreta para la última: el `409` al borrar un
proyecto con tareas no se puede comprobar, porque las tareas todavía no existen.

Una rama integrada **se borra**. En tres semanas, una rama abierta que ya está
en `main` no se distingue de trabajo pendiente.

## Si Algo Falla

| Señal | Causa habitual |
|---|---|
| `GET /states` responde `200` con una lista vacía | Las migraciones no están aplicadas. La suite las revierte al terminar |
| `/skills` no muestra tu skill | El directorio no existía al arrancar la sesión: `/reload-skills`, y si no, salir y volver a entrar |
| Claude confirma sin enseñarte el reparto | A la skill le falta esperar tu aprobación, y `git commit` está en tu `allow` |
| Un commit del reparto deja la suite en rojo | El orden está mal: la prueba llegó antes que el código, o el modelo antes que la migración |
| La skill empieza a implementar cuando solo debía planificar | Le falta el límite escrito. Corrige el archivo, no el resultado |
| El plan sale con decisiones en condicional | Corrige la skill, no solo este plan |
