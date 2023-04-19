

matriz = []

for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(int(input('Digite um elemento da matriz: ')))
    matriz.append(linha)

for lin in range(3):
    soma_linha = 0
    for col in range(3):
        soma_linha += matriz[lin][col]
    if (lin == 0):
        maior = soma_linha
        linha_maior_soma = 0
    else:
        if (soma_linha > maior):
            maior = soma_linha
            linha_maior_soma = lin

for lin in range(3):
    print(matriz[lin])

print(f'A maior soma é {maior} e está na linha {linha_maior_soma}')