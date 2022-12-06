from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.get_to_login_page()
    LoginPage.should_be_login_url(page)


def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.get_to_login_page()
    LoginPage.should_be_login_form(page)


def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.get_to_login_page()
    LoginPage.should_be_register_form(page)

