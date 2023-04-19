matriz = []

for lin in range(6):
    linha = []
    for col in range(3):
        linha.append(float(input('Digite um elemento da matriz: ')))
    matriz.append(linha)

maior = matriz[0][0]
lin_maior = 0
col_maior = 0

menor = matriz[0][0]
lin_menor = 0
col_menor = 0

for lin in range(6):
    for col in range(3):
        if (matriz[lin][col] > maior):
            maior = matriz[lin][col]
            lin_maior = lin
            col_maior = col
        if (matriz[lin][col] < menor):
            menor = matriz[lin][col]
            lin_menor = lin
            col_menor = col


for lin in range(6):
    print(matriz[lin])


print(f'O menor elemento da matriz é {menor} e está na linha {lin_menor} e coluna {col_menor}')
print(f'O maiot elemento da matriz é {maior} e está na linha {lin_maior} e coluna {col_maior}')