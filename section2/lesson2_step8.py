import os
import time
from selenium import webdriver



try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'catlogo.png')
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные
    # поля. ( Код для необязательных полей закоментирован.)
    name_first = browser.find_element_by_name('firstname')
    name_first.send_keys("Ivan")
    surname = browser.find_element_by_name('lastname')
    surname.send_keys("Petrov")
    email = browser.find_element_by_name('email')
    email.send_keys("Smolensk")
    input_file = browser.find_element_by_css_selector('[type="file"]')
    input_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

    

    
