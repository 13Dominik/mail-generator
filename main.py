#!/usr/bin/python
# -*- coding: utf-8 -*-
from fake_data import FakeData
from generate_login_password import GenerateLoginPassword
from Page_servicing import Page_service, SaveData
from selenium.webdriver.chrome.options import Options
from time import sleep
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
# from tbselenium import
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from seleniumwire import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


def main():
    while True:
        person = FakeData()
        # peron data
        name = person.first_name_male()
        surname = person.last_name_male()
        # login Password
        labels = GenerateLoginPassword(name, surname)
        password = labels.generate_password()
        login = labels.generate_login()

        sleep(3)

        options = Options()
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')

        # different way to set up a proxy with useragent
        # PROXY = "89.171.144.168:5678"
        # options.add_argument("--proxy-server=%s" % PROXY)

        page = Page_service(name, surname, password, login, person.get_random_toy_from_txt(), options)

        page.fill_all()

        sleep(5)

        if page.is_success():  # if account did successful
            save = SaveData(login, password)
            save.save_account_data()
            sleep(4)
            print(page.is_success())


if __name__ == '__main__':
    main()
