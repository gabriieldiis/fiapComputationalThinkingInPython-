def main():
    lista_numeros = []
    carrega_lista(lista_numeros)
    print('Numeros colocados na lista são: ')
    print(lista_numeros)



def carrega_lista(lista_numeros):

    for i in range(10):
        lista_numeros.append(int(input('Digite um elemento para a lista: ')))

if(__name__ == '__main__'):
    main()