soma_salarial = 0

nome_empresa = input("Digite o nome da empresa: ")

for cont in range(5):
    nome = input("Digite o nome do funcionário " + str(cont + 1 ) + " : ")
    salario = float(input(f"Digite o salário do funcionário " + str(cont + 1) + " : "))
    soma_salarial += salario
    if (cont == 0):
        maior_salario = salario
        menor_salario = salario
        nome_maior_salario = nome
        nome_menor_salario = nome
    else:
        if (salario > maior_salario):
            maior_salario = salario
            nome_maior_salario = nome
        if (salario > menor_salario):
            menor_salario = salario
            nome_menor_salario = nome

media = soma_salarial / 5

print(f"A media salarial da empresa {nome_empresa} é {media:.2f}")
print(f"{nome_menor_salario} recebe o menor salário que corresponde à {menor_salario:.2f}")
print(f"{nome_maior_salario} recebe o menor salário que corresponde à {maior_salario:.2f}")
