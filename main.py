from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

path = 'C:/Users/lucas/Downloads/chromedriver-win64/chromedriver.exe'

cService = webdriver.ChromeService(executable_path=path)

website = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/gm-chevrolet/celta/estado-go/grande-goiania-e-anapolis'
driver = webdriver.Chrome(service=cService)
driver.get(website)
driver.maximize_window()

pagination = driver.find_element(by=By.XPATH, value='//*[@id="listing-pagination"]')
all_pages = pagination.find_elements(by=By.TAG_NAME, value='button')
pages = all_pages[1:-2]
last_page = int(pages[-1].text)
next_page_button = all_pages[-2].find_element(by=By.TAG_NAME, value='a')

description_ad = []
price_car = []
ad_features = []

current_page = 1

while current_page <= last_page:
    time.sleep(2)

    container = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[7]')))
    ads = WebDriverWait(container, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'olx-ad-card')))

    for ad in ads:
        items = WebDriverWait(ad, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'olx-ad-card__labels-item')))
        description_ad.append(ad.find_element(by=By.CLASS_NAME, value='olx-ad-card__title-link').text)
        try:
            price_ad = ad.find_element(by=By.CLASS_NAME, value='olx-ad-card__price').text
        except:
            price_ad = '0,00'

        price_car.append(price_ad)

        features = []

        list(map(lambda item: features.append(item.text) if len(item.text) != 0 else None, items))

        ad_features.append(features)

    if current_page != last_page:
        pagination = driver.find_element(by=By.ID, value='listing-pagination')
        all_pages = pagination.find_elements(by=By.TAG_NAME, value='button')
        next_page_button = all_pages[-2].find_element(by=By.TAG_NAME, value='a')
        
        driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)
        time.sleep(2)

        next_page_button.click()

    current_page = current_page + 1

df = pd.DataFrame({'descricao_anuncio': description_ad,
                   'caracteristicas': ad_features,
                   'preco': price_car
                   })

df.to_csv('anuncios_carros_olx.csv', index=False)
df.to_json('data.json', orient='records')
