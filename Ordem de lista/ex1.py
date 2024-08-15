lista = [4,2,1,3,5]

def selection_sort(lista: list):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista


# Uso da lista 
lista_ordenada = selection_sort(lista)
print("Lista em ordem: " , lista_ordenada)