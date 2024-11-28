from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

webdriver_path = "C:/Users/Arwa Mahwish/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe"  
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

url = 'https://bachydicar.com/'
driver.get(url)

time.sleep(5)  

page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, 'html.parser')
products = soup.find_all('li', class_='wc-block-grid__product')

product_names = []
prices_pk = []
prices_usd = []
product_links = []
image_urls = []

conversion_rate = 270  
for product in products:
    title = product.find('div', class_='wc-block-grid__product-title').text.strip()
    price_text = product.find('div', class_='wc-block-grid__product-price').text.strip()

    try:
        price_pk = int(price_text.replace('₨', '').replace(',', '').split()[1])  # Extract the current price in PKR
    except (IndexError, ValueError):
        price_pk = 0  
   

    img_url = product.find('div', class_='wc-block-grid__product-image').img['src']
    product_url = product.find('a', class_='wc-block-grid__product-link')['href']

    product_names.append(title)
    prices_pk.append(price_pk)
    product_links.append(product_url)
    image_urls.append(img_url)

df = pd.DataFrame({
    "Product Name": product_names,
    "Price (PKR)": prices_pk,
    "Product Link": product_links,
    "Image URL": image_urls
})

csv_file = 'Toys.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file, index=False, encoding="utf-8")
