def organiza(lista: list):
    pos = len(lista) - 1
    aux = lista[pos]

    while lista[pos - 1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1

    lista[pos] = aux
    return lista

if __name__ == '__main__':
    lista = [5, 7, 11, 14, 25, 13]
    print(organiza(lista))
    
