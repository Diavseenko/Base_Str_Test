from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):

    def guest_sees_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESS), "The some product in cart"

    def guest_not_see_product_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_IN_CART), "Page has not product in cart"