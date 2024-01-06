import time

import pytest
from selenium.webdriver.common.by import By
from assertions import MainPage
from lib.user_interactions import UserInteractions
from conftest import driver
from locators import MainPageLocators

add_to_cart_buttons = [
    (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[1]'),
    (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[2]'),
    (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[3]'),
    (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[4]'),
    (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[5]'),
    (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[6]')
]


@pytest.mark.adding_items_to_cart
@pytest.mark.parametrize("items_to_add", [
    [MainPageLocators.first_item],
    [MainPageLocators.first_item, MainPageLocators.second_item],
    [MainPageLocators.first_item, MainPageLocators.second_item, MainPageLocators.third_item],
    [MainPageLocators.first_item, MainPageLocators.second_item, MainPageLocators.third_item, MainPageLocators.forth_item],
    [MainPageLocators.first_item, MainPageLocators.second_item, MainPageLocators.third_item, MainPageLocators.forth_item, MainPageLocators.fifth_item],
    [MainPageLocators.first_item, MainPageLocators.second_item, MainPageLocators.third_item, MainPageLocators.forth_item, MainPageLocators.fifth_item, MainPageLocators.sixth_item]
])
def test_adding_items_to_cart(driver, items_to_add):
    """
    Preconditions:
    User is already logged in.
    1.Add item/s to cart
    2.Click on login button
    Expected result: Item is being added to cart
    """

    page = UserInteractions(driver)
    page.login_with_tap_standard_user()

    for item_button in items_to_add:
        print(f"Before clicking on {item_button}")
        page.click(item_button)
        print(f"After clicking on {item_button}: Is visible?")

    adding_items = MainPage(driver)
    expected_counter = str(len(items_to_add))

    assert adding_items.cart_counter == expected_counter, 'Cart counter is not displayed'
