# Condicionales

## Ejercicio 1

En aprendizaje automático, un perceptrón es una neurona artificial que recibe varias entradas (x₁, x₂, ..., xₙ), cada una con un peso asociado (w₁, w₂, ..., wₙ), y un sesgo (b). La salida del perceptrón se obtiene al calcular la combinación lineal de las entradas y luego aplicar una función de activación.

Una función de activación muy utilizada es ReLU (Rectified Linear Unit), que devuelve:

- 0 si la entrada es negativa o cero.

- El mismo valor si la entrada es positiva.
$$
f(x) =
\begin{cases} 
0, & \text{si } x \leq 0 \\
x, & \text{si } x > 0
\end{cases}
$$

Modifica el código del perceptrón de la clase 5 para que use la función de activación ReLU. 
```python
# Pedimos las entradas al usuario
x1 = float(input("Ingresa el valor de x1: "))  # Calificación del primer examen
x2 = float(input("Ingresa el valor de x2: "))  # Calificación del segundo examen
# Definimos los pesos y el sesgo (esto lo puedes modificar según tu modelo)
w1 = 0.5
w2 = 0.7
b = -1.0
# Calculamos la salida del perceptrón
salida = (x1 * w1) + (x2 * w2) + b
# Aplicamos la función de activación ReLU
# Escribe tu código aquí
```

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/iR38Ziv1KsLJ1nA9A)

## Ejercicio 2
En ciencia de datos, muchas veces es necesario clasificar valores númericos en diferentes categorías. Supongamos que tenemos una lista de temperaturas en grados Celsius y queremos categorizarlas de la siguiente manera:

Menos de 15°C - Frío
Entre 15°C y 25°C - Templado

Escribe un programa que pida al usuario una temperatura y le diga si es "Frío" o "Templado". 

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/gNiCzAT9hXXWEZz26)