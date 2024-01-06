from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class LoginPageLocators:

    username_input = (AppiumBy.ACCESSIBILITY_ID, 'test-Username')
    password_input = (AppiumBy.ACCESSIBILITY_ID, 'test-Password')
    login_button = (AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN')
    locked_user_window = (By.XPATH, '//android.widget.TextView[@text="Sorry, this user has been locked out."]')
    invalid_user_window = (By.XPATH, '//android.widget.TextView[@text="Username and password do not match any user in this service."]')
    empty_username_window = (By.XPATH, '//android.widget.TextView[@text="Username is required"]')
    empty_password_window = (By.XPATH, '//android.widget.TextView[@text="Password is required"]')


class MainPageLocators:

    main_page_header = (By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]')