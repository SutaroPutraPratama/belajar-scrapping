from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.bilibili.tv/id/category?season_type=1,4"
driver_path = 
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
titles = soup.find_all('a', class_='bstar-video-card__title-text')
anime_titles = []

for title in titles:
    anime_titles.append(title.text.strip())

df = pd.DataFrame({'Judul Anime': anime_titles})
df.to_csv('judul_anime.csv', index=False)
driver.quit()

print("Data judul anime telah berhasil disimpan dalam file judul_anime.csv")