# Desafío Opcional — Sesión 6

## La Migración que Sí Cambió Algo

En el Lab 02 provocaste el desajuste entre `/rewind` y tu base de datos con
una migración vacía, y lo arreglaste con `alembic stamp` porque no había
nada real que deshacer. Este desafío quita esa red de seguridad: provoca el
mismo desajuste con una migración que **sí** cambia el esquema, y encuentra
una salida sin recrear el volumen de la base de datos.

Este desafío no se entrega y no hace falta para seguir el curso. Se registra
como experimento: no hay un único camino correcto, y cualquier salida que
funcione y que puedas explicar cuenta como resultado válido.

## Por qué importa

`alembic stamp` marca un número, no deshace una columna. Si la migración que
rebobinaste sí creó algo —una tabla, una columna, un índice—, ese algo sigue
en tu base de datos después del `stamp`, sin ningún archivo que lo explique.
Es el caso real: el que provocaste en el Lab 02 fue el más simple posible a
propósito, para que pudieras ver el mecanismo sin arriesgar nada. Este es el
que de verdad te vas a encontrar en un proyecto con datos.

## Antes de empezar

Trabaja en una rama nueva, desechable, y sobre un cambio que no te importe
perder: una tabla o una columna que inventes solo para este experimento, no
sobre nada del contrato. Si al final decides que la única salida razonable es
recrear el volumen, puedes hacerlo —pero hazlo tú mismo, fuera de lo que le
pides a Claude, y solo después de haber intentado lo demás.

## Qué hacer

1. **Provoca el desajuste con una migración real.** Pide una que cree algo
   concreto —una tabla de prueba, por ejemplo— y aplícala. Anota la revisión
   anterior. Rebobina a un punto antes de esa migración, igual que en el
   Lab 02.

2. **Confirma que `stamp` no basta.** Marca la tabla de control con la
   revisión anterior. Después comprueba si lo que creó la migración —la
   tabla o la columna— sigue existiendo en la base de datos, aunque ya no
   haya ningún archivo que la declare.

3. **Busca una salida.** Dos direcciones posibles, sin que ninguna sea la
   única:
   - Escribir una migración nueva cuyo `upgrade` no haga nada, pero cuyo
     `downgrade` sepa deshacer lo que la migración perdida dejó atrás —una
     migración que reconoce el estado real en vez de suponerlo.
   - Deshacer el cambio a mano, con una sentencia SQL directa, y después
     marcar la tabla de control en la revisión que corresponda.

   Investiga cuál te convence más, y por qué. Puedes pedirle a Claude que te
   explique las dos antes de elegir.

4. **Deja el repositorio limpio.** Al final, `alembic current` tiene que
   coincidir con el archivo más reciente que existe, y la base de datos no
   debe tener nada que ningún archivo explique.

## Cómo saber si salió bien

- Reprodujiste el desajuste con una migración que cambia el esquema de
  verdad, no una vacía.
- Sabes decir por qué `alembic stamp` no bastó esta vez, con la diferencia
  concreta frente al Lab 02.
- Intentaste al menos una de las dos salidas del paso 3 antes de recurrir a
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
