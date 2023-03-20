peso = float(input("Diigite seu peso: "))
altura = float(input("Diigite sua altura: "))

imc = peso / altura**2

if (imc < 18.5):
    print("Abaixo do peso")
elif ( imc <= 24.9):
    print("Peso Ideal")
elif (imc <= 29.9):
    print("Voce está levemente acima do peso")
elif (imc <= 34.9):
    print("Obesidade grau 1")
elif (imc <= 39.9):
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")
