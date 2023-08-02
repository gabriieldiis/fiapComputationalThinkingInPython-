def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo númeor:"))
    print(f"A soma dos números é igual a: {soma_numeros(num1,num2)}")

    n = int(input("Digite o valor de n: "))
    verifica_par_impar(n)

    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    print(f'O maior número é {retorna_maior(x,y)}')
def soma_numeros(num1, num2):
    soma = num1 + num2
    return(soma)

def verifica_par_impar(n):
    if (n % 2 == 0):
        print("O número é par!")
    else:
        print("O númeor não é par!")

def retorna_maior(x,y):
    if (x > y):
        return(x)
    else:       
        return(y)
    
if (__name__ == "__main__"):
    main()
