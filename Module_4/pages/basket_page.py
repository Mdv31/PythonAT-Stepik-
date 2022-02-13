from Module_4.pages.base_page import BasePage
from Module_4.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "In the basket there's something."

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "There's not text 'Your basket is empty'."
