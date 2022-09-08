import requests
from bs4 import BeautifulSoup
import pandas as pd

#Make sure you have python3.10 or greater installed.  Don't forget to update pip
#pip3 update 
#pip3 install bs4
#pip3 install requests
#pip3 install requests
#pip3 install bs4
#pip3 install pandas
#pip3 install lxml

#This script scrapes h2 elments from a site.  

articlelist = []
url = 'https://example.org'  #https://javapipe.com/blog/ddos-types/'

r = requests.get(url)
#print(r.status_code)

soup = BeautifulSoup(r.content, features='lxml')
#check the class that wraps the div you want to isolate.  in this example, the page had a class called
#elementor-widget-wrap elementor-element-populated
articles = soup.find_all('div', class_ = 'elementor-widget-wrap elementor-element-populated')


for item in articles:
    h2=' \n'.join([x.get_text() for x in item.find_all('h2')])
    print(h2)
  

#   print('Added article:', article)
#   articlelist.append(article)

# df = pd.DataFrame(articlelist)
#df.to_csv('articlelist.csv', index=False)