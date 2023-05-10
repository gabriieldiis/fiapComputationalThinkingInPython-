def main():
    a = int(input('Digite ovalor de a:'))
    b = int(input('Digite o valor de b: '))
    # chamada da função atribuindo o retorno a uma variavel
    maior = retorna_maior(a, b)

    linha()
    print(f'O maior valor é {maior}')
    linha()
    # chamada da função diretamente em um print
    print(f'O maior vaor é {retorna_maior(a, b)}')


def retorna_maior(a,b):
    if (a > b):
        return (a)
    else:
        return  (b)

def linha():
    print('-'*30)

if(__name__ == '__main__'):
    main()
