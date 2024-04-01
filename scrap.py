from selenium import webdriver
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome()

url = 'https://finance.yahoo.com/lookup'

driver.get(url)
html_data = driver.page_source

driver.quit()

soup = bs(html_data, 'html.parser')

# Find the element you are interested in
last_price = soup.find('td', {'class': 'data-col2 Ta(end) Pstart(20px)'})

print(last_price)
