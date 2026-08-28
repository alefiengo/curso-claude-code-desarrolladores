# Sesión 3: Mantener Señal durante una Tarea Larga

Conectar la API a una base de datos obliga a recorrer configuración, modelos,
migraciones, seed y fixtures antes de que un solo endpoint funcione. La
conversación acumula decisiones útiles junto con logs, intentos corregidos y
archivos que ya no necesitas.

En esta sesión completas ese cambio sin recibir código de la API. Claude Code
genera cada incremento; tú decides qué entra al contexto, qué debe quedar en
Git y cuándo conviene continuar, compactar o empezar con una conversación
vacía.

## Objetivo

Dirigir la conexión de la API a PostgreSQL mediante incrementos verificables y
gestionar el contexto a partir de señales observables, sin usar la conversación
como fuente de verdad ni un porcentaje como regla automática.

## Duración

2 horas.

| Bloque | Minutos |
|---|---:|
| [Lab 01 — Dirigir un cambio largo sin perder el control](labs/01-persistencia-vigilada/README.md) | 55 |
| Conceptos retrospectivos: contexto como presupuesto de trabajo | 15 |
| [Lab 02 — Cerrar con contexto deliberado](labs/02-presupuesto-contexto/README.md) | 40 |
| Evidencia y cierre | 10 |

## Materiales

- [Contrato de la API](../../proyecto-integrador/contrato-api.md)
- [Decisiones de ingeniería](../sesion-02-fundar-el-proyecto/labs/02-memoria-util/material/decisiones-ingenieria.md)
- [Flujo de trabajo con Git](../../proyecto-integrador/flujo-git.md)
- [Referencia rápida](referencia-rapida.md)
- [Desafío opcional](tareas/desafio-opcional.md)

## Laboratorios

| Lab | Situación profesional | Qué descubres |
|---|---|---|
| [01 — Dirigir un cambio largo sin perder el control](labs/01-persistencia-vigilada/README.md) | Un cambio de varios turnos entierra la desviación bajo el trabajo posterior | Interrumpir en el turno en que ocurre cuesta menos que descubrirlo al final |
| [02 — Cerrar la tarea con contexto deliberado](labs/02-presupuesto-contexto/README.md) | La implementación terminó, pero su conversación mezcla evidencia y razonamiento descartado | Compactar conserva continuidad; una conversación vacía permite revisar sin heredar la defensa de la solución |

## Arranque: Un Cambio que No Cabe en un Turno

No leas todavía los conceptos. Abre el Lab 01 y llega hasta el contrato de
tarea:

```bash
code $CURSO/sesiones/sesion-03-administrar-el-contexto/labs/01-persistencia-vigilada/README.md
```

En los primeros ocho minutos debes haber verificado `main`, creado
`feature/persistencia` y guardado la vista inicial de `/context all`. Completa el
lab y vuelve después a esta página: los conceptos ponen nombre a decisiones que
ya tomaste durante una conversación real.

## Al finalizar esta sesión podrás

- Descomponer una entrega multiarchivo en incrementos verificables sin recibir
  una implementación preparada.
- Predecir qué sobrevive a una compactación y qué hay que recuperar desde disco.
- Mantener contrato, tests, configuración e instrucciones protegidos mientras
  Claude genera código.
- Usar `/context all` para identificar qué consume capacidad sin convertirlo en
  una métrica de calidad.
- Elegir entre continuar, `/btw`, `/compact` y `/clear` según la tarea que queda.
- Redactar una compactación enfocada y comprobar su resumen contra Git.
- Revisar una rama desde una conversación vacía antes de integrarla.
- Integrar la primera rama del proyecto sin tags y dejar `main` reproducible.

Proyectos y tareas llegan en las sesiones 4 y 5. Hoy construyes la capa de
persistencia sobre la que se apoyan, que es la parte que de verdad llena una
conversación.

## Conceptos Clave

### El contexto es un presupuesto, no una puntuación

La **ventana de contexto** contiene instrucciones, conversación, respuestas,
archivos leídos, resultados de herramientas y definiciones que Claude necesita
para trabajar. `/context all` muestra cómo se reparte y advierte sobre fuentes
costosas. No dice si una respuesta es correcta.

Una ventana con espacio libre puede contener una hipótesis equivocada repetida
diez veces. Una ventana ocupada puede conservar justo la historia que una
migración necesita. La decisión combina dos tipos de evidencia:

| Evidencia | Pregunta |
|---|---|
| Composición y capacidad | ¿Qué está consumiendo la ventana? |
| Conducta observada | ¿Claude repite búsquedas, olvida límites o corrige en círculos? |

El **presupuesto de contexto** es la capacidad que decides gastar en
información que todavía cambia una decisión. No tiene un porcentaje universal.

### El estado de trabajo vive fuera de la conversación

Una conversación coordina el trabajo; no lo versiona. El estado recuperable
vive en artefactos que otra sesión puede comprobar:

- contrato y decisiones en archivos;
- tests que fijan comportamiento;
- commits que separan incrementos;
- salidas relevantes guardadas como evidencia;
- riesgo residual escrito.

Compactar o limpiar no pone en peligro una tarea que ya dejó esas huellas. Si
una decisión solo existe en un turno antiguo, todavía no es un estado de trabajo
profesional.

### Cinco acciones para cinco necesidades

| Necesidad actual | Acción | Coste o límite |
|---|---|---|
| La misma tarea sigue clara y el contexto es pertinente | Continuar | Cada turno conserva también el ruido anterior |
| Necesitas una respuesta sobre algo ya visto, sin interrumpir | `/btw` | Ve la conversación, pero no tiene herramientas ni añade la respuesta al historial principal |
| Sigues en la misma tarea y la historia útil ocupa demasiado | `/compact <foco>` | Sustituye el historial por un resumen; pierde detalle |
| Cambias de tarea o necesitas escapar de los supuestos anteriores | `/clear [nombre]` | Abre contexto vacío; la conversación anterior queda fuera y puede retomarse después |
| Un archivo concreto es una fuente necesaria | `@ruta` | Incluye el contenido completo del archivo; no es una carga gratuita |

La acción se elige por el trabajo que queda, no por costumbre. Compactar antes
de saber qué debe sobrevivir delega esa decisión al resumen automático.

### Qué conserva una compactación

`/compact` sustituye el historial por un resumen, pero no todo depende de ese
resumen. Lo que ocurre con cada cosa está definido:

| Contenido | Después de compactar |
|---|---|
| `CLAUDE.md` de la raíz y reglas sin `paths:` | Se reinyectan desde disco |
| Memoria automática | Se reinyecta desde disco |
| Archivos que Claude leyó o editó | Claude Code relee **hasta cinco**, los modificados más recientemente |
| Reglas con `paths:` y `CLAUDE.md` anidados | Se recargan cuando Claude vuelve a leer un archivo que los activa |
| Todo lo demás de la conversación | Se resume |

Dos consecuencias prácticas. La primera: un archivo grande vuelve como
referencia de ruta, sin su contenido, así que no cuentes con que siga cargado.
La segunda, y la que importa hoy: **una decisión que solo existe en un turno de
la conversación es exactamente lo que el resumen puede perder.** Si la escribiste
en un archivo o la fijaste en un commit, sobrevive; si solo la dijiste, no.

Por eso el Lab 02 comprueba tres hechos después de compactar. El objetivo no es
probar que Claude "recuerda"; es detectar qué debe recuperarse desde una fuente
estable.

### Contexto limpio no significa repositorio vacío

`/clear` inicia una conversación sin el historial anterior. El repositorio, la
rama, los commits y las instrucciones de proyecto siguen allí. Esa separación
permite cambiar de función: una conversación implementa y otra revisa el diff
sin recibir las justificaciones usadas para producirlo.

No es una revisión completamente independiente: sigue siendo el mismo modelo y
comparte las fuentes del repositorio. Sí elimina una contaminación concreta, la
conversación de implementación, y hace visible qué información necesita una
revisión para sostener sus hallazgos.

## Comandos Nuevos

| Comando | Uso en esta sesión |
|---|---|
| `/btw <pregunta>` | Consulta lateral sobre información ya presente, sin herramientas ni historial principal |
| `/compact <foco>` | Resumir la conversación para continuar la misma tarea |
| `/clear [nombre]` | Etiquetar la conversación anterior y empezar otra con contexto vacío |

`/context`, `/diff` y `@ruta` ya aparecieron antes. Aquí dejas de usarlos por
comodidad y los conviertes en decisiones de presupuesto: `/diff` recorre un
cambio que llegó en varios turnos, y `Esc` interrumpe en el turno en que aparece
la desviación, sin esperar al final.

`/autocompact` fija cuánto se llena la ventana antes de que la compactación
automática se dispare, y acepta un recuento de tokens: `/autocompact 500k`. No
forma parte del recorrido obligatorio. Automatizar el umbral antes de aprender
qué debe conservarse sustituiría la decisión que practicas hoy.

## Validación General

Desde `main`, después de integrar:

```bash
git status --short
uv lock --check
docker compose up -d --wait db
uv run alembic upgrade head
uv run pytest -q
uv run ruff check .
docker compose config -q
git log --oneline -6
```

- [ ] La API cumple las secciones Salud y Estados del contrato.
- [ ] La migración reconstruye esquema y catálogo sobre PostgreSQL vacío.
- [ ] Los tests estuvieron en rojo antes de implementar el catálogo y permanecen
      protegidos después.
- [ ] Los commits separan persistencia, contrato ejecutable, catálogo y
      evidencia de contexto.
- [ ] Registraste las desviaciones que interrumpiste durante la generación, o
      dejaste constancia de que no hubo ninguna.
- [ ] Conservaste mediciones antes y después de compactar.
- [ ] La revisión desde contexto limpio fue de solo lectura y cada hallazgo fue
      comprobado.
- [ ] Declaraste qué sigue sin estar probado.
- [ ] `main` está limpio y no existe ningún tag de sesión.

## Limpieza

Conserva el proyecto y sus evidencias. Detén PostgreSQL sin borrar el volumen:

```bash
docker compose down
docker compose ps
git status --short
```

No borres la conversación etiquetada por `/clear`. La sesión 6 trabaja la
recuperación de conversaciones e historiales; hoy basta con que el proyecto no
dependa de ella.

## Desafío Opcional

El [desafío opcional](tareas/desafio-opcional.md) compara dos presupuestos de
contexto sobre la misma pregunta de solo lectura en un repositorio propio. No se
entrega y no es requisito para la sesión 4.

## Cierre

Completa la sección **Cierre** de `evidencias/s03.md`, el archivo que copiaste en
el paso 1 del Lab 01. Debe quedar registrado cuándo continuaste, compactaste o
limpiaste y qué evidencia sostuvo esa decisión; qué comandos y fuentes permiten
reconstruir el estado sin leer la conversación; y qué sigue sin estar probado o
qué riesgo aceptaste al integrar.

Preguntas de repaso:

- ¿Qué información consumía más contexto y todavía cambiaba una decisión?
- ¿Qué hecho no sobrevivió a la compactación y dónde lo recuperaste?
- ¿Por qué `@archivo` puede ser mejor que pegar contenido, pero no cuesta cero?
- ¿Qué diferencia observable hubo entre revisar antes y después de `/clear`?
- ¿Qué evidencia permitiría continuar si ambas conversaciones desaparecieran?

## Versión

Material revisado el **27 de agosto de 2026** con Claude Code **2.1.247** y la
documentación oficial vigente:

- [Ventana de contexto](https://code.claude.com/docs/en/context-window)
- [Modo interactivo y `/btw`](https://code.claude.com/docs/en/interactive-mode)
- [Comandos incorporados](https://code.claude.com/docs/en/commands)

Comprueba tu versión con `claude --version` y los comandos con `/help`. Si
`/btw` no aparece, usa la alternativa del Lab 02; `/compact`, `/clear` y
`/context` siguen siendo obligatorios.

## Estado Final del Repositorio

La sesión 4 parte de aquí. En `~/curso-claude/curso-claude-code-api`, rama
`main`, con `feature/persistencia` ya integrada y borrada, y sin ninguna
etiqueta:

| Añadido en esta sesión | Contenido |
|---|---|
| Configuración de base de datos y modelos | La capa que conecta la API a PostgreSQL |
| Migración inicial | Reconstruye esquema y catálogo desde una base vacía |
| Catálogo de estados | La sección Estados del contrato, con sus tests en verde |
| Fixtures de test contra PostgreSQL | La base sobre la que se escriben los tests de las sesiones 4 y 5 |
| `evidencias/s03.md` y `evidencias/estados-rojo.txt` | Tu registro de contexto y el rojo previo |

Proyectos, tareas y filtros **no existen todavía**. Es correcto: llegan en las
sesiones 4 y 5.

## Preparación para la Sesión 4

El material se publica sesión a sesión, así que actualiza tu copia antes de la
clase:

```bash
cd $CURSO && git pull
```

Comprueba que el esquema nace desde una base vacía. La primera operación elimina
el volumen local del proyecto y sus datos de ejercicio:

```bash
docker compose down -v
docker compose up -d --wait db
uv run alembic upgrade head
uv run pytest -q
uv run ruff check .
git status --short
```

No implementes nada. Lee la sección **Proyectos** de `docs/contrato-api.md` y
anota qué decisiones deja abiertas. La sesión 4 empieza con esas preguntas y
convierte el cambio en un plan revisable antes de tocar código.
