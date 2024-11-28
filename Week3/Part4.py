from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#settuing chrome driver
service = Service(executable_path="C:/Users/Arwa Mahwish/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

course_codes = []
title = []
description = []
clos_list = []
book_list = []
instructors = []  
semesters = []    

# Opening the webpage
driver.get("http://eduko.spikotech.com")
time.sleep(5)

course_cards = driver.find_elements(By.XPATH, "//div[@class='card']")

for card in course_cards:
    try:
        # Scraping instructor name and semester
        instructor = card.find_element(By.XPATH, ".//h7[1]").text.strip() 
        semester = card.find_element(By.XPATH, ".//h7[2]").text.strip()  

        # Append instructor and semester to the lists
        instructors.append(instructor)
        semesters.append(semester)

        read_more_link = card.find_element(By.XPATH, ".//a[contains(text(), 'Read More')]")
        read_more_link.click()
        time.sleep(5)
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        # Scraping course code
        course_code = soup.find("div", id="CourseCode").text.strip()

        # Scraping course name
        course_name = soup.find("h5", id="CourseName").text.strip()

        # Scraping description
        course_description = soup.find("p", id="CourseDescription").text.strip()

        # Scraping (CLOs)
        course_clos = soup.find("ul", id="CourseClos").find_all("li")
        course_clos_text = ", ".join([clo.text.strip() for clo in course_clos])

        # Scraping textbooks
        course_books = soup.find("ul", id="CourseBooks").find_all("li")
        course_books_text = ", ".join([book.text.strip() for book in course_books])

        course_codes.append(course_code)          # Append data to lists
        title.append(course_name)
        description.append(course_description)
        clos_list.append(course_clos_text)
        book_list.append(course_books_text)

        driver.back()
        time.sleep(5)
        course_cards = driver.find_elements(By.XPATH, "//div[@class='card']")

    except Exception as e:
        print(f"Error scraping course: {e}")
        driver.back()
        time.sleep(5)
        course_cards = driver.find_elements(By.XPATH, "//div[@class='card']")

df = pd.DataFrame({                     # Creating DataFrame to store data
    "Course Code": course_codes,
    "Course Name": title,
    "Course Description": description,
    "CLOs": clos_list,
    "Books": book_list,
    "Instructor": instructors,
    "Semester": semesters
})

df.to_csv("eduko.csv", index=False, encoding="utf-8")
driver.close()