from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get(link)


try:
    question = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    answer = Select(browser.find_element_by_tag_name('select'))
    answer.select_by_value(str(question))
    browser.find_element_by_css_selector('button.btn.btn-default').click()
    
finally:
    time.sleep(10)
    browser.quit()

