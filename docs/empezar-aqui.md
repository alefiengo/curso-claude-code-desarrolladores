# Empezar aquí

Esta página es la única que necesitas para arrancar. Tres pasos, en orden.

Si ya hiciste el paso 1 en una sesión anterior, salta al 3.

---

## Paso 1 — Preparar la máquina (una sola vez, 45–60 min)

**Hazlo antes de la primera clase, no durante.**

Sigue la [guía de instalación](instalacion-entorno.md) de principio a fin.
Instala VS Code, la terminal, Docker, `uv`, Git y Claude Code, y clona el
material del curso.

Sabes que terminaste cuando estas nueve comprobaciones responden sin error:

```bash
code --version
claude --version
docker run --rm hello-world
docker image inspect postgres:18-alpine > /dev/null
uv --version
uv python find 3.12
git config --get user.name
git config --get user.email
ls $CURSO/sesiones
```

Si alguno falla, [problemas frecuentes](problemas-frecuentes.md) lo cubre. No
sigas con algo a medias: el resto del curso da por hecho que esto funciona.

---

## Paso 2 — Leer dos cosas cortas (15 min)

Solo dos, y son breves:

| Qué | Por qué antes de empezar | Tiempo |
|---|---|---|
| [Seguridad](seguridad.md) | Vas a dar acceso a tu código a un agente. Aquí están los límites | 5 min |
| [Guía del estudiante](guia-estudiante.md) | Cómo funcionan los labs y la evaluación | 10 min |

El resto —[plan del curso](../curso.md), [mapa de comandos](comandos.md),
[glosario](glosario.md), [compatibilidad](compatibilidad.md)— es **material de
consulta**. No lo leas
ahora de corrido; búscalo cuando lo necesites.

---

## Paso 3 — Hacer la sesión

Cada sesión sigue siempre la misma forma. Ábrela y recórrela en este orden:

1. **Objetivo y Duración** — qué vas a poder hacer al terminar.
2. **Arranque** — entra en la situación y produce la primera evidencia antes de
   estudiar la explicación.
3. **Conceptos Clave** — vuelve a ellos después de la primera práctica para
   poner nombre a las decisiones que tomaste.
4. **Laboratorios restantes** — continúa el cambio y aplica el criterio con menos
   ayuda.
5. **Validación General y Cierre** — confirma el resultado, registra el riesgo y
   responde las preguntas de repaso.

**Lo importante:** el aprendizaje está en los laboratorios. No postergues la
primera práctica para leer toda la teoría: ejecuta el arranque y vuelve a los
conceptos cuando ya tengas un resultado que interpretar.

### Sesión 1

```bash
code $CURSO/sesiones/sesion-01-especificar-y-verificar/README.md
```

Son dos o tres laboratorios encadenados sobre el mismo repositorio:

| Lab | Qué hace | Min |
|---|---|---:|
| [01 — Resolver un incidente real](../sesiones/sesion-01-especificar-y-verificar/labs/01-bucle-de-verificacion/README.md) | Corregir un webhook que aplica dos veces el mismo pago y auditar el diff | 45 |
| [02 — Convertir una petición en contrato](../sesiones/sesion-01-especificar-y-verificar/labs/02-criterio-falseable/README.md) | Cerrar decisiones, fijar tests e implementar contra evidencia independiente | 45 |

Empieza por el Lab 01 y hazlos en orden: el segundo continúa desde el commit del
primero.

---

## Antes de cada clase siguiente

El material se publica **sesión a sesión**. Si solo ves una carpeta en
`$CURSO/sesiones`, no te falta nada: las demás aparecen conforme se imparten.

Actualiza tu copia antes de cada sesión:

```bash
cd $CURSO && git pull
```

---

## Si algo no encaja

| Situación | Dónde mirar |
|---|---|
| Un comando falla | [Problemas frecuentes](problemas-frecuentes.md) |
| No recuerdo qué hace un comando | [Mapa de comandos](comandos.md) |
| No sé qué significa una palabra del material | [Glosario](glosario.md) |
| Mi cuenta o versión se comporta distinto | [Compatibilidad](compatibilidad.md) |
| Perdí el hilo del proyecto | [Flujo de trabajo con Git](../proyecto-integrador/flujo-git.md) |
| Quiero saber qué se ve en cada sesión | [Temario](temario.md) |
| Quiero ver el curso completo | [Plan del curso](../curso.md) |
