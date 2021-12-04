#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from generate_login_password import GenerateLoginPassword
import random




driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://poczta.o2.pl/rejestracja/')







class Page_service:

    def __init__(self,name : str,surname : str, password :str, login : str) -> None:
        self.name = name
        self.surname = surname
        self.password = password
        self.login = login

    def fill_name(self):
        """fill name label with randomly generate name"""
        name_located = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[1]/div[1]/div/input""")
        name_located.send_keys(self.name)

    def fill_surname(self):
        """fill surname label with randomly generate surname"""
        surname_located = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[1]/div[2]/div/input """)
        surname_located.send_keys(self.surname)

    def fill_sex(self):
        """clik sex label as man"""
        sex_located = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[2]/div/fieldset/div/div[2]/div/label""")
        sex_located.click()

    def fill_login(self):
        """ fill login label with randomly generate login"""
        login_located = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[4]/div/div[1]/div[1]/input """)
        login_located.send_keys(self.login)


    def choose_month(self):
        """ choosing randomly month"""
        month_located = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[3]/fieldset/div/div[2]/div/select""")
        values_of_month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        Select(month_located).select_by_value(random.choice(values_of_month))


password_object = GenerateLoginPassword('Jozef','Dupa')
page = Page_service("Jozef","Dupa",password_object.generate_password(),password_object.generate_login())
page.fill_name()
page.fill_surname()
page.fill_sex()
page.choose_month()
page.fill_login()


sleep(10)

