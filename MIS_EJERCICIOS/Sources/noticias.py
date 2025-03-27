import requests
import pandas as pd

url = "http://api.mediastack.com/v1/news?access_key=5de7eb8807d19d7976f5d23a3b80ef0c&limit=150"
parametros = {
    "access_key": "5de7eb8807d19d7976f5d23a3b80ef0c",
    "languages": "en",
    "limit": 100,
    "date_from": "2024-05-11",
    "date_to": "2024-05-12" 
}
response = requests.get(url,params=parametros)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error{response.status_code}:{response.text}")

noticias = {
    "autor": [],
    "titulo":[],
    "descripcion":[],
    "url":[],
    "fuente":[],
    "fecha":[]
}
    
lista_vacia = []

for noticia in data["data"]:
    for caracteristica in noticia.items():
        lista_vacia.append(caracteristica)

lista_vacia_2 = []
lista_autores = lista_vacia[::10]
for i in lista_autores:
    for autor in i:
        lista_vacia_2.append(autor)

lista_autores_final = lista_vacia_2[1::2]
noticias["autor"] = lista_autores_final
lista_titulos = lista_vacia[1::10]

lista_vacia_3 = []
for i in lista_titulos:
    for titulo in i:
        lista_vacia_3.append(titulo)

noticias["titulo"]=lista_vacia_3[1::2]
lista_descripciones = lista_vacia[2::10]

lista_vacia_4 = [] 
for i in lista_descripciones:
    for descripcion in i:
        lista_vacia_4.append(descripcion)

noticias["descripcion"] = lista_vacia_4[1::2]
lista_url = lista_vacia[3::10]

lista_vacia_5 =[]
for i in lista_url:
    for url in i:
        lista_vacia_5.append(url)
noticias["url"]= lista_vacia_5[1::2]
lista_fuente = lista_vacia[4::10]

lista_vacia_6 =[]
for i in lista_fuente:
    for fuente in i:
        lista_vacia_6.append(fuente)

noticias["fuente"]= lista_vacia_6[1::2]
lista_fechas = lista_vacia[9::10]
lista_vacia_7 =[]
for i in lista_fechas:
    for fecha in i:
        lista_vacia_7.append(fecha)

noticias["fecha"]=lista_vacia_7[1::2]
noticias_df = pd.DataFrame(noticias)

print(noticias_df)
noticias_df.to_csv("C:/Users/rafac/ONLINE_DS_THEBRIDGE_RAFACERCOS/MIS_EJERCICIOS/Sources",index=False)