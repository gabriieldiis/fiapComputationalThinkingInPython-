listas_numeros = []

for i in range(10):
    listas_numeros.append(int(input("Digite um numero: ")))

maior = listas_numeros [0]
pos_maior = 0

for i in range(10):
        if (listas_numeros[i] > maior):
            maior = listas_numeros[i]
            pos_maior = i

print(f"o maior elemento da lista é {maior} está na posição {pos_maior}")
