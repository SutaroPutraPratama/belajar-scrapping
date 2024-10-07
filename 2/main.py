from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import pathlib
import urllib.request

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('log-level=3')

service = Service(executable_path=r'./driver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.nasa.gov/image-of-the-day/')
images = driver.find_elements(By.XPATH, '//div[@class="hds-gallery-item-single hds-gallery-image"]//img')
os.makedirs('./images', exist_ok=True)
count = 0
for image in images:
    src = image.get_attribute('src')
    if src:
        print(src)
        suffix = pathlib.Path(src).suffix
        if suffix and suffix.strip():
            urllib.request.urlretrieve(src, f'./images/image{count+1}{suffix}')
        count += 1
driver.close()