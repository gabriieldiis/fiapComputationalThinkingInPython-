# library
from PIL import Image
import matplotlib.pyplot as plt
  
# opening up of images
img = Image.open(r"C:\Users\internet07\Desktop\python_apagar\176101d.jpg")
img1 = Image.open(r"C:\Users\internet07\Desktop\python_apagar\formato.png")
img.size
img1.size
img_size = img.resize((180, 180))
img1_size = img1.resize((54, 43))
  
# creating a new image and pasting 
# the images
img2 = Image.new("RGB", (180, 180), "white")
  
# pasting the first image (image_name,
# (position))
img2.paste(img_size, (180, 180))
  
# pasting the second image (image_name,
# (position))
img2.paste(img1_size, (54,43))
  
plt.imshow(img2)
plt.show()  # Adicionando esta linha para exibir a imagem