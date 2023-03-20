num = int(input("Digite um numero: "))

print("1 checar paridade do numero")
print("2 Dobro do numero")
print("3 Checar sinal do numero")

opc = int(input("Digite a opção desejada: "))

match opc:
    case 1:
        if ( num% 2 == 0):
            print("numero é par")
        else:
            print("numero é impar")
    case 2:
        dobro = 2 * num
        print("Dobro", dobro)
    case 3:
        if (num > 0):
            print("numero é positivo")
        else:
            print("O numeor é negativo")
    case _:
        print("opção invalida")