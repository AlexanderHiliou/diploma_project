import requests
from bs4 import BeautifulSoup as BS
import os


class ImgPars:

    def __init__(self, country):
        self.country = country.lower()
        self.url = 'https://wikiway.com'


    def get_html(self):
        url = f'https://wikiway.com/{self.country}/goroda'
        page = requests.get(url)
        if page.status_code == 200:
            return page.text
        else:
            return 'Error'


    def get_cities(self):
        result = []
        soup = BS(self.get_html(), 'html.parser')
        soup = soup.findAll('a', class_='ob-href')
        for href in soup:
            tag = href.get('href')
            result.append(self.url + tag + 'photo')
        return result[:3]


    def get_images(self):
        result = []
        for link in self.get_cities():
            directory_name = link.split('/')[-2].capitalize()
            if not os.path.exists(directory_name):
                os.mkdir(directory_name)
            page = requests.get(link)
            soup = BS(page.text, 'html.parser')
            soup = soup.findAll('a', class_='photo-item-inner fancybox')
            for href in soup:
                href = href.get('href')
                result.append(self.url + href)
            for photo in result[::-1][:10]:
                name = photo.split('/')[-1]
                photo = requests.get(photo)
                with open(f'{name}', 'wb') as file:
                    file.write(photo.content)
                    os.replace(f'{name}', f'{directory_name}/{name}')
            result.clear()


    def prep_img_to_db(self, city):
        current_dir = os.getcwd() + f'/{city}'
        result = os.listdir(current_dir)
        return result

                
if __name__ == "__main__":
    country_list = ['Finland', 'Sweden', 'Norway', 'Daniya']
    for country in country_list:
        img_pars = ImgPars(f'{country}')
        img_pars.get_images()

    
    