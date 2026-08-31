# Proyecto Final: Transferencia

## Propósito

Demostrar que puedes aplicar el método del curso a una capacidad que no aparece
resuelta paso a paso.

## Elige una Ruta

### A. Capacidad nueva de backend

Implementa *Tareas v2* del contrato —`due_at` y el filtro `overdue`—, o añade
etiquetas, asignación o historial de cambios. Debe afectar al menos contrato,
persistencia, API y tests.

### B. Cliente mínimo

Construye un cliente web o CLI **contra el BFF**, no contra la API. Debe
permitir listar, crear, actualizar estado y mostrar errores. El stack es libre,
pero la elección debe justificarse y no ampliar innecesariamente el alcance.

No elijas una tarea que ya resolviste en los labs.

## Restricciones

- Rama propia desde `main`, siguiendo el
  [flujo de trabajo con Git](flujo-git.md) del curso.
- Sin secretos ni acceso a producción.
- Plan revisado antes de implementar.
- Tests o verificaciones independientes.
- Revisión mediante subagente aislado y revisión humana del diff.
- Entrega reproducible desde una máquina limpia.

## Entregables

La lista completa de entregables y la rúbrica están en
[Evaluación y Portafolio](../docs/evaluacion.md). Uno de ellos es propio de este
proyecto: `FINAL.md`, con instrucciones de ejecución, decisiones, riesgos,
rollback y límites conocidos.

## Tiempo Sugerido

4 a 6 horas fuera de clase. Si supera ese límite, reduce alcance; no compenses
una especificación débil aumentando autonomía o esfuerzo del modelo.

## Revisión

La revisión es formativa: puede pedirte cambios, pero no recibe
nota. El listón lo fija la [rúbrica](../docs/evaluacion.md): `Competente` en
todas las dimensiones y `Sólido` en verificación, control humano y una dimensión
más a tu elección.

Y una condición que la rúbrica no puede medir: que puedas defender la evidencia
sin depender de la respuesta final de Claude.
