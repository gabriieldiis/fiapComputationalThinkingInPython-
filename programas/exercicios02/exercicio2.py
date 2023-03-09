# Tendo como base o valor da cotação do dólar (em reais) do dia, faça a conversão de um valor em dólares para reais.

print("-----------------")
print("Vamos calcular o quanto você tem na carteira/bolsa em dolares")
print("-----------------")

reais = float(input("Quantos R$ você tem na carteira/ bolsa? "))

print("Esse calculo é baseado na cotação do dia 08/03/2023 - Quarta-feira ")
print("-----------------")
print("Neste dia $1 está valendo À exatamente 5,15 Real brasileiro ")
print("-----------------")

#if real =< 10
 #   (print(" : [ "))
  #  else (" cheio da grana em")

dolar = 5.15
conversao = reais / dolar
#print( f"sua media é igual à: {media:.2f}")

print (f"Hoje você tem {conversao:.2f} doláres!")
