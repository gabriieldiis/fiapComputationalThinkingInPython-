from PIL import Image

# Carregando as imagens
imagem1 = Image.open(r"C:\Users\internet07\Desktop\python_apagar\176101d.jpg")
imagem2 = Image.open(r"C:\Users\internet07\Desktop\python_apagar\Camada.png")

# Obtendo as dimensões das imagens
largura_imagem1, altura_imagem1 = imagem1.size
largura_imagem2, altura_imagem2 = imagem2.size

# Calculando a largura total da imagem resultante
largura_total = largura_imagem1 - 20
altura_total = max(altura_imagem1, altura_imagem2)

# Criando uma nova imagem do tamanho total
imagem_completa = Image.new("RGB", (largura_total, altura_total))

# Colando as imagens na imagem resultante
imagem_completa.paste(imagem1, (0, 0))
imagem_completa.paste(imagem2, (largura_imagem1, 0))

# Salvando a imagem resultante
imagem_completa.save("imagem_completa.jpg")
