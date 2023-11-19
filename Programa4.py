def elemento_matriz(matriz, linha, coluna):
    print(matriz[linha][coluna])


matriz = []
tamanho_linha = int(input("Tamanho da linha: "))
tamanho_coluna = int(input("Tamanho da coluna: "))

for i in range(tamanho_coluna):
    linha = []
    for j in range(tamanho_linha):
        linha.append(int(input(f"elemento na posicao {i + 1} {j + 1}: ")))
    matriz.append(linha)

for elemento in matriz:
    print(elemento) 

linha = int(input("linha: "))
coluna = int(input("coluna: "))

elemento_matriz(matriz, (linha - 1), (coluna - 1))
