import os
import allure
import pytest
import shutil
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options

APP_PATH = 'C:\\Users\\rokit\\PycharmProjects\\AppiumLinkedIn\\apk\\linkedin.apk'


#APP_PATH = lambda p: os.path.abspath(
    #os.path.join(os.path.dirname(__file__), p)
#)


def remove_app(driver, app_path=APP_PATH):
    try:
        driver.quit()
        shutil.rmtree(app_path, ignore_errors=True)
        print(f"The application at {app_path} has been removed.")
    except Exception as e:
        print(f"Error while removing the application: {e}")


@pytest.fixture(scope="function")
def driver(request):
    desired_caps = dict(
        platformName='Android',
        deviceName='Android',
        app=APP_PATH,
        automationName='UiAutomator2',
        # appPackage='com.linkedin.android',
        # appActivity='com.linkedin.android.infra.navigation.LaunchActivity',
        noReset=True,
        fullreset=True,
        # autoLaunch=True,
        newCommandTimeout=500
    )

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4724', options=capabilities_options)
    driver.implicitly_wait(10)
    yield driver
    print('The driver has been set up')
    # driver.quit()
    remove_app(driver)


@pytest.fixture()
def log_on_failure(request, driver):
    yield
    item = request.node
    if item.rep_call.failed:
        driver_failure = driver
        allure.attach(driver_failure.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
