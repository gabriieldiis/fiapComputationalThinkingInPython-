ano = int(input("Em qua ano estamos? : "))

if (ano > 2999):
    print("Esse programa lê até o ano 2999")
else:
    print(f"ótimo estamos no ano {ano}")

ano_bisexto = ano % 400

if (ano_bisexto == 0):
    print("Ótimo o ano escolhido é bissexto")
else:
    print("O ano escolhido não é bissexto")