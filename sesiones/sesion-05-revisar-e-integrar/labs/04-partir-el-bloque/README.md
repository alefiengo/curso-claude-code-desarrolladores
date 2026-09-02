# Lab 04: El Bloque que Nadie Puede Revisar

## Objetivo

Convertir el bloque de código que acabas de generar en varios commits con una
intención cada uno, escribiendo el criterio del reparto en tu segunda skill, y
entregar el resultado.

## Por qué este lab

Tienes un recurso entero en verde y sin repartir: la migración, el modelo, los
esquemas, las rutas y las pruebas, todo junto. Funciona, y aun así nadie puede
revisarlo. Quien lo abra tiene que entender cinco decisiones a la vez y no
sabría cuál rechazar.

En la sesión 4 esto no te pasó, porque confirmabas cada incremento por separado
antes de empezar el siguiente. Hoy has ganado velocidad y has perdido eso, y el
reparto hay que hacerlo después. Es un trabajo que vas a repetir en todas las
sesiones que quedan, así que hoy lo escribes una vez.

Esta skill es distinta de la anterior en algo concreto: necesita saber qué has
cambiado **en el momento de invocarla**, no cuando la escribiste. Vas a ver cómo
se le pide eso a un archivo.

## Requisitos

- Lab 03 terminado, con la implementación de Proyectos en verde y **sin
  confirmar**.
- La sesión en modo manual.
- La skill del Lab 02 en `.claude/skills/`, ya confirmada.

## Ritmo de Trabajo

Este lab tiene 20 minutos:

| Min | Debe existir |
|---:|---|
| 0–3 | El tamaño real del cambio a la vista y un reparto propuesto, sin confirmar |
| 3–9 | La skill escrita, y la coautoría decidida |
| 9–14 | La skill aplicada y los commits confirmados, con una intención cada uno |
| 14–20 | Entrega integrada y contenedores detenidos |

**Si vas tarde:** este es el tramo más apretado de la sesión. Lo que no puede
faltar es la skill escrita y el reparto hecho, aunque sea con menos commits de
los ideales. La entrega y la integración se terminan fuera de clase; deja `main`
en verde antes de la próxima clase.

## Paso a Paso

### 1. Mirar el tamaño de lo que hay que revisar

```text
/diff
```

Recórrelo hasta el final, aunque sea largo: es la última vez que lo vas a ver
entero. Quédate con cuántas cosas distintas hay ahí dentro.

### 2. Pedir el reparto sin herramienta

```text
Propónme cómo repartir estos cambios en commits. Dime qué archivos van en cada
uno y con qué mensaje. No confirmes nada.
```

Cuando responda, pídelo otra vez con las mismas palabras y compara los dos
repartos.

Puede que coincidan y puede que no: eso depende de la ejecución. Lo que no
cambia es lo importante. En ninguno de los dos casos está escrito **en qué te
basas** para repartir, así que mañana no lo recuerdas, la semana que viene sale
distinto, y quien clone el repositorio no tiene forma de saberlo.

### 3. Escribir la skill

Tú decides el criterio. Estos son los elementos que el reparto de este proyecto
necesita:

```text
Crea una skill de proyecto llamada segmentar-commits. Enséñame el archivo antes
de guardarlo.

Que el procedimiento haga esto:

- Empiece por el estado real del repositorio en el momento de invocarla, no por
  lo que se supone que hay. Inyecta la salida de git status en corto y de git
  diff con el resumen por archivo, no el diff completo: hace falta el mapa del
  cambio, no su contenido.
- Reparta en commits con una sola intención cada uno, en un orden en el que cada
  commit deje el repositorio en un estado comprobable.
- Use Conventional Commits, y elija el prefijo según lo que hace el commit, no
  según el tipo de archivo.
- Me enseñe el reparto propuesto y espere mi aprobación antes de confirmar nada.

Dime también por qué inyectar el resumen y no el diff completo cambia lo que
cuesta invocarla.
```

El punto de esperar tu aprobación no es un adorno: sin él, la skill puede
confirmar sola. Tus reglas de la sesión 4 autorizan `git add` y `git commit`,
así que nadie va a detenerla.

Hay una decisión más que **no va en la skill**. Claude firma sus commits con una
línea de coautoría al final del mensaje, y si no la quieres en tu historial, eso
es una política del repositorio: vale para todos los commits, los haga la skill
o no.

```text
Añade a .claude/settings.json la configuración que oculta la línea de coautoría
de Claude en los mensajes de commit y en las descripciones de las solicitudes de
cambios. Enséñame el archivo antes de guardarlo y confírmame el nombre exacto del
campo.
```

La diferencia entre las dos decisiones es la misma que ya conoces entre una
instrucción y un permiso: el prefijo del mensaje es un juicio que depende
de qué cambió, y va en el procedimiento; la firma es una regla fija, y va en la
configuración.

Los commits que ya hiciste hoy conservan la línea, y eso está bien: una
configuración empieza a aplicar cuando existe, no hacia atrás. Reescribir el
historial para uniformarlo cuesta más de lo que vale.

Ese cambio en `settings.json` se queda sin confirmar, junto al código. No lo
confirmes aparte: es un archivo más para el reparto del paso siguiente, y su
commit propio —una decisión de configuración— es justo el tipo de cosa que un
revisor quiere ver separada del código.

### 4. Aplicarla y corregirla

Comprueba que la sesión la ve:

```text
/skills
```

Esta vez debería aparecer sin recargar nada: `.claude/skills/` ya existía cuando
arrancaste. Ahora invócala:

```text
/segmentar-commits
```

Revisa el reparto que propone. Compáralo con el del paso 2 y con lo que tú
harías. Si algo no encaja —un commit que mezcla la migración con las rutas, un
prefijo que describe el archivo en vez del cambio, o directamente confirmó sin
preguntarte—, el problema no es este reparto: es la skill. Dile qué falló y
pídele que corrija el archivo, no el resultado.

Una skill se estrena mal casi siempre. Corregirla ahora, con un caso real
delante, es más barato que escribirla perfecta antes de haberla usado.

Cuando el reparto te convenza, apruébalo y deja que confirme.

### 5. Entregar e integrar

```text
Publica la rama, abre la solicitud de cambios hacia main con una descripción que
diga qué cambia, qué decisión se tomó, cómo se comprueba y qué queda sin probar.
Enséñame la descripción antes de crearla. No la integres todavía.
```

Ábrela en el navegador y mira una cosa concreta: **la lista de commits**. Eso es
lo que ha cambiado hoy respecto a la entrega del Lab 01. Un revisor puede
aprobar el primero, pedir cambios en el tercero y no tener que opinar sobre los
otros.

Después:

```text
Integra la solicitud de cambios, actualiza main en local, borra la rama
feature/projects en local y en el remoto, y comprueba que la suite sigue verde
en main.
```

Antes de cerrar:

```text
/context
```

Mira cuánto has gastado hoy y en qué. Has dirigido dos entregas, escrito dos
skills y dejado que Claude implementara un recurso entero: sabes lo que cuesta
una sesión así.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy, el modo de permisos activo y si el árbol de trabajo está
   limpio.
2. Los commits nuevos de main, uno por línea, con los archivos de cada uno.
3. En qué commit de hoy deja de aparecer la línea de coautoría de Claude.
4. Qué skills de proyecto hay en el repositorio y en qué commit entró cada una.
5. uv run pytest -q y uv run ruff check .
6. Qué ramas existen en local y en el remoto.
```

El lab está completo si:

- [ ] Existe la skill de segmentación, versionada, y toma el estado del repositorio al invocarse.
- [ ] La skill propone el reparto y espera aprobación antes de confirmar.
- [ ] La corregiste al menos una vez con un caso real delante, o sabes decir por qué no hizo falta.
- [ ] Cada commit de hoy tiene una sola intención, y ninguno mezcla la migración con las rutas.
- [ ] Los mensajes siguen Conventional Commits y el prefijo describe el cambio, no el tipo de archivo.
- [ ] La coautoría está configurada en `.claude/settings.json`, no dentro de la skill.
- [ ] La solicitud de cambios está integrada, `main` está en verde y `feature/projects` ya no existe.
- [ ] Sabes qué parte del contrato de Proyectos sigue sin poder probarse.

## Limpieza

```text
Detén los contenedores del proyecto sin eliminar volúmenes y confírmame que el
volumen sigue existiendo.
```

Los datos no hacen falta: la migración los recrea. Pero borrar el volumen
tampoco aporta nada, y tu regla de la sesión 4 debería impedirlo. No lo pruebes
para verlo.

Deja la sesión en modo manual. Si mañana la retomas en autonomía sin recordarlo,
el primer encargo amplio hará más de lo que esperas.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| Los dos repartos del paso 2 salieron idénticos | Puede pasar. No invalida nada: la pregunta del paso no es si varía, es si el criterio está escrito en algún sitio. No lo está |
| La skill confirmó sin enseñarte el reparto | Le falta el punto de esperar aprobación, o está escrito de forma ambigua. Pídele que deshaga los commits conservando los cambios, corrige el archivo y vuelve a invocarla |
| No sabes cómo se inyecta la salida de un comando en una skill | Pídeselo describiendo qué quieres: que al invocarla llegue ya con el estado del repositorio. Es una línea del archivo, y que te la explique forma parte del paso |
| Inyectaste el diff completo y la invocación se volvió lentísima | Es la lección del paso 3. Cámbialo por el resumen por archivo y compara |
| El campo de la coautoría no es el que esperabas | Hay uno antiguo que todavía funciona y uno vigente. Pídele que compruebe cuál acepta tu versión y que te enseñe el archivo resultante |
| Un commit del reparto deja la suite en rojo | El orden está mal: una prueba llegó antes que el código que la hace pasar, o la migración después del modelo. Pídele que reordene y que compruebe la suite en cada commit |
| El reparto propone un commit por archivo | Demasiado fino: no es un commit por archivo, es un commit por decisión. Dile cuántas decisiones ves tú y pídele que agrupe |
| Se te acabó el tiempo con el reparto a medias | Confirma lo que tengas revisado y termina fuera de clase. `main` en verde es lo único que hace falta |
