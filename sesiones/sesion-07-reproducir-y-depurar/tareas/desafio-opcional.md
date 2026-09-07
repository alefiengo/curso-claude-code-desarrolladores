# Desafío Opcional — Sesión 7

## La Captura que no Se Puede Repetir

En el Lab 03 dejaste `api.http`: una colección de peticiones que cualquiera
puede volver a ejecutar contra la API, hoy o dentro de un mes. Este desafío
te pide comparar esa evidencia contra la que probablemente ya usaste antes
en tu vida profesional —una captura de pantalla— y decidir cuál de las dos
sobrevive a la pregunta que te van a hacer después.

Este desafío no se entrega y no hace falta para seguir el curso. Se registra
como experimento: no hay un único camino correcto, y cualquier conclusión
que puedas explicar cuenta como resultado válido.

## Por qué importa

Una captura de pantalla prueba que, en el momento en que la tomaste, algo
respondió lo que muestra la imagen. No prueba nada sobre ahora. Si alguien
te pregunta "¿sigue funcionando así?", la captura no puede contestar: solo
tú, ejecutándolo otra vez, puedes. `api.http` sí puede contestar solo,
porque es instrucciones ejecutables, no una fotografía de un resultado.

## Antes de empezar

No necesitas nada nuevo: trabajas sobre `main`, ya con `api.http` integrado
desde el Lab 03.

## Qué hacer

1. **Toma la captura.** Ejecuta contra la API corriendo la petición de
   `api.http` que prefieras —por ejemplo, crear un proyecto—, y guarda una
   captura de pantalla de la respuesta completa: cuerpo y código de estado.

2. **Deja pasar el tiempo, aunque sea simulado.** Pídele a Claude que
   cambie algo pequeño y real en el endpoint que capturaste —un campo que
   se serializa distinto, un código de estado que cambia en un caso
   límite— y que lo confirme en un commit, sin tocar `api.http` todavía.

3. **Pregúntale a cada evidencia lo mismo.** Con la captura delante, sin
   ejecutar nada: ¿sigue siendo cierta la respuesta que muestra? No hay
   forma de saberlo mirándola. Ahora ejecuta la petición correspondiente de
   `api.http` contra la API real: la respuesta te dice, hoy, si el cambio
   rompió algo.

4. **Decide qué falta.** Si `api.http` detectó el cambio, ¿qué le faltaría
   a la captura para poder decir lo mismo? Si no lo detectó, ¿por qué no
   —la petición no cubría ese caso, o el cambio no afectaba lo que prueba—?

5. **Deja el repositorio limpio.** Revierte el cambio del paso 2 si no
   quieres conservarlo, o corrige `api.http` para que sí lo hubiera
   detectado y confírmalo en su propio commit.

## Cómo saber si salió bien

- Tienes una captura y una ejecución real de la misma petición, separadas
  por un cambio real de por medio.
- Puedes decir, con el caso delante, qué pregunta responde cada una y cuál
  no.
- Si `api.http` no detectó el cambio, sabes exactamente qué le faltaba para
  detectarlo, y decidiste si vale la pena agregarlo.

## Si Te Atascas

| Situación | Qué hacer |
|---|---|
| No se te ocurre un cambio pequeño y real que hacer | Pídele a Claude tres candidatos: un campo que cambia de formato, un código de estado distinto en un caso límite, un orden que deja de ser estable. Elige el que más te sorprenda |
| `api.http` detectó el cambio a la primera | Es el resultado esperado: es la razón por la que existe. Anota qué habría pasado si solo tuvieras la captura |
| Te cuesta ver la diferencia entre las dos evidencias | Pregúntate quién puede usar cada una sin ti delante: la captura solo la interpretas tú, mirándola; `api.http` lo ejecuta cualquiera, incluida una máquina |
