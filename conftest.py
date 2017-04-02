import pytest

from selenium import webdriver
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--driver',
                     action='store',
                     default='firefox',
                     help='Desired Browser')

    parser.addoption('--url',
                     action='store',
                     default='http://app.myspd.co.uk/#/login',
                     help='url')

    parser.addoption('--user', action='store', help='user')
    parser.addoption('--password', action='store', help='password')


@pytest.fixture(scope='module', autouse=True)
def browser(request):
    import os
    today = datetime.today()
    path = "logs/{}/{}/{}".format(today.year, today.month, today.day)

    if not os.path.exists(path):
        os.makedirs(path)

    browser = request.config.getoption('--driver')
    if browser == 'firefox':
        browser = webdriver.Firefox(
            executable_path="drivers/geckodriver",
            log_path="{}/geckodriver_{}.log".format(
                path,
                today.time().microsecond
            )
        )
    elif browser == 'chrome':
        browser = webdriver.Chrome(executable_path="drivers/chromedriver")
    elif browser == 'edge':
        browser = webdriver.Edge(executable_path='MicrosoftWebDriver.exe')

    browser.maximize_window()
    browser.implicitly_wait(20)
    browser.get(request.config.getoption('--url'))

    yield browser

    import sys
    if sys.exc_info()[0]:
        browser.save_screenshot('screenshots/fail.png')

    browser.quit()


@pytest.fixture(scope='module')
def user(request):
    return request.config.getoption('--user')


@pytest.fixture(scope='module')
def password(request):
    return request.config.getoption('--password')
