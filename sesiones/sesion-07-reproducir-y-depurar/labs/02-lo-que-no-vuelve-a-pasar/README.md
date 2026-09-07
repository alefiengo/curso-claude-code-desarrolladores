# Lab 02: Lo que no Vuelve a Pasar

## Objetivo

Escribir las reglas que hubieran detectado antes el fallo del Lab 01, en
`.claude/rules/`, y decidir qué de tu `CLAUDE.md` merece seguir ahí y qué
merece vivir en una regla aparte.

## Por qué este lab

Tu `CLAUDE.md` existe desde la sesión 2 y ha ido creciendo desde entonces:
decisiones de persistencia, de permisos, de skills, de recuperación. Todo
entra al mismo archivo, y todo se carga en cada sesión, aunque hoy no toques
ni una línea de la API.

El fallo del Lab 01 era evitable con una regla escrita, no con más cuidado.
"Antes de corregir, reproduce con un caso real" no depende de qué archivo
tocas. "Ninguna automatización reescribe código para repartir un cambio que
ya existe" tampoco. Hoy las escribes, y compruebas que de verdad cambian lo
que Claude hace, no solo lo que Claude promete.

## Requisitos

- Lab 01 terminado: el fallo de `segmentar-commits` cerrado, en
  `feature/segmentar-commits`, sin publicar.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–5 | Tu `CLAUDE.md` revisado, con lo que es siempre relevante separado de lo que solo aplica a veces |
| 5–15 | `testing.md` y `code-style.md` escritos, con el criterio de hoy |
| 15–22 | `api-conventions.md` escrito y acotado por ruta |
| 22–27 | Las reglas comprobadas: que cargan, y que cambian el comportamiento sin que se lo pidas |
| 27–30 | Todo el trabajo del Lab 01 y del Lab 02 entregado e integrado |

## Paso a Paso

### 1. Mirar qué hay hoy en `CLAUDE.md`

```text
Enséñame el CLAUDE.md del proyecto completo. Para cada sección, dime si
aplica siempre que trabajas en este repositorio, o si solo importa cuando
tocas un tipo de archivo o un procedimiento concreto.
```

No lo edites todavía. Quédate con la lista de lo que Claude marcó como
"solo a veces": es la candidata a moverse.

### 2. Escribir `testing.md`

```text
Crea .claude/rules/testing.md. Que declare: antes de corregir cualquier
fallo reportado, se reproduce primero con un caso real contra el sistema
—un test que se ejecuta en rojo, o una ejecución real que deja evidencia del
fallo— y se corrige después. La corrección nunca oculta esa reproducción:
se queda tal como se escribió. Enséñamelo antes de guardarlo.
```

Esta regla no acota rutas: aplica en cualquier archivo, así que va sin
`paths` en el encabezado.

### 3. Escribir `code-style.md`

```text
Crea .claude/rules/code-style.md. Que declare: ninguna automatización de
este proyecto que reparta o reorganice cambios ya existentes en el árbol de
trabajo reescribe código para simular un estado intermedio. Usa git add,
completo o con git add -p, sobre el cambio que ya existe. Enséñamelo antes
de guardarlo.
```

Es la misma regla que corregiste dentro de `segmentar-commits` en el Lab 01,
pero ahora vale para cualquier skill que el proyecto tenga o vaya a tener,
no solo para esa.

### 4. Escribir `api-conventions.md`, acotado por ruta

Esta sí depende de dónde trabajas. Pídele primero el dato que necesitas:

```text
¿En qué ruta del repositorio viven los endpoints de la API? Dame la ruta
exacta, no una aproximación.
```

Con esa ruta:

```text
Crea .claude/rules/api-conventions.md, con paths apuntando a esa carpeta.
Que declare: cualquier endpoint nuevo o modificado sigue el esquema de
respuesta exacto del contrato —ni un campo de más ni de menos—, y cualquier
campo nuevo se añade en sus tres capas: migración, esquema y validación,
igual que priority en el Lab 01. Enséñamelo antes de guardarlo.
```

### 5. Comprobar que cargan

```text
/context
```

Busca las tres bajo **Memory files**. Si `api-conventions.md` no aparece
ahí, es porque su regla es condicional: solo se carga cuando Claude lee un
archivo de la ruta que le diste. Confírmalo pidiéndole que lea cualquier
archivo de esa carpeta y volviendo a mirar `/context`.

### 6. Probar que `testing.md` cambia algo, no solo que existe

Sin mencionar la regla ni el procedimiento de hoy:

```text
En el endpoint de tareas, el filtro overdue no distingue mayúsculas de
minúsculas en el parámetro de consulta y debería. Corrígelo.
```

Antes de aceptar la corrección, mira qué hizo primero. Lo que tiene que
haber ocurrido: escribió un test que reproduce el comportamiento actual
—incorrecto— y lo ejecutó en rojo, antes de tocar el código. Si corrigió
directo, sin ese paso, la regla no está cargando o no es lo bastante
concreta: ábrela, compara su redacción con la del paso 2, y corrígela.

Revisa el `/diff` completo de este cambio y confirma el fix en su propio
commit.

### 7. Decidir qué se queda en `CLAUDE.md`

Vuelve a la lista del paso 1.

```text
De lo que marcaste como "solo a veces", ¿alguna sección ya quedó cubierta
por testing.md, code-style.md o api-conventions.md? Enséñame cuáles, y
quítalas de CLAUDE.md sin tocar nada más del archivo.
```

Lo que no se solapa con ninguna regla nueva se queda donde está: no todo lo
que no es "siempre" merece su propia regla, y `CLAUDE.md` sigue siendo el
lugar para lo que de verdad aplica a cada sesión.

### 8. Entregar e integrar todo el lab

```text
Publica feature/segmentar-commits, abre la solicitud de cambios hacia main con la
descripción de siempre —qué cambia, qué se decidió y por qué, cómo se
comprueba, qué queda sin probar—, y enséñamela antes de crearla.
```

Revísala: tiene que listar los commits del Lab 01 y del Lab 02 por
separado, cada uno con su propia intención. Intégrala.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué archivos hay en .claude/rules/ y cuál de ellos tiene paths en su
   encabezado.
3. uv run pytest -q y uv run ruff check .
4. Los commits de main que no estaban al empezar el Lab 01, uno por línea.
5. Qué quitaste de CLAUDE.md en el paso 7, y por qué.
```

El lab está completo si:

- [ ] `testing.md` y `code-style.md` existen, sin `paths`, y aplican a todo el repositorio.
- [ ] `api-conventions.md` existe, con `paths` apuntando a la carpeta real de los endpoints.
- [ ] Comprobaste con `/context` que las tres cargan, condicional o no.
- [ ] Le diste una corrección sin mencionar la regla, y siguió el procedimiento de `testing.md` sin que se lo pidieras.
- [ ] `CLAUDE.md` perdió solo lo que ya cubre una regla nueva, nada más.
- [ ] `main` tiene el fallo del Lab 01 y las reglas del Lab 02, integrados desde una sola solicitud de cambios con un commit por intención.

## Limpieza

```text
Detén los contenedores del proyecto sin eliminar volúmenes.
```

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| `api-conventions.md` no aparece nunca en `/context`, ni leyendo archivos de esa carpeta | Revisa que el `paths` use el patrón correcto para tu estructura real, no una ruta inventada. Pídele a Claude que confirme el patrón contra un archivo real de esa carpeta |
| En el paso 6, corrigió directo sin escribir el test primero | La regla no es lo bastante concreta o no cargó. Comprueba primero con `/context` que `testing.md` está en Memory files; si está y aun así no la sigue, hazla más específica —menos "reproduce el fallo", más "escribe y ejecuta el test antes de tocar el código de producción" |
| No sabes qué mover de `CLAUDE.md` en el paso 7 | Vuelve a la respuesta del paso 1. Si Claude no marcó nada como "solo a veces", es un resultado válido: tu `CLAUDE.md` ya estaba bien acotado, y hoy no había nada que mover |
| El `paths` de `api-conventions.md` también captura archivos de test | Puede pasar si tus tests viven junto a los endpoints. Decide si te sirve así o si el patrón necesita excluirlos; cualquiera de las dos es una decisión válida, pero debe ser una decisión, no un accidente |
| Necesitas cortar el lab | Lo mínimo es `testing.md`, comprobada con el paso 6. `code-style.md` y `api-conventions.md` se terminan después |
