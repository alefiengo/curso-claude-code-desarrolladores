# Desafío Opcional — Sesión 8

## El que Vigila el Disco

Los dos hooks de hoy se disparan por una llamada a herramienta: uno antes,
otro después. Existe otro evento que no mira las herramientas sino el
**disco**: se dispara cuando un archivo cambia, lo haya cambiado Claude o lo
hayas cambiado tú en tu editor. Este desafío te pide montarlo y decidir cuál
de los dos enfoques te sirve más para la descripción del sistema.

Este desafío no se entrega y no hace falta para seguir el curso. Se registra
como experimento: cualquier conclusión que puedas defender cuenta como
resultado válido.

## Por qué importa

El hook del Lab 04 solo ve lo que edita Claude. Si abres el modelo en VS Code
y añades una columna a mano, ese hook no se enteró: la descripción queda
vieja y nada te avisa. Un vigilante de disco sí lo vería. Pero también se
dispara con cada guardado mientras escribes, y eso puede volverse ruido o
trabajo repetido.

No hay una respuesta correcta. Hay una decisión, y depende de cómo trabajes.

## Antes de empezar

Trabaja en una rama nueva y desechable. Vas a tocar
`.claude/settings.json`, así que confirma el estado bueno antes de empezar:
si el experimento deja la configuración rara, quieres poder volver.

## Qué hacer

1. **Averigua el evento.** Pídele a Claude que busque, en la documentación
   oficial de hooks, el evento que se dispara cuando un archivo cambia en
   disco, y que te diga qué recibe y si puede bloquear algo. No lo des por
   sabido: compruébalo contra la página.

2. **Móntalo sobre los mismos archivos.** Configúralo para que vigile los
   archivos de los que sale la especificación, y que haga lo mismo que el
   hook del Lab 04: regenerar `openapi.json`.

3. **Provoca el caso que el otro no ve.** Edita un modelo **tú mismo**, desde
   tu editor, sin pasar por Claude. Comprueba qué hizo cada uno de los dos
   hooks: el del ciclo de vida y el del disco.

4. **Provoca el caso incómodo.** Guarda el archivo tres o cuatro veces
   seguidas mientras escribes, como pasa de verdad al editar. Mira cuántas
   veces se disparó y qué costó eso.

5. **Decide y anótalo.** ¿Te quedas con el del ciclo de vida, con el del
   disco, con los dos, o con ninguno? Escribe el motivo en una frase, en el
   lugar del repositorio que le corresponda, y descarta el resto del
   experimento.

## Cómo saber si salió bien

- Comprobaste contra la documentación qué recibe ese evento y si puede
  bloquear, en vez de suponerlo.
- Viste con tus propios ojos un caso que el hook del Lab 04 no detecta.
- Viste también el coste: cuántas veces se dispara el del disco en una
  edición normal.
- Puedes defender tu decisión en una frase, incluida la opción de no quedarte
  con ninguno de los dos.

## Si Te Atascas

| Situación | Qué hacer |
|---|---|
| No encuentras el evento en la documentación | Pídele a Claude que liste todos los eventos de hook de la página de referencia y que te diga cuáles no dependen de una llamada a herramienta |
| El vigilante de disco se dispara en bucle | Es el riesgo real de este enfoque: si el hook regenera un archivo que también está vigilado, se llama a sí mismo. Acota qué archivos vigila y comprueba si el bucle desaparece |
| Los dos hooks hacen lo mismo dos veces | Es información, no un fallo. Anota si te molesta lo suficiente como para dejar solo uno |
| Terminaste quitando los dos | Es un resultado válido, y conviene decir por qué: puede que la comprobación del commit del Lab 03 ya te dé lo que necesitas, y lo demás sea ruido |
