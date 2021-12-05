#!/usr/bin/python
# -*- coding: utf-8 -*-
from fake_data import FakeData
from generate_login_password import GenerateLoginPassword
from Page_servicing import Page_service, SaveData
from time import sleep

def main():
    person = FakeData()
    # peron data
    name = person.first_name_male()
    surname = person.last_name_male()
    # login Password
    labels = GenerateLoginPassword(name, surname)
    password = labels.generate_password()
    login = labels.generate_login()
    # page obj
    page = Page_service(name, surname, password, login ,person.get_random_toy_from_txt())
    page.fill_all()

    sleep(5)

    if page.is_success(): # if account did successful
        save = SaveData(login, password)
        save.save_account_data()
        sleep(4)
        print(page.is_success())
    sleep(2000)


if __name__ == '__main__':
    main()