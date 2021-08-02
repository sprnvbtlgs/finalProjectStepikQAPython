from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def check_book_name_and_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_BEFORE).text
        title_of_book = self.browser.find_element(*ProductPageLocators.TITLE_OF_BOOK_BEFORE).text
        return book_price, title_of_book

    def find_and_click_buy_button(self):
        add_thing = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        add_thing.click()

    def check_that_book_was_added_by_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_ADDED), "Alert didn't show that book was added"

    def check_that_basket_was_updated(self, book_price, book_title):
        book_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_AFTER).text
        book_title_in_basket = self.browser.find_element(*ProductPageLocators.TITLE_OF_BOOK_AFTER).text
        assert book_price == book_price_in_basket, "Wishes book price added in basket"
        assert book_title == book_title_in_basket, "Book title not found in basket"