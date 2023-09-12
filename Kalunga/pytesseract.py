from pytesseract import pytesseract

caminho_pytesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
caminho_pytesseract_cmd = caminho_pytesseract

texto = pytesseract.image_to_string('downloaded_images\\Sem-Título-1.jpg')
print(texto)
