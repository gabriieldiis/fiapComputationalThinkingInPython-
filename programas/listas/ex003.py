lista_numeros = []
qtde_mult_3 = 0


for i in range(10):
    lista_numeros.append(int(input("Digite um numero: ")))

for i in range(10):
    if (lista_numeros[i] % 3 == 0):
        qtde_mult_3 +=1

print(f"Quantidade de numeros multiplos por 3 na lista: {qtde_mult_3}")
