listaA= []
listaB = []
listaC = []

for i in range(10):
    listaA.append(int(input("Digite um número: ")))
    listaB.append(int(input("Digite um número: ")))

for i in range(10):
    listaC.append(listaA[i])
    listaC.append(listaB[i])

print(listaA)
print(listaB)
print(listaC)