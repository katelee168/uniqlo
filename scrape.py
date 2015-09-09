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
            if float(s_pricepant) < 49.9:
                email(s_pricepant)
                break
        
def email(s_price):
    import sendemail

    # name of recipient
    recipient = ["cloudsrpretty168@gmail.com"]

    # Create the body of the message (a plain-text and an HTML version).
    text = 'there\'s a sale!! for ' + str(s_price)
    html = """\
<html>
  <body style="font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue&quot;;">
      <div style="padding: 20px 15px;margin-bottom: 15px;margin-left: 10%;width: -webkit-calc(80% - 30px);font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue&quot;;font-size: 14px;">
        Congrats! Your pants are on sale for """ + str(s_price) + """ 
      </div>
  </body>
</html>
"""
    sendemail.send_email(recipient, text, html)
def main():
    scrape()
    
if __name__ == "__main__": main()
