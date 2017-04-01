#!/home/marvss/Code/SelSuite/ve/bin/python

# -*- coding: utf-8 -*-
from page import home, login 


class TestCodecademy():
    def test_login(self, browser, user, password):
        browser.find_element_by_id('header__sign-in').click()
        browser.find_element_by_name('user[login]') \
               .send_keys(user)

        browser.find_element_by_name('user[password]') \
               .send_keys(password)

        browser.find_element_by_id('user_submit').click()
