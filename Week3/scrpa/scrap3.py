import time  
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:/Users/Arwa Mahwish/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.com/s?k=women+watch")  


time.sleep(5)  

soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

products = []
ratings = []
prices = []
product_links = []
image_urls = []

for div in soup.find_all("div", {"data-component-type": "s-search-result"}):

    name_tag = div.find("h2", class_="a-size-mini")
    if name_tag:
        name = name_tag.get_text(strip=True)
    
        rating_tag = div.find("span", class_="a-declarative")
        rating = rating_tag["aria-label"] if rating_tag and rating_tag.has_attr("aria-label") else "No rating"
   
        price_tag = div.find("span", class_="a-price-whole")
        if price_tag:
            price = price_tag.get_text(strip=True)
        else:
            price = "Price not available"
       
        link_tag = div.find("a", class_="a-link-normal")
        link = "https://www.amazon.com" + link_tag["href"] if link_tag else "Link not available"
    
        image_tag = div.find("img", class_="s-image")
        image_url = image_tag["src"] if image_tag else "Image not available"

        products.append(name)
        ratings.append(rating)
        prices.append(price)
        product_links.append(link)
        image_urls.append(image_url)

df = pd.DataFrame({
    "Product Name": products,
    "Rating": ratings,
    "Price": prices,
    "Product Link": product_links,
    "Image URL": image_urls
})
df.to_csv("watches.csv", index=False, encoding="utf-8")