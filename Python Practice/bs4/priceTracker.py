import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Google-Pixel-Just-Black-Storage/dp/B07K46215Z/ref=sr_1_5?keywords=google+pixel+3a&qid=1563033084&s=gateway&sr=8-5'
headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
page = requests.get(URL,headers)

soup = BeautifulSoup(page.content,'html.parser')
title = soup.find(id='priceblock_ourprice').get_text()
price = title[2:8]
print(price)
