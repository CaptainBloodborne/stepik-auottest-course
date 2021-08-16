from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)
    check_elem = browser.find_element_by_css_selector("[for='robotCheckbox']")
    check_elem.click()
    radio_elem = browser.find_element_by_css_selector("[for='robotsRule']")
    radio_elem.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
    
