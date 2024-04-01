from selenium import webdriver
from bs4 import BeautifulSoup as bs

# Set up the Selenium webdriver (make sure you have installed the appropriate browser driver)
driver = webdriver.Chrome()  # You can change to Firefox or other supported browsers

url = 'https://finance.yahoo.com/lookup'

driver.get(url)

# Extract the HTML content after the page has fully loaded
html_data = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = bs(html_data, 'html.parser')

# Find the element you are interested in
last_price = soup.find('td', {'class': 'data-col2 Ta(end) Pstart(20px)'})

print(last_price)
