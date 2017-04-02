from base import BasePage

from selenium.webdriver.common.by import By

email_field = (By.NAME, 'email')
password_field = (By.NAME, 'password')
login_btn = (By.CSS_SELECTOR, '.login')


class LoginPage(BasePage):
    url = "http://localhost:8000/#/login"

    def send_user(self, user_name):
        self.send_text_to_field(email_field, user_name)

    def send_password(self, user_password):
        self.send_text_to_field(password_field, user_password)

    def click_login(self):
        self.click_element(login_btn)

    def screenshot(self):
        pass
