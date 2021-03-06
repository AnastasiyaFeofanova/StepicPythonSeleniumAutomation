from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    input2.send_keys("Ivan")
    
    input3 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
    input3.send_keys("Ivan")

    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    
    time.sleep(1)
    browser.quit()