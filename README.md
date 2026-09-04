# Claude Code para Desarrollo Profesional

Aprende a completar cambios reales con Claude Code sin entregar el control de la
ingeniería: entender un repositorio, acordar el resultado, implementar, verificar
y entregar un diff que otra persona pueda revisar.

No es un curso de "prompts mágicos" ni un catálogo de comandos. Trabajas con
tickets, código existente, tests, Git, revisiones, permisos y automatización.

## Desde el Minuto Cero

La primera práctica parte de un incidente: un webhook reintentado acredita dos
veces el mismo pago. Recibes el ticket, el código y una regresión en rojo. Tu
trabajo es dirigir a Claude Code hasta una corrección mínima, comprobar el
resultado y decidir si el diff merece aceptarse.

En esa primera sesión ya practicas el ciclo que ordena todo el curso:

```text
entender → acordar → cambiar → comprobar → revisar
```

Las sesiones siguientes aumentan el alcance: de un archivo a un proyecto, de
una tarea a una entrega y de una ejecución supervisada a una automatización con
límites.

## La Promesa

Al terminar podrás:

- convertir un ticket incompleto en una tarea delegable y verificable;
- explorar un repositorio desconocido sin llenar la conversación de ruido;
- decidir cuándo investigar, cuándo planificar y cuándo implementar directo;
- dar a Claude contexto persistente que aporte información y no repita el README;
- intervenir, recuperar y continuar cuando una ejecución se desvía;
- depurar desde una reproducción y cerrar con una regresión;
- revisar alcance, evidencia y diff antes de aceptar;
- convertir trabajo repetido en skills y obligaciones en hooks;
- acotar permisos y conexiones externas con pruebas negativas;
- delegar revisiones con contexto aislado y ejecutar flujos sin interfaz.

## Qué Hace Diferente al Curso

| Curso superficial | Este curso |
|---|---|
| Enseña comandos aislados | Enseña decisiones dentro de un flujo de trabajo |
| Usa ejemplos de juguete | Usa incidentes, contratos, cambios multiarchivo y entregas |
| Celebra que el agente escribió código | Exige evidencia y revisión del diff |
| Presenta una respuesta ideal | Trabaja con salidas variables y resultados comprobables |
| Configura todo desde el principio | Añade contexto y automatización cuando aparece una necesidad real |
| Termina en una demo | Termina en una entrega reproducible y auditable |

## Recorrido

| Sesión | Problema profesional |
|---:|---|
| [1](sesiones/sesion-01-especificar-y-verificar/README.md) | Un ticket ambiguo o sin comprobación |
| [2](sesiones/sesion-02-fundar-el-proyecto/README.md) | Claude no conoce el repositorio o recibe instrucciones inútiles |
| [3](sesiones/sesion-03-administrar-el-contexto/README.md) | Una tarea larga degrada el contexto mientras crece el cambio |
| [4](sesiones/sesion-04-ejecutar-y-publicar/README.md) | Un plan aprobado, ejecutado sin límites y sin publicar |
| [5](sesiones/sesion-05-revisar-e-integrar/README.md) | El código funciona, pero el cambio no es revisable |
| [6](sesiones/sesion-06-interrumpir-y-recuperar/README.md) | Una línea de trabajo se desvía o debe continuar otro día |
| 7 _(aún no publicada)_ | Una explicación plausible reemplaza a la reproducción |
| 8 _(aún no publicada)_ | Un contrato entre servicios que ningún test vigila |
| 9 _(aún no publicada)_ | Una instrucción se confunde con una garantía |
| 10 _(aún no publicada)_ | Una ejecución aislada o automática puede exceder sus límites |

Consulta el [temario detallado](docs/temario.md) para ver las decisiones y los
artefactos de cada sesión.

## Formato

- 20 horas: 10 sesiones en vivo de 2 horas.
- Al menos 70 % del tiempo se trabaja sobre código y evidencia.
- Dos o más laboratorios encadenados por sesión.
- Un proyecto integrador que crece mediante cambios revisables.
- Evaluación formativa: no se premia memorizar comandos ni aceptar más código.

## Perfil de Entrada

Necesitas manejar Git y una terminal, y poder leer y depurar Python básico. No
necesitas experiencia previa con Claude Code, FastAPI ni MCP.

Desde la sesión 4 publicas tu trabajo, así que necesitas también una cuenta de
**GitHub o GitLab**. Cualquiera de las dos sirve.

Si nunca usaste la herramienta, llegas en igualdad de condiciones: la primera
sesión explica el modelo mental mientras resuelves un cambio real.

## Empezar

1. Sigue [Empezar aquí](docs/empezar-aqui.md).
2. Completa la comprobación del entorno antes de la clase.
3. Abre la [Sesión 1](sesiones/sesion-01-especificar-y-verificar/README.md).

El [plan completo](curso.md), el [glosario](docs/glosario.md) y el
[mapa de comandos](docs/comandos.md) son referencias; no necesitas leerlos de
corrido.

## Licencia

Material publicado bajo [CC BY-NC-SA 4.0](LICENSE): puedes compartirlo y
adaptarlo citando la autoría, sin uso comercial, y distribuyendo las obras
derivadas bajo la misma licencia.
