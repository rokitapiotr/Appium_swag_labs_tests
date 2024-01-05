from conftest import driver
from base_page import BasePage
from locators import *


class MainPage(BasePage):

    def __init__(self, driver: driver):
        super().__init__(driver)

    @property
    def is_header_displayed(self) -> bool:
        return self.is_displayed(MainPageLocators.main_page_header)
