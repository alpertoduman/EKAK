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

### filtreleme sözleşme imzalanmış

ihale_durumu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="autoScroll"]/div[4]/select'))).click()
ihale_sozlesme = driver.find_element(By.XPATH, '//*[@id="autoScroll"]/div[4]/select/option[5]')
ihale_sozlesme.click()

time.sleep(5)

ihale_pazarlik = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="autoScroll"]/div[10]/select'))).click()
ihale_pazarlik_durumu = driver.find_element(By.XPATH, '//*[@id="autoScroll"]/div[10]/select/option[2]')
ihale_pazarlik_durumu.click()


time.sleep(5)

filtre = driver.find_element(By.CSS_SELECTOR, '#pnlFiltreBtn .hidden-md-down')
filtre.click()
time.sleep(10)

bilgiler_button = driver.find_element(By.CSS_SELECTOR, '.col-sm-12:nth-child(1) .btn-outline-info .hide')
bilgiler_button.click()

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="sonuclar"]/div[1]/div/div[2]/iframe'))
#driver.switch_to.frame(driver.find_elements(By.CSS_SELECTOR, 'iframe')[1])
time.sleep(2)
#buyer = driver.find_element(By.CSS_SELECTOR, '.text-uppercase')
#time.sleep(2)
#print(buyer.text)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ulTabs"]/li[4]/a')))
sozlesme_bilgiler = driver.find_element(By.XPATH, '//*[@id="ulTabs"]/li[4]/a')
sozlesme_bilgiler.click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[2]/p/span[2]')))
sirket_sozlesme = driver.find_element(By.XPATH,'//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[2]/p/span[2]')
print(sirket_sozlesme.text)

time.sleep(2)
sirket_isim = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[1]')
print(sirket_isim.text)

time.sleep(2)
#close = driver.find_element(By.XPATH, '//*[@id="sonuclar"]/div[2]/div/div[2]/button/span')
#close.click()

driver.switch_to.default_content()

bilgiler_button2 = driver.find_element(By.CSS_SELECTOR, '.col-sm-12:nth-child(2) .btn-outline-info .hide')
bilgiler_button2.click()

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="sonuclar"]/div[2]/div/div[2]/iframe'))
#driver.switch_to.frame(driver.find_elements(By.CSS_SELECTOR, 'iframe')[1])
time.sleep(2)
#buyer = driver.find_element(By.CSS_SELECTOR, '.text-uppercase')
#time.sleep(2)
#print(buyer.text)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ulTabs"]/li[4]/a')))
sozlesme_bilgiler = driver.find_element(By.XPATH, '//*[@id="ulTabs"]/li[4]/a')
sozlesme_bilgiler.click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[2]/p/span[2]')))
sirket_sozlesme = driver.find_element(By.XPATH,'//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[2]/p/span[2]')
print(sirket_sozlesme.text)

time.sleep(2)
sirket_isim = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[1]')
print(sirket_isim.text)
time.sleep(1)

driver.switch_to.default_content()





#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


#d = driver.find_element(By.CSS_SELECTOR, '.col-sm-12:nth-child(2) .btn-outline-info')
#d.click()
#time.sleep(2)
#d2 = driver.find_element(By.CSS_SELECTOR, '.col-sm-12:nth-child(3) .btn-outline-info')
#d2.click()



time.sleep(2)