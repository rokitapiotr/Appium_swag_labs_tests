from test_cases.conftest import driver
from base_page import BasePage
from locators import *


class Assertions(BasePage):

    def __init__(self, driver: driver):
        super().__init__(driver)

    @property
    def search_bar_is_displayed(self) -> bool:
        return self.is_displayed(MainPageLocators.search_bar)

    @property
    def sign_out_header_is_displayed(self) -> bool:
        return self.is_displayed(SignOutLocators.sign_out_header)

