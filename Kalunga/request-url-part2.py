import requests


lista_urls = [
'https://img.kalunga.com.br/fotosdeprodutos/478159.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/478161.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/478162.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/478163.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/478164.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/478165.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/478167.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/479710.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/479759.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/998399.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/999367.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/999368.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/999369.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/999467.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/999800.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/999801.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/999802.jpg',
'https://img.kalunga.com.br/fotosdeprodutos/999810.jpg',
]


for url in lista_urls:
    requisicao = requests.get(url)
    if requisicao.status_code == 200:
        print(f'{url} {requisicao}')
    else:
        print(f'{url} nao encontrado')
