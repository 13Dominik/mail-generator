#!/usr/bin/python
# -*- coding: utf-8 -*-
from fake_data import FakeData
from generate_login_password import GenerateLoginPassword
from Page_servicing import Page_service, SaveData
from time import sleep

def main():
    person = FakeData()

    name = person.first_name_male()
    surname = person.last_name_male()
    login_password = GenerateLoginPassword(name, surname)
    password = login_password.generate_password()
    login = login_password.generate_login()
    page = Page_service(name, surname, password, login ,person.get_random_toy_from_txt())
    if page.fill_all():
        save = SaveData(login, password)
        save.save_account_data()
        sleep(4)
        print(page.is_success())
    sleep(2000)


if __name__ == '__main__':
    main()