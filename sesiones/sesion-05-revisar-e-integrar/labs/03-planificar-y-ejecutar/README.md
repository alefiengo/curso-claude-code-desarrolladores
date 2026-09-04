# Lab 03: Planificar y Ejecutar con Autonomía

## Objetivo

Estrenar tu skill de planificación sobre los proyectos del contrato, y ejecutar
ese plan completo sin aprobar cada acción, sabiendo qué te sigue protegiendo
mientras no mires.

## Por qué este lab

En la sesión 4 dirigiste los incrementos de tu plan, uno por uno, aprobando cada
comando. Salió bien y se llevó casi toda la clase. Hoy haces lo contrario a
propósito: un plan, una aprobación, y la implementación entera de un recurso sin
volver a intervenir.

Eso solo es sensato porque escribiste algo ayer. Cuando dejas de aprobar a mano,
otro modelo revisa las acciones antes de que se ejecuten, pero lo que tú
prohibiste sigue prohibido y lo que pediste que se te preguntara se te sigue
preguntando. Tu `.claude/settings.json` es la razón por la que hoy puedes
trabajar cómodo, y también vas a descubrir dónde se quedó corto.

Vas a usar tres frenos distintos sobre el mismo trabajo, y conviene que veas
para qué sirve cada uno: la skill dice **cómo** se planifica aquí, plan mode
impide tocar archivos **hasta que apruebes**, y tus reglas bloquean lo que no
debe pasar **decida lo que decida** el modelo.

## Requisitos

- Lab 02 terminado, con la skill de planificación en `.claude/skills/` y
  confirmada en `feature/projects`.
- La base de datos levantada, con las migraciones aplicadas.
- `docs/contrato-api.md` a mano: la sección **Proyectos** es lo que hay que
  implementar hoy, y no se amplía.

## Ritmo de Trabajo

Este lab tiene 35 minutos:

| Min | Debe existir |
|---:|---|
| 0–10 | El plan escrito en `docs/`, revisado y confirmado en su commit |
| 10–15 | La ejecución propuesta y aprobada, con la sesión en autonomía |
| 15–28 | Los cinco endpoints de Proyectos implementados y la suite en verde |
| 28–32 | Revisado qué se te denegó mientras no mirabas |
| 32–35 | Sesión de vuelta en modo manual, sin nada confirmado todavía |

## Paso a Paso

### 1. Estrenar la skill

Invócala por su nombre, diciéndole sobre qué planifica:

```text
/planificar-incremento los proyectos, según la sección Proyectos de
docs/contrato-api.md
```

Es probable que te haga una pregunta antes de escribir nada, y no es un fallo:
es el límite que le pusiste en el Lab 02 sobre no dejar decisiones aplazadas. La
pregunta que casi seguro aparece es qué hacer con el borrado de un proyecto,
porque el contrato exige `409` cuando tiene tareas y las tareas todavía no
existen.

La respuesta no la inventas: sale del contrato. El comportamiento acordado se
implementa **igual**, y lo que hoy no se puede comprobar se declara sin probar.
Dilo en una frase y deja que siga.

### 2. Revisar el plan como si lo fueras a ejecutar mañana

El plan está en `docs/`. Léelo entero con cuatro preguntas:

| Pregunta | Qué buscas |
|---|---|
| ¿Cuántos incrementos tiene y qué hace cada uno? | Que se puedan ejecutar en orden, sin que el tercero necesite algo del quinto |
| ¿Cada incremento declara su comprobación? | Un comando ejecutable, no "verificar que funciona" |
| ¿Hay alguna decisión en condicional? | "Se podría", "se propone", "se confirmará más adelante". Eso es una decisión que va a tomar Claude por ti |
| ¿El alcance es el del contrato? | Ni un endpoint más. Si aparece algo de tareas o de fechas, sobra |

Si algo no cuadra, dilo con el hecho delante —"el incremento 2 no dice con qué
comando se comprueba"— en lugar de pedirle que lo revise otra vez.

Cuando te convenza:

```text
Confirma el plan en un solo commit, con Conventional Commits y prefijo docs:.
Propón tú el mensaje y enséñamelo antes de confirmar.
```

### 3. Proponer la ejecución sin poder tocar nada

Ahora entra en el modo que bloquea las ediciones:

```text
/plan implementa el plan completo de docs/, todos sus incrementos
```

Mientras estés aquí, Claude no puede crear ni modificar un archivo: solo puede
leer, investigar y proponerte cómo lo haría. Léelo y compáralo con tu plan: son
dos documentos distintos, y el segundo debería no añadir nada al primero.

Si quieres cambiar algo de lo que propone antes de que empiece, `Ctrl+G` abre la
propuesta en tu editor y puedes editarla ahí mismo.

### 4. Aprobar y dejarlo trabajar

Cuando lo apruebes, Claude te pregunta cómo seguir. Elige la opción que **usa
auto mode**: aprueba el plan y deja la sesión trabajando sin pedirte permiso en
cada paso.

Antes de que empiece, quédate con esto, porque es lo que vas a comprobar en el
paso 5:

- Lo que pusiste en `deny` sigue bloqueado, en este modo y en todos.
- Lo que pusiste en `ask` te va a seguir preguntando, aunque todo lo demás pase
  sin consultarte.
- El resto lo revisa un modelo distinto, que bloquea lo que se sale de lo que
  pediste.

Añade una sola instrucción antes de dejarlo ir:

```text
Implementa todos los incrementos y ejecuta las comprobaciones que declara cada
uno. No hagas commit de nada: quiero revisar el conjunto antes de repartirlo.
```

Esa última frase importa. Confirmar está entre lo que autorizaste ayer, así que
sin decirlo te vas a encontrar el trabajo ya confirmado en un solo commit, y
repartirlo después cuesta más.

Ahora mira. No intervengas salvo que se salga del plan, y si lo hace, `Esc` en
ese turno.

### 5. Comprobar qué pasó mientras no mirabas

Primero el resultado:

```text
Dame el estado de cada punto por separado, sin corregir nada:

1. Qué archivos creaste o modificaste, uno por línea.
2. uv run pytest -q y uv run ruff check .
3. La respuesta de los cinco endpoints de Proyectos contra la API corriendo:
   crear, listar, obtener uno, actualizar parcialmente y borrar. Muestra el
   código de estado y el cuerpo.
4. GET /projects dos veces seguidas, con al menos tres proyectos creados, y si
   los ids salen en la misma posición las dos veces.
5. GET /projects/{id} con un id que no existe. Muestra el código de estado.
6. Qué parte de la sección Proyectos del contrato no quedó comprobada, y por
   qué.

Si algo falla, dime qué falló y detente.
```

Comprueba una cosa que no te va a decir ninguna prueba: que las respuestas
traen **exactamente** los campos del contrato, ni uno más, y que un
`description` ausente vuelve como `null` en vez de desaparecer.

Después, lo que te interesa del modo en el que has estado trabajando:

```text
/permissions
```

Ahí ves las reglas activas y, más importante hoy, **lo que se te denegó durante
la sesión**. Puede que la lista esté vacía, y también es un resultado: significa
que nada de lo que hizo se salió de lo que pediste. Léela con dos preguntas: si
hay algo, ¿la denegación fue acertada?; y si no hay nada, ¿había algo que
debería haberse denegado y pasó?

### 6. Volver a modo manual

```text
Shift+Tab
```

Cicla los modos hasta dejar la sesión en manual. La barra de estado nombra el
modo activo: compruébalo ahí en vez de suponerlo. El Lab 04 revisa y reparte lo que acabas de generar, y eso
se hace mirando cada paso.

No confirmes nada. Lo que tienes ahora es exactamente el material del último
laboratorio: mucho código, en verde, y sin repartir.

## Validación

```text
Sin cambiar nada, dime:

1. En qué rama estoy, el modo de permisos activo y si el árbol de trabajo está
   limpio.
2. Los commits de esta rama que no están en main, uno por línea.
3. Cuántos archivos están modificados o sin seguimiento, y cuántas líneas suman.
4. uv run alembic upgrade head, después downgrade base, después upgrade head.
5. uv run pytest -q y uv run ruff check .
6. Si aparece la palabra sqlite en app, tests o pyproject.toml.
7. Qué comandos ejecutaste durante la implementación sin preguntarme, cuáles me
   preguntaste y si alguno quedó bloqueado. Agrúpalos por herramienta.
```

El lab está completo si:

- [ ] El plan está escrito en `docs/`, con incrementos numerados y una comprobación por incremento.
- [ ] Ninguna decisión del plan quedó en condicional.
- [ ] El plan está confirmado en su propio commit, antes de que existiera el primer archivo de código.
- [ ] Propusiste la ejecución en un modo que no podía editar nada, y la aprobaste tú.
- [ ] Los cinco endpoints de Proyectos responden lo que dice el contrato, con el esquema exacto.
- [ ] Dos llamadas idénticas a `GET /projects` devuelven los ids en la misma posición.
- [ ] `GET /projects/{id}` con un id inexistente responde `404`.
- [ ] La migración sube, baja y vuelve a subir sin error.
- [ ] La suite y el linter están en verde, y no aparece SQLite en ninguna parte.
- [ ] Sabes qué se te denegó mientras trabajabas sin aprobar y si fue acertado, o que no se te denegó nada.
- [ ] Nada está confirmado todavía, salvo el plan.
- [ ] La sesión está de vuelta en modo manual.

## Limpieza

Ninguna. El Lab 04 trabaja sobre estos cambios sin confirmar.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| No te alcanza el tiempo para todos los incrementos | Para en cuanto `GET /projects` responda, aunque falten incrementos. Pídele que anote al final del plan qué queda pendiente y sigue al Lab 04 con lo que tengas: repartir tres commits enseña lo mismo que repartir seis |
| La skill no te pregunta nada y planifica sin más | Mira si el plan deja alguna decisión en condicional. Si la deja, el límite del Lab 02 no está funcionando: dile qué decisión quedó abierta y pídele que corrija la skill, no solo el plan |
| Al aprobar, no aparece la opción de trabajar sin permisos | Ese modo depende del modelo y de la política de tu organización. Elige aprobar revisando cada edición: el lab funciona igual y aprobarás más veces. Anótalo, porque cambia lo que compruebas en el paso 5 |
| Claude confirmó los cambios por su cuenta | Le faltó tu instrucción del paso 4. No reescribas el historial: pídele que deshaga el commit conservando los cambios en el árbol de trabajo, y sigue al Lab 04 |
| Se desvió del plan y añadió endpoints de tareas | `Esc` en ese turno. Dile qué endpoint no está en el plan y pídele que lo retire. Si ya está muy avanzado, `/rewind` devuelve la conversación y los archivos al punto anterior |
| Un incremento falla su comprobación | No pases al siguiente. Dile qué comprobación falló, con la salida delante, y pídele que lo corrija dentro de ese incremento |
| Te pregunta por publicar en medio del trabajo | Es tu regla `ask` de la sesión 4 haciendo su trabajo. Hoy no se publica nada: dile que no |
| `DELETE /projects/{id}` no puede comprobar el `409` | Correcto: no hay tareas todavía. Se implementa el comportamiento del contrato y se declara sin probar, que es lo que hay que hacer con lo que no se puede verificar |
| La migración baja pero no vuelve a subir | El `downgrade` deja algo a medias. Pídele la salida completa de los tres pasos y que corrija la migración, no el test |
| El diff es enorme y no sabes por dónde empezar | Es el punto de partida del Lab 04. No intentes revisarlo entero ahora |
