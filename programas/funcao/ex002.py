def main():
    x = int(input('Digite o valor que será dobrado:'))
    print(f'O dobro de {x} é: {calcula_dobro(x)}')



def calcula_dobro(x):
    dobro = 2 * x
    return dobro

if (__name__ == '__main__'):
    main()