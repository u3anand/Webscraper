import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.premierleague.com/')
soup = BeautifulSoup(page.content, 'html.parser')

a_tags = soup.find_all('a')
#print(a_tags)

article = ''
for i in soup.find_all('p'):
    article = article + ' ' +  i.text
    #print(article)

page1 = requests.get('https://www.premierleague.com/players')
soup1 = BeautifulSoup(page1.content, 'html.parser')

table1 = soup1.find('table')
table_rows1 = table1.find_all('tr')

for tr in table_rows1:
    td = tr.find_all('td')
    row1 = [i.text for i in td]
    #print(row1)

page2 = requests.get('https://www.premierleague.com/managers')
soup2 = BeautifulSoup(page2.content, 'html.parser')

table2 = soup2.find('table')
table_rows2 = table2.find_all('tr')

for tr in table_rows2:
    td2 = tr.find_all('td')
    row2 = [i.text for i in td2]
    #print(row2)

