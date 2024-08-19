def ordenar_pessoas(lista: list):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][0] > lista[j + 1][0]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            elif lista[j][0] == lista[j + 1][0] and lista[j][1] > lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return

lista_pessoas_idade = [('Joao', 25), ('Maria', 22), ('Pedro', 30), ('Joao', 20), ('Ana', 27)]
lista_pessoas_idade_ordenada = ordenar_pessoas(lista_pessoas_idade)
print(lista_pessoas_idade)
