
check1 = float(input("Digite a notado checkpoint 1 : "))
check2 = float(input("Digite a notado checkpoint 2 : "))
check3 = float(input("Digite a notado checkpoint 3 : "))

media = (check1 + check2 + check3) / 3
if (media >= 6):
    print(f"O aluno foi aprovado com a média {media:.2f}")
elif (media >= 4):
    print(f"O aluno está de exame com a média {media:.2f}")
else:
    print(f"O aluno foi reprovado com a média {media:.2f}")


