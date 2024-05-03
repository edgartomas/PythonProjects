import requests
from bs4 import BeautifulSoup

url = "https://www.skyshowtime.com/pt?lid=wycodr8y54th&market=pt&LoB=sst&Channel=sea&Platform=gad&Mobj=acq&campaign_name=22q4aomulti&Campaign_ID=71700000101442961&Placement_ID=na&Creative_ID=na&dispatch_id=na&datena&gad_source=1&gclid=CjwKCAjw88yxBhBWEiwA7cm6pcuHqvl-izJBPq_WB0T6w7ySvt_5qe8hUIbPgX_6nFU6TfxTI2XlWBoCEc8QAvD_BwE&gclsrc=aw.ds"
res = requests.get(url)

#print(res)

soup = BeautifulSoup(res.text, "html.parser")
value = soup.select("#ib-section-S-6795b370-963a-479b-bf3f-f2b68d51caa9 > div > div > div > div > div > p:nth-child(1) > span.richTextstyles__RTColorSpan-sc-10kl41a-2.ikgSYy > span")

print(value)
unformattedPrice = value[0]
unformattedPrice = unformattedPrice.text

print(unformattedPrice, "cheguei")

formatedPrice = unformattedPrice[:-2]
print(formatedPrice, "cheguei 2")
formatedPrice = formatedPrice.replace(",", "")


price = float(formatedPrice)
print(formatedPrice)

idealprice = 500
if price < idealprice:
   print("sky  value is favourable")







