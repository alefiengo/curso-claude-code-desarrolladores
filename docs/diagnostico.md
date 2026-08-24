# Diagnóstico Inicial y Tarea de Transferencia

Estas actividades no llevan nota. Sirven para medir si el curso cambia la forma
de trabajar, no solo el conocimiento de comandos.

El diagnóstico se realiza antes de la primera sesión y la transferencia junto al
proyecto final. No consumen las 20 horas de clases en vivo.

## Diagnóstico Inicial — 35 Minutos

Trabajas sobre un repositorio pequeño que no has visto, con un reporte de bug y
una suite parcialmente verde. Puedes usar Claude Code.

Lo recibes en el momento de la actividad: un módulo, su suite y un reporte que
describe síntomas, sin nombrar el archivo ni la causa. No hace falta instalar
nada más que `pytest`.

Entrega:

- prompt inicial;
- diff final o intento;
- comandos ejecutados;
- una frase: "considero terminado porque…".

Nadie interviene mientras trabajas. Lo que queda registrado:

- tiempo hasta la primera comprobación;
- si se reprodujo antes de editar;
- archivos fuera de alcance;
- si se revisó el diff;
- calidad del criterio de finalización.

Ninguno de esos cinco puntos lleva nota. Son los mismos que vas a comparar
contigo mismo al terminar el curso.

## Tarea de Transferencia — 45 Minutos

Al finalizar la sesión 10, recibe un repositorio y bug diferentes pero de
complejidad equivalente. Debes producir:

- reformulación con alcance y criterio;
- reproducción roja;
- plan breve cuando el cambio sea multiarchivo;
- corrección o diagnóstico de bloqueo;
- evidencia y handoff.

No se exige terminar a cualquier coste. Un bloqueo demostrado y acotado es mejor
que una afirmación sin evidencia.

## Comparación

Se comparan conductas, no líneas de código ni longitud de prompts:

| Indicador | Inicial | Final |
|---|---:|---:|
| Minutos hasta primera verificación | | |
| Reproducción antes de editar | | |
| Cambios fuera de alcance | | |
| Oráculo independiente | | |
| Diff revisado | | |
| Handoff reproducible | | |

Los dos repositorios tienen dificultad equivalente —mismo tamaño, misma
cantidad de tests, misma naturaleza del defecto y la misma corrección mínima— y
no siempre se entregan en el mismo orden: la comparación mide tu forma de
trabajar, no cuál de los dos te tocó primero.

Si una fila empeora, no es un mal resultado por sí sola. Léela junto a las demás:
tardar más en la primera verificación mientras sube "reproducción antes de
editar" suele significar que dejaste de adivinar.
