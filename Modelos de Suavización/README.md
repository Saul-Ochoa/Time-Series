# Modelos de Suavización 

## Modelo de Suavizacion Exponencial Simple

El modelo de suavización exponencial simple es una técnica de análisis de series temporales utilizada para predecir valores futuros en función de los datos históricos de la serie. Este modelo asume que la serie temporal exhibe un patrón exponencial y se utiliza para suavizar la variabilidad de la serie temporal al estimar una media móvil ponderada exponencialmente.

El modelo de suavización exponencial simple se calcula a partir de la siguiente fórmula:

Yt+1 = α* Xt + (1-α)*Yt

donde:

Yt+1: es la predicción para el período siguiente.
α: es el factor de suavización que toma valores entre 0 y 1 y determina el peso que se le da a los valores históricos en la predicción.
Xt: es el valor de la serie temporal para el período t.
Yt: es el valor suavizado de la serie temporal para el período t.
El modelo comienza con la estimación del primer valor suavizado, Y1, que generalmente se toma como el primer valor observado de la serie. A partir de ahí, se pueden utilizar las fórmulas anteriores para calcular la predicción para el siguiente período, Y2, y así sucesivamente.

El factor de suavización, α, es un parámetro crítico en el modelo de suavización exponencial simple. Si se elige un valor de α cercano a cero, se le da mayor peso a los valores históricos de la serie temporal y la predicción se ajustará más a los datos históricos. Por otro lado, si se elige un valor de α cercano a uno, se le da mayor peso a los valores recientes de la serie temporal y la predicción se ajustará más a los cambios recientes en la serie temporal.

En resumen, el modelo de suavización exponencial simple es un método útil para pronosticar valores futuros en función de los datos históricos de una serie temporal. Sin embargo, como con cualquier modelo de pronóstico, los resultados pueden ser imprecisos si la serie temporal tiene patrones complejos o cambia de manera inesperada. Por lo tanto, es importante considerar cuidadosamente los datos y ajustar el modelo según sea necesario.El modelo de suavización exponencial simple es una técnica de análisis de series temporales utilizada para predecir valores futuros en función de los datos históricos de la serie. Este modelo asume que la serie temporal exhibe un patrón exponencial y se utiliza para suavizar la variabilidad de la serie temporal al estimar una media móvil ponderada exponencialmente.

El modelo de suavización exponencial simple se calcula a partir de la siguiente fórmula:

Yt+1 = α* Xt + (1-α)*Yt

donde:

Yt+1: es la predicción para el período siguiente.
α: es el factor de suavización que toma valores entre 0 y 1 y determina el peso que se le da a los valores históricos en la predicción.
Xt: es el valor de la serie temporal para el período t.
Yt: es el valor suavizado de la serie temporal para el período t.
El modelo comienza con la estimación del primer valor suavizado, Y1, que generalmente se toma como el primer valor observado de la serie. A partir de ahí, se pueden utilizar las fórmulas anteriores para calcular la predicción para el siguiente período, Y2, y así sucesivamente.

El factor de suavización, α, es un parámetro crítico en el modelo de suavización exponencial simple. Si se elige un valor de α cercano a cero, se le da mayor peso a los valores históricos de la serie temporal y la predicción se ajustará más a los datos históricos. Por otro lado, si se elige un valor de α cercano a uno, se le da mayor peso a los valores recientes de la serie temporal y la predicción se ajustará más a los cambios recientes en la serie temporal.

En resumen, el modelo de suavización exponencial simple es un método útil para pronosticar valores futuros en función de los datos históricos de una serie temporal. Sin embargo, como con cualquier modelo de pronóstico, los resultados pueden ser imprecisos si la serie temporal tiene patrones complejos o cambia de manera inesperada. Por lo tanto, es importante considerar cuidadosamente los datos y ajustar el modelo según sea necesario.


## Modelo de suavización exponencial doble (HOLT)

El modelo de suavización exponencial doble, también conocido como modelo Holt, es una técnica de análisis de series temporales que se utiliza para predecir valores futuros en función de los datos históricos de la serie. A diferencia del modelo de suavización exponencial simple, este modelo asume que la serie temporal exhibe tanto un patrón de tendencia como un patrón estacional, lo que lo hace más adecuado para pronosticar series que tienen una tendencia no lineal y/o una estacionalidad.

El modelo de suavización exponencial doble se calcula a partir de dos fórmulas: una para estimar el nivel de la serie y otra para estimar la tendencia. La fórmula para estimar el nivel es similar a la del modelo de suavización exponencial simple:

St = αYt + (1-α)(St-1 + Tt-1)

donde:

* St: es la estimación del nivel de la serie para el período t.
* α: es el factor de suavización del nivel que toma valores entre 0 y 1 y determina el peso que se le da a los valores históricos en la predicción.
* Yt: es el valor de la serie temporal para el período t.
* St-1: es la estimación del nivel de la serie para el período anterior (t-1).
* Tt-1: es la estimación de la tendencia de la serie para el período anterior (t-1).
La fórmula para estimar la tendencia se calcula a partir de:

Tt = β*(St - St-1) + (1-β)*Tt-1

donde:

* Tt: es la estimación de la tendencia de la serie para el período t.
* β: es el factor de suavización de la tendencia que toma valores entre 0 y 1 y determina el peso que se le da a los valores históricos en la predicción.
* St: es la estimación del nivel de la serie para el período t.
* St-1: es la estimación del nivel de la serie para el período anterior (t-1).
* Tt-1: es la estimación de la tendencia de la serie para el período anterior (t-1).
La predicción para el próximo período se calcula a partir de:

Yt+h = St + h*Tt

donde:

* Yt+h: es la predicción para el período t+h, donde h es el número de períodos hacia el futuro.
* St: es la estimación del nivel de la serie para el período t.
* Tt: es la estimación de la tendencia de la serie para el período t.

En resumen, el modelo de suavización exponencial doble es un método útil para pronosticar valores futuros en función de los datos históricos de una serie temporal que exhibe un patrón de tendencia y estacionalidad. Al igual que con el modelo de suavización exponencial simple, la elección de los valores de los factores de suavización es crítica para obtener pronósticos precisos. Además, este modelo puede requerir ajustes adicionales para considerar otras fuentes de variabilidad en la serie temporal.

## La suavización exponencial triple Holt-Winter

La suavización exponencial triple Holt-Winter es un método de pronóstico utilizado para predecir valores futuros de una serie de tiempo, basado en sus valores históricos. Es una extensión del método de suavización exponencial simple y doble, que utiliza tres parámetros para modelar las tendencias, los patrones estacionales y los efectos de la variabilidad aleatoria.

El método de suavización exponencial triple Holt-Winter utiliza tres ecuaciones para modelar los tres componentes de una serie de tiempo: el nivel, la tendencia y la estacionalidad. El nivel representa el valor medio de la serie, la tendencia representa la dirección y la tasa de cambio de la serie, y la estacionalidad representa los patrones recurrentes que se observan en la serie en un período de tiempo fijo, como un mes o un año.

Nivel:

Nt = α * (Yt - St-m) + (1 - α) * (Nt-1 + Tt-1)

Tendencia:

Tt = β * (Nt - Nt-1) + (1 - β) * Tt-1

Estacionalidad:

St = γ * (Yt - Nt) + (1 - γ) * St-m

Donde:

* Yt: es el valor observado de la serie de tiempo en el momento t
* Nt: es el nivel estimado de la serie de tiempo en el momento t
* Tt: es la tendencia estimada de la serie de tiempo en el momento t
* St: es la estacionalidad estimada de la serie de tiempo en el momento t
* St-m: es la estacionalidad estimada de la serie de tiempo en el mismo período de tiempo del año anterior (o del período de estacionalidad correspondiente)
* α: es el parámetro de suavización del nivel, que controla la importancia relativa de los valores pasados y actuales de la serie de tiempo. Es un valor entre 0 y 1.
* β: es el parámetro de suavización de la tendencia, que controla la importancia relativa de la tendencia pasada y actual de la serie de tiempo. Es un valor entre 0 y 1.
* γ: es el parámetro de suavización de la estacionalidad, que controla la importancia relativa de la estacionalidad pasada y actual de la serie de tiempo. Es un valor entre 0 y 1.
La fórmula para predecir el valor futuro Yt+h de la serie de tiempo en el momento t+h es la siguiente:

Yt+h = Nt + h * Tt + St-m+h-M
Donde:

* h: es el número de períodos de tiempo en el futuro que se quiere predecir
* M: es la longitud del período de estacionalidad de la serie de tiempo (por ejemplo, si la serie es mensual, M=12 para representar el patrón anual de estacionalidad).

Es importante destacar que la elección adecuada de los valores de los parámetros α, β y γ es fundamental para obtener una buena predicción de la serie de tiempo. Esto se logra mediante la evaluación del ajuste del modelo a los datos históricos y la selección de los valores que minimizan el error de predicción.

Una vez que se han estimado los parámetros, se puede utilizar el modelo para predecir valores futuros de la serie de tiempo. La precisión de la predicción dependerá de la calidad de los datos históricos y de la elección adecuada de los parámetros.

En resumen, la suavización exponencial triple Holt-Winter es un método de pronóstico utilizado para predecir valores futuros de una serie de tiempo, que utiliza tres parámetros para modelar los componentes de la serie: el nivel, la tendencia y la estacionalidad.
