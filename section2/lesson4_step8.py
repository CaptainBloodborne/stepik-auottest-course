import time
import pyperclip
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    
    if button1:
        book_button = browser.find_element_by_id('book')
        book_button.click()
      
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

    confirm2 = browser.switch_to.alert
    pyperclip.copy(confirm2.text.split(' ')[-1])
    print('check')
    confirm2.accept()
    print('check2')

finally:
    time.sleep(5)
    browser.quit()
    
