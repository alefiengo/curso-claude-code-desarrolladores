# Lab 04: Después no es Antes

## Objetivo

Añadir un segundo hook que actúe **después** de editar el código, comprobar
con un caso real que no puede impedir nada, y entregar la sesión completa.

## Por qué este lab

El hook del Lab 03 te avisa tarde a propósito: en el commit, cuando ya
escribiste todo. Sería más cómodo que la especificación se regenerara en
cuanto tocas un endpoint, sin esperar al final.

Eso existe, y es otro evento: uno que se dispara **después** de que la
herramienta ya hizo su trabajo. Ese "después" no es un detalle de nombre. Es
la diferencia entre un guardarraíl y un aviso, y hoy la vas a comprobar en
vez de creerla.

## Requisitos

- Lab 03 terminado, en `feature/descripcion`, sin publicar: el hook que
  bloquea el commit, configurado y probado en los dos sentidos.

## Ritmo de Trabajo

Este lab tiene 25 minutos:

| Min | Debe existir |
|---:|---|
| 0–3 | Decidido qué debe pasar al editar un modelo, y qué no puede pasar |
| 3–10 | El segundo hook configurado, y visto en `/hooks` junto al primero |
| 10–15 | Comprobado que se dispara: la especificación se regenera sola |
| 15–20 | Comprobado que **no puede** bloquear, con el archivo ya escrito delante |
| 20–25 | La sesión entregada e integrada |

**Si necesitas cortar aquí:** lo mínimo es el segundo hook configurado y la
comprobación de que se dispara. La entrega se termina después.

## Paso a Paso

### 1. Decidir qué se le puede pedir a este evento

```text
En este proyecto hay dos descripciones generadas: openapi.json, que sale de
un comando, y docs/esquema.md, que lo produce la skill describir-esquema.
Si quiero que algo se regenere automáticamente justo después de que edites un
modelo, ¿cuál de las dos puede hacerlo un hook que ejecuta un comando de
shell, y cuál no? Explícame por qué.
```

Lo que tiene que haber ocurrido: `openapi.json` sí, porque su regeneración es
un comando. `docs/esquema.md` no, porque lo produce una skill, y una skill se
invoca en la sesión, no desde un comando de shell. Con un hook de comando, lo
más que puedes hacer por ese archivo es avisar de que quedó viejo.

Puede que Claude te diga además que un hook no está obligado a ser un
comando: la documentación lista otros tipos, entre ellos uno que manda un
prompt y otro que lanza un subagente —este último marcado como experimental—.
Es cierto, y hoy no lo usas: los subagentes son la sesión 9. Quédate con el límite del tipo que sí vas a
configurar: un comando de shell no invoca skills.

### 2. Configurar el segundo hook

```text
Configura en .claude/settings.json un segundo hook, en el evento que se
dispara justo después de que una herramienta de edición termina, y solo
cuando el archivo editado sea uno de los que afectan a la especificación.

Que haga dos cosas: regenerar openapi.json, y avisar de que docs/esquema.md
puede haber quedado viejo, nombrando la skill que lo regenera.

Enséñame el archivo antes de guardarlo, y confírmame el nombre exacto del
evento y cómo filtra por el archivo editado.
```

Revisa antes de guardar que el filtro no cubra cualquier edición: si se
dispara al editar un archivo de documentación, vas a regenerar la
especificación sin motivo.

### 3. Comprobar que cargó y que se dispara

```text
/hooks
```

Los dos hooks tienen que aparecer, cada uno con su evento. Fíjate en que son
eventos distintos: no es el mismo hook con dos comportamientos.

```text
Cambia el texto de descripción de un endpoint cualquiera, solo la
descripción. No regeneres nada a mano.
```

Después de la edición, mira el `/diff`: `openapi.json` tiene que aparecer
modificado sin que se lo pidieras, y el aviso sobre `docs/esquema.md` tiene
que haber salido.

### 4. Comprobar que no puede impedir nada

Aquí está la lección del lab, y es una comprobación, no una afirmación.

```text
Sin tocar el evento ni el filtro, haz que la comprobación de este segundo
hook falle a propósito —apúntala un momento a un comando que no existe—,
edita otra vez la descripción de ese endpoint, y después muéstrame git diff
del archivo que editaste.
```

Lo que tiene que haber ocurrido: el hook protestó, y **la edición está
igualmente en el archivo**. Cuando este evento se dispara, la herramienta ya
terminó: lo escrito está escrito. Puede avisar, puede dejar un mensaje, puede
ejecutar algo más — no puede deshacer ni impedir.

Devuelve el hook a su forma buena antes de seguir. Y quédate con la frase que
resume las dos capas de hoy: **el evento de antes decide si algo ocurre; el
de después solo reacciona a que ya ocurrió.**

### 5. Entregar la sesión

Deshaz la descripción que cambiaste como caso de prueba, revisa el `/diff`
completo, y entrega:

```text
Publica feature/descripcion, abre la solicitud de cambios hacia main con la
descripción de siempre —qué cambia, qué se decidió y por qué, cómo se
comprueba, qué queda sin probar—, y enséñamela antes de crearla.
```

En "qué se decidió y por qué" hay dos decisiones concretas de hoy: cuál
documento mandaba en cada diferencia del Lab 01, y por qué la comprobación
del commit es un hook y no una regla de permisos.

Revísala e intégrala.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué hooks hay configurados, con su evento y su filtro.
3. Si openapi.json coincide con lo que genera el código.
4. uv run pytest -q y uv run ruff check .
5. Los commits de main que no estaban al empezar el Lab 01, uno por línea.
6. Si queda alguna rama sin integrar.
```

El lab está completo si:

- [ ] Los dos hooks están confirmados y `/hooks` los muestra en eventos distintos.
- [ ] Al editar un endpoint, `openapi.json` se regeneró sin que lo pidieras.
- [ ] Comprobaste, con `git diff` delante, que el hook de después no pudo impedir una edición.
- [ ] Sabes decir en una frase la diferencia entre los dos eventos.
- [ ] Ninguna de las dos descripciones de prueba quedó en la rama.
- [ ] `main` integra `openapi.json`, `docs/esquema.md`, la skill y los dos hooks.

## Limpieza

```text
Detén los contenedores del proyecto sin eliminar volúmenes.
```

Antes de cerrar, `/context`: hoy dos hooks se dispararon varias veces sin que
tú los invocaras, y conviene que veas si eso se nota en lo que llevas gastado.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El segundo hook no se dispara al editar | Mira `/hooks` primero. Si está, revisa el filtro: puede estar esperando un nombre de herramienta que no es la que hizo la edición |
| Se dispara con cualquier archivo, incluso documentación | El filtro es demasiado ancho. Acótalo a los archivos de los que sale la especificación |
| El aviso sobre `docs/esquema.md` no aparece | Comprueba por dónde escribe el hook su mensaje: no todo lo que imprime un hook llega al mismo sitio. Pídele que te diga por qué canal lo manda |
| Al hacer fallar el hook a propósito, la edición se revirtió | Sería un resultado inesperado y vale la pena mirarlo despacio: comprueba con `git diff` y `git status` si de verdad se revirtió, o si lo que ves es otro cambio. La documentación oficial dice que en este evento la herramienta ya se ejecutó |
| El hook del Lab 03 bloquea todos tus commits mientras pruebas | Es el guardarraíl haciendo su trabajo: regenera la especificación antes de confirmar, o confirma primero el cambio de configuración y después el resto |
| Necesitas cortar el lab | Lo mínimo es el segundo hook configurado y comprobado que se dispara. La comprobación del paso 4 y la entrega se terminan después |
