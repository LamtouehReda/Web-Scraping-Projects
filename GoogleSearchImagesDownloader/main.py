import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os
from PIL import Image
import io
import hashlib


def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)    
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            break
        #     print("Found:", len(image_urls), "image links, looking for more ...")
        #     time.sleep(30)
        #     return
        #     load_more_button = wd.find_element_by_css_selector(".mye4qd")
        #     if load_more_button:
        #         wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls

def persist_image(folder_path:str,file_name:str,url:str,cmpe:int):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        folder_path = os.path.join(folder_path,file_name)
        if os.path.exists(folder_path):
            file_path = os.path.join(folder_path,f'{cmpe}.jpg')
        else:
            os.mkdir(folder_path)
            file_path = os.path.join(folder_path,f'{cmpe}.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=100)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")

if __name__ == '__main__':
    wd = webdriver.Chrome(ChromeDriverManager().install())
    queries = [
    # 'Mausolée Mohammed V',
    # 'Kasbah des oudayas',
    # 'Medina de Rabat',
    # 'Palais Royal de Rabat',
    # 'Rabat Old Town',
    # 'Cathédrale Saint-Pierre',
    # 'Galerie Bab Rouah',
    'Musée Mohammed VI',
    'Jardin exotique de Bouknadel',
    'Jardin d’essais botaniques',
    'Parc Hassan II'
    		   ]  
    queries1=[
  # 'Porte Bab Boujloud',
  # 'La mosquée Al Quaraouiyine',
  # 'Tannerie Chouara',
  # 'Mausolée de Moulay Idriss',
  # 'Place Seffarine',
  # 'Médersa Attarine',
  # 'Médersa Bou Inania',
  # 'Méders Cherratine',
  # 'Jardin Jnan Sbil',
  # 'Musée Nejjarîn des arts et métiers du bois',
  # 'Palais Royal de Fès',
  # 'Palais Glaoui',

  # 'Place Jamaa El fna',
  # 'Souk de Marrakech',
  # 'Palais de la Bahia',
  # 'Palais El Badi',
  # 'Médersa Ben Youssef',
  # 'Tombeaux saâdiens',
  # 'Musée de Marrakech',
  # 'Musée Dar si Said',
  # 'Jardin Majorelle',
  # 'Palmerie de Marrakech ',

  # 'Médina de Meknès',
  # 'Bab Mansour',
  # 'Médersa Bou Inania',
  # 'Heri es Souani',
  # 'Moulay Idriss Zerhoun',
  # 'Sahrij Swani',
  # 'Bab El-khemis',
  # 'Prison de Kara',
  # 'Mausolée Moulay Ismail',
  # 'Bab Berdaine',
  # 'Palais El Mansour',
  'Grande mosquée de Meknès',
  'Oualili'
    ]
    for query in queries1:
        wd.get('https://google.com')
        search_box = wd.find_element_by_css_selector('input.gLFyf')
        search_box.send_keys(query+' Images HD')
        links = fetch_image_urls(query,100,wd)
        images_path = r'C:\Users\Lenovo\OneDrive\Bureau\Python\Web Scrapping\GoogleSearchImagesDownloader'
        cmpe=1
        for i in links:
            persist_image(images_path,query,i,cmpe)
            cmpe+=1
    wd.quit()