from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login url isn't correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL_IN), "Email(sing in) not found"
        assert self.is_element_present(*LoginPageLocators.INPUT_PASSWORD_IN), "PASSWORD_IN not found"
        assert self.is_element_present(*LoginPageLocators.SUBMIT_IN), "SUBMIT_IN(sing in) not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL_UP), "INPUT_EMAIL_UP not found"
        assert self.is_element_present(*LoginPageLocators.INPUT_PASSWORD_UP), "INPUT_PASSWORD_UP not found"
        assert self.is_element_present(*LoginPageLocators.INPUT_CONFIRM_PASSWORD_UP), "INPUT_CONFIRM_PASSWORD_UP not found"
        assert self.is_element_present(*LoginPageLocators.SUBMIT_UP), "SUBMIT_UP not found"