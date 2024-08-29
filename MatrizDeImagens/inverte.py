import Imagem

matriz = Imagem.getMatrizImagemCinza("GatoShitpost.jpg")

lin = len(matriz)
col = len(matriz[0])

#Criar outra matriz
rot = []
for i in range(lin):
    rot.append([0] * col)

for i in range(lin):
    for j in range(col):
        rot[lin - 1 - i][col - 1 - j] = matriz[i][j]

Imagem.salvaImagemCinza("GatoShitpost2.jpg", rot)


   
