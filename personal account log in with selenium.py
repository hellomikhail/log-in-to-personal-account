import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.binary_location = r'PATH\firefox.exe' # path to firefox.exe file

s = Service('PATH\geckodriver.exe') # path to geckodriver.exe file
driver = webdriver.Firefox(service=s, options=options)
driver.get('https://moscow.megafon.ru/')

personal_account = driver.find_element(By.XPATH, "//div[@class='ch-account-controller ch-header__trigger ch-header__trigger_type_lk']//span[@class='ch-trigger__title ch-trigger__title_view_lk'][contains(text(),'Личный кабинет')]")
personal_account.click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'login-tile__title') , # element filtration
        'Вход в Личный кабинет'# the expected text
    )
)
phone_number = driver.find_element(By.CSS_SELECTOR, "input[placeholder='+7 ___ ___-__-__']")
phone_number.send_keys("9241111111")
getcode_button = driver.find_element(By.XPATH, "//div[@class='mfui-button__inner']")
getcode_button.click()