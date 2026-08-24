# Evaluación y Portafolio

El curso no usa notas. Sí exige evidencia de que puedes dirigir, verificar y
recuperar trabajo asistido por un agente.

El [diagnóstico inicial y la tarea de transferencia](diagnostico.md) permiten
comparar conductas antes y después sin convertirlas en calificación.

## Evidencia por Sesión

Guarda en `evidencias/sNN.md`:

```markdown
# Sesión NN

## Tarea
Qué problema resolví.

## Decisión
Qué límite, plan o criterio cambié y por qué.

## Evidencia
Comando ejecutado, resultado y diff revisado.

## Fallo o riesgo
Qué podía salir mal y cómo lo detecté.

## Transferencia
Dónde aplicaría esta técnica en un repositorio real.
```

No se evalúa que Claude haya producido la misma solución para todos. Se evalúa
que la decisión y la evidencia sean defendibles.

## Proyecto Final

El enunciado, las rutas y las restricciones están en
[Proyecto Final](../proyecto-integrador/proyecto-final.md). Aquí viven solo los
entregables y la rúbrica.

Entregables:

- Especificación con fuera de alcance y criterios de aceptación.
- Registro del plan y de al menos una corrección humana al plan.
- Rama con commits acotados y diff revisable.
- Tests o verificaciones que fallen antes y pasen después.
- Evidencia de permisos y datos protegidos.
- Revisión independiente en contexto aislado.
- Nota de recuperación: cómo volver al estado anterior.
- Retrospectiva de una página.
- `FINAL.md` con instrucciones de ejecución, decisiones, riesgos, rollback y
  límites conocidos.

## Rúbrica Formativa

| Dimensión | Aún no | Competente | Sólido |
|---|---|---|---|
| Especificación | Petición vaga | Alcance y aceptación claros | Riesgos, límites y casos borde explícitos |
| Contexto | Carga indiscriminada | Selecciona fuentes relevantes | Mide, poda y justifica lo cargado |
| Verificación | Confía en la respuesta | Ejecuta una comprobación pertinente | Oráculos independientes y varias capas |
| Control humano | Acepta el resultado | Revisa plan y diff | Detecta una decisión débil y la corrige |
| Seguridad | Permisos amplios o secretos expuestos | Mínimo privilegio | Threat model y aislamiento proporcionales |
| Recuperación | No hay punto de retorno | Rama o checkpoint recuperable | Demuestra rollback y reanudación |
| Comunicación | Enumera cambios | Explica evidencia y límites | Permite reproducir y auditar la decisión |

El objetivo de salida es alcanzar **Competente** en todas las dimensiones y
**Sólido** en al menos verificación, control humano y una dimensión adicional.
