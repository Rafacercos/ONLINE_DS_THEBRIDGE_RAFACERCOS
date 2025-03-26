from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get(url, headers=headers)

html = response.content
soup = bs(html, 'html.parser')

dict_1 = {"Título":[],
          "Año":[],
          "Duracion":[],
          "Rating":[]}
for x in soup.find_all("h3")[1:-1]:
    dict_1["Título"].append(x.get_text()[3:])

for i in soup.find_all("span",class_ = "sc-f30335b4-7 jhjEEd cli-title-metadata-item")[::3]:
    dict_1["Año"].append(i.get_text())

for i in soup.find_all("span",class_ = "sc-f30335b4-7 jhjEEd cli-title-metadata-item")[1::3]:
    dict_1["Duracion"].append(i.get_text())

for x in soup.find_all("span",class_="ipc-rating-star--rating"):
    dict_1["Rating"].append(i.get_text())

df = pd.DataFrame(dict_1)
df.index=(range(1,26))
print(df)