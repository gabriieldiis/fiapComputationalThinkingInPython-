#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias]

anos = int(input("quantos anos voce  tem ? "))

meses = int(input("quantos meses você tem? (com sua idade) "))

dias = int(input("quantos dias voce  tem  com sua idade ? (com sua idade) "))

dias_de_vida = anos*365+meses*30+dias

print(dias_de_vida)