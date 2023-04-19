matriz = []

for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(int(input('Digite um elemento da matriz: ')))
    matriz.append(linha)

for lin in range(3):
    print(matriz[lin])

k = int(input('Digite o valor de k:'))

for lin in range(3):
    for col in range(3):
        if (lin == col):
            matriz[lin][col] = matriz[lin][col] * k

for lin in range(3):
    print(matriz[lin])