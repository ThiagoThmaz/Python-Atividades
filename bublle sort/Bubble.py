def bubbleSort(lista: list):
    for j in range(len(lista)-1, 0, -1):
        for i in range(j):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(lista)
print(lista)