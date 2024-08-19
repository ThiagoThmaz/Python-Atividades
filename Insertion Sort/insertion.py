def organiza(lista: list, pos: int):
    aux = lista[pos]

    while pos > 0 and lista[pos - 1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1

    lista[pos] = aux
    return lista

def insertion_sort(lista: list):
    for i in range(1 , len(lista)):
        organiza(lista, i)

if __name__ == '__main__':
    lista = [10, 7, 13, 7, 25, 1]
    insertion_sort(lista)
    print(lista)
