import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options

APP_PATH = 'C:\\Users\\rokit\\PycharmProjects\\Appium_swag_labs_tests\\apk\\SauceApp.apk'


# APP_PATH = lambda p: os.path.abspath(
# os.path.join(os.path.dirname(__file__), p)
# )

@pytest.fixture(scope="function")
def driver(request):
    desired_caps = dict(
        platformName='Android',
        deviceName='Android',
        app=APP_PATH,
        automationName='UiAutomator2',
        appPackage='com.swaglabsmobileapp',
        appActivity='com.swaglabsmobileapp.MainActivity',
        noReset=True,
        newCommandTimeout=500
    )

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    print('The driver has been set up')
    driver.implicitly_wait(10)
    yield driver
    driver.remove_app('com.swaglabsmobileapp')
    print('The driver has been removed')
    driver.quit()
    print('The driver has been stopped')


@pytest.fixture()
def log_on_failure(request, driver):
    yield
    item = request.node
    if item.rep_call.failed:
        driver_failure = driver
        allure.attach(driver_failure.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)
    return rep
