from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)
    check_elem = browser.find_element_by_id("robotCheckbox")
    check_elem.click()
    radio_elem = browser.find_element_by_id("robotsRule")
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radio_elem.click()
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()
