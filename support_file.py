from appium.options.android import UiAutomator2Options
from appium import webdriver


APP_PATH = 'C:\\Users\\rokit\\PycharmProjects\\AppiumLinkedINTests\\apk\\SauceApp.apk'

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
driver.implicitly_wait(5)
# driver.background_app(5)


print('The driver has been set up')
driver.quit()