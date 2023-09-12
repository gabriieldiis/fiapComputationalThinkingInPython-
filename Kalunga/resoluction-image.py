import os
import requests
import threading
from urllib.parse import urlparse
from PIL import Image


def download_image(url, save_folder):
    response = requests.get(url)
    if response.status_code == 200:
        parsed_url = urlparse(url)
        image_name = os.path.basename(parsed_url.path)
        save_path = os.path.join(save_folder, image_name)

        with open(save_path, 'wb') as f:
            f.write(response.content)

        # Open the downloaded image
        image = Image.open(save_path)

        # Resize the image to 180x180 px
        resized_image = image.resize((180, 180), Image.ANTIALIAS)

        # Save the resized image back
        resized_image.save(save_path)

        print(f"Downloaded and resized {url} as {image_name}")
    else:
        print(f"Failed to download {url}")


def main():
    image_urls = [
        'https://img.kalunga.com.br/fotosdeprodutos/426833d.webp',
        # Add more image URLs here
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
