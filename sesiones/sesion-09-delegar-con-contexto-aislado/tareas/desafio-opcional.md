# Desafío Opcional — Sesión 9

## El Quinto que no Construiste

Hoy añadiste cuatro agentes a tu repositorio. Este desafío te pide proponer
un quinto y **no construirlo**, con un argumento que puedas defender; y
comprobar de primera mano qué pasa cuando a un agente no le declaras
herramientas.

Este desafío no se entrega y no hace falta para seguir el curso. Se registra
como experimento: cualquier conclusión que puedas defender cuenta como
resultado válido.

## Por qué importa

Un directorio de agentes crece igual que crece `.claude/skills/`: por
acumulación, porque cada uno parecía buena idea el día que se escribió. La
sesión 10 poda todo eso, y llega mucho más fácil si hoy sabes decir por qué
un agente no debía existir.

Hay un caso que engaña especialmente: el trabajo que **sí** se puede delegar,
pero que se hace mejor con una skill o con un hook. Delegarlo a un subagente
funciona, y aun así es la decisión equivocada.

## Antes de empezar

Trabaja en una rama nueva y desechable. Vas a crear un archivo de agente que
después vas a borrar.

## Qué hacer

1. **Propón tres candidatos.** Pídele a Claude tres trabajos de tu
   repositorio que hoy podrían delegarse a un subagente nuevo, sacados de lo
   que de verdad haces, no de una lista genérica.

2. **Rechaza dos, con la razón exacta.** Para cada uno, decide si le falta
   contexto tuyo —entonces es una skill—, si tiene que ocurrir siempre
   —entonces es un hook—, o si es una línea de comando que ya está en el
   `README.md`. Escribe el motivo en una frase por candidato.

3. **Construye el que sobreviva, si sobrevive alguno.** Puede que ninguno lo
   haga, y esa también es una respuesta. Si construyes uno, decláralo con la
   autoridad mínima de su oficio.

4. **Haz el experimento de la autoridad.** Crea un agente de prueba **sin
   declararle herramientas**, con un oficio cualquiera, y pregúntale qué
   puede hacer. Compáralo con lo que declara el revisor del Lab 02. Después
   bórralo.

5. **Comprueba qué sabe de ti.** Al agente de prueba, antes de borrarlo,
   pregúntale qué archivos de instrucciones cargó y si conoce algo de la
   conversación en la que lo creaste. Anota la respuesta: es la que explica
   por qué el revisor del Lab 02 vale como segunda opinión.

6. **Deja el repositorio como estaba.** Borra lo del experimento y descarta
   la rama. Lo único que puede sobrevivir es el agente del punto 3, si
   decidiste que valía la pena, y entonces va con su commit y su motivo.

## Cómo saber si salió bien

- Tienes dos candidatos rechazados y puedes decir, para cada uno, cuál era la
  herramienta correcta y por qué.
- Viste con tus propios ojos la diferencia entre un agente con herramientas
  declaradas y uno sin ellas.
- Sabes decir qué cargó el agente de prueba al arrancar y qué no.
- El repositorio quedó igual que al empezar, salvo lo que decidiste conservar
  con un motivo escrito.

## Si Te Atascas

| Situación | Qué hacer |
|---|---|
| Los tres candidatos parecen buenos | Pregúntate cuál necesita tu conversación para hacer bien su trabajo. Ese no es un subagente: es una skill |
| El agente sin herramientas dice que puede hacerlo todo | Es lo esperado, y es justo el problema. Compruébalo pidiéndole algo que el revisor no podría hacer |
| No sabes si algo debería ser hook o subagente | Un hook se ejecuta pase lo que pase, en un momento fijo. Un subagente se invoca cuando alguien lo pide. Si la respuesta es "siempre", no es un agente |
| Terminaste sin construir ninguno | Es un resultado válido, y probablemente el más honesto. Escribe por qué en una frase |
