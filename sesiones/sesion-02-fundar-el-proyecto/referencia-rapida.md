# Referencia Rápida: Sesión 2

## Contrato para Inicializar un Proyecto

| Parte | Pregunta que debe responder |
|---|---|
| Fuente | ¿Qué documento manda sobre el comportamiento? |
| Alcance | ¿Qué archivos y capacidades puede cambiar? |
| Límites negativos | ¿Qué no puede tocar, crear ni leer? |
| Criterios | ¿Qué resultados exactos deben observarse? |
| Proceso | ¿Debe explorar, planificar, esperar aprobación o implementar? |
| Terminación | ¿Qué comandos debe ejecutar antes de declarar éxito? |

Un prompt de inicio describe la entrega actual. No lo copies completo a
`CLAUDE.md`: conserva allí solo decisiones que sigan vigentes en tareas futuras.

## Decidir Dónde Vive una Instrucción

| Pregunta | Destino |
|---|---|
| ¿Debe estar presente en cualquier tarea del repositorio? | `CLAUDE.md` raíz |
| ¿Solo aplica al trabajar en ciertas rutas? | `.claude/rules/` con `paths:` |
| ¿Es personal y local? | `CLAUDE.local.md` ignorado |
| ¿Es un procedimiento que se invoca cuando hace falta? | Skill |
| ¿Debe cumplirse sin depender del modelo? | Permiso o hook |
| ¿Es explicación detallada o referencia? | README o `docs/` |

## Qué Sí Merece `CLAUDE.md`

- Fuentes de verdad y precedencia entre documentos.
- Comandos canónicos que se usan con frecuencia.
- Restricciones arquitectónicas no evidentes.
- Límites de trabajo y datos sensibles.
- Convenciones cuya omisión ya produjo errores.

## Qué No Merece Carga Permanente

- Árbol del repositorio.
- Lista de dependencias.
- Tutoriales completos.
- Estado temporal de una feature.
- Instrucciones de una sola tarea.
- Consejos genéricos como "escribe código limpio".

## Auditoría de una Línea

Para cada instrucción pregunta:

1. ¿Qué error evita o qué búsqueda repetida elimina?
2. ¿Aplica a cualquier tarea?
3. ¿Puede comprobarse si se siguió?
4. ¿Seguirá siendo cierta en tres meses?
5. ¿Necesita orientación o una garantía técnica?

## Comandos

```text
/init       genera o mejora una propuesta; no la confirma por ti
/context    muestra qué ocupa la ventana y qué memoria se cargó
/memory     lista y abre instrucciones cargadas; permite auditar auto memory
```

## Comprobar la Línea Base

```bash
uv sync --locked
uv lock --check
uv run pytest -q
uv run ruff check .
docker compose config -q
git check-ignore .env
git status --short
```

Antes del primer commit añade pruebas negativas:

```bash
git diff --exit-code -- docs/contrato-api.md .gitignore
test ! -e CLAUDE.md
test ! -e .env
```

## Prueba de Calidad

No preguntes "¿te gusta mi `CLAUDE.md`?". Entrégale una propuesta que contradiga
sus reglas y revisa:

- qué conflicto detectó;
- qué fuente citó;
- qué riesgo explicó;
- qué alternativa propuso;
- qué conflicto omitió.

Una omisión es evidencia. Si una regla no admite omisiones, no debe depender solo
de `CLAUDE.md`.
