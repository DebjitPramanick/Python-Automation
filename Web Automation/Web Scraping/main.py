from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driverLoc = 'Web Automation/chromedriver'

driver = webdriver.Chrome(driverLoc)
name = []
ratings = []
driver.get('https://www.imdb.com/chart/top/')

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('td', attrs={'class', 'titleColumn'}):
    name.append(str(a.text).strip())

for b in soup.findAll('td', attrs={'class', 'ratingColumn imdbRating'}):
    ratings.append(str(b.text).strip())

df = pd.DataFrame({'Product Name': name, 'Ratings': ratings})
df.to_csv('products.csv', index=True, encoding='utf-8')

