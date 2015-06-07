"""
car_generator module
contains CarGenerator class
"""
from os.path import dirname, abspath, join
from random import shuffle
from objects import car

class CarGenerator(object):
    """
    CarGenerator module
    generator of new cars with unique driver names and random plates
    """
    def __init__(self):
        self.reload_and_shuffle()

    def get_car(self):
        """
        get_car() -> Car
        yields another Car for every Car in data_file
        (default : names_list.txt)
        """
        for name in self.data:
            yield car.Car(driver=name.strip(), position=None)

    def reload_and_shuffle(self):
        """initializes and shuffles the whole generator data file
        """
        base_path = dirname(__file__)
        file_path = abspath(join(base_path, "..", "data", "names_list.txt"))
        with open(file_path, "r") as opened_file:
            self.data = opened_file.readlines()
        shuffle(self.data)
