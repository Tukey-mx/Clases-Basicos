# Iterar Listas y Cadenas

En esta sección, aprenderemos a iterar sobre listas y cadenas utilizando bucles en Python. La iteración es una técnica fundamental en programación que nos permite recorrer elementos de una colección (como listas o cadenas) y realizar operaciones sobre ellos.

## Bucle `for`
El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, una tupla o un rango). La sintaxis básica es la siguiente:

```python
for variable in secuencia:
    # Código a ejecutar en cada iteración
```

### Ejemplo 1
```python
# Imprimir los elementos de una lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```
Esto imprimirá cada número de la lista en una nueva línea.

### Ejemplo 2
```python
# Imprimir solo las vocales de una cadena
cadena = "Hola Mundo"
vocales = ["a", "e", "i", "o", "u"]
#Primero convertimos la cadena a minúsculas
cadena = cadena.lower()
for letra in cadena:
    if letra in vocales:
        print(letra)
```

### Ejemplo 3
```python
# Sumar los números de una lista
numeros = [1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma += numero
print("La suma es:", suma)
```