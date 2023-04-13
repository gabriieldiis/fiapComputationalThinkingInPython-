# Percorrer uma String

frase = input("Digite uma frase: ")
tam = len(frase)
print(tam)

for i in range(tam):
    print(frase[i])

# inverter uma string (notação slice)

palavra = "Fiap"
palavra_invertida = palavra[::-1]