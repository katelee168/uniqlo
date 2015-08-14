import urllib
import string
import re
from bs4 import BeautifulSoup

'''URL parameters'''
base = "http://www.uniqlo.com/us/women/jeans/ultra-stretch.html"

'''Get menu'''
f = urllib.urlopen(base)

html = f.read()

soup = BeautifulSoup(html)
#print soup.prettify()

'''Find all food in html'''
for price in soup.find_all("div", {'class':'price-content'}):
    if "(BLACK)" in price.parent.find("a").text:
        if price.find_all("span", {'class':'price-red-flag'}).length()>1:
            print float(price.find("span").text.replace('$','').strip())

"""categories = []
for category in soup.find_all("div", {'class':'menusampcats'}):
    '''Clean category text'''
cat = category.text
categories.append(re.sub('[^\w ]', '', cat).strip())

foods = []
for food in soup.find_all("a", {"name": "Recipe_Desc"}):
    foods.append(food.text)

    return [categories, foods]
"""
