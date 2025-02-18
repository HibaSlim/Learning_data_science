import requests
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://books.toscrape.com/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.content, 'html.parser')

books = []
article = soup.select('article.product_pod')
for book in article:
    title = book.h3.a['title']
    #print(title)
    price = book.select_one('p.price_color').text
    #print(price)
    books.append({'title':title,'price':price})
df = pd.DataFrame(books)
df.to_csv('books.csv',index=False)
print(df)