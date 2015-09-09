import urllib
import string
import re
from bs4 import BeautifulSoup

def scrape():
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
            #if price.find_all("span", {'class':'price-red-flag'}).length()>1:
            s_pricepant = float(price.find("span").text.replace('$','').strip())
            print s_pricepant
            if float(s_pricepant) < 50:
                email(s_pricepant)
                break
        
def email(s_price):
    

def main():
    scrape()
    
if __name__ == "__main__": main()