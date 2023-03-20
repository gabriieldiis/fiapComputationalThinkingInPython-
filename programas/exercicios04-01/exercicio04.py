valor_livro = float(input("Digite o valor do livro: "))

if(valor_livro <= 10.0):
    desc =  (valor_livro * 0.8)
elif(valor_livro <= 60):
    desc = (valor_livro *  0.10)
else:
    desc = (valor_livro * 0.20)

print(f"Desconto: {desc:.2f}")