from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    url = None

    def __init__(self, browser_name, exceptions=None):
        self.browser = browser_name
        self.wait = WebDriverWait(self.browser,
                                  10,
                                  poll_frequency=1,
                                  ignored_exceptions=exceptions)

    def navigate_to_url(self):
        self.browser.get(self.url)

    def verify_url(self, url):
        assert url == self.browser.current_url

    def send_text_to_field(self, locator, text):
        self.browser.find_element(*locator).send_keys(text)

    def click_element(self, locator):
        self.browser.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.browser.find_element(*locator)
        self.browser.execute_script("return arguments[0].scrollIntoView();",
                                    element)

    def screenshot(self, name):
        self.browser.save_screenshot("screenshots/{}.png".format(name))
