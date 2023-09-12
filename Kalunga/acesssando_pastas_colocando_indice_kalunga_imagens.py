import os

# Define o caminho da pasta
caminho_da_pasta = r"C:\Users\internet07\Desktop\acao\z"

# Verifica se o caminho da pasta é válido
if not os.path.isdir(caminho_da_pasta):
    print("Caminho da pasta inválido.")
    exit()

# Itera sobre os arquivos na pasta
for nome_arquivo in os.listdir(caminho_da_pasta):
    # Verifica se o arquivo é um arquivo (não uma pasta)
    if os.path.isfile(os.path.join(caminho_da_pasta, nome_arquivo)):
        # Verifica se o nome do arquivo tem pelo menos 7 caracteres
        if len(nome_arquivo) >= 7:
            # Adiciona 'z' na posição 7 do nome do arquivo
            novo_nome = nome_arquivo[:6] + 'z' + nome_arquivo[6:]
            # Renomeia o arquivo
            os.rename(os.path.join(caminho_da_pasta, nome_arquivo), os.path.join(caminho_da_pasta, novo_nome))
            print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome}")
        else:
            print(f"Nome do arquivo muito curto: {nome_arquivo}")

print("Concluído!")
