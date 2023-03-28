soma = 0

for i in range(10):
    num = int(input("Digite um numero: "))
    if (num < 40 ):
        soma += num
print(f"A soma dos valores que são inferiores à 40 é igual : {soma}")