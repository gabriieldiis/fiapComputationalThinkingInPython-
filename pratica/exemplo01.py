def mostra_linha():
    print('-' * 30)

def soma(a, b):
    print(f'A = {a} e B= {b}')
    s = a + b
    print(f'a Soma dos dois números é igual a: {s}')
    print('\n')



#Programa Principal
soma(4, 5)
soma(5, 1)
soma(2, 1)


mostra_linha()

# vamos fazer multiplicando agora

def mult(a, b):
    print(f'A = {a} e B = {b}')
    mult = a * b
    print(f'A multiplicação dos números é igual á: {mult}')
    print('\n')


mult(2, 2)
mult(4, 8)
mult(10, 0.5)