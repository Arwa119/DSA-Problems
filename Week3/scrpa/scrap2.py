import time  
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service


service = Service(executable_path="C:/Users/Arwa Mahwish/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.whatmobile.com.pk/")  

time.sleep(5)  

soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

products = []
prices = []
usd_prices = []
product_links = []
image_urls = []


for li in soup.find_all("li", class_="product"):
    name_tag = li.find("h4", class_="p4 biggertext")
    name = name_tag.get_text(strip=True).replace("\n", " ")
    price = li.find("span", class_="PriceFont").get_text(strip=True)
    usd_price = li.find("a")["title"].replace("Price USD ", "")
    link = li.find("a")["href"]
    image_url = li.find("img")["src"]
    products.append(name)
    prices.append(price)
    usd_prices.append(usd_price)
    product_links.append(link)
    image_urls.append(image_url)

df = pd.DataFrame({
    "Product Name": products,
    "Price (PKR)": prices,
    "Price (USD)": usd_prices,
    "Product Link": product_links,
    "Image URL": image_urls
})
df.to_csv("mobile.csv", index=False, encoding="utf-8")