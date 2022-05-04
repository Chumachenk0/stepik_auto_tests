from asyncio import log
from math import log
from math import sin
from cmath import sin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    

    price = WebDriverWait(browser, "13").until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()


    p = browser.find_element(By.ID, 'input_value').text
    b = int(p)
    y = log(abs(12*sin(b)))

    browser.find_element(By.ID, 'answer').send_keys(y)
    
    button = browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep()
    browser.close()













