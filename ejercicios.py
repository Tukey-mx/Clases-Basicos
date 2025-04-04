def esVocal(letra):
    return letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'
def recorrerLista(list, index):
    if index < len(list):
        if esVocal(list[index]):
            print(list[index], end = '')
        recorrerLista(list, index +1)
    else:
        print('\n')

#cadena = "aejnjfej"
#recorrerLista(cadena, 0)





def cuentaReg(lista, index):
    if index > -(len(lista) + 1):
        print(lista[index], end = '')
        cuentaReg(lista, index -1)
    else:
        print('\n')
        print("DESPEGUE...")
        

lista = [1, 2, 3, 4, 5]
cuentaReg(lista, -1)