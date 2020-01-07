from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_css_selector("button#book")
    button.click()
    
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    
    answerInput = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answerInput)
    answerInput.send_keys(y)
    
    button1 = browser.find_element_by_css_selector("button#solve")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()