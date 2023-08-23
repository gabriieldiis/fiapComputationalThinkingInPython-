lista_numeros = []
lista_pares = []
lista_impares =[]

for i in range(3):
    num = int(input("Digite um número: "))
    lista_numeros.append(num)

for i in range (3):
    if (lista_numeros[i] % 2  == 0):
        lista_pares.append(lista_numeros[i])
    else:
        lista_impares.append(lista_numeros[i])

print(lista_numeros)
print(lista_pares)
print(lista_impares)