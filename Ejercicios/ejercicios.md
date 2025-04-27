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

# 7. Condicionales

## Ejercicio 7.1

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

## Ejercicio 7.2
En ciencia de datos, muchas veces es necesario clasificar valores númericos en diferentes categorías. Supongamos que tenemos una lista de temperaturas en grados Celsius y queremos categorizarlas de la siguiente manera:

Menos de 15°C - Frío
Entre 15°C y 25°C - Templado

Escribe un programa que pida al usuario una temperatura y le diga si es "Frío" o "Templado". 

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/gNiCzAT9hXXWEZz26)

# 8. Iterar listas y cadenas
## Ejercicio 8.1
Supongamos que tenemos una lista de frutas, y queremos imprimir solo las frutas que terminan con la letra "a". Crea una lista de frutas y utiliza un bucle `for` para imprimir solo las frutas que terminan con "a".

```python
# Lista de frutas
frutas = ["MANZANA", "BANANA", "pera", "uva", "kiwi"]
# Escribe tu código aquí
```
[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/Mu1V5gfHYktEYUcf7)


## Ejercicio 8.2
Tenemos la siguiente cadena de texto: "Club de CIENCIA DE DATOS TUKEY". Queremos contar cuántas vocales y cuantas consonantes hay en la cadena. Escribe un programa que cuente las vocales y consonantes y muestre el resultado.

```python
cadena = "Club de CIENCIA DE DATOS TUKEY"
# Escribe tu código aquí
```
[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/RXdPxDwLcc3N7UVUA)


## Ejercicio 8.3
Tenemos dos lista que contienen las calificaciones (1 - 10) que distintos jueces le han dado a una dos barras de chocolate. 

Para cada una de las barras, calcula lo siguiente:

1. La calificacion promedio.

$$ promedio = \frac{1} {n}\sum_{i = 1}^{n}{calificación_i}$$

2. La calificación más alta (lo puedes hacer utilizando la función `max` de python)


3. La calificación más baja (lo puedes hacer utilizando la función `min` de python)

4. Desviación estándar de las calificaciones. La cual nos indica la distancia promedio entre cada calificación y la calificación promedio, es decir, nos indica que tan variables son las calificaciones. La fórmula para calcular el desvío estándar es:

$$
desviación\;estándar = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(calificacion_i - promedio\;calificacion)^2}$$


```python 
# Calificaciones de los jueces
calificaciones_barra1 = [7,5,9,7,9,10,7,7,10,6,7]
calificaciones_barra2 = [10,8,10,7,10,10,7,7,10,6,7]

# Escribe tu código aquí
```
En un comentario dentro de tu código, escribe la respuesta a la siguiente pregunta:

¿Cuál crees que es la mejor barra de chocolate? ¿Por qué?

**Pista: La desviación estándar nos indica que tan variables son las calificaciones. Si una barra tiene una calificación promedio alta, pero su desviación estándar es alta, significa que los jueces no están de acuerdo en la calificación. Por el contrario, si una barra tiene una calificación promedio alta y su desviación estándar es baja, significa que los jueces están de acuerdo en la calificación.**

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/AAAB8MZvkGKFvTi39)
