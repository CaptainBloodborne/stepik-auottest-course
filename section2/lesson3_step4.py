import time
import pyperclip
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_tag_name('button').click()
    confirm1 = browser.switch_to.alert
    confirm1.accept()
    time.sleep(1)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)
    
    button2 = browser.find_element_by_tag_name("button")
    button2.click()

    confirm2 = browser.switch_to.alert
    pyperclip.copy(confirm2.text.split(' ')[-1])
    confirm2.accept

finally:
    time.sleep(1)
    browser.quit()
    
