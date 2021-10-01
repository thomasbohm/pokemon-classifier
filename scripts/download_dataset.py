"""
Script to download images for the first 151 pokemon from google images and store them in the dir data/images/.
If an images cannot be downloaded it is skipped.
The script is inspired by: https://python.plainenglish.io/how-to-automatically-download-bulk-images-for-your-dataset-using-python-f1efffba7a03
"""

import os
import requests
from bs4 import BeautifulSoup
from progressbar import progressbar

pokeapi_base_url = 'https://pokeapi.co/api/v2/pokemon'
google_base_url = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1920&bih=937&'
user_agent = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36' }
image_dir = 'data/images'

def download_images(search_term, num_images):
    search_url = google_base_url + 'q=' + search_term
    res = requests.get(search_url, headers=user_agent)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'}) # single images have these css classes

    n = 0
    links = []
    for result in results:
        try:
            link = result['data-src']
            links.append(link)
            n += 1
            if n >= num_images:
                break
        except KeyError:
            continue

    for i, link in enumerate(links):
        res = requests.get(link)
        image_name = f'{image_dir}/{search_term}{i+1:03d}.jpg'

        with open(image_name, 'wb') as f:
            f.write(res.content)

def download_images_for_all_pokemon():
    print('Downloading images for 151 pokemon...')
    for i in progressbar(range(1, 152)):
        res = requests.get(f'{pokeapi_base_url}/{i}/').json()
        pokemon_name = res['name']
        download_images(pokemon_name, 100)
    print('Done.')

if __name__ == "__main__":
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    download_images_for_all_pokemon()
