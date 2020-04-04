import time
from pages.login_page import LoginPage
from pages.main_page import MainPage, BasePage
from pages.locators import BasePageLocators

link = "http://selenium1py.pythonanywhere.com/"
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()      # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) #инициализируем страницу сразу в тесте
    #login_page = page.go_to_login_page() #если инициализируем страницу в main_page
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_should_be_login_link(browser):
    page = BasePage(browser, link)
    page.open()
    assert page.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"