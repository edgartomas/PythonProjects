
import requests
from bs4 import BeautifulSoup

url = "https://www.binance.com/pt/price/bitcoin"
res = requests.get(url)

#print(res)

soup = BeautifulSoup(res.text, "html.parser")

#print(soup)

for parent_div in soup.find_all('div', class_='css-dbxihu'):
   value = parent_div.get_text()
   print(value)

formatPrice = value[5:]
formatPrice = formatPrice.replace(",","")
price = float(formatPrice)
print(price)

idealprice = 67000
if price < idealprice:
   print("bitcoin value is favourable")






