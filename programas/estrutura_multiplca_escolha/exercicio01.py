codigo = int(input("Digite o codigo do produto: 1-5: "))

match codigo:
    case 1:
        print("Produto escolhido: Caneta ")
        print("Valor: R$1.20 ")
    case 2:
        print("Produto escolhido: Lapis ")
        print("Valor: R$0.80 ")
    case 3:
        print("Produto escolhido: Caderno ")
        print("Valor: 4.50")
    case 4:
        print("Produto escolhido: Borracha")
        print("Valor: 1.00")
    case 4:
        print("Produto escolhido: Régua")
        print("Valor: 1.50 ")
    case _:
        print("Opção invalida")