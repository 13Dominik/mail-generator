#!/usr/bin/python
# -*- coding: utf-8 -*-
from fake_data import FakeData
from generate_login_password import GenerateLoginPassword
from Page_servicing import Page_service
from time import sleep

def main():
    person = FakeData()

    name = person.first_name_male()
    surname = person.last_name_male()
    login_password = GenerateLoginPassword(name, surname)
    page = Page_service(name, surname, login_password.generate_password(), login_password.generate_login(),person.get_random_toy_from_txt())
    page.fill_all()
    sleep(20)


if __name__ == '__main__':
    main()