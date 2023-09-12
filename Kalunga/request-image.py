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
        'https://img.kalunga.com.br/fotosdeprodutos/602564d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/602601d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/602624d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/602747d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/602748d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/602749d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/602823d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/603396d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/603397d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/603398d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/603399d.jpg',
        'https://img.kalunga.com.br/fotosdeprodutos/603400d.jpg',
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
