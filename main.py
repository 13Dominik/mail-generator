#!/usr/bin/python
# -*- coding: utf-8 -*-
from fake_data import FakeData
from generate_login_password import GenerateLoginPassword
from Page_servicing import Page_service

def main():
    person = FakeData()
    login_password = GenerateLoginPassword(person.first_name_male(), person.last_name_male())
    page = Page_service(person.first_name_male(), person.last_name_male(), login_password.generate_password(), login_password.generate_login())
    page.fill_all()


if __name__ == '__main__':
    main()