import os
import requests
import threading
from urllib.parse import urlparse


def download_image(url, save_folder):
    response = requests.get(url)
    if response.status_code == 200:
        parsed_url = urlparse(url)
        image_name = os.path.basename(parsed_url.path)
        save_path = os.path.join(save_folder, image_name)

        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {url} as {image_name} \n")
    else:
        print(f"Failed to download {url}")


def main():
    image_urls = [

        'https://img.kalunga.com.br/fotosdeprodutos/388907d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/388908d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/389558d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/389559d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/389560d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/389561d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/389567d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/389684d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/389686d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/391551d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/391556d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/391561d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/391678d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/391679d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/394102d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/394103d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/394104d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/394122d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/394159d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/394257d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/394259d.jpg'
    ]

    save_folder = 'downloaded_images'
    os.makedirs(save_folder, exist_ok=True)

    threads = []
    for url in image_urls:
        thread = threading.Thread(target=download_image, args=(url, save_folder))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
