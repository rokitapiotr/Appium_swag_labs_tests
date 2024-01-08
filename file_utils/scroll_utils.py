

class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text,driver):
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))").click()

    @staticmethod
    def swipe_up(swipes, driver):
        for _ in range(1, swipes+1):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipe_down(swipes, driver):
        for _ in range(1, swipes + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipe_left(swipes, driver):
        for _ in range(1, swipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipe_right(swipes, driver):
        for _ in range(1, swipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)