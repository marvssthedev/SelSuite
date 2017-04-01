
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self):



def get_selector(selector, element):
    # Prefered selector order
    if selector == "ID":
        locator = (By.ID, element)
    elif selector == "NAME":
        locator = (By.NAME, element)
    elif selector == "CSS":
        locator = (By.CSS_SELECTOR, element)
    elif selector == "CLASS":
        locator = (By.CLASS_NAME, element)
    elif selector == "LINK":
        locator = (By.LINK_TEXT, element)
    elif selector == "PARTIAL_LINK":
        locator = (By.PARTIAL_LINK_TEXT, element)
    elif selector == "TAG":
        locator = (By.TAG_NAME, element)
    elif selector == "XPATH":
        locator = (By.XPATH, element)

    return locator


def navigate_to_url(driver, url):
    driver.get(url)


def verify_url(driver, url):
    assert url == driver.current_url


def send_text_to_field(driver, selector, element, text, time, poll=None, exceptions=None):
    driver.find_element(*get_selector(selector, element)).send_keys(text)
    driver.find_element(selector, element).send_keys(text)

   wait = WebDriverWait(driver, time, poll_frequency=poll, ignored_exceptions=exceptions)

    wait.until(
        EC.text_to_be_present_in_element(get_selector(selector, element), text)
    )


def click_element(driver, selector, element, time, poll=None, exceptions=None):
    wait = WebDriverWait(driver,
                         time,
                         poll_frequency=poll,
                         ignored_exceptions=exceptions)

    wait.until(
        EC.element_to_be_selected(get_selector(selector, element))
    )

    driver.find_element(*get_selector(selector, element)).click()
