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

ihale_durumu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="autoScroll"]/div[4]/select'))).click()
ihale_sozlesme = driver.find_element(By.XPATH, '//*[@id="autoScroll"]/div[4]/select/option[5]')
ihale_sozlesme.click()
time.sleep(2)
filtre = driver.find_element(By.CSS_SELECTOR, '#pnlFiltreBtn .hidden-md-down')
filtre.click()
time.sleep(5)


#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#time.sleep(5)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-outline-info .hide')))
#//*[@id="sonuclar"]/div[102]/div/div/div/div[3]/div/div/ul/li[1]/button
#//*[@id="sonuclar"]/div[154]/div/div/div/div[3]/div/div/ul/li[1]/button


#button_ids = driver.find_elements(By.CSS_SELECTOR, '.btn-outline-info .hide')
for b in range(1,32000):
    button_id = driver.find_element(By.XPATH, f'//*[@id="sonuclar"]/div[{b}]/div/div/div/div[3]/div/div/ul/li[1]/button')
    button_id.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))

        # Process each iframe on the page
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        # Code to extract data from the iframe goes here
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ulTabs"]/li[5]/a')))
        sozlesme_bilgiler = driver.find_element(By.XPATH, '//*[@id="ulTabs"]/li[5]/a')
        sozlesme_bilgiler.click()
        time.sleep(2)
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[2]/p/span[2]')))
        sirket_sozlesme = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]')
        time.sleep(2)
        # sirket_isim = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[1]')
        print(sirket_sozlesme.text)
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sonuclar .close span"))).click()
        #close = driver.find_element(By.CSS_SELECTOR, '#sonuclar .close span')
        #close.click()
        #driver.execute_script('arguments[0].click();', close)
        #time.sleep(2)
        #driver.switch_to.default_content()
        #iframe.parent.execute_script("arguments[0].remove()", iframe)
        time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

# Scroll down to bottom
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")





