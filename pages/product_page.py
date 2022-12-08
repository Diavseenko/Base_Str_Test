from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def product_to_cart(self):
        self.add_product_to_cart()
        self.is_mess_add_to_cart_present()


    def add_product_to_cart(self):
        cart_btn = self.browser.find_element(*ProductPageLocators.CART_BTN)
        cart_btn.click()

    def is_mess_add_to_cart_present(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_CART_NAME), "Check your choice, you have " \
                                                                                        "not a successful message"

    def is_it_that_what_user_add(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_CART_NAME)
        assert product.text == message.text, "check your product that you added in cart"


    def comparing_price_item_and_cart(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_sum = self.browser.find_element(*ProductPageLocators.CART_SUM)
        assert product_price.text in cart_sum.text, "check the price in cart, may be you had wrong"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_CART), "The saccsesful message " \
                                                                                           "did not apeare after " \
                                                                                           "click on add to cart " \
                                                                                           "button "
