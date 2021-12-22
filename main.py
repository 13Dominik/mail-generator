#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep

import settings
from fake_data import FakeData
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from selenium.webdriver.support.select import Select
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager

from generate_login_password import GenerateLoginPassword
from Page_servicing import Page_service, SaveData


def main() -> int:
    number_new_accounts = 0

    while True:
        person = FakeData()
        # peron data
        name = person.first_name_male()
        surname = person.last_name_male()
        # login Password
        labels = GenerateLoginPassword(name, surname)
        password = labels.generate_password()
        login = labels.generate_login()

        save_data = SaveData(login, password)

        options = Options()  # setting headers / user agent
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')

        # different way to set up .env proxy with useragent
        # PROXY = "89.171.144.168:5678" # random proxy
        # options.add_argument("--proxy-server=%s" % PROXY)

        turn_proxy = settings.is_proxy()  # True if file .env exist or False if not
        # turn_proxy = False -> alternative version

        page = Page_service(name, surname, password, login, person.get_random_toy_from_txt(), options,
                            turn_proxy)

        if page.fill_all():  # check if did all
            if page.is_blocked():  # check if creating new accounts is blocked if so end program
                return number_new_accounts
            if page.is_success():  # check if new account is created
                number_new_accounts += 1
                save_data.save_account_data()
            else:
                raise Exception("New account not blocked and not created new account!")


if __name__ == '__main__':
    new_accounts = main()
    print(f"New accounts: {new_accounts}")
