soma = 0

for contador in range (1,11):
    soma = soma + contador

print(f"Soma : {soma}")


soma_impares = 0

for cont in range (1,11):
    if (cont % 2 != 0):
        soma_impares = soma_impares + cont

print(f"Soma Impares : {soma_impares}")

