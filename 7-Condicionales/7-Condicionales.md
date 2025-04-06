# Condicionales

En programación, un condicional es una estructura que permite ejecutar diferentes bloques de código según si una condición es verdadera o falsa. En Python, los condicionales se implementan principalmente con las palabras clave `if`, `elif` y `else`.

Antes de entender cómo funcionan los condicionales, es importante entender qué son las condiciones.
Una condición es una expresión que puede ser verdadera o falsa. Por ejemplo, la expresión `5 > 3` es verdadera, mientras que `3 > 5` es falsa. En Python, podemos usar operadores de comparación para crear condiciones. Algunos de los operadores de comparación más comunes son:
- `==`: Igual a
- `!=`: Diferente de
- `>`: Mayor que
- `<`: Menor que
- `>=`: Mayor o igual que
- `<=`: Menor o igual que

Ejemplo
```python
5 == 5 # True
5 != 3 # True
5 > 3 # True
5 < 3 # False
5 >= 5 # True
5 <= 3 # False
```

## Estructura de un condicional
La estructura básica de un condicional en Python es la siguiente:

```python
if condición1:
    # Código a ejecutar si la condición1 es verdadera
elif condición2:
    # Código a ejecutar si la condición2 es verdadera
else:
    # Código a ejecutar si ninguna de las condiciones anteriores es verdadera
```
### Ejemplo
```python
edad = 18
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")
```

Salida:
```python
Eres mayor de edad
```
### Explicación
1. **`if edad < 18:`**: Si la variable `edad` es menor que 18, se ejecuta el bloque de código indentado debajo de esta línea.
2. **`elif edad == 18:`**: Si la variable `edad` es igual a 18, se ejecuta este bloque de código.
3. **`else:`**: Si ninguna de las condiciones anteriores es verdadera, se ejecuta este bloque de código.

# Operadores lógicos
Los operadores lógicos se utilizan para combinar múltiples condiciones. Los operadores lógicos más comunes son:
- `and`: Devuelve verdadero si ambas condiciones son verdaderas.
- `or`: Devuelve verdadero si al menos una de las condiciones es verdadera.
- `not`: Devuelve verdadero si la condición es falsa.
### Ejemplo
```python
edad = 20
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres adulto")
else:
    print("Eres mayor de edad")
```
Salida:
```python
Eres adulto
```
### Explicación
1. **`if edad < 18:`**: Si la variable `edad` es menor que 18, se ejecuta el bloque de código indentado debajo de esta línea.
2. **`elif edad >= 18 and edad < 65:`**: Si la variable `edad` es mayor o igual a 18 y menor que 65, se ejecuta este bloque de código.
3. **`else:`**: Si ninguna de las condiciones anteriores es verdadera, se ejecuta este bloque de código.

### Uso de condicionales en Ciencia de Datos
Funcion de activación
En aprendizaje automático, un perceptrón es una neurona artificial que recibe varias entradas (x₁, x₂, ..., xₙ), cada una con un peso asociado (w₁, w₂, ..., wₙ), y un sesgo (b). La salida del perceptrón se obtiene al calcular la combinación lineal de las entradas y luego aplicar una función de activación.

La función de activación es una función matemática que transforma la salida del perceptrón.
Un ejemplo de función de activación es la función escalonada, que devuelve 1 si la salida es mayor o igual a un umbral (por ejemplo, 0) y 0 en caso contrario.
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
# Aplicamos la función de activación
if salida >= 0:
    print("La salida es 1")
else:
    print("La salida es 0")
```
