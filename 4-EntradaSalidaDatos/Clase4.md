# Entrada y salida de datos


## Entrada de datos

Supongamos que estamos creando un pequeño sistema para una tienda. Necesitamos preguntar el nombre del cliente, y el dinero que gastó en la tienda. Para ello, utilizamos la función `input()`.

```python
nombre = input("¿Cuál es tu nombre? ")
dinero_gastado = input("¿Cuánto dinero gastaste? ")
```

`input()` muestra un mensaje en pantalla, y espera a que el usuario escriba algo. Cuando el usuario presiona la tecla `Enter`, `input()` devuelve lo que el usuario escribió. En este caso, guardamos el nombre del cliente en la variable `nombre`, y el dinero gastado en la variable `dinero_gastado`.

Para mostrar los datos en pantalla, utilizamos la función `print()`.

¿De que tipo de dato son las variables `nombre` y `dinero_gastado`? Utiliza la función `type()` para averiguarlo.

```python
print(type(nombre))
print(type(dinero_gastado))
```
Creeriamos que la variable `dinero_gastado` es de tipo `int` o `float`, pero en realidad es de tipo `str`. Esto se debe a que `input()` siempre devuelve un texto, incluso si el usuario escribe un número. Para convertir `dinero_gastado` a un número, utilizamos la función `int()`.

```python
dinero_gastado_convertido = int(dinero_gastado)
```

Ahora, `dinero_gastado_convertido` es un número entero. Si queremos transformar la variable a un número con decimal usamos `float()`.

```python
dinero_gastado_convertido = float(dinero_gastado)
```

Mostremos el tipo de dato de `dinero_gastado_convertido`.

```python
print(type(dinero_gastado_convertido))
```

Output:
```python
<class 'float'>
```

## Salida de datos

Para mostrar los datos en pantalla, utilizamos la función `print()`.

```python
print("Hola", nombre, "gastaste", dinero_gastado_convertido, "en la tienda")
```

Output:
```python
Hola Jesús gastaste 100.0 en la tienda
```

Otra forma de hacerlo es usando f-strings. Para ello, colocamos una `f` antes de las comillas de apertura, y dentro de las llaves colocamos las variables que queremos mostrar.

```python
print(f"Hola {nombre} gastaste {dinero_gastado_convertido} en la tienda")
```
Output:
```python
Hola Jesús gastaste 100.0 en la tienda
```

## Ejercicio propuesto

Realiza un código que pregunte al usuario su nombre, edad y estatura. Convierte la edad a un número entero, y la estatura a un número con decimal. Muestra los datos y el tipo de dato de cada variable en pantalla utilizando f-strings

[Sube tu respuesta a este ejercicio en este enlace](https://forms.gle/QLC9cHKfeuyThr1C9)