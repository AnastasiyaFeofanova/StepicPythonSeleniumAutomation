import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

final=''
@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(final)

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links):
    global final
    link = f"{links}/"
    browser.get(link)
    input1 = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#ember67"))
    )
    input1.send_keys(format(math.log(int(time.time()))))
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    welcome_text_elt = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    welcome_text = welcome_text_elt.text
    try:
        assert welcome_text == "Correct!", "{} is not Correct!".format(welcome_text)
    except AssertionError:
        final += welcome_text + " "