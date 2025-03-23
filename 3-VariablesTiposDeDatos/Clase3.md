# Variables y tipos de datos

## Imaginemos lo siguiente:

Queremos almacenar los datos de una persona, por ejemplo:


```python
"Jesús"
22
1.68
"Skate"
```

Una forma de hacerlo sería escribriendo los datos cada vez que los necesitemos, pero esto no es muy práctico.

En programación, para guardar datos de forma más eficiente, utilizamos variables.

## Variables

Una variable es como una caja con etiqueta, donde  guardamos información para usarla más adelante.

Mas formalmente, una variable es un espacio en la memoria de la computadora que se utiliza para almacenar un valor.

Por ejemplo, si queremos guardar la edad de una persona, podemos hacerlo de la siguiente forma:

```python
edad = 22
```

Aqui, `edad` es la variable, y `22` es el valor que estamos guardando en ella.

### Reglas para nombrar variables

- El nombre de una variable debe comenzar con una letra o un guión bajo.
- El nombre de una variable no puede comenzar con un número.
- El nombre de una variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9, y _).
- Los nombres de las variables distinguen entre mayúsculas y minúsculas. (es decir, `edad` y `Edad` son dos variables diferentes).
- No puede ser una palabra reservada de Python (como `print`, `for`, `if`, etc.)

## Función print()
Una vez que guarda un valor en una variable, puede mostrarlo en la pantalla utilizando la función `print()`.
```python
nombre = "Jesús"
edad = 22
print(nombre)
print(edad)
```
Salida:
```python
22
```
Notemos que si queremos almacenar texto en una variable, debemos encerrarlo entre comillas dobles o simples. En caso contrario, Python interpretará el texto como una variable.

También podemos imprimir texto y variables juntos:
```python
nombre = "Jesús"
edad = 22
print("Mi nombre es", nombre, "y tengo", edad, "años")
```
Salida:
```python
Mi nombre es Jesús y tengo 22 años
```

## Tipos de datos
Has notado que en el ejemplo anterior, hemos utilizado diferentes tipos de datos: texto y números. En Python, los tipos de datos más comunes son:

### Tabla con los tipos de datos

| Tipo de dato | Descripción |
|--------------|-------------|
| `str`        | Texto       |
| `int`        | Números enteros |
| `float`      | Números decimales |

En Python, no es necesario declarar explícitamente el tipo de dato de una variable, ya que Python es un lenguaje de programación de tipado dinámico. Esto significa que Python puede cambiar el tipo de dato de una variable en tiempo de ejecución.

Por ejemplo, si queremos guardar un número decimal en una variable, podemos hacerlo de la siguiente forma:
```python
altura = 1.68
```

Si yo quiero cambiar el valor de la variable a un texto, simplemente asigno un nuevo valor a la variable:
```python
altura = "Uno punto sesenta y ocho"
```
Python ajustará automáticamente el tipo de dato de la variable.

### ¿Cómo saber el tipo de dato de una variable?
Para saber el tipo de dato de una variable, podemos utilizar la función `type()`, y para mostarlo en pantalla usamos la función `print()`.
```python
nombre = "Jesús"
edad = 22
altura = 1.68

print(type(nombre))
print(type(edad))
print(type(altura))
```
Salida:
```python
<class 'str'>
<class 'int'>
<class 'float'>
``` 
En este caso, `str` es el tipo de dato de la variable `nombre`, `int` es el tipo de dato de la variable `edad`, y `float` es el tipo de dato de la variable `altura`.

## Ejericio propuesto
Supongamos que queremos guardar los datos de una compra en una tienda. Crea las siguientes variables:

1. Una variable llamada `producto` con el valor "Laptop"

2. Una variable llamada `cantidad` con el valor 3

3. Una variable llamada `precio_unitario` con el valor 799.99

Luego, imprime los valores y el tipo de las variables en pantalla
