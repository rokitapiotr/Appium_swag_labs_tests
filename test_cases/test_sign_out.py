import pytest
from lib.assertions import Assertions
from lib.base_page import BasePage
from lib.locators import *
from test_cases.conftest import driver


#email = 'testmailpiotrrokita@gmail.com'
#password = 'ChrisReiko123!'


@pytest.mark.login_in
def test_login_with_valid_credentials(driver, email='testmailpiotrrokita@gmail.com', password='rusin1337!'):

    login_page = BasePage(driver)
    login_page.click(LoginPageLocators.sign_in_button)
    login_page.type(LoginPageLocators.email_input, email)
    login_page.type(LoginPageLocators.password_input, password)
    login_page.click(LoginPageLocators.continue_button)
    login_page.click(LoginPageLocators.skip_button)
    login_page.click(MainPageLocators.my_profile_button)
    login_page.click(ViewProfileLocators.sign_out_button)
    login_page.click(ViewProfileLocators.sign_out_button2)

    positive_logging = Assertions(driver)

    assert positive_logging.sign_out_header_is_displayed, "Actual header is not displayed"