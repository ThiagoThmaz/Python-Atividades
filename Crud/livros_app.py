def cadastra(conj: list):
    tit = input("informe o tit: ")
    cat = input("informe a cat: ")
    sin = input("informe a sin: ")
    aut = input("informe o aut: ")
    edi = input("informe o edi: ")
    prc = input("informe o prc: ")
    livro = [tit,cat,sin,aut,edi,prc,]
    conj.append(livro)

def consulta(conj: list):
    resultado = []
    cat = input("Informa a cat: ")
    for i in range(len(conj)):
        if conj[i][1] == cat:
            resultado.append(conj[i])
    if len(resultado) == 0:
        print("Nemhum")
    else:
        for livro in resultado:
            print(livro)

def busca(conj: list, titulo: str):
    for i in range(len(conj)):
        if conj[i][0] == titulo:
            return i
        return - 1
    
def altera(conj: list):
    tit = input("informe o tit: ")
    pos = busca(conj, tit)
    if pos == -1:
        print("N encontrei")
    else:
        rotulos = ['Titulo','Categoria','Sinopse','Autor','Editora','Preço']
        for i in range(len(rotulos)):
            aux = input(f"{rotulos[i]}: ({conj[pos][i]})")
        if rotulos[i] == 'Preço':
            conj[pos][i] = float(aux)
        else:
            conj[pos][i] = aux

def exclui(conj: list):
    tit = input('informe tit: ')
    pos = busca(conj, tit)
    if pos == -1:
        print('Não tem esse tit')
    else:
        print(conj[pos])
        print("Livro Excluido!!")
        conj.pop(pos)

estoque = []
# quais informações de livros vamos armazenar?
# titulo, categoria, sinopse, autor, editora, preço

opcao = 0
while opcao != 6:
    print(" Sistema de Livraria  ")
    print("1 - cadastra ")
    print("2 - consulta")
    print("3 - altera")
    print("4 - exclui")
    print("5 - sair")
    try:
        opcao = int(input("Informa uma opção"))
    except Exception:
        print("Opção Invalida! ")
        opcao = 0

    if opcao == 1:
        cadastra(estoque)
    elif opcao == 2:
        consulta(estoque)
    elif opcao == 3:
        altera(estoque)
    elif opcao == 4:
        exclui(estoque)
  

