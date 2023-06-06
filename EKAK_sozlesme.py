from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://ekap.kik.gov.tr/EKAP/Ortak/IhaleArama/index.html")
driver.maximize_window()
time.sleep(2)



ihale_ilan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="autoScroll"]/div[4]/select'))).click()
ihale_ilan_yayin = driver.find_element(By.XPATH, '//*[@id="autoScroll"]/div[4]/select/option[7]')
ihale_ilan_yayin.click()



filtre = driver.find_element(By.CSS_SELECTOR, '#pnlFiltreBtn .hidden-md-down')
filtre.click()
time.sleep(5)

buyer_info = []
seller_info = []
status_info = []
title_info = []
contract_price = []
expected_cost = []
highest_bid = []
lowest_bid = []
contract_date = []
df = pd.DataFrame()

#button_ids = driver.find_elements(By.CSS_SELECTOR, '.btn-outline-info .hide')
for b in range(1,1000):
    time.sleep(1)
    card = driver.find_element(By.XPATH, f'//*[@id="sonuclar"]/div[{b}]/div/div/div')
    #card_list.append(card.text[0])
    #print(card.text)

    buyer = driver.find_element(By.CSS_SELECTOR, '.col-sm-12:nth-child(1) .text-uppercase')
    buyer_t = buyer.text
    status = driver.find_element(By.XPATH, '//*[@id="sonuclar"]/div[2]/div/div/div/div[1]/div/div/div[2]/div')
    status_t = status.text
    title = driver.find_element(By.CSS_SELECTOR , '.ihaleAdi')
    title_t = title.text
    title_info.append(title_t)
    buyer_info.append(buyer_t)
    status_info.append(status_t)

    time.sleep(1)
    button_id = driver.find_element(By.XPATH, f'//*[@id="sonuclar"]/div[{b}]/div/div/div/div[3]/div/div/ul/li[1]/button')
    button_id.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))


    # Process each iframe on the page
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        # Code to extract data from the iframe goes here

        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ulTabs"]/li[5]/a/span[2]')))
            sozlesme_bilgiler = driver.find_element(By.XPATH, '//*[@id="ulTabs"]/li[5]/a/span[2]')
            sozlesme_bilgiler.click()
            time.sleep(1)
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[2]/p/span[2]')))
            sirket_sozlesme = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]')

            seller = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[1]')
            seller_t = seller.text
            contract = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[2]/p/span[2]')
            contract_t = contract.text
            cost = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[3]/p/span[2]')
            cost_t = cost.text
            hbid = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[5]/p/span[2]')
            hbid_t = hbid.text
            lbid = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[6]/p/span[2]')
            lbid_t = lbid.text
            cdate = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[2]/div/div[4]/p/span[2]')
            cdate_t = cdate.text

            seller_info.append(seller_t)
            contract_price.append(contract_t)
            expected_cost.append(cost_t)
            highest_bid.append(hbid_t)
            lowest_bid.append(lbid_t)
            contract_date.append(cdate_t)

        # sirket_isim = driver.find_element(By.XPATH, '//*[@id="ucBirBakistaIhale_sozlesmeUpdate"]/div[1]/div/div[1]')
            #soz_list.append(sirket_sozlesme.text[0])
            #print(sirket_sozlesme.text)




        except:
            pass
        driver.switch_to.default_content()
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sonuclar .close span"))).click()
        # close = driver.find_element(By.CSS_SELECTOR, '#sonuclar .close span')
        # close.click()
        # driver.execute_script('arguments[0].click();', close)
        # time.sleep(2)
        # driver.switch_to.default_content()
        # iframe.parent.execute_script("arguments[0].remove()", iframe)



df['seller'] = seller_info
df['buyer'] = buyer_info
df['status'] = seller_info
df['title'] = title_info
df['price'] = contract_price
df['cost'] = expected_cost
df['highes_bid'] = highest_bid
df['lowest_bit'] = lowest_bid
df['date_signed'] = contract_date
print(df)
df.to_csv('ilanyayinlanmis.csv')




#data = {
#        'Kart_Bilgisi': card_list,
#        'Sozlesme_Bilgisi': soz_list
#       }
#df = pd.DataFrame.from_dict(data)

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#df.to_csv('Ekak_ilan_yayin.csv' , index = 0)


