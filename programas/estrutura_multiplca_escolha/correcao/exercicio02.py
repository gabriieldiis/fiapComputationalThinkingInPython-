numero = float(input("Digite qualquer número: "))

opcao = float(input("Digite sua opção desejada ( 1 - 3 ):"))


match opcao:
    case 1:
        soma = numero + 5
        print(soma)
    case 2:
        subtracao = numero - 4
        print(subtracao)
    case 3:
        x = 2 + numero
        print(x)
    case _:
        print("opção inválida")