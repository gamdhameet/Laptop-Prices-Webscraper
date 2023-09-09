# import random
# import time
import random

import requests
from bs4 import BeautifulSoup
from xlwt import Workbook
proxy = 'http://114.121.248.251:8080'
xl = Workbook()
sheet = xl.add_sheet('sheet')
sheet.write(0, 0, 'Laptop Description')
sheet.write(0, 1, 'Price in $')
URL = ["https://www.amazon.com/s?k=laptops&ref=nb_sb_noss"]
HEADER = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'})
r = requests.get(URL, headers=HEADER)
# time.sleep(5)
print(r)
# print(r.content)
# print(r.content)
# print(r.url)

soup = BeautifulSoup(r.text, 'lxml')
productCard = soup.find_all('div',
                            class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")
# products = soup.find_all('span', class_="a-size-medium a-color-base a-text-normal")
# prices = soup.find_all('span', class_="a-price-whole")
for i, product in enumerate(productCard):
    s1 = product.find_next('span', class_="a-size-medium a-color-base a-text-normal").text
    s2 = product.find_next('span', class_="a-price-whole").text
    sheet.write(i + 1, 0, s1)
    sheet.write(i + 1, 1, s2)
    print(s1)
    print(s2)
xl.save(f'{random.randint(0,100000)}.xls')

