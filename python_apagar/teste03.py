from PIL import Image

def main():
    concatena_imagem_selo()
    ck_produto

def concatena_imagem_selo():
    # Carregando as imagens
    imagem_maior = Image.open(r"C:\Users\internet07\Desktop\python_apagar\176101d.jpg")
    imagem_menor = Image.open(r"C:\Users\internet07\Desktop\python_apagar\Camada.png")
    
    
    # Criando uma nova imagem do tamanho necessário (largura da imagem maior, altura total)
    largura_total = imagem_maior.width
    altura_total = imagem_maior.height
    imagem_resultante = Image.new("RGB", (largura_total, altura_total))
    
    # Colando as imagens na imagem resultante
    imagem_resultante.paste(imagem_maior, (0, 0))
    imagem_resultante.paste(imagem_menor, (110, 10))
    
    # Salvando a imagem resultante
    imagem_resultante.save("imagem_final.jpg")

if __name__ == "__main__":
    main()