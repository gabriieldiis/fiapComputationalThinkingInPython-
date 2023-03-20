numero01 = float(input("Digite um numero: "))
numero02 = float(input("Digite outro numero: "))

opcao = int(input("Digite uma opção 1-4"))

print("Opcao = 1: soma dos 2 números.")
print("Opcao = 2: subtração dos 2 números")
print("Opcao = 3: multiplicação dos 2 números.")
print("Opcao = 4: divisão dos 2 números.")


match opcao:
    case 1:
        soma = numero01 + numero02
        print(soma)
    case 2:
        sub = numero01 - numero02
        print(sub)
    case 3:
        mult = numero01 * numero02
        print(mult)
    case 4:
        div = numero01 / numero02
        print(div)