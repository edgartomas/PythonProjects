import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.com/itm/235511902951?epid=9050303340&itmmeta=01HWX67WSFRJJEJTHG2FHGJMN9&hash=item36d59a72e7:g:8U0AAOSwm~VmE-AJ&itmprp=enc%3AAQAJAAAA4HNRzRfm7JGtsirSRs3pBdVH0b0zd0LeHAFYvcSF8XzGIjR11COhuv7HoKOzLJgsvTvw%2BBBttGsgVIsUOTUEH7%2BXQLR5G6U9JQgaEn2U4HQwgQMzjL6OhV8Km4zLl585Xor99HLdk7sj3Pyis21xZ8nIm94EFxdZin0bgBXtYJuxVFmlLlzj3tuwXZiwDa%2Fr9MDYvUszrQ4O--ZQ1tF1xC3kzX3Xn%2BphV9b3F%2BDEse%2F%2Bf9k00ApK27rWMcbNwBI6q3L8VLNkkzqpmzHgwE3CY%2B9OI5t0IETOHeVxKV1iQG5R%7Ctkp%3ABFBMgM2fpudj"
res = requests.get(url)

#print(res)

soup = BeautifulSoup(res.text, "html.parser")
value = soup.select(".x-price-primary .ux-textspans")
unformattedPrice = value[0]
unformattedPrice = unformattedPrice.text

#print(unformattedPrice)

formatedPrice = unformattedPrice[4:]
#print(formatedPrice, "cheguei")
formatedPrice = formatedPrice.replace(",", "")

#print(formatedPrice, "cheguei 2")
price = float(formatedPrice)
print(formatedPrice)

idealprice = 10000
if price > idealprice:
   print("airpods value is not favourable")

#mainContent > div.vim.d-vi-evo-region > div.vim.x-price-section.mar-t-20 > div > div > div.x-price-primary > span
#print(soup)



