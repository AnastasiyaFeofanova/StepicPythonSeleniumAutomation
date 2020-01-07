from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    firstName = browser.find_element_by_css_selector("[name='firstname']")
    firstName.send_keys('Nastasiya')
    
    lastName = browser.find_element_by_css_selector("[name='lastname']")
    lastName.send_keys('Pupkina')
   
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys('Pupkina@gmail.com')
    
    myFile = browser.find_element_by_css_selector("[name='file']")
    email.send_keys('Pupkina@gmail.com')
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'myFile.txt')
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.dirname(__file__))
    myFile.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    
    time.sleep(10)
    browser.quit()
    