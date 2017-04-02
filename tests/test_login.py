from pages.login import LoginPage


class TestLogin():
    def test_login(self, browser, user, password):
        LoginPage(browser).send_user(user)
        LoginPage(browser).send_password(password)
        LoginPage(browser).click_login()
