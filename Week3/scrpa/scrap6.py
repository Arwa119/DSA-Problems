from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

gamingDesktops = {
    "Name": [],
    "Price": [],
    "Sold": [],
    "FreeShipping": [],
    "StoreName": [],
    "Link": []
}

driver = webdriver.Chrome()
driver.get("https://www.aliexpress.com/w/wholesale-Desktops.html?isFromCategory=y&categoryUrlParams=%7B%22q%22%3A%22Desktops%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22category_navigate%22%2C%22sg_search_params%22%3A%22%22%2C%22guide_trace%22%3A%22b3269b84-0b88-4bd8-ab28-7c3cf27ff97d%22%2C%22scene_id%22%3A%2237749%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22en%22%2C%22bizScene%22%3A%22category_navigate%22%2C%22guideModule%22%3A%22category_navigate_vertical%22%2C%22postCatIds%22%3A%227%2C21%22%2C%22scene%22%3A%22category_navigate%22%7D&g=n&SearchText=Desktops")
sleep(5)

for i in range(5):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for item in soup.find_all("div", class_="search-item-card-wrapper-list"):
        name = item.find("h3", class_="multi--titleText--nXeOvyr").text
        sold = item.find("span", class_="multi--trade--Ktbl2jB")
        sold = sold.text if sold else "0 sold"
        freeshipping = True if item.find("span", class_="tag--text--1BSEXVh tag--textStyle--3dc7wLU multi--serviceStyle--1Z6RxQ4") else False
        storeName = item.find("a", class_="cards--storeLink--XkKUQFS").text
        link = item.find("a", class_="search-card-item")["href"]
        price = ""
        for span in item.find("div", class_="multi--price-sale--U-S0jtj").find_all("span"):
            price += span.text
        for key, value in zip(gamingDesktops.keys(), [name, price, sold, freeshipping, storeName, link]):
            gamingDesktops[key].append(value)
    driver.find_element(By.CLASS_NAME, "comet-pagination-item-link").click()
    sleep(5)
driver.quit()

df = pd.DataFrame(gamingDesktops)
print(df)
df.to_csv("gaming.csv", index=False)