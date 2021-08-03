from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import faker


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
        assert self.is_element_present(*LoginPageLocators.INPUT_CONFIRM_PASSWORD_UP), "INPUT_CONFIRM_PASSWORD_UP not " \
                                                                                      "found "
        assert self.is_element_present(*LoginPageLocators.SUBMIT_UP), "SUBMIT_UP not found"

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        password = f.password()

        email_field = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_UP)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_UP)
        password_field.send_keys(password)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.INPUT_CONFIRM_PASSWORD_UP)
        password_confirm_field.send_keys(password)
        confirm_button = self.browser.find_element(*LoginPageLocators.SUBMIT_UP).click()


    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert 'login' in self.browser.current_url, "Link is invalid"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

