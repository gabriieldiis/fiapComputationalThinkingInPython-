soma = 0
contador_positivos = 0
for i in range(8):
    n = int(input("Digite um número inteiro e positivo: "))
    if  (n >= 0):
        soma =+ n
        contador_positivos += 1

media = soma  / contador_positivos
print(f"Soma positivos {soma}: ")
print(f"Media dos positivos {media:.2f}")
