lista_num = []
lista_par = []
lista_impar = []

for i in range(10):
    numero = int(input('Digite um número: '))
    lista_num.append(numero)

for i in range(10):
    if (lista_num[i] % 2 ==0):
        lista_par.append(lista_num[i])
    else:
        lista_impar.append(lista_num[i])


print(lista_num)
print(lista_par)
print(lista_impar)
