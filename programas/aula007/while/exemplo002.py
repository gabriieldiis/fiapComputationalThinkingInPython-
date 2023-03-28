soma = 0

n = int(input("Digite um número: "))

while (n >= 0):
    soma = soma + n
    n = int(input("Digite um número: "))

print(f"Soma dos positivos {soma}")