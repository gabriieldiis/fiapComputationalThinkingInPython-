import os
from PIL import Image

def resize_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            try:
                with Image.open(image_path) as img:
                    if img.width == 1000 and img.height == 1000:
                        resized_img = img.resize((500, 500))  # Correção aqui
                        resized_img.save(image_path)
                        print(f"Resized {filename} to 180x180 px")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    target_folder = r'C:\Users\internet07\Downloads\drive-download-20230912T182323Z-001\Produtos'
    resize_images_in_folder(target_folder)

if __name__ == "__main__":
    main()
