import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
load_dotenv()


usernameStr = os.environ.get("email")
passwordStr = os.environ.get("password")

Subjects = {
    "AA": "label_8_22",
    "AD": "label_8_23",
    "ITC": "label_8_24",
    "PL": "label_8_25",
    "WP-1": "label_8_26",
}
for i in Subjects.keys():
    print(i)
sub = input("Enter subject name from above: ")


browser = webdriver.Chrome(
    executable_path="E:\chromedriver_win32\chromedriver.exe")
browser.get(('https://lms-kjsce.somaiya.edu/login/index.php'))

username = browser.find_element_by_id('username')
username.send_keys(usernameStr)
password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('loginbtn')
signInButton.click()
sleep(5)

# found = False

# content = browser.find_element_by_xpath(
#     "/html/body/div[3]/div[2]/div/div[3]/aside/div/div[2]/ul/li/ul/li[3]/ul/li[1]/p/span")
# print(content)
# while not found:
#     content = browser.find_elements_by_xpath(
#     "/html/body/div[3]/div[2]/div/div[3]/aside/div/div[2]/ul/li/ul/li[3]/ul/li[1]").text


# /html/body/div[3]/div[2]/div/div[3]/aside/div/div[2]/ul/li/ul/li[3]/ul/li[1]/ul/li/p/span
IT = browser.find_element_by_id('label_3_15')
IT.click()
year = browser.find_element_by_id('label_4_16')
year.click()
even = browser.find_element_by_id('label_5_17')
even.click()
college_year = browser.find_element_by_id('label_6_18')
college_year.click()
div_b = browser.find_element_by_id('label_7_21')
div_b.click()
# print(div_b)
# /html/body/header/nav/div/div/div/div/div[1]/div[1]/ul/li/ul/li[10]

SubjectPage = browser.find_element_by_id(Subjects[sub])
SubjectPage.click()

if sub == "AA":
    attendance = browser.find_element_by_xpath(
        "/html/body/div[3]/div[2]/div/div[3]/div/section/div/div/ul/li[3]/div[3]/ul/li/div/div/div[2]/div/a")
    attendance.click()

# elems = browser.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     if "attendance" in elem.text.lower():
#         print(elem.text, elem.get_attribute("href"))

elements = browser.find_elements_by_css_selector("p.tree_item.branch p span")
for element in elements:
    print(element.text)
