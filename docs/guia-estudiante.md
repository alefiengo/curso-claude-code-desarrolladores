# Guía del Estudiante

## Qué cubre el curso

El curso avanza en tres bloques:

1. **Fundamentos:** formular tareas verificables, arrancar el proyecto y darle contexto al agente, gestionar sesiones.
2. **Flujo de trabajo:** planificar tareas largas, integrar el agente en git, verificar y depurar.
3. **Extender y escalar:** comandos y skills propios, hooks y permisos, subagentes, MCP y CI.

Cada bloque cierra con una versión del proyecto integrador.

## Antes de la primera sesión

Prepara el entorno siguiendo la [guía de instalación](instalacion-entorno.md). Necesitas:

- Claude Code instalado y autenticado. Revisa las opciones de cuenta y las
  capacidades opcionales en la [matriz de compatibilidad](compatibilidad.md).
- Docker funcionando.
- `uv` instalado.
- Git configurado con nombre y correo.
- Una terminal Linux, macOS o WSL 2 con Ubuntu.

Si nunca has usado Claude Code, o solo lo has usado como chat, ejecuta `/powerup` antes de la primera sesión: son diez lecciones cortas dentro del propio producto. Está descrito en la [guía de instalación](instalacion-entorno.md).

## Qué necesitas saber de antes

- Manejarte con git y la terminal.
- Dominar al menos un lenguaje de programación.

No hace falta que sepas Python ni FastAPI. Son el medio del curso, no la materia.

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

Cada estudiante construye su propio `curso-claude-code-api` durante el curso. Los laboratorios lo hacen crecer sesión a sesión: al terminar tienes una API funcionando y un `.claude/` con las herramientas que construiste.

Es tuyo. Trabajas en tu máquina y en tu repositorio.

Los labs son acumulativos. Antes de cada sesión comprueba el tag indicado en
[Checkpoints y Recuperación](../proyecto-integrador/checkpoints.md). Si faltas,
retoma desde el último estado válido; no etiquetes un estado roto para avanzar.

## Evaluación

No hay notas. Cada sesión cierra con una lista de comprobación y una evidencia
breve de proceso. El proyecto final se revisa con una rúbrica formativa. Consulta
[Evaluación y Portafolio](evaluacion.md).

El curso comienza con un [diagnóstico](diagnostico.md) y termina con una tarea
equivalente de transferencia. Se comparan hábitos de trabajo, no velocidad de
tecleo ni cantidad de código.

Lo que importa no es que la feature funcione, sino cómo llegaste hasta ella.

## Cuando algo falla

Consulta la [guía de problemas frecuentes](problemas-frecuentes.md) antes de pedir soporte.

## Canales de soporte

- **Durante la sesión:** bloque final de cada clase para preguntas técnicas.
- **Errores en los laboratorios:** abre un issue en el repositorio para que la corrección beneficie a todos.
