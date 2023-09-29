import pandas as pd
import qrcode

# Caminho do arquivo Excel
caminho_do_arquivo = r'C:\_projetos\python\Kalung\humberto\teste.xlsx'

# Lê a planilha Excel
dados = pd.read_excel(caminho_do_arquivo)

# Itera sobre os URLs e gera um QR code para cada um
for idx, row in dados.iterrows():
    url = row['URL']  # Supondo que o nome da coluna com os URLs é 'URL'
    
    # Cria o QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'C:/_projetos/python/Kalung/humberto/qrcode_{idx}.png')  # Salva o QR code, indexando pelo número da linha

print("QR codes gerados com sucesso!")
