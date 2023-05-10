def main():
    b = int(input('Digite o valor de b: '))
    print(f' A raiz quadrada de {b} é igual a:  {calcula_quadrado(b)}')


def calcula_quadrado(b):
    quadrado = b**2
    return (quadrado)



if (__name__ == '__main__'):
    main()