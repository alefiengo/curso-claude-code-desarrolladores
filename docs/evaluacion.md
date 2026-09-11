# Evaluación

La calificación del curso son dos cifras:

| Qué | Peso |
|---|---:|
| Cuestionario final sobre Claude Code | 80 % |
| Asistencia a las sesiones en vivo | 20 % |

Nada más entra en la nota. El trabajo de los laboratorios no se califica: se
comprueba contra la validación de cada sesión, y su valor es que te deja
preparado para el cuestionario.

El [diagnóstico inicial y la tarea de transferencia](diagnostico.md) tampoco
llevan nota: sirven para comparar conductas antes y después.

## Cuestionario Final

Se publica al terminar la última sesión, y tienes **24 horas desde su
publicación** para responderlo.

Cubre Claude Code: lo que practicaste durante las diez sesiones. No es un examen
de sintaxis ni de memoria de comandos —para eso está
[el mapa de comandos](comandos.md), y puedes consultarlo—, sino de las
decisiones que el curso trabaja: qué pieza resuelve qué problema, cuándo elegir
una y no otra, y qué se puede afirmar con la evidencia que deja cada una.

No se entrega el repositorio ni ningún documento junto al cuestionario. Tu
repositorio es la preparación, no el entregable: si dirigiste tú las diez
sesiones, ya tienes las respuestas.

Para prepararlo, el material que más rinde es el cierre de cada sesión —sus
preguntas de repaso—, la referencia rápida de cada una y
[el glosario](glosario.md).

## Evidencia por Sesión

Tu evidencia es el repositorio, no un informe aparte. Cada sesión la deja escrita
sola: los commits separan los incrementos, los tests fijan el comportamiento, el
diff muestra el alcance y las salidas que guardas quedan versionadas donde el lab
te las pide.

Lo único que Git no guarda por ti son dos respuestas, y las cierra cada sesión:

- qué decidiste y qué observaste para decidirlo;
- qué sigue sin estar probado.

Nadie espera que Claude te haya dado la misma solución que a los demás. Lo que
cuenta es que tu decisión y tu evidencia se sostengan.

## Autocomprobación

Esta tabla no se entrega y no se califica. Sirve para que te ubiques mientras
avanza el curso, y para saber qué repasar antes del cuestionario.

| Dimensión | Aún no | Competente | Sólido |
|---|---|---|---|
| Especificación | Petición vaga | Alcance y aceptación claros | Riesgos, límites y casos borde explícitos |
| Contexto | Carga indiscriminada | Selecciona fuentes relevantes | Mide, poda y justifica lo cargado |
| Verificación | Confía en la respuesta | Ejecuta una comprobación pertinente | Comprobaciones independientes y en varias capas |
| Control humano | Acepta el resultado | Revisa plan y diff | Detecta una decisión débil y la corrige |
| Autoridad y permisos | Permisos amplios o secretos expuestos | Mínimo privilegio, con una prueba negativa | Elige la capa que decide cada cosa —instrucción, regla, permiso o hook— y acota la autoridad de lo que delega |
| Recuperación | No hay punto de retorno | Rama o checkpoint recuperable | Demuestra rollback y reanudación |
| Comunicación | Enumera cambios | Explica evidencia y límites | Permite reproducir y auditar la decisión |

Al terminar el curso deberías reconocerte en **Competente** en todas las
dimensiones, y en **Sólido** al menos en verificación, control humano y una más.
