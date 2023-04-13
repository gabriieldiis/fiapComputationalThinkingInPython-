lista_palavras_ing = []
lista_palavras_port = []

resp = 1
while (resp != 0):
    lista_palavras_ing.append(input("Digite uma palavra em inglês:"))
    lista_palavras_port.append(input("Digite uma palavras em português"))

    resp = int(input("Deseja continuar 1 - SIM | 2 - NÃO : "))

palavra = input("Digite a palavra em inglês a ser traduzida: ")

if(palavra in lista_palavras_ing):
    pos_palavra = lista_palavras_ing.index(palavra)
    print(f"A palavra em português é: {lista_palavras_port[pos_palavra]}")