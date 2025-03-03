# Web Scrapy using beautifulsoup
from bs4 import BeautifulSoup
# import requests
from urllib.request import urlopen
import json

url = "https://books.toscrape.com/"
# r = requests.get(url)
page = urlopen(url)
soup = BeautifulSoup(page,'html.parser')
setdata = []
getdata = soup.find_all('article',class_='product_pod')

for d in getdata :
    name = d.find('h3').text.strip()
    price = d.find('p',class_='price_color').text.strip()
    stock = d.find('p',class_='instock').text.strip()

    setdata.append({
        'name':name,
        'price':price,
        'stock':stock,
    })

with open("raw_books_data.json","w") as f:
    json.dump(setdata,f)