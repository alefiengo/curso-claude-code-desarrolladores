# Desafío Opcional — Sesión 5

## La Skill que Trabaja Aparte

En el Lab 02 clasificaste tres recomendaciones y construiste una. De las que
sobrevivieron quedó al menos una sin escribir. Constrúyela ahora, con una
condición que no usaste en clase: que se ejecute **en su propio contexto** y te
devuelva solo el resultado.

Este desafío no se entrega y no hace falta para seguir el curso. Lo que te deja
es la tercera herramienta de tu repositorio, y la primera que trabaja sin
ocuparte la conversación.

## Por qué esta condición

Las dos skills de la sesión 5 trabajan dentro de tu conversación, y así tenía
que ser: el plan y el reparto de commits son cosas que necesitas tener delante
para seguir dirigiéndolas.

Hay trabajo que no es así. Arrancar la API, llamar a cinco endpoints, comparar
cada respuesta con el contrato y decir si cumple genera un muro de texto: cinco
peticiones, sus cabeceras, sus cuerpos y la salida del servidor. De todo eso te
interesa **una línea**: cumple o no cumple, y qué falló. El resto se queda
ocupando tu ventana de contexto durante el resto de la sesión.

Una skill puede declarar en su cabecera que se ejecute aparte, con su propia
ventana. Hace el trabajo, lee lo que necesite y te devuelve la conclusión. Lo
que leyó no vuelve contigo.

Aquí lo usas para ahorrar contexto. La misma idea sirve para otra cosa distinta:
cuando lo que necesitas no es ahorrar, sino un juicio que **no sepa** cómo
llegaste hasta aquí.

## Qué hacer

1. **Elige.** Vuelve a tu clasificación del Lab 02 y toma la que marcaste como
   **trabajo aparte**, que es exactamente lo que este desafío construye. Si no
   marcaste ninguna así, vale cualquiera que sobreviviera y no construyeras hoy.
   Y si las tres se rechazaron, la candidata evidente es una que verifique un
   recurso completo contra el contrato: es lo que hiciste a mano en el Lab 01 con
   `/states` y en el Lab 03 con `projects`.

2. **Averigua cómo se declara.** Pídele a Claude qué opción de la cabecera de un
   `SKILL.md` ejecuta la skill en su propio contexto, y que te enseñe la
   documentación oficial de donde lo saca. No te fíes de la primera respuesta si
   no viene con la fuente: la instalación te dice si algo existe, y la
   documentación qué significa. Ninguna de las dos basta sola.

3. **Escríbela** en `.claude/skills/`, en una rama propia, con un límite claro:
   verifica y **no corrige**. Una skill de verificación que arregla lo que
   encuentra deja de servir para verificar, porque ya no puedes distinguir qué
   estaba bien de qué acaba de arreglar.

4. **Pruébala dos veces.** Una con la API en verde: debe decir que cumple. Otra
   habiendo roto algo a propósito —quita un campo de un esquema de respuesta, o
   cambia un código de estado— y comprueba que lo detecta y que **no lo repara**.
   Deshaz el destrozo después.

5. **Compara el coste.** Mira `/context` antes y después de invocarla. Después
   pídele que haga el mismo trabajo sin la skill, en la conversación, y vuelve a
   mirar. La diferencia es el argumento de todo este desafío.

6. **Confírmala** en su propia rama, con Conventional Commits y prefijo `chore:`,
   y déjala publicada o intégrala: como prefieras. Ya sabes hacer las dos cosas.

## Cómo saber si salió bien

- La skill existe en `.claude/skills/` y `/skills` la reconoce.
- Su cabecera declara que se ejecuta en contexto aislado, y sabes decir en qué
  página de la documentación oficial lo comprobaste.
- Detecta un incumplimiento del contrato y no lo arregla.
- Con la API en verde dice que cumple, sin inventar problemas.
- Sabes cuánto contexto te ahorró, con el número delante.

## Si Te Atascas

| Situación | Qué hacer |
|---|---|
| No encuentras la opción de la cabecera | Pídele que te enseñe la página de la documentación oficial sobre skills y que busque ahí la parte de ejecución aislada. Si no aparece en tu versión, dilo y para: comprobar que algo no existe en tu instalación también es un resultado |
| La skill te devuelve el muro de texto igual | Entonces no se está ejecutando aparte, o le pediste que te lo enseñara todo. Revisa la cabecera y el último párrafo del procedimiento |
| Arregla lo que encuentra | Le falta el límite. Corrige el archivo y vuelve a probarla con el mismo destrozo |
| Dice que cumple cuando has roto algo | Está comprobando el código en vez de las respuestas. Pídele que verifique contra la API corriendo, no leyendo los archivos |
| `/context` no muestra diferencia | Puede que el trabajo fuera demasiado pequeño para notarse. Prueba con los cinco endpoints de proyectos, no con uno |
