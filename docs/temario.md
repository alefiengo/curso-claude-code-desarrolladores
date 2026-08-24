# Temario

Qué trabaja cada sesión y con qué sales de ella. El desarrollo completo está en
el [plan del curso](../curso.md) y en cada sesión.

Diez sesiones de dos horas, en tres bloques. El proyecto crece sesión a sesión:
lo que construyes en una es el punto de partida de la siguiente.

---

## Bloque 1 — Modelo mental y proyecto

Sesiones 1 a 3. De qué es un agente a un proyecto con memoria y contexto
administrado.

### 1. Especificar y verificar

**El problema:** "arregla los errores" no es una tarea; es un deseo. Y sin forma
de comprobarlo, el agente decide por su cuenta cuándo ha terminado.

**Sales sabiendo:** escribir un prompt con contexto, alcance y criterio de
terminación; detectar un criterio que el agente puede falsear —modificar los
tests con los que se le mide— y cerrarlo; y exigir la fuente de cada afirmación
antes de darla por buena.

### 2. Fundar el proyecto y su memoria

**El problema:** un proyecto que solo arranca en la máquina donde se creó, y un
`CLAUDE.md` tan largo que el agente lo ignora.

**Sales sabiendo:** dar un contrato técnico sin dictar la implementación,
validar la base desde una máquina limpia, y distinguir la regla que hay que
recordar del hecho que el código ya expresa.

### 3. Administrar el contexto

**El problema:** el rendimiento cae cuando la conversación se llena de ruido, y
no se nota hasta que el agente empieza a olvidar lo que dijiste.

**Sales sabiendo:** ver qué ocupa el contexto y decidir cuándo resumir, cuándo
limpiar y cuándo continuar; y completar un cambio en varios archivos sin perder
el contrato de vista.

---

## Bloque 2 — El ciclo de trabajo

Sesiones 4 a 6. Explorar, planificar, implementar, entregar, y recuperarse
cuando algo sale mal.

### 4. Explorar y planificar

**El problema:** pedirle una feature grande de golpe y descubrir a mitad de
camino que entendió otra cosa.

**Sales sabiendo:** separar la investigación de la ejecución con Plan mode;
leer, corregir y rechazar un plan antes de aprobarlo; y elegir modelo y esfuerzo
según el riesgo de la tarea, no por costumbre.

### 5. Implementar y entregar

**El problema:** un cambio correcto que nadie puede revisar, porque llega en un
solo commit de cuarenta archivos.

**Sales sabiendo:** implementar por incrementos comprobables, separar migración,
dominio y entrega en commits con intención, y producir una entrega que otra
persona pueda revisar y decidir si integrar.

### 6. Interrumpir y recuperar

**El problema:** la sesión se tuerce y sigues corrigiendo sobre lo torcido, en
vez de volver al último punto bueno.

**Sales sabiendo:** interrumpir antes de que el coste crezca; distinguir si hay
que deshacer la conversación, el código o los dos; y retomar el trabajo días
después sin depender de lo que recuerdes.

---

## Bloque 3 — Automatizar y escalar

Sesiones 7 a 10. Verificación real, extensiones propias, control automático y
delegación.

### 7. Reproducir y depurar

**El problema:** aceptar "ya lo arreglé" sin evidencia, y descubrir el fallo dos
semanas después.

**Sales sabiendo:** reducir un reporte a una reproducción mínima, comprobar que
el test falla por la razón esperada, separar síntoma de causa, y verificar lo
que una captura de pantalla **no** demuestra.

### 8. Extender con skills

**El problema:** el mismo procedimiento pegado a mano cada vez, con variaciones
que hacen incomparables los resultados.

**Sales sabiendo:** elegir entre `CLAUDE.md`, skill, subagente, hook y MCP;
convertir un procedimiento repetido en un skill versionado, con permisos
acotados; y evaluarlo con casos que deben pasar y casos que deben fallar.

### 9. Acotar permisos y automatizar

**El problema:** la fatiga de permisos lleva a conceder acceso global, y "ejecuta
los tests antes de terminar" es un consejo que el agente puede saltarse.

**Sales sabiendo:** diseñar reglas de mínimo privilegio y **probar que
bloquean**, no suponerlo; y convertir una verificación que hoy depende de
acordarse en una puerta automática con código de salida.

### 10. Delegar y ejecutar sin interfaz

**El problema:** pedirle a la misma conversación que revise su propio trabajo, y
conectar un servidor externo por comodidad sin evaluarlo.

**Sales sabiendo:** obtener una revisión que no herede tus supuestos, ejecutar
el agente sin nadie delante con límites reales de herramientas y coste, y
evaluar una integración externa antes de ampliar el límite de confianza.

---

## El hilo que une las diez

> Un agente rinde en proporción a **lo limpio que esté su contexto** y a **los
> medios que tenga para verificarse**.

Eso se ve en la **escalera de verificación**, que recorre el curso entero. El
criterio de "esto está terminado" va bajando desde el texto hasta el código:

| Peldaño | Dónde vive el criterio | Quién decide si se cumple | Sesión |
|---|---|---|---|
| 1 | En el prompt | El modelo, releyendo la tarea | 1 |
| 2 | En `/goal`, fuera de la tarea | Un modelo evaluador | 4 |
| 3 | En un script con código de salida | El código de salida | 9 |
| 4 | En un revisor con contexto propio | Otro agente aislado | 10 |

Cada peldaño es más difícil de falsear que el anterior. Ninguno es perfecto, y
el curso dice de cada uno **qué sigue sin garantizar**.

## Lo que construyes

Una API REST de gestión de tareas, con base de datos y una página mínima para
probarla. Crece contigo: al terminar tienes el proyecto funcionando y un
`.claude/` con las herramientas que construiste. Los detalles están en el
[proyecto integrador](../proyecto-integrador/README.md).

## Cómo se evalúa

**No hay notas.** Cada sesión cierra con una lista de comprobación y una
evidencia de proceso —una decisión y lo que la respalda—. El proyecto final usa
una rúbrica sin calificación, y los desafíos opcionales no se entregan.
