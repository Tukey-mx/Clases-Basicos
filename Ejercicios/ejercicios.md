# 2. Introducción a la línea de comandos
## Ejercicio 2.1
Crea la siguiente estructura de directorios y archivos:

```bash
Ejercicio
|
|
|---------->Carpeta1
|          |
|          |------->programa1.py
|
|---------->Carpeta2
           |
           |------->Carpeta3
           |         |
           |         |------->hola.py
           |
           |------->adios.txt
```


Escribe los comandos necesarios para crear la estructura de directorios y archivos mencionada.

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/PGHEhUPmyqgFHbLE9)

# 3. Variables y tipos de datos	

## Ejercicio 3.1

Supongamos que queremos guardar los datos de una compra en una tienda. Crea las siguientes variables:

1. Una variable llamada `producto` con el valor "Laptop"

2. Una variable llamada `cantidad` con el valor 3

3. Una variable llamada `precio_unitario` con el valor 799.99

Luego, imprime los valores y el tipo de las variables en pantalla

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/8EGndbGaUYoQf2iUA)

# 4. Entrada y salida de datos

## Ejercicio 4.1

Realiza un código que pregunte al usuario su nombre, edad y estatura. Convierte la edad a un número entero, y la estatura a un número con decimal. Muestra los datos y el tipo de dato de cada variable en pantalla utilizando f-strings

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/QLC9cHKfeuyThr1C9)

# 5. Operadores aritméticos

## Ejercicio 5.1
Hay modelos de machine learning que realizan una predicción basada en la distancia entre dos puntos. Un ejemplo es el algoritmo de K-Nearest Neighbors (KNN), que predice la clase de un punto basándose en la clase de los puntos más cercanos a él.

Tu tarea es realizar un código que pida al usuario dos puntos en el plano cartesiano, y calcule la distancia entre ellos. La fórmula para calcular la distancia entre dos puntos es:

$$distancia = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Donde:
- $(x_1, y_1)$ son las coordenadas del primer punto
- $(x_2, y_2)$ son las coordenadas del segundo punto

Una vez que tengas la distancia, muéstrala en pantalla.

Nota. Recuerda que puedes obtener la raiz cuadrada de un número utilizando el operador `**` con un exponente de `0.5`.

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/RGV5BSo9W69XMiur8)

# 6. Condicionales

## Ejercicio 6.1

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

## Ejercicio 6.2
En ciencia de datos, muchas veces es necesario clasificar valores númericos en diferentes categorías. Supongamos que tenemos una lista de temperaturas en grados Celsius y queremos categorizarlas de la siguiente manera:

Menos de 15°C - Frío
Entre 15°C y 25°C - Templado

Escribe un programa que pida al usuario una temperatura y le diga si es "Frío" o "Templado". 

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/gNiCzAT9hXXWEZz26)