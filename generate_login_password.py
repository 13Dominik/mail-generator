#!/usr/bin/python
# -*- coding: utf-8 -*-
import secrets
import string
import random


class GenerateLoginPassword:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def generate_login(self) -> str:
        """ Returns a login from name and surname of user"""
        from_name = self.name[0:random.randint(2, len(self.name))]
        from_surname = self.surname[0:random.randint(2, len(self.surname))]
        return from_name + from_surname + str(random.randint(80, 99))

    def generate_password(self) -> str:
        """ Returns a random password """
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for i in range(10))
