# import faker
from faker import Faker


class FakeData:

    def __init__(self):
        self.fake = Faker('pl-PL')

    def first_name_male(self):
        """
        :return: Polish, male first name without polish chars
        """
        first_name = self.fake.first_name_male()

        flag = True
        while flag:
            for char in first_name:
                if not char.isascii():
                    first_name = self.fake.first_name_male()
                    break
            flag = False
        return first_name

    def last_name_male(self):
        """
        :return: Polish, male surname without polish chars
        """
        last_name = self.fake.last_name_male()

        flag = True
        while flag:
            for char in last_name:
                if not char.isascii():
                    last_name = self.fake.last_name_male()
                    break
            flag = False
        return last_name

    def get_random_toy_from_txt(self) -> str:
        """ Returns random toy from file txt with names of toys """
        with open("random_toys.txt", mode='r') as toys_file:
            list_of_toys = toys_file.readlines()
        return random.choice(list_of_toys)
