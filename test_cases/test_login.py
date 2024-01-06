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
    Expected result: Header is being displayed on main page of application
    """

    login_page = UserInteractions(driver)
    login_page.login(login, password)
    positive_logging = MainPage(driver)

    assert positive_logging.is_header_displayed, 'Header is not displayed'


filename = 'locked_user_data.csv'
test_data_username_password_locked_user = get_CSV_data_as_dict(filename)


@pytest.mark.log_in
@pytest.mark.parametrize("login, password", test_data_username_password_locked_user)
def test_login_with_locked_user_data(driver, login, password):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1.Insert login credentials
    2.Insert password credentials
    3.Click on login button
    Expected result: Window with message "Sorry, this user has been locked out." is being displayed
    """

    login_page = UserInteractions(driver)
    login_page.login(login, password)
    logging_with_locked_user = MainPage(driver)

    assert logging_with_locked_user.locked_user_window_has_been_displayed, 'Header is not displayed'


filename = 'not_existing_user.csv'
test_data_not_existing_user = get_CSV_data_as_dict(filename)


@pytest.mark.log_in
@pytest.mark.parametrize("login, password", test_data_not_existing_user)
def test_login_with_not_existing_user_data(driver, login, password):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1.Insert login credentials
    2.Insert password credentials
    3.Click on login button
    Expected result: Window with message "Username and password do not match any user in this service." is being displayed
    """

    login_page = UserInteractions(driver)
    login_page.login(login, password)
    logging_with_not_existing_user = MainPage(driver)

    assert logging_with_not_existing_user.get_window_header_text == "Username and password do not match any user in this service.", 'Header is not displayed'


filename = 'empty_username_data.csv'
test_data_with_empty_login = get_CSV_data_as_dict(filename)


@pytest.mark.log_in
@pytest.mark.parametrize("login, password", test_data_with_empty_login)
def test_login_with_empty_username_data(driver, login, password):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1.Insert login credentials
    2.Insert password credentials
    3.Click on login button
    Expected result: Window with message "Username is required" is being displayed
    """

    login_page = UserInteractions(driver)
    login_page.login(login, password)
    logging_with_empty_username = MainPage(driver)

    assert logging_with_empty_username.get_window_header_text_empty_login == "Username is required", 'Header is not displayed'


filename = 'empty_password_data.csv'
test_data_with_empty_password = get_CSV_data_as_dict(filename)


@pytest.mark.log_in
@pytest.mark.parametrize("login, password", test_data_with_empty_password)
def test_login_with_empty_password_data(driver, login, password):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1.Insert login credentials
    2.Insert password credentials
    3.Click on login button
    Expected result: Window with message "Password is required" is being displayed
    """

    login_page = UserInteractions(driver)
    login_page.login(login, password)
    logging_with_empty_password = MainPage(driver)

    assert logging_with_empty_password.get_window_header_text_empty_password == "Password is required", 'Header is not displayed'


@pytest.mark.log_in
def test_login_with_valid_credentials_with_tap(driver):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1.Insert user credentials with tap
    2.Click on login button
    Expected result: Header is being displayed on main page of application
    """

    login_page = UserInteractions(driver)
    login_page.login_with_tap_standard_user()
    positive_logging = MainPage(driver)

    assert positive_logging.is_header_displayed, 'Header is not displayed'


@pytest.mark.log_in
def test_login_with_locked_user_data_tap(driver):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1.Insert user credentials with tap
    2.Click on login button
    Expected result: Header is being displayed on main page of application
    """

    login_page = UserInteractions(driver)
    login_page.login_with_tap_locked_user()
    logging_with_locked_user = MainPage(driver)

    assert logging_with_locked_user.locked_user_window_has_been_displayed, 'Header is not displayed'
