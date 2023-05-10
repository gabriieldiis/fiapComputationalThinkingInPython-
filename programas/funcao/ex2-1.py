def main():
    numero = int(input('Digite o numero que será multiplicado: '))
    print(f'O numero multiplcado por ele mesmo é igual a: {multiplica_numero(numero)}')


def multiplica_numero(numero):
    mult = numero * numero
    return (mult)


if (__name__ == '__main__'):
    main()