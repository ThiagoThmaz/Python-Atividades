def organiza(lista: list):
    pos = len(lista) - 1
    aux = lista[pos]

    while lista[pos - 1] > aux:
        lista[pos] = lista[pos-1]
        pos -= 1

    lista[pos] = aux
    return lista

lista = [5, 7, 11, 14, 25, 13]
lista_organiza = organiza(lista)
print('Lista ordenada: ', lista_organiza)