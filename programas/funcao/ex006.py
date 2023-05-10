def main():



def calcula_somamedia(lista_numeros, tam):
    soma = 0
    for i in range(0, tam):
        soma += lista_numeros[i]

    media = soma / tam
    return (soma, tam)



if (__name__ == '__main__'):
    main()