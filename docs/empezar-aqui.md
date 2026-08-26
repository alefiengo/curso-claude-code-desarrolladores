# Empezar aquí

Esta página es la única que necesitas para arrancar. Tres pasos, en orden.

Si ya hiciste el paso 1 en una sesión anterior, salta al 3.

---

## Paso 1 — Preparar la máquina (una sola vez, 45–60 min)

**Hazlo antes de la primera clase, no durante.**

Sigue la [guía de instalación](instalacion-entorno.md) de principio a fin.
Instala VS Code, la terminal, Docker, `uv`, Git y Claude Code, y clona el
material del curso.

Sabes que terminaste cuando estos cinco comandos responden sin error:

```bash
code --version
claude --version
docker run --rm hello-world
uv --version
git config --get user.email
```

Si alguno falla, [problemas frecuentes](problemas-frecuentes.md) lo cubre. No
sigas con algo a medias: el resto del curso da por hecho que esto funciona.

---

## Paso 2 — Leer dos cosas cortas (15 min)

Solo dos, y son breves:

| Qué | Por qué antes de empezar | Tiempo |
|---|---|---|
| [Seguridad](seguridad.md) | Vas a dar acceso a tu código a un agente. Aquí están los límites | 5 min |
| [Guía del estudiante](guia-estudiante.md) | Cómo funcionan los labs, las evidencias y la evaluación | 10 min |

El resto —[plan del curso](../curso.md), [mapa de comandos](comandos.md),
[glosario](glosario.md), [compatibilidad](compatibilidad.md)— es **material de
consulta**. No lo leas
ahora de corrido; búscalo cuando lo necesites.

---

## Paso 3 — Hacer la sesión

Cada sesión sigue siempre la misma forma. Ábrela y recórrela en este orden:

1. **Objetivo y Duración** — qué vas a poder hacer al terminar.
2. **Conceptos Clave** — léelos, pero no los memorices. Son lo que da sentido a
   los laboratorios; vuelves a ellos cuando algo no encaja.
3. **Laboratorios** — aquí está el trabajo real. Cada lab tiene su propia
   página con pasos numerados.
4. **Validación General** — la lista que confirma que la sesión quedó hecha.
5. **Cierre** — evidencias y preguntas de repaso.

**Lo importante:** el aprendizaje está en los laboratorios. Si vas con poco
tiempo, haz los labs y vuelve después a los conceptos.

### Sesión 1

```bash
code $CURSO/sesiones/sesion-01-especificar-y-verificar/README.md
```

Son tres laboratorios:

| Lab | Qué hace | Min |
|---|---|---:|
| [01 — Bucle de verificación](../sesiones/sesion-01-especificar-y-verificar/labs/01-bucle-de-verificacion/README.md) | Una tarea con criterio de terminación y otra sin él, sobre el mismo error | 25 |
| [02 — Criterio falseable](../sesiones/sesion-01-especificar-y-verificar/labs/02-criterio-falseable/README.md) | Reformular "arregla los errores" en algo comprobable | 35 |
| [03 — Preguntar al código](../sesiones/sesion-01-especificar-y-verificar/labs/03-preguntar-al-codigo/README.md) | Entender un repositorio ajeno exigiendo archivo y línea | 25 |

Empieza por el Lab 01 y hazlos en orden: el 02 da por hecho lo del 01.

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
