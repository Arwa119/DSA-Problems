from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="C:/Users/Arwa Mahwish/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

products = []
prices = []
discounts = []
ratings = []
image_urls = []

driver.get("https://www.daraz.pk/")
soup = BeautifulSoup(driver.page_source, "html.parser")

for a in soup.find_all("a", class_="pc-custom-link jfy-item hp-mod-card-hover"):
    name = a.find("div", class_="card-jfy-title")
    price = a.find("span", class_="price")
    discount = a.find("span", class_="hp-mod-discount")
    rating = a.find("div", class_="card-jfy-rating-layer top-layer checked")
    image = a.find("img")
    
    if name and price and image:

        products.append(name.get_text(strip=True))
        prices.append(price.get_text(strip=True))
        discounts.append(discount.get_text(strip=True) if discount else "No discount")
        ratings.append(rating['style'].replace('width: ', '').replace('%;', '') if rating else "No rating")
        image_urls.append(image['src'])
    if len(products) == 50:
        break

df = pd.DataFrame({
    "Product Name": products,
    "Price": prices,
    "Discount": discounts,
    "Rating (%)": ratings,
    "Image URL": image_urls
})
df.to_csv("Daraz.csv", index=False, encoding="utf-8")
driver.quit()