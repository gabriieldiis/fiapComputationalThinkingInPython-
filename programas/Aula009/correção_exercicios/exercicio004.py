cont = 1

taxa = float(input("Digite a taxa de abatimento: "))
nro_prest = int(input("Digite o numero de prestações: "))
valor_prim_prest = float(input("Digite o valor da prestação: "))

prest_abatimento = valor_prim_prest

while (cont <= nro_prest):
    prest_abatimento = prest_abatimento - (prest_abatimento * (taxa / 100))
    print(f"Prestação com abatimento {prest_abatimento:.2f}")
    cont += 1
