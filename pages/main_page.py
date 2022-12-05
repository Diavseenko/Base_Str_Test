from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    def get_to_login_page(self):
        login_page = self.browser.find_element(*MainPageLocators.LOGIN)
        login_page.click()
