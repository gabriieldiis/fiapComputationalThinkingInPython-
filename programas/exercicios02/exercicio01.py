#Crie um algoritmo que solicite ao usuário seu consumo de energia elétrica (em kWh), que deve ser uma variável real. O algoritmo deve, então, calcular o total da conta, considerando que cada kWh custa R$ 0,2

print("-----------------")
print("Vamos calcular o seu consumo de energia")
print("-----------------")

tempo = float(input("Quanto tempo você usa a energia eletrica em casa? "))
print("-----------------")

tempo = tempo * 60
kwh = tempo * 0.20

print (kwh)