from conftest import driver
from base_page import BasePage
from locators import *


class MainPage(BasePage):

    def __init__(self, driver: driver):
        super().__init__(driver)

    @property
    def is_header_displayed(self) -> bool:
        return self.is_displayed(MainPageLocators.main_page_header)

    @property
    def locked_user_window_has_been_displayed(self) -> bool:
        return self.is_displayed(LoginPageLocators.locked_user_window)

    @property
    def get_window_header_text(self) -> str:
        return self.get_text(LoginPageLocators.invalid_user_window)

    @property
    def get_window_header_text_empty_login(self) -> str:
        return self.get_text(LoginPageLocators.empty_username_window)

    @property
    def get_window_header_text_empty_password(self) -> str:
        return self.get_text(LoginPageLocators.empty_password_window)
