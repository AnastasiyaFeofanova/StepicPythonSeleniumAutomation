from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_el = browser.find_element_by_id("input_value")
    x = int(x_el.text)
    y = calc(x)
    answerInp = browser.find_element_by_id("answer")
    answerInp.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    
    time.sleep(10)
    browser.quit()
    