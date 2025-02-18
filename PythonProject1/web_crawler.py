import requests
from bs4 import BeautifulSoup

'''page = requests.get('https://en.wikipedia.org/wiki/History_of_Tunisia')
print(page.content)
soup = BeautifulSoup(page.content,'html.parser')'''
'''print(soup.prettify())'''
'''print(list(soup.children))'''

'''text1 = soup.find_all('p')
print(text1[1])
print(text1[1].text)'''

'''image = soup.find_all('img',class_='mw-file-element')
for img in image:
    print(img["src"])'''

'''image = soup.find_all('img',class_='mw-file-element')
for img in image:
    print(img["src"])'''

page = requests.get('https://en.wikipedia.org/wiki/Table_(database)')
soup = BeautifulSoup(page.content,'html.parser')
parent_div = soup.find('main',id='content',class_='mw-body')
div = parent_div.find('div',class_='navbox')
table = div.find('table')
#ou bien
table = soup.find('table')
li = table.find_all('li')
rows = table.find_all('tr')
for row in rows:
    value = row.find_all(['th', 'td'])
    text = [v.get_text(strip= True) for v in value]
    print('t'.join(text))

