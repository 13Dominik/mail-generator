#!/usr/bin/python
# -*- coding: utf-8 -*-
# from selenium import webdriver
from time import sleep
import random

from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generate_login_password import GenerateLoginPassword
from fake_data import FakeData


class PageException(Exception):
    """Raised when function didnt work"""

    def __init__(self, function_failed: str):
        self.function_failed = function_failed
        self.message = f"Something wrong with function: self.{self.function_failed}!"
        super().__init__(self.message)


class Page_service:

    def __init__(self, name: str, surname: str, password: str, login: str, toy: str, options: Options) -> None:
        self.name = name
        self.surname = surname
        self.password = password
        self.login = login
        self.toy = toy
        self.options = options  # for user agent

        # proxy
        #  polish proxy:
        proxy1 = {
            'proxy': {
                'http': 'http://tLC67ARs:qieSBY74@45.137.55.17:64012',
                'https': 'http://tLC67ARs:qieSBY74@45.137.55.17:64012',
                'no_proxy': "localhost,127.0.0.1"
            }
        }
        # rotating proxy:
        # proxy2 = {
        #    'proxy': {
        #         'http': 'http://pxu27239-0:hP4LKCLgKQr8kKZ6nliY@x.botproxy.net:8080',
        #         'https': 'http://pxu27239-0:hP4LKCLgKQr8kKZ6nliY@x.botproxy.net:8080',
        #         'no_proxy': "localhost,127.0.0.1"
        #     }
        #  }
        # user agent
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=self.options)

        # with proxy:                                                                      # user agent         # proxy
        #  self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=self.options, seleniumwire_options=proxy1)

        # clean cookie
        self.driver.delete_all_cookies()

    def load_page(self):
        self.driver.get('http://poczta.o2.pl/rejestracja/')

    def fill_name(self):
        """fill name label with randomly generate name"""
        name_located = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[1]/div[1]/div/input""")
        name_located.send_keys(self.name)

    def fill_surname(self):
        """fill surname label with randomly generate surname"""
        surname_located = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[1]/div[2]/div/input """)
        surname_located.send_keys(self.surname)

    def fill_sex(self):
        """click sex label as man"""
        sex_located = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[2]/div/fieldset/div/div[2]/div/label""")
        sex_located.click()

    def fill_login(self):
        """ fill login label with randomly generate login"""
        login_located = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[4]/div/div[1]/div[1]/input """)
        login_located.send_keys(self.login)

    def fill_day(self):
        """fill day label with randomly choosed day"""
        day_located = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[3]/fieldset/div/div[1]/input""")
        day_located.send_keys(str(random.randint(1, 28)))

    def choose_month(self):
        """ choosing randomly month"""
        month_located = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[3]/fieldset/div/div[2]/div/select""")
        values_of_month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        Select(month_located).select_by_value(random.choice(values_of_month))

    def choose_year(self):
        """choosing randomly year"""
        year_located = self.driver.find_element_by_xpath(
            """ /html/body/div[2]/div/div/div[2]/div/div[3]/form/div[3]/fieldset/div/div[3]/div/select""")
        Select(year_located).select_by_value(str(random.randint(1960, 2001)))

    def fill_pasword(self):
        """fill password and repeated password"""
        password_locate = self.driver.find_element_by_xpath(
            """ /html/body/div[2]/div/div/div[2]/div/div[3]/form/div[5]/div/div[1]/div[1]/input""")
        password_repeated_locate = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[5]/div/div[2]/div/input""")
        password_locate.send_keys(self.password)
        password_repeated_locate.send_keys(self.password)

    def fill_question(self):
        """chosing auxiliary question and fill"""
        label_with_question_located = self.driver.find_element_by_xpath(
            """ //*[@id="app"]/div/div/div[2]/div/div[3]/form/div[6]/div/div[3]/div""")
        first_question_located = label_with_question_located.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[6]/div/div[3]/div/div/button[1]""")
        second_question_located = label_with_question_located.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[6]/div/div[3]/div/div/button[2]""")
        if first_question_located.text == "Pytanie pomocnicze":
            first_question_located.click()


        else:
            second_question_located.click()

        selected_question = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[6]/div/div[4]/div/div/select""")
        Select(selected_question).select_by_value('q6')
        question_answered = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[6]/div/div[4]/input""")
        question_answered.send_keys(self.toy)

    def choose_account_type(self):
        """Chosing account type"""
        located_account_type = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[7]/div[1]/fieldset/div[2]/div[1]/div/label""")
        located_account_type.click()

    def fill_requirements(self):
        """confirming requirements"""
        located_requirements = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/div[7]/div[2]/div[1]/label""")
        located_requirements.click()

    def set_account(self):
        """clicking set up a new account"""
        located_set_account = self.driver.find_element_by_xpath(
            """/html/body/div[2]/div/div/div[2]/div/div[3]/form/button""")
        located_set_account.click()

    def fill_all(self) -> bool:
        """ Try to do all on site"""
        functions = [self.load_page, self.fill_name, self.fill_surname, self.fill_sex, self.choose_month,
                     self.choose_month, self.fill_login, self.fill_day, self.choose_year, self.fill_pasword,
                     self.fill_question, self.choose_account_type, self.fill_requirements, self.set_account]
        for function in functions:
            try:
                function()
            except:
                raise PageException(function.__name__)
        return True

    def is_success(self) -> bool:
        """ Check if information about success of creating new account is visible """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_selected((By.xpath, """//*[@id="app"]/div/div/div[2]/div[3]/h1"""))
            )
            return True
        except:
            return False

    def is_blocked(self):
        """ Check if information about blocked creating new accounts is visible """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div/div/div[2]/div/div[3]/div[2]"""))
            )
            return True
        except:
            return False


class SaveData:
    """ Save login and password of new account to txt file"""

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def save_account_data(self) -> None:
        """ Save account login and password to txt file """
        with open('saved_accounts.txt', mode='a') as file_to_save:
            file_to_save.write(f"{self.login}@o2.pl {self.password}\n")
