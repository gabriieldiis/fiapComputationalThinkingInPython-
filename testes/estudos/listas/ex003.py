qtde_maior_sete = 0
lista_medias = []

for i in range(3):
    check1 = float(input('Digite a nota do checkpoint 1: '))
    check2 = float(input('Digite a nota do checkpoint 2: '))
    check3 = float(input('Digite a nota do checkpoint 3: '))
    media = check1 + check2 + check3 / 3
    lista_medias.append(media)

for i in range(3):
    if (lista_medias[i] >= 7):
        qtde_maior_sete +=1

print(media)
print(lista_medias)