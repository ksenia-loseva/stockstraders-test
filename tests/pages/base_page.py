from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def find(self, locator):
        return self._driver.find_element(*locator)

    def wait_for_element(self, condition, timeout=5):
        return WebDriverWait(self._driver, timeout).until(condition)