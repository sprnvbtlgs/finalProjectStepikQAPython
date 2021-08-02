from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def find_and_click_buy_button(self):
        add_thing = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        add_thing.click()

    def check_that_book_was_added_by_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_ADDED), "Alert didn't show that book was added"

    def check_that_basket_was_updated(self):
        baskett = self.browser.find_element(*ProductPageLocators.BASKET_UPDATED).text
        print(baskett)
        assert '£9.99' in baskett, "Basket wasn't updated. The book not in basket"
