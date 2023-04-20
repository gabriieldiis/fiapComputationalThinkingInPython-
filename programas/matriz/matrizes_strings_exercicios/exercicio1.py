'''

Escreva um programa para ler uma matriz A com 8 linhas e 6 colunas.
Construir uma lista B que seja formado pela soma de cada linha da matriz A.
Ao final apresentar o somatório dos elementos da lista B

'''

matriz_a = []
lista_b = []

for lin in range(2):
    linha_a = []
    for col in range(2):
        linha_a.append(int(input('Digite um elemento da Matriz: ')))
        matriz_a.append(linha_a)

for i in range(1):
    print(matriz_a)

for lin in range(2):
    soma_linha = 0
    for col in range(2):
        soma_linha += matriz_a[lin][col]

print(soma_linha)


'''

matriz_b = matriz_a + matriz_a
for i in range(1):
    print(matriz_b)
    
'''
