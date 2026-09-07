# Desafío Opcional — Sesión 6

## Cuando el Archivo Sí Desaparece

En el Lab 02 rebobinaste una migración vacía y descubriste que el archivo
seguía en tu repositorio, sin trackear: `/rewind` solo le borró la memoria a
la conversación, no el archivo ni el cambio en la base de datos. Con eso
delante, es tentador pensar que un archivo huérfano que la conversación ni
menciona no sirve de nada, y borrarlo tú mismo. Este desafío prueba qué pasa
cuando de verdad lo haces —con una migración que sí cambia el esquema, no una
vacía—.

Este desafío no se entrega y no hace falta para seguir el curso. Se registra
como experimento: no hay un único camino correcto, y cualquier salida que
funcione y que puedas explicar cuenta como resultado válido.

## Por qué importa

Mientras el archivo de la migración exista, `downgrade` la deshace de la
forma normal, la hayas rebobinado o no. El riesgo real no es `/rewind`: es
borrar tú mismo un archivo que ya no aparece en la conversación, sin
comprobar antes si la base de datos todavía depende de él. Cuando eso pasa,
`alembic stamp` marca un número, pero no deshace una columna: si la migración
que perdiste creó algo —una tabla, una columna, un índice—, ese algo sigue en
tu base de datos, sin ningún archivo que lo explique.

## Antes de empezar

Trabaja en una rama nueva, desechable, y sobre un cambio que no te importe
perder: una tabla o una columna que inventes solo para este experimento, no
sobre nada del contrato. Si al final decides que la única salida razonable es
recrear el volumen, puedes hacerlo —pero hazlo tú mismo, fuera de lo que le
pides a Claude, y solo después de haber intentado lo demás.

## Qué hacer

1. **Provoca el desajuste con una migración real.** Pide una que cree algo
   concreto —una tabla de prueba, por ejemplo— y aplícala. Anota el
   identificador de la revisión anterior. Rebobina a un punto antes de esa
   migración, igual que en el Lab 02, y confirma con `git status` que el
   archivo sigue ahí, sin trackear.

2. **Pierde el archivo de verdad.** Bórralo tú mismo, fuera de lo que le
   pides a Claude —es la parte que `/rewind` no hizo por ti—. Ahora sí falta
   el archivo, pero la tabla o columna que creó sigue en la base de datos.

3. **Confirma que `stamp` no basta.** Marca la tabla de control con la
   revisión anterior. Después comprueba, directamente contra la base de
   datos y no contra Alembic, si lo que creó la migración sigue existiendo.

4. **Busca una salida.** Dos direcciones posibles, sin que ninguna sea la
   única:
   - Escribir una migración nueva cuyo `upgrade` no haga nada, pero cuyo
     `downgrade` sepa deshacer lo que la migración perdida dejó atrás —una
     migración que reconoce el estado real en vez de suponerlo.
   - Deshacer el cambio a mano, con una sentencia SQL directa, y después
     marcar la tabla de control en la revisión que corresponda.

   Investiga cuál te convence más, y por qué. Puedes pedirle a Claude que te
   explique las dos antes de elegir.

5. **Deja el repositorio limpio.** Al final, `alembic current` tiene que
   coincidir con el archivo más reciente que existe, y la base de datos no
   debe tener nada que ningún archivo explique.

## Cómo saber si salió bien

- Reprodujiste el desajuste con una migración que cambia el esquema de
  verdad, no una vacía, y con el archivo realmente ausente —no solo sin
  trackear, como en el Lab 02.
- Sabes decir por qué `alembic stamp` no bastó esta vez, con la diferencia
  concreta frente al Lab 02.
- Intentaste al menos una de las dos salidas del paso 4 antes de recurrir a
  recrear el volumen.
- Puedes explicar, en dos o tres frases, qué camino elegiste y por qué el
  otro te convencía menos —incluido, si terminaste ahí, por qué recrear el
  volumen fue la salida más barata esta vez.

## Si Te Atascas

| Situación | Qué hacer |
|---|---|
| No sabes cómo pedirle a Claude una migración que cree algo concreto | Pídele una tabla de una sola columna, sin relaciones con nada del contrato. Cuanto más aislada, menos arriesgas |
| Después de `stamp`, todo parece estar bien | Comprueba directamente contra la base de datos, no contra Alembic: pídele que liste las tablas o columnas existentes y las compare con lo que hay en `alembic/versions/` |
| Las dos salidas del paso 3 te parecen igual de válidas | Es un resultado razonable. Anota cuál habrías elegido en un proyecto con datos reales, y por qué cambia la respuesta |
| Terminaste recreando el volumen | No es un fracaso: es información. Anota en qué punto decidiste que las otras salidas costaban más de lo que valían |
