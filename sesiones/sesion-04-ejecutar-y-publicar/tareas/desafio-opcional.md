# Desafío Opcional — Sesión 4

## Instalar la CLI de tu proveedor

**Este desafío es opcional en el nombre.** El Lab 01 de la sesión 5 abre la
solicitud de integración de tu rama desde la conversación, y sin esta
herramienta Claude no puede hacerlo: solo puede publicar y darte una dirección
para que la abras a mano. Hazlo antes de la próxima clase.

## Por qué hace falta

Hoy publicaste tu trabajo por SSH, que es suficiente para mover commits. Pero un
pull request o un merge request no es un commit: es un objeto del proveedor, con
su título, su descripción, su rama base y sus revisores. Git no sabe nada de
eso, así que hace falta la herramienta del proveedor.

Y aquí aparece una idea que el curso repite: **Claude usa las herramientas que tú
tienes instaladas**. No hay que enseñarle nada ni conectarle nada; si `gh` está
en tu máquina y autenticado, Claude puede abrir la solicitud, leer su estado y
comentar en ella, igual que haces tú.

## Elige la tuya

| Proveedor | Herramienta |
|---|---|
| GitHub | `gh` |
| GitLab | `glab` |

Si todavía puedes elegir, la recomendación es **GitHub con `gh`**: está mejor
documentada, es la que verás en la mayoría de equipos y es la que se usa en los
ejemplos del curso. `glab` hace lo mismo y los pasos son equivalentes.

## Qué hacer

1. Instala la herramienta de tu proveedor. En WSL 2 y en Linux se instala desde
   el gestor de paquetes de tu distribución; en macOS, con Homebrew. Consulta la
   documentación oficial de la herramienta para tu sistema.
2. Autentícala con tu cuenta. Las dos abren un flujo en el navegador; no hace
   falta que pegues ningún token en la terminal.
3. Comprueba que quedó autenticada, y que reconoce tu repositorio.

## Comprobación

Desde `~/curso-claude/curso-claude-code-api`, con Claude Code abierto:

```text
Comprueba si tengo instalada y autenticada la CLI de mi proveedor de Git.

Si la tienes disponible, dime con qué cuenta está autenticada, qué repositorio
remoto reconoce desde este directorio y qué ramas ve publicadas.

No abras ninguna solicitud de cambios ni modifiques nada.
```

Has terminado si:

- [ ] La herramienta está instalada y responde.
- [ ] Está autenticada con la cuenta donde publicaste tu repositorio.
- [ ] Reconoce `curso-claude-code-api` desde el directorio del proyecto.
- [ ] Ve publicadas `main` y `feature/persistencia`.
- [ ] Claude pudo usarla sin que le explicaras nada.

Ese último punto es el que importa. Si Claude tuvo que preguntarte cómo se
llamaba la herramienta o qué hacía, algo quedó a medias.

## Si Aparece un Permiso Nuevo

Es lo normal: la configuración que escribiste en el Lab 02 salió de la lista de
comandos del Lab 01, y esta herramienta no estaba ahí. Tienes dos salidas y las
dos son válidas:

- Aprobar esta vez y dejar la regla para cuando sepas qué subcomandos usas de
  verdad.
- Añadir una regla acotada a los subcomandos de solo lectura, y dejar fuera los
  que crean o integran solicitudes de cambio.

Lo que no conviene es abrir la herramienta entera con un patrón amplio. Crear
una solicitud de integración es exactamente el tipo de acción que quieres que te
pregunte.

## Si No Llegas

No te quedes fuera de la sesión 5 por esto. Si la instalación se atasca, avísalo
antes de la clase en lugar de callarlo: la solicitud de cambios también se puede
abrir desde el navegador, y con eso puedes seguir la sesión. Pierdes la parte
interesante —dirigir la revisión desde la conversación— y ganas trabajo manual,
pero no te quedas sin hacer el laboratorio.
