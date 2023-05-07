import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from drive import Drive
import os
# start by defining the options
options = webdriver.ChromeOptions()
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'

options.add_argument('--headless=new')
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)
url = input("URL: ")
driver.get(url)
time.sleep(15)

options_list = driver.find_element(By.CLASS_NAME,"options")
options_buttons = options_list.find_elements(By.CLASS_NAME,"tab")

for option_button in options_buttons:
    if option_button.text == "Downloads":
        download_button = option_button
        download_button.click()

time.sleep(10)
download_menus = driver.find_elements(By.CSS_SELECTOR,".assignments.download-type")
transcript_menu = None

for download_menu in download_menus:
    if download_menu.find_element(By.TAG_NAME,"h3").text == "Transcripts":
        transcript_menu = download_menu
        break

transcript_menu.click()
transcript_links = list()
chapters = transcript_menu.find_elements(By.CLASS_NAME,"d-data")
a = Drive()
for chapter,i in zip(chapters,range(0,len(chapters))):
    chapter.find_element(By.CLASS_NAME,"c-language").click()
    time.sleep(0.5)
    chapter.find_element(By.TAG_NAME,"li").click()
    time.sleep(0.5)
    url = chapter.find_element(By.TAG_NAME,"a").get_attribute("href")
    file_id = url.split("/")[-2]
    a.download(file_id,"./transcripts/" + "lec" + str(i) + ".pdf")
    transcript_links.append( chapter.find_element(By.TAG_NAME,"a").get_attribute("href") )

print(transcript_links)
time.sleep(300)