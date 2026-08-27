# Guía del Estudiante

## Qué cubre el curso

El curso avanza en tres bloques:

1. **Controlar la tarea y el contexto:** formular cambios verificables, fundar el
   proyecto y mantener señal durante trabajo largo.
2. **Diseñar, implementar y recuperar:** planificar cambios multiarchivo,
   entregarlos con evidencia y recuperarse de una desviación.
3. **Verificar, extender y automatizar:** depurar, construir herramientas
   reutilizables, acotar permisos y ejecutar sin nadie delante.

Cada sesión deja una decisión transferible y una evidencia revisable. Algunas
hacen crecer la API; otras mejoran las instrucciones o herramientas que la
rodean. El valor no depende de fabricar un artefacto nuevo en cada clase.

## Antes de la primera sesión

Prepara el entorno siguiendo la [guía de instalación](instalacion-entorno.md). Necesitas:

- Claude Code instalado y autenticado. Revisa las opciones de cuenta y las
  capacidades opcionales en la [matriz de compatibilidad](compatibilidad.md).
- Docker funcionando.
- `uv` instalado.
- Git configurado con nombre y correo.
- Una terminal Linux, macOS o WSL 2 con Ubuntu.

Si nunca has usado Claude Code, o solo lo has usado como chat, ejecuta `/powerup`
antes de la primera sesión: abre una serie de lecciones cortas dentro del propio
producto. Está descrito en la [guía de instalación](instalacion-entorno.md).

## Qué necesitas saber de antes

- Manejarte con git y la terminal.
- Dominar al menos un lenguaje de programación.
- Poder leer y depurar Python básico, aunque no sea tu lenguaje principal.

No hace falta experiencia con FastAPI ni PostgreSQL. El curso no enseña Python
desde cero: el código se explica cuando aporta a la decisión, pero debes poder
seguir una función, un test y un traceback.

## Estructura de cada sesión

Cada sesión dura 2 horas y tiene:

- Conceptos clave con ejemplos.
- Laboratorios guiados con validación y limpieza.
- Referencia rápida con los comandos de la sesión.
- Desafío opcional para profundizar fuera del horario de clase.

Los desafíos opcionales no se entregan y no son requisito para avanzar.

## Dedicación Fuera de Clase

Reserva 35 minutos antes de la sesión 1 para el diagnóstico, 45 minutos al final
para la tarea de transferencia y 4–6 horas para el proyecto final. Los desafíos
opcionales añaden 30–45 minutos por sesión si decides realizarlos.

## El proyecto integrador

Construyes tu propio `curso-claude-code-api` a lo largo del curso. El curso no
entrega su implementación: Claude la genera progresivamente bajo los contratos,
tests y revisiones que tú diriges. Algunas sesiones amplían la API y otras
mejoran el proceso con instrucciones y herramientas en `.claude/`.

Es tuyo. Trabajas en tu máquina y en tu repositorio.

Los labs del proyecto son acumulativos. Antes de cada cambio comprueba que partes
de un estado bueno —`main` limpio y en verde—, como explica el
[flujo de trabajo con Git](../proyecto-integrador/flujo-git.md). Si faltas, el
laboratorio de esa sesión y el contrato bastan para recuperarla.

## Evaluación

No hay notas. Cada sesión cierra con una lista de comprobación y una evidencia
breve de proceso. El proyecto final se revisa con una rúbrica formativa. Consulta
[Evaluación y Portafolio](evaluacion.md).

El curso empieza con un [diagnóstico](diagnostico.md) y termina con una tarea
equivalente. Lo que comparas son tus hábitos de trabajo, no tu velocidad
tecleando ni cuánto código escribiste.

Que el cambio funcione es necesario, pero no suficiente. También importa cómo
definiste el resultado, qué evidencia usaste, cómo controlaste el alcance y qué
riesgo dejaste explícito.

## Cuando algo falla

Consulta la [guía de problemas frecuentes](problemas-frecuentes.md) antes de pedir soporte.

Las palabras que el curso usa con un significado preciso —criterio manipulable,
comprobación independiente, handoff, idempotente— están reunidas en el
[glosario](glosario.md).

## Canales de soporte

- **Durante la sesión:** bloque final de cada clase para preguntas técnicas.
- **Errores en los laboratorios:** abre un issue en el repositorio para que la corrección beneficie a todos.
