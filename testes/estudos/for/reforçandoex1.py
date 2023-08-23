print("seja bem vindo!")

numeros_pares = 0
numeros_impares = 0

num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))


lista = [num1, num2]

for i in lista:
    if (i % 2 == 0):
        numeros_pares += 1
        print("Quantidade de números pares: ", numeros_pares)
    else:
        numeros_impares += 1
        print("Quantidade de numeros impares:", numeros_impares)