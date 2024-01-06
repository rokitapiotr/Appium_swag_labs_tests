from lib.base_page import BasePage
from lib.locators import LoginPageLocators, MainPageLocators
from conftest import driver


class UserInteractions(BasePage):

    def __init__(self, driver: driver):
        super().__init__(driver)

    def login(self, login, password):
        self.type(LoginPageLocators.username_input, login)
        self.type(LoginPageLocators.password_input, password)
        self.click(LoginPageLocators.login_button)

    def login_with_tap_standard_user(self):
        self.tap(LoginPageLocators.standard_user_cords)
        self.click(LoginPageLocators.login_button)

    def login_with_tap_locked_user(self):
        self.tap(LoginPageLocators.locked_user_cords)
        self.click(LoginPageLocators.login_button)

    def logout(self):
        self.click(MainPageLocators.expand_button)
        self.click(MainPageLocators.logout_button)
