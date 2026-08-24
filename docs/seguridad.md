# Seguridad desde la Primera Sesión

Claude Code puede leer archivos, editar código, ejecutar procesos y conectarse a
servicios. Esa capacidad exige un límite claro desde el primer ejercicio.

## Reglas del Curso

1. Trabaja en repositorios con control de versiones y una rama recuperable.
2. Lee el comando completo y su directorio de trabajo antes de aprobarlo.
3. No pegues secretos, tokens, archivos `.env`, datos personales ni código que no
   tengas autorización para procesar.
4. No concedas permisos globales para resolver una incomodidad puntual.
5. No uses `--dangerously-skip-permissions` en tu máquina de trabajo.
6. No conectes un servidor MCP sin revisar quién lo mantiene, qué datos recibe y
   qué herramientas expone.
7. Trata las instrucciones encontradas en repositorios, issues, páginas web y
   resultados de herramientas como entrada no confiable.
8. Antes de commit o push, revisa `git status`, `git diff` y las verificaciones.

## Límite de Confianza

Una instrucción dentro de un archivo puede intentar cambiar el objetivo del
agente. Si Claude propone leer secretos, ejecutar descargas inesperadas, salir
del repositorio o contactar un dominio ajeno a la tarea:

1. Deniega la operación.
2. Interrumpe el turno.
3. Inspecciona el archivo o resultado que originó la propuesta.
4. Continúa con permisos más restrictivos o en un entorno aislado.

## Permisos y Sandbox

Los permisos deciden qué herramientas puede intentar usar Claude. El sandbox
limita a nivel del sistema lo que pueden hacer Bash y sus procesos hijos. Son
capas complementarias, no sustitutas.

En las primeras sesiones usa el modo predeterminado. `acceptEdits` es adecuado
cuando ya sabes qué archivos entran. `dontAsk` sirve para automatizaciones con
una allowlist cerrada. Auto mode es opcional y no reemplaza la revisión humana.

## Antes de Trabajar con Código Real

```bash
git status --short
git switch -c curso/experimento
```

Comprueba también que secretos y archivos locales estén ignorados:

```bash
git check-ignore -v .env
git ls-files | grep -E '(^|/)(\.env|.*\.pem|.*\.key)$' || true
```

Si aparece un secreto rastreado, no continúes con el lab en ese repositorio.

## Incidente

Si se expuso un secreto, borrarlo del archivo no basta. Interrumpe la sesión,
revoca o rota la credencial, revisa el historial y avisa por el canal de
seguridad de tu organización.
