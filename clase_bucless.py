list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list[0])

def Range(inicio, fin):
    if inicio < fin:
        print(inicio, end=' ')
        Range(inicio + 1, fin)
    else:
        print('\n')

Range(1, 10)

def reccorer_lista(lista, index):
    if index < len(lista):
        print(lista[index], end=' ')
        reccorer_lista(lista, index + 1)
    else:
        print('\n')

reccorer_lista(list, 0)


cadena = 'Hola'

def recorrer_cadena(cadena, index):
    if index < len(cadena):
        print(cadena[index], end=' ')
        recorrer_cadena(cadena, index + 1)
    else:
        print('\n')

recorrer_cadena(cadena, 0)

def mi_break(lista, valos_detener, index):
    if index < len(lista):
        if lista[index] == valos_detener:
            return
        else:
            print(lista[index], end=' ')
            mi_break(lista, valos_detener, index + 1)
    else:
        print('\n')

mi_break(list, 5, 0)

