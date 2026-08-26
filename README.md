# Claude Code para Desarrolladores

Curso práctico de 20 horas para dominar Claude Code como herramienta de desarrollo: formular tareas verificables, dar contexto al agente, integrarlo en el flujo de git, extenderlo con comandos propios y llevarlo a CI.

## Por dónde empezar

### → [Empezar aquí](docs/empezar-aqui.md)

Esa página es la única que necesitas para arrancar: preparar la máquina, qué
leer antes de la primera clase y cómo recorrer una sesión. Todo lo demás en
este repositorio es material de consulta.

Si ya tienes el entorno listo, ve directo a la
[Sesión 1](sesiones/sesion-01-especificar-y-verificar/README.md).

**El material se publica sesión a sesión.** Si en `sesiones/` solo ves la
primera, es lo esperado: las demás aparecen conforme se imparten. Actualiza tu
copia con `git pull` antes de cada clase.

## El eje

Un agente rinde en proporción a **lo limpio que esté su contexto** y a **los medios que tenga para verificarse**. Todo lo que enseña el curso sirve a una de esas dos cosas.

Cada sesión analiza un modo de fallo. Cuando el comportamiento depende del
modelo, el laboratorio lo trata como un experimento y registra la evidencia; no
promete una respuesta concreta.

## Al finalizar el curso podrás

- Formular tareas que el agente pueda comprobar por sí mismo.
- Documentar un proyecto para que el agente trabaje bien en él.
- Gestionar el contexto y las sesiones de trabajo.
- Planificar y delegar tareas largas sin perder el control.
- Integrar el agente en el flujo de ramas, commits y pull requests.
- Verificar y depurar lo que produce.
- Crear comandos y skills propios.
- Acotar permisos y automatizar de calidad con hooks y permisos.
- Delegar en subagentes y conectar servidores MCP.
- Ejecutar Claude Code sin interfaz en integración continua.

## Formato

- 10 sesiones de 2 horas.
- Cada sesión tiene conceptos, laboratorios guiados y validación.
- Modalidad práctica: trabajas en tu propia máquina.
- Sin notas: evaluación formativa mediante listas de comprobación, evidencias de
  proceso y un proyecto final.
- Diagnóstico inicial y tarea final de transferencia para medir cambio de conducta.

## Dedicación

| Componente | Tiempo |
|---|---:|
| Clases en vivo | 20 h |
| Diagnóstico + transferencia, fuera de clase | 1 h 20 min |
| Proyecto final | 4–6 h |
| Desafíos opcionales | 30–45 min por sesión |

Las 20 horas anunciadas corresponden a clase. El proyecto y el diagnóstico
forman parte de la experiencia completa y se comunican antes de la inscripción.

## Mapa del Curso

Qué trabaja cada sesión y con qué sales de ella: [temario](docs/temario.md).
Las palabras que el curso usa con un significado preciso: [glosario](docs/glosario.md).


| Sesión | Tema | Sales con |
|---:|---|---|
| [1](sesiones/sesion-01-especificar-y-verificar/README.md) | Especificar y verificar | — |
| [2](sesiones/sesion-02-fundar-el-proyecto/README.md) | Fundar el proyecto y su memoria | `CLAUDE.md` |
| 3 _(aún no publicada)_ | Diseñar antes de implementar | Un plan revisable |
| 4 _(aún no publicada)_ | El primer recurso | Tu primer skill |
| 5 _(aún no publicada)_ | El recurso con relaciones | Un skill con script |
| 6 _(aún no publicada)_ | Que no se te olvide nada | Dos hooks |
| 7 _(aún no publicada)_ | Probar contra la base real | Un MCP conectado |
| 8 _(aún no publicada)_ | Cuando algo se rompe | Un skill de regresión |
| 9 _(aún no publicada)_ | Dejar de fiarte de ti mismo | Un subagente revisor |
| 10 _(aún no publicada)_ | Entregar, automatizar y podar | Permisos, CI y un `.claude/` podado |

## Licencia

Material publicado bajo [CC BY-NC-SA 4.0](LICENSE): puedes compartirlo y
adaptarlo citando la autoría, sin uso comercial, y distribuyendo las obras
derivadas bajo la misma licencia.
