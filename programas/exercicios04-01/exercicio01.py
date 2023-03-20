nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if  (media >= 6 ):
    print("Você foi aprovado, com a media: ", media)
elif (media >= 4):
    print("Voce está de exame, com a media: ", media)
else:
    print("Você foi reprovado, com a media: ", media)