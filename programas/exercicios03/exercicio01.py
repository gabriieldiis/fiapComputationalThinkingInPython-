valor_produto = float(input("Quanto custa o produto que você quer comprar ? "))
valor_especie = float(input("Quanto você tem em mãos?  "))

if (valor_especie >= valor_produto ):
    print("Você pode comprar o produto")
else:
    print("Infelizmente você nao pode comprar o produto")