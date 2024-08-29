import Imagem as img

matriz_cinza = img.getMatrizImagemCinza('GatoShitpost.jpg')

lin = len(matriz_cinza)
col = len(matriz_cinza[0])
print(f"Dimensoes{lin}+{col}")

for i in range(lin):
    for j in range(col):
        if matriz_cinza[i][j] <= 128:
            matriz_cinza[i][j] = 0
        else:
            matriz_cinza[i][j] = 255
        
img.salvaImagemCinza('Gato3.jpg', matriz_cinza)