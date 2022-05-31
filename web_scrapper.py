import requests
from bs4 import BeautifulSoup as bs
import csv




url = "https://www.flipkart.com/audio-video/~cs-53mrbtcuf5/pr?sid=0pm&collection-tab-name=Audio+And+Video&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&fm=neo%2Fmerchandising&iid=M_5e60755d-2763-40de-9ace-b00a7676196c_2_372UD5BXDFYS_MC.9JGNW7M0TUHD&otracker=hp_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Electronics~Audio~All_9JGNW7M0TUHD&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=9JGNW7M0TUHD"
page = requests.get(url)
soup = bs(page.content, 'html.parser')


parent_divs = soup.findAll('div',class_="_4ddWXP")

data = []

for div in parent_divs:
    product_name = div.find('a','s1Q9rs')
    
    if "headset" in product_name.text.lower():
        rating = div.find('div','_3LWZlK')
        price = div.find('div','_30jeq3')
        data.append({'Product Name':product_name.text,'Rating':rating.text,'Price':price.text})

headers = ['Product Name','Rating',"Price"]      
with open('flipkart_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)