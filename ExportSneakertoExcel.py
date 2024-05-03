import pd as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from httpx import Client

url = "C:/Users/p059060/Desktop/chromedriver.exe"
driver = webdriver.Chrome()
driver.get(url)


models = []
prices = []
cards = []
content = driver.page_source

    # Add the cookie header to the headers object
headers = {"Cookie":"sib_cuid=8411d43c-0b3a-4a99-b430-d17ca185f406; db_ui=2ef6c37a-61b5-5935-56d9-be3885e4db36; db_uicd=8388c481-13eb-d762-b405-a44b786d17a1; gender=men; PrestaShop-057bf586429233ffbee1f12383261cc1=da22250387f17bec026fbecca3f36587ae50049963b9981c972e4820393a621f%3Ad8Z6ffw53tjbLf6C2n0MIwdONZcmvzYk4IOpr%2FCBizvs2heDAnMA9zsyr3w%2B6nsjgRDz%2FW24v0pSeuJSrWfQ8q66BJonn6h5k%2F0D9joXBXqI3oE1E9IcElnh%2FOMgtMjkgfbB5GXxwnYV%2FPrp9%2BzKenT4YlbmoPZlfonQM9BY1Lc%3D; _vsid=9502ae17-e9fb-4a21-a5a3-2152e26056af"}

with Client(headers=headers) as client:
    response = client.get("https://www.footshop.eu/en/2311-nike-men-s-shoes")
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup)

    for element in soup.findAll('div', attrs={'class': 'Products_product_1JtLQ'}):
       # print("Hello, World!shoes3")
       # model = element.find('h4', attrs={'class': 'Product_name_3eWGG'})
        #print(element)
        for line in element.get_text().split('\n'):
            parts = line.split(' ')
            ocorrencia = parts[-1]
            name = " ".join(parts[1:-2])
            #print(parts)
            cards.append({'preco': ocorrencia , "name": name})

    print(cards)
    #print(parts)

df = pd.DataFrame({'preco': cards})
df.to_csv('sneakers.csv', index=False, encoding='utf-8')



       #print(price)
       # models.append(model.text)
       #prices.append(price.text)


