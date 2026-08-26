# Desafío Opcional: Sesión 1

Práctica para reforzar lo visto después de clase. No se entrega y no es requisito para la siguiente sesión.

## Objetivo

Escribir criterios de terminación para dos casos más difíciles que los del laboratorio: uno de rendimiento y uno sobre código tuyo.

## Tiempo Estimado

30 a 45 minutos.

## Por Qué Importa

Los criterios del laboratorio eran binarios: el test pasa o no pasa. Casi ningún
encargo real llega así.

Un criterio de rendimiento obliga a poner un número donde la intuición pondría
"más rápido", y ese número decide también **cuándo parar**: sin él, el agente
sigue optimizando o se detiene en cuanto algo mejora. Y un encargo sobre tu
propio código quita la red que tenía el laboratorio: aquí nadie preparó un
comprobación por ti, y descubrir que no existe es el resultado más útil del desafío.

## Parte 1: Un criterio numérico

En el Lab 02 quedó un problema sin tocar. La función `buscar` de `medidas.py`
recorre la lista con dos bucles anidados y descarta todos los pares salvo
`i == j`: hace trabajo cuadrático para un resultado lineal.

### 1. Medir el estado actual

Si ya hiciste la limpieza de la sesión, recupera el archivo desde el material:

```bash
mkdir -p ~/curso-claude/desafio-01 && cd ~/curso-claude/desafio-01
cp $CURSO/sesiones/sesion-01-especificar-y-verificar/labs/02-criterio-falseable/material/medidas.py .
```

Mide el estado actual:

```bash
python3 -m timeit -s "import medidas as m; ms=[m.registrar('sensor%d'%i,20) for i in range(400)]" "m.buscar(ms,'sensor')"
```

Anota el tiempo por iteración.

### 2. Escribir la reformulación

"Mejora el rendimiento" no es un criterio. "Más rápido" tampoco: el agente no sabe cuánto es suficiente.

Escribe una reformulación con las tres partes, usando un **umbral numérico** medido con `timeit`.

### 3. Ejecutar y comprobar

Lanza la tarea y vuelve a medir. Responde:

- ¿El agente ejecutó `timeit` por su cuenta para comprobarse?
- ¿Se detuvo al alcanzar el umbral, o siguió optimizando?
- ¿Qué habría pasado con un umbral imposible, por ejemplo 0.001 ms?

## Parte 2: Código tuyo

Elige un repositorio real en el que trabajes, o uno propio.

### 1. Encontrar tres peticiones vagas

Piensa en tres cosas que le pedirías a un asistente sobre ese código, tal como se te ocurren de forma natural. Escríbelas sin corregirlas.

### 2. Someterlas a la pregunta

Para cada una: **¿cómo sabría el agente que terminó?**

Si no puedes responderlo, la petición no está lista.

### 3. Reformularlas

Reescribe las tres con contexto, alcance y criterio. Presta atención a dos cosas:

- Si el proyecto no tiene con qué medirse, el primer trabajo es **construir esa medida**. Puede que una de tus tres reformulaciones sea "añade tests a X" antes que la tarea que querías.
- Si el criterio se apoya en algo que el agente puede modificar, ciérralo.

### 4. Ejecutar una

Elige la que menos riesgo tenga y lánzala en una rama aparte:

```bash
git switch -c curso/s01-criterio
```

## Preguntas

Escribe las respuestas en tus notas:

- ¿Cuál de tus tres peticiones originales era la más difícil de convertir en criterio? ¿Por qué?
- ¿Alguna resultó imposible de verificar sin construir antes una medida?
- ¿En cuál dejaste el *cómo* abierto y en cuál tuviste que restringirlo? ¿Qué te hizo decidir?

## Comprueba

- [ ] Mediste con `timeit` antes de pedir la mejora, y después.
- [ ] Tu criterio de rendimiento contiene un número, no un adjetivo.
- [ ] Registraste si el agente se comprobó solo o solo afirmó haber mejorado.
- [ ] Las tres peticiones sobre tu código están reformuladas con contexto,
      alcance y criterio.
- [ ] Identificaste al menos una que necesitaba construir antes la medida.
- [ ] Ejecutaste una en una rama aparte, no sobre tu trabajo.

## Limpieza

```bash
rm -rf ~/curso-claude/sesion-01
git switch -        # vuelve a la rama anterior del repositorio propio
```

Si no quieres conservar el experimento, elimina después solo la rama
`curso/s01-criterio` una vez revisado que no contiene trabajo útil.
