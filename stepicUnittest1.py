import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    def input_col():
        input1 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Ivan")
        input3 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
        input3.send_keys("Ivan")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
    def test_test1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        TestAbs.input_col()
        self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!")
        browser.quit
    def test_test2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        TestAbs.input_col()
        self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!")
        browser.quit

if __name__ == "__main__":
    unittest.main()