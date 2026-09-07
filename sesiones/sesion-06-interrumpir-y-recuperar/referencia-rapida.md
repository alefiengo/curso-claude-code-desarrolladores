# Referencia Rápida — Sesión 6

## Comandos de la Sesión

| Comando o control | Qué hace | Dónde lo usas |
|---|---|---|
| `/rewind` | Abre el selector de puntos anteriores de la conversación y el código | Lab 02 |
| `Esc Esc` | Abre el mismo selector, con el campo de texto vacío | Lab 02 |
| `Esc` | Interrumpe el turno en curso | En cuanto veas una desviación |
| `/resume` | Retoma una conversación anterior de este directorio, con su historial completo | Lab 03 |
| `--continue` | Retoma la conversación más reciente de este directorio, sin selector | Lab 03 |
| `/rename` | Pone nombre a la sesión actual | Lab 03 |
| `/branch` | Copia la conversación hasta este punto y cambia a la copia, dejando la original intacta | Referencia |
| `/fork` | Copia la conversación en una sesión nueva, en segundo plano, y tú sigues en esta | Referencia |
| `/clear` | Vacía el contexto de la conversación, sin perder el archivo de la sesión | Lab 03, para simular retomar sin contexto |
| `/diff` | Revisa los cambios antes de confirmar | Lab 02 |
| `/context` | Muestra qué ocupa la ventana de contexto | Al cerrar la sesión |

Ni `/branch` ni `/fork` se usan hoy con hands-on, pero conviene distinguirlos:
`/branch` te cambia a la copia y sigues ahí; `/fork` deja la copia trabajando
en segundo plano mientras tú sigues en la conversación original. Los dos
sirven para probar un camino distinto sin arriesgar el que ya tienes,
planificados **antes** de un cambio riesgoso, no después.

## Qué Revierte `/rewind`, y Qué No

| Revierte | No revierte |
|---|---|
| Archivos que Claude editó con su herramienta de archivos | Archivos que un comando de shell modificó —`rm`, `mv`, `cp`, y cualquier redirección— |
| La conversación, hasta el punto que elijas | Un `git commit` ya confirmado sigue en tu historial de Git. Si eliges un punto anterior a ese commit, tu árbol de trabajo puede dejar de coincidir con él —`/rewind` no lo deshace, pero tampoco lo respeta— |
| — | Cualquier efecto de un comando ejecutado: una migración aplicada, un archivo publicado, un correo enviado |

La regla corta: si Claude lo hizo con su herramienta de edición de archivos,
`/rewind` puede deshacerlo. Si lo hizo ejecutando algo, no.

Restaurar código y conversación son dos opciones separadas en el selector.
Puedes rebobinar solo la conversación y dejar el código como está, o al
revés.

## El Desajuste de una Migración

Cuando rebobinas a un punto anterior a que Claude creara y aplicara una
migración:

1. El archivo de la migración sigue en tu repositorio, sin trackear —lo creó
   un comando, `alembic revision`, y eso `/rewind` no lo toca.
2. La base de datos sigue exactamente donde la dejó el comando
   `alembic upgrade head` —tampoco era una edición de archivo.
3. `alembic current` resuelve sin error: el archivo y la marca de la base de
   datos siguen coincidiendo entre sí. Lo que cambió es que la conversación ya
   no recuerda haber creado ni aplicado nada de eso.

El desajuste no es entre el archivo y la base de datos: los dos sobreviven
juntos. Es entre lo que tu conversación cree que pasó y lo que tu repositorio
y tu base de datos todavía tienen.

| Comando | Para qué |
|---|---|
| `alembic current` | Ver qué revisión cree la base de datos que tiene |
| `alembic downgrade <revisión>` | Deshacer una migración de verdad, ejecutando su función de bajada —solo funciona si el archivo todavía existe |
| `alembic stamp <revisión>` | Marcar la tabla de control con esa revisión, **sin ejecutar ningún cambio de esquema** |

Mientras el archivo siga ahí, `downgrade` es la recuperación normal: baja el
cambio y puedes borrar el archivo después. `stamp` solo entra cuando el
archivo de verdad ya no existe —porque lo borraste tú, no porque lo haya
borrado `/rewind`— y por eso no puede deshacer ningún cambio de esquema real:
solo corrige el número que la base de datos cree tener.

## `/resume` No Es un Traspaso

| | `/resume` o `--continue` | Traspaso escrito |
|---|---|---|
| Quién puede usarlo | Tú, en esta máquina | Cualquiera con el repositorio |
| Qué trae | La conversación entera, con cada herramienta ejecutada | Solo lo que quedó en commits, PRs y documentación |
| Cuándo deja de servir | Si borras la sesión, cambias de máquina, o pasa el tiempo de retención | Nunca, mientras el repositorio exista |

La prueba de si tu traspaso funciona no es preguntarte a ti mismo: es
preguntarle a una conversación que nunca vivió lo que tú viviste, y ver si
puede responder con lo que hay escrito.

## Si Algo Falla

| Señal | Causa habitual |
|---|---|
| El selector de `/rewind` no muestra el punto que buscas | Lista tus mensajes, no los de Claude. Busca el encargo que diste tú, no la respuesta |
| `alembic current` no muestra ningún error tras rebobinar | Es lo esperado: ahí no vas a ver el desajuste. Compara contra lo que dice la conversación cuando le preguntas por esa migración |
| `alembic downgrade` falla o no encuentra la revisión | Revisa que el identificador es el anterior a la migración que rebobinaste, completo y sin espacios, y que el archivo de esa migración sigue en `alembic/versions/` |
| `claude --resume <nombre>` no encuentra la sesión | El nombre se puso con `/rename` dentro de la conversación; sin ese paso, retómala por la lista |
| Después de `/clear`, la respuesta parece "recordar" la conversación | Está leyéndolo del repositorio, no de tu memoria de hoy. Comprueba de dónde lo saca |
