from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://ekap.kik.gov.tr/EKAP/Ortak/IhaleArama/index.html")
driver.maximize_window()
time.sleep(2)

# Get scroll height after first time page load
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page / use a better technique like `waitforpageload` etc., if possible
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    last_height = new_height

time.sleep(10)

while True:
    # it will be returning false until the element is located
    # "#message" id = "No more results" at the bottom of the YouTube search
    end_result = driver.find_element_by_css_selector('#message').is_displayed()
    driver.execute_script(
        "var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")

    # further code below

    # once the element is found it returns True. If so, it will break out of the while loop
    if end_result == True:
        break