from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    _IMPLICIT_TIMEOUT = 0
    _EXPLICIT_TIMEOUT = 30

    def __init__(self, browser, env):
        self.env = env
        self.browser = browser
        self.browser.implicitly_wait(BasePage._IMPLICIT_TIMEOUT)
        self.explicitly_wait = WebDriverWait(browser, BasePage._EXPLICIT_TIMEOUT)

    def find_element(self, locator):
        self.explicitly_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator)),
                                   message=f"'{locator}' element doesn't appear on the page")

    def click(self, locator):
        self.find_element(locator)
        self.browser.find_element_by_xpath(locator).click()

    def fill(self, locator, value):
        self.find_element(locator)
        self.browser.find_element_by_xpath(locator).send_keys(value)

    def goto_url(self, url):
        self.browser.get(url)
