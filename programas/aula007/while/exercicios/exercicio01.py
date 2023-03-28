n = int(input("Digite um número inteiro: "))
soma = 0
contador = 1

while contador <= n:
    soma = soma + contador
    contador = contador + 1

print("A soma dos números inteiros de 1 a", n, "é", soma)
