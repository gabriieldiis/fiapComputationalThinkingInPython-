n1 = int(input("Digite qualquer número: "))
n2 = int(input("Digite outro qualquer número: "))

cont = n1 + 1
cont_pares = 0
cont_impares = 0

while (cont <= n2):
    if ( cont % 2 == 0 ):
        cont_pares += 1
    else:
        cont_impares += 1
    cont += 1

print(f"Quantidade de pares de {n1} a {n2}: {cont_pares}")
print(f"Quantidade de pares de {n1} a {n2}: {cont_impares}")