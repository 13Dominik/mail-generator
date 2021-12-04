# import faker
from faker import Faker
import random


class FakeData:

    def __init__(self):
        self.fake = Faker('pl-PL')

    def first_name_male(self) -> str:
        """
        :return: Polish, male first name without polish chars
        """
        first_name = self.fake.first_name_male()

        while not first_name.isascii():
            first_name = self.fake.first_name_male()
        return first_name

    def last_name_male(self) -> str:
        """
        :return: Polish, male surname without polish chars
        """
        last_name = self.fake.last_name_male()

        while not last_name.isascii():
            last_name = self.fake.last_name_male()
        return last_name

    def get_random_toy_from_txt(self) -> str:
        """ Returns random toy from file txt with names of toys """
        with open("random_toys.txt", mode='r') as toys_file:
            list_of_toys = toys_file.readlines()
        return random.choice(list_of_toys)
