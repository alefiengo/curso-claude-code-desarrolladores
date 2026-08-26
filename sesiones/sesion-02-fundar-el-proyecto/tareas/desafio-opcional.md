# Desafío Opcional: Memoria por Alcance

Práctica para después de clase. No se entrega y no es requisito para la sesión 3.

## Objetivo

Comprobar cuándo se carga una memoria anidada y decidir qué reglas merecen vivir
cerca del código en lugar de en la raíz.

## Tiempo Estimado

30 a 40 minutos.

## Por Qué Importa

Todo lo que pongas en el `CLAUDE.md` raíz se carga siempre, en cada
conversación, hable de lo que hable. Una convención que solo aplica a los tests
paga ese coste en las cien conversaciones que no tocan tests.

Una memoria anidada resuelve eso: vive junto al código al que aplica.

## Parte 1: Crear la memoria anidada

Añade `tests/CLAUDE.md` con **dos convenciones que serían erróneas** si se
aplicaran a código de producción. Por ejemplo, decisiones sobre datos de prueba,
uso de dobles, o nomenclatura de casos.

Escríbelas como reglas, no como explicaciones:

```markdown
# Convenciones de tests

- Los datos de prueba se construyen en el propio test, no en fixtures
  compartidas entre archivos.
- Un test que necesite red se marca y se excluye de la ejecución por defecto.
```

Confírmalo:

```bash
git add tests/CLAUDE.md
git commit -m "Anade convenciones de tests con alcance propio"
```

## Parte 2: Comprobar cuándo se carga

Una memoria anidada no se carga por el tema del que hables: se carga cuando
Claude **lee un archivo** del directorio donde vive. Esa es la diferencia que
comprueba esta parte.

Abre dos conversaciones distintas, cada una en su sesión:

| Conversación | Qué haces | Qué comprobar |
|---|---|---|
| A | Preguntas sin abrir ningún archivo de `tests/` | ¿Aparece `tests/CLAUDE.md` en `/context`? |
| B | Pides a Claude que lea `tests/test_health.py` y luego preguntas | ¿Aparece ahora? |

En la A, pregunta sin dejar que lea nada:

```text
¿Qué convenciones de test se aplican en este momento? Cita el archivo del que
las tomas. No leas ningún archivo: responde solo con lo que ya tengas cargado.
```

En la B, primero la lectura y después la misma pregunta:

```text
Lee tests/test_health.py. Después dime qué convenciones de test se aplican en
este momento y cita el archivo exacto del que las tomas.
```

Ejecuta `/context` en las dos y compara la lista de **Memory files**.

Exige el archivo. Sin fuente, no sabes si la leyó o la infirió.

## Parte 3: Decidir el alcance

Para cada regla de tu `CLAUDE.md` raíz, responde:

- ¿Aplica a todo el repositorio, o solo a una carpeta?
- Si es lo segundo, ¿cuánto contexto cuesta tenerla siempre cargada?

Mueve al menos una regla a una memoria anidada, o justifica por escrito por qué
todas las que quedan en la raíz son verdaderamente transversales.

## Comprueba

- ¿En qué conversación se cargó `tests/CLAUDE.md` y en cuál no? ¿Qué acción
  concreta lo cargó?
- ¿Qué regla moviste, y qué habría pasado si un cambio en producción la hubiera
  aplicado por error?
- ¿Qué diferencia hay entre poner una regla en la raíz y ponerla cerca del
  archivo, más allá del coste de contexto?

Anota las respuestas en `evidencias/s02.md`.

## Limpieza

Nada que limpiar. Si decides no conservar `tests/CLAUDE.md`, elimínalo con un
commit que explique por qué la regla no justificaba su alcance.
