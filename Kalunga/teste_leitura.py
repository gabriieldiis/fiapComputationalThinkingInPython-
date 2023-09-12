from pytesseract import pytesseract

caminho_pytesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
texto = pytesseract.image_to_string(r'C:\_projetos\FIAP\python\fiapComputationalThinkingInPython-\Kalunga\downloaded_images\Sem-Título-1.jpg')
print(texto)
