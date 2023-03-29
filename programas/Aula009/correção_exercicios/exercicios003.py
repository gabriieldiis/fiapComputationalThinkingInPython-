num = int(input("Digite um número: "))
cont = 1

while (num > 0):
    if (cont == 1):
        maior = num
        menor = num
    else:
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num
    cont += 1
    int(input("Digite outro número: "))

print(f"Maior numero digitado {maior}")
print(f"Menor numero digitado {menor}")