from pages.base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self): #correct url
        login_link = self.browser.current_url()
        assert login_link.find("login"), "did not find"


    def should_be_login_form(self):#login form existing
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The login form is not present"


    def should_be_register_form(self):#register form existing
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The register form is not present"
