# Lab 03: El Guardarraíl que no se Negocia

## Objetivo

Configurar un hook que bloquee un commit cuando `openapi.json` ya no coincide
con el código, probarlo en los dos sentidos, y saber decir por qué esto no se
puede resolver con una regla de permisos.

## Por qué este lab

Ahora mismo nada impide que la deriva vuelva. Cambias una respuesta, no
regeneras la especificación, confirmas, y `openapi.json` queda mintiendo en
`main` sin que nadie se entere hasta que alguien lo lea.

Tienes tres capas para evitarlo y solo una sirve aquí. Una instrucción en
`CLAUDE.md` lo recuerda. Una regla de `.claude/rules/` lo escribe como
convención, y en la sesión 7 comprobaste que Claude la respeta —casi
siempre—. Un permiso decide qué herramienta puede intentarse. Ninguna de las
tres puede decir "solo si esta comprobación pasa", porque las tres deciden
antes de que exista un resultado que comprobar.

## Requisitos

- Lab 02 terminado, en `feature/descripcion`, sin publicar: `openapi.json`
  con su comando de regeneración escrito en el `README.md`, y
  `docs/esquema.md` generado por la skill.

## Ritmo de Trabajo

Este lab tiene 25 minutos:

| Min | Debe existir |
|---:|---|
| 0–4 | La deriva provocada y confirmada: nada la detuvo |
| 4–8 | Descartado que esto sea un permiso, con el motivo por escrito |
| 8–16 | El hook configurado, y visto en `/hooks` con su archivo de origen |
| 16–22 | Probado en los dos sentidos, y el hook confirmado en el caso permitido |
| 22–25 | La deriva del paso 1 deshecha, con la especificación regenerada en el mismo cambio |

**Si necesitas cortar aquí:** llega al menos hasta el caso permitido del paso
5. Si paras después del caso bloqueado, te quedas con el hook sin confirmar y
con la especificación desincronizada, y entonces bloquea todos tus commits
hasta que alguien la regenere.

## Paso a Paso

### 1. Provocar la deriva y ver que nadie la detiene

```text
Cambia el texto de descripción de un endpoint cualquiera —solo la
descripción, nada de comportamiento—, no regeneres openapi.json, y confirma
el cambio.
```

Confirmó sin protestar. Ahora mira el tamaño del problema:

```text
Regenera la especificación en un archivo temporal y compárala con el
openapi.json que acabo de confirmar. Dime si difieren y en qué.
```

Difieren, y el commit ya está hecho. Esa es la deriva, y entró en un turno.

### 2. Descartar que esto sea un permiso

Antes de escribir un hook, comprueba si la capa que ya conoces alcanza:

```text
/permissions
```

Mira tus tres listas de la sesión 4.

```text
Con la sintaxis de permisos de este proyecto, ¿se puede escribir una regla
que permita git commit solo cuando openapi.json coincide con el código?
Respóndeme sí o no, y por qué.
```

Lo que tiene que haber ocurrido: dice que no. Un permiso decide por
herramienta y por argumento, antes de ejecutar nada, y aquí la decisión
depende del **resultado de una comprobación**. Un permiso sabe bloquear
`git commit` siempre; no sabe bloquearlo solo cuando algo está
desincronizado.

Esa es la frontera exacta entre las dos capas, y es la respuesta a la
pregunta que abre la sesión.

### 3. Configurar el hook

```text
Configura en .claude/settings.json un hook que se dispare antes de que se
ejecute un git commit y lo bloquee si openapi.json no coincide con la
especificación que genera el código ahora mismo. Usa el comando de
regeneración que dejamos escrito en el README.md.

Que el mensaje de bloqueo diga qué hacer, no solo que falló. Ponle un
timeout corto: si la comprobación se cuelga, prefiero que falle a que me
deje esperando.

Enséñame el archivo antes de guardarlo, y confírmame el nombre exacto del
evento que usaste y cómo distingue un git commit de cualquier otro comando.
```

Dos cosas que revisar en lo que te enseñe, antes de guardarlo: que el evento
sea el que se dispara **antes** de la herramienta —el que puede bloquear— y
que el filtro no sea solo "cualquier uso de Bash", o cada comando de la
sesión pagará la comprobación.

### 4. Comprobar que cargó

```text
/hooks
```

Es un visor: no configura nada, muestra lo que hay. Busca tu hook, con qué
evento, qué filtro y **desde qué archivo** se cargó. Si no aparece ahí, no
existe para la sesión, por bien escrito que esté el JSON.

### 5. Probarlo en los dos sentidos

El caso bloqueado llega solo, y con una ironía útil: el hook todavía está sin
confirmar, y la deriva del paso 1 sigue ahí.

```text
Confirma el hook en un commit chore:, sin regenerar openapi.json.
```

Lo que tiene que haber ocurrido: el commit no ocurre. El primer commit que tu
guardarraíl bloquea es el suyo, porque la especificación sigue
desincronizada desde el paso 1. Si el commit pasa, vuelve al paso 3: o el
evento no es el que bloquea, o el filtro no está capturando el comando.

El caso permitido:

```text
Regenera openapi.json, y confirma ahora el hook y la especificación
regenerada.
```

Ahora sí confirma. Un guardarraíl que bloquea siempre no es un guardarraíl,
es una pared.

### 6. Dejar limpio, con el guardarraíl puesto

Falta deshacer la descripción que cambiaste en el paso 1: era el caso de
prueba. Pero si deshaces el código y confirmas sin más, la especificación
vuelve a quedar desincronizada —ahora al revés— y **tu propio hook te va a
bloquear**. Es correcto que lo haga, y es la última cosa que este lab te
enseña: el guardarraíl no distingue tu limpieza de tu descuido.

```text
Deshaz la descripción que cambié en el paso 1, regenera openapi.json en el
mismo cambio, y confírmalo.
```

Revisa el `/diff` antes de aprobarlo: tienen que ir juntos el código y la
especificación. Ese es el hábito que el hook está enseñando a la fuerza.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy y si el árbol de trabajo está limpio.
2. Qué hooks hay configurados, con su evento y su filtro, y en qué archivo
   están.
3. Si openapi.json coincide ahora mismo con lo que genera el código.
4. Qué pasó cuando intenté confirmar con la especificación desincronizada, y
   qué pasó después de regenerarla.
5. uv run pytest -q y uv run ruff check .
```

El lab está completo si:

- [ ] El hook está en `.claude/settings.json`, confirmado, y `/hooks` lo muestra con su evento y su filtro.
- [ ] Con `openapi.json` desincronizado, el commit no ocurre y el mensaje dice qué hacer.
- [ ] Con `openapi.json` regenerado, el commit ocurre normalmente.
- [ ] Sabes decir por qué esto no se puede expresar como una regla de permisos.
- [ ] La descripción que cambiaste en el paso 1 ya no está en la rama.

## Limpieza

Ninguna. El Lab 04 añade el segundo hook sobre esta misma configuración.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El commit pasa aunque la especificación esté desincronizada | Mira `/hooks`: si el hook no aparece, el JSON no cargó. Si aparece, el filtro no está capturando el comando, o el evento elegido no es de los que pueden bloquear |
| El hook bloquea absolutamente todo, incluso con la especificación al día | La comprobación devuelve error por otra razón —una ruta, el entorno, la base de datos—. Pídele que ejecute el comando del hook a mano y te enseñe su salida y su código de salida |
| Cada comando de la sesión se volvió lento | El filtro es demasiado ancho: está corriendo la comprobación en cada uso de Bash y no solo antes de un commit |
| El hook te bloquea un commit que sí querías hacer | Casi siempre es correcto: significa que el código y la especificación no van juntos en ese cambio. Regenera y vuelve a confirmar. Si de verdad necesitas confirmar sin la especificación al día, el camino no es pelearse con el hook: es desactivarlo a propósito, confirmar, y volver a activarlo |
| Te preocupa que esto sea una prohibición inviolable | No lo es, y conviene saberlo: un hook es una comprobación que siempre corre en esta sesión, no una barrera del sistema. La documentación oficial es explícita en que, para prohibir algo de plano, la capa correcta son los permisos |
| Confirmas desde otra terminal y el hook no se dispara | Correcto: el hook vive en el ciclo de vida de Claude Code y se dispara antes de una llamada a herramienta. Un comando que tecleas tú fuera de la sesión no es una llamada a herramienta. Si quieres cubrir ese caso, lo que corresponde es un hook de Git, no este |
| Necesitas cortar el lab | No pares en el caso bloqueado: el hook queda sin confirmar y la especificación desincronizada, así que bloquearía todo commit posterior. Llega al caso permitido del paso 5, y deja el paso 6 para después |
