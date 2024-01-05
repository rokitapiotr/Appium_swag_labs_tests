import pytest
from assertions import MainPage
from file_utils.data_utils import get_CSV_data_as_dict
from lib.user_interactions import UserInteractions
from conftest import driver

filename = 'valid_login_data.csv'
test_data_username_password = get_CSV_data_as_dict(filename)


@pytest.mark.log_in
@pytest.mark.parametrize("login, password", test_data_username_password)
def test_login_with_valid_credentials(driver, login, password):

    login_page = UserInteractions(driver)
    login_page.login(login, password)
    positive_logging = MainPage(driver)

    assert positive_logging.is_header_displayed, 'Header is not displayed'
