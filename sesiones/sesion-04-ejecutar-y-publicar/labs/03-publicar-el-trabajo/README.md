# Lab 03: Publicar el Trabajo

## Objetivo

Publicar tu repositorio en un remoto propio y leer el historial que escribiste
hoy como lo leería alguien que no estuvo en la sesión.

## Por qué este lab

Hasta ahora todo lo que has hecho vive en tu disco. Los mensajes de commit que
aprobaste en el Lab 01 eran notas para ti, y mientras nadie más los lea, no hay
forma de saber si sirven.

Al publicar cambia el lector. Ese historial pasa a ser la única explicación
disponible para quien llegue después, y ahí se nota una cosa que en local no se
ve: un mensaje escrito por un agente que acaba de hacer el cambio describe el
**qué** con precisión y se salta el **por qué**, que es justo lo que no se
deduce del diff.

De paso, este lab pone a prueba lo que escribiste en el Lab 02. Publicar quedó
en `ask`, así que Claude va a tener que preguntarte antes de hacerlo, una vez y
con un motivo.

## Requisitos

- Labs 01 y 02 terminados, con sus commits en `feature/persistencia`.
- Una cuenta de GitHub o de GitLab, con la sesión iniciada en el navegador.
- Claude Code abierto en el repositorio.

## Ritmo de Trabajo

Este lab tiene 30 minutos:

| Min | Debe existir |
|---:|---|
| 0–8 | Una llave de acceso creada y registrada en tu cuenta, y la conexión probada |
| 8–13 | Un repositorio remoto vacío y privado, con su dirección copiada |
| 13–20 | El remoto conectado y `main` publicado |
| 20–24 | `feature/persistencia` publicada, sin integrar |
| 24–30 | Tu historial leído desde el navegador, y una conclusión sobre tus mensajes |

## Paso a Paso

### 1. Preparar la llave de acceso

Tu máquina tiene que poder identificarse ante el proveedor sin que escribas una
contraseña en cada operación. Pídeselo a Claude:

```text
Comprueba si ya tengo una clave SSH en ~/.ssh y si hay un agente cargándola.

Si no tengo ninguna, crea una clave ed25519 sin frase de paso, con mi correo
como comentario, y enséñame la clave pública para que la registre en mi cuenta.

No modifiques nada del repositorio.
```

Sin frase de paso es lo razonable para el curso: con ella, cada operación te
pediría escribirla o montar un agente, y eso son minutos que hoy no tenemos. En
un equipo de trabajo la decisión es la contraria, y por eso conviene que sepas
que la estás tomando y no que te la encuentres tomada.

Copia la clave **pública** —la que termina en `.pub`, la que Claude te acaba de
enseñar— y regístrala en tu cuenta:

- **GitHub:** ajustes de la cuenta, sección de claves SSH, añadir una nueva.
- **GitLab:** preferencias del usuario, sección de claves SSH, añadir una nueva.

Vuelve y comprueba que la conexión funciona:

```text
Comprueba que mi máquina se autentica contra el proveedor por SSH y dime
exactamente qué respondió.
```

Una respuesta que te salude por tu nombre de usuario y diga que el acceso por
shell no está permitido **es la respuesta correcta**: significa que la
autenticación funcionó.

### 2. Crear el repositorio remoto

Esto se hace en el navegador, porque sin la CLI del proveedor no hay otra forma.
Crea un repositorio nuevo con estas tres condiciones:

| Condición | Por qué |
|---|---|
| **Privado** | Es tu trabajo del curso, no un ejemplo público |
| **Vacío** | Sin README, sin `.gitignore` y sin licencia. Si el remoto nace con un commit que tú no tienes, tu primer push será rechazado |
| Nombre `curso-claude-code-api` | Para que coincida con el local y no te confundas más adelante |

Copia su dirección **SSH**, la que empieza por `git@`. La de HTTPS no te sirve
con la llave que acabas de registrar.

### 3. Conectar y publicar `main`

Antes de publicar, comprueba que tu propia regla sigue en pie:

```text
/permissions
```

Publicar debe aparecer en la lista de lo que se pregunta. Ahora sí:

```text
Pídeme la dirección SSH de mi repositorio remoto y añádela como origin.

Después publica la rama main y déjala como rama de seguimiento. Enséñame el
resultado y los remotos configurados.
```

Cuando llegue al momento de publicar, Claude **te va a preguntar**. Eso no es el
comportamiento por defecto: es tu regla del Lab 02 funcionando. Fíjate en que te
pregunta una vez, por algo que sale de tu máquina, en vez de veinte veces por
cosas que no salían de ella.

`main` va primero a propósito. El primer push a un repositorio vacío fija su
rama por defecto, y además la sesión 5 necesita una rama base contra la que
abrir la solicitud de integración.

### 4. Publicar la rama de trabajo

```text
Publica ahora feature/persistencia en el mismo remoto y dime qué ramas existen
en origin. No la integres en main ni hagas merge de nada.
```

La rama se queda publicada y sin integrar. Hoy no la fusionas: integrar es
aceptar el cambio, y aceptar un cambio sin revisarlo es exactamente lo que el
curso no enseña. La revisión y la integración son el trabajo de la sesión 5, con
una solicitud de cambios de por medio.

### 5. Leer tu historial desde fuera

Abre el repositorio en el navegador y mira la lista de commits de
`feature/persistencia`. Léela como si acabaras de entrar al equipo.

Ahora una prueba honesta de si esos mensajes comunican algo:

```text
Lee únicamente los mensajes de commit de feature/persistencia, sin abrir ningún
diff ni ningún archivo. Para cada uno, dime qué crees que cambió y qué decisión
crees que se tomó.

Si un mensaje no te permite saberlo, dilo en vez de deducirlo del contexto.
```

Compara sus respuestas con lo que de verdad hiciste. Los mensajes que Claude
reconstruye bien están cumpliendo su función; los que no, describen el cambio
pero no la decisión.

Quédate con uno concreto: **cuál de tus commits no se entiende sin haber estado
hoy aquí**. Esa es la respuesta que cierra la sesión.

Cuando termines, mira `/context` y cierra la sesión con `/exit`. El trabajo de
hoy ya no vive en la conversación: vive en el repositorio, y eso es justamente
lo que acabas de comprobar.

## Validación

```text
Sin cambiar nada, dime:

1. Los remotos configurados y su dirección.
2. Qué ramas existen en origin.
3. Si main y feature/persistencia locales coinciden con las publicadas.
4. Los commits de feature/persistencia que no están en main, uno por línea.
5. Si el árbol de trabajo está limpio.
```

El lab está completo si:

- [ ] El repositorio remoto existe, es privado y nació vacío.
- [ ] `origin` apunta a una dirección SSH y la autenticación funciona.
- [ ] `main` está publicada y es la rama por defecto del remoto.
- [ ] `feature/persistencia` está publicada y **no** integrada.
- [ ] Claude te preguntó antes de publicar, por la regla que escribiste en el Lab 02.
- [ ] Abriste el repositorio en el navegador y leíste el historial desde ahí.
- [ ] Sabes decir cuál de tus commits no se entiende sin ti.

## Limpieza

Pídele que deje los contenedores parados sin tocar los datos:

```text
Detén los contenedores del proyecto sin eliminar volúmenes y confírmame que el
volumen sigue existiendo.
```

La sesión 5 continúa sobre estos mismos datos y sobre esta misma rama.

## Problemas Frecuentes

| Situación | Qué hacer |
|---|---|
| El push se rechaza y menciona historiales que no coinciden | El repositorio remoto no nació vacío: tiene un commit inicial que tú no tienes. No fuerces el push. Bórralo y créalo otra vez sin README, sin `.gitignore` y sin licencia |
| `Permission denied (publickey)` | La clave pública no está registrada en la cuenta, o registraste la privada por error. La pública es la que termina en `.pub`. Pídele a Claude que te la vuelva a enseñar y compárala carácter a carácter con la que guardaste |
| Te pide una frase de paso en cada operación | Tu clave tiene frase de paso. Para hoy, la salida rápida es crear una segunda clave sin ella y registrarla; después de clase decide cómo quieres trabajar |
| `remote origin already exists` | Ya habías conectado un remoto antes. Pídele que te enseñe a dónde apunta y que lo sustituya si no es el que acabas de crear |
| Claude no te preguntó antes de publicar | Tu regla de publicar no está activa o está mal escrita. Compruébalo en `/permissions`: publicar debe estar en la lista de lo que se pregunta, no en la de lo que se permite |
| Claude te pide permiso para cosas que creías cubiertas | Normal: la configuración del Lab 02 salió de la lista del Lab 01, y hoy aparecen comandos que ese lab no ejecutó. Una configuración de permisos envejece con el trabajo; se corrige cuando estorba, no antes |
| Claude dice que no puede mirar `~/.ssh` | Ese directorio está fuera de la carpeta del proyecto, así que sus herramientas de archivo no llegan. Pídeselo como comando de shell: listar el directorio y mostrar el contenido del archivo que termina en `.pub` |
| Usas GitLab y los menús no coinciden | Los pasos son los mismos: clave SSH en las preferencias del usuario, proyecto nuevo privado y sin archivos iniciales, y la dirección SSH del proyecto |
