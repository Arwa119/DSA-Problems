import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service


service = Service(executable_path="C:/Users/Arwa Mahwish/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.com/s?k=travel+backpack&_encoding=UTF8&content-id=amzn1.sym.1faf5a75-f10d-481a-9299-d0fe2e7649bd&pd_rd_r=e82b5c2a-0af3-444a-b19b-0e0fccce123f&pd_rd_w=8BMah&pd_rd_wg=QSUHD&pf_rd_p=1faf5a75-f10d-481a-9299-d0fe2e7649bd&pf_rd_r=G1X99QSCDB5MC6WENGRX&ref=pd_hp_d_btf_unk")  # Replace with actual URL


time.sleep(5) 

soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()


products = []
prices = []
usd_prices = []
product_links = []
image_urls = []

for div in soup.find_all("div", class_="puisg-col-inner"):

    name_tag = div.find("h2", class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
    name = name_tag.get_text(strip=True) if name_tag else "N/A"

    price_tag = div.find("span", class_="a-color-base")
    usd_price = price_tag.get_text(strip=True).replace("$", "") if price_tag else "N/A"
    link_tag = name_tag.find("a") if name_tag else None
    link = link_tag["href"] if link_tag else "N/A"
    image_tag = div.find("img")
    image_url = image_tag["src"] if image_tag else "N/A"

    products.append(name)
    prices.append("N/A")  
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
df.to_csv("Amazon_Phones.csv", index=False, encoding="utf-8")