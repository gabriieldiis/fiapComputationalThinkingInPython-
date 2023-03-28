cont = 0

for i in range(0,6):
    num = int(input("Digite um número: "))
    if (num >= 0):
        if (cont == 0):
            maior = num
        else:
            if (num > maior):
                maior = num

        cont += 1

print(f"Maior dos positivos {maior}")