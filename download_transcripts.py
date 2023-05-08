import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from drive import Drive
import os

def scroll(window,distance,driver):
    scroll = 0
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[1];',
                                window,distance)
    # add appropriate wait here, of course. 1-2 seconds each
    time.sleep(2)

# start by defining the options
options = webdriver.ChromeOptions()
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'
# Has issues with Ubuntu
# options.add_argument('--headless=new')
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)
url = input("URL: ")
output_dir_path = input("output directory path :")

#check if there's a directory else create one
if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)

#load page from url
driver.get(url)
#wait for page to load fully
time.sleep(15)

#find options list and   buttons inside the list
options_list = driver.find_element(By.CLASS_NAME,"options")
options_buttons = options_list.find_elements(By.CLASS_NAME,"tab")

#search for download  button in options
for option_button in options_buttons:
    if option_button.text == "Downloads":
        download_button = option_button
        download_button.click()
        break

#wait for js processing
time.sleep(10)

# find available download menus
download_menus = driver.find_elements(By.CSS_SELECTOR,".assignments.download-type")
transcript_menu = None

#search for transcript menu
for download_menu in download_menus:
    if download_menu.find_element(By.TAG_NAME,"h3").text == "Transcripts":
        transcript_menu = download_menu
        break

scroll_w = transcript_menu.find_element(By.CLASS_NAME,"data")
#click transcript menu
transcript_menu.click()
# find chapters  inside transcript menu
chapters = transcript_menu.find_elements(By.CLASS_NAME,"d-data")
# drive object to download transcript
a = Drive()
print("downloading transcripts, this may take several minutes depending on your internet connection, please wait patiently...")
scroll(scroll_w, 43.5,driver)
#iterate over each chapter, click select language and select english and find the link
for chapter,i in zip(chapters,range(0,len(chapters))):
    chapter.find_element(By.CLASS_NAME,"c-language").click()
    time.sleep(0.5)
    chapter.find_element(By.TAG_NAME,"li").click()
    time.sleep(0.5)
    url = chapter.find_element(By.TAG_NAME,"a").get_attribute("href")
    file_id = url.split("/")[-2]
    scroll(scroll_w, 69,driver)
    #download drive file from link
    print("downloading transcript pdf for lec" + str(i + 1) + "...")
    a.download(file_id,(output_dir_path + "/" + "lec" + "{:03d}" + ".pdf").format(i+1))