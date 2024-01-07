from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class LoginPageLocators:

    username_input = (AppiumBy.ACCESSIBILITY_ID, 'test-Username')
    password_input = (AppiumBy.ACCESSIBILITY_ID, 'test-Password')
    login_button = (AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN')
    top_image_swag_labs = (By.XPATH, '//android.widget.ScrollView[@content-desc="test-Login"]/android.view.ViewGroup/android.widget.ImageView[1]')
    bottom_image = (By.XPATH, '//android.widget.ScrollView[@content-desc="test-Login"]/android.view.ViewGroup/android.widget.ImageView[2]')
    locked_user_window = (By.XPATH, '//android.widget.TextView[@text="Sorry, this user has been locked out."]')
    invalid_user_window = (By.XPATH, '//android.widget.TextView[@text="Username and password do not match any user in this service."]')
    empty_username_window = (By.XPATH, '//android.widget.TextView[@text="Username is required"]')
    empty_password_window = (By.XPATH, '//android.widget.TextView[@text="Password is required"]')
    standard_user_cords = (375, 2120)
    locked_user_cords = (170, 2165)


class MainPageLocators:

    main_page_header = (By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]')
    expand_button = (By.XPATH, '//android.view.ViewGroup[@content-desc="test-Menu"]/android.view.ViewGroup/android.widget.ImageView')
    logout_button = (By.XPATH, '//android.widget.TextView[@text="LOGOUT"]')
    first_item = (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[1]')
    second_item = (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[2]')
    third_item = (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[3]')
    forth_item = (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[4]')
    fifth_item = (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[5]')
    sixth_item = (By.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[6]')
    cart_counter = (By.XPATH, '//android.widget.TextView[@text="1"]')

