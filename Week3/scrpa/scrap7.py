from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

courses = {
    "Title": [],
    "Partner": [],
    "Rating": [],
    "Reviews": [],
    "Skills": [],
    "Duration": [],
    "Link": []
}

driver = webdriver.Chrome()
driver.get("https://www.coursera.org/courses?query=free")
sleep(5)

for i in range(5):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for item in soup.find_all("div", class_="cds-ProductCard-base cds-ProductCard-grid css-1gwppjr"):
        title = item.find("h3", class_="cds-CommonCard-title css-6ecy9b").text
        partner = item.find("div", class_="cds-ProductCard-partners").get_text(strip=True)
        rating = item.find("p", class_="css-2xargn").text
        reviews = item.find("p", class_="css-vac8rf").text if item.find("p", class_="css-vac8rf") else "0 reviews"
        skills = item.find("p", class_="css-vac8rf").get_text(strip=True) if item.find("b", class_="css-l47nsn") else "N/A"
        duration = item.find("p", class_="css-vac8rf").text.split('·')[-1].strip() if "Beginner" in item.get_text() else "N/A"

    try:
        next_button = driver.find_element(By.CLASS_NAME, "rc-PaginationControls nav-button next")
        next_button.click()
        sleep(5)
    except:
        print("No more pages to load.")
        break

driver.quit()

df = pd.DataFrame(courses)
print(df)
df.to_csv("coursera_free_courses.csv", index=False)
