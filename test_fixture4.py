import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    def fin():
        print("teardown browser")
        browser.quit()    


class TestMainPage1(object):
    def test_guest_should_see_login_link(self, browser):
        return browser
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        request.addfinalizer(fin)

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        return browser
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        request.addfinalizer(fin)