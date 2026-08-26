# Referencia Rápida: Sesión 1

## El Ciclo

```text
entender → acordar → cambiar → comprobar → revisar
```

No aceptes el cierre por la redacción. Acéptalo por la evidencia y el diff.

## Contrato de Tarea

| Parte | Debe dejar claro |
|---|---|
| Resultado | Comportamiento observable que debe cambiar |
| Fuentes | Ticket, archivo, contrato o patrón que contiene la verdad |
| Alcance | Archivos o componentes que pueden cambiar |
| Restricciones | Compatibilidad, seguridad y decisiones que se conservan |
| Verificación | Comando o evidencia que prueba el resultado |

Plantilla breve:

```text
[RESULTADO] Resuelve...
[FUENTES] Usa @ticket.md y el patrón de...
[ALCANCE] Puedes cambiar... No cambies...
[RESTRICCIONES] Conserva... Queda fuera...
[VERIFICACIÓN] Termina cuando... Al cerrar muestra...
```

## Durante la Ejecución

| Control | Uso |
|---|---|
| `Esc` | Interrumpir y redirigir sin perder la conversación |
| `/diff` | Revisar los cambios producidos en la sesión |
| `/exit` | Salir de Claude Code |

Interrumpe cuando el agente:

- cambia una comprobación que debía conservar;
- toca archivos fuera de alcance;
- elige una interpretación que no acordaste;
- afirma que terminó sin ejecutar la verificación;
- convierte una corrección pequeña en un rediseño.

Redirección útil:

```text
Detente. [hecho observable]. [límite que debe respetarse].
Continúa desde [fuente o comprobación concreta].
```

## Antes de Aceptar

```bash
git status --short                    # todo lo modificado, incluido lo nuevo
git diff --check                      # errores básicos del patch
git diff -- ARCHIVO                   # cambio real
python3 -m unittest -v                # comportamiento y regresión
```

Comprueba cuatro capas:

- [ ] El caso que motivó el cambio pasa.
- [ ] Los casos anteriores siguen pasando.
- [ ] Solo cambiaron archivos justificados.
- [ ] El diff resuelve la causa sin complejidad accidental.

## Reporte de Cierre

Pide siempre:

1. causa con archivo y línea;
2. archivos modificados y motivo;
3. comandos ejecutados y resultado;
4. riesgo residual o trabajo fuera de alcance.

El reporte sirve para orientar la revisión. No sustituye el diff ni los
comandos.

## Errores Comunes

| Error | Corrección |
|---|---|
| "Arregla esto" | Define resultado y fuente |
| "Que quede bien" | Nombra una señal observable |
| "Que pasen los tests" | Confirma que los tests cubren el caso y no deben cambiar |
| Dictar cada línea | Da restricciones y deja abierta la implementación |
| Esperar hasta el final para corregir | Interrumpe al detectar la primera desviación |
| Confiar en "todo listo" | Revisa salida, estado de Git y diff |
