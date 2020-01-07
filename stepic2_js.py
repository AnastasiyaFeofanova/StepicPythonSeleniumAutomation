from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    answerInput = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answerInput)
    answerInput.send_keys(y)
   
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    
    time.sleep(10)
    browser.quit()
    