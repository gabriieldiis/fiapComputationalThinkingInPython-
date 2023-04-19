matriz = []

for lin in range(4):
    linha = []
    for col in range(4):
        linha.append(int(input('Digite um elemento da matriz: ')))
    matriz.append(linha)

cont_maior = 0

for lin in range(4):
    linha = []
    for col in range(4):
        if (matriz[lin][col]) > 10:
            cont_maior += 1
print(f'Valores maiores que 10 da  matriz: {cont_maior}')

print('---------------------')
print(matriz)