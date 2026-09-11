# Desafío Opcional — Sesión 9

## El Agente que no Hace Falta

Hoy añadiste tres agentes a tu repositorio. Este desafío te pide proponer
varios candidatos, rechazar los que no se justifiquen y comprobar de primera mano qué pasa cuando a un agente no le declaras
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

2. **Rechaza dos, con la razón exacta.** Para cada uno, decide si encaja mejor en una
   skill con un procedimiento reutilizable, en un hook ligado a un evento, o si es una línea de comando que ya está en el
   `README.md`. Escribe el motivo en una frase por candidato.

3. **Construye el que sobreviva, si sobrevive alguno.** Puede que ninguno lo
   haga, y esa también es una respuesta. Si construyes uno, decláralo con la
   autoridad mínima de su oficio.

4. **Haz el experimento de la autoridad.** Crea un agente de prueba **sin
   declararle herramientas**, con un oficio cualquiera, y pregúntale qué
   puede hacer. Compáralo con lo que declara el auditor del Lab 03. Conserva
   la instancia para el punto siguiente. Comprueba una capacidad con una tarea
   inocua, como ejecutar `git status --short`, y observa la llamada real.

5. **Comprueba qué sabe de ti.** Al agente de prueba, antes de borrarlo,
   pregúntale qué archivos de instrucciones cargó y si conoce algo de la
   conversación en la que lo creaste. Retoma la misma instancia y contrasta
   la respuesta con su encargo y el registro de invocación; su declaración
   por sí sola no prueba qué recibió. Después bórralo.

6. **Deja el repositorio como estaba.** Retira los archivos de prueba.
   Si conservas el agente del punto 3, revisa su diff, confirma solo ese archivo
   e integra la rama con su motivo. Si no conservas nada, vuelve a main y elimina
   la rama desechable una vez comprobado que no contiene trabajo que quieras guardar.

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
| Los tres candidatos parecen buenos | Comprueba si alguno ya queda cubierto por una skill o un encargo puntual; justifica los rechazos sin forzarlos |
| El agente sin herramientas dice que puede hacerlo todo | No tomes su declaración como prueba. Observa una llamada inocua que el auditor no tiene disponible |
| No sabes si algo debería ser hook o subagente | Un hook se ejecuta cuando ocurre su evento y coincide el filtro configurado. Un subagente se invoca cuando alguien lo pide. Si la respuesta es "siempre", no es un agente |
| Terminaste sin construir ninguno | Es un resultado válido, que debes justificar. Escribe por qué en una frase |
