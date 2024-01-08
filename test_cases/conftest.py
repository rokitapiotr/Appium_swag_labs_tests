import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APP_PATH = 'C:\\Users\\rokit\\PycharmProjects\\Appium_swag_labs_tests\\apk\\SauceApp.apk'


@pytest.fixture(scope="function")
def driver(request):

    desired_caps = dict(
        platformName='Android',
        deviceName='Android',
        app=APP_PATH,
        automationName='UiAutomator2',
        # appPackage='com.swaglabsmobileapp',
        # appActivity='com.swaglabsmobileapp.MainActivity',
        noReset=True,
        fullReset=False,
        newCommandTimeout=500
    )

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    print('The driver has been set up')

    driver.implicitly_wait(10)
    yield driver

    driver.remove_app('com.swaglabsmobileapp')
    print('The app has been removed')

    driver.quit()
    print('The driver has been stopped')

