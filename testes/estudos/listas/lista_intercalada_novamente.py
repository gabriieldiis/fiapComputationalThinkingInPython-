listaA =[]
listaB =[]
listaC =[]

for i in range(10):
    listaA.append(int(input("Digite um numero: ")))
    listaB.append(int(input("Digite um numero: ")))

for i in range(10):
    listaC.append(listaA[i])
    listaC.append(listaB[i])

print(listaA)
print(listaB)
print(listaC)
