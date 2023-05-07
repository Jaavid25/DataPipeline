import time
import os
from download_from_yt import download_audio_from_yt_link
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# start by defining the options
options = webdriver.ChromeOptions()
options.page_load_strategy = 'none'
#run chrome in headless mode
options.add_argument("--headless=new")
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)

url = input("course URL: ")
output_dir_path = input("output directory path :")

#check if there's a directory else create one
if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)
        
#load the page
driver.get(url)
# wait for site to be loaded completely
time.sleep(10)

# find unit elements, each unit represents a week
weeks = driver.find_elements(By.CLASS_NAME,"unit")

# iterate over each week to download videos
for week,i in zip(weeks,range(0,len(weeks))):
    week.click()
    time.sleep(5)
    print("week"+ str(i + 1))
    #find all lectures in the week
    lectures = week.find_elements(By.TAG_NAME,"li")
    #iterate over each lecture and download
    for lecture in lectures:
        lecture.click()
        driver.switch_to.frame("player")
        time.sleep(1)
        a = driver.find_element(By.CLASS_NAME, "ytp-impression-link")
        url = a.get_attribute("href")
        print(url)
        download_audio_from_yt_link(url,output_dir_path)
        driver.switch_to.default_content()