from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    INPUT_EMAIL_IN = (By.XPATH, "//input[@id='id_login-username']")
    INPUT_PASSWORD_IN = (By.XPATH, "//input[@id='id_login-password']")
    SUBMIT_IN = (By.XPATH, "//button[@name='login_submit']")
    INPUT_EMAIL_UP = (By.XPATH, "//input[@id='id_registration-email']")
    INPUT_PASSWORD_UP = (By.XPATH, "//input[@id='id_registration-password1']")
    INPUT_CONFIRM_PASSWORD_UP = (By.XPATH, "//input[@id='id_registration-password2']")
    SUBMIT_UP = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_ADDED = (By.XPATH, "//div[@class='alertinner ']//strong")
    BASKET_UPDATED = (By.XPATH, '//div[3]/div/p[1]/strong')
    PRICE_OF_BOOK_BEFORE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > p.price_color')
    TITLE_OF_BOOK_BEFORE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    PRICE_OF_BOOK_AFTER = (By.XPATH, '//div//p[@class="price_color"]')
    TITLE_OF_BOOK_AFTER = (By.XPATH, '//div[1]/div[1]/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_BUTTON = (By.XPATH, '//span/a')
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    CHECK_THAT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#basket_formset')