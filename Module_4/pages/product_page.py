from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_button_to_add_to_basket(self):
        try:
            button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
            button.click()
        except():
            assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "There's not the button"

    def should_see_product_page(self):
        current_url = self.browser.current_url
        substring = "promo=newYear"
        assert substring in current_url, "Guest is on wrong page."

    def should_see_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert price.text == basket_price.text, "There's wrong price or there's not price at all."

    def should_see_message_product_is_added(self):
        first_element = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT)
        second_element = self.browser.find_element(*ProductPageLocators.PRODUCT)
        assert first_element.text == second_element.text, "There's wrong product or there's not product at all."

    def should_not_be_success_message_on_product_page(self):
        self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented"

    def should_message_disappeared(self):
        self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message isn't disappeared."