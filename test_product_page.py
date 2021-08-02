from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.check_book_name_and_price()
    page.find_and_click_buy_button()
    page.solve_quiz_and_get_code()
    page.check_that_book_was_added_by_name()
    page.check_that_basket_was_updated(book_price=page.check_book_name_and_price()[0],
                                       book_title=page.check_book_name_and_price()[1])
