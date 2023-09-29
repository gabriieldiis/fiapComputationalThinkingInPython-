import barcode
from barcode import Code128

def gerar_codigo_barras (valor): 
    codigo = Code128(valor)
    codigo.save('barcode')
    print("Codigo de barras gerado")

valor = "1234-5678-9012"
gerar_codigo_barras(valor)