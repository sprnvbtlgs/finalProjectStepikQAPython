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
