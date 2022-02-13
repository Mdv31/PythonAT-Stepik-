from .base_page import BasePage
from .locators import LoginPageLocators, FixturePageLocators
import pytest
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "There's not the substring"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except():
            assert self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM), "There's not login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        except():
            assert self.browser.is_element_present(*LoginPageLocators.REGISTER_FORM), "There's not register form"

    def should_be_user_login_message(self):
        try:
            self.browser.is_element_present(*LoginPageLocators.USER_LOGIN)
        except():
            assert self.browser.is_element_present(*LoginPageLocators.USER_LOGIN), "User isn't login the system."

    def should_not_be_error_message(self):
        try:
            self.browser.is_not_element_present(*LoginPageLocators.ERROR_MESSAGE)
        except():
            assert self.browser.is_not_element_present(*LoginPageLocators.ERROR_MESSAGE), "There is some error message."

    def register_new_user(self, email, password):
        self.browser.find_element(*FixturePageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*FixturePageLocators.PASSWORD1).send_keys(password)
        self.browser.find_element(*FixturePageLocators.PASSWORD2).send_keys(password)
        self.browser.find_element(*FixturePageLocators.BUTTON).click()
        time.sleep(5)
