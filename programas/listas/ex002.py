lista_idades = []

soma_idades = 0
qtde_menores_18 = 0

idade = int(input("Digite a idade do usuário: "))

while (idade > 0):
    lista_idades.append(idade)
    idade = int(input("Digite a idade do usuário: "))

for i in range(len(lista_idades)):
    soma_idades += lista_idades [i]
    if (lista_idades[i] < 18):
        qtde_menores_18 += 1

media_idades = soma_idades / len(lista_idades) # sum(lista_idades) / len(lista_idades)
print(f"Media das idades é igual a: {media_idades:.2f}")
print(f"Quantidade de usuários menores que dezoito anos: {qtde_menores_18}")