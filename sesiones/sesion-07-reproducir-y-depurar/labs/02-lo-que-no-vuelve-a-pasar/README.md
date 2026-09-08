# Lab 02: Lo que no Vuelve a Pasar

## Objetivo

Escribir en `.claude/rules/` las convenciones de este repositorio que llevas
seis sesiones repitiéndole a Claude, acotar por ruta las que solo aplican a
una parte del código, y comprobar que cambian lo que hace, no solo lo que
promete.

## Por qué este lab

En el Lab 01 corregiste un procedimiento escrito —el archivo de la skill— y
con eso el fallo dejó de poder repetirse. Hay una segunda categoría de cosas
que también deberían estar escritas y no lo están: las convenciones del
proyecto que has ido corrigiendo a mano, sesión tras sesión. Que la respuesta
de una colección es una lista en la raíz y no un objeto envolvente. Que un
campo nuevo toca migración, esquema y validación. Que un test que prueba un
fallo no se toca para que pase un cambio.

Nada de eso está en `CLAUDE.md`, y no debería estar todo ahí: `CLAUDE.md` se
carga entero en cada sesión, aunque hoy no toques un endpoint. Las reglas de
`.claude/rules/` se pueden acotar por ruta, y así solo llegan cuando hacen
falta.

## Requisitos

- Lab 01 terminado en `feature/segmentar-commits`, sin publicar y sin el campo
  `priority`: la skill diagnosticada, y corregida y confirmada si hacía falta.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–6 | La lista de convenciones que ya has repetido, con el archivo o commit donde se ven |
| 6–14 | `code-style.md` y `testing.md` escritas, sin acotar |
| 14–21 | `api-conventions.md` escrita y acotada por ruta |
| 21–27 | Las tres comprobadas: que cargan, y que Claude las respeta sin que las menciones |
| 27–30 | `CLAUDE.md` podado, y todo entregado e integrado |

**Si necesitas cortar aquí:** lo mínimo es `api-conventions.md` acotada y
comprobada con el paso 6. Las otras dos se terminan después.

## Paso a Paso

### 1. Minar lo que ya dijiste más de una vez

No inventes convenciones: sácalas de tu propio repositorio.

```text
Lee CLAUDE.md, docs/contrato-api.md, los planes de docs/ y los últimos
veinte commits. Dime qué convenciones sigue este código que no están
escritas en ningún archivo, separadas en tres grupos: estilo de Python,
forma de los tests, y forma de los endpoints. Para cada una, dime en qué
archivo o commit la ves, y si aplica a todo el repositorio o solo a una
carpeta.
```

Quédate con dos listas: lo que aplica siempre, y lo que solo aplica donde
viven los endpoints.

### 2. Escribir `code-style.md`

```text
Crea .claude/rules/code-style.md con las convenciones de estilo que
encontraste y que aplican a todo el repositorio: tipado, esquemas frente a
diccionarios sueltos, funciones async, manejo de errores, y lo que ruff ya
exige hoy. Una línea por convención, concreta y verificable —"usa X", no
"escribe código limpio"—. Sin paths en el encabezado: esta aplica a todo.
Enséñamelo antes de guardarlo.
```

La documentación oficial fija un límite útil: menos de 200 líneas por
archivo de reglas. Si te sale más largo, estás documentando el código en vez
de sus convenciones.

### 3. Escribir `testing.md`

```text
Crea .claude/rules/testing.md con la forma real que tienen los tests de este
repositorio: dónde viven, cómo se nombran, cómo se prepara y se revierte la
base de datos entre pruebas, y qué invariantes del contrato no pueden faltar
—la Matriz Mínima de Tests de docs/contrato-api.md—. Añade una que
aprendiste a la fuerza: un test que prueba un fallo no se modifica para que
un cambio nuevo pase. Sin paths. Enséñamelo antes de guardarlo.
```

### 4. Escribir `api-conventions.md`, acotada por ruta

Esta sí depende de dónde trabajas. Pide primero el dato:

```text
¿En qué ruta del repositorio viven los endpoints de la API? Dame la ruta
exacta, no una aproximación.
```

Con esa ruta:

```text
Crea .claude/rules/api-conventions.md con paths apuntando a esa carpeta.
Dentro: el esquema de respuesta exacto —los campos declarados, ni uno más—,
qué código de estado corresponde a cada error (404, 409, 422), que una
colección devuelve una lista en la raíz y con orden estable, y que un campo
nuevo se añade en sus tres capas: migración, esquema y validación.
Enséñamelo antes de guardarlo.
```

### 5. Comprobar que cargan

```text
/context
```

Busca las tres bajo **Memory files**. `code-style.md` y `testing.md` tienen
que estar ahí desde el arranque. `api-conventions.md` puede no aparecer
todavía: al llevar `paths`, se carga cuando Claude lee un archivo de esa
carpeta. Confírmalo pidiéndole que abra uno y volviendo a mirar `/context`.

### 6. Probar que Claude las respeta sin que las menciones

Una regla que existe pero no cambia nada es un archivo muerto. Compruébalo
con dos encargos que la contradicen, sin nombrar ninguna regla.

El primero contradice `api-conventions.md`:

```text
Para que el frontend pueda paginar, cambia GET /tasks para que devuelva
{"items": [...], "total": N} en vez de la lista, y añade un campo
updated_at a cada tarea. Impleméntalo.
```

Lo que tiene que haber ocurrido: se detiene y objeta, señalando que el
contrato fija una lista en la raíz y un esquema de respuesta exacto, antes de
escribir código. Si lo implementó sin decir nada, la regla no cargó o no es
lo bastante concreta: revisa `/context` primero, y después su redacción.

El segundo contradice `testing.md`:

```text
El test que comprueba el esquema exacto de respuesta se va a romper cada vez
que añadamos un campo. Hazlo más flexible: que compruebe solo que están los
campos del contrato, y que no falle si aparece alguno de más.
```

Lo que tiene que haber ocurrido: se niega, y señala que ese test existe justo
para atrapar el campo de más. Si lo relaja, la regla no está cargando o no es
lo bastante concreta.

Los dos encargos suenan razonables, y ninguno lo es: uno rompe el contrato,
el otro desarma la comprobación que lo vigila. Eso es lo que hace que sirvan
de prueba.

Nada de esto se implementa. Si Claude alcanzó a escribir algo, descártalo
antes de seguir:

```text
Descarta cualquier cambio de los dos encargos anteriores y confírmame que el
árbol de trabajo solo tiene los archivos de .claude/rules/.
```

### 7. Podar `CLAUDE.md`

```text
De lo que ahora dicen code-style.md, testing.md y api-conventions.md,
¿algo estaba ya duplicado en CLAUDE.md? Enséñame qué, y quítalo de
CLAUDE.md sin tocar nada más del archivo.
```

Lo que no se duplica se queda: `CLAUDE.md` sigue siendo el lugar de lo que
aplica a cada sesión y no encaja en ninguna regla acotada.

### 8. Entregar e integrar

Revisa el `/diff` completo. Después:

```text
Publica feature/segmentar-commits, abre la solicitud de cambios hacia main
con la descripción de siempre —qué cambia, qué se decidió y por qué, cómo se
comprueba, qué queda sin probar—, y enséñamela antes de crearla.
```

Revísala: las reglas nuevas y, si la hubo, la corrección de la skill tienen que
aparecer como commits separados. Intégrala.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué archivos hay en .claude/rules/, y cuál de ellos tiene paths en su
   encabezado.
3. Cuántas líneas tiene cada uno.
4. uv run pytest -q y uv run ruff check .
5. Los commits de main que no estaban al empezar el Lab 01, uno por línea.
6. Qué quité de CLAUDE.md y por qué.
```

El lab está completo si:

- [ ] Las tres reglas salieron de convenciones que tu repositorio ya seguía, no de una lista genérica de buenas prácticas.
- [ ] `code-style.md` y `testing.md` no tienen `paths` y cargan siempre; cada una por debajo de 200 líneas.
- [ ] `api-conventions.md` tiene `paths` apuntando a la carpeta real de los endpoints, y la viste cargar solo al abrir un archivo de ahí.
- [ ] Claude objetó los dos encargos del paso 6 sin que le mencionaras ninguna regla.
- [ ] Ninguno de esos dos encargos dejó código en el árbol de trabajo.
- [ ] `CLAUDE.md` perdió solo lo que quedó duplicado en una regla, nada más.
- [ ] `main` integra las tres reglas y, si la hubo, la corrección de la skill, con un commit por intención.

## Limpieza

```text
Detén los contenedores del proyecto sin eliminar volúmenes.
```

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El paso 1 devuelve generalidades ("usa nombres descriptivos") | No sirven como regla. Pídele que cada convención venga con el archivo o el commit donde se ve, y descarta las que no puedan señalarlo |
| `api-conventions.md` no aparece nunca en `/context`, ni abriendo archivos de esa carpeta | Revisa que el patrón de `paths` case con tu estructura real. Pídele que lo compruebe contra la ruta exacta de un archivo de endpoints |
| En el paso 6 implementó el cambio en vez de objetar | Comprueba primero con `/context` que la regla estaba cargada. Si estaba, hazla más específica: menos "sigue el contrato", más "la colección devuelve una lista en la raíz; un objeto envolvente rompe el contrato" |
| Una regla te salió de 300 líneas | Estás copiando el código dentro de la regla. Deja la convención y el porqué; el código ya está en el repositorio |
| No sabes qué quitar de `CLAUDE.md` en el paso 7 | Si no hay duplicación, es un resultado válido: significa que `CLAUDE.md` ya estaba acotado y las reglas nuevas cubren terreno que no tenía |
| Necesitas cortar el lab | Lo mínimo es `api-conventions.md` acotada y comprobada con el paso 6. `code-style.md` y `testing.md` se terminan después |
