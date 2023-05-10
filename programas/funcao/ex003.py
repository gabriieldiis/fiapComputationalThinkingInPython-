def main():
    n = int(input('Digite o valor de n: '))

    # if de verificação da função da verificação de par e impar
    if verifica_par_impar(n) == 1:
        print(f'O numero é par, {n}')
    else:
        print(f'O numero é impar, {n}')


def verifica_par_impar(n):
    if (n % 2 == 0):
        return ('O número é par - ', 1)
    else:
        return ('O número é impar - ', 0)


if (__name__ == '__main__'):
    main()