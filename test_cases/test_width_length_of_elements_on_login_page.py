import pytest
from lib.user_interactions import UserInteractions
from conftest import driver
from locators import LoginPageLocators


@pytest.mark.dimensions
def test_login_input_dimensions(driver):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1. Check dimensions of login input
    """

    login_page = UserInteractions(driver)
    dimensions = login_page.get_dimensions(LoginPageLocators.username_input)

    print(dimensions)

    assert dimensions[0] == 870
    assert dimensions[1] == 128


@pytest.mark.dimensions
def test_password_input_dimensions(driver):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1. Check dimensions of login input
    """

    login_page = UserInteractions(driver)
    dimensions = login_page.get_dimensions(LoginPageLocators.password_input)

    print(dimensions)

    assert dimensions[0] == 870
    assert dimensions[1] == 128


def test_login_button_dimensions(driver):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1. Check dimensions of login input
    """

    login_page = UserInteractions(driver)
    dimensions = login_page.get_dimensions(LoginPageLocators.login_button)

    print(dimensions)

    assert dimensions[0] == 870
    assert dimensions[1] == 132


def test_top_image_dimensions(driver):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1. Check dimensions of login input
    """

    login_page = UserInteractions(driver)
    dimensions = login_page.get_dimensions(LoginPageLocators.top_image_swag_labs)

    print(dimensions)

    assert dimensions[0] == 870
    assert dimensions[1] == 147


def test_bottom_image_dimensions(driver):
    """
    Preconditions:
    The application is enabled on the start page - login page.
    1. Check dimensions of login input
    """

    login_page = UserInteractions(driver)
    dimensions = login_page.get_dimensions(LoginPageLocators.bottom_image)
    print(dimensions)

    assert dimensions[0] == 870
    assert dimensions[1] == 840
