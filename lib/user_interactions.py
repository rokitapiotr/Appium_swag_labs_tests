from lib.base_page import BasePage
from lib.locators import LoginPageLocators
from test_cases.conftest import driver


class UserInteractions(BasePage):

    def __init__(self, driver: driver):
        super().__init__(driver)

    def login(self, login, password):
        self.type(LoginPageLocators.username_input, login)
        self.type(LoginPageLocators.password_input, password)
        self.click(LoginPageLocators.login_button)

