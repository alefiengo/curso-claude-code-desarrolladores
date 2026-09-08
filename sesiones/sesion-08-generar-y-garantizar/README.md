# Sesión 8: Generar y Garantizar

## Objetivo

Dejar que el código describa el sistema —la especificación de la API, el
diagrama y el diccionario de la base de datos— en vez de escribirlo a mano, y
configurar los dos hooks que impiden que esa descripción envejezca en
silencio.

El problema profesional de hoy: **una descripción escrita a mano envejece sin
avisar**, y una convención escrita persuade pero no obliga.

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — Lo que la especificación no promete](labs/01-lo-que-la-especificacion-no-promete/README.md) | 30 |
| [Lab 02 — La descripción que se genera sola](labs/02-la-descripcion-que-se-genera-sola/README.md) | 25 |
| [Lab 03 — El guardarraíl que no se negocia](labs/03-el-guardarrail/README.md) | 25 |
| [Lab 04 — Después no es antes](labs/04-despues-no-es-antes/README.md) | 25 |
| Cierre y decisión transferible | 15 |

## Materiales

- Tu repositorio `~/curso-claude/curso-claude-code-api`, con `main` en verde:
  el contrato completo desde la sesión 6, y de la sesión 7 las tres reglas de
  `.claude/rules/`, `api.http` y el `README.md` reescrito.
- Docker arrancado. Los contenedores los levanta Claude.
- `docs/contrato-api.md`, completo. Hoy se compara entero contra lo que el
  código genera.
- La [referencia rápida](referencia-rapida.md) de la sesión, con la tabla de
  qué capa sirve para qué.

Sigues sin teclear los comandos del proyecto. `uv`, `docker`, `alembic`,
`pytest`, `git` y la CLI de tu proveedor los ejecuta Claude, y tú lees lo que
informa.

## Laboratorios

| Lab | Qué haces | Qué descubres |
|---|---|---|
| [01 — Lo que la especificación no promete](labs/01-lo-que-la-especificacion-no-promete/README.md) | Exportas la especificación OpenAPI y la confrontas con el contrato, clasificando cada diferencia | Que una especificación generada describe la forma pero no puede prometer garantías, y que por eso no reemplaza al contrato |
| [02 — La descripción que se genera sola](labs/02-la-descripcion-que-se-genera-sola/README.md) | Construyes una skill que produce el diagrama y el diccionario de datos desde los modelos y las migraciones | Que la documentación que se regenera no se corrige: se corrige el procedimiento que la produce |
| [03 — El guardarraíl que no se negocia](labs/03-el-guardarrail/README.md) | Configuras un hook que bloquea el commit cuando la especificación quedó desincronizada, y lo pruebas en los dos sentidos | Que un permiso no puede depender del resultado de una comprobación, y ahí es donde empieza un hook |
| [04 — Después no es antes](labs/04-despues-no-es-antes/README.md) | Añades un segundo hook, en el evento que actúa cuando la herramienta ya terminó | Que "después" no es una variante de "antes": ese evento puede avisar, ejecutar y registrar, pero no puede impedir |

## Al finalizar esta sesión podrás

- Distinguir lo que una especificación generada puede describir de lo que solo
  un contrato escrito puede prometer.
- Decidir cuál de dos documentos está mal cuando discrepan, en vez de tirar
  uno.
- Escribir una skill que genere documentación derivada del código, y
  corregirla cuando su resultado no sirve.
- Explicar por qué una condición que depende de una comprobación no cabe en
  una regla de permisos.
- Configurar un hook que bloquea y otro que solo reacciona, y probar cada uno
  con su caso positivo y su caso negativo.
- Decir dónde termina el alcance de un hook de Claude Code.

## Conceptos Clave

**Una especificación generada describe la forma; un contrato escrito guarda
las garantías.** El framework sabe declarar qué campos devuelve cada ruta y
con qué tipo, y eso lo hace mejor que tú porque lo lee del código. Lo que no
puede declarar es que dos llamadas idénticas devuelvan los elementos en el
mismo orden: eso es una promesa entre llamadas, y una especificación describe
respuestas de una en una. Con el formato de una fecha pasa algo más fino:
puede restringir la forma de la cadena, pero no obliga a nadie a cumplirla
—describe, no ejecuta—. Cuando los dos documentos discrepan, la pregunta no
es cuál sobra, es cuál de los dos está mal.

**La documentación derivada no se corrige a mano; se corrige su
procedimiento.** Un diagrama de tablas y un diccionario de columnas salen de
los modelos y de las migraciones, así que arreglar el archivo generado dura
hasta la siguiente migración. Lo que se arregla es la skill que lo produce, y
eso es lo mismo que ya hiciste en la sesión 7 con la skill de reparto: el
fallo estaba en el procedimiento, no en su resultado de aquel día.

**Cuatro capas de control, y cada una decide en un momento distinto.** Una
instrucción de `CLAUDE.md` orienta y puede omitirse. Una regla de
`.claude/rules/` fija una convención, pero sigue siendo contexto. Un permiso decide **antes**, por
herramienta y por argumento, y no sabe nada de resultados. Un hook ejecuta
código tuyo en un evento del ciclo de vida, así que es la única capa que puede
decir "solo si esta comprobación pasa". La escalera no va de débil a fuerte
por gusto: va de lo que persuade a lo que se ejecuta pase lo que pase. Una
skill no es una de estas capas: fija un procedimiento, no decide si algo
puede ocurrir.

**"Antes" y "después" no son dos sabores del mismo evento.** El evento que se
dispara antes de una herramienta puede impedir que se ejecute. El que se
dispara después llega cuando el archivo ya está escrito o el comando ya
corrió: puede avisar, puede lanzar otra cosa, puede dejar constancia, y no
puede deshacer. Elegir mal el evento produce el peor resultado posible: la
sensación de tener un guardarraíl donde solo hay un aviso.

## Comandos Nuevos

| Comando o control | Uso |
|---|---|
| `/hooks` | Visor de los hooks configurados: evento, filtro, tipo y desde qué archivo se cargó. No configura nada |

Los hooks se escriben en `.claude/settings.json`, el mismo archivo donde
versionaste los permisos en la sesión 4. `/hooks` sirve para comprobar que
cargaron, igual que `/skills` con las skills.

`/permissions` apareció en la sesión 4 y hoy vuelve con una pregunta
distinta: no qué autorizar, sino qué **no** se puede expresar como permiso.
`/skills`, `/diff` y `/context` ya aparecieron; hoy `/skills` confirma una
skill nueva, `/diff` revisa lo que un hook regeneró sin pedírtelo, y
`/context` cierra cada lab.

## Validación General

Pídele a Claude la comprobación completa y léela entera antes de marcar nada:

```text
Comprueba el estado del proyecto y dame el resultado de cada punto por separado,
sin corregir nada:

1. La rama actual y si el árbol de trabajo está limpio.
2. Los commits de main que no estaban antes de hoy, uno por línea.
3. Si openapi.json está confirmado y si coincide con la especificación que
   genera el código ahora mismo.
4. Si el README.md dice con qué comando se regenera la especificación.
5. Cuántas tablas y columnas describe docs/esquema.md, y si coinciden con las
   que crean las migraciones.
6. Qué skills de proyecto hay, y si describir-esquema declara su límite.
7. Qué hooks hay configurados, con su evento, su filtro y su archivo de
   origen.
8. uv run pytest -q y uv run ruff check .
9. Si queda alguna rama sin integrar.

Si algo falla, dime qué falló y detente. No lo arregles.
```

La sesión está completa si:

- [ ] `openapi.json` está en `main`, y regenerarlo no produce diferencias.
- [ ] `docs/esquema.md` describe todas las tablas y columnas que crean las migraciones, sin repetir el contrato.
- [ ] La skill que lo genera está versionada y declara que describe y no modifica.
- [ ] Los dos hooks están en `.claude/settings.json`, en eventos distintos, y `/hooks` los muestra.
- [ ] Con la especificación desincronizada, un commit no ocurre; con la especificación al día, sí.
- [ ] Comprobaste con `git diff` que el hook de después no pudo impedir una edición.
- [ ] Sabes decir qué promete el contrato que la especificación no puede expresar.
- [ ] Ningún cambio de prueba quedó en `main`.

## Limpieza

Detén los contenedores sin eliminar volúmenes, igual que en las sesiones
anteriores. Los dos hooks se quedan configurados: son parte del repositorio a
partir de hoy, y la sesión 10 los va a necesitar.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) te pide llevar la
comprobación del commit al otro extremo: un evento que vigila el disco en vez
del ciclo de vida de una herramienta, y decidir cuál de los dos te sirve más.

## Cierre

Preguntas de repaso:

- ¿Qué encontró el Lab 01 que el contrato promete y la especificación no puede expresar?
- ¿Hubo alguna diferencia donde uno de los dos documentos estaba mal? ¿Cuál corregiste y por qué ese y no el otro?
- ¿Por qué la comprobación del commit no cabe en una regla de permisos?
- ¿Qué comprobaste exactamente para saber que el segundo hook no puede impedir nada?
- Si mañana alguien añade una columna sin regenerar nada, ¿qué se lo dice, y en qué momento?

## Versión

Material revisado el **8 de septiembre de 2026** con Claude Code **2.1.263**
y la documentación oficial de hooks. Comprueba tu versión con
`claude --version` y la disponibilidad local con `/help`.

- [Referencia de hooks](https://code.claude.com/docs/en/hooks)
- [Guía de hooks](https://code.claude.com/docs/en/hooks-guide)

## Estado Final del Repositorio

La sesión 9 parte exactamente de aquí.

En `~/curso-claude/curso-claude-code-api`, con `main` en verde y sin ramas
abiertas:

| Ruta | Origen |
|---|---|
| `openapi.json`, y la línea que lo regenera en el `README.md` | Lab 01 |
| `docs/esquema.md`, con diagrama y diccionario de datos | Lo genera la skill en el Lab 02 |
| `.claude/skills/describir-esquema/SKILL.md` | Lab 02 |
| `.claude/settings.json`, con dos hooks en eventos distintos | Labs 03 y 04 |
| El contrato o el código, si alguna diferencia del grupo 3 obligó a corregir | Decisión del Lab 01 |

El contrato de la API sigue siendo el de la sesión 6: hoy no se añade
ninguna capacidad. Lo que cambia es que la descripción del sistema ya no
depende de que alguien se acuerde de actualizarla.

## Preparación para la Sesión 9

Antes de la clase:

- Deja `main` en verde, con los dos hooks configurados y funcionando.
- Actualiza tu copia del material:

```bash
cd $CURSO && git pull
```
