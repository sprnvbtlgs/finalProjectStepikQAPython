from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def open_basket_page(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_not_be_goods_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), "Message not found"
        assert self.is_not_element_present(*BasketPageLocators.CHECK_THAT_BASKET_IS_EMPTY), "Something be in basket"
