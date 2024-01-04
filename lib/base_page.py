from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def type(self, locator: tuple, text: str, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).send_keys(text)

    def clear(self, locator: tuple, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).clear()

    def click(self, locator: tuple, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).click()

    def wait_until_element_is_visible(self, locator: tuple, time: int = 25):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def wait_until_element_is_clickable(self, locator: tuple, time: int = 25):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def select_by_value(self, locator: tuple, value: str, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        select = Select(self.find(locator))
        select.select_by_value(value)

    def select_div_by_value(self, locator: tuple, option_value: str, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        select_element = Select(self.find(locator))
        select_element.select_by_value(option_value)

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def open_url(self, url: str):
        self.driver.get(url)

    def get_text(self, locator: tuple, time: int = 25) -> str:
        self.wait_until_element_is_visible(locator, time)
        return self.find(locator).text

    def scroll_to_element(self, locator: tuple, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switch_to_window_by_index(self, index: int = 1, time: int = 25):
        wait = WebDriverWait(self.driver, time)
        wait.until(lambda driver: len(self.driver.window_handles) > index)

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    @staticmethod
    def scroll_to_text_by_android_UI_automator(self, text):
        self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance("
                                                        "0)).scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))").click()

    @staticmethod
    def swipe_up(self, swipes):
        for _ in range(1, swipes + 1):
            self.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipe_down(self, swipes):
        for _ in range(1, swipes + 1):
            self.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipe_left(self, swipes):
        for _ in range(1, swipes + 1):
            self.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipe_right(self, swipes):
        for _ in range(1, swipes + 1):
            self.swipe(200, 600, 900, 600, 1000)
