import pytest
from assertions import MainPage
from file_utils.data_utils import get_CSV_data_as_dict
from lib.user_interactions import UserInteractions
from conftest import driver

filename = 'valid_login_data.csv'
test_valid_data_username_password = get_CSV_data_as_dict(filename)


@pytest.mark.log_in
@pytest.mark.parametrize("login, password", test_valid_data_username_password)
def test_login_with_valid_credentials(driver, login, password):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1.Insert login credentials
    2.Insert password credentials
    3.Click on login button
    4.Click on expand button on the left top corner
    5.Click on logout button
    Expected result: User should be transferred to the login page
    """

    login_page = UserInteractions(driver)
    login_page.login(login, password)
    login_page.logout()
    positive_logout = MainPage(driver)

    assert positive_logout.is_header_swag_labs_displayed, 'Header is not displayed'
