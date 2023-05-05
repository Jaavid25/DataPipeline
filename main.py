import time
import pandas as pd
from download import downloadAudioFromYTLink
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# start by defining the options
options = webdriver.ChromeOptions()
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)

url = input("course URL: ")
output_dir_path = input("output directory path :")


driver.get(url)
time.sleep(10)
# driver.switch_to.frame("player")
# weeks = driver.find_elements(By.CLASS_NAME,"unit")
# for week,i in zip(weeks,range(0,len(weeks))):
#     week.click()
#     time.sleep(10)
#     print("week"+ str(i + 1))
#     lectures = week.find_elements(By.TAG_NAME,"li")
#     for lecture in lectures:
#         lecture.click()
#         driver.switch_to.frame("player")
#         time.sleep(5)
#         a = driver.find_element(By.CLASS_NAME, "ytp-impression-link")
#         url = a.get_attribute("href")
#         print(url)
#         downloadAudioFromYTLink(url,output_dir_path)
#         driver.switch_to.default_content()

opts = driver.find_element(By.CLASS_NAME,"options")
buttons = opts.find_elements(By.CLASS_NAME,"tab")
for button in buttons:
    print(button.text)
    if button.text == "Downloads":
        button.click()

time.sleep(300)