#Funções em Strings

# Retorna o tamanho (quantidade de caracteres) da String

palavra = input("Digite uma palavra : ")
print(len(palavra))

#converter todos os caracteres para minusculos

palavra_minusculo = palavra.lower()
print(palavra_minusculo)

#converter todas as palavras em maiusculos

palavra_maiusculo = palavra.upper()
print(palavra_maiusculo)

#Separar palavras de um texto   

palavras = palavra.split(" ")
print(palavras)

# Substituir  (trocar) palavras de um texto

nova_palavra = palavra.replace("bambi" , "legal")
print(nova_palavra)