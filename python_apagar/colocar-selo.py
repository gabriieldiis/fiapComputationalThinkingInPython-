from PIL import Image
import os

def acessar_imagens_os():
    pasta_imagens = r"C:\_projetos\FIAP\python\fiapComputationalThinkingInPython-\Kalunga\downloaded_images"
    arquivos = os.listdir(pasta_imagens)
    extensoes_suportadas = [".jpg", ".png"]
    arquivos_imagens = [arquivo for arquivo in arquivos if os.path.splitext(arquivo)[1].lower() in extensoes_suportadas]
    imagens = []

    for arquivo in arquivos_imagens:
        caminho_completo = os.path.join(pasta_imagens, arquivo)
        imagem = Image.open(caminho_completo)
        imagens.append((arquivo, imagem))  # Armazena nome do arquivo junto com a imagem
    
    return imagens

def concatena_imagem_selo(nome_arquivo, imagem_maior):
    imagem_menor = Image.open(r"C:\Users\internet07\Desktop\python_apagar\selos\A3.png")
    
    largura_total = imagem_maior.width
    altura_total = imagem_maior.height
    imagem_resultante = Image.new("RGB", (largura_total, altura_total))
    
    imagem_resultante.paste(imagem_maior, (0, 0))
    imagem_resultante.paste(imagem_menor, (110, 10)) #se quiser mudar para outro lado variar entre 10 = esquerda e 110 # direita
    
    nome_final = os.path.splitext(nome_arquivo)[0] + "_final.jpg"
    imagem_resultante.save(nome_arquivo)

# Chama a função para obter a lista de imagens
imagens = acessar_imagens_os()

# Itera sobre as imagens e chama a função para concatenar e salvar a imagem final
for nome_arquivo, imagem in imagens:
    concatena_imagem_selo(nome_arquivo, imagem)
